import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

def normfun(x, mean, var):
    pdf = np.exp(-((x - mean)**2)/(2*var)) / (np.sqrt(var) * np.sqrt(2*np.pi))
    return pdf

if __name__ == '__main__':
    x = np.arange(0, 1, 0.01)
    x_fraction = np.arange(1.5, 4.5)
    I = normfun(x, 0.125666864, 0.002494339)
    I_ext = normfun(x, 0.129781494, 0.002430265)
    E = normfun(x, 0.047612564, 0.000324735)
    E_ext = normfun(x, 0.045638258, 0.000285778)
    fraction = normfun(x_fraction, 2.65659, 0.15771)
    fraction_ext = normfun(x, 2.900734, 0.482875)
    plt.subplot(1,3,1), plt.plot(x, I), plt.plot(x, I_ext), plt.xlim(0,0.5)
    plt.legend(['interior', 'exterior']), plt.title('I')
    plt.subplot(1,3,2), plt.plot(x, E), plt.plot(x, E_ext), plt.xlim(0,0.5)
    plt.legend(['interior', 'exterior']), plt.title('E')
    plt.subplot(1,3,3), plt.plot(x, fraction), plt.plot(x, fraction_ext)
    plt.legend(['interior', 'exterior'])

    plt.title('Zeb comparison'), plt.show()