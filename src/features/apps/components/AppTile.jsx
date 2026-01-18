import { Icon } from '@iconify/react'
import { Link } from 'react-router-dom'

import CardShell from '../../../components/common/CardShell'

function AppTile({ app }) {
  return (
    <Link to={app.path} className="block h-full">
      <CardShell>
        <div className="flex h-full items-start gap-3">
          <span className="shrink-0 inline-flex items-center justify-center rounded-md bg-indigo-100 p-1 shadow-md mr-2">
            <Icon icon={app.icon} width={60} height={60} className="text-indigo-500" />
          </span>
          <div className="flex flex-col">
            <h3 className="text-lg font-semibold text-slate-900">{app.name}</h3>
            <p className="mt-2 text-sm text-slate-600">{app.description}</p>
          </div>
        </div>
      </CardShell>
    </Link>
  )
}

export default AppTile
