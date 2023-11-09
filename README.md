# CS5610 Assignments

## Initialization

Install the latest versions of dependencies via chocolatey

```PowerShell
& choco install python
& choco install mingw
& choco install rust
```

Configure a python virtual environment for the class (from the project directory):

```PowerShell
& python -m venv cs5610
& ./cs5610/Scripts/activate.ps1
& pip install -U pip wheel
& pip install numpy scipy matplotlib pandas scikit-learn `
	seaborn patsy statsmodels jupyter `
	pyarrow `
	graphviz `
	xlrd
```

NOTE: Install other required packages to this virtual environment.
There was at least one but I didn't write it down when I installed it.


At some point, I needed to run `pip install -U scikit-learn` to get `sklearn` imports to work.

## Other Dependencies For PDF Export

```PowerShell
& choco install pandoc
```

Download and install [MiKTeX](https://miktex.org/download) (required for notebook exports).
Follow the prompts to install updates after initial installation.
NOTE: I required a reboot to ensure `xelatex` was correctly path'd for exports.

## Other Dependencies for GraphViz (Decision Tree visualizer)

Download and install graphviz:
https://gitlab.com/api/v4/projects/4207231/packages/generic/graphviz-releases/9.0.0/windows_10_cmake_Release_graphviz-install-9.0.0-win64.exe


NOTE: The `choco install -y graphviz` does not work and complains it does not support 64-bit architecture.

## Local Development

From the project directory:

```PowerShell
& ./cs5610/Scrtips/activate.ps1
& jupyter notebook
```

This will start the jupyter notebook web interface where you can do your development.
