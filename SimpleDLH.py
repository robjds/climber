from dynamixel_helper import DxlHelper

helper1 = DxlHelper("climber_preset.json")

motor_id1 = 2
motor1 = helper1.get_motor(motor_id1)
motor1.set_torque(True)

dxl_unit, res = motor1.get_present_position()
motor1.set_goal_position((dxl_unit + 2000) % 4096)

helper2 = DxlHelper("climber_preset2.json")

motor_id2 = 1
motor2 = helper2.get_motor(motor_id2)
motor2.set_torque(True)

dxl_unit, res = motor2.get_present_position()
motor2.set_goal_position((dxl_unit + 2000) % 4096)
