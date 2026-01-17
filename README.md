# React + Vite Boilerplate (Vercel-ready)

Lightweight React setup with Vite, tailored for quick deploys to Vercel. Comes with a minimal landing layout you can extend into a blog or marketing page.

## Install & run

```bash
npm install
npm run dev
```

## Build

```bash
npm run build
```

Vite outputs to `dist/` (declared in `vercel.json`). Use `npm run preview` to check the production build locally.

## Deploy to Vercel

- **CLI:** `vercel --prod` (after authenticating with `vercel login`). The included `vercel.json` sets `buildCommand` to `npm run build` and `outputDirectory` to `dist`.
- **Dashboard:** Push this repo to GitHub/GitLab/Bitbucket and import it on Vercel. Framework detection will pick Vite automatically.

Once deployed, every git push will create a preview deployment; merging to the default branch promotes the changes to production.
