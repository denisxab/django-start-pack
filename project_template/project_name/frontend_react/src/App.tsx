import React from "react";
import './App.css'

const App: React.FunctionComponent = () => {
    return (
        <div>
            Hello React + Django + Py
            <div className="main_text">
                Стили CSS
            </div>
            <div className="container" style={{background: '#f12f'}}>
                Сетка bootstrap
                <div style={{padding: "10px", border: '3px solid #000'}}>
                    <div className="row">
                        <div className="col">1 из 2</div>
                        <div className="col">2 из 2</div>
                    </div>
                    <div className="row">
                        <div className="col">1 из 3</div>
                        <div className="col">2 из 3</div>
                        <div className="col">3 из 3</div>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default App;