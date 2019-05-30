# -*- coding: utf-8 -*-

from geolite2 import geolite2

from aioli.package.service import BaseService

from .. import database


class VisitorService(BaseService):
    __model__ = database.VisitorModel

    def __init__(self):
        self.geoip = geolite2.reader()

    async def get_many(self, **kwargs):
        return await self.db.get_many(**kwargs)

    async def get_one(self, visitor_id):
        return await self.db.get_one(id=visitor_id)

    async def ipaddr_location(self, value):
        def in_english(*locations):
            for loc in locations:
                yield loc['names']['en']

        geoip = await self.loop.run_in_executor(None, self.geoip.get, value)

        if value in ['127.0.0.1', '::1']:
            return 'Localhost', 'Localdomain'
        if not geoip:
            return 'Unknown City', 'Unknown Country'

        return in_english(geoip['city'], geoip['country'])
