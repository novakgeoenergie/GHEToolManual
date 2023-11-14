.. _interpret results::

How to interpret temperature profiles
#####################################

At the very center of a good borefield design, is the temperature plot with all the fluid temperatures. This plot
tells you everything you need to know about your design, but it also has some limitations. In this article, the interpretation
behind those temperature plots will be explained (:ref:`interpretation plots`) and also some of the effects that are not included
are discussed (:ref:`not included`).

.. tip:: Test 1,2,3
    Software is designed for general cases, and special projects will always require customized advice or a tailored study.
    If you find yourself questioning whether the complexity of a particular project exceeds the current capabilities of the software,
    feel free to reach out to us at `wouter@ghetool.eu <mailto:wouter@ghetool.eu>`_ for a specialised method or consultancy advice.
    We can provide tailored guidance and assistance to address any challenges you may encounter, along with general training in borefield design.

.. _interpretation plots::

Interpretation temperature profiles
***********************************

.. image:: Figures/results.png
  :alt: Monthly temperature profile



.. _not included::

What is not included?
*********************

While GHEtool demands numerous parameters across its various tabs to generate a single result, it is essential to note that
certain factors are not considered and merit special attention. The design of a geothermal system, particularly for large projects,
poses an intriguing challenge that necessitates extensive knowledge, complemented by valuable tools such as GHEtool Pro.

Thermal interference
--------------------
The influence of geothermal borefields extends beyond the borders of the borefield, affecting every geothermal system in their vicinity.
This influence can lead, for example, to lower-than-expected ground temperatures at your location, necessitating adjustments to the design criteria.

When undertaking a project in proximity to an existing borefield, it is crucial to carefully consider this influence during the system design.
One approach is to increase, for instance, the minimum allowed average fluid temperature to introduce an additional layer of safety.
For a more robust design, a specific thermal interference study is necessary.

.. image:: Figures/Interference.png
  :alt: Geothermal interference
  :width: 300
  :align: center

Dynamic behaviour
-----------------
All the ground models within GHEtool are what is called 'static.' This means that it neglects the thermal inertia inside the fluid and the borehole grout.
Every kilowatt (kW) of power you obtain outside the borefield is drawn instantaneously from the ground.

This assumption can be seen as an intrinsic safety feature when designing geothermal systems, as the average fluid temperatures
you obtain are most likely better than they will be in reality when there is thermal inertia.
If you want to reduce the investment cost of a borefield, it can be a solution to request a study on the dynamic behavior of the geothermal system.

Varying SCOP/SEER
-----------------
GHEtool operates under the assumption that the geothermal demand (refer to the :ref:`tab thermal demand` tab) remains
constant every year. This also implies that the Seasonal Coefficient of Performance (SCOP) and Seasonal Energy Efficiency Ratio (SEER)
are identical for both the first and last years. However, in the case of a system with a significant imbalance, this assumption is highly conservative.

For instance, consider a scenario where there is a persistent imbalance that progressively cools down the ground each year.
In practice, as the ground temperature decreases, the SCOP will also decrease, resulting in less heat being extracted from the soil.
This counteracts the initial imbalance, compensating for its effects.

Moreover, with a lower ground temperature, the SEER will likely increase due to the improved heat transfer during cooling.
Additionally, the cooling capacity increases, making it improbable for the thermal demand to remain constant throughout the years.

.. rubric:: References
.. [1] Lee, Seung-Min & Park, Seunghoon & Jang, Yong-Sung & Kim, Eui-Jong. (2021). Proposition of Design Capacity of Borehole Heat Exchangers for Use in the Schematic-Design Stage. Energies. 14. 822. 10.3390/en14040822.
