# -*- coding: utf-8 -*-

from aioli.config import PackageConfigSchema, fields


class ConfigSchema(PackageConfigSchema):
    visits_max = fields.Integer(required=True)
