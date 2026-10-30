# 47 Skin — Anti-Blemish & Scar Repair Serum campaign concept

Speculative portfolio campaign, not commissioned, reviewed, or published by 47 Skin.

## Source files

- `index.html` — document and SEO metadata
- `package.json` — React 19, React DOM 19, Lucide and Vite 7 dependencies
- `vite.config.js` — Vite config
- `src/main.jsx` — React entry
- `src/App.jsx` — page sections, image fallbacks, accessible menu and FAQ
- `src/style.css` — editorial layouts, responsive adjustments, scientific decoration
- `asset-manifest.json` — original assets and first-party URLs
- `fetch_original_assets.py` — optional validated retrieval of original imagery
- `public/assets/` — locally downloaded brand assets when available

## GitHub → Vercel

1. Extract the ZIP. Upload the *contents* of `47skin-campaign/` to the root of your GitHub repository (not a nested folder).
2. In Vercel: **Add New → Project → Import Git Repository**, select the repository.
3. Framework: **Vite**. Root Directory: `./`. Install: `npm install`. Build: `npm run build`. Output directory: `dist`. No environment variables are required.
4. Deploy. Check the Vercel build log. A build has **not** been verified in this environment.
5. Open the preview deployment and check images, hover/focus states, CTA links and FAQ at mobile, tablet and desktop widths.

## Local commands (optional; Vercel can run these)

```sh
npm install
npm run dev
npm run build
npm run preview
```

## Asset retrieval

Authentic original images are preferred. When direct 47 Skin CDN access is available, install Pillow and run `python fetch_original_assets.py`. The script validates HTTP status, MIME, image dimensions and original extension, and keeps existing valid files.

Images first load from `/assets/filename`, then the corresponding official CDN URL, then a deliberately styled unavailable-image panel. The `public/assets/` directory currently contains **no original brand photographs** because the container couldn't resolve `47skin.com`; **the website is not self-contained**. The 16-image inventory in `asset-manifest.json` includes the authentic product photo `PDP_Serum_Frame_12.jpg`. It is from the official product page. To make the project self-contained, download every required original image from 47 Skin and save it with the exact manifest filename.

Do not replace authentic clinical or customer photos with generated content. No fictional testimonials, customer videos, press logos or safety certificates are provided. Without a verified press-logo set, the Featured In area is replaced by a *Further Reading* panel linking to the original clinical research page.

## Design and content choices

- Hero: official serum photo reference; the amber-brown bottle/black pump/white label are preserved in the source image rather than AI recreations.
- Ingredient panels: CSS/SVG conceptual diagrams, including AgCl and a chitosan polymer schematic. **Not the undisclosed proprietary molecular structure.**
- Laboratory: retains original microscope composition reference.
- Original clinical and before/after images: retained as verified-first-party-source references; not edited or enhanced.
- Evidence sources are separate: 99.9% lab result; six 12-week, 30-person clinical results; two 97% 30-day, 100-person consumer-survey results.
- Real results: links to the brand clinical page instead of fabricating individual customer stories.
- Video: omitted for lack of verified serum-specific videos.
- Newsletter: demonstration-only; typing an address will not create a subscription.

## Verification and limitations

**Verified in container:** six source files exist; original source inspected and selectively edited; manifests and Python download script parse; validated original product photo URL via web research; offline npm installation attempted.

**Unverified:** React production build, running browser, real-device responsive QA, JavaScript interactions, original CDN image rendering. `npm install --offline` returned `ENOTCACHED` for `lucide-react`; no packages installed. DNS resolution of `47skin.com` fails in the container. Vercel must install packages from its own build network.

**Preview checklist:** confirm all images or intentional fallback panels; hero bottle size and legibility; 320/375/768/1024/1440px widths; no horizontal scroll; menu opens/closes; FAQ expands/collapses; CTA and research links resolve; laboratory/clinical/survey footnotes remain separate; check browser console; verify reduced-motion preference.

Official references:
- https://47skin.com/pages/clinical-trials
- https://47skin.com/products/anti-blemish-scar-repair-serum
- https://47skin.com/pages/silver-chitoderm
