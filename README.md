# Spotify Discover Weekly Recommendation Model

## Project Overview

This project investigates how the proportion of familiar music in a simulated listening history relates to the diversity of unfamiliar artists and genres in a 30-track Discover Weekly-style recommendation list.

The model uses Python and Mesa to simulate a simplified genre-similarity recommendation mechanism. It does not reproduce Spotify's actual recommendation algorithm.

## Requirements

- Python
- Mesa 3.5.2

Install Mesa using:

`pip install mesa==3.5.2`

## Running the Model

Open a terminal in the project folder and run:

`python SpotifyPrototype.py`

No external datasets are required. The synthetic music library is included in the Python file.

## Experimental Conditions

- Baseline: 80% familiar music.
- Alternative: 40% familiar music.
- 60 songs in the synthetic music library.
- 20 songs per listening history.
- 30 recommendations per list.
- 30 simulations per condition.
- Controlled random seeds from 42 to 71.

## Results

| Measurement | Baseline | Alternative |
|---|---:|---:|
| Average unfamiliar artists | 4.33 | 4.33 |
| Average unfamiliar genres | 1.53 | 0.27 |

## Repository Contents

- `SpotifyPrototype.py` — Computational model.
- `outputs/` — Raw recommendations, listening histories, processed results and final comparison.
- `docs/evidence/` — Supporting evidence and input documentation.
- `docs/figures/` — Ecosystem map.

## Changes from DEL02 to DEL03

- Introduced controlled random seeds for reproducibility.
- Increased the experiment to 30 simulations per condition.
- Implemented CSV exports for raw and processed results.
- Calculated average diversity measurements.
- Added supporting evidence and documentation.

## Limitations

The model uses synthetic data, two experimental conditions and a simplified recommendation mechanism. Its results cannot be generalised to actual Spotify listeners or Spotify's recommendation algorithm. Statistical significance has not been tested.