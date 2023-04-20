import React, { createContext, useContext, useEffect, useState } from "react";

export const iFrameContext = createContext({
  isIFrame: false,
});

export const useIFrameContext = () => useContext(iFrameContext);

export default function Root({ children }) {
  const [isIFrame, setIsIFrame] = useState(false);
  useEffect(() => {
    setIsIFrame(window.self !== window.top);
    if (window.self !== window.top) {
      document.addEventListener("keydown", (e) => {
        if ((e.metaKey || e.ctrlKey) && e.key === "k") {
          e.preventDefault();
          e.stopPropagation();
        }
      });
    }
  }, []);
  return (
    <iFrameContext.Provider
      value={{
        isIFrame,
      }}
    >
      {children}
    </iFrameContext.Provider>
  );
}
