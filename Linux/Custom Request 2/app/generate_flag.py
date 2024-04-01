#!/usr/bin/python3

#|###############################|#
#| Chronos Security | Marin Radu |#
#| https://chronossec.site       |#
#| https://github.com/ChronosPK  |#
#|###############################|#

import hashlib, datetime, pytz

def generate_flag(salt):
	desired_timezone = pytz.timezone('Europe/Bucharest')
	current_time = datetime.datetime.now(desired_timezone).time()
	num_blocks_passed = (current_time.hour * 3600 + current_time.minute * 60 + current_time.second) // 300  # renew every 300 seconds

	flag = f"CSCTF{{}}{num_blocks_passed}{salt}"
	hashed_flag = hashlib.sha256(flag.encode()).hexdigest()
	flag = f"CSCTF{{{hashed_flag}}}"

	return flag
