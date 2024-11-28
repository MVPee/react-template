import React, { useState } from "react";

function Nav() {
  const [content, setContent] = useState("<h1>Home</h1>");

  const navigateTo = (page) => {
    fetch(`/api/views/${page}/`)
      .then((response) => {
        if (!response.ok)
          throw new Error(`${response.status}`);
        return response.json();
      })
      .then((data) => { setContent(data.html); })
      .catch((err) => {
        setContent(err);
      });
  };

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
