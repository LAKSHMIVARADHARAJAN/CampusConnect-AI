
import React from 'react';
import { HashRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import Chatbot from './pages/Chatbot';
import Login from './pages/Login';
import Search from './pages/Search';

const App: React.FC = () => {
  return (
    <Router>
      <div className="min-h-screen bg-[#f8fafc]">
        <Navbar />
        <main className="transition-all duration-300">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/chatbot" element={<Chatbot />} />
            <Route path="/login" element={<Login />} />
            <Route path="/search" element={<Search />} />
          </Routes>
        </main>
        
        {/* Simple Footer */}
        <footer className="py-8 text-center text-slate-400 text-sm border-t border-slate-100 mt-12">
          &copy; {new Date().getFullYear()} CampusConnect. All rights reserved.
        </footer>
      </div>
    </Router>
  );
};

export default App;
