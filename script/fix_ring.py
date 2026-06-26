import re

with open("files/landing.css", "r") as f:
    css = f.read()

# 1. Add smooth transition to ring
old_ring = """.net-ring {
    position: absolute;
    top: 50%;
    left: 50%;
    width: 80%;
    height: 80%;
    transform: translate(-50%, -50%);
    border-radius: 50%;
    border: 1px solid rgba(255, 140, 66, 0.08);
    animation: ringSpin 30s linear infinite;
}"""

new_ring = """.net-ring {
    position: absolute;
    top: 50%;
    left: 50%;
    width: 80%;
    height: 80%;
    transform: translate(-50%, -50%);
    border-radius: 50%;
    border: 1px solid rgba(255, 140, 66, 0.08);
    animation: ringSpin 30s linear infinite;
    transition: transform 0.8s cubic-bezier(0.34, 1.56, 0.64, 1);
}"""

if old_ring in css:
    css = css.replace(old_ring, new_ring)

# 2. Add counter-rotation to keep logos upright
old_slot_inner = """.net-slot-inner {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    background: rgba(26, 10, 46, 0.85);
    border: 2px solid rgba(255, 140, 66, 0.25);
    backdrop-filter: blur(8px);
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 10px;
    transition: all 0.3s ease;
    box-shadow: 0 4px 20px rgba(255, 140, 66, 0.08);
}"""

new_slot_inner = """.net-slot-inner {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    background: rgba(26, 10, 46, 0.85);
    border: 2px solid rgba(255, 140, 66, 0.25);
    backdrop-filter: blur(8px);
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 10px;
    transition: all 0.3s ease;
    box-shadow: 0 4px 20px rgba(255, 140, 66, 0.08);
    animation: slotCounterSpin 30s linear infinite;
}

@keyframes slotCounterSpin {
    from { transform: rotate(0deg); }
    to { transform: rotate(-360deg); }
}"""

if old_slot_inner in css:
    css = css.replace(old_slot_inner, new_slot_inner)

# 3. Add glow for active slot
old_active = """.net-slot:hover .net-slot-inner,
.net-slot.active .net-slot-inner {
    border-color: rgba(255, 140, 66, 0.9);
    box-shadow: 0 8px 30px rgba(255, 140, 66, 0.35);
    background: rgba(255, 140, 66, 0.12);
}"""

new_active = """.net-slot:hover .net-slot-inner,
.net-slot.active .net-slot-inner {
    border-color: #ff8c42;
    box-shadow: 0 0 30px rgba(255, 140, 66, 0.6), 0 0 60px rgba(255, 60, 127, 0.3), 0 8px 30px rgba(255, 140, 66, 0.35);
    background: rgba(255, 140, 66, 0.15);
}"""

if old_active in css:
    css = css.replace(old_active, new_active)

# 4. When ring is paused, stop counter-spin on slots
old_paused = """.net-ring.paused {
    animation-play-state: paused;
}"""

new_paused = """.net-ring.paused {
    animation-play-state: paused;
}

.net-ring.paused .net-slot-inner {
    animation-play-state: paused;
}"""

if old_paused in css:
    css = css.replace(old_paused, new_paused)

with open("files/landing.css", "w") as f:
    f.write(css)

print("Fixed ring CSS")
