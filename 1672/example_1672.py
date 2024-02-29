def maximumWealth(accounts):
    """
    :type accounts: List[List[int]]
    :rtype: int
    """
    maxWealthyAccount = 0

    for allAccountsByClient in accounts:
        summarization = sum(allAccountsByClient)
        maxWealthyAccount = summarization if maxWealthyAccount < summarization else maxWealthyAccount

    return maxWealthyAccount

def maximumWealth_2(accounts):
    """
    :type accounts: List[List[int]]
    :rtype: int
    """
    moneySummarizedByClient = []

    for clientIndex in range(0, len(accounts)):
        allMoneyByCurrentClient = sum(accounts[clientIndex])
        moneySummarizedByClient.append(allMoneyByCurrentClient)
    return max(moneySummarizedByClient)
