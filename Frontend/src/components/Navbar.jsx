import { Link } from "react-router-dom";

function Navbar({ onSidebarToggle }) {
  return (
    <nav className="bg-white text-black p-4 shadow-md fixed top-0 w-full z-50">
      <div className="container mx-auto flex justify-between items-center">
        {/* Sidebar Toggle Button */}
        <button className="md:hidden text-black" onClick={onSidebarToggle}>
          ☰
        </button>

        {/* Logo */}
        <Link to="/" className="text-2xl font-bold">
          KAYAseek
        </Link>

        {/* Desktop Navigation */}
        <div className="hidden md:flex space-x-6 text-lg">
          <Link to="/dashboard" className="hover:text-gray-600 transition duration-300 font-medium">
            Dashboard
          </Link>
          <Link to="/jobs" className="hover:text-gray-600 transition duration-300 font-medium">
            Jobs
          </Link>
          <Link to="/apply" className="hover:text-gray-600 transition duration-300 font-medium">
            Apply
          </Link>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
