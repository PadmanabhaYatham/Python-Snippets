def solve(heights):
    stk = [-1]
    heights.append(0)
    ans = [0]

    for i in range(len(heights)):
        while heights[i] < heights[stk[-1]]:
            h = heights[stk.pop()]
            width = i - stk[-1] - 1
            ans.append(h * width)
        stk.append(i)
    return ans


nums = list(map(int, input().split()))


print(max(solve(nums)))
