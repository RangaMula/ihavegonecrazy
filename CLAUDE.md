# ihavegonecrazy

## Saving work (owner's standing instruction)

- **Cloud session** (`CLAUDE_CODE_REMOTE=true`: Claude Code on the web, mobile or a scheduled task): follow
  `.claude/agents/work-saver-cloud.md`.
  - Deliverables, session log and raw transcript go to Google Drive `Claude Workspace Backup/<Project>/` through the
    Google Drive connector.
  - Commit and push to the session's branch, and verify that the remote sha equals the local sha.
  - Create `_cloud-sync/PENDING … <Project>.md`. The nightly laptop sync (~7:42 pm Asia/Dhaka) then copies the work into
    `E:\Claude Workspace`.
  - Say "Cloud work-saver armed…" at session start, and report each layer without being asked.
- **On the laptop** (Claude Code / Cowork): follow `E:\Claude Workspace\agents\work-saver.md`
  (E: primary → GitHub → Drive mirror) and `E:\Claude Workspace\CLAUDE.md`.

Projects in this repo: `muwatta/` (al-Muwaṭṭaʾ bilingual editions; see `muwatta/README.md`).
