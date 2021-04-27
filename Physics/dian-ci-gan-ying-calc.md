# 物理电磁感应任意时刻速度、路程与任意路程速度

###### tags: `Physics`

导体以 $v_0$ 的速度进入磁感应强度为 $B$ 的磁场区域，经过 $s$ 路程后出磁场，导体质量为 $m$，长度为 $L$，电阻为 $R$，求任意时刻路程、速度。

首先列出关于物体状态的式子：

$$
\begin{aligned}
F = -ma = \dfrac{B^2L^2}{R} v \\
\iff -m\dfrac{\mathrm{d}v}{\mathrm{d}t} = \dfrac{B^2L^2}{R}v \\
\iff \dfrac{\mathrm{d}v}{v} = -\dfrac{B^2L^2}{mR}\mathrm{d}t \\
\iff \int \dfrac{\mathrm{d}v}{v} = \int -\dfrac{B^2L^2}{mR}\mathrm{d}t \\
\implies \ln v = -\dfrac{B^2L^2t}{mR} + C
\end{aligned}
$$

另 $t = 0$，解得 $C = \ln v_0$.

$$
\begin{aligned}
\ln v = -\dfrac{B^2L^2t}{mR} + \ln v_0 \\
\iff \ln \dfrac{v}{v_0} = -\dfrac{B^2L^2t}{mR}\\
\iff \ln \dfrac{v_0}{v} = \dfrac{B^2L^2t}{mR}\\
\implies \dfrac{v_0}{v} = e^{(B^2L^2t)/(mR)}\\
\iff v = \dfrac{v_0}{e^{(B^2L^2t)/(mR)}}
\end{aligned}
$$

这样就得到了 $v$ 关于 $t$ 的式子，接下来对该式积分得到关于 $x$ 的式子：

$$
\begin{aligned}
\int v\mathrm{d}t = \int \dfrac{v_0}{e^{(B^2L^2t)/(mR)}} \mathrm{d}t\\
\implies x = v_0 \int e^{-(B^2L^2t)/(mR)} \mathrm{d}t\\
\iff x = v_0 \dfrac{e^{-(B^2L^2t)/(mR)} - 1}{-\dfrac{B^2L^2}{mR}}\\
\end{aligned}
$$

还可以求任意路程的速度，将 $x = d$ 带入：

$$
\begin{aligned}
& -\dfrac{B^2L^2d}{mR} = v_0(e^{-(B^2L^2t)/(mR)} - 1)\\
& v = \dfrac{v_0}{e^{(B^2L^2t)/(mR)}} = v_0e^{-(B^2L^2t)/(mR)}\\
\implies & v = v_0 - \dfrac{B^2L^2}{R} \times \dfrac{d}{m}\\
\end{aligned}
$$

最终的形式相当简洁。

综上所述，在导体棒于磁场中只受安培力的运动中，我们有：

$$
\begin{aligned}
& \text{let } k = -\dfrac{B^2L^2}{mR}\\
& v = v_0e^{kt}\\
& x = \dfrac{v_0(e^{kt} - 1)}{k}\\
& v = v_0 + kd\\
\end{aligned}
$$