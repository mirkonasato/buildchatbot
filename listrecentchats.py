from Skype4Py import Skype

skype = Skype()
skype.Attach()
for chat in skype.RecentChats:
  print '"%s" -> "%s"' % (chat.FriendlyName, chat.Name)

