import cv2


input = [[[199.2112, 157.8867],
         [214.17532, 139.92976],
         [181.25424, 145.9154],
         [238.11792, 142.92259],
         [169.28294, 157.8867],
         [244.10356, 232.70732],
         [148.33318, 244.67863],
         [262.06052, 343.44183],
         [145.34035, 373.3701],
         [286.0031, 364.39163],
         [259.0677, 358.40598],
         [253.08205, 427.24094],
         [190.23271, 448.1907],
         [426.66586, 484.1046],
         [306.95288, 517.0257],
         [401.22687, 596.3355],
         [371.2986, 596.3355]]]



# k = image_bgr[:, :, 0] - image[:, :, 2]
# l = image_bgr[:, :, 1] - image[:, :, 1]
# m = image_bgr[:, :, 2] - image[:, :, 0]
# print(k)
# print("----------------------------------------------------------")
# print(l)
# print("----------------------------------------------------------")
# print(m)
# print("----------------------------------------------------------")

# print(type(image_bgr))
# print(image_bgr.shape)
# print(image.shape)




SKELETON = [
    [1, 3], [1, 0], [2, 4], [2, 0], [0, 5], [0, 6], [5, 7], [7, 9], [6, 8], [8, 10], [5, 11], [6, 12], [11, 12], [11, 13], [13, 15], [12, 14], [14, 16]
]


CocoColors = [[255, 0, 0], [255, 85, 0], [255, 170, 0], [255, 255, 0], [170, 255, 0], [85, 255, 0], [0, 255, 0],
              [0, 255, 85], [0, 255, 170], [0, 255, 255], [0, 170, 255], [0, 85, 255], [0, 0, 255], [85, 0, 255],
              [170, 0, 255], [255, 0, 255], [255, 0, 170], [255, 0, 85]]

NUM_KPTS = 17

# print(len(SKELETON))
# print(SKELETON[1][0])             # 1
# print(SKELETON[1][1])             # 0
# print(SKELETON[5][1])             # 6

# for i in range(len(SKELETON)):
#     kpt_a, kpt_b = SKELETON[i][0], SKELETON[i][1]
#     print(kpt_a, kpt_b)
# image = image_bgr[:, :, [2, 1, 0]]

def draw_pose(keypoints,img):
    """draw the keypoints and the skeletons.
    :params keypoints: the shape should be equal to [17,2]
    :params img:
    """
    # assert keypoints.shape == (NUM_KPTS,2)
    for i in range(len(SKELETON)):
        kpt_a, kpt_b = SKELETON[i][0], SKELETON[i][1]
        x_a, y_a = keypoints[kpt_a][0],keypoints[kpt_a][1]
        x_b, y_b = keypoints[kpt_b][0],keypoints[kpt_b][1]
        cv2.circle(img, (int(x_a), int(y_a)), 6, CocoColors[i], -1)
        cv2.circle(img, (int(x_b), int(y_b)), 6, CocoColors[i], -1)
        cv2.line(img, (int(x_a), int(y_a)), (int(x_b), int(y_b)), CocoColors[i], 2)


image_bgr = cv2.imread('videos/123.jpg')        #BGR
# image = image_bgr[:, :, [2, 1, 0]]
"""
for kpt in input:
    draw_pose(kpt, image_bgr)

cv2.imshow('demo', image_bgr)
cv2.waitKey(0)
"""

# video = cv2.VideoCapture("output.avi")

lis = []
sum = 0


def draw_min(min_frame, video_path, min_frame_kpt):
    """
    输出不标准的那个动作

    :param min_frame:
    :param video_path:
    :param min_frame_kpt:
    :return:
    """
    sum = 0
    video = cv2.VideoCapture(video_path)
    while True:

        ret, img = video.read()
        sum += 1
        if sum == min_frame:
            if min_frame_kpt.shape == (17, 2):
                min_frame_kpt.resize(1, 17, 2)

            for kpt in min_frame_kpt:
                draw_pose(kpt, img)
            break

    return img


# img = cv2.cvtColor(img, cv2.COLOR_BayerBG2RGB)



print(len(lis))
print(sum)


# cv2.imshow('testing', img)
# cv2.waitKey(0)
# print(img[0])

