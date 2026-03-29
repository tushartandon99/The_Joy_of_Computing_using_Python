import matplotlib.pyplot as plt
import statistics
estimates=[450, 470, 490, 510, 530, 480, 495, 505, 520, 460,475, 485, 500, 515, 525, 540, 455, 465, 478, 492,508, 518, 535, 550, 445, 460, 472, 488, 499, 507,519, 528, 538, 560, 430, 440, 452, 468, 479, 491,503, 512, 522, 534, 548, 565, 420, 435, 447, 459,471, 483, 496, 504, 516, 529, 542, 555, 570, 410,425, 438, 449, 461, 474, 487, 498, 506, 517, 531,545, 558, 575, 590, 600]
estimates.sort()
y=[]

tv=int(0.1*(len(estimates)))
estimates=estimates[tv:]
estimates=estimates[:len(estimates)-tv]
for i in range (len(estimates)):
    y.append(5)
plt.plot(estimates,y,'r--')
plt.plot([statistics.mean(estimates)],[5],'ro')
plt.plot([statistics.median(estimates)],[5],'bs')
plt.plot([500],[5],'g^')
plt.show()