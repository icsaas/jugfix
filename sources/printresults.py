import re
def printresults(name,inputfile):
    order = ('Jaccard','Hausdorff', 'Distances', 'Basics:Split', 'Basics:Merged', 'Basics:Added', 'Basics:Missing')
    pat = re.compile('([A-Z][A-Za-z:]+) ?\((IC100|GNF):.*\): ([0-9.]+)$')
    values = {}
    for line in file('results/'+inputfile):
        match = pat.match(line)
        if match is not None:
            dist,dataset,value = match.groups()
            values[dist,dataset] = float(value)
            
    print '%-24s &' % name,
    print '%s\\%%/%s\\%%    &' %(int(100*values['Rand','GNF']),int(100*values['Rand','IC100'])),
    for m in order:
        scale = (10 if m == 'Distances' else 1)
        print '%-16s&' % ('%.1f/%.1f'  % (scale*values[m,'GNF'],scale*values[m,'IC100'])),
    print r'\\'
printresults('AS Manual','AS.txt')
printresults('RC Threshold','rc_t.txt')
printresults('Otsu Threshold','otsu.txt')
printresults('Mean Threshold','mean_t.txt')
printresults('Watershed (direct)','watershed:direct_mean.txt')
printresults('Watershed (gradient)','watershed:gradient_mean.txt')
printresults('Active Masks','active_masks:filtered.txt')
printresults("Merging Algorithm",'roysams_mean_filter_no_AS.txt')

