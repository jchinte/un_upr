import os, errno
import mimetypes
from os.path import join


hard_coded_path = '/home/jchinte/git/benetech/un_upr/env'
truePath = join(os.path.abspath(os.path.curdir), 'env')
    
print "target: " + truePath

def inplace_change(filename, old_string, new_string):
    #safely read the input filename using 'with'
    isSymlink = False
    try:
        isSymlink = os.path.islink(filename)
        with open(filename) as f:
            s = f.read()
            if old_string not in s:
                #print '"{old_string}" not found in {filename}.'.format(**locals())
                return
    except IOError, e:
        if isSymlink:
            if os.path.exists(join(truePath, os.path.basename(filename))):          
                os.remove(filename)
                os.symlink(join(truePath, os.path.basename(filename)), filename)
                return
        raise e
    with open(filename, 'w') as f:
        print 'Changing "{old_string}" to "{new_string}" in {filename}'.format(**locals())
        s = s.replace(old_string, new_string)
        f.write(s)

def main():
    
    for root, dirs, files in os.walk('env'):
        print root, ":"
        for f in files:
            fname = join(root, f)
            mime = mimetypes.guess_type(fname)
            if mime[0] and (mime[0].find('application')!=-1):
                continue
            #print '\t'+fname+'\t' + str(mime)
            inplace_change(fname, hard_coded_path, truePath)
            
    
main()