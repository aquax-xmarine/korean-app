import greetingsImage from "../assets/greetings.avif";

function AudioSection() {
  return (
    <div className="audio-section">
      <img
        src={greetingsImage}
        alt="Lesson"
        className="lesson-image"
      />

      <audio controls className="audio-player">
        <source src="/topic1_lesson.mp3" type="audio/mpeg" />
      </audio>
    </div>
  );
}

export default AudioSection;