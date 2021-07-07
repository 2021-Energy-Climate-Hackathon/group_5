# Linking Results of Power System Expansion Optimizations to Differences in Meteorological Inputs
## Resources, outputs and findings from group 5 of the 2021 Energy-Climate Hackathon

### Introduction
The weather-driven availability of the variable renewable resources (VRES) is one of the key inputs to numerical power system expansion models. Commonly, this information is derived from a meteorological data set, which covers a relatively short time period compared to the variability time scales of weather and climate. Hence, the variability of the availability of the VRES is only partially captured by the power system models. Furthermore, the connection between the meteorological inputs and the simulation results are not fully understood. In power system optimization models, the meteorological parameters co-act with the other techno-economical parameters and determine the optimization results [[Schyska et al., 2020]](#2).

Aim of this project is the investigation of the effect of varying meteorological inputs on the results of numerical power system optimization models by describing the relation between the meteorological input and the optimization results in a statistically concise manner. Therefore, we used the data of Schlott et al. [[2018]](#1), which provides the meteorological input time series as well as the optimization results for three different climate models, the RCP8.5 scenario and the time span 1970 through 2100 devided into 5-6 year slices.

### About this Repository
During the 2021 Energy-Climate Hackathon a few first steps to investigate the differences in the meteorological input data sets as well as in the results of the power system optimizations using these data sets have been conducted. This repository includes the python scripts and notebooks created for this purpose. It's work in progress. Note that the raw data, and `pickle` files generated from the raw data, that were ued in the analyses have not been included in this repository because they are very large in data size and we do not want to make the repository very slow to load. Therefore the data directory as-is only contains some CSV files generated from the raw data.
  
### LICENCE
Copyright (C) 2021 Sadie Bartholomew (NCAS-CMS), Jaap Pedersen (ZIB), Eugenio Salvador Arellano Ruiz (DLR), Johannes Schwenzer, Matthias Zech (DLR), Bruno Schyska (DLR)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>

### References
<a id="1">[Schlott et al.]</a> Schlott, M., Kies, A., Brown, T., Schramm, S., & Greiner, M. (2018). The impact of climate change on a cost-optimal highly renewable European electricity network. Applied energy, 230, 1645-1659, <https://arxiv.org/pdf/1805.11673>.

<a id="2">[Schyska et al.]</a> Schyska, B. U., Kies, A., Schlott, M., von Bremen, L., & Medjroubi, W. (2020). The Sensitivity of Power System Expansion Models. arXiv preprint arXiv:2007.09956, <https://arxiv.org/pdf/2007.09956>.
