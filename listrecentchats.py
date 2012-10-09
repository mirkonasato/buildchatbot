import platform
from Skype4Py import Skype

if platform.system() == 'Windows':
  skype = Skype()
else:
  skype = Skype(Transport='x11')
skype.Attach()
for chat in skype.RecentChats:
  print '"%s" -> "%s"' % (chat.FriendlyName, chat.Name)

