import { useEffect, useState } from "react";
import { fetchJobs } from "../services/jobApi";
import JobCard from "../components/JobCard";

function Jobs() {
  const [jobs, setJobs] = useState([]);
  const [filters, setFilters] = useState({ company: "", location: "" });
  const [page, setPage] = useState(1);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const limit = 10;

  useEffect(() => {
    setLoading(true);
    setError(null);

    const delayFetch = setTimeout(() => {
      fetchJobs(filters, page, limit)
        .then(setJobs)
        .catch(() => setError("Failed to load jobs"))
        .finally(() => setLoading(false));
    }, 500); // 500ms debounce to avoid too many API calls

    return () => clearTimeout(delayFetch);
  }, [filters, page]);

  return (
    <div className="p-6 bg-white rounded-lg shadow-md m-6 text-black">
      <h2 className="text-3xl font-bold mb-4">Job Listings</h2>

      {/* Filters */}
      <div className="mb-4 flex space-x-4">
        <input
          type="text"
          placeholder="Company"
          value={filters.company}
          onChange={(e) => setFilters({ ...filters, company: e.target.value })}
          className="border p-2 rounded-md w-full"
        />
        <input
          type="text"
          placeholder="Location"
          value={filters.location}
          onChange={(e) => setFilters({ ...filters, location: e.target.value })}
          className="border p-2 rounded-md w-full"
        />
      </div>

      {/* Loading Indicator */}
      {loading && <p className="text-gray-500">Loading jobs...</p>}
      
      {/* Error Message */}
      {error && <p className="text-red-500">{error}</p>}

      {/* Job Listings */}
      <ul>
        {jobs.length > 0 ? (
            jobs.map((job, index) => <JobCard key={index} job={job} />)
          ) : (
            !loading && <p>No jobs found.</p>
          )}
      </ul>

      {/* Pagination */}
      <div className="mt-4 flex justify-between">
        <button
          onClick={() => setPage(page - 1)}
          disabled={page === 1}
          className="bg-blue-500 text-white p-2 rounded-md disabled:bg-gray-300"
        >
          Previous
        </button>

        <button
          onClick={() => setPage(page + 1)}
          className="bg-blue-500 text-white p-2 rounded-md"
        >
          Next
        </button>
      </div>
    </div>
  );
}

export default Jobs;
