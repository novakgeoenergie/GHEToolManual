Within GHEtool, you can set a reference temperature for your fluid parameters (see :ref:`tab thermal resistance`), which
has an influence on the Reynolds number and hence the thermal behaviour of your system. By default, this reference temperature is 10°C,
which is more or less the undisturbed ground temperature.

If you want a more conservative approach, you can set this temperature to the maximum or minimum average fluid temperature.
In that case you are sure that, whenever the thermal resistance matters the most (i.e. during the peak loads), they are calculated
with the worst case fluid parameters.