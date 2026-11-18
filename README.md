# Bunga Telang — Colour Chemistry Lab

An interactive single-page website about the **Butterfly Pea flower** (_Clitoria ternatea_), built as a science exhibition project. It turns the botany and anthocyanin chemistry of the bunga telang into hands-on simulations, games and quizzes.

## What's inside

| Section | What it does |
| --- | --- |
| **Experiment** | Pour "reagents" or drag the pH slider and watch the beaker liquid change colour like a real anthocyanin pH indicator |
| **Information** | Flip cards covering the botanist, culinary, traditional medicine, ecology and industry perspectives |
| **Magic Cafe** | Step-by-step cooking simulators for Nasi Kerabu and a blue colour-changing mocktail |
| **UN SDGs** | How the project ties into SDG 3, 4, 12 and 15 |
| **Quiz** | Shuffled multiple-choice quiz with streaks, XP and scoring |
| **AR Lab** | Camera-backed 3D molecular viewer (Three.js) of delphinidin that recolours by pH |

## Tech

- Plain HTML, CSS and JavaScript — no build step, no dependencies to install
- [Tailwind CSS](https://tailwindcss.com/) and [Three.js](https://threejs.org/) loaded from CDN
- All styling and logic live inside `index.html`
- Ambient sound effects generated at runtime with the Web Audio API

## Run it locally

Just open `index.html` in a browser. For a proper local server (needed for the camera/AR feature):

```bash
py server.py            # http://localhost:8000
py server.py 3000       # use a specific port
py server.py 3000 --no-open
```

`server.py` is a small Python wrapper around `http.server` that serves the folder with correct MIME types and no caching.

## Resources

- `bunga-telang.svg` — vector illustration of the flower
- `bunga telang 2.jpg` — photograph used on the Information page (place this file next to `index.html`)

## Notes

- Camera access requires `localhost` or HTTPS — it works on the GitHub Pages deployment and when served locally.
- The site falls back to a simulated AR camera mode automatically if camera permission is unavailable.
