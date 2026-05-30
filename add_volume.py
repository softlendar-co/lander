# Run this: python3 add_volume.py

with open("index.html", "r") as f:
    lines = f.readlines()

# Find the features card line
for i, line in enumerate(lines):
    if "head-title:feature" in line:
        # Find the opening div of context-card (should be a few lines above)
        card_start = i - 1
        while card_start > 0 and '<div class="context-card"' not in lines[card_start]:
            card_start -= 1

        # Build volume bars + wrapped card
        indent = "            "
        new_lines = [
            indent + '<div class="volume-wrap">\n',
            indent + '    <div class="volume-bar left-bar">\n',
            indent + '        <div class="bar" style="--h:30%"></div>\n',
            indent + '        <div class="bar" style="--h:60%"></div>\n',
            indent + '        <div class="bar" style="--h:45%"></div>\n',
            indent + '        <div class="bar" style="--h:80%"></div>\n',
            indent + '        <div class="bar" style="--h:55%"></div>\n',
            indent + '        <div class="bar" style="--h:70%"></div>\n',
            indent + '        <div class="bar" style="--h:40%"></div>\n',
            indent + '        <div class="bar" style="--h:90%"></div>\n',
            indent + "    </div>\n",
            indent + '    <div class="context-card feature-card">\n',
        ]

        # Replace the old context-card div with wrapped version
        lines[card_start] = "".join(new_lines)
        break

# Now find closing of feature card and add right volume bar
for i, line in enumerate(lines):
    if "<!-- Card #3: New Card -->" in line:
        indent = "            "
        new_lines = [
            indent + "    </div>\n",
            indent + '    <div class="volume-bar right-bar">\n',
            indent + '        <div class="bar" style="--h:50%"></div>\n',
            indent + '        <div class="bar" style="--h:75%"></div>\n',
            indent + '        <div class="bar" style="--h:35%"></div>\n',
            indent + '        <div class="bar" style="--h:65%"></div>\n',
            indent + '        <div class="bar" style="--h:85%"></div>\n',
            indent + '        <div class="bar" style="--h:45%"></div>\n',
            indent + '        <div class="bar" style="--h:70%"></div>\n',
            indent + '        <div class="bar" style="--h:55%"></div>\n',
            indent + "    </div>\n",
            indent + "</div>\n",
            "\n",
        ]
        lines[i] = "".join(new_lines)
        break

with open("index.html", "w") as f:
    f.writelines(lines)

print("volume bars added!")
