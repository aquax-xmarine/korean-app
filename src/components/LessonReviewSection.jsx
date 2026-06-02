import { useState } from "react";
import { useNavigate } from "react-router-dom";

const reviewItems = [
  {
    id: "voice-coach",
    icon: (
      <svg viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg" width="38" height="38">
        <circle cx="20" cy="20" r="20" fill="#6C63FF" opacity="0.15" />
        <circle cx="20" cy="16" r="6" fill="#6C63FF" />
        <path d="M10 32c0-5.523 4.477-10 10-10s10 4.477 10 10" stroke="#6C63FF" strokeWidth="2" strokeLinecap="round" />
      </svg>
    ),
    title: "Voice Coach",
    description: "Perfect your pronunciation and test your accuracy with Speech Recognition.",
    stats: [
      { value: "7", total: "10", label: "Phrases Mastered" },
      { value: "86", label: "Challenge Score" },
    ],
  },
  {
    id: "reading",
    icon: (
      <svg viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg" width="38" height="38">
        <circle cx="20" cy="20" r="20" fill="#6C63FF" opacity="0.15" />
        <rect x="10" y="13" width="8" height="14" rx="1" stroke="#6C63FF" strokeWidth="2" />
        <rect x="22" y="13" width="8" height="14" rx="1" stroke="#6C63FF" strokeWidth="2" />
        <line x1="12" y1="17" x2="16" y2="17" stroke="#6C63FF" strokeWidth="1.5" strokeLinecap="round" />
        <line x1="12" y1="20" x2="16" y2="20" stroke="#6C63FF" strokeWidth="1.5" strokeLinecap="round" />
        <line x1="24" y1="17" x2="28" y2="17" stroke="#6C63FF" strokeWidth="1.5" strokeLinecap="round" />
        <line x1="24" y1="20" x2="28" y2="20" stroke="#6C63FF" strokeWidth="1.5" strokeLinecap="round" />
      </svg>
    ),
    title: "Reading",
    description: "Dr. Pimsleur's phonetic approach to reading.",
  },
  {
    id: "flash-cards",
    icon: (
      <svg viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg" width="38" height="38">
        <circle cx="20" cy="20" r="20" fill="#6C63FF" opacity="0.15" />
        <rect x="11" y="13" width="18" height="14" rx="2" stroke="#6C63FF" strokeWidth="2" />
        <rect x="14" y="16" width="12" height="8" rx="1" fill="#6C63FF" opacity="0.2" stroke="#6C63FF" strokeWidth="1.5" />
      </svg>
    ),
    title: "Flash Cards",
    description: "Master essential vocabulary.",
  },
  {
    id: "quick-match",
    icon: (
      <svg viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg" width="38" height="38">
        <circle cx="20" cy="20" r="20" fill="#6C63FF" opacity="0.15" />
        <circle cx="20" cy="20" r="9" stroke="#6C63FF" strokeWidth="2" />
        <path d="M15 20l3.5 3.5L25 16" stroke="#6C63FF" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
        <circle cx="28" cy="13" r="4" fill="#FF6B6B" />
        <path d="M27 13h2M28 12v2" stroke="white" strokeWidth="1.5" strokeLinecap="round" />
      </svg>
    ),
    title: "Quick Match",
    description: "Challenge yourself with a fast quiz.",
  },
  {
    id: "speak-easy",
    icon: (
      <svg viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg" width="38" height="38">
        <circle cx="20" cy="20" r="20" fill="#6C63FF" opacity="0.15" />
        <rect x="11" y="14" width="18" height="13" rx="3" stroke="#6C63FF" strokeWidth="2" />
        <circle cx="16" cy="20" r="1.5" fill="#6C63FF" />
        <circle cx="20" cy="20" r="1.5" fill="#6C63FF" />
        <circle cx="24" cy="20" r="1.5" fill="#6C63FF" />
        <path d="M20 27v3" stroke="#6C63FF" strokeWidth="2" strokeLinecap="round" />
      </svg>
    ),
    title: "Speak Easy",
    description: "Refine your pronunciation, rhythm, cadence, and accent.",
  },
  {
    id: "speed-round",
    icon: (
      <svg viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg" width="38" height="38">
        <circle cx="20" cy="20" r="20" fill="#6C63FF" opacity="0.15" />
        <rect x="10" y="14" width="20" height="14" rx="2" stroke="#6C63FF" strokeWidth="2" />
        <path d="M14 20h5l2-3 2 6 2-3h1" stroke="#6C63FF" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round" />
        <line x1="10" y1="24" x2="30" y2="24" stroke="#6C63FF" strokeWidth="1" opacity="0.4" />
      </svg>
    ),
    title: "Speed Round",
    description: "Are you up for the challenge?",
  },
];

function StatBadge({ value, total, label }) {
  return (
    <div className="stat-badge">
      <div className="stat-badge-circle">
        {total ? (
          <span>
            {value}<span className="stat-badge-total">/{total}</span>
          </span>
        ) : (
          value
        )}
      </div>
      <span className="stat-badge-label">{label}</span>
    </div>
  );
}

function ReviewItem({ item }) {
  const [hovered, setHovered] = useState(false);

  return (
    <div
      className={`review-item${hovered ? " review-item--hovered" : ""}`}
      onMouseEnter={() => setHovered(true)}
      onMouseLeave={() => setHovered(false)}
    >
      {hovered && <div className="review-item-accent" />}
      <div className="review-item-row">
        <div className="review-item-icon">{item.icon}</div>
        <div className="review-item-text">
          <div className="review-item-title">{item.title}</div>
          <div className="review-item-description">{item.description}</div>
        </div>
        <div className={`review-item-chevron${hovered ? " review-item-chevron--visible" : ""}`}>
          <svg width="14" height="14" viewBox="0 0 16 16" fill="none">
            <path d="M6 4l4 4-4 4" stroke="#6C63FF" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
          </svg>
        </div>
      </div>
      {item.stats && (
        <div className="review-item-stats">
          {item.stats.map((stat, i) => (
            <StatBadge key={i} {...stat} />
          ))}
        </div>
      )}
    </div>
  );
}

function LessonReviewSection() {
  return (
    <div className="lesson-review-section">
      <div className="review-header">
        <div className="review-header-accent" />
        <span className="review-header-title">Review</span>
      </div>
      <div className="review-items-scroll">
        {reviewItems.map((item) => (
          <ReviewItem key={item.id} item={item} />
        ))}
      </div>
    </div>
  );
}

export default LessonReviewSection;