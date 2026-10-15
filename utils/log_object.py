import logger
import pformat


def log_object(name: str, obj: object) -> None:
    logger.info(
        "%s（类型：%s）：\n%s",
        name,
        type(obj).__name__,
        pformat(obj, width=100),
    )