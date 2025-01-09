const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
  entry: path.resolve(__dirname, 'main.js'), // Entry point for the JS files
  output: {
    path: path.resolve(__dirname, 'dist'), // Output directory for JavaScript and CSS files
    filename: 'bundle.js', // The output file for JavaScript
  },
  module: {
    rules: [
      // Handling .riot files
      {
        test: /\.riot$/,
        include: [
          path.resolve(__dirname, 'components'), // Include components directory
        ],
        use: [
          {
            loader: '@riotjs/webpack-loader',
          },
        ],
      },
      // Handling .css files
      {
        test: /\.css$/,
        use: [
          MiniCssExtractPlugin.loader, // Extracts CSS into its own file
          'css-loader', // Resolves imports in CSS files
        ],
      },
    ],
  },
  resolve: {
    extensions: ['.js', '.riot'], // Resolve JavaScript and Riot extensions
    alias: {
      '@components': path.resolve(__dirname, 'components'),  // Giving a name to easily import components instead of relative imports
    },
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: 'styles.css', // Output the CSS file
    }),
  ],
  devServer: {
    static: path.resolve(__dirname), // Serve static files from the current directory
    port: 8080, // Development server port
  },
  mode: 'development', // Development mode (set to 'production' for production builds)
};
