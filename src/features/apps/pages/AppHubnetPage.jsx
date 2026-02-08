import AppPageLayout from './AppPageLayout'

function AppHubnetPage({ app }) {
  return (
    <AppPageLayout
      app={app}
      intro="Lacak armada dan aktivitas Dinas Perhubungan melalui HUBNET."
      checklist={[
        'Integrasikan data lokasi atau jadwal yang disediakan HUBNET.',
        'Bangun tampilan peta atau daftar status perangkat/armada.',
        'Tambahkan filter dan pencarian untuk memudahkan monitoring lapangan.',
      ]}
    />
  )
}

export default AppHubnetPage
