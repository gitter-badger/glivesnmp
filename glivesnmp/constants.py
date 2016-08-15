##
#     Project: gLiveSNMP
# Description: Detect information on various devices via SNMP
#      Author: Fabio Castelli (Muflone) <muflone@vbsimple.net>
#   Copyright: 2016 Fabio Castelli
#     License: GPL-2+
#  This program is free software; you can redistribute it and/or modify it
#  under the terms of the GNU General Public License as published by the Free
#  Software Foundation; either version 2 of the License, or (at your option)
#  any later version.
#
#  This program is distributed in the hope that it will be useful, but WITHOUT
#  ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
#  FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
#  more details.
#  You should have received a copy of the GNU General Public License along
#  with this program; if not, write to the Free Software Foundation, Inc.,
#  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA
##

import sys
import os.path

from xdg import BaseDirectory


# Application constants
APP_NAME = 'gLiveSNMP'
APP_VERSION = '0.0.1'
APP_DESCRIPTION = 'Detect information on various devices via SNMP'
APP_ID = 'glivesnmp.muflone.com'
APP_URL = 'http://www.muflone.com/glivesnmp/'
APP_AUTHOR = 'Fabio Castelli'
APP_AUTHOR_EMAIL = 'muflone@vbsimple.net'
APP_COPYRIGHT = 'Copyright 2016 %s' % APP_AUTHOR
# Other constants
DOMAIN_NAME = 'glivesnmp'
VERBOSE_LEVEL_QUIET = 0
VERBOSE_LEVEL_NORMAL = 1
VERBOSE_LEVEL_MAX = 2
REQUESTS_MULTIPLE = 0
REQUESTS_SINGLE = 1

# Paths constants
# If there's a file data/glivesnmp.png then the shared data are searched
# in relative paths, else the standard paths are used
if os.path.isfile(os.path.join('data', 'glivesnmp.png')):
    DIR_PREFIX = '.'
    DIR_LOCALE = os.path.join(DIR_PREFIX, 'locale')
    DIR_DOCS = os.path.join(DIR_PREFIX, 'doc')
else:
    DIR_PREFIX = os.path.join(sys.prefix, 'share', 'glivesnmp')
    DIR_LOCALE = os.path.join(sys.prefix, 'share', 'locale')
    DIR_DOCS = os.path.join(sys.prefix, 'share', 'doc', 'glivesnmp')
# Set the paths for the folders
DIR_DATA = os.path.join(DIR_PREFIX, 'data')
DIR_UI = os.path.join(DIR_PREFIX, 'ui')
try:
    # In read-only environments, the settings folder cannot be created
    # (eg in a Debian pbuilder fakeroot)
    DIR_SETTINGS = BaseDirectory.save_config_path(DOMAIN_NAME)
    DIR_HOSTS = BaseDirectory.save_config_path(
        os.path.join(DOMAIN_NAME, 'hosts'))
except:
    # Get the settings path without actually creating it
    DIR_SETTINGS = os.path.join(BaseDirectory.xdg_config_home, DOMAIN_NAME)
    DIR_HOSTS = os.path.join(BaseDirectory.xdg_config_home, DOMAIN_NAME,
                             'hosts')
# Set the paths for the data files
FILE_ICON = os.path.join(DIR_DATA, 'glivesnmp.png')
FILE_CONTRIBUTORS = os.path.join(DIR_DOCS, 'contributors')
FILE_TRANSLATORS = os.path.join(DIR_DOCS, 'translators')
FILE_LICENSE = os.path.join(DIR_DOCS, 'license')
FILE_RESOURCES = os.path.join(DIR_DOCS, 'resources')
# Set the paths for configuration files
FILE_SETTINGS = os.path.join(DIR_SETTINGS, 'settings.conf')
FILE_WINDOWS_POSITION = os.path.join(DIR_SETTINGS, 'windows.conf')
FILE_SERVICES = os.path.join(DIR_SETTINGS, 'services.conf')
FILE_DEVICES = os.path.join(DIR_SETTINGS, 'devices.conf')
