module.exports = {
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  theme: {
    extend: {
      lineHeight: {
        // Need refactor these px values
        13: "13px",
        19: "19px",
        130: "130%",
        134: "134%",
        137: "137%",
        138: "138%",
        35: "35px",
      },
      screens: {
        sx: "320px",
        xs: "375px",
        ms: "500px",
        sm: "640px",
        md: "768px",
        dm: "992px",
        lg: "1024px",
        xl: "1280px",
        "2xl": "1536px",
        xxl: "1536px",
      },
      colors: {
        black: "#232323",
      },
    },
  },
  plugins: [],
};
