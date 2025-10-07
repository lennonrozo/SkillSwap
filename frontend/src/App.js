import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Home from './components/Home';
import Profile from './components/Profile';
import Match from './components/Match';
import Review from './components/Review';

function App() {
    return (
        <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/profile" element={<Profile />} />
            <Route path="/match" element={<Match />} />
            <Route path="/review" element={<Review />} />
        </Routes>
    );
}

export default App;