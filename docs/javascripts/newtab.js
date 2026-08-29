function openContentLinksInNewTab() {
  const root = document.querySelector(".md-content");
  if (!root) return;

  root.querySelectorAll("a[href]").forEach((anchor) => {
    const href = anchor.getAttribute("href");
    if (!href || href.startsWith("#")) return;

    anchor.setAttribute("target", "_blank");
    anchor.setAttribute("rel", "noopener noreferrer");
  });
}

if (typeof document$ !== "undefined") {
  document$.subscribe(openContentLinksInNewTab);
} else {
  document.addEventListener("DOMContentLoaded", openContentLinksInNewTab);
}
