import '../Stylesheet/EmailVerify.css'
import {React, useEffect} from 'react'
import mail from '../Images/mail.png';
import axios from 'axios';
import {email} from './Register';
import { useNavigate} from 'react-router-dom';

export default function EmailVerify() {
    const Navigate = useNavigate();

    useEffect(() => {
        let otpInput = document.querySelector('.otpInput');
        const handleKeyPress = (event) => {
          if (event.key === "Enter") {
            event.preventDefault();
            otpInput.nextSibling();
          }
        }
    
    
        otpInput.addEventListener('keypress', handleKeyPress);
        return () => {
            otpInput.removeEventListener('keypress', handleKeyPress);
        }
      }, []);

    let filled = "";
    let ChangeHandler = (e) => {
        filled += e.target.value;
    }
    let submithandler = (e) => {
        e.preventDefault();
        const otpverify = {
            email:email,
            otp:filled
        }
        axios.post('https://testapp-9prn.onrender.com/api/verify/',otpverify).then((res)=>{
            alert(res.data.msg);
            if(res.data.status === 200){
                Navigate('/');
            }
        }).catch((err)=>{
            alert("Please Try Again");
        })
        
    }
    return (
        <>
            <div className="email-verify">
                <div className="email-verify-head">
                    <img src={mail} alt="" />
                    <h1>Verify Your Email Address</h1>
                    <p>You've entered {email} as the email address for your account <br />
                        Please verify the email address by entering the otp you recived on your mail</p>
                </div>
                <form onSubmit={submithandler} className="otp-content">
                    <div className="email-input-item">
                        <input className='otpInput' type="text" onChange={ChangeHandler} maxLength={1} />
                        <input className='otpInput' type="text" onChange={ChangeHandler} maxLength={1} />
                        <input className='otpInput' type="text" onChange={ChangeHandler} maxLength={1} />
                        <input className='otpInput' type="text" onChange={ChangeHandler} maxLength={1} />
                    </div>
                    <button type='submit'>Verify</button>
                </form>
            </div>



        </>
    )
}
