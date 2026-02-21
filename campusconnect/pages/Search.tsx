
import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { studentApi } from '../services/api';
import { Student } from '../types';

const Search: React.FC = () => {
  const [regNo, setRegNo] = useState('');
  const [student, setStudent] = useState<Student | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem('access_token');
    if (!token) {
      navigate('/login');
    }
  }, [navigate]);

  const handleSearch = async (e: React.FormEvent) => {
    e.preventDefault();
    const token = localStorage.getItem('access_token');
    if (!token) {
      navigate('/login');
      return;
    }

    if (!regNo.trim()) return;

    setIsLoading(true);
    setError('');
    setStudent(null);

    try {
      const data = await studentApi.getDetails(regNo.trim(), token);
      setStudent(data);
    } catch (err: any) {
      setError(err.response?.status === 404 ? 'Student not found.' : 'Failed to fetch student details. Please try again.');
      if (err.response?.status === 401) {
        localStorage.removeItem('access_token');
        navigate('/login');
      }
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="max-w-4xl mx-auto px-4 py-12">
      <div className="text-center mb-12">
        <h1 className="text-4xl font-extrabold text-slate-900 mb-4">Student Search</h1>
        <p className="text-slate-600">Enter a register number to retrieve comprehensive student profile and performance data.</p>
      </div>

      <div className="glass p-6 rounded-3xl mb-12 shadow-sm">
        <form onSubmit={handleSearch} className="flex flex-col sm:flex-row gap-4">
          <div className="flex-grow relative">
            <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 absolute left-4 top-1/2 -translate-y-1/2 text-slate-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
            </svg>
            <input 
              type="text"
              value={regNo}
              onChange={(e) => setRegNo(e.target.value)}
              placeholder="Enter Register Number (e.g., 22CS101)"
              className="w-full pl-12 pr-4 py-4 rounded-2xl border border-slate-200 focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none transition-all placeholder:text-slate-300 text-lg"
            />
          </div>
          <button 
            type="submit"
            disabled={isLoading || !regNo.trim()}
            className="sm:w-auto w-full px-10 py-4 bg-indigo-600 text-white rounded-2xl font-bold hover:bg-indigo-700 shadow-lg shadow-indigo-100 disabled:opacity-50 transition-all flex items-center justify-center gap-2"
          >
            {isLoading ? 'Searching...' : 'Search'}
          </button>
        </form>

        {error && (
          <div className="mt-6 p-4 bg-amber-50 border border-amber-100 text-amber-700 rounded-xl text-center font-medium">
            {error}
          </div>
        )}
      </div>

      {student && (
        <div className="animate-in fade-in slide-in-from-bottom-4 duration-500">
          <div className="bg-white rounded-[2.5rem] shadow-xl border border-slate-100 overflow-hidden">
            <div className="bg-gradient-to-r from-indigo-600 to-violet-600 px-8 py-10 text-white relative">
              <div className="relative z-10 flex flex-col md:flex-row md:items-center justify-between gap-6">
                <div>
                  <h2 className="text-4xl font-bold mb-1">{student.name}</h2>
                  <p className="text-indigo-100 text-lg opacity-90">{student.class} • Reg: {student.reg_no}</p>
                </div>
                <div className="flex gap-4">
                  <div className="bg-white/20 backdrop-blur-md px-4 py-2 rounded-2xl text-center">
                    <p className="text-xs font-bold uppercase tracking-wider opacity-70 mb-1">CGPA</p>
                    <p className="text-2xl font-black">{student.cgpa}</p>
                  </div>
                  <div className="bg-white/20 backdrop-blur-md px-4 py-2 rounded-2xl text-center">
                    <p className="text-xs font-bold uppercase tracking-wider opacity-70 mb-1">Arrears</p>
                    <p className="text-2xl font-black">{student.current_arrear}</p>
                  </div>
                </div>
              </div>
              <div className="absolute top-0 right-0 p-8 opacity-10">
                <svg className="w-32 h-32" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M12 2L1 7l11 5 11-5-11-5zM2 17l10 5 10-5M2 12l10 5 10-5" />
                </svg>
              </div>
            </div>
            
            <div className="p-8 md:p-10 grid grid-cols-1 md:grid-cols-2 gap-8">
              <section className="space-y-6">
                <h3 className="text-xl font-bold text-slate-900 border-b border-slate-100 pb-2">Student Information</h3>
                <div className="grid grid-cols-2 gap-6">
                  <div>
                    <p className="text-xs font-bold text-slate-400 uppercase tracking-widest mb-1">Blood Group</p>
                    <p className="text-slate-900 font-semibold text-lg">{student.blood_group}</p>
                  </div>
                  <div>
                    <p className="text-xs font-bold text-slate-400 uppercase tracking-widest mb-1">Contact Number</p>
                    <p className="text-slate-900 font-semibold text-lg">{student.mobile_number}</p>
                  </div>
                </div>
              </section>

              <section className="space-y-6">
                <h3 className="text-xl font-bold text-slate-900 border-b border-slate-100 pb-2">Guardian Details</h3>
                <div className="grid grid-cols-2 gap-6">
                  <div>
                    <p className="text-xs font-bold text-slate-400 uppercase tracking-widest mb-1">Parent Name</p>
                    <p className="text-slate-900 font-semibold text-lg">{student.parent_name}</p>
                  </div>
                  <div>
                    <p className="text-xs font-bold text-slate-400 uppercase tracking-widest mb-1">Parent Contact</p>
                    <p className="text-slate-900 font-semibold text-lg">{student.parent_number}</p>
                  </div>
                </div>
              </section>
            </div>

            <div className="bg-slate-50 p-6 flex justify-center gap-4">
              <button className="flex-1 max-w-[200px] py-3 bg-white text-slate-700 border border-slate-200 rounded-xl font-bold hover:bg-slate-100 transition-colors">
                Remarks
              </button>
              <button className="flex-1 max-w-[200px] py-3 bg-indigo-50 text-indigo-600 rounded-xl font-bold hover:bg-indigo-100 transition-colors">
                Good
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default Search;
