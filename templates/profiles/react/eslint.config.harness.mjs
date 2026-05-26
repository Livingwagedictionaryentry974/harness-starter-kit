// React harness snippet. Merge relevant rules into your eslint.config.mjs.
// Requires: eslint-plugin-react-hooks, eslint-plugin-react-refresh
// Install: npm install -D eslint-plugin-react-hooks eslint-plugin-react-refresh

import reactHooks from "eslint-plugin-react-hooks";
import reactRefresh from "eslint-plugin-react-refresh";

export default [
  {
    files: ["**/*.{js,jsx,ts,tsx}"],
    plugins: {
      "react-hooks": reactHooks,
      "react-refresh": reactRefresh,
    },
    rules: {
      // Enforce Rules of Hooks (no conditional hook calls, etc.)
      ...reactHooks.configs.recommended.rules,

      // Warn when components are not safe for React Fast Refresh
      "react-refresh/only-export-components": ["warn", { allowConstantExport: true }],

      // Catch common mistakes
      "no-console": "warn",
      "prefer-const": "error",
      "no-unused-vars": ["error", { argsIgnorePattern: "^_" }],
    },
  },
];
