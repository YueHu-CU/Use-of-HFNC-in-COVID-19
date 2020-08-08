## About
This repository contains code and the data for the working paper: **The Impact of High-Flow Nasal Cannula Use on Patient Mortality and the Availability of Mechanical Ventilators in COVID-19**. 

Authors: **Hayley B. Gershengorn<sup>1,2</sup>, Yue Hu<sup>3</sup>, Jen-Ting Chen<sup>2</sup>, S. Jean Hsieh<sup>4</sup>, Jing Dong<sup>3</sup>, Michelle Ng Gong<sup>2</sup>, Carri Chan<sup>3</sup>**. 

1.	Division of Pulmonary, Critical Care, and Sleep Medicine, University of Miami Miller School of Medicine, Miami, FL, USA.
2.	Division of Critical Care Medicine, Albert Einstein College of Medicine, Bronx, NY, USA.
3.	Division of Decision, Risk, and Operations, Columbia University Business School, New York, NY, USA.
4.	Division of Pulmonary, Critical Care, and Sleep Medicine, Mount Sinai School of Medicine, New York, NY, USA.

## Software
Python is our programming language. You will need the following Python packages:

- \_future\_ (for Python versions prior to 3.0)

- itertools

- Matplotlib

- NumPy

- pandas

- random

- SciPy

- Seaborn

## Data
The `Data` folder contains the data files to replicate results in the paper, which were obtained from the following sources:

- IHME COVID-19 Projections: https://covid19.healthdata.org/united-states-of-america (accessed on 2020-08-02)

- COVID-19 Forecast Hub: https://viz.covid19forecasthub.org (accessed on 2020-08-02)

## Code

The `Home` folder contains the code to replicate results in the paper. 

The `Data` folder should be placed within a parent folder that contains all the code. 

Some codes are to be run sequentially. <!-- For example, to examine the impact of use of high-flow nasal cannula on mortality in the United States (Figure 2 in the paper), you will need to first select the appropriate national-level parameters in `Parameters.py`, and then run `Compare Policies.py` to obtain the output.--> Please contact the authors of the paper for guidance or clarification on using the code.
