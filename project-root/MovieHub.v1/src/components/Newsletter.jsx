export default function Newsletter() {
  const handleSubmit = (e) => {
    e.preventDefault();
    const email = e.target.querySelector('input[type="email"]').value;
    if (email) {
      const subscribers = JSON.parse(localStorage.getItem('newsletterSubscribers') || '[]');
      subscribers.push(email);
      localStorage.setItem('newsletterSubscribers', JSON.stringify(subscribers));
      alert('Subscribed! Email saved.');
      window.location.href = \mailto:selvamthiru712@gmail.com?subject=New Newsletter Subscription&body=Hi, Please add my email to the list: \\;
      e.target.reset();
    }
  };

  return (
    <section className="relative overflow-hidden rounded-3xl border border-white/10 bg-gradient-to-r from-emerald-200/10 via-slate-950 to-slate-950 px-8 py-10">
      <div className="absolute -left-20 top-6 h-40 w-40 rounded-full bg-emerald-200/20 blur-3xl" />
      <div className="relative z-10 flex flex-col gap-6 md:flex-row md:items-center md:justify-between">
        <div>
          <p className="text-xs uppercase tracking-[0.3em] text-emerald-200">
            Weekly Signal
          </p>
          <h3 className="text-2xl font-semibold text-white md:text-3xl">
            Get fresh reviews every Friday
          </h3>
          <p className="text-sm text-slate-300">
            No spam. Just cinematic highlights and sharp takes.
          </p>
        </div>
        <form onSubmit={handleSubmit} className="flex w-full max-w-md flex-col gap-3 sm:flex-row">
          <input
            type="email"
            placeholder="your@email.com"
            required
            className="w-full rounded-full border border-white/15 bg-white/5 px-5 py-3 text-sm text-white placeholder:text-slate-400 focus:border-emerald-200/70 focus:outline-none"
          />
          <button
            type="submit"
            className="rounded-full bg-emerald-200 px-6 py-3 text-sm font-semibold text-slate-900 transition hover:-translate-y-0.5"
          >
            Join list
          </button>
        </form>
      </div>
    </section>
  );
}
