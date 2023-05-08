import React from 'react'
import { Link } from 'react-router-dom'
import AimWhite from '../Images/AimWhite.png'

export default function NavBar() {
    return (
        <div>
            <header className='nav'>
                <div className="logo">
                    <img src={AimWhite} alt="" />
                </div>
                <div className="items">
                    <Link to="/profilecomplete">Student Data </Link>
                    <Link to="/profilemgmt">Profile</Link>
                    <Link to="/sign-up">Sign Up</Link>
                    <Link to="/login">Login</Link>
                </div>
            </header>
        </div>
    )
}
