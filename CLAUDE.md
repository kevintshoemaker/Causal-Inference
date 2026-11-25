# CLAUDE.md

Guidance for Claude (and other contributors) working in this repository.

## What this project is

Course materials for **NRES 701A: Causal Inference and Analysis**, a 2-credit, letter-graded graduate
course at the University of Nevada, Reno, first offered **Spring 2027**. Todd set the course up in
Curriculog and is pushing the official name change there.

- **Instructors:** Kevin Shoemaker and Todd Steury (Dept. of Natural Resources & Environmental Science).
  An NRES course only, with no cross-listing.
- **Format:** an instructor-led class, not a student-led seminar. Each weekly meeting (one per week)
  opens with a **20–25 minute lecture/discussion by Kevin or Todd**, followed by discussion of the
  readings (students help lead) and a hands-on in-class exercise. Kevin and Todd hold all
  organizational and leadership responsibilities.
- **Connor Ball** (UNR Anthropology PhD student) drafted syllabus v1 but is **simply a student
  participant**. He has no organizer, instructor or grading role. Don't list him as an organizer or
  instructor in course materials.
- **Audience:** graduate students from NRES, Anthropology, EECB and other programs. One regression-level
  statistics course is recommended but **not enforced**; assume no prior causal inference, philosophy or R.
- **Grading scale:** the UNR Graduate School requires C or better for graduate credit, so the scale's
  lowest passing grade is C (73); below that is F. No C− or D grades.
- **Final project:** individual. Each student builds a well-reasoned causal DAG of their own study system
  to support their thesis research: initial DAG around Week 5, revised through the semester, with a final
  presentation and write-up.

The repo has two jobs:

1. Working space for course documents (reading lists, assignments, planning notes). The syllabus
   itself lives in a Claude Doc, not in the repo (see below).
2. Source for the **public course website on GitHub Pages**:
   https://kevintshoemaker.github.io/Causal-Inference/ (repo:
   `https://github.com/kevintshoemaker/Causal-Inference`, public).

## Current state (as of 2026-11-25)

- **The syllabus lives in one place: the Claude Doc (Draft v5)**
  https://claude.ai/artifact/QaQxtB6SDMe67wzjiWVZfG. The only other current copy is the PDF exported
  from it, `syllabus/NRES701A_Syllabus_v5_DRAFT.pdf` (the one to email; the website serves a copy as
  `docs/Syllabus.pdf`). Everything else (v1, v2 Markdown/Word and its build script, Connor's v3, the
  v4 PDF, the v5 Word export) was moved to `syllabus/archive/` on 2026-11-23 at Kevin's request: too
  many versions were in play. Don't create new Word/Markdown copies of the syllabus in the repo; if
  Todd needs Word, export a one-off from the doc and merge his changes back into the doc. Connor's v1
  and v3 drafts in the archive are git-ignored (local only). Connor's v3 was built from v1, not v2, so
  diff v3 against v1 to see his real edits. The older v2 Claude Doc
  (https://claude.ai/artifact/FfbPf9nXA92B1aZifMCVPq) still exists but is superseded; don't edit it.
- **Any syllabus change is a three-step job:** edit the Claude Doc, re-export the PDF, and refresh
  the website (see Build), then commit and push. The doc, the PDF and the website home/schedule
  pages must always say the same thing.
- The syllabus and the website link to each other: the doc's contact block has a "Course website"
  line, and the website home page has a "Syllabus (PDF)" line (added by `build_site.py`) plus the
  Schedule → "Syllabus (PDF)" menu entry. The website links to the PDF, never to the Claude Doc
  (the doc is private).
- Syllabus layout follows Kevin's NRES 470 syllabus (`syllabus/Syllabus_NRES_470.pdf`): a "Welcome to
  NRES 701A" title with a subtitle line, labeled contact lines (no table and no author byline), a
  meeting-time section, then bullet-list Prerequisites, Texts and Software, and "SLO 1." outcomes. The
  grading components are a % list, followed by a one-line grading scale.
- Contact lines list offices (Kevin: Fleischmann Agriculture 220e; Todd: Fleischmann Agriculture 217)
  and email, marked "(preferred contact)". Phone numbers were removed on purpose (2026-11-24); don't
  add them back. Todd prefers to edit in Word.
- UNR syllabus boilerplate comes verbatim from the Provost's **Fall 2026 syllabus template**, saved
  at `syllabus/syllabus-template-fall-2026.docx` (download requires a UNR NetID). Its University
  Policies statements: Academic Standards (UAM 6,502); Student Compliance with University Policies;
  Disability Services (seated-classroom version + third-party content sentence); Audio and Video
  Recording (student- and instructor-created); Maintaining a Safe Learning and Work Environment
  (Center for Civil Rights & Equal Access); Campus Closures or Delays; Academic Success Services;
  Mental Health Support; Veteran. The appendix has three sample AI statements; the course uses the "allowed for certain purposes
  and/or assignments" version, so each assignment's instructions must say which AI uses are allowed. Never paraphrase these
  or reuse v1's older text; when a newer template is released, update from it.
- `planning/` holds internal planning material (meeting agenda PDF, citation-check notes, email
  drafts). It is git-ignored and stays local.
- **What is public:** the repo is public and pushed to `main`. Tracked: `CLAUDE.md` (Kevin chose to
  track it on 2026-11-25, so everything written here is public), `docs/`, `build_site.py`,
  `.gitignore`, the root `index.html`/`.nojekyll`, and `syllabus/` (current PDF, NRES 470 layout
  reference, UNR template, and the archive minus Connor's drafts). Local only: `planning/`,
  `.claude/` and Connor's v1/v3 drafts. Never `git add -A` here; add paths by name.
- MyNevada listing (2026-11-23): NRES 701A section 1003, class number 30643, 2 units, in person,
  letter grade, capacity 15 (waitlist 999; easy to raise, so don't advertise the cap), 1/19/2027–5/4/2027, days/times and room TBA. It still shows
  the old title "Advanced Resource Management" (topic "Stat & Data Analysis for Ecol", description
  "Forest/range management") and lists only Kevin as instructor. The name change is in progress, but
  no one knows when it will show; student-facing messages should say to enroll anyway.
- Meeting time (confirmed 2026-11-25): **Tuesdays 1:30 to 3:30 PM**; room still TBD.
  Office hours are by appointment. Still open: the room and whether enrollment
  needs instructor/department permission.
- Schedule dates (from UNR's Spring 2027 academic calendar, unr.edu/admissions/records/academic-calendar):
  15 Tuesday meetings, Week 1 = Jan 19 through Week 15 = May 4 (final presentations). No class
  Mar 23 (spring break, Mar 20–28); the doc's schedule table has a spring-break row between Weeks 9
  and 10. Prep day May 5; finals week May 6–12 (the final write-up is due then).
- **Announcement email:** `planning/2026-11-23_email_drafts.md` holds Kevin's short version (he
  prefers it bare-bones; don't pad it), updated 2026-11-25 with the confirmed time, a MyNevada
  old-name note and the draft website link. It also holds the earlier note to Todd and Connor (sent;
  asked for feedback and their GitHub usernames). Kevin sends email himself from Outlook. Connor and
  Todd will help spread the word.
- **Website (live since 2026-11-23):** https://kevintshoemaker.github.io/Causal-Inference/. An
  R Markdown site in `docs/`, modeled at Kevin's request on his NRES 746 and NRES 470 sites (flatly
  theme, `_site.yml` navbar), not Quarto. Structure:
  - **Home** (`index.Rmd`): the syllabus, minus the schedule table and reading list, with a floating
    table of contents and a pointer to the Schedule page.
  - **Schedule** dropdown: "Course Schedule" (`schedule.Rmd`: the weekly table, readings by week and
    suggested readings) and "Syllabus (PDF)" (`Syllabus.pdf`).
  - **Lectures** dropdown: Weeks 1–13 by topic, each pointing at a placeholder section of
    `docs/lectures.Rmd` (`lectures.html#weekN`). Give each week its own page as notes are written and
    update `docs/_site.yml`. If week titles change in the syllabus, update `lectures.Rmd` and
    `_site.yml` by hand to match.
  - **Links** (`Links.Rmd`): dagitty, R/RStudio, free books, Laura Dee's reading list, Stats Chats.
- **Hosting:** GitHub Pages serves `main` → `/docs` (Kevin set this on 2026-11-23; verified). The
  site lives in `docs/`, not the repo root as in NRES 746, so that internal files at the root are
  never rendered or served. The root `index.html` (a redirect to `docs/`) and root `.nojekyll` are
  leftovers from when Pages briefly served the root; they are unused and harmless. Publishing is just
  commit + push to `main`; Pages redeploys in about a minute. So far Kevin has had site updates he
  asked for pushed straight to `main`. The `gh` CLI is not installed; check the live site with
  `curl` or the browser instead.

## Build

Build the website with:

```
python build_site.py
```

Run it with no argument to re-render the site from the existing pages. To refresh the syllabus
pages after the Claude Doc changes: export the doc as PDF over `syllabus/NRES701A_Syllabus_v5_DRAFT.pdf`,
export it as Word or Markdown to a temporary location (not the repo), and run
`python build_site.py <path-to-export>`. That regenerates `docs/index.Rmd` and `docs/schedule.Rmd`,
copies the PDF to `docs/Syllabus.pdf`, and runs `rmarkdown::render_site("docs")`.

- `docs/index.Rmd` and `docs/schedule.Rmd` are generated; don't hand-edit them. The one shortcut
  used so far: when the doc change is a line or two and no export can be saved to disk, make the
  identical text change in the `.Rmd` and re-render, so the page still matches the doc exactly.
- `docs/lectures.Rmd`, `docs/Links.Rmd`, `docs/_site.yml` and `docs/styles.css` are hand-edited.
- The rendered `.html` and `site_libs/` are committed (Pages serves them as-is; `docs/.nojekyll`
  turns Jekyll off).
- The script splits the syllabus at its `## Course schedule` and `## Readings by week` headings, so
  those two headings must keep their names in the doc. It also drops the title and subtitle line
  (they go in the page header), turns escaped square brackets into plain ones (R Markdown would
  render `\[...\]` as display math), and sets the schedule table's column widths through the dash
  counts in its separator row.
- Tools: R 4.5.1 at `C:\Program Files\R\R-4.5.1` with rmarkdown; the script points rmarkdown at
  RStudio's bundled pandoc 3.x because the pandoc on PATH is 1.17 (too old). Both paths are constants
  at the top of the script.
- Getting exports out of the Claude Doc: a docs-connector PDF export is large enough that the harness
  saves the result to a file (decode its `bytes_b64` with Python). Smaller Word/Markdown exports come
  back inline as base64 and can't be written to disk reliably; ask Kevin to use the doc's Export
  menu, or use the shortcut above.
- Preview locally with the `course-site` launch config (`.claude/launch.json`, port 8701), and check
  the pages in the browser before pushing.

## Course design principles

- **Light reading load:** at most 2 required readings a week, usually one framing piece and one
  applied paper. Only 4 *Book of Why* chapters are required (Intro, Ch. 1, 4, 7).
- **Emphasize reading and critiquing applied papers,** with ecology/conservation examples alongside
  anthropology/archaeology ones.
- **"Causal claims in the wild" critique:** students find a paper that makes causal claims *without*
  formal causal methods and evaluate whether the claims hold up.
- **Weekly hands-on exercise:** problems solvable with pencil and paper; R is an optional extension.
- The complexity, feedback and systems material (diversity–stability debate; M. Salmon 1978) is kept
  as two late-semester weeks. Connor dropped Flannery 1968 from Week 12 in v5 (2026-11-23) as a weak reading;
  v5 also dropped "archaeology/archaeologists" from the course description. Kevin kept both edits.

## Ideas to revisit (Connor's instructor notes from v3, 2026-11-23)

Kept here, not in student-facing materials. Connor never saw v2 before writing v3, so his v3 changes
reflect v1's structure.

- Reading lists he drew on: Laura Dee's Ecology Causal Inference readings
  (https://lauradee.github.io/EcologyCausalInference/readings.html) and a causal-AI course syllabus
  (https://www.causalai.net/cs4775_syllabus22f.pdf).
- Short (10-min) student presentations on papers they find that make implicit causal claims.
  Adopted in v4 as pair presentations for the "claims in the wild" critique.
- Core Book of Why chapters: Intro, Ch. 1 (ladder of causation), Ch. 4 (confounding), Ch. 7
  (do-calculus). Adopted.
- Best readings for building complex DAGs: Bulbulia 2024 Parts 1 and 2; Laubach et al. 2021 is also good.
- "Testing assumptions?" — a session on testing a DAG's assumptions against data.
- One class day on testing for and addressing missing or impossible-to-measure confounders.
- Fisher on smoking and lung cancer (found: Fisher 1958, "Lung cancer and cigarettes?", Nature
  182: 108; follow-up letter Nature 182: 596). Now in Week 4 (confounding and the smoking debate).
- Review DAGs and explain them in small groups.
- "Correctness" exercise: rerun the adjustment sets in the Arif & MacNeil paper. Adopted as a Week 4
  exercise.
- A written DAG review assignment.
- Student involvement is key: discussion of ideas, examples, and reviewing each other's work.
- Connor's early-weeks sequence (v3 Weeks 2–8): adopted on 2026-11-23 as a hybrid with v4's design
  weeks: 2 What is a cause (Woodward, Cheng 1997); 3 Causal models and graphs (Arif & MacNeil 2022,
  Bulbulia Pt 1); 4 Confounding and the smoking debate (BoW Ch. 4, Arif & MacNeil 2023, Fisher 1958);
  5 Back-door criterion and do-operator (BoW Ch. 7, McElreath Ch. 6; initial DAG due); 6 Two frameworks
  and mediation (Hernán 2019, Bulbulia Pt 2); 7 Experiments and quasi-experiments (Arif & Massey 2023,
  Butsic 2017); 8 Unmeasured confounders (Byrnes & Dee 2025 + Watson 2025 or Cardillo & Carranza 2025).
  Cut from required, still available: Glymour 2003, Holland 1986, W. Salmon 1982, Kimmel 2021,
  Laubach 2021, Dee et al. 2023, Ferraro 2009, Ferraro & Hanauer 2014.
- Still open: Connor's late weeks (v3 Weeks 11–14: networks week, Bateson, May, Tainter, Johansson);
  see the comment thread in the syllabus doc.

## Conventions

- **Never commit copyrighted readings (PDFs) to this public repo.** They go on WebCampus. The website
  lists citations and links (DOIs, open-access versions) only.
- Anything under the website source is public. Keep student information, grades and internal planning
  notes out of published pages.
- Treat citations as unverified until someone has checked the DOI or journal page; see
  `planning/syllabus_v2_citation_notes.md` for what has and hasn't been checked.
- Write for a mixed audience (ecologists, anthropologists, archaeologists): define jargon, use plain
  language.
- Prefer Markdown/Quarto (`.md`/`.qmd`) over `.docx` as the source of new materials other than the
  syllabus (which lives in the Claude Doc), so changes show in git diffs.
