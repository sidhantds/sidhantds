"""Render the profile README's SVG assets.

Edit PROFILE below, then run:  python scripts/render.py
Every image lands in .github/assets/. No dependencies beyond the standard library.
"""
import base64
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / ".github" / "assets"

PROFILE = {
    "location": "Pune, India",
    "name": "Sidhant Pujara",
    "tagline": "AI engineer building ML systems that ship.",
    "headline": "AI & Data Engineer",
    "subline": "Building ML systems that ship.",
    "whoami": "data science intern @ globallogic",
    "now": [
        ("Writing an IEEE paper on agentic AI", "Autonomous agents for supply chain decisions"),
        ("Building ML models at GlobalLogic", "Data Science Intern, Hitachi group"),
        ("Shipping models to production", "FastAPI services, Docker images, AWS"),
    ],
    "education": ("BCA, MIT World Peace University", "Class of 2027"),
    "previously": ("Unified Mentor", "Data Science Intern, 2024"),
    "projects": [
        {
            "slug": "neo-sentinel",
            "kind": "ML engineering",
            "title": "NEO Sentinel",
            "lines": ["Asteroid hazard screening API trained on NASA's", "Near Earth Object data, served with FastAPI."],
            "tech": ["scikit-learn", "fastapi", "docker", "pytest", "ci"],
        },
        {
            "slug": "ticket-triage",
            "kind": "NLP",
            "title": "AI Ticket Triage",
            "lines": ["Classifies support tickets, predicts priority and", "SLA, and flags low-confidence cases for review."],
            "tech": ["scikit-learn", "tf-idf", "sqlite", "streamlit"],
        },
        {
            "slug": "waste-classification",
            "kind": "Computer vision",
            "title": "Waste Classification",
            "lines": ["MobileNetV2 transfer learning sorts waste photos", "into 5 classes at 93% accuracy, live on Streamlit."],
            "tech": ["tensorflow", "keras", "jax", "streamlit"],
        },
        {
            "slug": "airline-churn",
            "kind": "Predictive modelling",
            "title": "Airline Loyalty Churn",
            "lines": ["Ranks loyalty members by churn risk and value", "so a retention team knows who to call first."],
            "tech": ["python", "scikit-learn", "random forest"],
        },
    ],
    "stack": [
        ("Languages", ["Python", "SQL"]),
        ("Deep learning", ["PyTorch", "TensorFlow", "Keras"]),
        ("ML", ["scikit-learn", "XGBoost", "Pandas", "NumPy"]),
        ("Shipping", ["FastAPI", "Docker", "AWS", "GitHub Actions", "pytest"]),
        ("Apps", ["Streamlit", "SQLite"]),
    ],
    "links": [("portfolio", 132), ("linkedin", 124), ("email", 108)],
}

# ── Design tokens ──────────────────────────────────────────────
BG = "#0A0A0B"
LINE = "#FFFFFF14"
INK = "#EDEDEF"
MUTED = "#8A8A93"
DIM = "#55555C"
LIVE = "#3FB950"
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, 'Liberation Mono', monospace"
MONO_CHAR = 0.6  # advance width of a monospace glyph, in ems
W = 840

BASE_STYLE = f"""
  .sans {{ font-family: {SANS}; }}
  .mono {{ font-family: {MONO}; }}
  .label {{ font-family: {MONO}; font-size: 11px; letter-spacing: 2.4px; fill: {MUTED}; }}
  @media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} }}
"""


def svg(width, height, body, style="", title=""):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-label="{escape(title)}">\n'
        f"<title>{escape(title)}</title>\n<style>{BASE_STYLE}{style}</style>\n{body}\n</svg>\n"
    )


def card(width, height, x=0.5, y=0.5):
    return f'<rect x="{x}" y="{y}" width="{width - 1}" height="{height - 1}" rx="14" fill="{BG}" stroke="{LINE}"/>'


def text(x, y, value, cls="sans", size=14, fill=INK, weight=400, extra=""):
    return (
        f'<text x="{x}" y="{y}" class="{cls}" font-size="{size}" font-weight="{weight}" '
        f'fill="{fill}" {extra}>{escape(value)}</text>'
    )


def arrow(x, y, size=12, color=MUTED):
    s = size
    return (
        f'<path d="M{x} {y + s} L{x + s} {y} M{x + 3} {y} H{x + s} V{s - 3 + y}" '
        f'stroke="{color}" stroke-width="1.4" fill="none" stroke-linecap="round"/>'
    )


# ── Header: full width photo, slow drift, text rises in over a left shade ──
def header():
    p = PROFILE
    photo = base64.b64encode((OUT / "header-photo.jpg").read_bytes()).decode()
    style = """
  .photo { transform-box: fill-box; transform-origin: 50% 50%; animation: drift 16s ease-in-out infinite alternate; }
  .rise { animation: rise 1.1s cubic-bezier(.22,1,.36,1) .2s both; }
  .rise2 { animation-delay: .45s; }
  .rise3 { animation-delay: .7s; }
  @keyframes drift { from { transform: scale(1.02); } to { transform: scale(1.1); } }
  @keyframes rise { from { opacity: 0; transform: translateY(14px); } to { opacity: 1; transform: translateY(0); } }
"""
    body = f"""
<defs>
  <linearGradient id="shade" x1="0" x2="1" y1="0" y2="0">
    <stop offset="0" stop-color="{BG}" stop-opacity=".94"/>
    <stop offset=".5" stop-color="{BG}" stop-opacity=".6"/>
    <stop offset="1" stop-color="{BG}" stop-opacity=".08"/>
  </linearGradient>
  <clipPath id="frame"><rect width="{W}" height="320" rx="14"/></clipPath>
</defs>
<g clip-path="url(#frame)">
  <image class="photo" href="data:image/jpeg;base64,{photo}" x="-12" y="-12" width="{W + 24}" height="344" preserveAspectRatio="xMidYMid slice"/>
  <rect width="{W}" height="320" fill="url(#shade)"/>
</g>
<rect x="0.5" y="0.5" width="{W - 1}" height="319" rx="14" fill="none" stroke="{LINE}"/>
<text x="48" y="92" class="label rise" font-size="11">{escape(p['location'].upper())}</text>
{text(46, 168, p['headline'], size=50, weight=600, cls='sans rise rise2', extra='letter-spacing="-1.4"')}
{text(48, 206, p['subline'], size=18, fill=INK, cls='sans rise rise3')}
"""
    return svg(W, 320, body, style, f"{p['name']}. {p['headline']}. {p['tagline']}")


# ── Now / education / previously ──────────────────────────────
def now():
    p = PROFILE
    style = """
  .pulse { animation: pulse 1.8s ease-in-out infinite; transform-origin: 53px 37px; }
  @keyframes pulse { 50% { opacity: .25; transform: scale(.7); } }
"""
    items = "".join(
        text(48, 82 + i * 50, title, size=16, weight=600) + text(48, 102 + i * 50, sub, size=12.5, fill=MUTED)
        for i, (title, sub) in enumerate(p["now"])
    )
    side = ""
    for i, (label, (head, sub)) in enumerate((("Education", p["education"]), ("Previously", p["previously"]))):
        y = i * 117
        side += f'<rect x="540.5" y="{y + 0.5}" width="299" height="{105 if i == 0 else 106}" rx="14" fill="{BG}" stroke="{LINE}"/>'
        side += text(566, y + 36, label.upper(), cls="label") + text(566, y + 66, head, size=15, weight=600)
        side += text(566, y + 86, sub, size=12.5, fill=MUTED)
    body = f"""
{card(526, 224)}
<circle class="pulse" cx="53" cy="37" r="4" fill="{LIVE}"/>
{text(66, 41, 'RIGHT NOW', cls='label')}
{items}
<g transform="translate(0,1)">{side}</g>
"""
    alt = "Right now: " + "; ".join(t for t, _ in p["now"]) + f". Education: {p['education'][0]}."
    return svg(W, 226, body, style, alt)


# ── Section label ─────────────────────────────────────────────
def label(name, index):
    caption = f"{index:02d} / {name.upper()}"
    end = len(caption) * (11 * MONO_CHAR + 2.4) + 16
    body = f"""
{text(0, 22, caption, cls='label')}
<line x1="{end:.0f}" x2="{W}" y1="18" y2="18" stroke="{LINE}"/>
"""
    return svg(W, 32, body, "", name)


# ── Project card ──────────────────────────────────────────────
def project(i, proj):
    cw, ch = 410, 196
    body = f"""
{card(cw, ch)}
{text(28, 40, f"{i + 1:02d} · {proj['kind'].upper()}", cls='label')}
{arrow(cw - 40, 28)}
{text(27, 82, proj['title'], size=23, weight=600, extra='letter-spacing="-0.4"')}
{text(28, 112, proj['lines'][0], size=13.5, fill=MUTED)}
{text(28, 132, proj['lines'][1], size=13.5, fill=MUTED)}
<line x1="28" x2="{cw - 28}" y1="152" y2="152" stroke="{LINE}"/>
{text(28, 176, '  ·  '.join(proj['tech']), cls='mono', size=11.5, fill=INK)}
"""
    return svg(cw, ch, body, "", f"{proj['title']}: {' '.join(proj['lines'])}")


# ── Stack ─────────────────────────────────────────────────────
def stack():
    rows, y = "", 30
    for name, items in PROFILE["stack"]:
        rows += text(28, y + 20, name.upper(), cls="label")
        x = 180
        for item in items:
            w = len(item) * 12.5 * MONO_CHAR + 24
            rows += f'<rect x="{x}" y="{y}" width="{w:.0f}" height="30" rx="7" fill="#FFFFFF08" stroke="{LINE}"/>'
            rows += text(x + 12, y + 20, item, cls="mono", size=12.5)
            x += w + 8
        y += 44
    height = y + 16
    body = card(W, height) + rows
    alt = "Stack: " + "; ".join(f"{n}: {', '.join(i)}" for n, i in PROFILE["stack"])
    return svg(W, height, body, "", alt)


# ── Link pill ─────────────────────────────────────────────────
def pill(name, width):
    body = f"""
<rect x="0.5" y="0.5" width="{width - 1}" height="39" rx="20" fill="{BG}" stroke="{LINE}"/>
{text(20, 25, name, cls='mono', size=13)}
{arrow(width - 32, 15, size=9, color=INK)}
"""
    return svg(width, 40, body, "", name)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    files = {
        "header.svg": header(),
        "now.svg": now(),
        "label-work.svg": label("Selected work", 1),
        "label-stack.svg": label("Stack", 2),
        "stack.svg": stack(),
    }
    for i, proj in enumerate(PROFILE["projects"]):
        files[f"project-{proj['slug']}.svg"] = project(i, proj)
    for name, width in PROFILE["links"]:
        files[f"link-{name}.svg"] = pill(name, width)
    for name, content in files.items():
        (OUT / name).write_text(content, encoding="utf-8")
    print(f"wrote {len(files)} files to {OUT}")


if __name__ == "__main__":
    main()
