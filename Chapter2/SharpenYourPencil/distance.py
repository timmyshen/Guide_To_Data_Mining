__author__ = 'Benqing'

users = {
    "Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0,
                 "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
    "Bill": {"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5,
             "Vampire Weekend": 3.0},
    "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5,
             "Slightly Stoopid": 1.0},
    "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5,
            "The Strokes": 4.0, "Vampire Weekend": 2.0},
    "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
    "Jordyn": {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5,
               "The Strokes": 4.0, "Vampire Weekend": 4.0},
    "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0,
            "The Strokes": 5.0},
    "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
}

# Compute the Euclidean Distance between Hailey and Veronica
import math


def minkowski_dist(user_ratings1, user_ratings2, r):
    """Minkowski Distance between two users"""
    if not (isinstance(user_ratings1, dict) and isinstance(user_ratings2, dict)):
        exit()
    item_score_diff_r_sum = 0.0
    for item_name in user_ratings1:
        if item_name in user_ratings2:
            # there is a matched item
            item_score_diff_r_sum += abs(user_ratings1[item_name] - user_ratings2[item_name]) ** r
    return math.pow(item_score_diff_r_sum, 1.0/r)


def euclidean_dist(user_ratings1, user_ratings2):
    """Euclidean Distance between two users"""
    if not (isinstance(user_ratings1, dict) and isinstance(user_ratings2, dict)):
        exit()
    item_score_diff_sqr_sum = 0.0
    for item_name in user_ratings1:
        if item_name in user_ratings2:
            # there is a matched item
            item_score_diff_sqr_sum += (user_ratings1[item_name] - user_ratings2[item_name]) ** 2
    return math.sqrt(item_score_diff_sqr_sum)


def manhattan_dist(user_ratings1, user_ratings2):
    """Manhattan Distance between two users"""
    if not (isinstance(user_ratings1, dict) and isinstance(user_ratings2, dict)):
        exit()
    item_score_diff_abs_sum = 0.0
    for item_name in user_ratings1:
        if item_name in user_ratings2:
            # there is a matched item
            item_score_diff_abs_sum += abs(user_ratings1[item_name] - user_ratings2[item_name])
    return item_score_diff_abs_sum


def compute_nearest_neighbor(username, users_in):
    """creates a sorted list of users based on their distance to username"""
    distances = []
    for user in users_in:
        if user != username:
            distance = minkowski_dist(users_in[user], users_in[username], 2)
            distances.append((distance, user))
    # sort based on distance -- closest first
    distances.sort()
    return distances


if __name__ == '__main__':
    print 'tesing...'
    # my_dict1 = {'a': 1, 'b': 2}
    # print my_dict1
    # for k in my_dict1:
    #     print k
    # print type(my_dict1)
    # print type(my_dict1) == dict
    print euclidean_dist(users['Hailey'], users['Veronica'])
    print euclidean_dist(users['Hailey'], users['Jordyn'])
    print manhattan_dist(users['Hailey'], users['Veronica'])
    print manhattan_dist(users['Hailey'], users['Jordyn'])
    print minkowski_dist(users['Hailey'], users['Veronica'], 4)
    print compute_nearest_neighbor('Hailey', users)