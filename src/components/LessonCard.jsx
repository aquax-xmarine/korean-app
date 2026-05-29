import { useNavigate } from "react-router-dom";

function LessonCard({ image, title, id }) {
  const navigate = useNavigate();

  const handleClick = () => {
    if (id === 1) {
      navigate("/lesson/1");
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
