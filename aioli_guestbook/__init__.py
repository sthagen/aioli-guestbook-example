from aioli import Package

from .service import VisitService, VisitorService
from .controller import HttpController
from .config import ConfigSchema


export = Package(
    controllers=[HttpController],
    services=[VisitService, VisitorService],
    config=ConfigSchema,
    name="aioli_guestbook",
    version="0.1.0",
    description="Example guestbook Package",
)
