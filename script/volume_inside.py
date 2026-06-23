# Run: python3 volume_inside.py

with open("index.html", "r") as f:
    c = f.read()

# Wrap feature card content + add bars inside
old = """<div class="context-card feature-card">
            <h2 id="head-title:feature">features:</h2>"""

new = """<div class="context-card feature-card">
    <div class="volume-bar left-bar">
        <div class="bar" style="--h:30%"></div>
        <div class="bar" style="--h:60%"></div>
        <div class="bar" style="--h:45%"></div>
        <div class="bar" style="--h:80%"></div>
        <div class="bar" style="--h:55%"></div>
        <div class="bar" style="--h:70%"></div>
        <div class="bar" style="--h:40%"></div>
        <div class="bar" style="--h:90%"></div>
    </div>
    <div class="feature-content">
        <h2 id="head-title:feature">features:</h2>"""

c = c.replace(old, new)

# Close feature-content and add right bar before closing feature-card
old2 = """            </div>

            <div class="context-card" id="new-card">"""

new2 = """            </div>
    </div>
    <div class="volume-bar right-bar">
        <div class="bar" style="--h:50%"></div>
        <div class="bar" style="--h:75%"></div>
        <div class="bar" style="--h:35%"></div>
        <div class="bar" style="--h:65%"></div>
        <div class="bar" style="--h:85%"></div>
        <div class="bar" style="--h:45%"></div>
        <div class="bar" style="--h:70%"></div>
        <div class="bar" style="--h:55%"></div>
    </div>
</div>

            <div class="context-card" id="new-card">"""

c = c.replace(old2, new2)

with open("index.html", "w") as f:
    f.write(c)

print("volume bars moved inside feature card!")
