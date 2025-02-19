const JobCard = ({ job }) => {
    return (
      <li className="border p-4 mb-4 rounded-lg shadow-md">
        <a
          href={`https://internshala.com${job.job_detail}`}
          target="_blank"
          rel="noopener noreferrer"
          className="text-blue-500 hover:underline"
        >
          <h3 className="text-xl font-semibold">{job.title}</h3>
          <p className="text-gray-600">
            {job.company} - {job.location}
          </p>
        </a>
      </li>
    );
  };
  
  export default JobCard;