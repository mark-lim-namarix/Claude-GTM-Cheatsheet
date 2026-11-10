---
name: mock-drift-check
description: Compares a fake copy of an outside service (a mock) with a fresh real sample from that service, field by field, and lists what moved, disappeared or appeared.
tools: Read
version: 0.1.0
---

# Mock drift check

## The problem
Tests use a fake copy of an outside service. When the real service changes, the fake does not, so the tests stay green while the live feature is broken.

## When to use it
When a live feature misbehaves while its tests are green, and every few months for each outside service your tests fake.

## Inputs
- The fake response your tests use (paste it).
- A fresh real response from the same call, with private values removed.
- Optional: the code that reads the response.

## Steps
1. List the fields of the real response, including nested ones.
2. List the fields of the fake response.
3. Mark each field MATCH, MOVED (same data, new place, only when you confirm it is the same data; otherwise list the old field as MISSING IN FAKE and the new one as unconfirmed), MISSING IN FAKE or ONLY IN FAKE. If a field fits MOVED, label it MOVED only; do not also label its old and new locations MISSING IN FAKE or ONLY IN FAKE.
4. For a MOVED field, name the old and new location.
5. Report which code reads the old locations if the user provides it, and recommend keeping the old field as a fallback rather than deleting it.

## The check that fires
One MOVED or MISSING IN FAKE field means DRIFTED. An ONLY IN FAKE field gives DRIFTED only if you confirm the real service no longer returns it; otherwise it is reported as unconfirmed and does not count. A fake that matches on every field is labelled CURRENT only for the sample you provided. Example (synthetic):

```
Real sample fields: canvas.tabs[0].file_id, channel.name, channel.topic
Fake fields: canvas.document_id, channel.name, channel.legacy_flag
channel.name -> MATCH
channel.topic -> MISSING IN FAKE
channel.legacy_flag -> ONLY IN FAKE, unconfirmed (not in this sample; does not count toward DRIFTED)
canvas.document_id -> MOVED: old location canvas.document_id, new location canvas.tabs[0].file_id (not present in this sample at the old place)
Result: DRIFTED. Move the read to tabs[0].file_id and keep document_id as a fallback.
If every field had matched -> CURRENT, only for the sample you provided
```

## Approval route
The agent only compares and recommends. You update the fake and the code that reads it, in the same change.

## Outcome to measure
Live bugs that tests did not catch because of a stale fake. Count them per quarter.

## Credits
Method developed and used by Mark Lim, Founder at Namarix and Cheatsheet.
