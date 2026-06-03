import { useRef, useState, useEffect } from "react";

function VideoSection({ video, thumbnail }) {
  const videoRef = useRef(null);
  const [isPlaying, setIsPlaying] = useState(false);
  const [isLoaded, setIsLoaded] = useState(false);
  const [isMounted, setIsMounted] = useState(false);  // ← delay video render

  useEffect(() => {
    const timer = setTimeout(() => setIsMounted(true), 500); // wait 500ms after mount
    return () => clearTimeout(timer);
  }, []);

  const handlePlay = () => {
    videoRef.current.play();
    setIsPlaying(true);
  };

  return (
    <div className="video-section">
      <div className="video-wrapper">

        {!isLoaded && (
          <img src={thumbnail} className="lesson-video" alt="" />
        )}

        {isMounted && (  // ← video only renders after delay
          <video
            ref={videoRef}
            className="lesson-video"
            controls
            preload="none"          // ← changed from "metadata" to "none"
            poster={thumbnail}
            style={{ display: isLoaded ? "block" : "none" }}
            onLoadedMetadata={() => setIsLoaded(true)}
            onPause={() => setIsPlaying(false)}
            onPlay={() => setIsPlaying(true)}
          >
            <source src={video} type="video/mp4" />
          </video>
        )}

        {!isPlaying && (
          <button className="play-overlay" onClick={handlePlay}>▶</button>
        )}

      </div>
    </div>
  );
}

export default VideoSection;