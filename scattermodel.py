import matplotlib.pyplot as plt
from scipy import stats
x=[5,7,8,7,2,17,9,4,11,12,9,6]
y=[99,86,87,88,111,103,87,94,78,77,85,86]
slope.intersect.r.p,std.err=stats.linregress(x,y)
def myfunc(x):
    return slope *x + intercept
mymodel=list(map(myfunc,x))
plt.scatter(x, y)
plt.plot(x,mymodel)
plt.show()