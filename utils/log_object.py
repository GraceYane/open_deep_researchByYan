import logging
from pprint import pformat

# 使用专门的日志名称
logger = logging.getLogger("research_flow")
logger.setLevel(logging.INFO)

# 不再交给框架重复输出
logger.propagate = False

# 避免重复添加处理器
if not logger.handlers:
    handler = logging.StreamHandler()
    handler.setFormatter(
        logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s",
            datefmt="%H:%M:%S",
        )
    )
    logger.addHandler(handler)


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