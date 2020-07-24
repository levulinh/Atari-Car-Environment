
import random
import numpy as np
from array2gif import write_gif 
import cv2


class Environment:
    def __init__(self, refresh_frame=3):
        self.size = (12, 3)
        self.refresh_frame = refresh_frame
        # enermy: (x: lane, y: vertical position)
        self.enermies_queue = [(-2, random.choice([0, 1, 2]))]
        self.ground = np.zeros(self.size)
        self.player = (9, random.choice([0, 1, 2]))
        self.time_frame = self.refresh_frame
        self.enermies_queue = [(-2, random.choice([0, 1, 2]))]

    def gen_ground(self):
        # Empty ground
        self.ground = np.zeros(self.size)
        # Add all enermies
        for enermy in self.enermies_queue:
            if enermy[0] == -1:
                self.ground[0, enermy[1]] = -1
            elif enermy[0] == 11:
                self.ground[11, enermy[1]] = -1
            elif enermy[0] >= 0:
                self.ground[enermy[0], enermy[1]] = -1
                self.ground[enermy[0]+1, enermy[1]] = -1

        # Add our player (agent)
        self.ground[self.player] = 1
        self.ground[self.player[0]+1, self.player[1]] = 1

    def gen_and_get_ground(self):
        self.gen_ground()
        return self.ground

    def step(self, action):
        self.time_frame -= 1
        if action == 0:
            # move to left lane
            if self.player[1] > 0:
                self.player = (self.player[0], self.player[1]-1)
        if action == 2:
            # move to right lane
            if self.player[1] < 2:
                self.player = (self.player[0], self.player[1]+1)

        if self.time_frame <= 0:
            # Time to refresh enermy state

            # Update new vertical position for all enermies on the ground
            for i in range(len(self.enermies_queue)):
                self.enermies_queue[i] = (
                    self.enermies_queue[i][0]+1, self.enermies_queue[i][1])

            # Add new enermy and remove enermy who is out of the board
            last_enermy = self.enermies_queue[-1]

            # if the enermy on top has vertical pos > min
            min_dist = random.choice([2, 3, 4])
            if last_enermy[0] >= min_dist:
                if random.choice([0, 1]) == 1:
                    x_s = random.sample({0, 1, 2}, 2)
                    self.enermies_queue.append((-2, x_s[0]))
                    self.enermies_queue.append((-2, x_s[1]))
                else:
                    self.enermies_queue.append((-2, random.choice([0, 1, 2])))
            # if first enermy is out of the screen
            while self.enermies_queue[0][0] >= 12:
                self.enermies_queue.pop(0)

            self.time_frame = self.refresh_frame

        # Check game ternimal
        for enermy in self.enermies_queue:
            if enermy[1] == self.player[1] and\
                    (enermy[0] >= 8 and enermy[0] <= 10):
                return [-1], True

        # Game not exits
        return [1], False

    def reset(self):
        self.enermies_queue = [(-2, random.choice([0, 1]))]
        self.time_frame = self.refresh_frame
        self.player = (9, random.choice([0, 1]))

# history là mảng môi trường tại một thời điểm, score là điểm tại lúc đó
def create_img(history, score):
    img = np.zeros((40*12, 480, 3), dtype = "uint8")
    img[:, 200:360] = 255
    font = cv2.FONT_HERSHEY_SIMPLEX 
    cv2.putText(img, 'SCORE: {}'.format(score), (10, 20), 
            font, 0.3, (0, 255, 0), 1, cv2.LINE_AA)
    for i in range(12):
        for j in range(4):
            if history[i][j] == -1:
                cv2.rectangle(img, (j*40+200, i*40), (j*40+240, i*40+40), (100, 100, 255), cv2.FILLED)
            elif history[i][j] == 1:
                cv2.rectangle(img, (j*40+200, i*40), (j*40+240, i*40+40), (255, 100, 100), cv2.FILLED)
    return img

# Hiện ảnh thì cv2.imshow(img)
                    self.enermies_queue.append((-2, x_s[0]))ảnh 
                    self.enermies_queue.append((-2, x_s[0]))
