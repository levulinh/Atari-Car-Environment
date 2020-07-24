# Atari-Car-Environment

## Class Environment
**Constructor** 
__init__(refresh_frame)
refresh_frame: tốc độ làm mới vật cản, mặc định 3 (tức là player có thể thực hiện 3 hành động trước khi vật cản update vị trí)

**Parameters**
- enermies_queue: mảng chứa vị trí đầu của các vật cản
- player: tuple vị trí của đầu người chơi
- ground: nền trò chơi

**Functions**
- step(action): update player với 3 hành động (qua trái, đứng yên, qua phải), nếu hành động không khả thi (ra rìa màn hình) thì player sẽ đứng yên
- gen_and_get_ground(): trả về trạng thái của trò chơi (mảng hai chiều, ô trống là 0, địch là -1, player là 1)
- reset(): reset game


## Ví dụ sử dụng
```
env = Environment()
for i in range(10):
    env.step(i % 3)
```  
