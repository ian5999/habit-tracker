/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}"],
  theme: {
    extend: {
      spacing: {
        '100': '594px',
        '150': '3.75rem',
        '200': '32rem',
        '250': '36rem',
      },

      colors
    }
  },

  plugins: [],
}
