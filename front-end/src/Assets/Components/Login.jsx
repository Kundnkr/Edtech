import '../Stylesheet/Login.css';
import React, { useState } from 'react'
import { Link } from 'react-router-dom'
import axios from 'axios'
import loginGIF from '../Images/loginGIF.gif'

export default function Login() {


    const [user, setuser] = useState({
        email: "",
        password: ""
    })

    let changehandler = (e) => {
        let data = e.target.value;
        setuser({ ...user, [e.target.name]: data })
    }
    let submithandler = (e) => {
        e.preventDefault();
        const userdata = {
            email: user.email,
            password: user.password
        }
        axios.post('https://testapp-9prn.onrender.com/api/login/', userdata).then((res) => {
            alert(res.data.msg + " with token id :" + res.data.token);
        }).catch((err) => {
            alert("Inviled Crediential");
        })
    }
    return (
        <>
            <div className="login-page">
                <div className='side-temp'>
                    <img src={loginGIF} alt="" />
                </div>
                <form onSubmit={submithandler}>
                    <h1>Login</h1>
                    <div className="input-box">
                        <input required type="email" className='email' id='email' name='email' onChange={changehandler} />
                        <label htmlFor="email" className='emailLablel'>Your Email</label>
                    </div>
                    <div className="input-box">
                        <input required id='password' type="password" className='password' name='password' onChange={changehandler} />
                        <label htmlFor="password" className='passLablel'>Password</label>
                    </div>
                    <div className='forget-signup-link'>
                        <Link to="/sign-up">Sign Up</Link>
                        <Link to="/forget_password">Forget Password</Link>
                    </div>
                    <button>Login</button>
                </form>
            </div>

        </>
    )
}
