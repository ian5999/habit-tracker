/** @type {import('tailwindcss').Config} */
module.exports = {
  theme: {
    screens: {
      sm: '480px',
      md: '768px',
      lg: '976px',
      xl: '1440px',
    },

  content: ["./src/**/*.{html,js}"],

  theme: {
    extend: {
      colors: {
        'vuejs': "#49e659"
      },
    },
  },
  plugins: [],
}
