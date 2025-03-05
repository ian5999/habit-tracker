/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}"],
  theme: {
    extend: {
      spacing: {
        '1120':'1120px',
        '32.279': '32.278px',
        '160':'160',
        '154':'154',
        '100': '594px',
        '200': '1406px',
        '300': '454px',
        '400': '1120px',
      },

      colors: {
        'beige': '#F3DDC4',
        'lbeige': '#FAF6F0',
      }
    }
  },

  plugins: [],
}
