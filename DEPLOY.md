# SlateMind website

Static site, no build step. Push the folder root to the website repo; Vercel serves it as is.

- Website: https://slatemind-webpage.vercel.app
- App: https://slate-mind.vercel.app
- Contact form: https://saksham-mogha.vercel.app/contact

If the domain changes, search and replace `https://slatemind-webpage.vercel.app` in every .html, .txt and .xml file.

## Media
- `assets/demo.mp4`: 54 s product demo (home page player).
- `assets/demo-poster.webp`, `assets/pitch-poster.webp`: designed video covers (rendered from HTML, 1600x900).
- `assets/pitch.mp4`: the recorded pitch (720p, about 20 MB, pitch page).
- `assets/synopsis-p1.webp`, `synopsis-p2.webp`: the synopsis as images (view only). The PDF itself is intentionally not published.
- `og.jpg`: 1200x630 share image.

## Check after every deploy
- Both Launch buttons open the app
- The demo and pitch videos play, seek, go full screen and close
- /og.jpg loads; /privacy, /terms, /cookies, /pitch open
- Verify against the running app that the entered name stays in the browser (the Privacy Policy says so)

## View-only note
Videos and synopsis pages have no download buttons, native download controls are off, and right-click/drag is blocked. This only deters casual saving: anything a browser can show can still be captured by a determined user. Keep the original files private (do not commit the PDF or source recordings).
