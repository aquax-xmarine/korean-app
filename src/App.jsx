import { Routes, Route } from "react-router-dom";

import Lessons from "./pages/Lessons";
import LessonPage from "./pages/LessonPage";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Lessons />} />
      <Route path="/lesson/1" element={<LessonPage />} />
    </Routes>
  );
}

export default App;