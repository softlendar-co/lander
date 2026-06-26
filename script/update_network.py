import re

with open("files/index.html", "r") as f:
    content = f.read()

# Find the last </script> before </body>
idx = content.rfind("</script>\n    </body>\n</html>")
if idx == -1:
    idx = content.rfind("</script>\n</body>\n</html>")

if idx != -1:
    new_script = """\n\n        <!-- Spinning Ring Product Network -->
        <script>
            (function () {
                "use strict";
                var ring = document.getElementById("net-ring");
                var slots = document.querySelectorAll(".net-slot");
                var cards = document.querySelectorAll(".product-detail-card");
                var autoRotateInterval;
                var currentIndex = 0;
                var total = slots.length;

                function showCard(slug) {
                    cards.forEach(function (c) {
                        c.classList.toggle("active", c.dataset.slug === slug);
                    });
                }

                function rotateTo(index) {
                    if (ring) ring.classList.add("paused");
                    clearInterval(autoRotateInterval);
                    var targetAngle = -1 * (index * 40);
                    if (ring) {
                        ring.style.animation = "none";
                        ring.style.transform = "rotate(" + targetAngle + "deg)";
                    }
                    slots.forEach(function (s, i) {
                        s.classList.toggle("active", i === index);
                    });
                    var slug = slots[index].dataset.slug;
                    showCard(slug);
                    currentIndex = index;
                }

                function resumeAuto() {
                    if (ring) {
                        ring.style.animation = "";
                        ring.style.transform = "";
                        ring.classList.remove("paused");
                    }
                    autoRotateInterval = setInterval(function () {
                        currentIndex = (currentIndex + 1) % total;
                        var slug = slots[currentIndex].dataset.slug;
                        showCard(slug);
                        slots.forEach(function (s, i) {
                            s.classList.toggle("active", i === currentIndex);
                        });
                    }, 4000);
                }

                slots.forEach(function (slot, index) {
                    slot.addEventListener("click", function () {
                        rotateTo(index);
                    });
                });

                var center = document.querySelector(".net-center");
                if (center) {
                    center.addEventListener("click", resumeAuto);
                }

                autoRotateInterval = setInterval(function () {
                    currentIndex = (currentIndex + 1) % total;
                    var slug = slots[currentIndex].dataset.slug;
                    showCard(slug);
                    slots.forEach(function (s, i) {
                        s.classList.toggle("active", i === currentIndex);
                    });
                }, 4000);
            })();
        </script>"""

    content = (
        content[: idx + len("</script>")]
        + new_script
        + content[idx + len("</script>") :]
    )

    with open("files/index.html", "w") as f:
        f.write(content)
    print("Updated successfully")
else:
    print("ERROR: Could not find insertion point")
