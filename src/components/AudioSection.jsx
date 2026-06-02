function AudioSection({ language, lessonId }) {
  const imagePath = `/assets/${language}/lesson${lessonId}.avif`;
  const audioPath = `/assets/audio/${language}/lesson${lessonId}.mp3`;

  return (
    <div className="audio-section">
      <img
        src={imagePath}
        alt="Lesson"
        className="lesson-image"
      />

      <audio controls className="audio-player">
        <source src={audioPath} type="audio/mpeg" />
      </audio>
    </div>
  );
}

export default AudioSection;