import { Navigate, Route, Routes } from 'react-router-dom'

import { apps } from '../features/apps/data/apps'
import AppApIiPage from '../features/apps/pages/AppApIiPage'
import AppEdiPage from '../features/apps/pages/AppEdiPage'
import AppHubnetPage from '../features/apps/pages/AppHubnetPage'
import AppListPage from '../features/apps/pages/AppListPage'
import AppPageLayout from '../features/apps/pages/AppPageLayout'
import AppSettingPage from '../features/apps/pages/AppSettingPage'
import AppTpsOnlinePage from '../features/apps/pages/AppTpsOnlinePage'

const appPages = {
  edi: AppEdiPage,
  'tps-online': AppTpsOnlinePage,
  'ap-ii': AppApIiPage,
  hubnet: AppHubnetPage,
  setting: AppSettingPage,
}

function AppRoutes() {
  return (
    <Routes>
      <Route path="/" element={<AppListPage />} />
      {apps.map((app) => {
        const Page = appPages[app.key] || AppPageLayout
        return <Route key={app.key} path={app.path} element={<Page app={app} />} />
      })}
      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  )
}

export default AppRoutes
