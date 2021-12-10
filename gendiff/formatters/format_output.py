from .plain import plain_result
from .stylish import stylish_result
from ..diff_builder import Node


def create_output_result(diff_data: list[Node], output_format: str) -> str:
    if output_format == 'stylish':
        return stylish_result(diff_data)
    elif output_format == 'plain':
        return plain_result(diff_data)