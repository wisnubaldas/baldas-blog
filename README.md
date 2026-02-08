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

## Project structure

- `src/app/` holds the app shell (`App.jsx`) and route config (`AppRoutes.jsx`).
- `src/features/apps/` groups app-specific pieces: data (`data/apps.js`), list page (`pages/AppListPage.jsx`), per-app default pages (`pages/AppEdiPage.jsx`, `pages/AppTpsOnlinePage.jsx`, `pages/AppApIiPage.jsx`, `pages/AppHubnetPage.jsx`, `pages/AppSettingPage.jsx`), shared layout (`pages/AppPageLayout.jsx`), and tiles (`components/AppTile.jsx`).
- `src/components/common/` keeps shared UI (e.g., `CardShell.jsx`).

### Folder diagram

```
src/
|-- app/
|   |-- App.jsx
|   |-- App.css
|   `-- AppRoutes.jsx
|-- assets/            # static assets (images, fonts, etc.)
|-- components/
|   |-- common/CardShell.jsx
|   `-- ui/
|       |-- button.jsx
|       `-- card.jsx
|-- features/
|   `-- apps/
|       |-- components/AppTile.jsx
|       |-- data/apps.js
|       `-- pages/
|           |-- AppApIiPage.jsx
|           |-- AppEdiPage.jsx
|           |-- AppHubnetPage.jsx
|           |-- AppListPage.jsx
|           |-- AppPageLayout.jsx
|           |-- AppSettingPage.jsx
|           `-- AppTpsOnlinePage.jsx
|-- lib/utils.js
|-- index.css
`-- main.jsx
```

## Routing

- Client routing uses `react-router-dom` (`BrowserRouter` in `src/main.jsx`).
- Routes are centralized in `src/app/AppRoutes.jsx`, auto-generated from `apps` data.

## Deploy to Vercel

- **CLI:** `vercel --prod` (after authenticating with `vercel login`). The included `vercel.json` sets `buildCommand` to `npm run build` and `outputDirectory` to `dist`.
- **Dashboard:** Push this repo to GitHub/GitLab/Bitbucket and import it on Vercel. Framework detection will pick Vite automatically.

Once deployed, every git push will create a preview deployment; merging to the default branch promotes the changes to production.
