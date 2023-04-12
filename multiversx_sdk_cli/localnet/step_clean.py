import logging
from typing import Any

from multiversx_sdk_cli import utils
from multiversx_sdk_cli.localnet.config import ConfigRoot

logger = logging.getLogger("localnet")


def clean(args: Any):
    config = ConfigRoot.from_file(args.configfile)
    utils.remove_folder(config.root())
