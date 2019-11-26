[![Build Status](https://travis-ci.com/MFTabriz/reaction_pypaths.svg?branch=master)](https://travis-ci.com/MFTabriz/reaction_pypaths)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/MFTabriz/reaction_pypaths.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/MFTabriz/reaction_pypaths/context:python)

## reaction_pypaths
A simple yet flexible python script for drawing reaction path energy diagrams.

### Customization
All the diagram parameters can be tweaked in the [configs.py](https://github.com/MFTabriz/reaction_pypaths/blob/master/configs.py) file.
Check out the [matplotlib guide](https://matplotlib.org/tutorials/text/usetex.html) on the text rendering with LaTeX.

### Requirements
The script is written for python 3 and relies on the [matplotlib](https://matplotlib.org/) module for drawing the diagrams which in turn uses the [TeX Live](https://tug.org/texlive/) for generating the labels in the TeX format.

### Example
```python
import reaction_pypaths

energy_plot = reaction_pypaths.Diagram()

# add levels to the diagram
FORMULA1 = energy_plot.add_level(1.1, "crazy formula $[ZX_2]_5^{+}$")
PMM14 = energy_plot.add_level(-0.1, "$(PMM14)_3$", True)
PZX14_mix = energy_plot.add_level(-0.5, "$(PZX14)_3 + P4$")
TS = energy_plot.add_level(0, "TS")
PD1 = energy_plot.add_level(-1.1, "product 1")
PD2 = energy_plot.add_level(-0.4, "product 2")

# add links between the levels
energy_plot.add_link(FORMULA1, PZX14_mix)
energy_plot.add_link(PMM14, PZX14_mix)
energy_plot.add_link(PZX14_mix, TS)
energy_plot.add_link(TS, PD1)
energy_plot.add_link(TS, PD2)

# plot the diagram and save the final result to the file
energy_plot.plot("output.png")
```
![Sample diagram](https://github.com/MFTabriz/reaction_pypaths/raw/master/output.png)

### License and attributions
reaction_pypaths is available under the [GNU GPL v3+] (attribution: MFTabriz@github)
