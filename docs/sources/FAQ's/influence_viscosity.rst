What is the effect of the Reynolds number?
##########################################

The borehole equivalant thermal resistance is a rather important parameter in the design of borefields, and it is significantly influenced by the Reynolds number.
But what is this number exactly.

    The Reynolds number is a non-dimensional number, i.e. a number without a unit, which tells you something about the fluid regime inside the borefield.
    A turbulent regime, is good for heat transfer giving a lower thermal resistance, but causing higher pressure drops.
    Laminar regime, is not as good for heat transfer giving a higher thermal resistance, but it has lower pressure drops and hence pumping costs.
    The transition between a laminar and a turbulent flow, is not very clear and within GHEtool it is assumed to be laminar below Re<2300 and turbulent for Re>4000.
    Everything in between is interpolated.

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
Within GHEtool, you can set a reference temperature for your fluid parameters (see :ref:`tab thermal resistance`), which
has an influence on the Reynolds number and hence the thermal behaviour of your system. By default, this reference temperature is 10°C,
which is more or less the undisturbed ground temperature.

If you want a more conservative approach, you can set this temperature to the maximum or minimum average fluid temperature.
In that case you are sure that, whenever the thermal resistance matters the most (i.e. during the peak loads), they are calculated
with the worst case fluid parameters.

.. note::
    In a following version of GHEtool this reference temperature will be automatically chosen based on the calculated fluid temperatures.