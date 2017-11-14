################################################################################
#      This file is part of LibreELEC - https://libreelec.tv
#      Copyright (C) 2017-present Team LibreELEC
#
#  LibreELEC is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 2 of the License, or
#  (at your option) any later version.
#
#  LibreELEC is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with LibreELEC.  If not, see <http://www.gnu.org/licenses/>.
################################################################################

import os
import stat
import subprocess
import sys
import threading
import xbmc
import xbmcaddon
import xbmcgui

def systemctl(command):
   subprocess.call(['systemctl', command, xbmcaddon.Addon().getAddonInfo('id')])

class Monitor(xbmc.Monitor):

   def __init__(self, player):
      super(Monitor, self).__init__(self)
      self.player = player

   def onSettingsChanged(self):
      self.player.stop()

if __name__ == '__main__':
   #player = Player()
   #controller = Controller(player)
   #controller.start()
   Monitor(player).waitForAbort()
   #controller.stop()
