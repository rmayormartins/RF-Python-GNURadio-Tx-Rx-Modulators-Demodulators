#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Qpsk Rx
# Generated: Wed Nov 23 15:36:44 2016
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import audio
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import numpy as np
import osmosdr
import sip
import sys
import time


class qpsk_rx(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Qpsk Rx")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Qpsk Rx")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "qpsk_rx")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 240e3
        self.Rs = Rs = 48e3
        self.sps = sps = int(samp_rate / Rs)
        self.sdr_rate = sdr_rate = 2.4e6
        self.freq_corr = freq_corr = 11
        self.constellation = constellation = digital.constellation_calcdist(([1, 1j, -1, -1j]), ([0, 1, 3, 2]), 4, 1).base()
        self.carrier = carrier = 671e6
        self.access_code = access_code = "1010110111001001"

        ##################################################
        # Blocks
        ##################################################
        self.tab = Qt.QTabWidget()
        self.tab_widget_0 = Qt.QWidget()
        self.tab_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_0)
        self.tab_grid_layout_0 = Qt.QGridLayout()
        self.tab_layout_0.addLayout(self.tab_grid_layout_0)
        self.tab.addTab(self.tab_widget_0, "Received / Costas Loop")
        self.tab_widget_1 = Qt.QWidget()
        self.tab_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_1)
        self.tab_grid_layout_1 = Qt.QGridLayout()
        self.tab_layout_1.addLayout(self.tab_grid_layout_1)
        self.tab.addTab(self.tab_widget_1, "Tab 1")
        self.tab_widget_2 = Qt.QWidget()
        self.tab_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_2)
        self.tab_grid_layout_2 = Qt.QGridLayout()
        self.tab_layout_2.addLayout(self.tab_grid_layout_2)
        self.tab.addTab(self.tab_widget_2, "Tab 2")
        self.top_layout.addWidget(self.tab)
        self._freq_corr_range = Range(-100, 100, 1, 11, 200)
        self._freq_corr_win = RangeWidget(self._freq_corr_range, self.set_freq_corr, "freq_corr", "counter_slider", float)
        self.tab_layout_0.addWidget(self._freq_corr_win)
        self.rtlsdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "rtl=0" )
        self.rtlsdr_source_0.set_sample_rate(sdr_rate)
        self.rtlsdr_source_0.set_center_freq(carrier, 0)
        self.rtlsdr_source_0.set_freq_corr(freq_corr, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(0, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(0, 0)
        self.rtlsdr_source_0.set_gain_mode(False, 0)
        self.rtlsdr_source_0.set_gain(30, 0)
        self.rtlsdr_source_0.set_if_gain(30, 0)
        self.rtlsdr_source_0.set_bb_gain(30, 0)
        self.rtlsdr_source_0.set_antenna("", 0)
        self.rtlsdr_source_0.set_bandwidth(0, 0)
          
        self.root_raised_cosine_filter_0_0 = filter.interp_fir_filter_ccf(1, firdes.root_raised_cosine(
        	1, samp_rate, Rs, 0.35, int(11*sps)))
        self.rational_resampler_xxx_1 = filter.rational_resampler_fff(
                interpolation=4,
                decimation=1,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_ccc(
                interpolation=int(samp_rate),
                decimation=int(sdr_rate),
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_time_sink_x_0_1 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0_1.set_update_time(0.10)
        self.qtgui_time_sink_x_0_1.set_y_axis(-2, 2)
        
        self.qtgui_time_sink_x_0_1.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_1.set_trigger_mode(qtgui.TRIG_MODE_AUTO, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_1.enable_autoscale(False)
        self.qtgui_time_sink_x_0_1.enable_grid(False)
        self.qtgui_time_sink_x_0_1.enable_control_panel(True)
        
        if not True:
          self.qtgui_time_sink_x_0_1.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(2*2):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0_1.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_1.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1.pyqwidget(), Qt.QWidget)
        self.tab_layout_1.addWidget(self._qtgui_time_sink_x_0_1_win)
        self.qtgui_sink_x_1 = qtgui.sink_f(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	48e3, #bw
        	"", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_1.set_update_time(1.0/20)
        self._qtgui_sink_x_1_win = sip.wrapinstance(self.qtgui_sink_x_1.pyqwidget(), Qt.QWidget)
        self.tab_layout_2.addWidget(self._qtgui_sink_x_1_win)
        
        self.qtgui_sink_x_1.enable_rf_freq(False)
        
        
          
        self.qtgui_sink_x_0_0 = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	sdr_rate, #bw
        	"", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_0_win = sip.wrapinstance(self.qtgui_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.tab_layout_0.addWidget(self._qtgui_sink_x_0_0_win)
        
        self.qtgui_sink_x_0_0.enable_rf_freq(False)
        
        
          
        self.qtgui_sink_x_0 = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	sdr_rate, #bw
        	"", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)
        self.tab_layout_0.addWidget(self._qtgui_sink_x_0_win)
        
        self.qtgui_sink_x_0.enable_rf_freq(False)
        
        
          
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, Rs, 5e3, firdes.WIN_HAMMING, 6.76))
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_ccc(sps, (1, ))
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.digital_costas_loop_cc_0 = digital.costas_loop_cc(np.pi/100, 4, False)
        self.digital_correlate_access_code_xx_ts_0 = digital.correlate_access_code_bb_ts(access_code,
          0, "frame_start")
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(constellation)
        self.digital_clock_recovery_mm_xx_0 = digital.clock_recovery_mm_cc(sps, 0.25*0.175*0.175, 0.5, 0.175, 0.005)
        self.blocks_unpack_k_bits_bb_1 = blocks.unpack_k_bits_bb(2)
        self.blocks_pack_k_bits_bb_0 = blocks.pack_k_bits_bb(8)
        self.blocks_char_to_float_0_0 = blocks.char_to_float(1, 128)
        self.audio_sink_0 = audio.sink(48000, "", True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_char_to_float_0_0, 0), (self.rational_resampler_xxx_1, 0))    
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.blocks_char_to_float_0_0, 0))    
        self.connect((self.blocks_unpack_k_bits_bb_1, 0), (self.digital_correlate_access_code_xx_ts_0, 0))    
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.digital_constellation_decoder_cb_0, 0))    
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.interp_fir_filter_xxx_0, 0))    
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.blocks_unpack_k_bits_bb_1, 0))    
        self.connect((self.digital_correlate_access_code_xx_ts_0, 0), (self.blocks_pack_k_bits_bb_0, 0))    
        self.connect((self.digital_costas_loop_cc_0, 0), (self.qtgui_sink_x_0, 0))    
        self.connect((self.digital_costas_loop_cc_0, 0), (self.root_raised_cosine_filter_0_0, 0))    
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.qtgui_time_sink_x_0_1, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.digital_costas_loop_cc_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_sink_x_0_0, 0))    
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.low_pass_filter_0, 0))    
        self.connect((self.rational_resampler_xxx_1, 0), (self.audio_sink_0, 0))    
        self.connect((self.rational_resampler_xxx_1, 0), (self.qtgui_sink_x_1, 0))    
        self.connect((self.root_raised_cosine_filter_0_0, 0), (self.digital_clock_recovery_mm_xx_0, 0))    
        self.connect((self.root_raised_cosine_filter_0_0, 0), (self.qtgui_time_sink_x_0_1, 1))    
        self.connect((self.rtlsdr_source_0, 0), (self.rational_resampler_xxx_0_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "qpsk_rx")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.Rs, 5e3, firdes.WIN_HAMMING, 6.76))
        self.root_raised_cosine_filter_0_0.set_taps(firdes.root_raised_cosine(1, self.samp_rate, self.Rs, 0.35, int(11*self.sps)))
        self.set_sps(int(self.samp_rate / self.Rs))
        self.qtgui_time_sink_x_0_1.set_samp_rate(self.samp_rate)

    def get_Rs(self):
        return self.Rs

    def set_Rs(self, Rs):
        self.Rs = Rs
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.Rs, 5e3, firdes.WIN_HAMMING, 6.76))
        self.root_raised_cosine_filter_0_0.set_taps(firdes.root_raised_cosine(1, self.samp_rate, self.Rs, 0.35, int(11*self.sps)))
        self.set_sps(int(self.samp_rate / self.Rs))

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.digital_clock_recovery_mm_xx_0.set_omega(self.sps)
        self.root_raised_cosine_filter_0_0.set_taps(firdes.root_raised_cosine(1, self.samp_rate, self.Rs, 0.35, int(11*self.sps)))

    def get_sdr_rate(self):
        return self.sdr_rate

    def set_sdr_rate(self, sdr_rate):
        self.sdr_rate = sdr_rate
        self.qtgui_sink_x_0_0.set_frequency_range(0, self.sdr_rate)
        self.qtgui_sink_x_0.set_frequency_range(0, self.sdr_rate)
        self.rtlsdr_source_0.set_sample_rate(self.sdr_rate)

    def get_freq_corr(self):
        return self.freq_corr

    def set_freq_corr(self, freq_corr):
        self.freq_corr = freq_corr
        self.rtlsdr_source_0.set_freq_corr(self.freq_corr, 0)

    def get_constellation(self):
        return self.constellation

    def set_constellation(self, constellation):
        self.constellation = constellation

    def get_carrier(self):
        return self.carrier

    def set_carrier(self, carrier):
        self.carrier = carrier
        self.rtlsdr_source_0.set_center_freq(self.carrier, 0)

    def get_access_code(self):
        return self.access_code

    def set_access_code(self, access_code):
        self.access_code = access_code


def main(top_block_cls=qpsk_rx, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
