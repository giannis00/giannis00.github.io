---
layout: page
permalink: /software/
title: software
description: Open-source software from my research.
nav: true
nav_order: 4.5
---

<div class="row" style="align-items: flex-start; margin-top: 1rem;">
  <div class="col-sm-2" style="text-align: center; margin-bottom: 1rem;">
    <img src="https://raw.githubusercontent.com/giannis00/PhasmaNet-SNR/main/assets/phasmanet_symbol.png" alt="PhasmaNet symbol" style="width: 100%; max-width: 110px; background: #ffffff; padding: 10px; border-radius: 6px;">
  </div>
  <div class="col-sm-10">
    <h2 style="margin-top: 0;">PhasmaNet</h2>
    <p><strong>A deep learning library for tabular data.</strong></p>
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
    <h3 style="margin-top: 1.8rem;">Benchmarks on public tabular data</h3>
    <p>
      The paper tests PhasmaNet on three standard public benchmarks, one regression and two classification problems,
      against the nine deep tabular architectures reported by
      <a href="https://arxiv.org/abs/2106.11959" target="_blank" rel="noopener">Gorishniy et al. (2021)</a>, on the same
      train, validation and test splits. PhasmaNet was run out of the box, with no tuning on these datasets, while each
      reference model was tuned per dataset.
    </p>
    <div class="table-responsive">
    <table class="table table-sm" style="font-size: 0.9rem;">
      <thead>
        <tr><th>Dataset</th><th>Task</th><th>Features</th><th>Metric</th><th>PhasmaNet (untuned)</th><th>Rank</th><th>Best tuned model</th></tr>
      </thead>
      <tbody>
        <tr><td>Covertype</td><td>classification, 7 classes</td><td>54</td><td>accuracy (higher is better)</td><td><strong>0.9664</strong></td><td><strong>2 of 9</strong></td><td>FT-Transformer 0.970</td></tr>
        <tr><td>YearPredictionMSD</td><td>regression</td><td>90</td><td>RMSE (lower is better)</td><td><strong>8.874</strong></td><td>6 of 10</td><td>NODE 8.784</td></tr>
        <tr><td>Epsilon</td><td>binary classification</td><td>2,000</td><td>accuracy (higher is better)</td><td><strong>0.8915</strong></td><td>9 of 10</td><td>FT-Transformer 0.8982</td></tr>
      </tbody>
    </table>
    </div>
    <p style="font-size: 0.9rem;">
      On Covertype, PhasmaNet is ahead of seven of the eight other architectures with a result. Epsilon, with 2,000 input
      features, is a deliberate stress test: all ten models lie within about 0.9 percentage points of accuracy there.
    </p>
    <h3 style="margin-top: 1.8rem;">Install</h3>
    <pre><code>pip install phasmanet</code></pre>
    <p style="font-size: 0.9rem;">
      Ioannis Tsioulis, Anastasios Tefas, Nikolaos Stergioulas. MIT licence. Python 3.9 or later. The current release runs on PyTorch.
    </p>
    <p>
      <a class="btn z-depth-0" role="button" style="font-size: 0.95rem; padding: 0.35rem 1rem; margin-right: 0.5rem; border: 1px solid var(--global-theme-color); border-radius: 4px;" href="https://giannis00.github.io/PhasmaNet-SNR/" target="_blank" rel="noopener">Docs</a>
      <a class="btn z-depth-0" role="button" style="font-size: 0.95rem; padding: 0.35rem 1rem; margin-right: 0.5rem; border: 1px solid var(--global-theme-color); border-radius: 4px;" href="https://pypi.org/project/phasmanet/" target="_blank" rel="noopener">PyPI</a>
      <a class="btn z-depth-0" role="button" style="font-size: 0.95rem; padding: 0.35rem 1rem; margin-right: 0.5rem; border: 1px solid var(--global-theme-color); border-radius: 4px;" href="https://github.com/giannis00/PhasmaNet-SNR" target="_blank" rel="noopener">GitHub</a>
      <span class="btn z-depth-0" role="button" aria-disabled="true" title="The arXiv link will be added as soon as the identifier is assigned" style="font-size: 0.95rem; padding: 0.35rem 1rem; margin-right: 0.5rem; border: 1px dashed var(--global-theme-color); border-radius: 4px; opacity: 0.6; cursor: default;">Paper (arXiv, soon)</span>
    </p>
  </div>
</div>
