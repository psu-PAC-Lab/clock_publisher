import rclpy
from rclpy.node import Node

import rosgraph_msgs.msg

class ClockPublisher(Node):
    def __init__(self):
        super().__init__('clock_publisher')

        # Publisher for clock messages
        self.clock_pub = self.create_publisher(rosgraph_msgs.msg.Clock, '/clock', 10)

        # Timer to publish clock messages at a fixed rate
        self.timer = self.create_timer(0.001, self.publish_clock)

        self.get_logger().info('ClockPublisher node has been started.')

    def publish_clock(self):
        clock_msg = rosgraph_msgs.msg.Clock()
        clock_msg.clock = self.get_clock().now().to_msg()
        self.clock_pub.publish(clock_msg)
        self.get_logger().debug(f'Published clock: {clock_msg.clock}')

def main(args=None):
    rclpy.init(args=args)
    clock_publisher = ClockPublisher()
    rclpy.spin(clock_publisher)
    clock_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()