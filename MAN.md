# softlendar — Vocabulary Man

This is the active MAN vocabulary for the softlendar landing page.
Kep this man handy so you don't forget!

## Shorthand Reference

| Shorthand | Full Word     |
| --------- | ------------- |
| plese     | please        |
| valid     | validate      |
| mak       | make          |
| erl       | early         |
| brose     | browse        |
| voce      | voice         |
| static    | fun / victory |
| kep       | keep          |
| man       | manual        |
| ed        | edit          |
| msg       | message       |
| col       | column        |
| nw        | now           |
| se        | see           |
| loc       | location      |
| sv        | save          |
| late      | lately        |
| wwt       | wait          |
| sm        | some          |
| latr      | later         |
| evr       | ever          |
| lang      | language      |
| mem       | memory        |
| ne        | new           |

## Notes

- Use these shorthands when writing comments, docs, and msgs.
- If you're erl in the project and need to brose the code, this man will help you valid things.
- Kep it updated if new shorthands are added — it's a static reference!
- Nw you can se the loc of any file using these shorthands.
- Wwt no more — sv this man and ed it anytime!
- Sm shorthands save sm time!
### Total: 21 Shorthands
---
## technic
***overview** = take a look at every file related to current project*
***redo** = cut/rm current project and rebuild it*
## Developing works
***feedyday** = user comment, complain, feedback;*
***logoday** = logo updating*
## Shorthand Rules
- *shh = shorthand*
- **any 4 letter word that has consonant at 1st and 3rd letter and vowel in 2nd and at last an e** — cut e = shh
- **any word that has two vowels in the middle** — cut one vowel from those 2 = shh
- **any word that has two consonants in the 3rd and 4th places and one vowel in the 2nd place and another consonant at the 1st place** — cut vowel = shh
- use **data/import lng**

## Project Rules
- ***alwasys plan before act***
- **"scc" = stage & generate a short commit msg & update commit logs** — when user says "scc", run git add and stage all modified files then generate a commit message (do NOT commit)
- **in any chats if said listen then listen until said do it** — if user say listen then do not get on it until user say do it or mak it
- **when said committed** — know that it is committed
- **when said deployed** — know that it's live and run: fetch softlendar.com
- **when said data listen** — listen for detail
---
## Commit Log

### var:0 — initial commit

- index.html — login modal added, keyboard shortcut button added
- ct.js — Login() updated to use modal instead of prompt(), welcome h1 shows username
- ct.css — login overlay, box, inputs, button, error styles added
- keymap-ct.js — keyboard shortcuts (T, V, 1-4, H, W, N, ?)
- sound-ct.js — playSound() using Web Speech API with voice loading fix
- bootin-ct.js — showAlert1(), showAlert2() keymap help
- act-ct.js — imageUrls object, changeImage()
- deploy.md — deployment platform reference created
- man.md — vocabulary shorthand reference created

### var:1 — power command system

- power-ct.js — time-travel command system created (commit save, commit log, commit now, change code to date=, change code to var=)
- index.html — added power-ct.js script link, command input box with run button
- ct.css — power command box styles (black background, green terminal text, lawngreen borders)

### var:2 — termirator landing update

- index.html — future project links removed; marquee labels removed (logos only); nav bar added with smooth-scroll anchors; termirator_logo.svg, nametermer_logo.svg, haster_logo.svg, setomoly_logo.svg, brose_logo.svg, serch_logo.svg added to marquee; terminal section added with 3 contexts (softlender/cyberdyne/termitoria); tab autocomplete; termirator added alongside catlearning.fyi; contact form added with email backend; favicon replaced with softlendar_logo.svg
- landing.css — terminal styles added (dark card, prompt, output, input, scrollbar); badge categories organized; badge-float animation added; contact form styles added (gradient bg, frosted card, animated button with loader); nav bar styles added
- main.py — Flask backend with /, /contact (POST), /api/projects, /api/health, and dynamic project detail routes (/softlendar, /catlearning, /termirator, /brose, /serch, /nametermer, /haster, /setomoly, /redarbot, /dobart, /bylothon)
- project.html — project detail page template with logo, tagline, description, stack, status, and visit button
- 404.html — dark theme 404 page with back link
- .env.example + requirements.txt — email config and Python dependencies
- man.md — commit log updated
- termirator_logo.svg — hex frame T-prompt with blink cursor
- nametermer_logo.svg — wifi mark with orange N
- haster_logo.svg — hex frame H with lightning crossbar and speed dot
- setomoly_logo.svg — atom orbit with nucleus dots and spinning electron
- brose_logo.svg — browser window with globe and traffic dots
- serch_logo.svg — magnifying lens with sparkle dots and scan line
- softlendar_logo.svg — sun with rays, glow ring, S-curve, sparkle dots

### var:3 — back link styling and routing

- landing.css — `.intertype-back` styled as gradient pill button with shadow and hover lift effect
- intertype.css — `.it-back` styled as gradient pill button using CSS vars with shadow and hover lift effect
- project.html — `.back-link` styled as gradient pill button with shadow and hover lift effect
- 404.html — `.back-home` hover updated to match lift effect
- intertype.js — `goBack()` changed from `window.history.back()` to `window.location.href = "/"` to avoid returning to /interType/
- index.html — `.intertype-back` changed from `<div>` to `<a href="/">` so it navigates to root

### var:4 — interType chat polish + alarm widget

- intertype.js — rotating greeting and help responses added (GREETING_RESPONSES + GREETING_RESPONSES arrays with index rotation); `isHelp()` detection added; typing dots delay logic updated (3s for greetings, 5s for help)
- index.html — alarm widget added: ⏰ fixed button, pulsing fullscreen ring overlay with "Alarm rang!" message, Web Audio API do-re-mi melody (10 notes), auto-dismiss after 3s; settings panel dark-mode toggle and theme persistence added
- landing.css — alarm widget styles added (.alarm-btn, .alarm-ring, .alarm-ring-inner, alarmPulse keyframes); settings-panel dark overrides refined
- MAN.md — "alwasys plan before act" rule added

### var:5 — README polish

- README.md — fixed live demo link label (`soflendar` → `softlendar`); removed italics from "engine" and "assistant" for consistent bold emphasis; cleaned grammar ("theres" → "there's", added "on top-right" detail)

### var:6 — interType profile system + technoly keyword + homepage greeting

- intertype.js — profile localStorage helpers (`getUserName`, `getUserLogo`, `updateProfilePreview`, `loadProfile`, `saveProfile`); `TECHNOL` keyword regex + `isTechnoly()`; user message bubble refactored to avatar + username + message wrap; profile modal wired to open/close
- intertype.html — `👤` profile button in header, profile sidebar item, profile modal with logo preview, username input, file upload, save button
- intertype.css — profile modal styles (`.it-profile-wrap`, `.it-profile-row`, `.it-profile-preview`, `.it-profile-save`); user message avatar layout (`.it-msg-user-wrap`, `.it-msg-user-avatar`, `.it-msg-user-col`, `.it-msg-user-name`); profile button responsive hide
- index.html — hero greeting `<p class="hero-greeting">` added below `.hero-sub`; inline script reads `intertype-user` from localStorage and displays "Welcome {username}!"
- landing.css — `.settings-btn` position changed from `right: 16px` to `left: 16px`

### var:7 — stop button interrupts in-flight responses

- intertype.js — `generating` flag + `activeCard` reference added to `send()`; stop click sets `generating = false`, removes the active dots card, and bails out of pending `wait()` / `fetch()` replies; `finally` block resets state after success or error

### var:8 — profile modal synced across homepage + interType

- index.html — profile modal (`pf-modal`) added with avatar preview, username input, logo file upload, Save button; `👤` nav icon wired to `open()` the modal; JS shares same localStorage keys (`intertype-user`, `intertype-logo`) as interType so profile data is synced
- landing.css — `.pf-*` modal styles added (dark card, orange/pink accent, backdrop blur, input focus glow, save button hover lift)
- intertype.html — `👤` icon changed back to `<a href="/">` with `text-decoration: none`; profile modal still reachable via sidebar menu
- intertype.js — `profileBtn` click listener restored with `preventDefault()` so header icon opens modal instead of navigating; `loadProfile()` + `openModal("profile")` flow preserved
- intertype.css — `.it-profile` group restored to `text-decoration: none` for the anchor tag

### var:9 — logo folder cleanup

- created `logo/` directory; moved all `*_logo.svg` files into it
- updated references in `index.html`, `intertype.html`, `project.html`, `add_nav.py`

### var:10-fix — stricter email validation on contact form

- main.py — `POST /api/contact` returns `"wrong/unexisting email"` for bad emails (missing @, missing dot, too short)
- index.html — frontend parses backend error JSON and displays exact message to user

### var:10 — contact form + PostgreSQL data store

- index.html — contact card (`user-contact-email-input`, `user-contact-msg-input`, `contact-sv-btn`) added with email + message fields; JS posts to `/api/contact`
- landing.css — `.contact-form`, `.contact-input`, `.contact-textarea`, `.contact-feedback` styles (ok/err colors)
- main.py — `UserMsg` class with `.save()` and `.all()` using PostgreSQL via `psycopg`; `POST /api/contact` stores messages; `GET /api/messages` returns all
- requirements.txt — added `psycopg==3.1.18`
- `init_db()` auto-creates `user_messages` table on startup

### var:11 — project reorganization + owner logo

- reorganized project: moved web assets (`index.html`, `landing.css`, `intertype.html`, `intertype.css`, `intertype.js`, `project.html`, `404.html`) into `files/` directory
- moved utility scripts (`add_nav.py`, `add_volume.py`, `css_all.py`, `ed_all.py`, `fix_volume.py`, `fix_volume_html.py`, `volume_css.py`, `volume_inside.py`) into `script/` directory
- moved `.env.example` and `package-lock.json` into `files/` directory
- moved `volume_fix.css` and `volume_margin.css` into `files/` directory
- added `logo/owner.svg` — personal logo (InD with 3 stars on light green background)
- updated `main.py` file paths and imports to match new directory structure

### var:11-deploy — deploy readiness fixes

- `main.py` — added `time` import; fixed `is_real_email()` to use regex + MX record lookup (dnspython) with graceful fallback; added `_rate_limit` in-memory store + rate limiting (60s per email) on `/api/contact/send-code`; added `/logo/<path:filename>` route to serve root `logo/` directory; fixed `/` prefix on project detail CSS/logo paths
- `files/project.html` — changed relative paths (`landing.css`, `logo/...`) to absolute paths (`/landing.css`, `/logo/...`) so they resolve correctly on project detail pages
- `requirements.txt` — added `dnspython==2.6.1` for MX record email validation
- compiled `main.py` successfully with `python3 -m py_compile`
