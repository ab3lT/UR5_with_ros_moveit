import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/abel/CODE/AAiT/robotics/UR5_with_ros_moveit/src/lab_3/install/lab_3'
