# -*- coding: utf-8 -*-

from aioli import Package
from .service import VisitService, VisitorService
from .controller import HttpController


package = Package(
    controllers=[HttpController],
    services=[VisitService, VisitorService],
    name="aioli-guestbook",
    version="0.1.0",
    description="Example guestbook package",
)
