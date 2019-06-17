# -*- coding: utf-8 -*-

from aioli import Unit
from .service import VisitService, VisitorService
from .controller import HttpController


export = Unit(
    controllers=[HttpController],
    services=[VisitService, VisitorService],
    name="aioli-guestbook",
    version="0.1.0",
    description="Example guestbook Unit",
)
