import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faSpider, faBug, faPastafarianism } from '@fortawesome/free-solid-svg-icons'
import Select from 'react-select';
import './App.css';

class App extends React.Component{
  constructor(props) {
    super(props);
    this.state = {
      color1: "red",
      color2: "red",
      color3: "blue",
      response: "",
      data: []
    }
  }


  render(){
    const element = <FontAwesomeIcon icon={faSpider} size="6x" color={this.state.color1}/>
    const element2 = <FontAwesomeIcon icon={faBug} size="6x" color={this.state.color2}/>
    const element3 = <FontAwesomeIcon icon={faPastafarianism } size="6x" color={this.state.color3}/>
    let handleChange = (selectedOption) => {
      this.setState({color1: selectedOption.value})
      console.log(`Option selected:`, selectedOption);
    };
    let handleChange2 = (selectedOption) => {
      this.setState({color2: selectedOption.value})
      console.log(`Option selected:`, selectedOption);
    };
    let handleChange3 = (selectedOption) => {
      this.setState({color3: selectedOption.value})
      console.log(`Option selected:`, selectedOption);
    };
    let response = () =>{
      let num = Math.floor(Math.random() * 6) + 1
      console.log(num)
      switch(num){
        case 1:
          this.setState({response: "Horrible. You should be ashamed of yourself."})
          break;
        case 2:
          this.setState({response: "Great work! I think it's beautiful!"})
          break;
        case 3:
          this.setState({response: "I don't like the colors, but I like the way they match."})
          break;
        case 4:
          this.setState({response: "I don't have time to worry about the colors you just picked. My car is on Fire! Ahhhhhhhhhh!"})
          break;
        case 5:
          this.setState({response: "Woah! It's georgous!"})
          break;
        default:
          this.setState({response: "This is humiliating to me. I could never pick such lovely colors. By being so good at picking colors, you have shamed not only me but my wife as well, because she clearly could have picked a better partner."})
      }
    }
  const colors = [
    { label: "Red", value: "red" },
    { label: "Green", value: "green" },
    { label: "Blue", value: "blue" },
    { label: "Yellow", value: "yellow" },
    { label: "Pink", value: "pink" },
    { label: "HotPink", value: "hotpink" },
    { label: "Purple", value: "purple" },
    { label: "Grey", value: "grey" },
    { label: "Black", value: "black" },
    { label: "Champagne", value: "#F7E7CE"}
  ];
  const colors2 = [
    { label: "Orange", value: "orange" },
    { label: "Gold", value: "gold" },
    { label: "Silver", value: "silver" },
    { label: "Brown", value: "brown" },
    { label: "Turquoise", value: "#40E0D0" },
    { label: "Teal", value: "teal" },
    { label: "Salmon", value: "salmon" },
    { label: "Plum", value: "plum" },
    { label: "Olive", value: "olive" },
    { label: "Periwinkle", value: "#CCCCFF" },
  ];
  const colors3 = [
    { label: "Sea Weed Green", value: "#7faa44" },
    { label: "Baby Poop Green", value: "#8a9b00" },
    { label: "Bright Sea Green", value: "#05ffa6" },
    { label: "Greenish Cyan", value: "#2afeb7" },
    { label: "Turquoise", value: "#40E0D0" },
    { label: "Greenish Brown", value: "#696112" },
    { label: "Ultramarine Blue", value: "#1805db" },
    { label: "Dark Indigo", value: "#1f0954" },
    { label: "Eggplant", value: "#380835" },
    { label: "Light Eggplant", value: "#894585" },
    { label: "Light Neon Green", value: "#4efd54" },
    { label: "Maroon", value: "#650021" },
    { label: "Bright Lime Green", value: "#65fe08" },
    { label: "Poop Brown", value: "#7a5901" },
  ];
    return (
      <div className="App">
        <body>
          <div>
            <h1>Welcome to Alice and Hazel's Bug App!</h1>
            <Select 
              options={ colors } 
              onChange={handleChange}/>
            {element}
            <Select 
              options={ colors2 } 
              onChange={handleChange2}/>
            {element2}
            <Select 
              options={ colors3 } 
              onChange={handleChange3}/>
            {element3}
          </div>
            <button style={{height:"14px;",background:"blue;",color:"blue;"}}onClick={response}>Is this a good color combination?</button>
            <p>{this.state.response}</p>
        </body>
      </div>
    );
  }  

}

export default App;
