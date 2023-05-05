import React from 'react'
import '../Stylesheet/Home.css';

export default function Home() {
  return (
    <>
      <section className="landing-page-0">
          <div className="scroll-image">
              <div className="image"></div>
              <div className="image"></div>
              <div className="image"></div>
              <div className="image"></div>
          </div>
      </section>
      <div className="courses">
        <div className="course">
          <div><img src="" alt="" /></div>
          <div className="courses-text">
          <h2>Title</h2>
          <p>Discription</p>
          </div>
        </div>
        <div className="course">
          <div><img src="" alt="" /></div>
          <div className="courses-text">
          <h2>Title</h2>
          <p>Discription</p>
          </div>
        </div>
        <div className="course">
          <div><img src="" alt="" /></div>
          <div className="courses-text">
          <h2>Title</h2>
          <p>Discription</p>
          </div>
        </div>
      </div>
    </>
  )
}
