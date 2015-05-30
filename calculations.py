__author__ = 'George Pamfilis'
__version__ = '1.0'
__contact__ = 'gpamfilis@gmail.com'

import numpy

class EvapoTranspiration(object):
    """
    this class uses the pennman montif method for calculating ET0
    """
    def __init__(self, max_temperature, min_temperature, rh_max, rh_min, elevation,
                 net_radiation_at_the_crop_surface, h):
        self.max_temperature = max_temperature
        self.min_temperature = min_temperature
        self.mean_temperature = 0.5 * (self.min_temperature + self.max_temperature)  # degrees celsius
        self.rh_max = rh_max
        self.rh_min = rh_min
        self.rh_mean = 0.5 * (self.rh_max + self.rh_min)
        self.elevation = elevation
        self.ra = net_radiation_at_the_crop_surface
        self.h = h  # height of wind speed measurement

    def rs_step_2_mean_daily_solar_radiation(self):
        rs = self.ra*0.0864
        return rs

    def u2_step_3_wind_speed(self):
        u_2 = (4.87/(numpy.log(67.8*self.h-5.42)))
        return u_2

    def delta_step_4_slope_of_saturation_vapor_pressure_curve(self):

        delta = ((4098. * (0.610 * numpy.exp((17.27*self.mean_temperature)/(self.mean_temperature+237.3))))/
                 (self.mean_temperature+273.3)**2)
        return delta

    def p_step_5_atmospheric_pressure(self):
        p = 101.3*((293. - 0.0065 * self.elevation) / 293.)**5.26
        return p

    @classmethod
    def gamma_step_6_psychrometric_constant(cls):
        """
        :rtype : float
        :type cls: float
        """
        gamma = 0.000665 * cls.p_step_5_atmospheric_pressure()
        return gamma

    def dt_step_7_delta_term(self):

        dt = (self.step_4_slope_of_saturation_vapor_preassure_curve() /
              (self.step_4_slope_of_saturation_vapor_preassure_curve()+self.step_6_psychrometric_constant() *
               (1+0.34*self.step_3_wind_speed())))
        return dt

    def pt_step_8_psi_term(self):

        pt = self.step_6_psychrometric_constant() / (self.step_4_slope_of_saturation_vapor_preassure_curve() +
                                                     self.step_6_psychrometric_constant() *
                                          (1+0.34*self.step_3_wind_speed()))
        return pt

    def tt_step_9_temperature_term(self):
        tt = (900./(self.mean_temperature+273.)) * self.u2_step_3_wind_speed()
        return tt

    def es_mean_saturation_vapor_pressure_derived_from_air_temperature(self):
        etmax = 0.618* numpy.exp((17.27*self.max_temperature)/self.max_temperature+237.3)
        etmin = 0.618* numpy.exp((17.27*self.min_temperature)/self.min_temperature+237.3)
        es = (etmax+etmin)/2.
        return es, etmin, etmax

    def ea_actual_vapor_pressure(self):
        ea = (self.rh_mean/100.) * ((self.es_mean_saturation_vapor_pressure_derived_from_air_temperature()[1] +
                                     self.es_mean_saturation_vapor_pressure_derived_from_air_temperature()[2])/2)
        return ea

