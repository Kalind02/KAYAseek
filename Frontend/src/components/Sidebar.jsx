import { Link } from "react-router-dom";

const Sidebar = ({ isOpen, onClose }) => {
  return (
    <div>
      {/* Overlay for closing sidebar when clicking outside */}
      {isOpen && (
        <div
          className="fixed inset-0 bg-black bg-opacity-50 z-40"
          onClick={onClose}
        ></div>
      )}

      {/* Sidebar Panel */}
      <div
        className={`fixed left-0 top-0 h-full bg-gray-900 text-white p-5 space-y-4 transition-transform duration-300 z-50 
          ${isOpen ? "translate-x-0 w-64" : "-translate-x-full"}`}
      >
        {/* Close Button */}
        <button onClick={onClose} className="text-white text-2xl">
          ✖
        </button>

        {/* Sidebar Links */}
        <nav className="mt-6">
          <Link to="/dashboard" className="block py-2 px-4 hover:bg-gray-700 rounded-md">
            Dashboard
          </Link>
          <Link to="/jobs" className="block py-2 px-4 hover:bg-gray-700 rounded-md">
            Jobs
          </Link>
          <Link to="/applications" className="block py-2 px-4 hover:bg-gray-700 rounded-md">
            Applications
          </Link>
        </nav>
      </div>
    </div>
  );
};

export default Sidebar;
