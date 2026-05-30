# Run this: python3 volume_css.py

css = """
/* ===================================================================================
 * RAINBOW VOLUME BARS
 * =================================================================================== */

.volume-wrap {
    display: flex;
    align-items: stretch;
    justify-content: center;
    gap: 24px;
    max-width: 720px;
    margin: 0 auto;
}

.volume-bar {
    display: flex;
    align-items: flex-end;
    gap: 4px;
    height: 120px;
    padding: 0 8px;
}

.volume-bar .bar {
    width: 8px;
    height: var(--h);
    border-radius: 4px;
    animation: volume-dance 1.2s ease-in-out infinite alternate;
    opacity: 0.85;
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

.feature-card {
    flex: 1;
    min-width: 0;
}

@media (max-width: 640px) {
    .volume-wrap {
        gap: 12px;
    }
    .volume-bar {
        height: 80px;
        gap: 2px;
        padding: 0 4px;
    }
    .volume-bar .bar {
        width: 5px;
    }
}
"""

with open("landing.css", "a") as f:
    f.write(css)

print("css added!")
