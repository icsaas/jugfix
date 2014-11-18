from __future__ import with_statement, division
from juglib.task import Task, TaskGenerator
import numpy as np
from scipy import ndimage
import pyslic
import pymorph
import morph

segment_watershed = TaskGenerator(pyslic.segmentation.watershed.watershed_segment)

@TaskGenerator
def extend_R(R):
    return morph.cwatershed(np.zeros(R.shape,np.uint8),R)

