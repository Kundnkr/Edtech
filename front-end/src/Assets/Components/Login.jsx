import '../Stylesheet/Login.css';
import React, { useState } from 'react'
import { Link } from 'react-router-dom'
import axios from 'axios'

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
                <h1>Login</h1>
                <form onSubmit={submithandler}>
                    <input type="email" name='email' placeholder='Your Email' onChange={changehandler} />
                    <input type="password" name='password' placeholder='Password' onChange={changehandler} />
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
