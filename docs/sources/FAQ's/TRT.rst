.. _TRT:

How do you input a TRT?
#######################
In this short article, you will learn what a TRT-test is and how you can input its data into GHEtool.

What is a TRT-test?
===================
TRT stands for *Thermal Response Test*. It is an in-situ test to measure the ground thermal properties at a specific location.
Since all the tabulated ground data is an oversimplification of reality and ground properties play an important role in the final
design of the borefield, it is recommended to use TRT for big projects.

.. note::
    Practically, a TRT-test takes place after the first borehole has been drilled. This borehole should be representative
    for the whole borefield. A monitoring machine is connected to the pipes and a fluid starts circulating, measuring
    the initial ground temperature. After a while, the machine start injecting a constant power into the ground and measuring
    the temperature evolution of inlet and outlet. (Based on (François et al., 2016) [1]_.)

A TRT test measures three different things:

#. The initial (undisturbed) ground temperature
#. The ground thermal conductivity
#. The borehole equivalent thermal resistance

How to enter this into GHEtool?
===============================
Since a TRT measures 1) the ground temperature at infinity (i.e. the undisturbed ground temperature), 2) ground thermal conductivity and 3) the borehole thermal resistance,
we have to enter all those parameters in GHEtool.

Ground properties
-----------------
For the ground properties, you go to the :ref:`tab earth` tab and you select *Measured* as the source for the
ground temperature data. The ground thermal conductivity you can enter straight away.

In the example below, the TRT measured a thermal conductivity of 1.85W/mK and an undisturbed ground temperature of 11.83°C.

.. image:: Figures/earth_properties_TRT.png
  :alt: Earth properties

Borehole thermal resistance
---------------------------
To set the value of the borehole thermal resistance, you go to the :ref:`tab options` tab and select *constant*
for the borehole resistance. Next, you go to the :ref:`tab thermal resistance` tab and you enter the value
from the TRT.

.. include:: ../General/warning_TRT.rst

.. rubric:: References
.. [1] François L., Van de Bossche P., Van Lysebetten, G. (2016) Technische voorlichting (259): Ondiepe geothermie, ontwerp en uitvoering van bodemenergiesystemen met U-vormige bodemwarmtewisselaars (in Dutch).