#!/usr/bin/python3
# run with python3
import curses
import sys
from gpiozero import LED


if __name__ == '__main__':
	if len(sys.argv) != 5:
		print('test.py <up_pin_num> <down_pin_num> <left_pin_num> <right_pin_num>')
		sys.exit(1)
	up_pin_num = sys.argv[1]
	down_pin_num = sys.argv[2]
	left_pin_num = sys.argv[3]
	right_pin_num = sys.argv[4]

	up = LED(up_pin_num)
	down = LED(down_pin_num)
	left = LED(left_pin_num)
	right = LED(right_pin_num)

	screen = curses.initscr()
	curses.noecho()
	curses.cbreak()
	screen.keypad(True)

	prev = None
	try:
		while True:
			char = screen.getch()
			if char == ord('q'):
				break
			elif char == curses.KEY_RIGHT and prev != right:
				prev.off()
				right.on()
				prev = right
				print('right\r')
			elif char == curses.KEY_LEFT and prev != left:
				prev.off()
				left.on()
				prev = left
				print('left\r')
			elif char == curses.KEY_UP and prev != up:
				prev.off()
				up.on()
				prev = up
				print('up\r')
			elif char == curses.KEY_DOWN and prev != down:
				prev.off()
				down.on()
				prev = down
				print('down\r')
	finally:
		curses.nocbreak()
		screen.keypad(0)
		curses.echo()
		curses.endwin()