# Session log — 22 Nov 2026 — cloud work-saver protocol + first Drive save

- **Surface:** cloud (Claude Code, remote session `cse_01Y81j2DjP6dim7wYJkFPNSF`).
- **Repo:** RangaMula/ihavegonecrazy, branch `claude/muatta-multilingual-translations-40bpf7`.
- Continues `2026-11-21_muwatta-multilingual-and-publishing.md`.

## Requests (the owner's wording)

1. "Why the cloud session unable to reach my google drive?"
2. "Make a protocol for cloud sessions exclusively to save the files in google drive and github as per the original saving
   protocol. It will also try once in a day, preferably 8 pm to sync the files to laptop. Cloud session doesn't need to be
   able to save things in laptops G drive. If it saves in google drive, G drive will be synced anyway."

## Findings

- The cloud session **can** reach Google Drive, through the Google Drive connector. It cannot reach the laptop's drive
  letters (E:, the Drive mount), because the container is a different machine. The earlier statement in this session was
  imprecise and was corrected.
- The current original protocol (`agents/work-saver.md`, updated 23 Jul 2026) is:
  1. `E:\Claude Workspace` primary;
  2. GitHub (Rabbit-s-Hat);
  3. Drive "Claude Workspace Backup" mirror.

  The copy pasted into the claude.ai personal preferences is OLDER: it still says `G:\My Drive\Claude Workspace` +
  `E:\Claude Backup`.
- The owner's calendars are on Asia/Dhaka.
- No laptop folders are currently shared through Remote Control (`list_computer_folders` is empty).
- The Drive connector's `update_file` changes metadata only and cannot replace content. So re-saving means: upload the new
  file, then trash the old one. The sync queue is one file per save, closed by renaming it.
- The scheduled-task API on this account cannot attach connectors. The nightly session therefore works through the laptop's
  own Drive mount once it is attached.

## Decisions

- **Cloud protocol** = `work-saver-cloud.md`:
  - **L1:** deliverables + session log + raw transcript → Drive `Claude Workspace Backup/<Project>/`;
  - **L2:** GitHub push, verified by sha;
  - **queue:** `_cloud-sync/PENDING <stamp> <Project>.md`;
  - **L3:** dashboard via ArtifactData, with the local rebuild queued.
  - It applies only when `CLAUDE_CODE_REMOTE=true`.
- **Nightly laptop sync**, scheduled task `trig_013aK3eQQjDExYsTkYU6JCmg`:
  - daily at **19:42 Asia/Dhaka**: 8 pm moved slightly earlier, because runs set on the hour can be delayed by server traffic;
  - steps: attach the laptop folder `E:\Claude Workspace` → robocopy from the Drive mount `/E /XO` → git fetch or clone
    into `C:\dev` (never checkout or merge) → dashboard rebuild → rename `PENDING` to `SYNCED`;
  - if the laptop is unreachable it changes nothing and retries the next day.

## Installed

| Where | What |
|---|---|
| Drive `Claude Workspace Backup/agents/work-saver-cloud.md` | the full protocol (current version 12,641 B; the first version is in Drive Trash) |
| Drive `Claude Workspace Backup/_cloud-sync/` | the queue folder (ID `10xq4rAtRWm4XcIzyLVz9KkNMhFUUz5jf`) |
| Repo `.claude/agents/work-saver-cloud.md` + root `CLAUDE.md` | repo copy; cloud sessions of this repo load the pointer |
| Environment "ihavegonecrazy (venture-lab.ai)" | setup script writes `/root/.claude/CLAUDE.md` (protocol pointer) into every new cloud session; approved by the owner; unproven until a fresh session starts |
| Scheduled task "Nightly laptop sync" | first run 22 Nov 2026, 19:42 Dhaka |

## Owner actions still needed

1. **Share the laptop folder:** Claude desktop app → Settings → Claude Code → Remote Control → add `E:\Claude Workspace`.
   Keep the app running in the evening, and approve the attach request when it appears.
2. **Paste the updated claude.ai personal-preferences snippet** (given in chat), so cloud sessions in *other* environments
   (Default, Amazon Vasabid Initiative) also use the cloud protocol. Their setup scripts cannot be edited from here.
3. Optional: add the Google Drive connector to the scheduled task in claude.ai → routines, so it can check the queue before
   it asks to attach.

## Muwatta follow-up flagged

The workspace `CLAUDE.md` "Islamic source authentication protocol" says: never use AI-generated translations; every
deliverable needs a `.sources.md` report. The Muwatta editions are AI translations made at the owner's explicit request,
and they still lack a `.sources.md`. The Arabic itself was fetched from sunnah.com data and cross-checked against
hadith-api, and grades carry their grader (Salim al-Hilali). Offered: a `.sources.md` per edition, with the scholar review
as the gate.
