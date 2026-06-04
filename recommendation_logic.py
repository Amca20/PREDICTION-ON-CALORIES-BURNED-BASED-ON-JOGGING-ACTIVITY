def generate_recommendation(weight, height, time, distance, goal_weight_loss, goal_weeks, calories_per_hour):
    """
    Generate personalized recommendations based on user input and predicted calorie expenditure.
    """
    # Constants
    CALORIES_PER_KG_FAT = 7700  # 1 kg of fat = 7700 kcal

    # Calculate total calories needed to lose the goal weight
    total_calories_to_lose = goal_weight_loss * CALORIES_PER_KG_FAT

    # Calculate daily calories to burn to achieve the goal
    daily_calories_to_burn = total_calories_to_lose / (goal_weeks * 7)

    # Calculate time and distance needed per day to achieve the goal
    time_needed_per_day = daily_calories_to_burn / calories_per_hour
    distance_needed_per_day = (time_needed_per_day * distance) / time

    # Weights for balancing time and distance (sum of weights should be 1)
    weight_time = 0.5
    weight_distance = 0.5

    # Adjust time and distance using weights
    adjusted_time_needed_per_day = time_needed_per_day * weight_time + time * (1 - weight_time)
    adjusted_distance_needed_per_day = distance_needed_per_day * weight_distance + distance * (1 - weight_distance)

    # Create a personalized recommendation
    if daily_calories_to_burn <= (calories_per_hour * time):
        recommendation = (
            "Great job! Your capable to achieve your goal of losing\n"
            f"{goal_weight_loss} kg in {goal_weeks} weeks,\n"
            "=============================================\n"
            "Here are some tips to keep you motivated:\n"
            "- Stay hydrated and maintain a balanced diet.\n"
            "- Track your progress and celebrate small milestones.\n"
            "- Mix up your jogging routine to keep it interesting.\n"
            "Keep up the great work!"
        )
    else:
        recommendation = (
            f"To achieve your goal of losing {goal_weight_loss} kg in {goal_weeks} weeks,\n"
            f"you will need to increase your jogging time to {adjusted_time_needed_per_day:.2f} hours per day\n"
            f"and distance to {adjusted_distance_needed_per_day:.2f} km per day.\n"
            "=============================================\n"
            "You can do it! Keep pushing towards your goal! Consider these tips:\n"
            "- Break your workout into multiple shorter sessions throughout the day.\n"
            "- Increase your intensity gradually to avoid injury.\n"
            "- Stay consistent and make sure to rest appropriately.\n"
            "Believe in yourself and stay focused on your goal!"
        )

    return recommendation, adjusted_time_needed_per_day, adjusted_distance_needed_per_day
