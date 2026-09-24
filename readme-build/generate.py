#!/usr/bin/env python3
"""Generate pixel-art SVG assets for the GitHub profile README."""
import os

OUT = "/Users/geeky/Downloads/assets"
os.makedirs(OUT, exist_ok=True)

# ---------------------------------------------------------------- pixel font
F = {
    'A': [".#.", "#.#", "###", "#.#", "#.#"],
    'B': ["##.", "#.#", "##.", "#.#", "##."],
    'C': [".##", "#..", "#..", "#..", ".##"],
    'D': ["##.", "#.#", "#.#", "#.#", "##."],
    'E': ["###", "#..", "##.", "#..", "###"],
    'F': ["###", "#..", "##.", "#..", "#.."],
    'G': ["###", "#..", "#.#", "#.#", "###"],
    'H': ["#.#", "#.#", "###", "#.#", "#.#"],
    'I': ["###", ".#.", ".#.", ".#.", "###"],
    'J': ["..#", "..#", "..#", "#.#", ".#."],
    'K': ["#.#", "#.#", "##.", "#.#", "#.#"],
    'L': ["#..", "#..", "#..", "#..", "###"],
    'M': ["#.#", "###", "###", "#.#", "#.#"],
    'N': ["#.#", "##.", "###", ".##", "#.#"],
    'O': ["###", "#.#", "#.#", "#.#", "###"],
    'P': ["##.", "#.#", "##.", "#..", "#.."],
    'Q': ["##.", "#.#", "#.#", "##.", "..#"],
    'R': ["##.", "#.#", "##.", "#.#", "#.#"],
    'S': ["###", "#..", "###", "..#", "###"],
    'T': ["###", ".#.", ".#.", ".#.", ".#."],
    'U': ["#.#", "#.#", "#.#", "#.#", "###"],
    'V': ["#.#", "#.#", "#.#", "#.#", ".#."],
    'W': ["#.#", "#.#", "###", "###", "#.#"],
    'X': ["#.#", "#.#", ".#.", "#.#", "#.#"],
    'Y': ["#.#", "#.#", ".#.", ".#.", ".#."],
    'Z': ["###", "..#", ".#.", "#..", "###"],
    '0': ["###", "#.#", "#.#", "#.#", "###"],
    '1': [".#.", "##.", ".#.", ".#.", "###"],
    '2': ["##.", "..#", ".#.", "#..", "###"],
    '3': ["###", "..#", ".##", "..#", "###"],
    '4': ["#.#", "#.#", "###", "..#", "..#"],
    '5': ["###", "#..", "###", "..#", "###"],
    '6': ["###", "#..", "###", "#.#", "###"],
    '7': ["###", "..#", ".#.", ".#.", ".#."],
    '8': ["###", "#.#", "###", "#.#", "###"],
    '9': ["###", "#.#", "###", "..#", "###"],
    '.': ["...", "...", "...", "...", ".#."],
    ',': ["...", "...", "...", ".#.", "#.."],
    ':': ["...", ".#.", "...", ".#.", "..."],
    '!': [".#.", ".#.", ".#.", "...", ".#."],
    '?': ["##.", "..#", ".#.", "...", ".#."],
    '-': ["...", "...", "###", "...", "..."],
    '_': ["...", "...", "...", "...", "###"],
    '/': ["..#", "..#", ".#.", "#..", "#.."],
    '\\': ["#..", "#..", ".#.", "..#", "..#"],
    '|': [".#.", ".#.", ".#.", ".#.", ".#."],
    '(': [".#.", "#..", "#..", "#..", ".#."],
    ')': [".#.", "..#", "..#", "..#", ".#."],
    '[': ["##.", "#..", "#..", "#..", "##."],
    ']': [".##", "..#", "..#", "..#", ".##"],
    '<': ["..#", ".#.", "#..", ".#.", "..#"],
    '>': ["#..", ".#.", "..#", ".#.", "#.."],
    '+': ["...", ".#.", "###", ".#.", "..."],
    '=': ["...", "###", "...", "###", "..."],
    "'": [".#.", ".#.", "...", "...", "..."],
    '"': ["#.#", "#.#", "...", "...", "..."],
    '#': ["#.#", "###", "#.#", "###", "#.#"],
    '*': ["#.#", ".#.", "###", ".#.", "#.#"],
    '~': ["...", "#.#", "#.#", "...", "..."],
    '·': ["...", "...", ".#.", "...", "..."],
    '●': ["..", "##", "##", "##", ".."],
    '█': ["###", "###", "###", "###", "###"],
}
F[' '] = ["...", "...", "...", "...", "..."]

GREEN = "#3fb950"
FG    = "#c9d1d9"
DIM   = "#8b949e"
BORD  = "#30363d"
PANEL = "#10141b"
PANEL2= "#161b22"


def gw(ch):
    return len(F[ch.upper()][0])


def text_width(segments, px):
    w = 0
    for txt, _ in segments:
        for ch in txt:
            w += gw(ch) + 1
    return (w - 1) * px


def render_text(segments, px, x=0, y=0):
    """segments: list of (text, color). Returns svg group string."""
    out = []
    cx = x
    for txt, color in segments:
        rects = []
        for ch in txt:
            g = F[ch.upper()]
            w = gw(ch)
            for r, row in enumerate(g):
                for c, v in enumerate(row):
                    if v == '#':
                        rects.append(f'<rect x="{cx + c * px}" y="{y + r * px}" width="{px}" height="{px}"/>')
            cx += (w + 1) * px
        if rects:
            out.append(f'<g fill="{color}">' + "".join(rects) + "</g>")
    return "".join(out)


def svg(w, h, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}" shape-rendering="crispEdges">{body}</svg>')


def save(name, content):
    with open(os.path.join(OUT, name), "w") as f:
        f.write(content)
    print("wrote", name)


# ------------------------------------------------------------------- avatar
AVATAR = [
    "................",
    "....HHHHHHHH....",
    "...HHHHHHHHHH...",
    "..HHHHHHHHHHHH..",
    "..HHSSSSSSSSHH..",
    "..HSSSSSSSSSSH..",
    "..HSSESSSSESSH..",
    "..HSSESSSSESSH..",
    "..HSSSSSSSSSSH..",
    "..HSSSSMMSSSSH..",
    "...HSSSSSSSSH...",
    ".....HSSSSH.....",
    "....BBBBBBBB....",
    "...BBBBBBBBBB...",
    "..BBBBBBBBBBBB..",
    "..BBBBBGGBBBBB..",
]

PAL = {'H': "#414a61", 'h': "#566179", 'S': "#e9bc90", 'E': "#22262e",
       'M': "#b06a4a", 'B': "#3a4358", 'G': GREEN, '.': None}


def gen_avatar():
    T = 18          # tile size in px-units
    px = 8          # scale
    body = [f'<rect width="{T*px}" height="{T*px}" fill="{PANEL}"/>',
            f'<rect x="0" y="0" width="{T*px}" height="{T*px}" fill="none" stroke="{BORD}" stroke-width="{px}"/>']
    open_px, closed_px = [], []
    for r, row in enumerate(AVATAR):
        for c, ch in enumerate(row):
            if ch == 'E':
                closed_px.append((c, r))   # eyes -> handled separately
                continue
            col = PAL[ch]
            if col:
                body.append(f'<rect x="{(c+1)*px}" y="{(r+1)*px}" width="{px}" height="{px}" fill="{col}"/>')
    # eyes: skin base + open/closed overlays
    for c, r in closed_px:
        body.append(f'<rect x="{(c+1)*px}" y="{(r+1)*px}" width="{px}" height="{px}" fill="{PAL["S"]}"/>')
    op = "".join(f'<rect x="{(c+1)*px}" y="{(r+1)*px}" width="{px}" height="{px}" fill="{PAL["E"]}"/>'
                 for c, r in closed_px)
    cl = "".join(f'<rect x="{(c+1)*px}" y="{(r+2)*px}" width="{px}" height="{px}" fill="{PAL["E"]}"/>'
                 for c, r in closed_px)
    blink_open = ('<animate attributeName="opacity" values="1;1;0;0;1;1" keyTimes="0;0.90;0.901;0.96;0.961;1" '
                  'dur="4.5s" repeatCount="indefinite"/>')
    blink_closed = ('<animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.90;0.901;0.96;0.961;1" '
                    'dur="4.5s" repeatCount="indefinite"/>')
    body.append(f'<g>{op}{blink_open}</g>')
    body.append(f'<g>{cl}{blink_closed}</g>')
    save("avatar.svg", svg(T * px, T * px, "".join(body)))


# ------------------------------------------------------------------ tagline
def gen_tagline():
    segs = [("AUTOMATION", DIM), (" / ", BORD), ("AI AGENTS", GREEN), (" / ", BORD), ("FULLSTACK", DIM)]
    px = 3
    pad = 2
    w = text_width(segs, px) + 2 * pad * px
    h = 5 * px + 2 * pad * px
    body = render_text(segs, px, x=pad * px, y=pad * px)
    save("tagline.svg", svg(w, h, body))


# ----------------------------------------------------------------- terminal
def gen_terminal():
    px = 4
    pad = 3           # in units
    bar_h = 7         # title bar height in units
    lines = [
        [("> ", GREEN), ("whoami", DIM)],
        [("  roman :: automation / ai / fullstack", FG)],
        [],
        [("> ", GREEN), ("ls ./focus", DIM)],
        [("  automation/   ai-agents/", FG)],
        [("  integrations/ fullstack/", FG)],
        [],
        [("> ", GREEN), ("status", DIM)],
        [("  ", FG), ("●", GREEN), (" open to work · dms open", FG)],
        [],
        [("> ", GREEN), ("█", GREEN)],
    ]
    inner = []
    # blinking cursor
    cursor_blink = ('<animate attributeName="opacity" values="1;0;0;1" keyTimes="0;0.5;0.5;1" '
                    'dur="1.2s" repeatCount="indefinite"/>')
    lines[-1] = [("> ", GREEN)]
    lh = 6  # line height in units
    for i, ln in enumerate(lines):
        y = (bar_h + pad + i * lh)
        if ln:
            inner.append(render_text(ln, px, x=pad * px, y=y * px))
    # cursor after last prompt
    lx = pad * px + text_width([("> ", GREEN)], px)
    ly = (bar_h + pad + (len(lines) - 1) * lh) * px
    inner.append(f'<g fill="{GREEN}"><rect x="{lx}" y="{ly}" width="{px}" height="{5*px}"/>' + cursor_blink + "</g>")

    maxw = max(text_width(ln, px) for ln in lines if ln)
    maxw = max(maxw, text_width([("> ", GREEN), ("█", GREEN)], px))
    wu = pad + gw * 0 if False else 0
    w = maxw + 2 * pad * px
    h = (bar_h + pad + len(lines) * lh + pad - 1) * px

    d = 2 * px  # window dot size
    dots = ""
    for i, col in enumerate(["#ff5f57", "#febc2e", "#28c840"]):
        dots += f'<rect x="{(pad + i * 2) * px}" y="{2.5 * px:.0f}" width="{d}" height="{d}" fill="{col}" rx="{px//2}"/>'
    title = render_text([("~/profile", DIM)], px, x=pad * px + 7 * px, y=2 * px)
    body = [
        f'<rect width="{w}" height="{h}" fill="{PANEL2}" stroke="{BORD}" stroke-width="{px}"/>',
        f'<line x1="0" y1="{bar_h*px}" x2="{w}" y2="{bar_h*px}" stroke="{BORD}" stroke-width="{px}"/>',
        dots, title,
    ] + inner
    save("terminal.svg", svg(w, h, "".join(body)))


# -------------------------------------------------------------------- icons
ICONS = {
    "automation": {  # gear
        "....IIII....",
        ".I..IIII..I.",
        ".IIIIIIIIII.",
        "..IIIIIIII..",
        "..III..III..",
        "IIII....IIII",
        "IIII....IIII",
        "..III..III..",
        "..IIIIIIII..",
        ".IIIIIIIIII.",
        ".I..IIII..I.",
        "....IIII....",
    },
    "speed": {  # lightning
        "....IIII....",
        "...IIII.....",
        "..IIII......",
        ".IIIIIIIII..",
        "....IIII....",
        "...IIII.....",
        "..IIII......",
        ".IIII.......",
        "IIII........",
        "II..........",
        "............",
        "............",
    },
    "ai": {  # robot
        ".....GG.....",
        ".....II.....",
        "..IIIIIIII..",
        "..IIIIIIII..",
        ".IIGGIIGGII.",
        ".IIGGIIGGII.",
        "..IIIIIIII..",
        "...IIIIII...",
        "............",
        "............",
        "............",
        "............",
    },
    "integrations": {  # plug
        ".GG......GG.",
        ".GG......GG.",
        ".IIIIIIIIII.",
        ".IIIIIIIIII.",
        ".IIIIIIIIII.",
        "..IIIIIIII..",
        "...IIIIII...",
        "....IIII....",
        ".....II.....",
        ".....II.....",
        ".....II.....",
        "............",
    },
    "fullstack": {  # layers
        ".....II.....",
        "...IIIIII...",
        ".IIIIIIIIII.",
        "...IIIIII...",
        ".....II.....",
        "............",
        "...IIIIII...",
        ".IIIIIIIIII.",
        "...IIIIII...",
        "............",
        "...IIIIII...",
        ".IIIIIIIIII.",
    },
    "telegram": {  # paper plane
        ".........III",
        "........IIII",
        ".......IIIII",
        "..II..IIIIII",
        "..III.IIIIII",
        "..IIIIIIIIII",
        "...IIIIIIIII",
        "....IIIIIIII",
        ".....IIIIIII",
        "......IIIIII",
        "............",
        "............",
    },
    "email": {  # envelope
        "............",
        "IIIIIIIIIIII",
        "III......III",
        "IIII....IIII",
        "IIIII..IIIII",
        "IIIIIIIIIIII",
        "IIIIIIIIIIII",
        "IIIIIIIIIIII",
        "IIIIIIIIIIII",
        "............",
        "............",
        "............",
    },
}
ICON_COLORS = {'I': DIM, 'G': GREEN}


def gen_icon(name, rows, color_map, tile=False):
    px = 4
    n = 12
    body = []
    if tile:
        body += [f'<rect width="{n*px}" height="{n*px}" fill="{PANEL2}" stroke="{BORD}" stroke-width="2"/>']
        off = 1
    else:
        off = 0
    for r, row in enumerate(rows):
        for c, ch in enumerate(row):
            col = color_map.get(ch)
            if col:
                body.append(f'<rect x="{(c+off)*px}" y="{(r+off)*px}" width="{px}" height="{px}" fill="{col}"/>')
    size = (n + 2 * off) * px
    save(f"icon-{name}.svg", svg(size, size, "".join(body)))


# ------------------------------------------------------------------- badges
BADGES = ["TYPESCRIPT", "PYTHON", "NODE.JS", "REACT", "NEXT.JS",
          "OPENAI", "LANGCHAIN", "DOCKER", "POSTGRES"]


def gen_badge(text):
    px = 2
    pad = 3
    w = text_width([(text, FG)], px) + 2 * pad * px
    h = 5 * px + 2 * pad * px
    body = [f'<rect width="{w}" height="{h}" fill="{PANEL2}" stroke="{BORD}" stroke-width="{px}"/>',
            render_text([(text, FG)], px, x=pad * px, y=pad * px)]
    save(f"badge-{text.lower().replace('.', '')}.svg", svg(w, h, "".join(body)))


# ------------------------------------------------------------------ buttons
def gen_button(text, icon_rows):
    px = 2
    ipx = 2          # icon pixel size (12px art -> 24)
    pad = 3
    icon_size = 12 * ipx
    gap = 3 * px
    tw = text_width([(text, FG)], px)
    w = pad * px + icon_size + gap + tw + pad * px
    h = max(icon_size, 5 * px) + 2 * pad * px
    iy = (h - icon_size) // 2
    ty = (h - 5 * px) // 2
    body = [f'<rect width="{w}" height="{h}" fill="{PANEL2}" stroke="{BORD}" stroke-width="{px}"/>']
    for r, row in enumerate(icon_rows):
        for c, ch in enumerate(row):
            col = ICON_COLORS.get(ch)
            if col:
                body.append(f'<rect x="{pad*px + c*ipx}" y="{iy + r*ipx}" width="{ipx}" height="{ipx}" fill="{col}"/>')
    body.append(render_text([(text, FG)], px, x=pad * px + icon_size + gap, y=ty))
    save(f"button-{text.lower()}.svg", svg(w, h, "".join(body)))


# ------------------------------------------------------------------ banner
def gen_banner():
    segs = [("ROMAN", GREEN), ("_ON_GITHUB", FG)]
    px = 5
    pad = 3
    w = text_width(segs, px) + 2 * pad * px
    h = 5 * px + 2 * pad * px
    body = render_text(segs, px, x=pad * px, y=pad * px)
    save("banner.svg", svg(w, h, body))


# ------------------------------------------------------------------- cards
CARDS = [
    ("automation", "AUTOMATION", ["I MAKE BORING STUFF", "RUN ITSELF."]),
    ("speed", "SPEED", ["PROCESSES FASTER,", "PIPELINES SHORTER."]),
    ("ai", "AI AGENTS", ["LLM APPS, AGENTS,", "AI IN REAL WORKFLOWS."]),
    ("integrations", "INTEGRATIONS", ["APIS TALKING", "TO EACH OTHER."]),
    ("fullstack", "FULLSTACK", ["WEB APPS END TO END,", "DEPLOY TO PROD."]),
]


def gen_card(icon, title, lines):
    px = 2
    ipx = 3          # icon pixel (12*3 = 36 icon)
    pad = 4 * px
    icon_size = 12 * ipx
    gap = 5 * px
    tpx = 3          # title text px
    bpx = 2          # body text px
    tw = text_width([(title, GREEN)], tpx)
    bw = max(text_width([(ln, DIM)], bpx) for ln in lines)
    w = pad + icon_size + gap + max(tw, bw) + pad
    h = max(icon_size, tpx * 5 + bpx * 5 * len(lines) + 4 * px) + 2 * pad
    # center icon vertically
    iy = (h - icon_size) // 2
    body = [f'<rect width="{w}" height="{h}" fill="{PANEL2}" stroke="{BORD}" stroke-width="{px}"/>']
    icon_rows = ICONS[icon]
    for r, row in enumerate(icon_rows):
        for c, ch in enumerate(row):
            col = ICON_COLORS.get(ch)
            if col:
                body.append(f'<rect x="{pad + c*ipx}" y="{iy + r*ipx}" width="{ipx}" height="{ipx}" fill="{col}"/>')
    tx = pad + icon_size + gap
    ty = (h - (tpx * 5 + 2 * px + bpx * 5 * len(lines))) // 2
    body.append(render_text([(title, GREEN)], tpx, x=tx, y=ty))
    yy = ty + tpx * 5 + 2 * px
    for ln in lines:
        body.append(render_text([(ln, DIM)], bpx, x=tx, y=yy))
        yy += bpx * 6
    save(f"card-{icon}.svg", svg(w, h, "".join(body)))


# ----------------------------------------------------------------- divider
def gen_divider():
    px = 3
    cell = 3 * px   # filled
    gapc = 3 * px   # gap
    n = 71
    w = n * (cell + gapc) - gapc
    h = cell
    rects = []
    for i in range(n):
        ch = "##-=-##"[i % 7]
        if ch == '#':
            rects.append(f'<rect x="{i*(cell+gapc)}" y="0" width="{cell}" height="{cell}"/>')
        elif ch == '-':
            rects.append(f'<rect x="{i*(cell+gapc)+px}" y="0" width="{px}" height="{cell}"/>')
        elif ch == '=':
            rects.append(f'<rect x="{i*(cell+gapc)}" y="{px}" width="{cell}" height="{px}"/>')
    save("divider.svg", svg(w, h, f'<g fill="{BORD}">{"".join(rects)}</g>'))


# ------------------------------------------------------------------- footer
def gen_footer():
    segs = [("~ ", DIM), ("AUTOMATE THE BORING. SHIP THE COOL.", GREEN), (" ~", DIM)]
    px = 2
    pad = 2
    w = text_width(segs, px) + 2 * pad * px
    h = 5 * px + 2 * pad * px
    body = render_text(segs, px, x=pad * px, y=pad * px)
    save("footer.svg", svg(w, h, body))


# ---------------------------------------------------------------------- run
gen_avatar()
gen_tagline()
gen_terminal()
gen_banner()
for icon, title, lines in CARDS:
    gen_card(icon, title, lines)
gen_divider()
gen_footer()
for name, rows in ICONS.items():
    gen_icon(name, rows, ICON_COLORS)
for b in BADGES:
    gen_badge(b)
gen_button("TELEGRAM", ICONS["telegram"])
gen_button("EMAIL", ICONS["email"])
print("done")
