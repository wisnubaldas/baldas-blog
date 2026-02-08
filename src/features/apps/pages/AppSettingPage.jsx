import AppPageLayout from './AppPageLayout'

function AppSettingPage({ app }) {
  return (
    <AppPageLayout
      app={app}
      intro="Kelola konfigurasi dan akses pengguna untuk seluruh integrasi."
      checklist={[
        'Tambahkan form untuk memperbarui kredensial atau konfigurasi global.',
        'Kelola role & permissions yang mempengaruhi modul lain.',
        'Pastikan perubahan tersimpan dan tervalidasi sebelum diterapkan.',
      ]}
    />
  )
}

export default AppSettingPage
