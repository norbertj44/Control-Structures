###
# Checking whether the test is passed
# Test is passed when the number of correctly completed
# tasks is at least 50%
#
users_tasks = int(input(print('tasks done correctly: ')))
total_tasks = 20
tasks_ok = 10
test_passed = False

if users_tasks >= total_tasks * 0.5:
    test_passed = True

if test_passed:
    print('Congratulations! You passed the test.')
else:
    print('Unfortunately, you failed the test.')