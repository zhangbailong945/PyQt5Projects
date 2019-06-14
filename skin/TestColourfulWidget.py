#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2019年1月20日
@author: Irony
@site: https://pyqt5.com https://github.com/892768447
@email: 892768447@qq.com
@file: Utils.TestColourfulWidget
@description: 
"""
from PyQt5.QtCore import Qt
from CommonUtil import Signals
from ColourfulWidget import ColourfulWidget
from PreviewWidget import PreviewWidget


class ColorWidget(ColourfulWidget):

    def __init__(self,*args,**kwargs):
        super(ColorWidget,self).__init__(self,*args,**kwargs)
        # 背景透明
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        # 无边框
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.widgetBottom.setVisible(False)
        # 预览界面
        self.previewWidget = PreviewWidget(self.widgetSkinBg)
        self.previewWidget.setVisible(False)
        # 初始化信号槽
        self._initSignals()
    
    def _initSignals(self):
        # 点击颜色
        Signals.colourfulItemClicked.connect(self.onColourfulItemClicked)
    
    def onColourfulItemClicked(self, name, color):
        """
        :param name:        颜色名字
        :param color:       颜色
        """
        self.previewWidget.setVisible(True)
        self.previewWidget.setTitle(name)
        self.previewWidget.setPixmap(PreviewWidget.Color, color)