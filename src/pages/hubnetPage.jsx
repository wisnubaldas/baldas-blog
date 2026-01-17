import AppDetailPage from './appDetailPage'
import { getApp } from '../data/apps'

const app = getApp('hubnet')

export default function HUBNETPage() {
  return <AppDetailPage app={app} />
}
