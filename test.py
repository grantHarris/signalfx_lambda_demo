import time
import random

import signalfx_lambda

from mock_context import MockContext

@signalfx_lambda.emits_metrics
def test(event, context):

    for i in range(event):
        sleep = random.random()
        print('Sleep for:', sleep)

        signalfx_lambda.send_counter('TestExecutions', 1, {'qwerty': 'high' if sleep > 0.5 else 'low'})
        signalfx_lambda.send_gauge('TestSleepTime', sleep)

        time.sleep(sleep)



test(1000, MockContext('LuluSignalFxDemo', '1'))

