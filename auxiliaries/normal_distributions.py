import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 400)

params = [
    (0.0, 1.0, r"$\mu=0,\ \sigma=1$"),
    (1.5, 1.0, r"$\mu=1.5,\ \sigma=1$"),
    (-1.0, 0.6, r"$\mu=0,\ \sigma=0.6$"),
]

plt.figure(figsize=(5, 3))
for mu, sigma, label in params:
    y = (1/(np.sqrt(2*np.pi)*sigma)) * np.exp(-(x-mu)**2/(2*sigma**2))
    plt.plot(x, y, label=label)

plt.xlabel("$\omega$")
plt.ylabel("$p(\mu,\sigma;\omega)$")
plt.legend(loc="upper right", fontsize=8)
plt.tight_layout()
plt.savefig("auxiliaries/normals-mu-sigma.png", dpi=200)
plt.close()
