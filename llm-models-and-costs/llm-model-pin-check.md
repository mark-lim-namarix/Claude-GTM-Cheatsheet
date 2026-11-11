---
name: llm-model-pin-check
description: Reads your settings and code for model names and flags any that are an alias, a bare family name, or not in your provider's list, instead of an exact versioned id, including fallback entries.
tools: Read
version: 0.1.0
---

# Model pin check

## The problem
An alias such as "latest" or a bare family name keeps its text but changes meaning when a new model ships. Your setup quietly switches models, and you cannot tell why results changed.

## When to use it
Once a month, after any model release, and when results change and nobody changed the code.

## Inputs
- The settings or config files that name a model.
- The code lines that name a model (paste them).
- The list of exact model ids your provider currently offers.

## Steps
1. List every place that names a model, including fallbacks and defaults.
2. For each, check it against the exact ids list. An exact versioned id is PINNED.
3. An alias, "latest", or a bare family name is ALIAS.
4. A name that looks like an exact id but is not in the provider's list is UNKNOWN. If a name is not in the list and looks like an alias, label it ALIAS.
5. Report each ALIAS and UNKNOWN with the file and line, and the exact id it would resolve to today, only if your provider's list states it.
6. One ALIAS or UNKNOWN anywhere means the result is NOT PINNED; otherwise PINNED.

## The check that fires
One ALIAS or UNKNOWN anywhere, including a fallback, means NOT PINNED. Example (synthetic):

```
settings: model = "model-x" -> ALIAS (resolves to a different model after each release)
settings: fallback = "model-x-4-8" -> PINNED
script.js line 12: "model-latest" -> ALIAS
README example: "model-x-4-9" -> UNKNOWN (looks like an exact id, not in the provider's list)
Result: NOT PINNED, 3 places to fix
```

## Approval route
The agent only reports. You change the names, and you make a model change on purpose, not by an alias.

## Outcome to measure
Unexpected result changes traced to a model switch. The target is zero.

## Credits
Method developed and used by Mark Lim, Founder at Namarix and Cheatsheet.
