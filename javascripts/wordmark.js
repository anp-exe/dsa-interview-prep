/* Paint the "anna" brand text one letter per Google colour.
   Runs on first load and again after every instant-navigation swap. */
(function () {
  var CLASSES = ["wm-b", "wm-r", "wm-y", "wm-g"];

  function colour(text) {
    var frag = document.createDocumentFragment();
    text.split("").forEach(function (ch, i) {
      var span = document.createElement("span");
      span.className = CLASSES[i % CLASSES.length];
      span.textContent = ch;
      frag.appendChild(span);
    });
    return frag;
  }

  /* header brand: the site name sits in its own <span class="md-ellipsis"> */
  function paintElement(el) {
    if (!el || el.dataset.wm === "done") return;
    var text = el.textContent.trim();
    if (!text) return;
    el.dataset.wm = "done";
    el.classList.add("wordmark");
    el.textContent = "";
    el.appendChild(colour(text));
  }

  /* sidebar title: the site name is a bare text node next to the logo link */
  function paintTextNode(parent) {
    if (!parent || parent.dataset.wm === "done") return;
    var node = null;
    for (var i = parent.childNodes.length - 1; i >= 0; i--) {
      var n = parent.childNodes[i];
      if (n.nodeType === 3 && n.textContent.trim()) { node = n; break; }
    }
    if (!node) return;
    parent.dataset.wm = "done";
    parent.classList.add("wordmark");
    var wrap = document.createElement("span");
    wrap.appendChild(colour(node.textContent.trim()));
    node.parentNode.replaceChild(wrap, node);
  }

  function run() {
    paintElement(document.querySelector(".md-header__topic:first-child .md-ellipsis"));
    paintTextNode(document.querySelector(".md-nav--primary > .md-nav__title"));
  }

  /* first load: document$ does not replay to late subscribers, so call run directly */
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", run);
  } else {
    run();
  }

  /* and again after each instant-navigation page swap */
  if (typeof document$ !== "undefined" && document$.subscribe) {
    document$.subscribe(run);
  }
})();
