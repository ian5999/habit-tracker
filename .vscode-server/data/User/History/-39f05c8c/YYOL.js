/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}"],

  theme: {
    fontFamily:{
      _normal: ['roboto'],
      get normal() {
        return this._normal;
      },
      set normal(value) {
        this._normal = value;
      },
    }, 
    extend: {
      colors: {
        'vuejs': "#49e659"
      },
    },
  },
  plugins: [],
}

