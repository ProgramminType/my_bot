import os
from launch import LaunchDescription
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        ExecuteProcess(
            cmd=['ros2', 'launch', 'sllidar_ros2', 'view_sllidar_c1_launch.py'],
            output='screen'
        )
    ])

