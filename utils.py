def data_string_to_float(number_string):
   
    if ("N/A" in number_string) or ("NaN" in number_string):
        return "N/A"
    elif number_string == ">0":
        return 0
    elif "B" in number_string:
        return float(number_string.replace("B", '')) * 1000000000
    elif "M" in number_string:
        return float(number_string.replace("M", '')) * 1000000
    elif "K" in number_string:
        return float(number_string.replace("K", '')) * 1000
    else:
        return float(number_string)


def duplicate_error_check(df):

    df.drop(['Unix', 'Price', 'stock_p_change', 'SP500', 'SP500_p_change', 'Float', '200-Day Moving Average', 'Short Ratio',
             'Operating Margin'], axis=1, inplace=True)

    for i in range(len(df)):
        # Check if there are any duplicates.
        if pd.Series(df.iloc[i] == df.iloc[i].shift()).any():
            duplicates = set([x for x in list(df.iloc[i])
                              if list(df.iloc[i]).count(x) > 1])
            # A duplicate value of zero is quite common. We want other duplicates.
            if duplicates != {0}:
                print(i, df.iloc[i], duplicates, sep="\n")


def status_calc(stock, sp500, outperformance=10):

    if outperformance < 0:
        raise ValueError("outperformance must be positive")
    return stock - sp500 >= outperformance
