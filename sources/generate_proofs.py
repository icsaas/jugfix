from pylab import *
import numpy
import numpy as np
from images import *                           
from aabid import *
from segment_base import *
from segment_base import *
from aabid import *
from segment_base import *
def borders(img):
    res = np.zeros(img.shape,bool)
    res[:-1,:-1] = (img[:-1,:-1] != img[:-1,1:])
    res[1:,:] |= (img[1:,:] != img[:-1,:])
    res[:,1:] |= (img[:,1:] != img[:,:-1])
    return res

for idx,r,img in zip(xrange(48),gnf_ref,gnf_imgs):
    dna=img.get('dna')
    img.unload()
    rr = load_ref('gnf',gnf_idxs[idx])
    rr2 = r.result
    if np.all(rr == rr2): continue
    clf()
    imshow(pymorph.overlay(dna,borders(rr)))
    savefig('t/gnf_b%s.png' % idx)
    r.unload()
    
for idx,r,img in zip(xrange(48),ic100_ref,ic100_imgs):
    dna=img.get('dna')
    img.unload()
    rr = load_ref('ic100',ic100_idxs[idx])
    rr2 = r.result
    if np.all(rr == rr2): continue
    clf()
    imshow(pymorph.overlay(dna,borders(rr)))
    savefig('t/ic100_b%s.png' % idx)
    r.unload()
    
for idx,r,img in zip(xrange(5),aabids[5:10],gnf_imgs):
    dna=img.get('dna')
    img.unload()
    rr = load_ref('gnf',gnf_idxs[idx])
    rr2 = r.result
    if np.all(rr == rr2): continue
    clf()
    imshow(pymorph.overlay(dna,borders(rr)))
    savefig('t/aabid_gnf_b%s.png' % idx)
    r.unload()
    
for idx,r,img in zip(xrange(5),aabids[:5],ic100_imgs):
    dna=img.get('dna')
    img.unload()
    rr = load_ref('ic100',ic100_idxs[idx])
    rr2 = r.result
    if np.all(rr == rr2): continue
    clf()
    imshow(pymorph.overlay(dna,borders(rr)))
    savefig('t/aabid_ic100_b%s.png' % idx)
    r.unload()
    
