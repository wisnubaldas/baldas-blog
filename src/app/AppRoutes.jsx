import { Navigate, Route, Routes } from 'react-router-dom'

import { apps } from '../features/apps/data/apps'
import AppDetailPage from '../features/apps/pages/AppDetailPage'
import AppListPage from '../features/apps/pages/AppListPage'

function AppRoutes() {
  return (
    <Routes>
      <Route path="/" element={<AppListPage />} />
      {apps.map((app) => (
        <Route key={app.key} path={app.path} element={<AppDetailPage app={app} />} />
      ))}
      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  )
}

export default AppRoutes
