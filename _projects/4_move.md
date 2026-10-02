---
layout: page
title: "NiceMove: AI-Powered Move Smart-Contract Linter"
description: A VS Code extension that detects issues in Sui Move smart contracts locally, with frontier-model fixes on demand.
img: assets/img/nicemove_icon.png
importance: 3
category: work
website: https://marketplace.visualstudio.com/items?itemName=BakalisVasilis.nicemove
---

**NiceMove** is a VS Code extension for Move developers that flags smart-contract issues (missing authorisation checks, unsafe transfers, dead code, and logic errors) inline as you write. Detection runs on a small, specialised model locally: fast, private, and free to run. When a fix is needed, the issue is handed to Claude Code for a concrete correction.

The detection model was trained at minimal cost on ordinary hardware with no cloud GPUs. In our preliminary evaluation it reached ~99% accuracy on the classification task, outperforming general-purpose LLMs used out-of-the-box. A small, specialised local model beating much larger general ones at a fraction of the cost.

The model and extension were brought to their final form in an MSc thesis I supervised at Mediterranean College. The underlying dataset (~3,300 labelled Sui Move snippets) was produced by a student team under my supervision and is archived on Zenodo. The students were first introduced to Move in a <a href="https://www.linkedin.com/feed/update/urn:li:activity:7424163965355626496/" target="_blank">hands-on session at SuiHub Athens</a>, and then helped collect and label the data.

**Collaboration:** <a href="https://www.sui.io/blog/suihub-athens-opens" target="_blank">SuiHub Athens</a> / <a href="https://www.mystenlabs.com" target="_blank">Mysten Labs</a>

<a href="https://sui.io" target="_blank">Sui</a> is a layer-1 blockchain whose smart contracts are written in Move. It was built by Mysten Labs, a company founded in 2021 by former Meta engineers who led the Diem blockchain and the Move language. Mysten Labs raised USD 300 million in 2022 at a valuation above USD 2 billion, and the Sui network went live in May 2023. SuiHub Athens, opened by the Sui Foundation in June 2025, is the third SuiHub worldwide after Dubai and Ho Chi Minh City.

<div style="margin-top:1.25rem;">
  <a href="https://marketplace.visualstudio.com/items?itemName=BakalisVasilis.nicemove" role="button" target="_blank" style="display:inline-block; padding:0.5rem 1.1rem; margin:0 0.6rem 0.6rem 0; border:1px solid var(--global-theme-color); border-radius:0.375rem; color:var(--global-theme-color); font-size:1rem; font-weight:500; text-decoration:none;">VS Code Marketplace</a>
  <a href="https://doi.org/10.5281/zenodo.19682589" role="button" target="_blank" style="display:inline-block; padding:0.5rem 1.1rem; margin:0 0.6rem 0.6rem 0; border:1px solid var(--global-theme-color); border-radius:0.375rem; color:var(--global-theme-color); font-size:1rem; font-weight:500; text-decoration:none;">Dataset (Zenodo)</a>
</div>
