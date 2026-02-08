import AppPageLayout from './AppPageLayout'

function AppApIiPage({ app }) {
  return (
    <AppPageLayout
      app={app}
      intro="Kelola billing dan invoice Angkasa Pura II dari satu tempat."
      checklist={[
        'Hubungkan endpoint otorisasi AP II dan simpan token secara aman.',
        'Tampilkan ringkasan tagihan, status pembayaran, dan riwayat transaksi.',
        'Sediakan ekspor laporan ke CSV atau PDF bila diperlukan.',
      ]}
    />
  )
}

export default AppApIiPage
