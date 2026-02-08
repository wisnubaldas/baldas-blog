import { Icon } from "@iconify/react";
import { Link } from "react-router-dom";

import CardShell from "../../../components/common/CardShell";

const defaultChecklist = [
  "Tambahkan komponen utama (tabel, form, atau chart) yang dibutuhkan aplikasi ini.",
  "Hubungkan ke API atau data source terkait setelah backend siap.",
  "Perbarui detail di data/apps.js bila ada perubahan path, ikon, atau nama.",
];

function AppPageLayout({ app, intro, checklist = defaultChecklist, children }) {
  if (!app) {
    return (
      <main className="min-h-screen bg-slate-50">
        <section className="mx-auto max-w-4xl px-4 py-10">
          <CardShell>
            <p className="text-slate-600">Aplikasi tidak ditemukan.</p>
          </CardShell>
        </section>
      </main>
    );
  }

  return (
    <main className="min-h-screen bg-slate-50">
      <section className="w-full max-w-full mx-auto lg:max-w-5xl px-4 py-10 space-y-8">
        <CardShell>
          <div className="flex flex-col gap-6">
            <div className="flex flex-wrap items-start gap-4 sm:gap-6">
              <span className="inline-flex h-20 w-20 shrink-0 items-center justify-center rounded-md bg-indigo-100 p-4 shadow-lg">
                <Icon
                  icon={app.icon}
                  width={64}
                  height={64}
                  className="text-indigo-600"
                />
              </span>
              <div className="space-y-1">
                <p className="text-xs uppercase tracking-[0.2em] text-slate-500">
                  {app.key}
                </p>
                <h1 className="text-3xl font-bold text-slate-900">
                  {app.name}
                </h1>
                <p className="text-slate-600">{app.description}</p>
              </div>
            </div>

            <div className="grid gap-6 md:grid-cols-[1.1fr,0.9fr]">
              <div className="space-y-3">
                <h2 className="text-lg font-semibold text-slate-900">
                  Halaman default
                </h2>
                <p className="text-slate-600">
                  {intro ||
                    `Gunakan halaman ini sebagai titik awal untuk mengembangkan modul ${app.name}.`}
                </p>
                {children}
              </div>
              <div className="rounded-md border border-indigo-100 bg-indigo-50/60 p-4 shadow-inner">
                <p className="text-sm font-semibold text-indigo-900">
                  Checklist awal
                </p>
                <ul className="mt-2 space-y-2 text-sm text-indigo-800">
                  {checklist.map((item) => (
                    <li key={item} className="flex gap-2">
                      <span aria-hidden="true">•</span>
                      <span>{item}</span>
                    </li>
                  ))}
                </ul>
              </div>
            </div>

            <div className="flex flex-wrap gap-3">
              <Link
                to="/"
                className="inline-flex items-center text-sm font-semibold text-indigo-600 hover:text-indigo-700"
              >
                Kembali ke daftar
              </Link>
            </div>
          </div>
        </CardShell>
      </section>
    </main>
  );
}

export default AppPageLayout;
