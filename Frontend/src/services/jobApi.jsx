export const fetchJobs = async (filters, page, limit) => {
    try {
      const response = await fetch(
        `http://127.0.0.1:8000/jobs/?company=${filters.company}&location=${filters.location}&limit=${limit}&page=${page}`
      );
      if (!response.ok) {
        throw new Error("Failed to fetch jobs");
      }
      return await response.json();
    } catch (error) {
      console.error("API error:", error);
      throw error;
    }
  };
  