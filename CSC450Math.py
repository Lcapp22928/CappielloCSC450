import numpy as np
from scipy import stats

# Functs for mean and changes 
def calculate_mean_and_change(pre_scores, post_scores, group_name, question):
    mean_pre = np.mean(pre_scores)
    mean_post = np.mean(post_scores)
    mean_change = np.mean(post_scores - pre_scores)
    print(f"{group_name} - {question}:")
    print(f"Mean Pre-Test Score: {mean_pre}")
    print(f"Mean Post-Test Score: {mean_post}")
    print(f"Mean Change: {mean_change}\n")

# Function to perform paired t-test with NaN check
def paired_t_test(pre_scores, post_scores, group_name, question):
    # you need to check for the for NaN values or no variance bc they are causing issues
    if np.isnan(pre_scores).any() or np.isnan(post_scores).any():
        print(f"Error: NaN values found in {group_name} for {question}.\n")
        print(f"Pre-Test Scores: {pre_scores}")
        print(f"Post-Test Scores: {post_scores}\n")
        return
    elif np.std(pre_scores) == 0 and np.std(post_scores) == 0:
        print(f"No variance in {group_name} for {question}, t-test not applicable.\n")
        return
    
    # dp the paired t-test!!!!!!
    t_stat, p_value = stats.ttest_rel(pre_scores, post_scores)
    print(f"{group_name} - {question} Paired t-test:")
    print(f"t-statistic = {t_stat}, p-value = {p_value}\n")
    return p_value

#   perform independent t-test with that NaN check
def independent_t_test(control_change, experimental_change, question):
    # Check for NaN values or mis mat ched  array len
    if np.isnan(control_change).any() or np.isnan(experimental_change).any():
        print(f"Error: NaN values found in independent t-test for {question}.\n")
        return
    if len(control_change) != len(experimental_change):
        # do another same for the larger array to match the smaller array length
        smaller_length = min(len(control_change), len(experimental_change))
        if len(control_change) > smaller_length:
            control_change = np.random.choice(control_change, size=smaller_length, replace=False)
        if len(experimental_change) > smaller_length:
            experimental_change = np.random.choice(experimental_change, size=smaller_length, replace=False)
        print(f"Resampled arrays to length: {smaller_length}")

    # Perform an indepented  t-test
    t_stat, p_value = stats.ttest_ind(control_change, experimental_change)
    print(f"Independent t-test for {question}:")
    print(f"t-statistic = {t_stat}, p-value = {p_value}\n")
    return p_value

########## TIME TO GET MEANNNNNNN!!
# Beginner group - Control
pre_control_beginner_general = np.array([8, 3, 5,3])
post_control_beginner_general = np.array([8, 5, 8, 4])

pre_control_beginner_java = np.array([4, 3, 2, 3])
post_control_beginner_java = np.array([5, 4, 6, 4])

pre_control_beginner_loops = np.array([8, 3, 2, 4])
post_control_beginner_loops = np.array([8, 4, 8, 5])

# Intermediate group - Control
pre_control_intermediate_general = np.array([7, 9, 7, 7, 4])
post_control_intermediate_general = np.array([6, 9, 7, 8, 4])

pre_control_intermediate_java = np.array([7, 6, 6, 6, 4])
post_control_intermediate_java = np.array([7, 6, 7, 6, 4])

pre_control_intermediate_loops = np.array([8, 8, 10, 9, 5])
post_control_intermediate_loops = np.array([9, 9, 10, 9, 6])

# Advanced group - Control
pre_control_advanced_general = np.array([10])
post_control_advanced_general = np.array([10])

pre_control_advanced_java = np.array([10])
post_control_advanced_java = np.array([10])

pre_control_advanced_loops = np.array([10])
post_control_advanced_loops = np.array([10])

# Pre-test and Post-test scores for Experimental Group
# Beginner group - Experimental
pre_experimental_beginner_general = np.array([5, 6, 2, 4, 3])
post_experimental_beginner_general = np.array([5, 7, 3, 4, 6])

pre_experimental_beginner_java = np.array([4, 1, 2, 1, 1])
post_experimental_beginner_java = np.array([6, 3, 5, 4, 3])

pre_experimental_beginner_loops = np.array([4, 1, 2, 2, 1])
post_experimental_beginner_loops = np.array([8, 6, 7, 6, 6])

# Intermediate group - Experimental
pre_experimental_intermediate_general = np.array([8, 8])
post_experimental_intermediate_general = np.array([9, 8])

pre_experimental_intermediate_java = np.array([9, 6])
post_experimental_intermediate_java = np.array([9, 6])

pre_experimental_intermediate_loops = np.array([8, 9])
post_experimental_intermediate_loops = np.array([8, 8])

# Advanced group - Experimental
pre_experimental_advanced_general = np.array([10, 10])
post_experimental_advanced_general = np.array([10, 10])

pre_experimental_advanced_java = np.array([10, 10])
post_experimental_advanced_java = np.array([10, 10])

pre_experimental_advanced_loops = np.array([10, 10])
post_experimental_advanced_loops = np.array([10, 10])

# Calculate and print for each question and each experience level
experience_levels = ['Beginner', 'Intermediate', 'Advanced']
questions = ['General Confidence', 'Java Confidence', 'Java Loops Understanding']

# Control Group
control_pre_post = [
    (pre_control_beginner_general, post_control_beginner_general),
    (pre_control_beginner_java, post_control_beginner_java),
    (pre_control_beginner_loops, post_control_beginner_loops),
    (pre_control_intermediate_general, post_control_intermediate_general),
    (pre_control_intermediate_java, post_control_intermediate_java),
    (pre_control_intermediate_loops, post_control_intermediate_loops),
    (pre_control_advanced_general, post_control_advanced_general),
    (pre_control_advanced_java, post_control_advanced_java),
    (pre_control_advanced_loops, post_control_advanced_loops)
]

# Experimental Group
experimental_pre_post = [
    (pre_experimental_beginner_general, post_experimental_beginner_general),
    (pre_experimental_beginner_java, post_experimental_beginner_java),
    (pre_experimental_beginner_loops, post_experimental_beginner_loops),
    (pre_experimental_intermediate_general, post_experimental_intermediate_general),
    (pre_experimental_intermediate_java, post_experimental_intermediate_java),
    (pre_experimental_intermediate_loops, post_experimental_intermediate_loops),
    (pre_experimental_advanced_general, post_experimental_advanced_general),
    (pre_experimental_advanced_java, post_experimental_advanced_java),
    (pre_experimental_advanced_loops, post_experimental_advanced_loops)
]

# Calculate for Control and Experimental Group, and perform t-tests
for i, level in enumerate(experience_levels):
    print(f"Control Group - {level}")
    for j, question in enumerate(questions):
        # Control group analysis
        pre_control = control_pre_post[i * 3 + j][0]
        post_control = control_pre_post[i * 3 + j][1]
        calculate_mean_and_change(pre_control, post_control, f"Control {level}", question)
        paired_t_test(pre_control, post_control, f"Control {level}", question)

    print(f"Experimental Group - {level}")
    for j, question in enumerate(questions):
        # Experimental group analysis
        pre_experimental = experimental_pre_post[i * 3 + j][0]
        post_experimental = experimental_pre_post[i * 3 + j][1]
        calculate_mean_and_change(pre_experimental, post_experimental, f"Experimental {level}", question)
        paired_t_test(pre_experimental, post_experimental, f"Experimental {level}", question)

        # Perform independent t-test comparing control and experimental group changes
        control_change = post_control - pre_control
        experimental_change = post_experimental - pre_experimental
        independent_t_test(control_change, experimental_change, question)

print('################################################################')
