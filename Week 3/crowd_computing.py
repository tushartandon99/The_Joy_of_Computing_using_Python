from statistics import mean
from scipy import stats
estimates=[450, 470, 490, 510, 530, 480, 495, 505, 520, 460,475, 485, 500, 515, 525, 540, 455, 465, 478, 492,508, 518, 535, 550, 445, 460, 472, 488, 499, 507,519, 528, 538, 560, 430, 440, 452, 468, 479, 491,503, 512, 522, 534, 548, 565, 420, 435, 447, 459,471, 483, 496, 504, 516, 529, 542, 555, 570, 410,425, 438, 449, 461, 474, 487, 498, 506, 517, 531,545, 558, 575, 590, 600]
estimates.sort()
m= stats.trim_mean(estimates,0.1)
print (m)
# trimmed_value=int(0.1*len(estimates))
# estimates=estimates[trimmed_value:len(estimates)-trimmed_value]
# print (mean(estimates))
