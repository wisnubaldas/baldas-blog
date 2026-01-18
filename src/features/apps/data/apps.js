export const apps = [
  { key: 'edi', name: 'EDI', description: 'Electronic Data Interchange', icon: 'solar:document-add-broken', path: '/edi' },
  { key: 'tps-online', name: 'TPS Online', description: 'Beacukai Cargo Monitoring', icon: 'mdi:radar', path: '/tps-online' },
  { key: 'ap-ii', name: 'AP II', description: 'Angkasapura II Invoice', icon: 'ph:air-traffic-control-duotone', path: '/ap-ii' },
  { key: 'hubnet', name: 'HUBNET', description: 'Dinas Perhubungan Tracking', icon: 'mdi:lan', path: '/hubnet' },
  { key: 'setting', name: 'Setting', description: 'Manage Application', icon: 'lucide:settings', path: '/setting' },
]

export function getApp(keyOrPath) {
  return apps.find((app) => app.key === keyOrPath || app.path === keyOrPath)
}
