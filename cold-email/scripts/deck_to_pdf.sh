#!/usr/bin/env bash
# Export a slide deck to PDF, one slide per page, at the deck's own aspect ratio.
#
#   deck_to_pdf.sh <url> <output.pdf> [slide-count]
#
# Why not `agent-browser pdf`: it ignores the page's `@page { size }`, so a 16:9
# deck comes out letterboxed on letter paper. Screenshotting each slide at the
# viewport size and stitching keeps the framing the deck was designed for.
#
# Needs: agent-browser, img2pdf.

set -euo pipefail

URL="${1:?usage: deck_to_pdf.sh <url> <output.pdf> [slide-count]}"
OUT="${2:?usage: deck_to_pdf.sh <url> <output.pdf> [slide-count]}"
COUNT="${3:-}"
SELECTOR="${DECK_SLIDE_SELECTOR:-.deck-slide}"
WIDTH="${DECK_WIDTH:-1600}"
HEIGHT="${DECK_HEIGHT:-900}"

for bin in agent-browser img2pdf; do
  command -v "$bin" >/dev/null || { echo "missing: $bin" >&2; exit 1; }
done

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

agent-browser open "$URL" >/dev/null
# Older agent-browser builds have no `viewport`; the window size is then used as-is.
agent-browser viewport "$WIDTH" "$HEIGHT" >/dev/null 2>&1 || true
agent-browser wait --load networkidle >/dev/null

# Screenshots do not trigger print styles, so the deck's own navigation UI would
# end up in a file sent to a sponsor. Hide it the same way @media print does.
CHROME="${DECK_CHROME_SELECTOR:-.deck-chrome,.deck-controls,.deck-index}"
agent-browser eval "
  var s = document.createElement('style');
  s.textContent = '${CHROME} { display: none !important; }';
  document.head.appendChild(s);
" >/dev/null 2>&1 || true

if [ -z "$COUNT" ]; then
  COUNT="$(agent-browser eval "document.querySelectorAll('${SELECTOR}').length" 2>/dev/null | tr -dc '0-9')"
fi
[ -n "$COUNT" ] && [ "$COUNT" -gt 0 ] 2>/dev/null || {
  echo "could not count slides with selector '${SELECTOR}'; pass the count as the third argument" >&2
  exit 1
}

echo "exporting ${COUNT} slides from ${URL}"
for i in $(seq 1 "$COUNT"); do
  printf -v page "%02d" "$i"
  agent-browser screenshot "${TMP}/slide-${page}.png" >/dev/null
  [ "$i" -lt "$COUNT" ] && agent-browser press ArrowRight >/dev/null
done

img2pdf --pagesize "${WIDTH}px x ${HEIGHT}px" -o "$OUT" "${TMP}"/slide-*.png 2>/dev/null \
  || img2pdf -o "$OUT" "${TMP}"/slide-*.png

echo "wrote ${OUT}"
