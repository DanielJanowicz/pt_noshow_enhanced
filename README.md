# Exploring causes of Patient No Shows
Aiming to research the variables that come into effect that can hinder patients from attending their medical appointments and skip them entirely.  This was completed in 4-part structure:

1. Research
2. Enhancement
3. Visualization
4. Statistical & ML Insight

Results will be posted below in this file; however, investigate the data provided in this repository to ultimately come up with your own decisions.

## Prerequisites: 
- [Python 3.10.9](https://www.python.org/downloads/) or later for Windows, MacOS & Linux
- [Anaconda Navigator](https://www.anaconda.com/) compatible with Python 3.9 or later.
- [Pip 21.3](https://pip.pypa.io/en/stable/) or later

## Packages: 
```python
    import pandas as pd
    import numpy as np
    import strealit as st
    from sklearn.metrics import accuracy_score
    from sklearn.model_selection import train_test_split
    from supervised.automl import AutoML
    import datetime as dt
    import re
    import math
    import random
    import researchpy as rp
    import scipy.stats as stats
```

## External Data:
- [U.S. County-Level COVID-19 Data](https://github.com/nytimes/covid-19-data)
- [Zipcode to County FIPS](https://www.huduser.gov/portal/datasets/usps_crosswalk.html)

## Structured Documentation:
Each aforementioned structure has its own unique markdown file with its association.  They have been placed in their respective field in order to provide clear information on that specific topic.  Here is a directory for each documentation file:

1. Research

- ahi-competition/research/[PubMed.md](https://github.com/DanielJanowicz/ahi-competition/blob/main/research/PubMed.md)

2. Enhancement

- ahi-competition/scripts/[enhancements.md](https://github.com/DanielJanowicz/ahi-competition/blob/main/scripts/enhancements.md)

3. Visualization

- ahi-competition/visuals/[streamlit.md](https://github.com/DanielJanowicz/ahi-competition/blob/main/visuals/streamlit.md)

4. Statistical & ML Insight

- ahi-competition/insights/[stats_ml.md](https://github.com/DanielJanowicz/ahi-competition/blob/main/insights/stats_ml.md)

## Usage:
The results and insights from this repository is __not__ a final answer to the complex question that has been posed, but rather a staging point for further research.  Information from this repository should not be taken to be 100% accurate, as not all variables or circumstances were taken into consideration.  This is foundational work.

## Results:
tba

## License:
[GNU GENERAL PUBLIC LICENSE](https://www.gnu.org/licenses/gpl-3.0.en.html)