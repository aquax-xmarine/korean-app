import { Routes, Route } from "react-router-dom";

import Lessons from "./pages/Lessons";
import LessonPage from "./pages/LessonPage";
import LanguageSelection from "./pages/LanguageSelection";

function App() {
  return (
    <Routes>
      <Route path="/" element={<LanguageSelection />} />
      <Route path="/lessons/:language" element={<Lessons />} />
      <Route path="/lesson/:language/:lessonId" element={<LessonPage />} />
    </Routes>
  );
}

export default App;