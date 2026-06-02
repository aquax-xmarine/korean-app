import LessonCard from "../components/LessonCard";
import { useParams } from "react-router-dom";


const lessonData = {
  korean: [
    { id: 1, title: "Lesson 1 - Greetings", image: "/assets/korean/lesson1.avif" },
    { id: 2, title: "Lesson 2 - Numbers", image: "/assets/korean/lesson2.jpg" },
    { id: 3, title: "Lesson 3 - Advanced Numbers", image: "/assets/korean/lesson3.png" },
  ],
  chinese: [
    { id: 1, title: "Lesson 1 - Greetings", image: "/assets/chinese/lesson1.avif" },
    { id: 2, title: "Lesson 2 - Numbers", image: "/assets/chinese/lesson2.jpg" },
    { id: 3, title: "Lesson 3 - Advanced Numbers", image: "/assets/chinese/lesson3.png" },
    { id: 4, title: "Lesson 4 - Directions", image: "/assets/chinese/lesson4.avif" },
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