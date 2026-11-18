import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import { ErrorBoundary } from "./components/common/ErrorBoundary";
import "./index.css";
import "./brand.css";
import "./learning-journey.css";

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <ErrorBoundary>
      <App />
    </ErrorBoundary>
  </React.StrictMode>,
);
import "./readability.css";
import "./curriculum.css";
import "./reading-scaffold.css";
import "./progressive-reading.css";
import "./academy-demo.css";
import "./report.css";
import "./student-assessment.css";
import "./thinking-experience.css";
import "./reading-garden.css";
import "./read-x-tokens.css";
import "./read-x.css";
import "./product-ui.css";
