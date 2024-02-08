# BE-H2-Hypatia
**Hydrogen network infrastructure model for Belgium**

[![DOI](https://zenodo.org/badge/754676270.svg)](https://zenodo.org/doi/10.5281/zenodo.10636755)

This repository contains the dataset for Belgium's long-term hydrogen infrastructure cost optimization model, focusing on the decarbonization of energy-intensive industries.

## At a glance
The MILP BE-H2-Hypatia model is developed with a high spatial and hourly temporal resolution, allowing investment and operational optimization of the prospective hydrogen infrastructure of Belgium, including the production technologies, transmission network, and storage facilities. The model can endogenously choose among the available sizes of the pipe segments (e.g., DN500mm, DN900mm, DN1200mm) to be optimally installed among each pair of nodes based on the required hourly flow capacities throughout the connections. Therefore, a few minimum investment capacities have been considered for each candidate pipe and these investments consist of certain fixed and variable costs dependent on the size. The candidate pipe sizes are taken from the values proposed by [European Hydrogen Backbone (EHB)](https://www.ehb.eu/page/publications) considering the gaseous hydrogen flow characteristics within a pipe such as the maximum possible operating flow velocity and pressure. Various scenarios, including options for green and blue hydrogen production, as well as the import of clean molecules, have been considered within the model. These scenarios are intended to provide insights into various low-carbon hydrogen supply alternatives, their associated system-Levelized Cost of Hydrogen (LCOH), and their effects on the short-term and long-term capacity adequacy of a potential national-level hydrogen network.

## More information
The model's scenarios can be executed by using the [development branch of Hypatia framework](https://github.com/Hypatia-Energy-Modelling-Framework/Hypatia/tree/development) as follows:

```
git clone https://github.com/Hypatia-Energy-Modelling-Framework/Hypatia.git
git cd Hypatia
git checkout development
```
To use the Hypatia modeling framework for this case study, please follow the steps below:

Create a new environment using a Python package management software such as [Anaconda](https://www.anaconda.com/):

```
conda create -n hypatia python=3.8
```

If you create a new environment for hypatia, you need to activate the environment each time you want to use it, by writing the following line in Anaconda Prompt:

```
conda activate hypatia
```

After activating the environment, you need to install CVXPY, version 1.1.18:

```
conda install -c conda-forge cvxpy=1.1.18
```

Change the directory of the terminal to where the Hypatia framework is cloned (where the "setup.py" file is located):

```
python setup.py bdist_wheel
pip install -e.
```

After the installation, you can run the scenarios by running the "main.py" script:

```
python main.py
```
