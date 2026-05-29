import LessonCard from "../components/LessonCard";

const lessons = [
  { id: 1, title: "Lesson 1 - Greetings", image: "/src/assets/greetings.avif" },
  { id: 2 },
  { id: 3 },
  { id: 4 },
  { id: 5 },
  { id: 6 },
  { id: 7 },
  { id: 8 },
  { id: 9 },
  { id: 10 },

  { id: 11 },
  { id: 12 },
  { id: 13 },
  { id: 14 },
  { id: 15 },
  { id: 16 },
  { id: 17 },
  { id: 18 },
  { id: 19 },
  { id: 20 },

  { id: 21 },
  { id: 22 },
  { id: 23 },
  { id: 24 },
  { id: 25 },
  { id: 26 },
  { id: 27 },
  { id: 28 },
  { id: 29 },
  { id: 30 },
];

function Lessons() {
  return (
    <div className="lessons-page">
      <h1>Lessons</h1>
      <div className="lessons-grid">
        {lessons.map((lesson) => (
          <LessonCard
            key={lesson.id}
            image={lesson.image}
            title={lesson.title}
          />
        ))}
      </div>
    </div>
  );
}

export default Lessons;