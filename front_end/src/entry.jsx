import React, {Component} from "react";
import {render} from "react-dom";
import {ApolloClient, ApolloProvider} from 'react-apollo';

const client = new ApolloClient();

import HomepageContainer from "./containers/HomepageContainer.jsx";


class Homepage extends Component {
    render() {
        return (
            <ApolloProvider client={client}>
                <HomepageContainer />
            </ApolloProvider>
        )
    }
}


render(<Homepage/>, document.getElementById('root'));