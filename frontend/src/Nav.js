import React, { useState, useEffect } from "react";

function Nav() {
  const [content, setContent] = useState("<h1>loading</h1>");

  const navigateTo = (page) => {
    window.history.pushState({ page }, "", `/${page}`);
    fetchContent(page);
  };

  const fetchContent = (page) => {
    fetch(`/api/views/${page}/`)
      .then((response) => {
        if (!response.ok) throw new Error(`${response.status}`);
        return response.json();
      })
      .then((data) => {
        setContent(data.html);
      })
      .catch((err) => {
        setContent(`<p>Error: ${err.message}</p>`);
      });
  };

  useEffect(() => {
    const initialPage = window.location.pathname.replace("/", "") || "home";
    fetchContent(initialPage);
    
    const handlePopState = (event) => {
      fetchContent(event.state?.page || "home");
    };

    window.addEventListener("popstate", handlePopState);
    
    return () => {
      window.removeEventListener("popstate", handlePopState);
    };
  }, []);

  return (
    <div>
      <nav>
        <ul>
          <li>
            <button onClick={() => navigateTo("home")}>Home</button>
          </li>
          <li>
            <button onClick={() => navigateTo("about")}>About</button>
          </li>
          <li>
            <button onClick={() => navigateTo("contact")}>Contact</button>
          </li>
        </ul>
      </nav>
      <div id="content">
        <div dangerouslySetInnerHTML={{ __html: content }} />
      </div>
    </div>
  );
}

export default Nav;
