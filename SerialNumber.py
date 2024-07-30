import pyperclip
import wx
import subprocess
class main(wx.Frame):
	def __init__(self):
		super().__init__(None, title="SerialNumber")
		self.panel = wx.Panel(self)
		wx.StaticText(self.panel, label="Your computer's serial number is:")
		self.serial_number = wx.TextCtrl(self.panel, -1,style=wx.TE_MULTILINE+wx.HSCROLL+wx.TE_READONLY, value=self.get_serial_number(), size=(300, -1))
		copy= wx.Button(self.panel, -1, "&copy")
		self.Center()
		self.Show()
		self.Bind(wx.EVT_BUTTON, lambda event: 		pyperclip.copy(self.serial_number.Value), copy)
	def get_serial_number(self):
		output = subprocess.run(['wmic', 'bios', 'get', 'serialnumber'], capture_output=True).stdout.decode('utf-8')
		return output.split('\n')[1].strip()
app=wx.App()
w=main()
w.Show()
app.MainLoop()