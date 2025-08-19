// eslint.config.js
export default [
  { ignores: ['node_modules/'] },
  {
    files: ['**/*.js'],
    languageOptions: {
      ecmaVersion: 2021,
      sourceType: 'module',
    },
    rules: {
      'no-underscore-dangle': 'off',
      'no-console': 'off',
    },
  },
];
