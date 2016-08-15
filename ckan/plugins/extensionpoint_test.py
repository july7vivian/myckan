#encoding: utf-8
from pyutilib.component.core import ExtensionPoint
from pyutilib.component.core import Interface, implements
from pyutilib.component.core import Plugin, SingletonPlugin
import pprint

class IMyInterface (Interface) :
	'''my interface'''
	# pass 
	

class MyPlugin(SingletonPlugin):
	implements(IMyInterface)

	def __init__(self):
		self.name='myname'




class MySingletonPlugin(SingletonPlugin):
	implements(IMyInterface)

	def __init__(self):
		self.name = "mysingletonname"


class MySingletonPlugin2(SingletonPlugin):
	implements(IMyInterface)

	def __init__(self):
		self.name = "mysingletonname2"

class MySingletonPlugin3(SingletonPlugin):
	implements(IMyInterface)

	def __init__(self):
		self.name = "mysingletonname2"


service1 = MyPlugin()
service2 = MyPlugin()
service3 = MyPlugin()
service4 = MySingletonPlugin()
service5 = MySingletonPlugin()
print service5
print type(service5)
print type(MySingletonPlugin3)

ep = ExtensionPoint(IMyInterface)
print len(ep('mysingletonname2'))
print len(ep.extensions(all = True))
print 'extensions' 
for p in ep:
	print p
	
print 'service'
print  ep.service('')

# conclusion: ep() or ep or ep.extension 中包含的是实现接口的类，而不是具体的service实例
# 并且好像，要继承singtonplugin才能被识别，plugin不行 