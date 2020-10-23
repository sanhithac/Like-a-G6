import React from 'react';
import './App.css';
import * as ReactBootStrap from 'react-bootstrap'

function App() {
  return (
    <div className="App">
      <ReactBootStrap.Navbar collapseOnSelect expand="sm" bg="dark" variant="dark">
  <ReactBootStrap.Navbar.Brand href="landing">Like A G6</ReactBootStrap.Navbar.Brand>
  <ReactBootStrap.Navbar.Toggle aria-controls="responsive-navbar-nav" />
  <ReactBootStrap.Navbar.Collapse id="responsive-navbar-nav">
    <ReactBootStrap.Nav className="mr-auto">
      <ReactBootStrap.Nav.Link href="#about">About</ReactBootStrap.Nav.Link>
      <ReactBootStrap.NavDropdown title="Account Details" id="collasible-nav-dropdown">
        <ReactBootStrap.NavDropdown.Item href="#action/3.1">See Avg Buy and Sell</ReactBootStrap.NavDropdown.Item>
        <ReactBootStrap.NavDropdown.Item href="#action/3.2">See Ending Positions</ReactBootStrap.NavDropdown.Item>
        <ReactBootStrap.NavDropdown.Item href="#action/3.3">See Realized Profit and Loss</ReactBootStrap.NavDropdown.Item>
        <ReactBootStrap.NavDropdown.Item href="#action/3.4">See Effective Profit and Loss</ReactBootStrap.NavDropdown.Item>
        <ReactBootStrap.NavDropdown.Divider />
      </ReactBootStrap.NavDropdown>
    </ReactBootStrap.Nav>
    <ReactBootStrap.Nav>
      <ReactBootStrap.Nav.Link href="#contact">Contact Us</ReactBootStrap.Nav.Link>
    </ReactBootStrap.Nav>
  </ReactBootStrap.Navbar.Collapse>
</ReactBootStrap.Navbar>
<div class='cardContainer'>

<ReactBootStrap.Card style={{ width: '18rem', margin:'10px' }}>
  <ReactBootStrap.Card.Img variant="top" src="https://ei.marketwatch.com/Multimedia/2015/09/21/Photos/ZQ/MW-DU756_Stock_20150921172954_ZQ.jpg?uuid=e6db074c-60a7-11e5-98d7-0015c588e0f6" />
  <ReactBootStrap.Card.Body>
    <ReactBootStrap.Card.Title>Avg Buy/Sell</ReactBootStrap.Card.Title>
    <ReactBootStrap.Card.Text>
      See the average buy/sell prices for each instrument.
    </ReactBootStrap.Card.Text>
    <ReactBootStrap.Button variant="dark" bg="dark">Check it out!</ReactBootStrap.Button>
  </ReactBootStrap.Card.Body>
</ReactBootStrap.Card>

<ReactBootStrap.Card style={{ width: '18rem', margin:'10px'}}>
  <ReactBootStrap.Card.Img variant="top" src="https://ei.marketwatch.com/Multimedia/2015/09/21/Photos/ZQ/MW-DU756_Stock_20150921172954_ZQ.jpg?uuid=e6db074c-60a7-11e5-98d7-0015c588e0f6" />
  <ReactBootStrap.Card.Body>
    <ReactBootStrap.Card.Title>Ending Positions</ReactBootStrap.Card.Title>
    <ReactBootStrap.Card.Text>
      See the ending positions for each dealer.
    </ReactBootStrap.Card.Text>
    <ReactBootStrap.Button variant="dark" bg="dark">Check it out!</ReactBootStrap.Button>
  </ReactBootStrap.Card.Body>
</ReactBootStrap.Card>

<ReactBootStrap.Card style={{ width: '18rem', margin:'10px'}}>
  <ReactBootStrap.Card.Img variant="top" src="https://ei.marketwatch.com/Multimedia/2015/09/21/Photos/ZQ/MW-DU756_Stock_20150921172954_ZQ.jpg?uuid=e6db074c-60a7-11e5-98d7-0015c588e0f6" />
  <ReactBootStrap.Card.Body>
    <ReactBootStrap.Card.Title>Realized Profit/Loss</ReactBootStrap.Card.Title>
    <ReactBootStrap.Card.Text>
      See the realised profit/loss for each dealer.
    </ReactBootStrap.Card.Text>
    <ReactBootStrap.Button variant="dark" bg="dark">Check it out!</ReactBootStrap.Button>
  </ReactBootStrap.Card.Body>
</ReactBootStrap.Card>

<ReactBootStrap.Card style={{ width: '18rem', margin:'10px'}}>
  <ReactBootStrap.Card.Img variant="top" src="https://ei.marketwatch.com/Multimedia/2015/09/21/Photos/ZQ/MW-DU756_Stock_20150921172954_ZQ.jpg?uuid=e6db074c-60a7-11e5-98d7-0015c588e0f6" />
  <ReactBootStrap.Card.Body>
    <ReactBootStrap.Card.Title>Effective Profit/Loss</ReactBootStrap.Card.Title>
    <ReactBootStrap.Card.Text>
      See the effective profit/loss for each dealer.
    </ReactBootStrap.Card.Text>
    <ReactBootStrap.Button variant="dark" bg="dark">Check it out!</ReactBootStrap.Button>
  </ReactBootStrap.Card.Body>
</ReactBootStrap.Card>
</div>
    </div>
  );
}

export default App;
