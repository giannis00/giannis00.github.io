---
layout: page
title: NiceMove — AI-Powered Move Smart-Contract Linter
description: A VS Code extension that detects issues in Sui Move smart contracts locally, with frontier-model fixes on demand.
img: assets/img/nicemove_icon.png
importance: 3
category: work
website: https://marketplace.visualstudio.com/items?itemName=BakalisVasilis.nicemove
---

**NiceMove** is a VS Code extension for Move developers that flags smart-contract issues — missing authorisation checks, unsafe transfers, dead code, and logic errors — inline as you write. Detection runs on a small, specialised model locally: fast, private, and free to run. When a fix is needed, the issue is handed to Claude Code for a concrete correction.

The detection model was trained at minimal cost on ordinary hardware with no cloud GPUs. In our preliminary evaluation it reached ~99% accuracy on the classification task, outperforming general-purpose LLMs used out-of-the-box — a small, specialised local model beating much larger general ones at a fraction of the cost.

The model and extension were brought to their final form by **Vasilis Bakalis** as part of his thesis at Mediterranean College. The underlying dataset (~3,300 labelled Sui Move snippets) was produced by the student team I supervised and is archived on Zenodo.

**Collaboration:** SuiHub Athens / Mysten Labs

<div class="links mt-3">
  <a href="https://marketplace.visualstudio.com/items?itemName=BakalisVasilis.nicemove" class="btn btn-sm z-depth-0" role="button" target="_blank">VS Code Marketplace</a>
  <a href="https://doi.org/10.5281/zenodo.19682589" class="btn btn-sm z-depth-0" role="button" target="_blank">Dataset (Zenodo)</a>
</div>
