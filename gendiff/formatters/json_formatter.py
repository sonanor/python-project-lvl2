import dataclasses
import json
from json import JSONEncoder
from typing import Any

from gendiff.diff_builder import Node, ChangeStatus


class NodeJsonEncoder(JSONEncoder):
    def default(self, obj: Any) -> Any:
        if isinstance(obj, ChangeStatus):
            return obj.value
        if dataclasses.is_dataclass(obj):
            return dataclasses.asdict(obj)


def json_result(diff_nodes: list[Node]):
    return json.dumps(diff_nodes, cls=NodeJsonEncoder)
