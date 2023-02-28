import docker
import simplejson as json
from subprocess import check_output






client = docker.from_env()
checkmk_data={}
#servicelist = client.services.list()
dockerstats =  ''''b\'"mintsd_hpsm.1.26a7cokbz6ol1enowf4i3qya9 0.34% 8.57%"'''
stats = dockerstats.replace('%','').replace('\\n\\','').splitlines()
print(stats)
exit()

