import sys
import matplotlib
import numpy as np
from numpy import matlib
import scipy.stats as stats
from scipy.stats import norm, chi2, t, f
import math
matplotlib.use("Qt5Agg")
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from collections import OrderedDict

class MyMplCanvas(FigureCanvas):
    """FigureCanvas的最终的父类其实是QWidget。"""

    def __init__(self, parent=None,  width=5, height=4, dpi=100):

        # 配置中文显示
        plt.rcParams['font.family'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

        self.fig = Figure(figsize=(width, height), dpi=dpi)  # 新建一个figure
        self.axes = self.fig.add_subplot(111)  # 建立一个子图，如果要建立复合图，可以在这里修改

        #plt.hold(False)  # 每次绘图的时候不保留上一次绘图的结果

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        '''定义FigureCanvas的尺寸策略，这部分的意思是设置FigureCanvas，使之尽可能的向外填充空间。'''
        FigureCanvas.setSizePolicy(self,QSizePolicy.Expanding,QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def fill_chi_plot(self, chi_n, quantile,  a,  b,  arfa):
        c1 = stats.chi2.isf(0.0000001,  chi_n)
        x=np.linspace(quantile, c1, 100)
        self.axes.fill_between(x, stats.chi2.pdf(x,chi_n), alpha=0.5)

        arrowprops = dict(arrowstyle = "-",  color='red',  connectionstyle = "angle,angleA=5,angleB=45,rad=10")
        arrowprops1 = dict(arrowstyle = "->",  color='blue',  connectionstyle = "angle,angleA=0,angleB=45,rad=10")
        self.axes.annotate('分位点坐标：%.3f' % quantile, color='blue',  xy=(quantile, 0), xytext=(0.63,  0.2), textcoords='figure fraction' , arrowprops=arrowprops1)
        self.axes.annotate('α：%.2f' % arfa, color='red',  xy=(quantile + 1, stats.chi2.pdf(quantile+1,chi_n)/2), xytext=(a, b), textcoords='figure fraction' , arrowprops=arrowprops)
        self.draw()
        
    def fill_chi2_plot1(self,a,N, X):
        c2=stats.chi2.isf(0.0000001, N)
        c1=stats.chi2.isf(0.9999999, N)
        x=np.linspace(c1,c2,100)
        p=chi2.ppf(a, N)
        self.axes.fill_between(x, stats.chi2.pdf(x,N), x>p, x<c1 ,color='dodgerblue', edgecolor='black', alpha=0.5)
        self.axes.fill_between(x, stats.chi2.pdf(x,N), x<c1, x>p , color='dodgerblue', edgecolor='black', alpha=0.5)
        self.axes.annotate('观察值', xy=(X, 0), xytext=(0.9, 0.2), textcoords='axes fraction',arrowprops = dict(arrowstyle = "->", connectionstyle = "arc3"))
        self.draw()
        
    def fill_chi2_plot(self, a, N, X):
        p=chi2.ppf(a/2, N)
        q=chi2.ppf(1-a/2, N)
        c2=stats.chi2.isf(0.0000001, N)
        c1 = stats.chi2.isf(0.9999999,  N)
        x=np.linspace(c1,c2,100)
        self.axes.fill_between(x, stats.chi2.pdf(x, N),x<p, x>q, color='dodgerblue', edgecolor='black', alpha=0.5)
        self.axes.fill_between(x, stats.chi2.pdf(x, N),x>q, x<p, color='dodgerblue', edgecolor='black', alpha=0.5)
        self.axes.annotate('观察值', xy=(X, 0), xytext=(0.9, 0.2), textcoords='axes fraction',arrowprops = dict(arrowstyle = "->", connectionstyle = "arc3"))
        self.draw()
    
    def fill_t_plot(self,t_n, quantile, a,  b):
        x=np.linspace(quantile,5, 100 )
        self.axes.fill_between(x, stats.t.pdf(x,t_n), alpha=0.5)
        arrowprops = dict(arrowstyle = "->", connectionstyle = "angle,angleA=0,angleB=45,rad=10")
        self.axes.annotate('%f' % quantile, xy=(quantile, 0), xytext=(a, b), textcoords='figure fraction' , arrowprops=arrowprops)
        self.draw()
        
    def fill_t_plot1(self, a, N, T):
        p=t.ppf(a/2, N)
        q=t.ppf(1-a/2, N)
        x=np.linspace(-10,10,100)
        self.axes.fill_between(x, stats.t.pdf(x, N),x<p, x>q, color='dodgerblue', edgecolor='black', alpha=0.5)
        self.axes.fill_between(x, stats.t.pdf(x, N),x>q, x<p, color='dodgerblue', edgecolor='black', alpha=0.5)
        self.axes.annotate('观察值', xy=(T, 0), xytext=(0.9, 0.2), textcoords='axes fraction',arrowprops = dict(arrowstyle = "->", connectionstyle = "arc3"))
        self.draw()
        
    def fill_f_plot(self, f_m, f_n,  quantile,  a,  b,  arfa):
        x=np.linspace(quantile,7, 100 )
        self.axes.fill_between(x, stats.f.pdf(x,f_m, f_n), alpha=0.5)
        arrowprops = dict(arrowstyle = "-",  color='red',  connectionstyle = "angle,angleA=5,angleB=45,rad=10")
        arrowprops1 = dict(arrowstyle = "->",  color='blue',  connectionstyle = "angle,angleA=0,angleB=45,rad=10")
        #self.axes.annotate('%f' % quantile, xy=(quantile, 0), xytext=(a, b), textcoords='figure fraction' , arrowprops=arrowprops)
        self.axes.annotate('分位点坐标：%.3f' % quantile, color='blue',  xy=(quantile, 0), xytext=(0.63,  0.2), textcoords='figure fraction' , arrowprops=arrowprops1)
        self.axes.annotate('α：%.2f' % arfa, color='red',  xy=(quantile + 1, stats.f.pdf(x,f_m, f_n)/2), xytext=(a, b), textcoords='figure fraction' , arrowprops=arrowprops)
        self.draw()
        
    def fill_f_plot1(self, a, N1, N2, u):
        p=f.ppf(a/2, N1, N2)
        q=f.ppf(1-a/2, N1, N2)
        x=np.linspace(0,7,100)
        self.axes.fill_between(x, stats.f.pdf(x, N1, N2),x<p, x>q, color='dodgerblue', edgecolor='black', alpha=0.5)
        self.axes.fill_between(x, stats.f.pdf(x, N1, N2),x>q, x<p, color='dodgerblue', edgecolor='black', alpha=0.5)
        self.axes.annotate('观察值', xy=(u, 0), xytext=(0.9, 0.2), textcoords='axes fraction',arrowprops = dict(arrowstyle = "->", connectionstyle = "arc3"))
        self.draw()
        
    def fill_f_plot2(self, a, N1, N2, u):
        q=f.ppf(1-a/2, N1, N2)
        x=np.linspace(0,7,100)
        self.axes.fill_between(x, stats.f.pdf(x, N1, N2),x>q,x<0, color='dodgerblue', edgecolor='black', alpha=0.5)
        self.axes.fill_between(x, stats.f.pdf(x, N1, N2),x<0, x>q, color='dodgerblue', edgecolor='black', alpha=0.5)
        self.axes.annotate('观察值', xy=(u, 0), xytext=(0.9, 0.2), textcoords='axes fraction',arrowprops = dict(arrowstyle = "->", connectionstyle = "arc3"))
        self.draw()
    
    def fill_normal_plot(self, a, m, n, U):
        q=norm.ppf(1-a/2)
        p=norm.ppf(a/2)
        x=np.linspace(-10,10,100)
        self.axes.fill_between(x, stats.norm.pdf(x, m, n), x<p, x>q,  color='dodgerblue', edgecolor='black', alpha=0.5)
        self.axes.fill_between(x, stats.norm.pdf(x, m, n), x>q, x<p,  color='dodgerblue', edgecolor='black', alpha=0.5)
        self.axes.annotate('观察值', xy=(U, 0), xytext=(0.9, 0.2), textcoords='axes fraction',arrowprops = dict(arrowstyle = "->", connectionstyle = "arc3"))
        self.draw()
    
    def start_normal_plot(self, m, n): 
        self.axes.cla()
        x=np.linspace(-10,10,100)
        self.axes.plot(x,stats.norm.pdf(x,m,n), label='均值='+str(m )+'方差='+str(n))
        self.axes.set_xlabel('x')
        self.axes.set_ylabel('y')
        self.axes.grid(True)
        self.fig.suptitle("正态分布")
        self.axes.legend()
        self.draw()

    def start_chi_plot(self, chi_n):
        self.fig.suptitle('n为'+str(int(chi_n))+'的卡方分布')
        c2=stats.chi2.isf(0.0000001, chi_n)
        c1 = stats.chi2.isf(0.9999999,  chi_n)
        x = np.linspace( c1, c2, 100)
        self.axes.plot(x, stats.chi2.pdf(x,chi_n), label='n='+str(int(chi_n)))
        self.axes.set_ylabel('Y轴')
        self.axes.set_xlabel('X轴')
        self.axes.grid(True)
        self.axes.legend()
        self.draw()
        
    def start_chi2_plot(self,N):
        self.axes.cla()
        c2=stats.chi2.isf(0.0000001, N)
        c1 = stats.chi2.isf(0.9999999,  N)
        x=np.linspace(c1,c2,100)
        self.axes.plot(x,stats.chi2.pdf(x,N), label='自由度='+str(int(N)))
        self.axes.set_xlabel('x')
        self.axes.set_ylabel('y')
        self.axes.grid(True)
        self.fig.suptitle("卡方分布")
        self.axes.legend()
        self.draw()
        
    def start_f_plot(self,N1, N2):
        self.axes.cla() 
        x=np.linspace(0,7,100)
        self.axes.plot(x,stats.f.pdf(x, N1, N2), label="F(%d,%d)" %(N1, N2))
        self.axes.set_xlabel('x')
        self.axes.set_ylabel('y')
        self.axes.grid(True)
        self.fig.suptitle("F分布")
        self.axes.legend()
        self.draw()
        
    def start_t_plot(self, t_n, flag):
        self.fig.suptitle('n为'+str(int(t_n))+'的t分布')
        x = np.linspace( -5, 5, 100)
        if flag:
            self.axes.plot(x, stats.norm.pdf(x), label='normal')
        self.axes.plot(x,stats.t.pdf(x, t_n), label='n='+str(int(t_n)))
        self.axes.set_ylabel('Y轴')
        self.axes.set_xlabel('X轴')
        self.axes.grid(True)
        handles, labels = self.fig.gca().get_legend_handles_labels()
        by_label = OrderedDict(zip(labels, handles))
        self.axes.legend(by_label.values(), by_label.keys())
        self.draw() 
        
    def start_t_plot1(self,N): 
        self.axes.cla()
        x=np.linspace(-10,10,100)
        self.axes.plot(x,stats.t.pdf(x, N), label='自由度='+str(N))
        self.axes.set_xlabel('x')
        self.axes.set_ylabel('y')
        self.axes.grid(True)
        self.fig.suptitle("t分布")
        self.axes.legend()
        self.draw()
        
    def liner_fitting(self, data_x,data_y):
        size = len(data_x);
        i=0
        sum_xy=0
        sum_y=0
        sum_x=0
        sum_sqare_x=0
        average_x=0;
        average_y=0;
        while i<size:
            sum_xy+=data_x[i]*data_y[i];
            sum_y+=data_y[i]
            sum_x+=data_x[i]
            sum_sqare_x+=data_x[i]*data_x[i]
            i+=1
        average_x=sum_x/size
        average_y=sum_y/size
        return_k=(size*sum_xy-sum_x*sum_y)/(size*sum_sqare_x-sum_x*sum_x)
        return_b=average_y-average_x*return_k
        return [return_k,return_b]
        
    def calculate(self, data_x,k,b):
        datay=[]
        for x in data_x:
            datay.append(k*x+b)
        return datay
        
    def start_Linear_regression_plot(self, data_x,data_y_new,data_y_old):
        self.axes.cla()
        self.fig.suptitle("一元线性拟合数据")
        self.axes.plot(data_x,data_y_new,label="拟合曲线",color="black")
        self.axes.scatter(data_x,data_y_old,label="离散数据")       
        self.axes.legend(loc="upper left")
        self.axes.grid(True)
        self.draw()   
    def start_Single_Normal_plot1(self, m, n, mu, sigma):
        self.axes.cla()
        X=sigma * matlib.randn((n, m)) + mu#模拟抽样，每一列是一个样本容量为n的样本，共抽样m次
        Xmean=np.mean(X,axis=0)#样本均值
        z=(Xmean-mu)/(sigma/math.sqrt(n))
        Z=np.array(z).flatten()
        x=np.linspace(-5, 5, 100)
        N, bins, patches =self.axes.hist(Z, 50, density=1, facecolor="yellow", edgecolor="black", alpha=0.7)
        self.axes.plot(x, stats.norm.pdf(x),"b", label="N(0,1)")
        self.axes.set_xlabel('x')
        self.axes.set_ylabel('pdf')
        self.fig.suptitle("方差$\sigma^2$已知时,样本均值的抽样分布")
        self.axes.legend()
        self.draw()  
    
    def start_Single_Normal_plot2(self, m, n, mu, sigma):
        self.axes.cla()
        X=sigma * matlib.randn((n, m)) + mu#模拟抽样，每一列是一个样本容量为n的样本，共抽样m次
        Xmean=np.mean(X,axis=0)#样本均值
        Xstd=np.std(X,axis=0)#标准差
        T=(Xmean-mu)/(Xstd/math.sqrt(n))
        t=np.array(T).flatten()
        x=np.linspace(-5, 5, 100)
        N, bins, patches =self.axes.hist(t, 50, density=1, facecolor="yellow", edgecolor="black", alpha=0.7)
        self.axes.plot(x, stats.norm.pdf(x),"b", label="N(0,1)")
        self.axes.plot(x, stats.t.pdf(x, n-1),"r", label="t(n-1)")
        self.axes.set_xlabel('x')
        self.axes.set_ylabel('pdf')
        self.fig.suptitle("方差$\sigma^2$未知时,样本均值的抽样分布")
        self.axes.legend()
        self.draw()

    def start_Single_Normal_plot3(self, m, n, mu, sigma):
        self.axes.cla()
        X=sigma * matlib.randn((n, m)) + mu#模拟抽样，每一列是一个样本容量为n的样本，共抽样m次
        c2=stats.chi2.isf(0.0000001, n-1)
        x=np.linspace(0, c2, 100)
        zhen2=np.var(X, axis=0)
        xchi2=(np.dot((n), np.array(zhen2)))/(sigma*sigma)
        Xchi2=np.array(xchi2).flatten()
        N, bins, patches =self.axes.hist(Xchi2, 50, density=1, facecolor="yellow", edgecolor="black", alpha=0.7)
        self.axes.plot(x, stats.chi2.pdf(x, n-1),"b", label="$\chi2(n-1)$")
        self.axes.set_xlabel('x')
        self.axes.set_ylabel('pdf')
        self.fig.suptitle("方差$S^2$的抽样分布")
        self.axes.legend()
        self.draw()
    
    def start_Double_Normal_plot1(self, m1, n1, m2, n2,  mu1, sigma1, mu2, sigma2):
        self.axes.cla()
        X=sigma1 * matlib.randn((n1, m1)) + mu1#模拟抽样，每一列是一个样本容量为n的样本，共抽样m次
        Y=sigma2 * matlib.randn((n2, m2)) + mu2
        zhen1=np.var(X, axis=0)#样本方差
        zhen2=np.var(Y,axis=0)
        S1=np.array(zhen1).flatten()
        S2=np.array(zhen2).flatten()
        F=(S1*sigma2*sigma2)/(S2*sigma1*sigma1)
        c2=stats.f.isf(0.005, n1-1,n2-1)
        x=np.linspace(0, c2, 100)
        N, bins, patches =self.axes.hist(F, 100, density=1, facecolor="yellow", edgecolor="black", alpha=0.7)
        self.axes.plot(x, stats.f.pdf(x, n1-1,n2-1),"b", label="F(n1-1,n2-1)")
        self.axes.set_xlabel('x')
        self.axes.set_ylabel('pdf')
        self.fig.suptitle("已知方差$σ^2$的两总体的样本方差比的分布")
        self.axes.legend()
        self.draw()
        
    def start_Double_Normal_plot2(self, m1, n1, m2, n2,  mu1, sigma1, mu2, sigma2):
        self.axes.cla()
        sigma=sigma1
        X=sigma * matlib.randn((n1, m1)) + mu1#模拟抽样，每一列是一个样本容量为n的样本，共抽样m次
        Y=sigma * matlib.randn((n2, m2)) + mu2
        Xmean1=np.mean(X,axis=0)
        Xmean2=np.mean(Y,axis=0)
        Xmean=np.array(Xmean1).flatten()
        Ymean=np.array(Xmean2).flatten()
        zhen1=np.var(X, axis=0)#样本方差
        zhen2=np.var(Y,axis=0)
        S1=np.array(zhen1).flatten()
        S2=np.array(zhen2).flatten()
        S=np.sqrt(((n1-1)*S1+(n2-1)*S2)/(n1+n2-2))
        t=(Xmean-Ymean-(mu1-mu2))/(S*(math.sqrt(1/n1+1/n2)))
        c2=stats.t.isf(0.00001, n1+n2-2)
        x=np.linspace(-c2, c2, 100)
        N, bins, patches =self.axes.hist(t, 50, density=1, facecolor="yellow", edgecolor="black", alpha=0.7)
        self.axes.plot(x, stats.t.pdf(x, n1+n2-2),"b", label="t(n1+n2-2)")
        self.axes.set_xlabel('x')
        self.axes.set_ylabel('pdf')
        self.fig.suptitle("方差$σ^2$相等的两总体的样本方差比的分布")
        self.axes.legend()
        self.draw()

    def start_Double_Normal_plot3(self, m1, n1, m2, n2,  mu1, sigma1, mu2, sigma2):
        self.axes.cla()
        X=sigma1 * matlib.randn((n1, m1)) + mu1#模拟抽样，每一列是一个样本容量为n的样本，共抽样m次
        Y=sigma2 * matlib.randn((n2, m2)) + mu2
        xmean=np.mean(X,axis=0)
        ymean=np.mean(Y,axis=0)
        Xmean=np.array(xmean).flatten()
        Ymean=np.array(ymean).flatten()
        U=(Xmean-Ymean-(mu1-mu2))/(np.sqrt((sigma1*sigma1)/n1+(sigma2*sigma2)/n2))
        c2=stats.norm.isf(0.001, 0,1)
        x=np.linspace(-c2, c2, 100)
        N, bins, patches =self.axes.hist(U, 50, density=1, facecolor="yellow", edgecolor="black", alpha=0.7)
        self.axes.plot(x, stats.norm.pdf(x, 0,1),"b", label="N(0,1)")
        self.axes.set_xlabel('x')
        self.axes.set_ylabel('pdf')
        self.fig.suptitle("已知方差$σ^2$的两总体的样本均值的分布")
        self.axes.legend()
        self.draw()
        
        
    def draw_hist(self, N,y):
        self.axes.cla()
        x = np.arange(1, N+1, 1)
        ys = np.mean(y)
        self.axes.bar(x,y)
        if N<=20:
            for a,b in zip(x,y):
                if b>0:
                    self.axes.text(a,b+0.15,'%.2f'%b,ha = 'center',va = 'bottom')
                else:
                    self.axes.text(a,b-0.4,'%.2f'%b,ha = 'center',va = 'bottom')
        self.axes.axhline(y=ys,c="r")
        self.axes.text(-1, ys+0.2, '均值=%.4f' % ys, ha='center', va= 'bottom',fontsize=12, color = "b")
        self.axes.set_xlabel('样本编号')
        self.axes.set_ylabel('样本值')
        self.fig.suptitle("样本分布图")
        self.axes.legend()
        self.draw()
        #ymin = math.floor(y[0])
        #ymax = math.ceil(y[-1])
        #self.fig.suptitle('样本分布图')
        #self.axes1.spines['bottom'].set_position(('data',ymin))
        #self.axes1.spines['left'].set_position(('data', 0))
        #self.axes2.spines['bottom'].set_position(('data',ymin))
        #self.axes2.spines['left'].set_position(('data', 0))
        #self.axes2.bar(num.keys(), num.values())
        #self.axes1.set_yticks(np.linspace(ymin,ymax)
        #self.axes1.set_xticks(np.linspace(1,N,num=10))
        #self.axes1.autoscale()
        #if N <= 20:
            #self.axes1.set_xticks(np.linspace(1,N,num=N))
            #self.axes2.set_xticks(np.linspace(1,N,num=N))
        
    def draw_hist2(self,N, y, mean, std, m, n):
        self.axes.cla()
        ys = math.ceil(max(abs(min(y)), max(y)))
        x=np.linspace(mean-ys, mean+ys, 100)
        N, bins, patches =self.axes.hist(y, 50, density=1, facecolor="yellow", edgecolor="black", alpha=0.7)
        self.axes.plot(x, stats.norm.pdf(x, loc=m, scale=n),"b", label='N(%.2f,%.2f)' %(m, n))
        self.axes.axvline(x=mean , c='r')
        self.axes.text(mean, -0.08/len(N), '样本均值=%.4f' %mean, ha='center', va= 'bottom',fontsize=12, color = "b")
        self.axes.set_xlabel('x')
        self.axes.set_ylabel('pdf')
        self.fig.suptitle("样本的分布")
        self.axes.legend()
        self.draw()
        
    def draw_hist3(self, N1,N2, y1, y2):
        self.axes.cla()
        N = max(N1, N2)
        x1 = np.arange(1, N1+1, 1)
        x2 = np.arange(1, N2+1, 1)
        y1.sort()
        y2.sort()
        ys1 = np.mean(y1)
        ys2 = np.mean(y2)
        bar_width = 0.3*20/N
        self.axes.bar(x1-bar_width /2,y1, width=bar_width, color = 'r')
        self.axes.bar(x2+bar_width /2,y2, width=bar_width, color = 'g')
        if N<=15:
            for a,b in zip(x1,y1):
                if b>0:
                    self.axes.text(a,b+0.15,'%.2f'%b,ha = 'center',va = 'bottom')
                else:
                    self.axes.text(a,b-0.4,'%.2f'%b,ha = 'center',va = 'bottom')
            for a,b in zip(x2,y2):
                if b>0:
                    self.axes.text(a,b+0.15,'%.2f'%b,ha = 'center',va = 'bottom')
                else:
                    self.axes.text(a,b-0.4,'%.2f'%b,ha = 'center',va = 'bottom')
        #self.axes.axhline(y=ys1,c="r")
        #self.axes.axhline(y=ys2,c="g")
        self.axes.plot(x1, np.array([ys1]*N1), label = '均值=%.4f'%ys1, color = 'r')
        self.axes.plot(x2, np.array([ys2]*N2), label = '均值=%.4f'%ys2, color = 'g')
        #self.axes.text(-1, ys1+0.2, '均值=%.4f' % ys1, ha='center', va= 'bottom',fontsize=12, color = "b")
        #self.axes.text(-1, ys2+0.2, '均值=%.4f' % ys2, ha='center', va= 'bottom',fontsize=12, color = "b")
        self.axes.set_xlabel('样本编号')
        self.axes.set_ylabel('样本值')
        self.fig.suptitle("样本分布图")
        self.axes.legend()
        self.draw()
    
class Plot(QWidget):
    def __init__(self, parent=None):
        super(Plot, self).__init__(parent)
        self.initUi()

    def initUi(self):
        self.layout = QVBoxLayout(self)
        self.mpl = MyMplCanvas(self,width=5, height=4, dpi=100)
        self.mpl_ntb = NavigationToolbar(self.mpl, self)
        self.layout.addWidget(self.mpl)
        self.layout.addWidget(self.mpl_ntb)
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Plot()
    ui.mpl.start_Single_Normal_plot3()
    ui.show()
    sys.exit(app.exec_())
