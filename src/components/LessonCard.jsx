import { useNavigate } from "react-router-dom";

function LessonCard({ image, title, id, language }) {
  const navigate = useNavigate();

  const handleClick = () => {
    if (id === 1) {
      navigate(`/lesson/${language}/1`);
    }
    if (id === 2) {
      navigate(`/lesson/${language}/2`);
    }
    if (id === 3) {
      navigate(`/lesson/${language}/3`);
    }
  };

  return (
    <div className="lesson-card" onClick={handleClick}>
      {image && <img src={image} alt={title} />}
      {title && <p>{title}</p>}
    </div>
  );
}

export default LessonCard;
