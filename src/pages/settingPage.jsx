import AppDetailPage from './appDetailPage'
import { getApp } from '../data/apps'

const app = getApp('setting')

export default function SettingPage() {
  return <AppDetailPage app={app} />
}
