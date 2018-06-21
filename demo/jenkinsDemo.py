#!/usr/bin/python
# -*- coding: UTF-8 -*-
import jenkins

server = jenkins.Jenkins('http://172.20.11.214:8080', username='admin', password='hll111111')
# user = server.get_whoami()
# print 'user====>',user

# job_info = server.get_job_info('im-server')
# print job_info['lastBuild']['number']

job_build_detail = server.get_build_info('php001', 2)
print 'job_detail====>',job_build_detail
