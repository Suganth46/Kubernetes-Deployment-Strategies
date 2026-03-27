/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./static/**/*.{html,js}", "./src/**/*.{js,jsx}"],
  safelist: ["hidden", "opacity-0", "opacity-100", "opacity-70", "bg-emerald-300", "bg-white/30", "w-6", "w-1.5", "hover:bg-white/50"],
  theme: {
    extend: {
      keyframes: {
        fade: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        }
      },
      animation: {
        fade: 'fade 0.7s ease-in-out',
      }
    },
  },
  plugins: [],
};
