def solution(bridge_length, weight, truck_weights):
#     answer = 0 # 소요시간
#     on_bridge = [0 for i in range(bridge_length)] # 다리 큐
#     arrive = [] # 도착한 트럭
#     truck_weights_start = sum(truck_weights) # 초기값 저장

#     while sum(arrive) != truck_weights_start: # 다리를 모두 건널 때 까지
#         if truck_weights:
#             if sum(on_bridge) + truck_weights[0] <= weight: # 하중 오버시 진입불가 
#                 on_bridge.append(truck_weights[0])
#                 truck_weights.pop(0)
#                 p = on_bridge.pop(0)
#                 arrive.append(p) 
#                 answer += 1
#             else:
#                 if sum(on_bridge) - on_bridge[0] + truck_weights[0] <= weight: # 하중 OK시 진입과 빠져나가기 동시
#                     on_bridge.append(truck_weights[0])
#                     truck_weights.pop(0)
#                     p = on_bridge.pop(0)
#                     arrive.append(p) 
#                     answer += 1
#                 else:
#                     on_bridge.append(0)
#                     p = on_bridge.pop(0)
#                     arrive.append(p)
#                     answer += 1
#         else: # 시작지점에 모든 트럭이 빠져나갔을 때 다리가 빌 때까지 반복
#             if sum(on_bridge) !=0:
#                 on_bridge.append(0)
#                 p = on_bridge.pop(0)
#                 arrive.append(p)
#                 answer += 1
#             else:
#                 break
#     return answer 
#
# 시간초과 발생

    time = 0
    bridge = [0] * bridge_length
    sum_trucks = 0

    while truck_weights:
      sum_trucks += truck_weights[0]
      if sum_trucks <= weight:
        sum_trucks -= bridge.pop(0)
        bridge.append(truck_weights.pop(0))  
      else:
        sum_trucks -= truck_weights[0]
        sum_trucks -= bridge.pop(0)
        if sum_trucks + truck_weights[0] <= weight:
          sum_trucks += truck_weights[0]
          bridge.append(truck_weights.pop(0))    
        else:
          bridge.append(0) 
      time += 1

    return time + len(bridge)