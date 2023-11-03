.. caution::
    Within GHEtool, the fluid temperatures are *the average fluid temperatures*, meaning the average between the intlet
    and outlet fluid temperature. The minimum average fluid temperature is therefore not the lowest temperature you inject into
    your borefield during the heating peak, but the average between the inlet and outlet temperatures of your borefield.

    This is the case since in the background, the only temperature that matters for the heat transfer is the average fluid temperature,
    and since the inlet and outlet temperatures are depending on the mass flow rate, it is easier to work with an average temperature.

    If you typically work with, e.g. a minimum inlet temperature of 0, with a :math:`\Delta T` across your borefield of 4°C,
    you enter 2°C as a minimum average fluid temperature.