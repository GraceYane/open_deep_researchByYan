import logging
from pprint import pformat

logger = logging.getLogger(__name__)


def log_object(name: str, obj: object = None) -> None:
    if obj is None:
        logger.info("%s", name)
        return

    logger.info(
        "%s（类型：%s）：\n%s",
        name,
        type(obj).__name__,
        pformat(obj, width=100),
    )