# Fix volume bars placement in index.html
# Run: python3 fix_volume.py

with open("index.html", "r") as f:
    c = f.read()

# Find gradient section closing and insert volume-wrap before product marquee
old = """        </section>

        <!-- Product Logos Marquee -->"""

new = """        </section>

        <!-- Feature Card with Volume Bars -->
        <div class="volume-wrap">
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
            <div class="context-card feature-card">
                <h2 id="head-title:feature">features:</h2>
                <p>
                    <strong>Softlendar</strong> will get you back to science,
                    glowing stars, cats, latest research, computer science,
                    programming and more. A collection of interactive web
                    experiences built with care and curiosity.
                </p>
                <p>
                    Our current project — <strong>termirator</strong> — is
                    a terminal-style interactive web app where you can run
                    power commands, switch contexts, explore systems, and
                    experience a cyberpunk HUD. Built with
                    <strong>Shell</strong>, <strong>Rust</strong>,
                    <strong>JavaScript</strong>, <strong>CSS</strong>,
                    and <strong>HTML</strong>.
                </p>
                <p>
                    Our original project — <strong>ct</strong> — is
                    a cat-themed interactive web app where you can explore cat
                    facts, pick toys, chat with an AI assistant, run power
                    commands, and join a community of cat lovers. Built with
                    <strong>Ruby on Rails 8</strong> and
                    <strong>PostgreSQL</strong>.
                </p>
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

        <!-- Product Logos Marquee -->"""

if old in c:
    c = c.replace(old, new)
    with open("index.html", "w") as f:
        f.write(c)
    print("done")
else:
    print("anchor not found")
