import React, { useEffect, useState } from 'react'
// import StudentInput from './StudentInput';
import '../Stylesheet/StudentProfile.css';
import { useNavigate } from 'react-router-dom';

export default function StudentProfile() {
  const Navigate = useNavigate();
  let [studentDetails, setstudentDetails] = useState({
    name: "",
    collegeName: "",
    intrest: "",
    branch: ""
  })

  let submithandler = (e) => {
    e.preventDefault();
    console.log(studentDetails);
    Navigate('/profilemgmt')

  }

  useEffect(() => {
    let nextBtn = document.querySelector('.nextBtn');
    let profileInput = document.querySelector('.profileInput');

    const handleKeyPress = (event) => {
      if (event.key === "Enter") {
        event.preventDefault();
        nextBtn.click();
      }
    }


    profileInput.addEventListener('keypress', handleKeyPress);
    return () => {
      profileInput.removeEventListener('keypress', handleKeyPress);
    }
  }, []);

  let IncrementDisplay = () => {
    if (count === 1) {
      return (
        <div className='input-item'>
          <label htmlFor="name" >Name : </label>
          <input value={studentDetails.name} className='profileInput' onChange={handleChange} placeholder='Your name' name='name' type='text' />
          <input type='button' className='nextBtn' onClick={increemmnt} value="Next" />
        </div>
      )
    }

    else if (count === 2) {
      return (
        <div className='input-item' >
          <label htmlFor="name" >College Name :</label>
          <input value={studentDetails.collegeName} className='profileInput' onChange={handleChange} placeholder='Your college name' name='collegeName' type='text' />
          <input type='button' className='nextBtn' onClick={increemmnt} value="Next" />
        </div>
      )
    }

    else if (count === 3) {
      return (
        <div className='input-item' >
          <label htmlFor="name" >Intrest : </label>
          <input value={studentDetails.intrest} className='profileInput' onChange={handleChange} placeholder='Your intrest' name='intrest' type='text' />
          <input type='button' className='nextBtn' onClick={increemmnt} value="Next" />
        </div>

      )
    }

    else if (count === 4) {
      return (
        <div className='input-item input-item-1'>
          <label htmlFor="name" >Branch :</label>
          <input value={studentDetails.branch} className='profileInput' onChange={handleChange} placeholder='Your Branch' name='branch' type='text' />
          <input type="button" className='nextBtn' onClick={increemmnt} value="Next" />
        </div>
      )
    }

    else if (count === 5) {
      return (
        <div className='input-details-confirm' >
          <h1>Confirm Details :</h1>
          <p>Name : <span>{studentDetails.name}</span></p>
          <p>College Name : <span>{studentDetails.collegeName}</span></p>
          <p>Intrest : <span>{studentDetails.intrest}</span></p>
          <p>Branch : <span>{studentDetails.branch}</span></p>
          <input type="submit" value="Submit" />
        </div>
      )
    }
  }


  let handleChange = (e) => {
    let value = e.target.value;

    setstudentDetails({ ...studentDetails, [e.target.name]: value })

  }


  let [count, setcount] = useState(1)
  let increemmnt = (e) => {
    if (count === 5) {
      setcount(1);
    }
    else {
      setcount(count += 1);
    }
  }
  return (
    <>
      <form onSubmit={submithandler} className='studentProfile'>
        {IncrementDisplay()}
      </form>
    </>
  )
}
