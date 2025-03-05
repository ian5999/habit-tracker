/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}"],

  theme: {
    fontFamily:{
      normal: ['roboto'],
    }, 
    extend: {
      colors: {
        'vuejs': "#49e659"
      },
    },
  },
  plugins: [],
}

