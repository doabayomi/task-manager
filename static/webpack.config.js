const path = require('path');

module.exports = {
  entry: './main.js', // Entry point
  output: {
    path: path.resolve(__dirname, 'js'), // Output directory
    filename: 'bundle.js', // Output file name
  },
  module: {
    rules: [
      {
        test: /\.riot$/, // Process .riot files
	include : [
          path.resolve(__dirname, 'comoonents'),
          path.resolve(__dirname, '.'),
	],
        use: [
          {
            loader: '@riotjs/webpack-loader',
          },
        ],
      },
    ],
  },
  resolve: {
    extensions: ['.js', '.riot'], // Resolve these extensions
  },
  devServer: {
    static: path.resolve(__dirname, 'static'), // Serve files from dist
    port: 8080, // Development server port
  },
  mode: 'development', // Mode (can be 'production' for optimized builds)
};
