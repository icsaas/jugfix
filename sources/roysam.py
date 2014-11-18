from __future__ import with_statement, division
from scipy import ndimage
import numpy as np
from juglib.task import Task, TaskGenerator
import pyslic
from pyslic.image import loadedimage
import pyslic.segmentation.roysam
from images import load_aabid

@TaskGenerator
def compute_mu_sigma(col):
    aabids = [np.array(load_aabid(col,i).tolist()) for i in xrange(5)]

    # print type(aabids)
    # print aabids[0]
    print type(aabids[0])
    print aabids[0].dtype
    return pyslic.segmentation.roysam.train_classifier(aabids)

classif_ic100 = compute_mu_sigma('ic100')
classif_gnf = compute_mu_sigma('gnf')

@TaskGenerator
def roysam_seg(img, classif):
    with loadedimage(img):
        dna = img.get('dna')
        return pyslic.segmentation.roysam.greedy_roysam_merge(dna,classif)

def compute_roysams(ic100_imgs,gnf_imgs):
    roysams_ic100 = [roysam_seg(img,classif_ic100) for img in ic100_imgs]
    roysams_gnf = [roysam_seg(img,classif_gnf) for img in gnf_imgs]
    return roysams_ic100 + roysams_gnf

@TaskGenerator
def roysam_seg_mean(img,classif):
    with loadedimage(img):
        dna = img.get('dna')
        return pyslic.segmentation.roysam.greedy_roysam_merge(dna,classif,dna.mean())

def compute_roysams_mean(ic100_imgs,gnf_imgs):
    roysams_ic100 = [roysam_seg_mean(img,classif_ic100) for img in ic100_imgs]
    roysams_gnf = [roysam_seg_mean(img,classif_gnf) for img in gnf_imgs]
    return roysams_ic100 + roysams_gnf

@TaskGenerator
def filter_small_nuclei(img, min_size=2500):
    img = img.copy()
    N = img.max()
    obj = 1
    while obj <= N:
        if (img == obj).sum() < min_size:
            img[img == obj] = 0
            img[img > obj] -= 1
            N -= 1
        else:
            obj += 1
    return img
