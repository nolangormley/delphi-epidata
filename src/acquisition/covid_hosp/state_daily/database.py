# first party
from delphi.epidata.acquisition.covid_hosp.common.database import Database as BaseDatabase
from delphi.epidata.acquisition.covid_hosp.common.database import Columndef
from delphi.epidata.acquisition.covid_hosp.common.utils import Utils

import pandas as pd


class Database(BaseDatabase):

  # note we share a database with state_timeseries
  TABLE_NAME = 'covid_hosp_state_timeseries'
  KEY_COLS = ['state', 'reporting_cutoff_start']
  # These are 3-tuples of (CSV header name, SQL db column name, data type) for
  # all the columns in the CSV file.
  # Note that the corresponding database column names may be shorter
  # due to constraints on the length of column names. See
  # /src/ddl/covid_hosp.sql for more information.
  # Additionally, all column names below are shared with state_timeseries,
  # except for reporting_cutoff_start (here) and date (there). If you need
  # to update a column name, do it in both places.
  ORDERED_CSV_COLUMNS = [
      Columndef('state', 'state', str),
      Columndef('reporting_cutoff_start', 'date', Utils.int_from_date),
      Columndef('adult_icu_bed_covid_utilization', 'adult_icu_bed_covid_utilization', float),
      Columndef('adult_icu_bed_covid_utilization_coverage', 'adult_icu_bed_covid_utilization_coverage', int),
      Columndef('adult_icu_bed_covid_utilization_denominator', 'adult_icu_bed_covid_utilization_denominator',
       int),
      Columndef('adult_icu_bed_covid_utilization_numerator', 'adult_icu_bed_covid_utilization_numerator',
       int),
      Columndef('adult_icu_bed_utilization', 'adult_icu_bed_utilization', float),
      Columndef('adult_icu_bed_utilization_coverage', 'adult_icu_bed_utilization_coverage', int),
      Columndef('adult_icu_bed_utilization_denominator', 'adult_icu_bed_utilization_denominator', int),
      Columndef('adult_icu_bed_utilization_numerator', 'adult_icu_bed_utilization_numerator', int),
      Columndef('critical_staffing_shortage_anticipated_within_week_no',
       'critical_staffing_shortage_anticipated_within_week_no', int),
      Columndef('critical_staffing_shortage_anticipated_within_week_not_reported',
       'critical_staffing_shortage_anticipated_within_week_not_reported', int),
      Columndef('critical_staffing_shortage_anticipated_within_week_yes',
       'critical_staffing_shortage_anticipated_within_week_yes', int),
      Columndef('critical_staffing_shortage_today_no', 'critical_staffing_shortage_today_no', int),
      Columndef('critical_staffing_shortage_today_not_reported',
       'critical_staffing_shortage_today_not_reported', int),
      Columndef('critical_staffing_shortage_today_yes', 'critical_staffing_shortage_today_yes', int),
      Columndef('deaths_covid', 'deaths_covid', int),
      Columndef('deaths_covid_coverage', 'deaths_covid_coverage', int),
      Columndef('geocoded_state', 'geocoded_state', str),
      Columndef('hospital_onset_covid', 'hospital_onset_covid', int),
      Columndef('hospital_onset_covid_coverage', 'hospital_onset_covid_coverage', int),
      Columndef('icu_patients_confirmed_influenza', 'icu_patients_confirmed_influenza', int),
      Columndef('icu_patients_confirmed_influenza_coverage', 'icu_patients_confirmed_influenza_coverage',
       int),
      Columndef('inpatient_bed_covid_utilization', 'inpatient_bed_covid_utilization', float),
      Columndef('inpatient_bed_covid_utilization_coverage', 'inpatient_bed_covid_utilization_coverage', int),
      Columndef('inpatient_bed_covid_utilization_denominator', 'inpatient_bed_covid_utilization_denominator',
       int),
      Columndef('inpatient_bed_covid_utilization_numerator', 'inpatient_bed_covid_utilization_numerator',
       int),
      Columndef('inpatient_beds', 'inpatient_beds', int),
      Columndef('inpatient_beds_coverage', 'inpatient_beds_coverage', int),
      Columndef('inpatient_beds_used', 'inpatient_beds_used', int),
      Columndef('inpatient_beds_used_coverage', 'inpatient_beds_used_coverage', int),
      Columndef('inpatient_beds_used_covid', 'inpatient_beds_used_covid', int),
      Columndef('inpatient_beds_used_covid_coverage', 'inpatient_beds_used_covid_coverage', int),
      Columndef('inpatient_beds_utilization', 'inpatient_beds_utilization', float),
      Columndef('inpatient_beds_utilization_coverage', 'inpatient_beds_utilization_coverage', int),
      Columndef('inpatient_beds_utilization_denominator', 'inpatient_beds_utilization_denominator', int),
      Columndef('inpatient_beds_utilization_numerator', 'inpatient_beds_utilization_numerator', int),
      Columndef('on_hand_supply_therapeutic_a_casirivimab_imdevimab_courses',
       'on_hand_supply_therapeutic_a_casirivimab_imdevimab_courses', int),
      Columndef('on_hand_supply_therapeutic_b_bamlanivimab_courses',
       'on_hand_supply_therapeutic_b_bamlanivimab_courses', int),
      Columndef('on_hand_supply_therapeutic_c_bamlanivimab_etesevimab_courses',
       'on_hand_supply_therapeutic_c_bamlanivimab_etesevimab_courses', int),
      Columndef('percent_of_inpatients_with_covid', 'percent_of_inpatients_with_covid', float),
      Columndef('percent_of_inpatients_with_covid_coverage', 'percent_of_inpatients_with_covid_coverage',
       int),
      Columndef('percent_of_inpatients_with_covid_denominator',
       'percent_of_inpatients_with_covid_denominator', int),
      Columndef('percent_of_inpatients_with_covid_numerator', 'percent_of_inpatients_with_covid_numerator',
       int),
      Columndef('previous_day_admission_adult_covid_confirmed',
       'previous_day_admission_adult_covid_confirmed', int),
      Columndef('previous_day_admission_adult_covid_confirmed_18-19',
       'previous_day_admission_adult_covid_confirmed_18_19', int),
      Columndef('previous_day_admission_adult_covid_confirmed_18-19_coverage',
       'previous_day_admission_adult_covid_confirmed_18_19_coverage', int),
      Columndef('previous_day_admission_adult_covid_confirmed_20-29',
       'previous_day_admission_adult_covid_confirmed_20_29', int),
      Columndef('previous_day_admission_adult_covid_confirmed_20-29_coverage',
       'previous_day_admission_adult_covid_confirmed_20_29_coverage', int),
      Columndef('previous_day_admission_adult_covid_confirmed_30-39',
       'previous_day_admission_adult_covid_confirmed_30_39', int),
      Columndef('previous_day_admission_adult_covid_confirmed_30-39_coverage',
       'previous_day_admission_adult_covid_confirmed_30_39_coverage', int),
      Columndef('previous_day_admission_adult_covid_confirmed_40-49',
       'previous_day_admission_adult_covid_confirmed_40_49', int),
      Columndef('previous_day_admission_adult_covid_confirmed_40-49_coverage',
       'previous_day_admission_adult_covid_confirmed_40_49_coverage', int),
      Columndef('previous_day_admission_adult_covid_confirmed_50-59',
       'previous_day_admission_adult_covid_confirmed_50_59', int),
      Columndef('previous_day_admission_adult_covid_confirmed_50-59_coverage',
       'previous_day_admission_adult_covid_confirmed_50_59_coverage', int),
      Columndef('previous_day_admission_adult_covid_confirmed_60-69',
       'previous_day_admission_adult_covid_confirmed_60_69', int),
      Columndef('previous_day_admission_adult_covid_confirmed_60-69_coverage',
       'previous_day_admission_adult_covid_confirmed_60_69_coverage', int),
      Columndef('previous_day_admission_adult_covid_confirmed_70-79',
       'previous_day_admission_adult_covid_confirmed_70_79', int),
      Columndef('previous_day_admission_adult_covid_confirmed_70-79_coverage',
       'previous_day_admission_adult_covid_confirmed_70_79_coverage', int),
      Columndef('previous_day_admission_adult_covid_confirmed_80+',
       'previous_day_admission_adult_covid_confirmed_80plus', int),
      Columndef('previous_day_admission_adult_covid_confirmed_80+_coverage',
       'previous_day_admission_adult_covid_confirmed_80plus_coverage', int),
      Columndef('previous_day_admission_adult_covid_confirmed_coverage',
       'previous_day_admission_adult_covid_confirmed_coverage', int),
      Columndef('previous_day_admission_adult_covid_confirmed_unknown',
       'previous_day_admission_adult_covid_confirmed_unknown', int),
      Columndef('previous_day_admission_adult_covid_confirmed_unknown_coverage',
       'previous_day_admission_adult_covid_confirmed_unknown_coverage', int),
      Columndef('previous_day_admission_adult_covid_suspected',
       'previous_day_admission_adult_covid_suspected', int),
      Columndef('previous_day_admission_adult_covid_suspected_18-19',
       'previous_day_admission_adult_covid_suspected_18_19', int),
      Columndef('previous_day_admission_adult_covid_suspected_18-19_coverage',
       'previous_day_admission_adult_covid_suspected_18_19_coverage', int),
      Columndef('previous_day_admission_adult_covid_suspected_20-29',
       'previous_day_admission_adult_covid_suspected_20_29', int),
      Columndef('previous_day_admission_adult_covid_suspected_20-29_coverage',
       'previous_day_admission_adult_covid_suspected_20_29_coverage', int),
      Columndef('previous_day_admission_adult_covid_suspected_30-39',
       'previous_day_admission_adult_covid_suspected_30_39', int),
      Columndef('previous_day_admission_adult_covid_suspected_30-39_coverage',
       'previous_day_admission_adult_covid_suspected_30_39_coverage', int),
      Columndef('previous_day_admission_adult_covid_suspected_40-49',
       'previous_day_admission_adult_covid_suspected_40_49', int),
      Columndef('previous_day_admission_adult_covid_suspected_40-49_coverage',
       'previous_day_admission_adult_covid_suspected_40_49_coverage', int),
      Columndef('previous_day_admission_adult_covid_suspected_50-59',
       'previous_day_admission_adult_covid_suspected_50_59', int),
      Columndef('previous_day_admission_adult_covid_suspected_50-59_coverage',
       'previous_day_admission_adult_covid_suspected_50_59_coverage', int),
      Columndef('previous_day_admission_adult_covid_suspected_60_69', #this is correct; csv header is irregular
       'previous_day_admission_adult_covid_suspected_60_69', int),
      Columndef('previous_day_admission_adult_covid_suspected_60-69_coverage',
       'previous_day_admission_adult_covid_suspected_60_69_coverage', int),
      Columndef('previous_day_admission_adult_covid_suspected_70-79',
       'previous_day_admission_adult_covid_suspected_70_79', int),
      Columndef('previous_day_admission_adult_covid_suspected_70-79_coverage',
       'previous_day_admission_adult_covid_suspected_70_79_coverage', int),
      Columndef('previous_day_admission_adult_covid_suspected_80',
       'previous_day_admission_adult_covid_suspected_80plus', int),
      Columndef('previous_day_admission_adult_covid_suspected_80+_coverage',
       'previous_day_admission_adult_covid_suspected_80plus_coverage', int),
      Columndef('previous_day_admission_adult_covid_suspected_coverage',
       'previous_day_admission_adult_covid_suspected_coverage', int),
      Columndef('previous_day_admission_adult_covid_suspected_unknown',
       'previous_day_admission_adult_covid_suspected_unknown', int),
      Columndef('previous_day_admission_adult_covid_suspected_unknown_coverage',
       'previous_day_admission_adult_covid_suspected_unknown_coverage', int),
      Columndef('previous_day_admission_influenza_confirmed', 'previous_day_admission_influenza_confirmed',
       int),
      Columndef('previous_day_admission_influenza_confirmed_coverage',
       'previous_day_admission_influenza_confirmed_coverage', int),
      Columndef('previous_day_admission_pediatric_covid_confirmed',
       'previous_day_admission_pediatric_covid_confirmed', int),
      Columndef('previous_day_admission_pediatric_covid_confirmed_coverage',
       'previous_day_admission_pediatric_covid_confirmed_coverage', int),
      Columndef('previous_day_admission_pediatric_covid_suspected',
       'previous_day_admission_pediatric_covid_suspected', int),
      Columndef('previous_day_admission_pediatric_covid_suspected_coverage',
       'previous_day_admission_pediatric_covid_suspected_coverage', int),
      Columndef('previous_day_deaths_covid_and_influenza', 'previous_day_deaths_covid_and_influenza', int),
      Columndef('previous_day_deaths_covid_and_influenza_coverage',
       'previous_day_deaths_covid_and_influenza_coverage', int),
      Columndef('previous_day_deaths_influenza', 'previous_day_deaths_influenza', int),
      Columndef('previous_day_deaths_influenza_coverage', 'previous_day_deaths_influenza_coverage', int),
      Columndef('previous_week_therapeutic_a_casirivimab_imdevimab_courses_used',
       'previous_week_therapeutic_a_casirivimab_imdevimab_courses_used', int),
      Columndef('previous_week_therapeutic_b_bamlanivimab_courses_used',
       'previous_week_therapeutic_b_bamlanivimab_courses_used', int),
      Columndef('previous_week_therapeutic_c_bamlanivimab_etesevimab_courses_used',
       'previous_week_therapeutic_c_bamlanivimab_etesevimab_courses_used', int),
      Columndef('staffed_adult_icu_bed_occupancy', 'staffed_adult_icu_bed_occupancy', int),
      Columndef('staffed_adult_icu_bed_occupancy_coverage', 'staffed_adult_icu_bed_occupancy_coverage', int),
      Columndef('staffed_icu_adult_patients_confirmed_and_suspected_covid',
       'staffed_icu_adult_patients_confirmed_suspected_covid', int),
      Columndef('staffed_icu_adult_patients_confirmed_and_suspected_covid_coverage',
       'staffed_icu_adult_patients_confirmed_suspected_covid_coverage', int),
      Columndef('staffed_icu_adult_patients_confirmed_covid', 'staffed_icu_adult_patients_confirmed_covid',
       int),
      Columndef('staffed_icu_adult_patients_confirmed_covid_coverage',
       'staffed_icu_adult_patients_confirmed_covid_coverage', int),
      Columndef('total_adult_patients_hospitalized_confirmed_and_suspected_covid',
       'total_adult_patients_hosp_confirmed_suspected_covid', int),
      Columndef('total_adult_patients_hospitalized_confirmed_and_suspected_covid_coverage',
       'total_adult_patients_hosp_confirmed_suspected_covid_coverage', int),
      Columndef('total_adult_patients_hospitalized_confirmed_covid',
       'total_adult_patients_hosp_confirmed_covid', int),
      Columndef('total_adult_patients_hospitalized_confirmed_covid_coverage',
       'total_adult_patients_hosp_confirmed_covid_coverage', int),
      Columndef('total_patients_hospitalized_confirmed_influenza',
       'total_patients_hospitalized_confirmed_influenza', int),
      Columndef('total_patients_hospitalized_confirmed_influenza_coverage',
       'total_patients_hospitalized_confirmed_influenza_coverage', int),
      Columndef('total_patients_hospitalized_confirmed_influenza_covid',
       'total_patients_hospitalized_confirmed_influenza_covid', int),
      Columndef('total_patients_hospitalized_confirmed_influenza_covid_coverage',
       'total_patients_hospitalized_confirmed_influenza_covid_coverage', int),
      Columndef('total_pediatric_patients_hospitalized_confirmed_and_suspected_covid',
       'total_pediatric_patients_hosp_confirmed_suspected_covid', int),
      Columndef('total_pediatric_patients_hospitalized_confirmed_and_suspected_covid_coverage',
       'total_pediatric_patients_hosp_confirmed_suspected_covid_coverage', int),
      Columndef('total_pediatric_patients_hospitalized_confirmed_covid',
       'total_pediatric_patients_hosp_confirmed_covid', int),
      Columndef('total_pediatric_patients_hospitalized_confirmed_covid_coverage',
       'total_pediatric_patients_hosp_confirmed_covid_coverage', int),
      Columndef('total_staffed_adult_icu_beds', 'total_staffed_adult_icu_beds', int),
      Columndef('total_staffed_adult_icu_beds_coverage', 'total_staffed_adult_icu_beds_coverage', int),
  ]

  def __init__(self, *args, **kwargs):
    super().__init__(
        *args,
        **kwargs,
        table_name=Database.TABLE_NAME,
        columns_and_types=Database.ORDERED_CSV_COLUMNS,
        key_columns=Database.KEY_COLS,
        additional_fields=[Columndef('D', 'record_type', None)])
