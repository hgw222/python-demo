#!/usr/bin/python
# -*- coding: UTF-8 -*-
import jenkins

server = jenkins.Jenkins('http://172.20.11.214:8080', username='admin', password='hll111111')
# user = server.get_whoami()
# print 'user====>',user
job_info = server.get_job_info('im-server')
print job_info['lastBuild']['number']
