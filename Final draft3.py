import sensor, time, image, pyb
from pyb import Pin
# from machine import Pin
# from machine import UART
# from machine import LED
# from machine import Timer

# blue_led = LED("LED_BLUE")

# 初始化摄像头设置
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
sensor.set_auto_gain(False)
sensor.set_auto_whitebal(False)
sensor.set_auto_exposure(False)
sensor.skip_frames(10)
clock = time.clock()

# 定义串口
#uart = UART(3, 115200)

# 定义一个输出引脚
p_out = pyb.Pin('P0', pyb.Pin.OUT_PP)
# p_in = Pin("P0", Pin.IN, Pin.PULL_UP)
# value = p_in.value()

# 颜色阈值
black_threshold = [(0, 9, 11, -14, -4, 17)] # 黑色
white_threshold = [(100, 79, 8, -8, -8, 18)] # 白色

while True:
    clock.tick()
    img = sensor.snapshot()
    p_out.high()
    # Flag = 1

    # 寻找黑色色块
    black_blobs = img.find_blobs(black_threshold, x_stride=10, y_stride=10, pixels_threshold=8500, area_threshold=8500)
    # 寻找白色色块
    white_blobs = img.find_blobs(white_threshold, x_stride=10, y_stride=10, area_threshold=3800, pixels_threshold=3800)

    # 检测黑色色块
    for black_blob in black_blobs:
        print("检测到黑色色块", black_blob.pixels())
        img.draw_rectangle(black_blob.rect(), color=(255, 0, 0)) #画框
        # img.draw_cross(black_blob.cx(), black_blob.cy())
        time.sleep_ms(10)
        # Flag = 1
        # uart.write('0')  # 发送黑色色块
        p_out.low()
        # p_out.low()

    # if Flag == 1:
    # 检测白色色块
    #    for white_blob in white_blobs:
    #        print("检测到白色色块", white_blob.pixels())
    #        img.draw_rectangle(white_blob.rect(), color=(0, 0, 255))
    #        time.sleep_ms(500)
            # Flag = 0
            # uart.write('1')  # 发送白色色块
            # p_out.low()
    #        p_out.high()
            # time.sleep_ms(1000)
            # p_out.low()



    print(clock.fps())
