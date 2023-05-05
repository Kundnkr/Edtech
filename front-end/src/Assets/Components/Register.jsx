import React from 'react'
import { useState } from 'react'
import axios from 'axios'
import '../Stylesheet/Regsiter.css';
import AIM from '../Images/AIM.png'
import { useNavigate } from 'react-router-dom';

let email = "";

export default function Register() {
    const Navigate = useNavigate();
    const [data, setdata] = useState({
        username: "",
        first_name: "",
        last_name: "",
        email: "",
        phone: "",
        password: "",
        confirm_password: ""
    })

    let handlechange = (e) => {
        const value = e.target.value;
        setdata({ ...data, [e.target.name]: value });
    }

    let handlesubmit = (e) => {

        e.preventDefault();
        const userdata = {
            username: data.username,
            first_name: data.first_name,
            last_name: data.last_name,
            email: data.email,
            phone: data.phone,
            password:data.password,
            confirm_password:data.confirm_password
        }
        
        email = data.email;
        axios.post('https://testapp-9prn.onrender.com/api/register/', userdata).then((res) => {
            let registrationForm = document.getElementById('form');
            alert(res.data.msg);
            if(res.data.status===200){
                Navigate('/otp-verify');
            }
            registrationForm.reset();
        }).catch((err) => {
            console.log(err
            );
        })
    }



    return (
        <>
            <section className="registration-box">
                <div className="content">
                    <div className="disc">
                        <h1>Registration page</h1>
                    </div>
                </div>
                <div id='registration-from' onSubmit={handlesubmit} >
                    <div className="img">
                    <img src={AIM} alt="" />
                    </div>
                    <form id='form' className="form-item">
                
                        <input required type="text" name='username' id='username' placeholder='Username' onChange={handlechange} />
                        
                       
                        <input required type="text" name="first_name" id="first_name" placeholder='First Name' onChange={handlechange} />

                        
                        <input required type="text" name='last_name' placeholder='Last Name' onChange={handlechange} />

                        
                        <input required type="email" name='email' placeholder='Email' onChange={handlechange} />

                        
                        <input required type="tel" name='phone' placeholder='Mobile' onChange={handlechange} />

                        
                        <input required type="password" name='password' placeholder='Password' onChange={handlechange}/>

                        
                        <input required type="password" name='confirm_password' placeholder='Confirm Password' onChange={handlechange}/>
                        <button>REGISTER</button>
                    </form>
                </div>
            </section>
        </>
    )
}

export {email};