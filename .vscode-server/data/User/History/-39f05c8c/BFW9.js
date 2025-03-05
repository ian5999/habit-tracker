/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}"],
  theme: {
    extend: {
      spacing: {
        '100': '3.25rem',
        '150': '3.75rem',
        '200': '32rem',
        '250': '36rem',
      }
    }
  },

  plugins: [],
}
