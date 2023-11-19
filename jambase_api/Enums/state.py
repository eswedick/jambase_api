from enum import Enum


class StateCode(Enum):
    """State code in ISO 3166-2 format. Note 1: Available for the United States, Canada, and Australia only. Note 2: The
    country and numUpcomingEvents nodes are only provided in the Geography lookup endpoints, not as part of
    addressRegion within a Concert, Festival, or Stream."""

    US_AL = "US-AL"
    US_AK = "US-AK"
    US_AZ = "US-AZ"
    US_AR = "US-AR"
    US_CA = "US-CA"
    US_CO = "US-CO"
    US_CT = "US-CT"
    US_DE = "US-DE"
    US_FL = "US-FL"
    US_GA = "US-GA"
    US_HI = "US-HI"
    US_ID = "US-ID"
    US_IL = "US-IL"
    US_IN = "US-IN"
    US_IA = "US-IA"
    US_KS = "US-KS"
    US_KY = "US-KY"
    US_LA = "US-LA"
    US_ME = "US-ME"
    US_MD = "US-MD"
    US_MA = "US-MA"
    US_MI = "US-MI"
    US_MN = "US-MN"
    US_MS = "US-MS"
    US_MO = "US-MO"
    US_MT = "US-MT"
    US_NE = "US-NE"
    US_NV = "US-NV"
    US_NH = "US-NH"
    US_NJ = "US-NJ"
    US_NM = "US-NM"
    US_NY = "US-NY"
    US_NC = "US-NC"
    US_ND = "US-ND"
    US_OH = "US-OH"
    US_OK = "US-OK"
    US_OR = "US-OR"
    US_PA = "US-PA"
    US_RI = "US-RI"
    US_SC = "US-SC"
    US_SD = "US-SD"
    US_TN = "US-TN"
    US_TX = "US-TX"
    US_UT = "US-UT"
    US_VT = "US-VT"
    US_VA = "US-VA"
    US_WA = "US-WA"
    US_WV = "US-WV"
    US_WI = "US-WI"
    US_WY = "US-WY"
    US_DC = "US-DC"
    # US_AS = "US-AS"
    # US_GU = "US-GU"
    # US_MP = "US-MP"
    # US_PR = "US-PR"
    # US_UM = "US-UM"
    # US_VI = "US-VI"
    AU_ACT = "AU-ACT"
    AU_NSW = "AU-NSW"
    AU_NT = "AU-NT"
    AU_QLD = "AU-QLD"
    AU_SA = "AU-SA"
    AU_TAS = "AU-TAS"
    AU_VIC = "AU-VIC"
    AU_WA = "AU-WA"
    CA_AB = "CA-AB"
    CA_BC = "CA-BC"
    CA_MB = "CA-MB"
    CA_NB = "CA-NB"
    CA_NL = "CA-NL"
    CA_NS = "CA-NS"
    CA_NT = "CA-NT"
    CA_NU = "CA-NU"
    CA_ON = "CA-ON"
    CA_PE = "CA-PE"
    CA_QC = "CA-QC"
    CA_SK = "CA-SK"
    CA_YT = "CA-YT"
