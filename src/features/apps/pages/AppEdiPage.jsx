import { FileText, LayoutDashboard, Settings, Users } from 'lucide-react'

import AppPageLayout from './AppPageLayout'

const nav = [
  { title: 'Dashboard', href: '/dashboard', icon: LayoutDashboard },
  { title: 'Invoice', href: '/invoice', icon: FileText },
  { title: 'Users', href: '/users', icon: Users },
  { title: 'Settings', href: '/settings', icon: Settings },
]

function AppEdiPage({ app }) {
  return (
    <AppPageLayout
      app={app}
      intro="Siapkan integrasi Electronic Data Interchange untuk pertukaran data otomatis dengan partner bisnis."
      checklist={[
        'Definisikan mapping dokumen EDI (ORDERS, DESADV, INVOIC, dsb.).',
        'Tambahkan endpoint webhook atau polling untuk menerima dan mengirim pesan.',
        'Monitor log transaksi dan tangani retry saat koneksi gagal.',
      ]}
    >
      <div className="grid gap-6 lg:grid-cols-[260px,1fr]">
        <nav className="rounded-md border border-slate-200 bg-white shadow-sm">
          <div className="border-b border-slate-200 px-4 py-3">
            <p className="text-sm font-semibold text-slate-900">Menu</p>
            <p className="text-xs text-slate-500">Navigasi EDI</p>
          </div>
          <ul className="divide-y divide-slate-100">
            {nav.map((item) => (
              <li key={item.href}>
                <a
                  href={item.href}
                  className="flex items-center gap-3 px-4 py-3 text-sm font-medium text-slate-700 transition hover:bg-indigo-50 hover:text-indigo-700"
                >
                  <item.icon className="h-4 w-4" />
                  <span>{item.title}</span>
                </a>
              </li>
            ))}
          </ul>
        </nav>

        <div className="rounded-md border border-dashed border-slate-200 bg-white/60 p-6 text-sm text-slate-600">
          <p className="font-semibold text-slate-900">Konten utama EDI</p>
          <p className="mt-2">
            Gunakan area ini untuk menaruh dashboard, tabel transaksi, atau detail dokumen EDI. Integrasikan dengan API
            yang relevan lalu ganti placeholder ini.
          </p>
        </div>
      </div>
    </AppPageLayout>
  )
}

export default AppEdiPage
