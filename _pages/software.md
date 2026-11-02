---
layout: page
permalink: /software/
title: software
description: Open-source software from my research.
nav: false
nav_order: 7
sitemap: false
---

<div class="row" style="align-items: flex-start; margin-top: 1rem;">
  <div class="col-sm-2" style="text-align: center; margin-bottom: 1rem;">
    <img src="https://raw.githubusercontent.com/giannis00/PhasmaNet-SNR/main/assets/phasmanet_symbol.png" alt="PhasmaNet symbol" style="width: 100%; max-width: 110px;">
  </div>
  <div class="col-sm-10">
    <h2 style="margin-top: 0;">PhasmaNet</h2>
    <p><strong>A deep learning library for tabular data, built on PyTorch.</strong></p>
    <p>
      PhasmaNet (from Greek <em>φάσμα</em>, spectrum) is a compact neural architecture for structured tabular data.
      Learned input tokens are refined by an ordered cascade of attention-based Φ-Stages, each followed by a
      Φ-Refractor subspace-mixing module, and then revisited through gated top-down Φ-Feedback passes.
    </p>
    <p>
      The package provides <code>PhasmaNetRegressor</code> and <code>PhasmaNetClassifier</code>, estimators with the familiar
      <code>fit</code> / <code>predict</code> interface that work on any table of numerical features and with scikit-learn tools,
      together with the PyTorch module itself and a rank-preserving calibration step.
    </p>
    <p>
      <strong>Application: gravitational waves.</strong> The package includes a pretrained surrogate for the phase-averaged
      optimal signal-to-noise ratio of precessing, higher-mode binary black hole signals (<code>phasmanet.gw.optimal_snr</code>).
    </p>
    <pre><code>pip install phasmanet</code></pre>
    <p style="font-size: 0.9rem;">
      Ioannis Tsioulis, Anastasios Tefas, Nikolaos Stergioulas. MIT licence. Python 3.9 or later.
    </p>
    <p>
      <a class="btn btn-sm z-depth-0" role="button" href="https://pypi.org/project/phasmanet/" target="_blank" rel="noopener">PyPI</a>
      <a class="btn btn-sm z-depth-0" role="button" href="https://github.com/giannis00/PhasmaNet-SNR" target="_blank" rel="noopener">GitHub</a>
    </p>
  </div>
</div>
