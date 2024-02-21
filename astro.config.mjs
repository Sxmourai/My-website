import { defineConfig } from "astro/config";
import tailwind from "@astrojs/tailwind";

import react from "@astrojs/react";

// https://astro.build/config
export default defineConfig({
  server: {
    port: 8000,
  },
  // output: 'server'
  integrations: [
    tailwind({
        applyBaseStyles: false,
    }),
    react(),
  ],
});
