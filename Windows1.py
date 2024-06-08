# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class MyWindow1
###########################################################################

class MyWindow1 ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Mein erstes Fenster"), pos = wx.DefaultPosition, size = wx.Size( 640,339 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.lbl_ueber = wx.StaticText( self, wx.ID_ANY, _(u"Benutzeranfrage"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.lbl_ueber.Wrap( -1 )

        self.lbl_ueber.SetFont( wx.Font( 25, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer1.Add( self.lbl_ueber, 0, wx.ALL|wx.EXPAND, 5 )

        self.lbl_name = wx.StaticText( self, wx.ID_ANY, _(u"Ihr Name"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lbl_name.Wrap( -1 )

        bSizer1.Add( self.lbl_name, 0, wx.ALL, 5 )

        self.txtctl_name = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.txtctl_name, 0, wx.ALL|wx.EXPAND, 5 )

        self.lbl_mail = wx.StaticText( self, wx.ID_ANY, _(u"E-Mail"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lbl_mail.Wrap( -1 )

        bSizer1.Add( self.lbl_mail, 0, wx.ALL, 5 )

        self.txtctl_mail = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.txtctl_mail, 0, wx.ALL|wx.EXPAND, 5 )

        self.lbl_comment = wx.StaticText( self, wx.ID_ANY, _(u"Kommentar"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lbl_comment.Wrap( -1 )

        bSizer1.Add( self.lbl_comment, 0, wx.ALL, 5 )

        self.txtctl_comment = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
        bSizer1.Add( self.txtctl_comment, 1, wx.ALL|wx.EXPAND, 5 )

        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

        self.btn_save = wx.Button( self, wx.ID_ANY, _(u"Speichern"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.btn_save, 1, wx.ALL|wx.EXPAND, 5 )

        self.btn_cancel = wx.Button( self, wx.ID_ANY, _(u"Abbrechen"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.btn_cancel, 1, wx.ALL|wx.EXPAND, 5 )


        bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.btn_save.Bind( wx.EVT_BUTTON, self.OnBtnSaveClicked )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnBtnSaveClicked( self, event ):
        event.Skip()


