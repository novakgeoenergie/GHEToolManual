.. _reynolds number:

What is the Reynolds number?
##########################################

The borehole equivalant thermal resistance is a rather important parameter in the design of borefields, and it is significantly influenced by the Reynolds number.
But what is this number exactly.

The Reynolds number
===================

The Reynolds number is a non-dimensional number, i.e. a number without a unit, which tells you something about the fluid regime inside the borefield.

A turbulent regime, is good for heat transfer giving a lower thermal resistance, but causing higher pressure drops.

Laminar regime, is not as good for heat transfer giving a higher thermal resistance, but it has lower pressure drops and hence pumping costs.

The transition between a laminar and a turbulent flow, is not very clear and within GHEtool it is assumed to be laminar below Re<2300 and turbulent for Re>4000.
Everything in between is interpolated. This approach follows (Gnielinski, 2013) [1]_.

.. note::
    The Reynolds number is calculated as follows:
    :math:`\frac{\rho D \dot{V}}{\mu}`
    Where:

    * :math:`\rho` is the density of the fluid [kg/m³]

    * :math:`D` is the diameter of the tube [m]

    * :math:`\dot{V}` is the speed of the fluid inside the pipe [m/s]

    * :math:`\mu` is the dynamic viscosity of the fluid [Pa s]


Influence of the reference temperature
======================================

Within GHEtool, the fluid temperatures are *the average fluid temperatures*, meaning the average between the intlet
and outlet fluid temperature. The minimum average fluid temperature is therefore not the lowest temperature you inject into
your borefield during the heating peak, but the average between the inlet and outlet temperatures of your borefield.

This is the case since in the background, the only temperature that matters for the heat transfer is the average fluid temperature,
and since the inlet and outlet temperatures are depending on the mass flow rate, it is easier to work with an average temperature.

If you typically work with, e.g. a minimum inlet temperature of 0, with a :math:`\Delta T` across your borefield of 4°C,
you enter 2°C as a minimum average fluid temperature.

.. note::
    In a following version of GHEtool this reference temperature will be automatically chosen based on the calculated fluid temperatures.

.. rubric:: References
.. [1] Gnielinski, V. (2013). On heat transfer in tubes. International Journal of Heat and Mass Transfer, 63, 134–140. https://doi.org/10.1016/j.ijheatmasstransfer.2013.04.015