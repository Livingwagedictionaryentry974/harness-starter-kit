// Vue harness snippet. Merge relevant rules into your eslint.config.mjs.
// Requires: eslint-plugin-vue, vue-eslint-parser
// Install: npm install -D eslint-plugin-vue

import pluginVue from "eslint-plugin-vue";

export default [
  // Vue 3 recommended rules (includes essential + strongly-recommended + recommended)
  ...pluginVue.configs["flat/recommended"],

  {
    files: ["**/*.{vue,js,ts}"],
    rules: {
      // Enforce <script setup> usage
      "vue/component-api-style": ["error", ["script-setup"]],

      // Enforce PascalCase component names
      "vue/component-name-in-template-casing": ["error", "PascalCase"],

      // Disallow mutation of props
      "vue/no-mutating-props": "error",

      // Require defineProps and defineEmits to have type annotations
      "vue/define-props-declaration": ["error", "type-based"],
      "vue/define-emits-declaration": ["error", "type-based"],

      // Catch common mistakes
      "no-console": "warn",
      "prefer-const": "error",
      "no-unused-vars": ["error", { argsIgnorePattern: "^_" }],
    },
  },
];
