.. warning::
    This method can sometimes give you the answer that no solution can be found.
    If you are using a ground model with a non-constant ground temperature (see :ref:`tab earth`), it is possible that it is
    impossible to put the cooling load onto the borefield.

    This can be understood as follows: if the peak cooling is too high, the algorithm will try to deepen the borefield, so there is
    less heat injection per meter borehole, lowering the temperature peaks. On the other hand, a deeper borefield means a higher
    average ground temperature. If the cooling peak is therefore too big or the borefield dimensions/temperature limits are too strict,
    it is possible that no solution can be found.

    In that case, you can try to increase the field dimensions.