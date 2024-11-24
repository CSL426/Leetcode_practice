import math


def calculate_optimal_rebate(amount: int, plan="UP", available_points=0):
    """
    計算最高實際回饋的點數抵扣與回饋百分比。

    :param amount: 消費金額（int）
    :param plan: 回饋方案，預設為 "UP"
    :param available_points: 可用點數（int），預設為 0
    :return: None (直接打印結果)
    """
    # 定義回饋百分比
    rebate_rates = [0.003, 0.007, 0.005]  # 基本回饋 0.3%, 0.7%
    if plan == "任意選":
        extra_rate = 0.025  # 任意選 2.5%
    elif plan == "UP":
        extra_rate = 0.035  # UP 3.5%
    else:
        raise ValueError("方案必須是 '任意選' 或 'UP'")

    # 初始化最佳結果
    optimal_points = 0
    max_effective_rate = 0.0
    best_rebate_points = 0

    # 遍歷所有可能的抵押點數（最多消費金額的30%或可用點數）
    max_deductible_points = min(available_points, math.floor(amount * 0.3))
    for points_to_deduct in range(max_deductible_points + 1):
        # 抵扣後的金額
        new_amount = amount - points_to_deduct
        if new_amount <= 0:
            continue

        # 計算新回饋點數
        base_rebate_points_new = sum(math.floor(
            new_amount * rate + 0.5) for rate in rebate_rates)
        extra_rebate_points_new = math.floor(new_amount * extra_rate + 0.5)
        total_points_new = base_rebate_points_new + extra_rebate_points_new

        # 略過沒有回饋的情況
        if total_points_new == 0:
            continue

        # 計算實際回饋百分比
        effective_rate = total_points_new / new_amount

        # 更新最佳方案
        if effective_rate > max_effective_rate:
            max_effective_rate = effective_rate
            optimal_points = points_to_deduct
            best_rebate_points = total_points_new

    # 打印結果
    print(f"消費金額: {amount} 元，方案: {plan}")
    print(f"最佳抵扣點數: {optimal_points}")
    print(f"回饋點數: {best_rebate_points}")
    print(f"實際回饋: {max_effective_rate * 100:.2f}%")


# 測試函數
calculate_optimal_rebate(199, available_points=300)
