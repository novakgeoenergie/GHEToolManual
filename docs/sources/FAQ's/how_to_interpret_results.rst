.. _interpret results::

How to interpret temperature profiles
#####################################

At the very center of a good borefield design, is the temperature plot with the fluid temperatures. This plot
tells you everything you need to know about your design, but it also has some limitations. In this article, the interpretation
behind these temperature plots will be explained (:ref:`interpretation plots`) and also some of the effects that are not included
are discussed (:ref:`not included`).

.. tip::
    Software is built for general cases and special projects will always need special advice are custom study work.
    If you find yourself wondering if the complexity of a certain project is beyond the (current) capabilities of the software,
    you can contact us at `wouter@ghetool.eu<mailto:wouter@ghetool.eu>`_ for a specialised method or consultancy advice.
    We can help you, advice you and train you in any of the challenges below.

.. _interpretation plots::

Interpretation temperature profiles
***********************************

.. image:: Figures/results.png
  :alt: Monthly temperature profile



.. _not included::

What is not included?
*********************
Although GHEtool requires quite a lot of parameters throughout all the different tabs in order to give you back a single result,
there are a lot of things that are not taken into account and that require special attention. The design of a geothermal system,
especially for large projects, is an interesting challenge that requires a lot of knowledge next to useful tools like GHEtool Pro.

Thermal interference
--------------------
The influence of geothermal borefields does not stop at the border of the borefield, but they influence every geothermal system around them.
This can cause for example lower-than-expected ground temperatures at your location, which require other design criteria.

If you build a project in the neighbourhood of an already existing borefield,
you must be careful to take this into account when you design your system. This can be done by increasing for example the
minimum allowed average fluid temperature to create an extra safety. If you want a more robust design, you need
a specific thermal interference study.

.. image:: Figures/interference.png
  :alt: Geothermal interference
  :width: 350

Dynamic behaviour
-----------------
All the ground models within GHEtool are what is called 'static'. This means that it neglects the thermal inertia inside the fluid
and the borehole grout. Every kW of power you get outside the borefield, instantaneously is drawn from the ground.

This assumption can be seen as an intrinsic safety when designing geothermal systems, since the average fluid temperatures you
get, are mostly likely better than they will be in reality, when there is thermal inertia. If you want to lower the investment cost
of a borefield, it can be a solution to request a study for the dynamic behaviour of the geothermal system.

Varying SCOP/SEER
-----------------
GHEtool uses the assumption that the geothermal demand (see also :ref:`tab thermal demand` tab) is the same for every year.
This also implies that the SCOP and SEER are the same for both first and last year. However, if you have a system with a
(strong) imbalance, this is a very conservative assumption.

Assume, for example, that you have a imbalance which cools down the ground year after year. What happens in practise is,
that with a lower ground temperature, your SCOP will also lower, extracting less heat from the soil. This works against
the initial imbalance and compensates for this effect.

Also, when you have a lower ground temperature, the SEER will increase since heat transfer in cooling will be easier.
Besides this effect, the cooling capacity also increases, so the thermal demand will most likely not be the same throughout the years.


.. rubric:: References
.. [1] Lee, Seung-Min & Park, Seunghoon & Jang, Yong-Sung & Kim, Eui-Jong. (2021). Proposition of Design Capacity of Borehole Heat Exchangers for Use in the Schematic-Design Stage. Energies. 14. 822. 10.3390/en14040822.
