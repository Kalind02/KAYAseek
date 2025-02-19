import { useState } from "react";
import { submitApplication } from "../services/UserDataApi"; // Import the API function

const ApplicationForm = () => {
  const [formData, setFormData] = useState({
    fullName: "",
    email: "",
    phone: "",
    location: "",
    linkedIn: "",
    github: "",
    profileSummary: "",
    skills: "",
    education: "",
    workExperience: "",
    certifications: "",
    projects: "",
    languages: "",
    coverLetterNotes: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const result = await submitApplication(formData);
    alert(result.message);
    if (result.success) {
      setFormData({
        fullName: "",
        email: "",
        phone: "",
        location: "",
        linkedIn: "",
        github: "",
        profileSummary: "",
        skills: "",
        education: "",
        workExperience: "",
        certifications: "",
        projects: "",
        languages: "",
        coverLetterNotes: "",
      });
    }
  };

  return (
    <form onSubmit={handleSubmit} className="bg-white p-6 rounded-lg shadow-md w-full max-w-2xl mx-auto mt-5">
      <h2 className="text-2xl font-bold mb-4">Generate ATS-Friendly Resume & Cover Letter</h2>

      <input type="text" name="fullName" placeholder="Full Name" value={formData.fullName} onChange={handleChange} required className="border p-2 w-full rounded-md mb-3" />
      <input type="email" name="email" placeholder="Email Address" value={formData.email} onChange={handleChange} required className="border p-2 w-full rounded-md mb-3" />
      <input type="text" name="phone" placeholder="Phone Number" value={formData.phone} onChange={handleChange} required className="border p-2 w-full rounded-md mb-3" />
      <input type="text" name="location" placeholder="Current Location" value={formData.location} onChange={handleChange} required className="border p-2 w-full rounded-md mb-3" />
      <input type="text" name="linkedIn" placeholder="LinkedIn Profile" value={formData.linkedIn} onChange={handleChange} className="border p-2 w-full rounded-md mb-3" />
      <input type="text" name="github" placeholder="GitHub Profile (if applicable)" value={formData.github} onChange={handleChange} className="border p-2 w-full rounded-md mb-3" />
      
      <textarea name="profileSummary" placeholder="Profile Summary" value={formData.profileSummary} onChange={handleChange} className="border p-2 w-full rounded-md mb-3" rows="2"></textarea>
      <textarea name="skills" placeholder="List Your Skills (comma separated)" value={formData.skills} onChange={handleChange} className="border p-2 w-full rounded-md mb-3" rows="2"></textarea>
      <textarea name="education" placeholder="Education Details" value={formData.education} onChange={handleChange} className="border p-2 w-full rounded-md mb-3" rows="2"></textarea>
      <textarea name="workExperience" placeholder="Work Experience" value={formData.workExperience} onChange={handleChange} className="border p-2 w-full rounded-md mb-3" rows="3"></textarea>
      <textarea name="certifications" placeholder="Certifications (if any)" value={formData.certifications} onChange={handleChange} className="border p-2 w-full rounded-md mb-3" rows="2"></textarea>
      <textarea name="projects" placeholder="Notable Projects (if any)" value={formData.projects} onChange={handleChange} className="border p-2 w-full rounded-md mb-3" rows="2"></textarea>
      <textarea name="languages" placeholder="Languages Known" value={formData.languages} onChange={handleChange} className="border p-2 w-full rounded-md mb-3" rows="2"></textarea>
      
      <textarea name="coverLetterNotes" placeholder="Cover Letter Notes (Why you're a good fit)" value={formData.coverLetterNotes} onChange={handleChange} className="border p-2 w-full rounded-md mb-3" rows="3"></textarea>

      <button type="submit" className="bg-blue-500 text-white p-2 rounded-md w-full hover:bg-blue-600 transition">
        Submit Application
      </button>
    </form>
  );
};

export default ApplicationForm;
