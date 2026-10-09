---
name: user-persona
description: Interview one question at a time until a specific user persona is clear. Covers the moment, bio, goals, frustrations, and the rest, and recommends an answer on every question. Use when the user invokes /user-persona, asks to be grilled about their user, or wants a user persona before designing.
disable-model-invocation: true
---

# User persona

Interview until one specific person is clear. Do not design the screen. Do not stop while a required field is still a segment, a guess, or a blank.

## How to ask

One question per message. Wait for the answer.

On every question, recommend information:

- If the project, files, or conversation already contain the fact, look it up and recommend that. Name the source.
- If you are inferring, label it as a recommendation and say what it rests on.
- Offer a sharper version when the answer is a segment, a demographic, or a role bucket.

The user confirms or corrects it. An unconfirmed recommendation is not part of the persona.

Ask in the user's language.

## Order

Skip a question only when the user already answered it. Confirm that answer in one line, then continue.

1. **Moment.** One sentence. In Spanish it starts with "Está a punto de…". In English, "They are about to…". It names what they are about to do, what they fear, and what they must decide today.
2. **Bio.** Who this person is, specific enough to pick them out of a room.
3. **Goals.** What they want out of this moment.
4. **Frustrations.** What blocks them, what they fear, and what they have already tried.
5. **Other stuff.** Keep asking while something still fuzzy would change a design decision: where they are, how much time they have, who is with them, what device they are on, what they refuse to do, and what done looks like for them.

## Done

Stop only when all of these are true:

- The moment sentence is one person and one decision. It would become false if you swapped in a different product.
- Bio, goals, and frustrations are confirmed by the user.
- Other stuff has no open question that would change what gets designed.

Then write the persona and stop. Do not propose screens, flows, or copy.

## Persona

**Moment**

**Bio**

**Goals**

**Frustrations**

**Other stuff**

Leave a field as unknown if the user did not confirm it. Do not fill it with a recommendation they skipped.
