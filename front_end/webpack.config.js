const path = require('path');
const webpack = require('webpack');

const BundleTracker = require('webpack-bundle-tracker');


const staticFilesDir = path.resolve(__dirname, '../static/js/');

module.exports = {
    entry: {
        app: './src/app.js',  // declare the entry point where all starts
        vendors: ['react']    // declare the external libs that will be bundled into a separate file (good for caching)
    },
    output: {
        path: staticFilesDir,           // dir name to save the bundles (app and vendor)
        filename: '[name]-[hash:8].js'  // filename of my app's bundle. The [name] is the "app" defined in the "entry" object above.
    },
    module: {
        rules: [
            {
                test: /\.js$/, exclude: /node_modules/, use: "babel-loader"
            }
        ]
    },
    plugins: [
        new webpack.optimize.CommonsChunkPlugin({
            name: 'vendors',        // this must match the "entry's" property above (vendors)
            filename: 'vendors.js'  // the filename of the bundle that will be created from all libs listed in the "vendors" array above.
        }),
        new BundleTracker({
            path: staticFilesDir,
            filename: 'webpack-stats.json'
        })
    ]
    // devServer: {
    //     contentBase: path.join(__dirname, 'dist'),
    //     port: 9000,
    //     stats: 'errors-only',
    //     open: true
    // }
};