for i in range(10):
    lux.setCamera("相机 {}".format(i+1))
    opts = lux.getRenderOptions()
#    opts.setMaxTimeRendering(10)
    lux.renderImage("E:/学校资源/表格/KeyShot-Scripts-master/{}.png".format(i+1), width=2560, height=2560, opts=opts)
