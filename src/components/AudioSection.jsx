function AudioSection({ image, language, lessonId }) {
  const audioPath = `/assets/audio/${language}/lesson${lessonId}.mp3`;

  return (
    <div className="audio-section">
      <img
        src={image}
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