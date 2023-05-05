import React, {useState} from 'react'
import pass from '../Images/pass.png'
import '../Stylesheet/ResetPass.css'

export default function ForgetPass() {
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
        <img src={pass} alt="" />
        <h1>Forget Password</h1>
        
    </div>
    <form onSubmit={submithandler}>
        <input type="password" placeholder='Password' onChange={chnagehandler} name='old_password' />
        <input type="password" placeholder='Confirm Password' onChange={chnagehandler} name='confirm_password' />
        <button>Forget Password</button>
    </form>

</div>
    
    
    </>
  )
}
