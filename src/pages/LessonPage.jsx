import { useParams } from "react-router-dom";
import VideoSection from "../components/VideoSection";
import LessonReviewSection from "../components/LessonReviewSection";
import { lessonData } from "../data/lessonData";

function LessonPage() {
  const { language, lessonId } = useParams();

  const lesson = lessonData[language]?.find(
    (lesson) => lesson.id === Number(lessonId)
  );



  return (
    <div className="lesson-page">
      <h1>{lesson?.title}</h1>

      <div className="lesson-layout">
        <VideoSection
          video={`/assets/video/${language}/lesson${lesson.id}.mp4`}
          thumbnail={lesson.image}
        />
        <LessonReviewSection />
      </div>
    </div>
  );
}

export default LessonPage;