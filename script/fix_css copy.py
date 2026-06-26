with open("files/landing.css", "r") as f:
    css = f.read()

old = """@keyframes ringSpin {
    from {
        transform: rotate(0deg);
    }
    to {
        transform: rotate(360deg);
    }
}"""

new = """@keyframes ringSpin {
    from {
        transform: translate(-50%, -50%) rotate(0deg);
    }
    to {
        transform: translate(-50%, -50%) rotate(360deg);
    }
}"""

if old in css:
    css = css.replace(old, new)
    with open("files/landing.css", "w") as f:
        f.write(css)
    print("Fixed ringSpin keyframe")
else:
    print("Could not find ringSpin keyframe")
