with open("files/index.html", "r") as f:
    content = f.read()

old_js = """                function rotateTo(index) {
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
                }"""

new_js = """                function rotateTo(index) {
                    if (ring) ring.classList.add("paused");
                    clearInterval(autoRotateInterval);
                    // Calculate angle to bring this slot to the top (0deg = top)
                    // Each slot is 40deg apart. Top is 0deg (or 360, 720, etc)
                    var targetAngle = -1 * (index * 40) % 360;
                    if (ring) {
                        // Get current rotation if possible, or just set
                        ring.style.animation = "none";
                        ring.style.transform = "translate(-50%, -50%) rotate(" + targetAngle + "deg)";
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
                }"""

if old_js in content:
    content = content.replace(old_js, new_js)
    with open("files/index.html", "w") as f:
        f.write(content)
    print("Fixed JS rotation")
else:
    print("Could not find JS to fix")
