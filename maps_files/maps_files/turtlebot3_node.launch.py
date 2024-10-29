import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from turtlesim.msg import Pose
# from tf.transformations import euler_from_quaternion

# Global variables
desired_x = -1.5  # Desired x-coordinate
desired_y = -0.498765  # Desired y-coordinate
threshold = 3.3  # Distance threshold for considering the position reached
position_reached = False

# x = -2



class project_node(Node):


    def odom_callback(self, odom_msg):
        global position_reached
        
        # Extract the current position from the Odometry message
        x = odom_msg.pose.pose.position.x
        y = odom_msg.pose.pose.position.y

        # Calculate the distance between the current position to the desired position
        distance = ((desired_x - x) * 2 + (desired_y - y) * 2) ** 0.5

        self.get_logger().info(f'x:{x:.2f}')
        # Check if the position has been reached
        if abs(x - desired_x) < threshold:
            # rospy.loginfo("Position reached!")
            # self.get_logger().info('goal reached!!!!!!!!!!!!!!')
            position_reached = True


    def _init_(self):
        super()._init_('go_to_goal')


        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer_ = self.create_timer(0.1, self.call_subscriber)
        # self.create_timer(0.5, self.send_cmd_vel_callback)


    def call_subscriber(self):
        self.create_subscription(Odometry, '/odom', self.publish_goal, 10)

    def publish_goal(self, odom: Odometry):
        global position_reached
        global desired_x
        # Create a Twist message to control the robot's velocity
        cmd_vel_msg = Twist()
        cmd_vel_msg.linear.x = 0.09  # Desired linear velocity
        cmd_vel_msg.angular.z = 0.0  # Desired angular velocity

        x = odom.pose.pose.position.x
        # y = odom.pose.pose.position.y
        
        self.get_logger().info(f'x:{x:.2f}')
        self.get_logger().info('still going')
        # self.get_logger().info('still going')
        # Subscribe to the Odometry topic to get the current position
        
        # rospy.Subscriber('/odom', Odometry, odom_callback)
        # self.create_subscription(Odometry, '/odom', self.odom_callback, 10)

        # Check if the position has been reached
        if x >= desired_x:
            # rospy.loginfo("Position reached!")
            self.get_logger().info('goal reached!!!!!!!!!!!!!!')

            # Stop the robot
            cmd_vel_msg.linear.x = 0.0
            position_reached = True
            self.publisher_.publish(cmd_vel_msg)
        

        # Run the loop until the node is shut down or the position is reached
        while not position_reached:
            self.publisher_.publish(cmd_vel_msg)
        # rate.sleep()
        
        # continue 
        self.publisher_.publish(cmd_vel_msg)

 
def main(args=None):
    rclpy.init(args=args)

    node1 = project_node()
    rclpy.spin(node1)
    # node1.destroy_node()
    rclpy.shutdown()

if  __name__  == '_main_':
    main()