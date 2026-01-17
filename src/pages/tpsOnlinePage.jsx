import AppDetailPage from './appDetailPage'
import { getApp } from '../data/apps'

const app = getApp('tps-online')

export default function TPSOnlinePage() {
  return <AppDetailPage app={app} />
}
