import { useParams } from "react-router-dom";
import AudioSection from "../components/AudioSection";
import LessonReviewSection from "../components/LessonReviewSection";

function LessonPage() {
  const { language, lessonId } = useParams();

  const title = `${language.charAt(0).toUpperCase() + language.slice(1)} - Lesson ${lessonId}`;

  return (
    <div className="lesson-page">
      <h1>{title}</h1>

      <div className="lesson-layout">
        <AudioSection language={language} lessonId={lessonId} />
        <LessonReviewSection />
      </div>
    </div>
  );
}

export default LessonPage;