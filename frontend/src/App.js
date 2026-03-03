import React, { useState } from "react";
import axios from "axios";

function App() {
  const [resume, setResume] = useState(null);
  const [jobDescription, setJobDescription] = useState("");
  const [result, setResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append("resume", resume);
    formData.append("job_description", jobDescription);

    try {
      const response = await axios.post(
        "http://127.0.0.1:5000/analyze",
        formData
      );

      setResult(response.data);
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <div style={{ padding: "40px", fontFamily: "Arial" }}>
      <h1>AI Resume Analyzer</h1>

      <form onSubmit={handleSubmit}>
        <div>
          <label>Upload Resume (PDF):</label><br />
          <input
            type="file"
            accept=".pdf"
            onChange={(e) => setResume(e.target.files[0])}
            required
          />
        </div>

        <br />

        <div>
          <label>Paste Job Description:</label><br />
          <textarea
            rows="6"
            cols="60"
            value={jobDescription}
            onChange={(e) => setJobDescription(e.target.value)}
            required
          />
        </div>

        <br />

        <button type="submit">Analyze Resume</button>
      </form>

      {result && (
        <div style={{ marginTop: "30px" }}>
          <h2>Analysis Result</h2>
          <p><strong>ATS Score:</strong> {result.ats_score}%</p>
          <p><strong>Skill Match:</strong> {result.skill_match_percentage}%</p>

          <h3>Missing Skills</h3>
          <ul>
            {result.missing_skills.map((skill, index) => (
              <li key={index}>{skill}</li>
            ))}
          </ul>

          <h3>Suggestions</h3>
          <ul>
            {result.suggestions.map((suggestion, index) => (
              <li key={index}>{suggestion}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;