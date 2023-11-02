.. _tab aim:

Aim
###

In this tab the user can define what he or she is going to be calculating in this specific scenario.

Determine temperature profile
*****************************
This is the most basic and widely used functionality within GHEtool. If you have a certain (geothermal) heating and cooling demand given
and you select a specific borefield design (including the borehole depth), this aim will give you the temperature profile back.
It can be used with both a monthly load profile and an hourly load profile (see also :ref:`tab thermal demand`).

.. note::
If you want to use an hourly profile with this aim, you need to set the software to use the hourly profile under the tab :ref:`tab options`.

Determine required depth
************************
If you have a certain (hourly) load profile given even as the borefield configuration, this method calculates the required borehole depth
so that the load can be achieved by the borefield. There are three different methods implemented for this calculation, which are explained
in depth here: :ref:`sizing methods`.

.. warning::
    This method can sometimes give you the answer that no solution can be found.
    If you are using a ground model with a non-constant ground temperature (see :ref:`tab earth`), it is possible that it is
    impossible to put the cooling load onto the borefield.

    This can be understood as follows: if the peak cooling is too high, the algorithm will try to deepen the borefield, so there is
    less heat injection per meter borehole, lowering the temperature peaks. On the other hand, a deeper borefield means a higher
    average ground temperature. If the cooling peak is therefore too big or the borefield dimensions/temperature limits are too strict,
    it is possible that no solution can be found.

    In that case, you can try to increase the field dimensions.

Optimise load profile
*********************
Most of the times, it is economically unattractive to put 100% of your load onto a geothermal borefield, either due to high peak loads or a large imbalance.
In that case, you want to hybridise your system, but which part of the load can be put onto the borefield?
This methodology will give you back how many percentage of the heating and cooling can be full-filled geothermally and how
many peak heating/cooling has to be full-filled with another solution.

.. note::
    Since this method uses the load-duration curve of the thermal demand profile in the background,
    this method only works when **an hourly load profile** is used.
    If this is not set in the tab :ref:`tab thermal demand`, the interface disables further actions.

.. note::
    This method currently does not allow a DHW load on top of the hourly load.
    Please include your DHW load into the hourly profile if you want to take it into account.
