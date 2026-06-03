import LessonCard from "../components/LessonCard";
import { useParams } from "react-router-dom";
import { lessonData } from "../data/lessonData";



function Lessons() {
  const { language } = useParams();

  const lessons = lessonData[language] || [];

  return (
    <div className="lessons-page">
      <h1>{language.charAt(0).toUpperCase() + language.slice(1)} Lessons</h1>
      <div className="lessons-grid">
        {lessons.map((lesson) => (
          <LessonCard
            key={lesson.id}
            id={lesson.id}
            image={lesson.image}
            title={lesson.title}
            language={language}
          />
        ))}
      </div>
    </div>
  );
}

export default Lessons;