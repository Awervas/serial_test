import argparse
import logging
import serial
import time

# port='COM1', baudrate=19200, bytesize=8, parity='N', stopbits=1, timeout=None
logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(levelname)s : %(message)s")
logger = logging.getLogger(__name__)


def send_data(parse_args):
    logger.info('Run loop')
    try:
        with serial.Serial(port=parse_args.port, baudrate=parse_args.baudrate, bytesize=parse_args.bytesize,
                           parity=parse_args.parity,
                           stopbits=parse_args.stopbits, timeout=parse_args.timeout) as ser:
            while True:
                result = ser.write(parse_args.text.encode("utf-8"))
                logger.info(f'Done send {result} bytes, text: {parse_args.text}')
                read_bytes = ser.read()
                logger.info(f'Done read {read_bytes}')
    finally:
        logger.info('Loop end')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run loop send data in serial port ')

    parser.add_argument('--port', type=str, help='serial port, e.x: /dev/ttyS5')
    parser.add_argument('--baudrate', type=int, help='baudrate (default 9600)', default=9600)
    parser.add_argument('--bytesize', type=int, default=8,
                        help=' default 8')
    parser.add_argument('--parity', type=str, choices=['O', 'E', 'N'], default='N', help="default N")

    parser.add_argument('--stopbits', type=int,
                        help='default 1', default=1)

    parser.add_argument('--timeout', type=int, default=5, help="default 5 second")
    parser.add_argument('--text', type=str, default="HELLO WORLD",
                        help="Write text in serial port, default HELLO WORLD")
    args = parser.parse_args()

    send_data(args)
