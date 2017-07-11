import React, {Component} from "react";

import Header from "../components/Header.jsx";
import Section from "../components/Section.jsx";
import Footer from "../components/Footer.jsx";


export default class HomepageContainer extends Component {
    render() {
        return (
            <div className="grid-container">
                <div className="col-sm-12">
                    <Header>My Product Shop</Header>
                    <Section/>
                    <Footer/>
                </div>
            </div>
        )
    }
}