# Deploying the SlateMind site

1. Run `python3 configure.py --site ... --app ... --owner ...` (see top of the file). It fills in every placeholder.
2. Create a new Vercel project from this folder (no build command, output = this folder). Point your domain at it.
3. Keep the app as a separate Vercel project (for example at app.yourdomain.com) and use that as `--app`.
4. Open every page on a phone, check the Menu, the sample-lesson buttons and the legal pages.
5. Submit `/sitemap.xml` in Google Search Console.

## Verify before launch
- The legal pages describe your code as I read it: no accounts, no database, IP used for rate limiting, Groq and Vercel as processors, progress in localStorage. Re-check against the running app.
- Confirm the feature counts on the home page (10 levels, 16 badges, 3 quiz questions, 3 themes) in the app.
- Have a parent/guardian or a lawyer review the Privacy Policy and Terms. They are good-faith drafts, not legal advice.
- Re-do the Privacy Policy and add consent flows before adding accounts, analytics or payments.

## Media
- `assets/demo.mp4` is a 56 s, 1.0 MB web cut of your screen recording (browser tabs and URL bar cropped out, idle time and the failed follow-up removed). The original is not included.
- Screenshots are cropped WebP copies. Re-export the same way if the app UI changes.
