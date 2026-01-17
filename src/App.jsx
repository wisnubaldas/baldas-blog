import './App.css'

const deploymentSteps = [
  {
    title: 'Install dependencies',
    detail: 'npm install',
  },
  {
    title: 'Run locally',
    detail: 'npm run dev',
  },
  {
    title: 'Build for production',
    detail: 'npm run build',
  },
  {
    title: 'Deploy to Vercel',
    detail: 'vercel --prod (or connect the repo in the Vercel dashboard)',
  },
]

function App() {
  return (
    <div className="page">
      <header className="hero">
        <p className="eyebrow">React + Vite • Ready for Vercel</p>
        <h1>Launch a fast blog starter in minutes.</h1>
        <p className="lede">
          Opinionated React boilerplate with sensible defaults, clean styles, and a
          Vercel-ready build configuration. Extend it into your own blog or landing page
          without wrestling the setup.
        </p>
        <div className="hero-actions">
          <a className="button primary" href="https://vercel.com/new" target="_blank" rel="noreferrer">
            Deploy to Vercel
          </a>
          <a className="button ghost" href="https://vite.dev/guide/" target="_blank" rel="noreferrer">
            View Vite guide
          </a>
        </div>
      </header>

      <section className="panel">
        <div className="panel-head">
          <h2>Quick start</h2>
          <p>Follow these commands to run locally and ship to Vercel.</p>
        </div>
        <ol className="step-list">
          {deploymentSteps.map((step) => (
            <li key={step.title} className="step">
              <span className="pill">{step.title}</span>
              <code className="code">{step.detail}</code>
            </li>
          ))}
        </ol>
      </section>

      <section className="grid">
        <div className="card">
          <h3>Performance-first</h3>
          <p>
            Vite builds to an optimized `dist/` directory with out-of-the-box code splitting,
            so Vercel only needs `npm run build` and `dist` as the output folder.
          </p>
        </div>
        <div className="card">
          <h3>Modern styling</h3>
          <p>
            A lightweight layout and typography system is in place—swap colors and sections
            to shape your own blog or marketing page quickly.
          </p>
        </div>
        <div className="card">
          <h3>Zero config deploys</h3>
          <p>
            Framework detection, `vercel.json`, and the included scripts keep deploys predictable.
            Connect your repo on Vercel or use the CLI with one command.
          </p>
        </div>
      </section>
    </div>
  )
}

export default App
