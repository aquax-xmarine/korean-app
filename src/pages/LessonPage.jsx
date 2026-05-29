import AudioSection from "../components/AudioSection";
import LessonReviewSection from "../components/LessonReviewSection";

function LessonPage() {
  return (
    <div className="lesson-page">
      <h1>Lesson 1 - Greetings</h1>

      <div className="lesson-layout">
        <AudioSection />
        <LessonReviewSection />
      </div>
    </div>
  );
}

export default LessonPage;