import { Link } from 'react-router-dom'
import { Icon } from '@iconify/react'

import CardShell from '../../../components/common/CardShell'

function AppDetailPage({ app }) {
  if (!app) {
    return (
      <main className="min-h-screen bg-slate-50">
        <section className="mx-auto max-w-4xl px-4 py-10">
          <CardShell>
            <p className="text-slate-600">Aplikasi tidak ditemukan.</p>
          </CardShell>
        </section>
      </main>
    )
  }

  return (
    <main className="min-h-screen bg-slate-50">
      <section className="mx-auto max-w-4xl px-4 py-10">
        <CardShell>
          <div className="flex flex-col gap-3">
            <div className="flex items-start gap-6">
              <span className="shrink-0 inline-flex items-center justify-center rounded-md bg-indigo-100 p-6 shadow-lg mr-2">
                <Icon icon={app.icon} width={80} height={80} className="text-indigo-600" />
              </span>
              <div>
                <h1 className="text-2xl font-bold text-slate-900">{app.name}</h1>
                <p className="mt-1 text-slate-600">{app.description}</p>
              </div>
            </div>
            <p className="text-sm text-slate-500">Halaman ini bisa diisi konten khusus untuk aplikasi {app.name}.</p>
            <Link to="/" className="inline-flex text-sm font-semibold text-indigo-600 hover:text-indigo-700">
              Kembali ke daftar
            </Link>
          </div>
        </CardShell>
      </section>
    </main>
  )
}

export default AppDetailPage
