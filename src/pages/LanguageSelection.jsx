import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "../css/LanguageSelection.css";

function LanguageSelection() {
  const [selectedLanguage, setSelectedLanguage] = useState("");
  const navigate = useNavigate();

  const handleSelect = (language) => {
    setSelectedLanguage(language);
    console.log("Selected:", language);
  };

  const handleContinue = () => {
    if (selectedLanguage) {
      navigate(`/lessons/${selectedLanguage.toLowerCase()}`);
    }
  };

  return (
    <div className="language-page">
      <div className="language-container">
        <h1>Choose Your Language</h1>
        <p>Select the language you want to learn</p>

        <div className="language-cards">
          <div
            className={`language-card ${selectedLanguage === "Chinese" ? "selected" : ""}`}
            onClick={() => handleSelect("Chinese")}
          >
            <div className="flag">🇨🇳</div>
            <h2>Chinese</h2>
            <p>Learn Mandarin Chinese</p>
          </div>

          <div
            className={`language-card ${selectedLanguage === "Korean" ? "selected" : ""}`}
            onClick={() => handleSelect("Korean")}
          >
            <div className="flag">🇰🇷</div>
            <h2>Korean</h2>
            <p>Learn Korean</p>
          </div>
        </div>

        {selectedLanguage && (
          <button className="continue-btn" onClick={handleContinue}>
            Continue with {selectedLanguage}
          </button>
        )}
      </div>
    </div>
  );
}

export default LanguageSelection;