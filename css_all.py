# css_all.py — Run: python3 css_all.py
with open("landing.css", "a") as f:
    f.write("""
/* ===================================================================================
 * HEAD TITLES
 * =================================================================================== */
[id^="head-title"] {
    font-size: 1.4rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 3px;
    color: transparent;
    background: linear-gradient(135deg, #ff8c42, #ff3c7f);
    -webkit-background-clip: text;
    background-clip: text;
    margin-bottom: 20px;
    text-align: center;
    position: relative;
    padding-bottom: 12px;
}
[id^="head-title"]::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 60px;
    height: 3px;
    background: linear-gradient(90deg, #ff8c42, #ff3c7f);
    border-radius: 3px;
}

/* ===================================================================================
 * CARD GAPS
 * =================================================================================== */
.context-card + .context-card,
.context-card + .volume-wrap,
.volume-wrap + .context-card {
    margin-top: 54px;
}
.volume-wrap {
    margin-bottom: 54px;
}

/* ===================================================================================
 * RAINBOW VOLUME BARS
 * =================================================================================== */
.volume-wrap {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 40px;
    max-width: 720px;
    margin: 0 auto;
    padding: 0 24px;
}
.volume-bar {
    display: flex;
    align-items: flex-end;
    gap: 5px;
    height: 160px;
}
.volume-bar .bar {
    width: 8px;
    height: var(--h);
    border-radius: 4px;
    animation: volume-dance 1.2s ease-in-out infinite alternate;
}
.left-bar .bar:nth-child(1) { background: #ff6b6b; animation-delay: 0.0s; }
.left-bar .bar:nth-child(2) { background: #ffa94d; animation-delay: 0.1s; }
.left-bar .bar:nth-child(3) { background: #ffd43b; animation-delay: 0.2s; }
.left-bar .bar:nth-child(4) { background: #69db7c; animation-delay: 0.3s; }
.left-bar .bar:nth-child(5) { background: #38d9a9; animation-delay: 0.4s; }
.left-bar .bar:nth-child(6) { background: #4dabf7; animation-delay: 0.5s; }
.left-bar .bar:nth-child(7) { background: #748ffc; animation-delay: 0.6s; }
.left-bar .bar:nth-child(8) { background: #da77f2; animation-delay: 0.7s; }
.right-bar .bar:nth-child(1) { background: #ff6b6b; animation-delay: 0.3s; }
.right-bar .bar:nth-child(2) { background: #ffa94d; animation-delay: 0.4s; }
.right-bar .bar:nth-child(3) { background: #ffd43b; animation-delay: 0.5s; }
.right-bar .bar:nth-child(4) { background: #69db7c; animation-delay: 0.6s; }
.right-bar .bar:nth-child(5) { background: #38d9a9; animation-delay: 0.7s; }
.right-bar .bar:nth-child(6) { background: #4dabf7; animation-delay: 0.0s; }
.right-bar .bar:nth-child(7) { background: #748ffc; animation-delay: 0.1s; }
.right-bar .bar:nth-child(8) { background: #da77f2; animation-delay: 0.2s; }
@keyframes volume-dance {
    0% { height: calc(var(--h) * 0.4); opacity: 0.5; }
    100% { height: calc(var(--h) * 1.2); opacity: 1; }
}

/* ===================================================================================
 * RED WAVE
 * =================================================================================== */
.wave-section {
    position: relative;
    height: 120px;
    overflow: hidden;
    background: linear-gradient(180deg, #fff5e6 0%, #ffe0b2 50%, #ffb3b3 100%);
}
.wave-svg {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
}
.wave-path {
    animation: wave-flow 6s ease-in-out infinite;
}
.wave-path.delay {
    animation: wave-flow-reverse 8s ease-in-out infinite;
}
@keyframes wave-flow {
    0%, 100% { transform: translateX(0) scaleY(1); }
    25% { transform: translateX(-20px) scaleY(1.1); }
    50% { transform: translateX(0) scaleY(1); }
    75% { transform: translateX(20px) scaleY(0.9); }
}
@keyframes wave-flow-reverse {
    0%, 100% { transform: translateX(0) scaleY(1); }
    25% { transform: translateX(20px) scaleY(0.9); }
    50% { transform: translateX(0) scaleY(1); }
    75% { transform: translateX(-20px) scaleY(1.1); }
}
""")
print("css done!")
