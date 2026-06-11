"""Generate the three figures for 'Where Do Good Vision Targets Come From?'.

Clean, distill-style line diagrams. Run: python3 generate_figures.py
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, FancyArrowPatch
from matplotlib.lines import Line2D
import os

HERE = os.path.dirname(os.path.abspath(__file__))

INK   = "#333333"
GREY  = "#777777"
LIGHT = "#c8c8c8"
BLUE  = "#1772d0"
ORANGE = "#f09228"
PAPER = "#fafafa"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "savefig.dpi": 200,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.15,
})


def fig1():
    fig, ax = plt.subplots(figsize=(6.8, 4.6))
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)
    # axis arrows
    ax.add_patch(FancyArrowPatch((0.05, 0.07), (0.99, 0.07), arrowstyle="-|>",
                 mutation_scale=14, color=INK, lw=1.3))
    ax.add_patch(FancyArrowPatch((0.07, 0.05), (0.07, 0.99), arrowstyle="-|>",
                 mutation_scale=14, color=INK, lw=1.3))
    ax.text(0.53, 0.012, "accessible information", ha="center", va="bottom",
            fontsize=11, color=INK)
    ax.text(0.018, 0.53, "objective SNR", ha="center", va="center",
            rotation=90, fontsize=11, color=INK)

    # empty corner (wide enough for the text to sit inside)
    ax.add_patch(Rectangle((0.55, 0.63), 0.42, 0.32, facecolor="#fff6e9",
                 edgecolor=ORANGE, lw=1.6, linestyle=(0, (5, 4))))
    ax.text(0.76, 0.855, "the corner we want", ha="center", va="center",
            fontsize=11.5, color="#b06a12", fontweight="bold")
    ax.text(0.76, 0.78, "high SNR + high info", ha="center", va="center",
            fontsize=10.5, color="#b06a12", style="italic")

    # data points, labels kept well clear of the box, arrows, and the axes
    ax.plot(0.18, 0.78, "o", ms=11, color=BLUE, zorder=5)
    ax.text(0.18, 0.69, "latent\nself-supervision", ha="center", va="top",
            fontsize=10, color=INK)
    ax.plot(0.82, 0.27, "o", ms=11, color=BLUE, zorder=5)
    ax.text(0.82, 0.185, "pixel prediction", ha="center", va="top",
            fontsize=10, color=INK)

    # A raises SNR (vertical), arrowhead stops short of the box bottom (0.63)
    ax.add_patch(FancyArrowPatch((0.82, 0.35), (0.82, 0.57), arrowstyle="-|>",
                 mutation_scale=12, color=GREY, lw=1.5))
    ax.text(0.865, 0.46, "A: factorize / score", ha="left", va="center",
            fontsize=8.6, color=GREY, rotation=90)
    # B–E add information (horizontal), arrowhead stops short of the box left (0.55)
    ax.add_patch(FancyArrowPatch((0.26, 0.78), (0.50, 0.78), arrowstyle="-|>",
                 mutation_scale=12, color=GREY, lw=1.5))
    ax.text(0.37, 0.83, "B–E: ground the target", ha="center", va="bottom",
            fontsize=8.6, color=GREY)

    fig.savefig(os.path.join(HERE, "fig1-empty-corner.png"))
    plt.close(fig)


def fig2():
    cards = [
        ("A", "Loss", "how the loss\ntreats ambiguity", "compute", False),
        ("B", "Physics", "image-formation\nmodel", "measurement", False),
        ("C", "Time", "long-horizon\nprediction", "data", False),
        ("D", "Geometry", "cross-view\ncorrespondence", "views", False),
        ("E", "Action", "what you\ncan control", "embodiment", True),
    ]
    fig, ax = plt.subplots(figsize=(8.4, 3.0))
    ax.set_xlim(0, len(cards)); ax.set_ylim(0, 1)
    ax.axis("off")
    w = 0.90
    for i, (letter, name, inv, cost, hi) in enumerate(cards):
        x = i + (1 - w) / 2
        edge = ORANGE if hi else LIGHT
        face = "#fff6e9" if hi else "white"
        ax.add_patch(FancyBboxPatch((x, 0.10), w, 0.80,
                     boxstyle="round,pad=0.012,rounding_size=0.04",
                     facecolor=face, edgecolor=edge, lw=1.6))
        head = ORANGE if hi else BLUE
        ax.text(x + w/2, 0.78, letter, ha="center", va="center",
                fontsize=15, fontweight="bold", color=head)
        ax.text(x + w/2, 0.645, name, ha="center", va="center",
                fontsize=11, color=INK)
        ax.text(x + w/2, 0.44, inv, ha="center", va="center",
                fontsize=8.0, color=GREY)
        ax.text(x + w/2, 0.20, cost, ha="center", va="center",
                fontsize=8.2, color=("#b06a12" if hi else GREY), style="italic")
    ax.text(len(cards)/2, 0.015, "source of invariance  →  cost",
            ha="center", va="bottom", fontsize=9, color=GREY)
    fig.savefig(os.path.join(HERE, "fig2-five-sources.png"))
    plt.close(fig)


def fig3():
    fig, ax = plt.subplots(figsize=(7.8, 3.6))
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.axis("off")

    # ---- left panel: passive ----
    ax.text(0.23, 0.96, "passive axes (A–D)", ha="center", va="center",
            fontsize=10.5, color=INK, fontweight="bold")
    # ceiling
    ax.plot([0.03, 0.43], [0.78, 0.78], color=ORANGE, lw=1.8,
            linestyle=(0, (5, 4)))
    ax.text(0.23, 0.815, "information the sensor never recorded",
            ha="center", va="bottom", fontsize=7.8, color="#b06a12",
            style="italic")
    # losses box (near the ceiling)
    ax.add_patch(FancyBboxPatch((0.06, 0.50), 0.34, 0.15,
                 boxstyle="round,pad=0.01,rounding_size=0.03",
                 facecolor="white", edgecolor=BLUE, lw=1.4))
    ax.text(0.23, 0.575, "losses A–D", ha="center", va="center",
            fontsize=10, color=BLUE)
    # dataset box (bottom)
    ax.add_patch(FancyBboxPatch((0.06, 0.18), 0.34, 0.15,
                 boxstyle="round,pad=0.01,rounding_size=0.03",
                 facecolor="white", edgecolor=LIGHT, lw=1.4))
    ax.text(0.23, 0.255, "fixed dataset", ha="center", va="center",
            fontsize=10, color=INK)
    # dataset -> losses
    ax.add_patch(FancyArrowPatch((0.23, 0.33), (0.23, 0.49), arrowstyle="-|>",
                 mutation_scale=12, color=GREY, lw=1.4))
    # losses pushes up but is capped by ceiling
    ax.add_patch(FancyArrowPatch((0.23, 0.655), (0.23, 0.765), arrowstyle="-|>",
                 mutation_scale=12, color=GREY, lw=1.4))
    ax.text(0.41, 0.715, "capped", ha="left", va="center", fontsize=8.0,
            color="#b06a12", style="italic")

    # divider
    ax.plot([0.48, 0.48], [0.06, 0.90], color="#e3e3e3", lw=1.2)

    # ---- right panel: active loop ----
    ax.text(0.74, 0.96, "active axis (E)", ha="center", va="center",
            fontsize=10.5, color="#b06a12", fontweight="bold")
    cx, cy = 0.74, 0.50
    nodes = {
        "perceive": (cx, cy + 0.24),
        "act":      (cx + 0.135, cy - 0.14),
        "collect":  (cx - 0.135, cy - 0.14),
    }
    bw, bh = 0.080, 0.055
    for name, (x, y) in nodes.items():
        ax.add_patch(FancyBboxPatch((x-bw, y-bh), 2*bw, 2*bh,
                     boxstyle="round,pad=0.006,rounding_size=0.025",
                     facecolor="#fff6e9", edgecolor=ORANGE, lw=1.5))
        ax.text(x, y, name, ha="center", va="center", fontsize=9.0,
                color="#9a5a0e")
    order = ["perceive", "act", "collect", "perceive"]
    for a, b in zip(order, order[1:]):
        xa, ya = nodes[a]; xb, yb = nodes[b]
        ax.add_patch(FancyArrowPatch((xa, ya), (xb, yb), arrowstyle="-|>",
                     mutation_scale=11, color=ORANGE, lw=1.6,
                     shrinkA=12, shrinkB=12,
                     connectionstyle="arc3,rad=-0.22"))
    ax.text(0.76, 0.085, "moves the ceiling by\ngenerating new observations",
            ha="center", va="center", fontsize=8.0, color=GREY, style="italic")

    fig.savefig(os.path.join(HERE, "fig3-passive-vs-active.png"))
    plt.close(fig)


if __name__ == "__main__":
    fig1(); fig2(); fig3()
    print("wrote fig1-empty-corner.png, fig2-five-sources.png, fig3-passive-vs-active.png")
