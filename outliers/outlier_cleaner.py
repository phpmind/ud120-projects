# !/usr/bin/python

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    errors = {}
    cleaned_data = []

    # your code goes here
    for i, pred in enumerate(predictions):
        error = predictions[i] - net_worths[i]
        error = abs(error[0])
        cleaned_data.append((ages[i][0], net_worths[i][0], error))

    sorted_data = sorted(cleaned_data, key=lambda x: x[2])


    #     errors[i] = error
    # print errors
    # sortedErrors = sorted(errors.iteritems(), key=lambda (k,v): (v,k))
    # print sortedErrors



    # for d in sorted_data[:81]:
        # print d
    # print cleaned_data
    return sorted_data[:81]

