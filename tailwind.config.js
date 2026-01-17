/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      fontFamily: {
        display: ['Space Grotesk', 'Manrope', 'Segoe UI', 'sans-serif'],
        body: ['Manrope', 'Space Grotesk', 'Segoe UI', 'sans-serif'],
      },
      colors: {
        accent: '#36cfc9',
        midnight: '#0b1224',
      },
    },
  },
  plugins: [],
}
