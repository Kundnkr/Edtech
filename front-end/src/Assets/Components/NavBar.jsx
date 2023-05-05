import React from 'react'
import { Link } from 'react-router-dom'

export default function NavBar() {
    return (
        <div>
            <header className='nav'>
                <div className="logo">
                    <Link to="/">Logo</Link>
                </div>
                <div className="items">
                    <Link to="/profilecomplete">Student Data </Link>
                    <Link to="/profilemgmt">Profile</Link>
                    <Link to="/sign-up">Sign Up</Link>
                    <Link to="/otp-verify">OTP-page</Link>
                    <Link to="/login">Login</Link>
                    <Link to="/change_password">Change Password</Link>
                </div>
            </header>
        </div>
    )
}
