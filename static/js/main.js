/*
 * Minimal vanilla JS: mobile nav toggle + active-link highlighting on scroll.
 */
(function () {
    "use strict";

    var navToggle = document.getElementById("navToggle");
    var navMenu = document.getElementById("navMenu");

    if (navToggle && navMenu) {
        navToggle.addEventListener("click", function () {
            var isOpen = navMenu.classList.toggle("is-open");
            navToggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
        });

        navMenu.querySelectorAll(".nav-link").forEach(function (link) {
            link.addEventListener("click", function () {
                navMenu.classList.remove("is-open");
                navToggle.setAttribute("aria-expanded", "false");
            });
        });
    }

    var sections = document.querySelectorAll("main section[id]");
    var navLinks = document.querySelectorAll(".nav-link");

    function setActiveLink() {
        var scrollPos = window.scrollY + 120;
        var current = sections[0] ? sections[0].id : null;
        var atBottom = window.innerHeight + window.scrollY >= document.body.offsetHeight - 2;

        if (atBottom) {
            current = sections[sections.length - 1].id;
        } else {
            sections.forEach(function (section) {
                if (section.offsetTop <= scrollPos) {
                    current = section.id;
                }
            });
        }

        navLinks.forEach(function (link) {
            link.classList.toggle("active", link.getAttribute("href") === "#" + current);
        });
    }

    if (sections.length && navLinks.length) {
        window.addEventListener("scroll", setActiveLink, { passive: true });
        window.addEventListener("load", setActiveLink);
        setActiveLink();
    }
})();
