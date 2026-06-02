import LessonCard from "../components/LessonCard";
import { useParams } from "react-router-dom";


const lessonData = {
  korean: [
    { id: 1, title: "Lesson 1 - Greetings", image: "/src/assets/korean/lesson1.avif" },
    { id: 2, title: "Lesson 2 - Numbers" },
    { id: 3, title: "Lesson 3 - Family" },
  ],
  chinese: [
    { id: 1, title: "Lesson 1 - Greetings", image: "/src/assets/chinese/lesson1.avif" },
    { id: 2, title: "Lesson 2 - Numbers" },
    { id: 3, title: "Lesson 3 - Family" },
  ],
};

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