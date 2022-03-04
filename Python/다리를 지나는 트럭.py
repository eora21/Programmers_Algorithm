def solution(bridge_length, weight, truck_weights):
    now_weight = 0
    now_count = 0
    turn = 0
    head = 0
    rear = 0
    status = [bridge_length] * len(truck_weights)

    while rear < len(truck_weights):
        for i in range(head, rear):
            status[i] -= 1
            if status[i] <= 0:
                now_weight -= truck_weights[i]
                now_count -= 1
                head += 1

        if now_weight + truck_weights[rear] <= weight and now_count < bridge_length:
            now_weight += truck_weights[rear]
            now_count += 1
            rear += 1
            turn += 1

        else:
            skip_turn = status[head]
            for i in range(head, rear):
                status[i] -= skip_turn - 1
            turn += skip_turn

    return turn + bridge_length