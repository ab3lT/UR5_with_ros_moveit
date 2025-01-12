import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/abel/CODE/AAiT/robotics/UR5_with_ros_moveit/install/lab_3'
