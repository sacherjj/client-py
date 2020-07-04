import argparse
from dataclasses import dataclass
from enum import Enum
from typing import List, Dict


class ValidationType(Enum):
    UP_TO_ONE = 1
    ONLY_ONE = 2
    AT_LEAST_ONE = 3


@dataclass(frozen=True)
class GroupValidator:
    type: ValidationType
    fields: list

    def values_in_group(self, args: dict) -> list:
        return [value for key, value in args.items() if key in self.fields]

    def count_not_none(self, args: dict) -> int:
        return len([value for value in self.values_in_group(args) if value is not None])

    def validate(self, args: dict):
        call_map = {
            ValidationType.UP_TO_ONE: self.validate_up_to_one,
            ValidationType.AT_LEAST_ONE: self.validate_at_least_one,
            ValidationType.ONLY_ONE: self.validate_only_one,
        }
        error = call_map[self.type](args)
        if error:
            raise ValueError(error)

    def validate_up_to_one(self, args: dict):
        if self.count_not_none(args) > 1:
            return f"May only include zero or one of {self.fields}."

    def validate_at_least_one(self, args: dict):
        if self.count_not_none(args) == 0:
            return f"Must includes at least one of {self.fields}."

    def validate_only_one(self, args: dict):
        if self.count_not_none(args) != 1:
            return f"Must include one and only one of {self.fields}."


PAYMENT_VALIDATOR = GroupValidator(
    type=ValidationType.AT_LEAST_ONE,
    fields=[
        "payment",
        "payment_args",
        "payment_amount",
        "payment_hash",
        "payment_name",
        "payment_package_hash",
        "payment_package_name",
    ],
)

SESSION_VALIDATOR = (
    GroupValidator(
        type=ValidationType.AT_LEAST_ONE,
        fields=[
            "session",
            "session_args",
            "session_hash",
            "session_name",
            "session_package_hash",
            "session_package_name",
        ],
    ),
)
