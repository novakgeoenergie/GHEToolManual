.. _tab earth:

Earth
#####
The earth tab contains information w.r.t. the ground parameters and also the fluid parameters.
Both are explained below.

Earth properties
================
.. image:: Figures/earth_properties.png
  :alt: Earth properties

Temperature constraints and simulation period
=============================================
Here you enter parameters w.r.t. the temperature boundaries.
Since it is important that over time the ground temperature stays between certain limits,
this information is asked on this page.

* **Minimum average fluid temperature [°C]** The minimum average fluid temperature (i.e. the temperature in heating)
* **Maximum average fluid temperature [°C]** The maximum average fluid temperature (i.e. the temperature in cooling)

.. include:: ../General/caution_temperatures.rst

* **Simulation period [years]** The simulation period in years, oftentimes between 20-60 years.
* **Peak duration heating [hours]** The duration of the peak in heating. For slower emission systems, this is longer.
* **Peak duration cooling [hours]** The duration of the peak in cooling. For slower emission systems, this is longer and typically lower than the duration for the heating peak.

.. image:: Figures/temperature_constraints.png
  :alt: Temperature constraints and simulation period

.. note::
    Please note that the peak duration heating and peak duration cooling option is not always visible.
    It can be hidden when you use calculate using hourly data.
