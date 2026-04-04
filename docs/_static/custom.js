/**
 * Custom JS to handle foldable "Game Methodology" sections.
 */

document.addEventListener("DOMContentLoaded", function () {
    const methodologyBlocks = document.querySelectorAll(".deemphasized.container");
    if (methodologyBlocks.length === 0) return;

    // Create the global toggle icon button
    const iconContainer = document.querySelector(".content-icon-container");
    if (iconContainer) {
        const toggleWrapper = document.createElement("div");
        toggleWrapper.className = "methodology-toggle-container";
        
        const globalBtn = document.createElement("button");
        globalBtn.className = "methodology-btn global-icon";
        globalBtn.title = "Toggle all Game Methodology notes";
        globalBtn.setAttribute("aria-label", "Toggle all Game Methodology notes");
        
        // Use a "Book" icon SVG
        globalBtn.innerHTML = `
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-book">
                <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path>
                <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path>
            </svg>`;
        
        let allExpanded = false;
        // globalBtn.classList.add("active"); // Removed: Active now represents "all expanded"
        globalBtn.addEventListener("click", () => {
            allExpanded = !allExpanded;
            methodologyBlocks.forEach(block => {
                const content = block.querySelector(".methodology-content");
                const localBtn = block.querySelector(".methodology-btn.local");
                const isCollapsed = content.classList.contains("collapsed");
                
                // If the state doesn't match the desired global state, toggle it
                if (allExpanded === isCollapsed) {
                    content.classList.toggle("collapsed");
                    if (localBtn) {
                        localBtn.innerText = content.classList.contains("collapsed") ? "Show" : "Hide";
                    }
                }
            });
            globalBtn.classList.toggle("active", allExpanded);
        });

        toggleWrapper.appendChild(globalBtn);
        // Prepend to the icon container
        iconContainer.insertBefore(toggleWrapper, iconContainer.firstChild);
    }

    // Process each methodology block
    methodologyBlocks.forEach(block => {
        // Assume the first child (often a bold paragraph) is the header
        const headerElement = block.firstElementChild;
        if (!headerElement) return;

        // Wrap remaining children in a content div
        const contentDiv = document.createElement("div");
        contentDiv.className = "methodology-content collapsed";
        
        while (block.children.length > 1) {
            contentDiv.appendChild(block.children[1]);
        }
        block.appendChild(contentDiv);

        // Add local toggle button to the header
        const localBtn = document.createElement("button");
        localBtn.innerText = "Show";
        localBtn.className = "methodology-btn local";
        
        localBtn.addEventListener("click", () => {
            contentDiv.classList.toggle("collapsed");
            localBtn.innerText = contentDiv.classList.contains("collapsed") ? "Show" : "Hide";
        });

        // If the header is a paragraph, append the button there
        if (headerElement.tagName === "P") {
            headerElement.appendChild(document.createTextNode(" "));
            headerElement.appendChild(localBtn);
        } else {
            // Otherwise create a wrapper for the header
            const headerWrapper = document.createElement("div");
            headerWrapper.className = "methodology-header";
            headerWrapper.appendChild(headerElement.cloneNode(true));
            headerWrapper.appendChild(localBtn);
            block.replaceChild(headerWrapper, headerElement);
        }
    });
});
