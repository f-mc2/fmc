# AGENTS.md — Codex guardrails for this Quarto website repo
Last updated: 2026-02-17 | Version: 1.4


## 0) Path conventions (read this first)
- `REPO_ROOT` is the directory that contains this file (the repository root): `~/accademismi/fmc`.
- Any path written like `foo/bar/` (no leading `/` or `~`) is **repo-relative** and means `REPO_ROOT/foo/bar/`.
  - Example: `docs/` means `~/accademismi/fmc/docs/`.
- Any path starting with `/` or `~` is an **absolute path** and is **outside the scope** of this repo (forbidden), except when referring to `REPO_ROOT` itself.
- Do not use `..` traversal to access anything outside `REPO_ROOT` (forbidden).
- Do not follow or write through symlinks that point outside `REPO_ROOT` (forbidden).


## Quick reference (policy matrix)
| Action | Rule | Notes |
|---|---|---|
| Edit/add/rename `*.qmd` in `courses/`, `misc/`, `presentations/`, `publications/` | Allowed | Commit per logical change |
| Fix typos in the above | Allowed | Keep edits minimal |
| Edit repo-root `*.qmd` / `*.md` | Allowed | |
| Edit repo-root `*.yml` / `*.txt` | Ask first | Use §3.1 |
| Edit infra: `auxiliaries/`, `csl/`, `css/`, `includes/`, `.gitignore`, `.nojekyll` | Allowed | |
| Edit `requirements.txt` | Ask first | |
| Edit `_quarto.yml` | Ask first | |
| Edit `AGENTS.md` | Ask first (special protocol) | §3.2 |
| Edit anything in `docs/` | Never | Generated output only |
| Run any non-git command (`quarto`, `python`, `pip`, `npm`, etc.) | Ask first | Provide exact command(s) |
| Git commands locally (except `push`) | Allowed | Includes `commit` |
| `git push` | Never | |
| Delete files | Never | See §2.4 exception for renames |

If in doubt: stop and ask, explaining what you want to do and why.


## 1) Repo context
- Quarto website deployed via GitHub Pages.
- Output directory is `docs/`.
- Primary source content:
  - `courses/`, `misc/`, `presentations/`, `publications/`
  - plus some repo-root content files.
- Infrastructure:
  - `auxiliaries/`, `csl/`, `css/`, `includes/`
  - `.gitignore`, `.nojekyll`, `requirements.txt`, `_quarto.yml`


## 2) Allowed without asking

### 2.1 Content edits
- Edit/add/rename `*.qmd` under: `courses/`, `misc/`, `presentations/`, `publications/`
- Fix typos (minimal edits) in those areas
- In repo root: edit `*.qmd` and `*.md`

### 2.2 Infrastructure edits (explicit exceptions)
- You may edit anything under: `auxiliaries/`, `csl/`, `css/`, `includes/`
- You may edit: `.gitignore`, `.nojekyll`
- Exceptions (permission-gated): `_quarto.yml`, `requirements.txt`

### 2.3 Git operations (local only)
- Allowed: `git status`, `git diff`, `git log`, `git show`, `git add`, `git commit`, `git restore`, `git reset`
- Work on `main` unless I explicitly request a branch
- Commit frequently: one commit per logical change (Conventional Commits)
- Forbidden: `git push`

### 2.4 Renames vs deletions (important)
- File **renames** are allowed only where renames are explicitly allowed above (e.g., `*.qmd` in content dirs).
- Pure **deletions** are never allowed (no `rm`, no `git rm`, no “remove unused file”).
- If a rename implies a delete+add at the git level, treat it as a rename only when it is a 1-to-1 move of an allowed filetype in an allowed directory.


## 3) Requires permission (ask first, wait for explicit OK)
Ask permission before you do any of the following:
- Run any non-git command (including `quarto render` / `quarto preview`)
- Edit `_quarto.yml`
- Edit `requirements.txt`
- In repo root: edit any `*.yml` or `*.txt`
- Edit `AGENTS.md` (special protocol in §3.2)

### 3.1 Permission request requirements (must include)
A permission request must contain:
1) Why it is needed
2) Exact command(s) OR exact file(s) to edit
3) Expected side effects (which files will change; `docs/` changes may occur only as generated output)

Good example:
"I need to run `quarto render` to verify math and crossrefs after editing `courses/XYZ.qmd`. This will regenerate files under `docs/` as build output (I will not edit them manually). May I run: `quarto render`?"

Bad example:
"Can I run some commands to fix the site?"

### 3.2 Policy file protection (`AGENTS.md`)
- This file defines the safety constraints for all AI agents in this repo.
- Treat `AGENTS.md` as read-only by default.
- You may edit `AGENTS.md` only if I explicitly request a specific change to it.
- Before editing `AGENTS.md`, you must:
  1) propose an exact diff/patch showing old → new text,
  2) explain how the change affects permissions and safety constraints,
  3) explicitly note if any Hard Stop (§4) or Forbidden action (§5) would be weakened,
  4) wait for explicit approval of that specific diff (approval of “improve AGENTS.md” is not sufficient).
- You must not weaken Hard Stops (§4) or Forbidden actions (§5) unless I explicitly instruct you to weaken that specific rule by name.


## 4) Hard stops (non-negotiable)
1. Never read, write, or modify anything outside `~/accademismi/fmc`.
   - Example forbidden: `/tmp/`, `~/Downloads/`, `../other-project/`, `~/docs/`
2. Never edit `docs/`. Treat it as generated output only.
3. Never run any non-git command unless I explicitly grant permission for the exact command(s).
4. Never install dependencies unless I explicitly grant permission.
5. Never modify `_quarto.yml` unless I explicitly grant permission.
6. Never `git push`.
7. Never delete files.

If you are unsure whether an action violates a hard stop: stop and ask.


## 5) Forbidden outright
- `git push`
- Any edits in `docs/`
- Any read/write outside `REPO_ROOT`
- Deleting files
- Any non-git commands without permission
- Editing `_quarto.yml` without permission


## 6) Standard operating procedure (default workflow)

### Before edits
1. Restate the task in one sentence.
2. Cite which rules apply (e.g., “content edit allowed”, “requires permission because `_quarto.yml`”).
3. Provide a short plan (3–6 steps) listing the files you intend to touch.
4. Proceed immediately only if the plan contains no permission-gated actions.
   - If the plan includes a permission-gated action: stop and ask first.

### While editing
- Make changes incrementally (one logical unit at a time).
- Prefer minimal edits; do not refactor unless asked.
- If you discover mid-task that you need to run a command or edit a permission-gated file: stop and ask.
- Commit frequently: one commit per logical change, Conventional Commits.

### After editing
- Provide a per-file summary (what changed, why).
- Provide a concise diff summary (high level).
- List commits created (hash and message).


## 7) Commit policy
- Work on `main` unless I explicitly request a branch.
- Conventional Commits types: `docs`, `fix`, `style`, `refactor`, `chore`
- Examples:
  - `docs(courses): add week-03 notes`
  - `fix(css): prevent mobile nav overflow`
  - `style(publications): normalize citation formatting`


## 8) If something goes wrong (damage control)
- If you suspect you violated a rule: stop immediately.
- Explain what happened, what files are affected, and the safest revert plan.
- Typical revert commands (safe to use):
  - `git restore <file>` — discard working changes to a file
  - `git reset --soft HEAD~1` — undo last commit, keep changes staged/unstaged
  - `git diff` — inspect what changed
  - `git status` — inspect repository state
- Do not attempt a silent fix.
- Never delete files as a fix — use git operations instead.


## 9) Rule conflicts (priority order)
When rules appear to conflict, resolve them in this order:
1) Hard stops in §4 and forbidden list in §5
2) Permission-gated actions in §3
3) Allowed actions in §2
4) SOP in §6

If still ambiguous: ask, using the smallest concrete question possible.


## 10) Common scenarios (quick answers)
Q: Can I create a new `.qmd` file in `courses/`?
A: Yes, immediately (§2.1).

Q: Can I update package versions in `requirements.txt`?
A: No, ask permission first (§3).

Q: I found a typo in `_quarto.yml`. Can I fix it?
A: No, ask permission first (§3).

Q: Can I run `quarto preview` to test changes?
A: No, ask permission with the exact command (§3.1).

Q: Can I commit content changes?
A: Yes, immediately (§2.3). Use Conventional Commits (§7).

Q: The rendered site in `docs/` looks wrong. Can I edit HTML there?
A: No, never edit `docs/` (§4). Fix the source `.qmd` / templates / CSS / includes instead (§2.1–§2.2).
