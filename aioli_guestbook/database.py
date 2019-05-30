# -*- coding: utf-8 -*-

import datetime
import orm

from aioli.db import Model


class VisitorModel(Model):
    __tablename__ = 'visitor'

    id = orm.Integer(primary_key=True)
    name = orm.String(index=True, max_length=64)
    ip_addr = orm.String(index=True, max_length=15)
    location = orm.String(allow_null=True, max_length=64)


class VisitModel(Model):
    __tablename__ = 'visit'

    id = orm.Integer(primary_key=True)
    visited_on = orm.DateTime(default=datetime.datetime.utcnow)
    message = orm.String(max_length=64)
    visitor = orm.ForeignKey(VisitorModel)
