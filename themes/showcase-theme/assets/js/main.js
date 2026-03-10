window.tailwind = window.tailwind || {};
window.tailwind.config = {
	darkMode: "class",
	theme: {
		extend: {
			colors: {
				brand: {
					DEFAULT: "#0bb8da",
					dark: "#0891ac",
					light: "#3ec7e1"
				},
				background: "#0a0a0a",
				darkBg: "#0f172a",
				darkSurface: "#1e293b"
			},
			fontFamily: {
				sans: ["Inter", "sans-serif"]
			},
			borderRadius: {
				custom: "8px"
			},
			boxShadow: {
				glow: "0 0 15px -3px rgba(11, 184, 218, 0.5)"
			}
		}
	}
};
