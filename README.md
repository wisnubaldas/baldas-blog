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

## Styling (Tailwind + custom CSS)

- Tailwind is installed and configured (`tailwind.config.js`, `postcss.config.js`).
- Global directives live at the top of `src/index.css`; custom theme styles follow.
- Use Tailwind utilities alongside the existing CSS classes in `src/App.css`.

## shadcn/ui

- Base setup is ready for shadcn/ui primitives (tailwindcss-animate, tokens, `cn` helper).
- Existing components live in `src/components/ui/` (example: `src/components/ui/button.jsx`).
- Helper for class merging: `src/lib/utils.js` (`cn`).
- To add more components, copy from https://ui.shadcn.com/docs/components and drop them into `src/components/ui/` (adjust imports to `.jsx` and the Vite/React pathing). Utilities and theme tokens already exist in `tailwind.config.js`.

## Iconify

- Iconify is installed (`@iconify/react`). Import with `import { Icon } from '@iconify/react'`.
- Use any icon by id, e.g. `<Icon icon="lucide:settings" width={24} height={24} />`.

## Routing

- Client routing uses `react-router-dom` (`BrowserRouter` in `src/main.jsx`).
- Landing cards link to per-application pages defined in `src/App.jsx`; add new routes by extending the `apps` array.

## Deploy to Vercel

- **CLI:** `vercel --prod` (after authenticating with `vercel login`). The included `vercel.json` sets `buildCommand` to `npm run build` and `outputDirectory` to `dist`.
- **Dashboard:** Push this repo to GitHub/GitLab/Bitbucket and import it on Vercel. Framework detection will pick Vite automatically.

Once deployed, every git push will create a preview deployment; merging to the default branch promotes the changes to production.
