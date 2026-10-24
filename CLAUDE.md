# ttnganhuyen.com — Margot's personal website

Personal site of Trần Thị Ngân Huyền (Huyen Tran / Margot), closely modelled on untold.site/en.
Tagline: "consulting by day, blooming by night".

## Owner rules (always follow)

- Margot writes in Vietnamese; reply to her in Vietnamese.
- Commit straight to `main`. Do not create new branches and do not delete other files in the repo.
- Cloudflare Pages deploys `main` automatically; there is no build step.
- Never print the contact email anywhere in the page or in messages. The form sends via Web3Forms, and the visitor only sees "Submitted".
- Never change the wording of her blog posts (`#/stories/...`).
- Keep `<meta charset="utf-8">` in `index.html`. `_headers` also forces UTF-8; without it, Vietnamese turns into mojibake.
- English name is **Margot** (never "Hailey").

## Files

| Path | What it is |
| --- | --- |
| `index.html` | The whole site: one file with inline CSS and JS, and base64 images (~1.2 MB) |
| `_headers` | Cloudflare header rules (UTF-8) |
| `favicon.ico`, `apple-touch-icon.png` | Flower-in-coupe-glass drawing, white lines on blue `#8FACD8` |
| `img/chuyen-ke.jpg` | Cover photo of the blog post "Chuyện kể" |
| `img/flower-*.png` | Source doodles for the hero flower |

## Design system

- Background: pure white. Accent blue: `#8FACD8`. The CSS var is still named `--orange` for historical reasons. Small accent text uses `--accent-ink` `#4d6f9f`.
- Spacing is like untold: wide gutters, compact sections, and mostly headlines on scroll.
- Thin faint rules sit exactly on text baselines; they are computed in JS (`layoutHero`, `baselineRules`). Annotation text is never crossed by a rule.
- Buttons (`.btn`) are compact. **Every CTA label ends with "!"** in both EN and VI.
- Carets (`|`) never blink. They only show while text is typing, then stop.
- EN/VI toggle: English is in the markup, and Vietnamese is in a `data-vi` attribute on the same element (`setLang`).
- Mobile (≤720px) must fit the screen width with no sideways scroll.

## Routes (hash router, `route()`)

Each route maps to a `<div class="view" id="v-…">`. Nav and menu order: **about, work, consulting, blog, contact**.

| Hash | View | Content |
| --- | --- | --- |
| `#/` | `v-home` | About page (home); see below |
| `#/work` | `v-work` | Text-only list of roles from the `WORK` array (no photos, no logos yet; outputs will be added later) |
| `#/work/<id>` | `v-case` | Case page filled by `fillCase(id)` from `WORK` (mark, years, role, paragraphs `p`, capabilities `caps`, placeholder `slides`) |
| `#/consulting` | `v-consulting` | "use cases coming soon": 01 Strategy, 02 Data, 03 Process |
| `#/stories` | `v-stories` | Blog index ("coming soon", Follow me on Instagram) |
| `#/stories/<id>` | `v-post` | Blog posts, e.g. `post-chuyen-ke` (Vietnamese, 24.10.2026) |
| contact | `#talk` dialog | Contact / "advice" form (`.talk-open` buttons, `data-mode="contact"`/`"advice"`) |

## Home page (`v-home`), top to bottom

1. **Loader**: her signature "h" drawn on a blue background.
2. **Header**: "Huyen Tran / Margot" at the top left with a caret, a nav whose labels collapse to their first letter, the EN/VI toggle, and a hamburger that opens a full blue menu.
3. **Hero** `#hero`: the headline "consulting ( card stack ) by day & blooming ( stack ) by ( stack ) night |".
   - **Photo card** `.shot` with nine `.slide.scN` cards. Each card shows a spinning `*`, an organisation, a role and years:
     - sc2 HUST · Business Analytics
     - sc6 TEDxBachkhoa · Communications
     - sc5 SoICT Innovation Club · Public Relations
     - sc7 Young Leaders Network · National Project Manager
     - sc4 Maritime Bank · Data Administration
     - sc1 Base.vn · Business Analyst
     - sc3 FPT Telecom International · Account Manager
     - sc8 Hasselt University · Entrepreneurial Governance
     - sc9 De Orangerie · Barback
   - The cards auto-rotate every 2.2s. A click or tap jumps to the next card with a quick fade and restarts the timer.
   - **Stacks** (Flowers / Bartender / Sketching): fan out on hover, or toggle on tap on touch screens.
   - **Coupe glass** `.sun`: a flower rising from a cocktail glass, drawn stroke by stroke, with a moon/sun swap behind the flower head.
   - **Poem** (*): her grandfather's poem, caption "My grandfather, Nghệ An, 07/01/2006".
   - **CTA**: "Grab a drink with me!".
4. **About** `#about`: "four names, one person". A carousel (`replaySpec`, `typeMargot`, swipe) of type specimens:
   - Ngân Huyền (Danh, from her grandfather; caption "The Cosmic Origin of Carbonado")
   - Pie At Ounl (Tự, from "Enigma")
   - Margot Tran (Hiệu)
   - Each swipe replays the animation.
5. **Where I've lived** `#t-work`: Nghệ An → Hà Nội → Thành phố Hồ Chí Minh → Hasselt, with flags, and a "Give me some advice!" CTA.
6. **Where I've worked** `#t-projects`: a draggable book shelf in time order (`fitBooks` fits the spine text). "Every step has a story" links to `#/work`.
7. **The circles of my life** `#t-community`: six circles: Business, Flowers, Nature, Cocktails, Technology, Sketching. The four craft circles use her blue-duotone photos. CTA "Let's connect!".
8. **My untold stories** `#t-stories`: three sticky notes (4 names / 4 loves / 4 cities).
   - A click spreads them sideways, then they settle back in place.
   - The "Click to uncover more!" hint sits left of the spread-out notes.
   - CTA "Read the stories!".
9. **I believe…** line, then **Contact** ("let's grab the next drink", CTA "Ready when you are!").
10. **Footer** (dark): "margot tran" wordmark, section links, and LinkedIn, Instagram and Facebook.

## Images

- Photos are Margot's own, embedded as base64 data URIs.
- Use her crops as they are; do not re-crop them.
- Hero and circle photos get a blue duotone, made with PIL: `ImageOps.colorize(autocontrast(gray, cutoff=1), black='#1d2a40', mid='#8facd8', white='#f2f6fc', midpoint=110)`.
- Hero cards add a dark gradient overlay so the text stays readable.

## Identity links

- Substack: https://substack.com/@lofopmartii
- LinkedIn: https://www.linkedin.com/in/ttnganhuyen
- Instagram: https://www.instagram.com/pie.at.ounl
- Facebook: https://www.facebook.com/pie.at.ounl/

## Checking changes

- No test suite. Before committing, open `index.html` with Playwright (Chromium is preinstalled) at 390px and 1440px wide.
- Confirm there are no `pageerror`s, and screenshot the part you changed.
