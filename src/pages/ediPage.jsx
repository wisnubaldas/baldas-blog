import AppDetailPage from './appDetailPage'
import { getApp } from '../data/apps'

const app = getApp('edi')

export default function EDIPage() {
  return <AppDetailPage app={app} />
}
