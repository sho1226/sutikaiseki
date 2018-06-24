def dichotomy(xn,xp,f,e):
	xc = (xn+xp)/2
	if abs(f(xc)) < e: return xc
	d = dichotomy
	return d(xn,xc,f,e) if f(xc) > 0 else d(xc,xp,f,e)