const path = require('path');
const webpack = require('webpack');

const constants = require('../constants');


module.exports = {
    context: path.resolve(__dirname, '..', 'src'),  // the current file is inside the webpack/ dir do we need to go up (..) once.
    entry: {
        app: './entry.jsx',  // declare the entry point where all starts (relative to context above, which means src/entry.jsx)
        vendors: ['react']   // declare the external libs that will be bundled into a separate file (good for caching)
    },
    output: {
        path: constants.staticFilesJsDir,  // dir name to save the bundles (two bundles will be created, "app" and "vendor").
        filename: '[name]-[hash:8].js'     // filename of my app's bundle. The [name] is the "app" defined in the "entry" object above.
    },
    plugins: [
        new webpack.EnvironmentPlugin(['NODE_ENV']),
        new webpack.optimize.CommonsChunkPlugin({
            name: 'vendors',        // this must match the "entry's" property above (vendors)
            filename: 'vendors.js'  // the filename of the bundle that will be created from all libs listed in the "vendors" array above.
        }),
    ],
    resolve: {}
};
