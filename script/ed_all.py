# ed_all.py — Run: python3 ed_all.py
with open("index.html", "r") as f:
    c = f.read()

# ============================================
# 1. CUT TERMINAL SECTION
# ============================================
start = c.find("<!-- Command Terminal --\u003e")
end = c.find("<!-- Product Logos Marquee --\u003e", start)
if start != -1 and end != -1:
    c = c[:start] + "\n        " + c[end:]
    print("cut terminal")

# ============================================
# 2. SPLIT INTO 3 CARDS
# ============================================
# Card 1: feature text (keep first two paragraphs)
# Card 2: badges
# Card 3: links

old = """<div class="badge-categories">"""
new = """</div>

            <!-- Card #2: Badges --\u003e
            <div class="context-card badge-card">
                <h2 id="head-title:badge">badges:</h2>
                <div class="badge-categories">"""
c = c.replace(old, new)

old2 = """                </div>

                <div class="links-row">"""
new2 = """                </div>
            </div>

            <!-- Card #3: Product Links --\u003e
            <div class="context-card product-card">
                <h2 id="head-title:product">products:</h2>
                <div class="links-row">"""
c = c.replace(old2, new2)

# Add head-title to card 1
old3 = """<div class="context-card">
                <p>
                    <strong>Softlendar</strong> will get you back to science,"""
new3 = """<div class="context-card feature-card">
                <h2 id="head-title:feature">features:</h2>
                <p>
                    <strong>Softlendar</strong> will get you back to science,"""
c = c.replace(old3, new3)

# Close product card properly
old4 = '''                <div class="paws"'''
new4 = '''            </div>

                <div class="paws"'''
c = c.replace(old4, new4)

print("cards split")

# ============================================
# 3. ADD VOLUME BARS BETWEEN FEATURE AND BADGE
# ============================================
old5 = """            </div>

            <!-- Card #2: Badges --\u003e"""
new5 = """            </div>

            <!-- Rainbow Volume --\u003e
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

            <!-- Card #2: Badges --\u003e"""
c = c.replace(old5, new5)

print("volume added")

# ============================================
# 4. ADD RED WAVE BEFORE MARQUEE
# ============================================
old6 = """        </section>

        <!-- Product Logos Marquee --\u003e"""
new6 = """        </section>

        <!-- Red Wave --\u003e
        <section class="wave-section">
            <svg class="wave-svg" viewBox="0 0 1440 320" preserveAspectRatio="none">
                <defs>
                    <linearGradient id="waveGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                        <stop offset="0%" stop-color="#ff6b6b" />
                        <stop offset="50%" stop-color="#ff3c7f" />
                        <stop offset="100%" stop-color="#ff8c42" />
                    </linearGradient>
                </defs>
                <path class="wave-path" fill="url(#waveGrad)" d="M0,160 C240,240 480,80 720,160 C960,240 1200,80 1440,160 L1440,320 L0,320 Z" />
                <path class="wave-path delay" fill="rgba(255, 60, 127, 0.3)" d="M0,180 C240,100 480,260 720,180 C960,100 1200,260 1440,180 L1440,320 L0,320 Z" />
            </svg>
        </section>

        <!-- Product Logos Marquee --\u003e"""
c = c.replace(old6, new6)

print("wave added")

with open("index.html", "w") as f:
    f.write(c)
print("all done!")
