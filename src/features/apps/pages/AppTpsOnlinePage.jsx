import AppPageLayout from './AppPageLayout'

function AppTpsOnlinePage({ app }) {
  return (
    <AppPageLayout
      app={app}
      intro="Pantau status cargo Beacukai dan sinkronkan data TPS Online dengan sistem internal."
      checklist={[
        'Konfigurasi kredensial API TPS Online dan variabel lingkungan yang dibutuhkan.',
        'Buat tabel atau kartu ringkasan untuk memantau pergerakan kontainer.',
        'Tambahkan notifikasi atau export data bila diperlukan oleh operasional.',
      ]}
    />
  )
}

export default AppTpsOnlinePage
