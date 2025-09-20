from typing import List

MOVE_GROUP_ARM: str = "robot600_group"
MOVE_GROUP_GRIPPER: str = "gripper"

OPEN_GRIPPER_JOINT_POSITIONS: List[float] = [0.04, 0.04]
CLOSED_GRIPPER_JOINT_POSITIONS: List[float] = [0.0, 0.0]


def joint_names(prefix: str = "") -> List[str]:
    return [
        prefix + "joint1",
        prefix + "joint2",
        prefix + "joint3",
        prefix + "joint4",
        prefix + "joint5",
        prefix + "joint6",
    ]


def base_link_name(prefix: str = "") -> str:
    return prefix + "world"


def end_effector_name(prefix: str = "") -> str:
    return prefix + "joint6"


def gripper_joint_names(prefix: str = "") -> List[str]:
    return [
        prefix + "",
        prefix + "",
    ]
