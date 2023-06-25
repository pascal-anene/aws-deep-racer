def reward_function(params):
    #######################################################################
    '''Example of using steps and progress
    '''

    # Read input variable
    steps = params['steps']
    progress = params['progress']

    # Total num of steps we want the car to finish the lap, it will vary depending on the track length
    TOTAL_NUM_STEPS = 300

    # Initialize the reward with a typical value
    reward = 1.0

    # Give additional reward if the car passes every 100 steps faster than expected
    if (steps % 100) == 0 and progress > (steps / TOTAL_NUM_STEPS) * 100 :
        reward = reward + 10.0

    return float(reward)
