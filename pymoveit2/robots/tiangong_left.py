from typing import List

MOVE_GROUP_ARM: str = "left_arm_group"
MOVE_GROUP_GRIPPER: str = "gripper"

OPEN_GRIPPER_JOINT_POSITIONS: List[float] = [0.04, 0.04]
CLOSED_GRIPPER_JOINT_POSITIONS: List[float] = [0.0, 0.0]


def joint_names(prefix: str = "") -> List[str]:
    return [
        prefix + "shoulder_pitch_l_joint",
        prefix + "shoulder_roll_l_joint",
        prefix + "shoulder_yaw_l_joint",
        prefix + "elbow_pitch_l_joint",
        prefix + "elbow_yaw_l_joint",
        prefix + "wrist_pitch_l_joint",
        prefix + "wrist_roll_l_joint",
    ]


def base_link_name(prefix: str = "") -> str:
    return prefix + "world"


def end_effector_name(prefix: str = "") -> str:
    return prefix + "wrist_roll_l_link"


def gripper_joint_names(prefix: str = "") -> List[str]:
    return [
        prefix + "wrist_roll_l_link",
        prefix + "wrist_roll_r_link",
    ]
