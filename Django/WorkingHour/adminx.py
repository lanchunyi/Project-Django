# -*- coding: utf-8 -*-
import xadmin

from .models import User


class UserAdmin(xadmin.AdminSite):
    def _meta(self):
        abstract = False


xadmin.site.register(UserAdmin, User)
