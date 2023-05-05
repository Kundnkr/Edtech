import React, { useState } from 'react'
import '../Stylesheet/ResetPass.css'
import forget from '../Images/forget.png'

export default function ResetPass() {
    let [password, setpassword] = useState({
        old_password: "",
        confirm_password: ""
    })

    let chnagehandler = (e) => {
        let value = e.target.value;
        setpassword({ ...password, [e.target.name]: value })
    }
    let submithandler = (e) => {

    }
    return (
        <>
            <div className="change_password">
                <div>
                    <img src={forget} alt="" />
                    <h1>Change Password</h1>
                    
                </div>
                <form onSubmit={submithandler}>
                    <input type="password" placeholder='Old Password' onChange={chnagehandler} name='old_password' />
                    <input type="password" placeholder='New Password' onChange={chnagehandler} name='confirm_password' />
                    <button>Update Password</button>
                </form>

            </div>
        </>
    )
}
