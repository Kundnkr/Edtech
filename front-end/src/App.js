import './App.css';
import EmailVerify from './Assets/Components/EmailVerify';
import Register from './Assets/Components/Register';
import Login from './Assets/Components/Login';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import ResetPass from './Assets/Components/ResetPass';
import ForgetPass from './Assets/Components/ForgetPass';
import NavBar from './Assets/Components/NavBar';
import Home from './Assets/Components/Home';
import StudentProfile from './Assets/Components/StudentProfile';
import ProfileManagement from './Assets/Components/ProfileManagement';

function App() {
  return (
    <Router>
      <NavBar/>
      <Routes>
        <Route path= '/' element = {<Home/>} ></Route>
        <Route path= '/profilecomplete' element = {<StudentProfile/>} ></Route>
        <Route path= '/profileMgmt' element = {<ProfileManagement/>} ></Route>
        <Route path='/sign-up' element={<Register />} ></Route>
        <Route path='/otp-verify' element={<EmailVerify />} ></Route>
        <Route path='/login' element={<Login/>} ></Route>
        <Route path='/change_password' element={<ResetPass/>} ></Route>
        <Route path='/forget_password' element={<ForgetPass/>} ></Route>
      </Routes>
    </Router>
  );
}

export default App;
