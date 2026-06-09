import numpy as np
import matplotlib.pyplot as plt

# random.txt: egy sorban egy unsigned 64 bites egész, decimálisan
data = np.loadtxt("random.txt", dtype=np.uint64)

print("Darabszam:", len(data))
print("Minimum:", data.min())
print("Maximum:", data.max())
print("Atlag:", data.mean())
print("Szoras:", data.std())

unique_count = len(np.unique(data))
print("Egyedi ertekek:", unique_count)
print("Duplikaciok:", len(data) - unique_count)

# Bitbalansz
ones = sum(int(x).bit_count() for x in data)
total_bits = len(data) * 64
zeros = total_bits - ones

print("Osszes bit:", total_bits)
print("Egyesek:", ones)
print("Nullak:", zeros)
print("Egyes arany:", ones / total_bits)

# Also 8 bit
low8 = (data & np.uint64(0xFF)).astype(np.uint16)

plt.figure()
plt.hist(low8, bins=256, range=(0, 255))
plt.title("Also 8 bit eloszlasa")
plt.xlabel("Ertek")
plt.ylabel("Darabszam")
plt.show()

# Felso 8 bit
high8 = ((data >> np.uint64(56)) & np.uint64(0xFF)).astype(np.uint16)

plt.figure()
plt.hist(high8, bins=256, range=(0, 255))
plt.title("Felso 8 bit eloszlasa")
plt.xlabel("Ertek")
plt.ylabel("Darabszam")
plt.show()

# Also 16 bit, kevesebb binbe csoportositva
low16 = (data & np.uint64(0xFFFF)).astype(np.uint32)

plt.figure()
plt.hist(low16, bins=256, range=(0, 65535))
plt.title("Also 16 bit eloszlasa 256 csoportban")
plt.xlabel("Ertek")
plt.ylabel("Darabszam")
plt.show()

# Egymast koveto ertekek scatter plotja
sample_size = min(50000, len(data) - 1)

x = data[:sample_size].astype(np.float64)
y = data[1:sample_size + 1].astype(np.float64)

plt.figure()
plt.scatter(x, y, s=1)
plt.title("Egymast koveto RDRAND ertekek")
plt.xlabel("random[i]")
plt.ylabel("random[i+1]")
plt.show()

# Egymast koveto ertekek scatter plotja
# x tengely: random[i]
# y tengely: random[i+1]
# Jo RNG eseten strukturamentes, egyenletes pontfelhot varunk.

sample_size = min(50000, len(data) - 1)

x = data[:sample_size].astype(np.float64)
y = data[1:sample_size + 1].astype(np.float64)

plt.figure(figsize=(8, 8))
plt.scatter(x, y, s=1, alpha=0.35)

plt.title("Egymast koveto RDRAND ertekek kapcsolata")
plt.xlabel("random[i]")
plt.ylabel("random[i + 1]")

plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()