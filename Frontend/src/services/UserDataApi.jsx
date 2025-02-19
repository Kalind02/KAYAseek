export const submitApplication = async (formData) => {
    try {
      const response = await fetch("http://127.0.0.1:8000/submit-application/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData),
      });
  
      const data = await response.json();
      if (!response.ok) {
        throw new Error(data.detail || "Error submitting application");
      }
      
      return { success: true, message: "Application submitted successfully!" };
    } catch (error) {
      console.error("Submission error:", error);
      return { success: false, message: "Failed to submit application" };
    }
  };
  