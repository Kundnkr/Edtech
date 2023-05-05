import React from 'react'
import man from '../Images/man.png'
import '../Stylesheet/ProfileManagement.css'

export default function ProfileManagement() {
    let StudentDetails = {
        name: 'Kamalpreet',
        Department: "Computer Science Department",
        College: "Sant longowal Institute of engineering and technology punjab",
        Intrest: "Machine Learning",
        Courses: "Data Science",
        Semester:"8th",
        EnrolledCourse: "Backend With Django"
    }
    return (
        <>
            <div className="profile">
                <div className="container-profile">
                    <div className="student-pic">
                            <img src={man} alt="Kundan Kumar" />
                            <p>Name : {StudentDetails.name} </p>
                            <p>Semester : {StudentDetails.Semester} </p>
                    </div>
                    <div className="student-details">
                        <h2>Personal Information</h2>
                        <div className="personal-details">
                            <li>Name : {StudentDetails.name} </li>
                            <li>Department : {StudentDetails.Department} </li>
                            <li>College : {StudentDetails.College} </li>
                            <li>Intrest : {StudentDetails.Intrest} </li>
                        </div>
                        <h2>Professional Information</h2>
                        <div className="professional-details">
                            <li>Courses : {StudentDetails.Courses}</li>
                            <li>Semester : {StudentDetails.Semester}</li>
                            <li>Enrolled Courses : {StudentDetails.EnrolledCourse}</li>
                        </div>
                    </div>
                </div>
            </div>

        </>
    )
}
