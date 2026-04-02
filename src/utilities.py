def filter_outliers(feedbacks):
    if not feedbacks:
        return feedbacks

    mean = sum(feedbacks) / len(feedbacks)

    filtered = []
    for x in feedbacks:
        if abs(x - mean) <= 1.5:
            filtered.append(x)
        elif abs(x-mean) <= 2.5:
            filtered.append(x*0.5)
        else:
            pass

    return filtered if filtered else feedbacks
