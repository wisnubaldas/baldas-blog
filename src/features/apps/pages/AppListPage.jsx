import AppTile from '../components/AppTile'
import { apps } from '../data/apps'

function AppListPage() {
  return (
    <main className="min-h-screen bg-slate-50">
      <section className="mx-auto max-w-6xl px-4 py-10 space-y-8">
        <header className="space-y-2">
          <p className="text-sm uppercase tracking-[0.2em] text-slate-500">Integrations</p>
          <h1 className="text-3xl font-bold text-slate-900">Choose an application to continue</h1>
          <p className="text-slate-600">
            Quick access to each service with clear labels and matching icons. Tap any tile to open the corresponding
            system.
          </p>
        </header>

        <div className="grid gap-4 md:grid-cols-2 xl:grid-cols-3 auto-rows-fr">
          {apps.map((app) => (
            <AppTile key={app.key} app={app} />
          ))}
        </div>
      </section>
    </main>
  )
}

export default AppListPage
