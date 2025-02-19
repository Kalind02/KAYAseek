import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import { useState } from "react";
import Navbar from "./components/Navbar";
import Sidebar from "./components/Sidebar";
import ApplicationForm from "./components/ApplicationForm";
import Dashboard from "./pages/Dashboard";
import Jobs from "./pages/Jobs";

function Home() {
  return (
    <div className="p-6 bg-white rounded-lg shadow-md m-6 text-black text-center">
      <h2 className="text-3xl font-bold mb-4">Welcome to KAYAseek</h2>
      <p className="text-lg">Find your dream Internship effortlessly!</p>
    </div>
  );
}

function App() {
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);

  // Function to handle form submission
  const handleApplicationSubmit = (formData) => {
    console.log("Application Submitted:", formData);
    alert("Application submitted successfully!");
  };

  return (
    <Router>
      <div className="flex bg-gray-200 min-h-screen">
        {/* Sidebar (Controlled by isSidebarOpen) */}
        <Sidebar isOpen={isSidebarOpen} onClose={() => setIsSidebarOpen(false)} />

        {/* Main Content */}
        <div className={`flex-1 transition-all duration-300`}>
          <Navbar onSidebarToggle={() => setIsSidebarOpen(!isSidebarOpen)} />

          {/* Page Content */}
          <div className="pt-16 p-6">
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/dashboard" element={<Dashboard />} />
              <Route path="/jobs" element={<Jobs />} />
              <Route path="/apply" element={<ApplicationForm onSubmit={handleApplicationSubmit} />} />
              <Route path="*" element={<Navigate to="/" />} />
            </Routes>
          </div>
        </div>
      </div>
    </Router>
  );
}

export default App;
