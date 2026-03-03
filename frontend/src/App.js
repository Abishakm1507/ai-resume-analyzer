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
      console.error(error);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 p-10">
      <div className="max-w-4xl mx-auto bg-white p-8 rounded-2xl shadow-lg">
        <h1 className="text-3xl font-bold mb-6 text-center">
          AI Resume Analyzer
        </h1>

        <form onSubmit={handleSubmit} className="space-y-6">
          <div>
            <label className="font-semibold">Upload Resume (PDF)</label>
            <input
              type="file"
              accept=".pdf"
              onChange={(e) => setResume(e.target.files[0])}
              className="mt-2 block w-full border p-2 rounded"
              required
            />
          </div>

          <div>
            <label className="font-semibold">Job Description</label>
            <textarea
              rows="5"
              value={jobDescription}
              onChange={(e) => setJobDescription(e.target.value)}
              className="mt-2 block w-full border p-2 rounded"
              required
            />
          </div>

          <button
            type="submit"
            className="w-full bg-blue-600 text-white py-2 rounded-xl hover:bg-blue-700 transition"
          >
            Analyze Resume
          </button>
        </form>

        {result && (
          <div className="mt-10 space-y-6">
            <div>
              <h2 className="text-xl font-semibold">ATS Score</h2>
              <div className="w-full bg-gray-200 rounded-full h-6 mt-2">
                <div
                  className="bg-green-500 h-6 rounded-full text-center text-white text-sm"
                  style={{ width: `${result.ats_score}%` }}
                >
                  {result.ats_score}%
                </div>
              </div>
            </div>

            <div>
              <h2 className="text-xl font-semibold">Skill Match</h2>
              <p className="text-lg">{result.skill_match_percentage}%</p>
            </div>

            <div>
              <h2 className="text-xl font-semibold">Missing Skills</h2>
              <ul className="list-disc list-inside text-red-500">
                {result.missing_skills.map((skill, index) => (
                  <li key={index}>{skill}</li>
                ))}
              </ul>
            </div>

            <div>
              <h2 className="text-xl font-semibold">Suggestions</h2>
              <ul className="list-disc list-inside text-blue-600">
                {result.suggestions.map((suggestion, index) => (
                  <li key={index}>{suggestion}</li>
                ))}
              </ul>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;