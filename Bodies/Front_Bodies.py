import matplotlib.pyplot as plt

gf1 = [30, -30]
gf2 = [50, 50]
plt.plot(gf1, gf2)

rf1 = [0]
for i in range(0, 1):
    rfvm = int(input("Enter the reference length in inches: "))

    rfv = rfvm + 2
    rf1.append(rfv)
rf2 = [-1, -1]
print(rf1, rf2)

plt.plot(rf2, rf1)

y1 = []
for i in range(0, 1):
    yvm = int(input("Enter the width of yoke in inches: "))

    ylv = yvm / 2
    ylv = rf2[1] - ylv
    y1.append(ylv)
    y1.append(rf2[1])
y2 = [rf1[1], rf1[1]]
print(y1, y2)
plt.plot(y1, y2)

chvm = int(input("Enter the width of chest in inches: "))
ahvl = (chvm / 4) - 1
print(ahvl)
rfv = rfv - ahvl

ahvl1 = [y1[0], y1[0]]
ahvl2 = [y2[0], rfv]

print(ahvl1, ahvl2)
plt.plot(ahvl1, ahvl2)

clv = (chvm / 4) + 2
print(clv)
clv = rf2[0] - clv
print(clv)
cl1 = [rf2[0], clv]
cl2 = [rfv, rfv]

print(cl1, cl2)
plt.plot(cl1, cl2)

chb1 = [cl1[1], cl1[1]]
chb2 = [rf1[0], cl2[1]]
print(chb1, chb2)
plt.plot(chb1, chb2)

ncvm = int(input("Enter the width of neck in inches: "))
nc = ncvm / 6
print(nc)
nc = rf2[1] - nc
nw1 = [nc, rf2[1]]
nw2 = [rf1[1], rf1[1]]
print(nw1, nw2)

plt.plot(nw1, nw2)

nc = ncvm / 6
nc = nc + 1.5
print(nc)
nc = rf1[1] - nc
nd1 = [rf2[1], rf2[1]]
nd2 = [nc, rf1[1]]
print(nd1, nd2)

plt.plot(nd1, nd2)

yoe = chvm / 24
print(yoe)
yoe = rf1[1] - yoe
yoe1 = [ahvl1[0], ahvl1[0]]
yoe2 = [rf1[1], yoe]
print(yoe1, yoe2)

plt.plot(yoe1, yoe2)

lsp1 = [yoe1[1], nw1[0]]
lsp2 = [yoe2[1], yoe2[0]]

lsp1[0] = lsp1[0] - 0.2
lsp2[0] = lsp2[0] - 0.2
print(lsp1, lsp2)

plt.plot(lsp1, lsp2)

#for normalizing below lsp values:
lsp1[0] = lsp1[0] + 0.2
lsp2[0] = lsp2[0] + 0.2

ndp1 = [lsp1[1], nd1[0]]
ndp2 = [lsp2[1], nd2[0]]
print(ndp1, ndp2)

plt.plot(ndp1, ndp2)

absv = lsp2[0] - cl2[0]
absv = absv / 2
print(absv)
absv1 = lsp2[0] - absv
print(absv1)
absv2 = y1[0] + 0.5
abs1 = [absv2, lsp1[0]]
abs2 = [absv1, absv1]
print(abs1, abs2)

plt.plot(abs1, abs2)

sawv = nd1[0] + 1
saw1 = [nd1[0], sawv]
saw2 = [nd2[0], nd2[0]]
print(saw1, saw2)

plt.plot(saw1, saw2)

sal1 = [saw1[1], saw1[1]]
sal2 = [saw2[1], saw1[1]]
print(sal1, sal2)

plt.plot(sal1, sal2)

bplv = sal1[0] + 2
bpw1 = [sal1[0], bplv]
bpw2 = [sal2[0], sal2[0]]
print(bpw1, bpw2)

plt.plot(bpw1, bpw2)

bpl1 = [bpw1[1], bpw1[1]]
bpl2 = [bpw2[1], bpw1[0]]
print(bpl1, bpl2)

plt.plot(bpl1, bpl2)

bl1 = [bpl1[1], chb1[0]]
bl2 = [bpl2[1], chb2[0]]
print(bl1, bl2)

plt.plot(bl1, bl2)
#----------------------Mirror------------------------------
# print('------mirror------')
# rfv = rfvm
# rf11 = [0]
# for i in range(0, 1):

#     rfv = rfv + 2
#     rf11.append(rfv)
# rf21 = [0, 0]
# print(rf11, rf21)

# plt.plot(rf21, rf11)

# yv = yvm
# y11 = []
# for i in range(0, 1):

#     ylv = yv / 2
#     ylv = rf21[1] - ylv
#     y11.append(ylv)
#     y11.append(rf21[1])
# y21 = [rf11[1], rf11[1]]

# y11 = [ -x for x in y11]

# print(y11, y21)
# plt.plot(y11, y21)

# chv = chvm
# ahvl = (chv / 4) - 1
# print(ahvl)
# rfv = rfv - ahvl
# ahvl11 = [y11[0], y11[0]]
# ahvl21 = [y21[0], rfv]

# print(ahvl11, ahvl21)
# plt.plot(ahvl11, ahvl21)

# clv = (chv / 4) + 2
# print(clv)
# clv = rf21[0] - clv
# print(clv)
# cl11 = [rf21[0], clv]
# cl21 = [rfv, rfv]

# cl11 = [ -x for x in cl11]

# print(cl11, cl21)
# plt.plot(cl11, cl21)

# chb11 = [cl11[1], cl11[1]]
# chb21 = [rf11[0], cl21[1]]
# print(chb11, chb21)
# plt.plot(chb11, chb21)

# ncv = ncvm
# nc = ncv / 6
# print(nc)
# nc = rf21[1] - nc
# nw11 = [nc, rf21[1]]
# nw21 = [rf11[1], rf11[1]]
# print(nw11, nw21)

# nw11 = [ -x for x in nw11]

# plt.plot(nw11, nw21)

# nc = ncv / 6
# nc = nc + 1.5
# print(nc)
# nc = rf11[1] - nc
# nd11 = [rf21[1], rf21[1]]
# nd21 = [nc, rf11[1]]
# print(nd11, nd21)

# plt.plot(nd11, nd21)

# yoe = chv / 24
# print(yoe)
# yoe = rf11[1] - yoe
# yoe11 = [ahvl11[0], ahvl11[0]]
# yoe21 = [rf11[1], yoe]
# print(yoe11, yoe21)

# plt.plot(yoe11, yoe21)

# lsp11 = [yoe11[1], nw11[0]]
# lsp21 = [yoe21[1], yoe21[0]]
# print(lsp11, lsp21)

# plt.plot(lsp11, lsp21)

# ndp11 = [lsp11[1], nd11[0]]
# ndp21 = [lsp21[1], nd21[0]]
# print(ndp11, ndp21)

# plt.plot(ndp11, ndp21)

# absv2 = y11[0] - 0.2
# abs11 = [absv2, lsp11[0]]
# abs21 = [absv1, absv1]
# print(abs11, abs21)

# plt.plot(abs11, abs21)

plt.show()