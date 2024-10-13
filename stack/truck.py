def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    
    time = 0
    waiting_trucks = truck_weights[:]
    bridge = [0] * bridge_length
    current_bridge_weight =0
    
    while waiting_trucks or current_bridge_weight > 0:
        time += 1
        
        truck_leaving = bridge.pop(0)
        current_bridge_weight -= truck_leaving
        
        if waiting_trucks:
            if current_bridge_weight + waiting_trucks[0] <= weight:
                truck_entering = waiting_trucks.pop(0)
                bridge.append(truck_entering)
                current_bridge_weight += truck_entering
            else:
                bridge.append(0)
        else:
            bridge.append(0)

    return time

truck_weights = 	[7,4,5,6]
weight = 10
bridge_length = 2

solution(bridge_length, weight,truck_weights)