import React, { Component } from "react";
import {gql, graphql} from 'react-apollo';


class Section extends Component {
    render() {
        let {data} = this.props;

        if (data.loading) {
            return <p>Loading ...</p>;
        }

        if (data.error) {
            return <p>{data.error.message}</p>;
        }

        const products = data.products.map((product) => {
            return (
                <li key={product.slug}>{product.name} - {product.slug}</li>
            );
        });

        return (
            <div>
                <h1>{ this.props.children }</h1>
                <ul>
                    {products}
                </ul>
            </div>
        );
    }
}


export default graphql(gql`
query {
  products {
    name, slug
  }
}
`
)(Section);
