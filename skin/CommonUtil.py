from PyQt5.QtCore import QSettings, QTextCodec, QObject, pyqtSignal

class _Signals(QObject):

    # 显示代码
    showCoded = pyqtSignal(str)
    # 显示Readme.md
    showReadmed = pyqtSignal(str)
    # 加载网址
    urlLoaded = pyqtSignal(str)
    # 运行例子信号
    runExampled = pyqtSignal(str)
    # 过滤筛选目录
    filterChanged = pyqtSignal(str)
    # 更新进度条(当前值,最大值)
    progressUpdated = pyqtSignal(int, int)
    # 关闭进度条
    progressStoped = pyqtSignal()
    # 克隆完成
    cloneFinished = pyqtSignal(str)
    # 跳转到item
    itemJumped = pyqtSignal(str)

    # 显示更新对话框
    updateDialogShowed = pyqtSignal()
    # 更新版本文字改变
    updateTextChanged = pyqtSignal(str, str, str)
    # 更新完成
    updateFinished = pyqtSignal(str)
    # 更新进度条(当前值,最小值,最大值)
    updateProgressChanged = pyqtSignal(int, int, int)

    # 登录失败
    loginErrored = pyqtSignal(str)
    # 登录成功发送用户的id和昵称
    loginSuccessed = pyqtSignal(str, str)

    # 添加多彩item
    colourfulItemAdded = pyqtSignal(int, int, str, object)
    # 添加多彩item完成
    colourfulItemAddFinished = pyqtSignal()
    # 多彩item点击,色彩
    colourfulItemClicked = pyqtSignal(str, object)

    # 添加主题item
    themeItemAdded = pyqtSignal(int, int, str, object)
    # 添加主题item完成
    themeItemAddFinished = pyqtSignal()
    # 主推item点击,路径
    themeItemClicked = pyqtSignal(str, object)

    # 分类图片下载完成并添加item
    pictureItemAdded = pyqtSignal(object, int, str, str)
    # 分类图片item点击,路径
    pictureItemClicked = pyqtSignal(str, object)
    # 单个分类下载完成
    pictureDownFinished = pyqtSignal(object)


# 说白了就是全局信号定义
Signals = _Signals()