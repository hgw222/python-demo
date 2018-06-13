#!/usr/bin/python
# -*- coding: UTF-8 -*-
import jenkins

server = jenkins.Jenkins('http://172.20.11.110:8080', username='admin', password='hll111111')
user = server.get_whoami()
print 'user====>',user