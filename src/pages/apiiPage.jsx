import AppDetailPage from './appDetailPage'
import { getApp } from '../data/apps'

const app = getApp('ap-ii')

export default function APIIPage() {
  return <AppDetailPage app={app} />
}
