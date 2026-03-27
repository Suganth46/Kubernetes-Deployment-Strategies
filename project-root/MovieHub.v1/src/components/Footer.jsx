export default function Footer() {
  return (
    <footer className="flex flex-col gap-6 border-t border-white/10 pt-8 text-sm text-slate-400 md:flex-row md:items-center md:justify-between">
      <div>
        <p className="text-white">MovieHub v1</p>
        <p className="text-xs uppercase tracking-[0.2em]">Original Hollywood archive</p>
      </div>
      <div className="flex flex-wrap gap-6 text-xs uppercase tracking-[0.2em]">
        <a className="transition hover:text-white" href="#">
          Reviews
        </a>
        <a className="transition hover:text-white" href="#">
          Interviews
        </a>
        <a className="transition hover:text-white" href="#">
          About
        </a>
      </div>
      <p className="text-xs">2026 MovieHub v1. All rights reserved.</p>
    </footer>
  );
}
