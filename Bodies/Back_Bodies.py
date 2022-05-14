import matplotlib.pyplot as plt
import Front_Bodies

gf1 = [30, -30]
gf2 = [50, 50]
plt.plot(gf1, gf2)

rf1 = [0]
for i in range(0, 1):
    rfv = Front_Bodies.rfvm

    rfv = rfv + 2
    rf1.append(rfv)
rf2 = [0, 0]
print(rf1, rf2)

plt.plot(rf2, rf1)

y1 = []
for i in range(0, 1):
    yv = Front_Bodies.yvm

    ylv = yv / 2
    ylv = rf2[1] - ylv
    y1.append(ylv)
    y1.append(rf2[1])
y2 = [rf1[1], rf1[1]]
print(y1, y2)

plt.plot(y1, y2)

y1av = y1[0] - 0.2
esw1 = [y1[0], y1av]
esw2 = [y2[0], y2[0]]
print(esw1, esw2)

plt.plot(esw1, esw2)

chv = Front_Bodies.chvm
ahvl = (chv / 4) - 1
print(ahvl)
rfv = rfv - ahvl

ahvl1 = [y1[0], y1[0]]
ahvl2 = [y2[0], rfv]

print(ahvl1, ahvl2)
plt.plot(ahvl1, ahvl2)

clv = (chv / 4) + 2
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

ncv = Front_Bodies.ncvm
bnwv = ncv / 6
bnwv = rf1[0] + bnwv
print(bnwv)

bnw1 = [rf1[0], bnwv]
bnw2 = [rf1[1], rf1[1]]
print(bnw1, bnw2)

plt.plot(bnw1, bnw2)

byhv = chv / 24
byhv = bnw2[1] + byhv
print(byhv)
byh1 = [bnw1[1], bnw1[1]]
byh2 = [bnw2[1], byhv]
print(byh1, byh2)

plt.plot(byh1, byh2)

bnc1 = [byh1[1], bnw1[0]]
bnc2 = [byh2[1], bnw2[1]]
print(bnc1, bnc2)

plt.plot(bnc1, bnc2)

print([int(ahvl1) for ahvl1 in ahvl1])
ahvlv = [ -x for x in ahvl1]

bsl1 = [bnc1[0], ahvlv[0]]
bsl2 = [bnc2[0], ahvl2[0]]
print(bsl1, bsl2)

plt.plot(bsl1, bsl2)
# nc = ncv / 6
# print(nc)
# nc = rf2[1] - nc
# nw1 = [nc, rf2[1]]
# nw2 = [rf1[1], rf1[1]]
# print(nw1, nw2)

# plt.plot(nw1, nw2)

# nc = ncv / 6
# nc = nc + 1.5
# print(nc)
# nc = rf1[1] - nc
# nd1 = [rf2[1], rf2[1]]
# nd2 = [nc, rf1[1]]
# print(nd1, nd2)

# plt.plot(nd1, nd2)

# yoe = chv / 24
# print(yoe)
# yoe = rf1[1] - yoe
# yoe1 = [ahvl1[0], ahvl1[0]]
# yoe2 = [rf1[1], yoe]
# print(yoe1, yoe2)

# plt.plot(yoe1, yoe2)

# lsp1 = [yoe1[1], nw1[0]]
# lsp2 = [yoe2[1], yoe2[0]]
# print(lsp1, lsp2)

# plt.plot(lsp1, lsp2)

# ndp1 = [lsp1[1], nd1[0]]
# ndp2 = [lsp2[1], nd2[0]]
# print(ndp1, ndp2)

# plt.plot(ndp1, ndp2)

# absv = lsp2[0] - cl2[0]
# absv = absv / 2
# print(absv)
# absv1 = lsp2[0] - absv
# print(absv1)
# absv2 = y1[0] + 0.2
# abs1 = [absv2, lsp1[0]]
# abs2 = [absv1, absv1]
# print(abs1, abs2)

# plt.plot(abs1, abs2)

#----------------------Mirror------------------------------
print('------mirror------')

y11 = []
for i in range(0, 1):

    ylv = yv / 2
    ylv = rf2[1] - ylv
    y11.append(ylv)
    y11.append(rf2[1])
y21 = [rf1[1], rf1[1]]

y11 = [ -x for x in y11]

print(y11, y21)

plt.plot(y11, y21)

y11av = y11[0] + 0.2
esw11 = [y11[0], y11av]
esw21 = [y21[0], y21[0]]
print(esw11, esw21)

plt.plot(esw11, esw21)

ahvl11 = [y11[0], y11[0]]
ahvl21 = [y21[0], rfv]

print(ahvl11, ahvl21)
plt.plot(ahvl11, ahvl21)

clv = (chv / 4) + 2
print(clv)
clv = rf2[0] - clv
print(clv)
cl11 = [rf2[0], clv]
cl21 = [rfv, rfv]

cl11 = [ -x for x in cl11]

print(cl11, cl21)
plt.plot(cl11, cl21)

chb11 = [cl11[1], cl11[1]]
chb21 = [rf1[0], cl21[1]]
print(chb11, chb21)
plt.plot(chb11, chb21)

# nc = ncv / 6
# print(nc)
# nc = rf2[1] - nc
# nw11 = [nc, rf2[1]]
# nw21 = [rf1[1], rf1[1]]
# print(nw11, nw21)

# nw11 = [ -x for x in nw11]

# plt.plot(nw11, nw21)

# nc = ncv / 6
# nc = nc + 1.5
# print(nc)
# nc = rf1[1] - nc
# nd11 = [rf2[1], rf2[1]]
# nd21 = [nc, rf1[1]]
# print(nd11, nd21)

# plt.plot(nd11, nd21)

# yoe = chv / 24
# print(yoe)
# yoe = rf1[1] - yoe
# yoe11 = [ahvl11[0], ahvl11[0]]
# yoe21 = [rf1[1], yoe]
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

bnwv = ncv / 6
bnwv = rf1[0] + bnwv
print(bnwv)

bnw11 = [rf1[0], bnwv]
bnw21 = [rf1[1], rf1[1]]
# bnw11 = [ -x for x in bnw11]
print(bnw1, bnw2)

plt.plot(bnw11, bnw21)

byhv = chv / 24
byhv = bnw21[1] + byhv
print(byhv)
byh11 = [bnw11[1], bnw11[1]]
byh21 = [bnw21[1], byhv]
byh11 = [ -x for x in byh11]
print(byh11, byh21)

plt.plot(byh11, byh21)

bnc11 = [byh11[1], bnw11[0]]
bnc21 = [byh21[1], bnw21[1]]
print(bnc11, bnc21)

plt.plot(bnc11, bnc21)

print([int(ahvl11) for ahvl11 in ahvl11])
ahvlv = [ -x for x in ahvl11]

bsl11 = [bnc11[0], ahvlv[0]]
bsl21 = [bnc21[0], ahvl21[0]]
print(bsl11, bsl21)

plt.plot(bsl11, bsl21)

bl1 = [chb1[0], chb11[0]]
bl2 = [chb21[0], chb2[0]]
print(bl1, bl2)

plt.plot(bl1, bl2)

plt.show()
