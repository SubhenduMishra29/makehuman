# Script to create a humanoid character
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
**Project Name:**      MakeHuman

**Product Home Page:** http://www.makehumancommunity.org/

**Github Code Home Page:**    https://github.com/makehumancommunity/

**Authors:**           Joel Palmius, Marc Flerackers, Jonas Hauquier

**Copyright(c):**      MakeHuman Team 2001-2020

**Licensing:**         AGPL3

    This file is part of MakeHuman Community (www.makehumancommunity.org).

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.


Abstract
--------

TODO
"""

import numpy as np
import algos3d
import guicommon
from core import G
from progress import Progress
import events3d
from getpath import getSysDataPath, canonicalPath
import log
import material
import animation
import sys
from uuid import uuid4
from mesh_operations import calculateSurface, calculateVolume

from makehuman import getBasemeshVersion, getShortVersion, getVersionStr, getVersion

class cartoon(guicommon.Object, animation.AnimatedMesh):
    
