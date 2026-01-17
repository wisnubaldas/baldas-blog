import './App.css'
import { Icon } from '@iconify/react'
import { Link, Route, Routes } from 'react-router-dom'

import CardShell from './components/CardShell'
import { apps } from './data/apps'
import APIIPage from './pages/apiiPage'
import EDIPage from './pages/ediPage'
import HUBNETPage from './pages/hubnetPage'
import SettingPage from './pages/settingPage'
import TPSOnlinePage from './pages/tpsOnlinePage'

function Landing() {
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

        <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-3 auto-rows-fr">
          {apps.map((item) => (
            <Link key={item.name} to={item.path} className="block h-full">
              <CardShell>
                <div className="flex h-full items-start gap-6">
                  <span className="shrink-0 inline-flex items-center justify-center rounded-md bg-indigo-100 p-6 shadow-lg mr-2">
                    <Icon icon={item.icon} width={80} height={80} className="text-indigo-600" />
                  </span>
                  <div className="flex flex-col">
                    <h3 className="text-lg font-semibold text-slate-900">{item.name}</h3>
                    <p className="mt-2 text-sm text-slate-600">{item.description}</p>
                  </div>
                </div>
              </CardShell>
            </Link>
          ))}
        </div>
      </section>
    </main>
  )
}

function App() {
  return (
    <Routes>
      <Route path="/" element={<Landing />} />
      <Route path="/edi" element={<EDIPage />} />
      <Route path="/tps-online" element={<TPSOnlinePage />} />
      <Route path="/ap-ii" element={<APIIPage />} />
      <Route path="/hubnet" element={<HUBNETPage />} />
      <Route path="/setting" element={<SettingPage />} />
    </Routes>
  )
}

export default App
