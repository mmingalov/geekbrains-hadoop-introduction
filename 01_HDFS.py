from hdfs3 import HDFileSystem
hdfs = HDFileSystem(host='89.208.221.132', port=7180)
import sys
print(sys.version)
#hdfss.ls('/')
#hdfs.put('local-file.txt', '/user/data/remote-file.txt')
#hdfs.cp('/user/data/file.txt', '/user2/data')

# 89.208.221.132 manager.novalocal
# 89.208.222.81 node1.novalocal
# 89.208.220.216 node2.novalocal
# 89.208.222.201 node3.novalocal
# https://stackoverflow.com/questions/43987081/openslide-python-import-error