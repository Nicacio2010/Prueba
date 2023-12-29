from hub import light_matrix,port
import runloop,color_sensor, color
import motor_pair

sensor_i=0
sensor_d=1

async def main():
    motor_pair.pair(motor_pair.PAIR_1, 4, 5)
    while True:
        if color_sensor.color(sensor_i) is color.WHITE and color_sensor.color(sensor_d) is color.WHITE:
            motor_pair.move(0,0)
        elif color_sensor.color(sensor_i) is color.WHITE and color_sensor.color(sensor_d) is color.BLACK:
            motor_pair.move(0,90)
        elif color_sensor.color(sensor_i) is color.BLACK and color_sensor.color(sensor_d) is color.WHITE:
            motor_pair.move(0,-90)
        elif color_sensor.color(sensor_i) is color.BLACK and color_sensor.color(sensor_d) is color.BLACK:
            motor_pair.move(0,0)              
        else:
            motor_pair.stop(0)
        

runloop.run(main())
