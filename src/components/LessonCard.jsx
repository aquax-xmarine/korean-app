function LessonCard({ image, title }) {
  return (
    <div className="lesson-card">
      {image && <img src={image} alt={title} />}
      {title && <p>{title}</p>}
    </div>
  );
}

export default LessonCard;