import asyncio
import logging
import random

from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class YourMod(loader.Module):
    """Put the baka"""
    strings = {"cfg_doc": "",
                "name": "roll",
               "after_sleep": "Now you can make baka"}

    @loader.unrestricted  # Security setting to change who can use the command (defaults to owner | sudo)
    async def rollcmd(self, message):
        """Roll random number. Syntax: .roll [min number] [max number]"""
        logger.debug("rolled number")
        x = message.text.split(" ")
        await utils.answer(message, random.randrange(x[1],x[2]))
