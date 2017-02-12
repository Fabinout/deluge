# -*- coding: utf-8 -*-
#
# This file is part of Deluge and is licensed under GNU General Public License 3.0, or later, with
# the additional special exception to link portions of this program with the OpenSSL library.
# See LICENSE for more details.
#

from __future__ import unicode_literals

import deluge.component as component
from deluge.core.authmanager import AUTH_LEVEL_ADMIN, AuthManager

from .basetest import BaseTestCase


class AuthManagerTestCase(BaseTestCase):
    def set_up(self):
        self.auth = AuthManager()
        self.auth.start()

    def tear_down(self):
        # We must ensure that the components in component registry are removed
        return component.shutdown()

    def test_authorize(self):
        from deluge.ui import common
        self.assertEquals(
            self.auth.authorize(*common.get_localhost_auth()),
            AUTH_LEVEL_ADMIN
        )
