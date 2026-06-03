function VideoSection({ video, thumbnail }) {
  return (
    <div className="video-section">
      <video
        className="lesson-video"
        controls
        preload="metadata"
        poster={thumbnail}
      >
        <source src={video} type="video/mp4" />
        Your browser does not support video playback.
      </video>
    </div>
  );
}

export default VideoSection;