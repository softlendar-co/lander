with open("index.html", "r") as f:
    c = f.read()

# The right bar is outside volume-wrap — move it inside
old = """            </div>

                </div>
                <div class="volume-bar right-bar">"""

new = """            </div>
                <div class="volume-bar right-bar">"""

if old in c:
    c = c.replace(old, new)
    with open("index.html", "w") as f:
        f.write(c)
    print("fixed")
else:
    print("not found")
