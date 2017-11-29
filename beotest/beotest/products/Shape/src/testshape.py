'''
Created on Oct 6, 2017

@author: bharati
'''
import time
from BTE.src.CommonTestClasses import BeoTestClass
import Common.src.Constants as comm_const


class Firsttimesetup(BeoTestClass):
  """
    This is class for testing the first time setup flow for BeoSound Shape.
    Testing the FTS flow for setup one amplifier and two speakers with the design ID => TYW5FUS8LT63
  """

  def verify_soundwall_configured(self, state="complete"):
    """
    Verify that BeoSound shape FTS is completed or not
    Arguments:
    state: Complete (As we are checking the BeoSoundshape has configured so the state should be complete.)

    """
    status = self.tal_http.send_http_command_get(comm_const.BEOZONE_SHAPE_STATUS)
    self.assertEqual(status["soundwallStatus"], state, "The soundwall is not configured it is with status %s" % (status["soundwallStatus"]))

  def verify_total_nodes(self, nodes=1):
    """
    Verifies the total number of nodes.
    1)Get the number of nodes configured
    2)Verify with required number of nodes
    Arguments:
    nodes: required number of nodes(As we have installed one Amplifier so required nodes is nodes=1)
    """
    total_nodes = self.tal_http.send_http_command_get(comm_const.BEOZONE_SHAPE_TOTALNODES)
    self.assertEqual(total_nodes["soundwallNumberOfNodes"], nodes, "The Soundwall has total nodes as %s" % (total_nodes["soundwallNumberOfNodes"]))

  def verify_testtone_for_all_speakers(self):
    """
    Verifies the testtone for all speakers.
    As we have installed one amplifier with two speakers .
    """
    node_speaker_values = [(1, 1), (1, 2)]
    for i in node_speaker_values:
      data = {"testTone": {
              "node": i[0],
              "speaker": i[1],
              "sound": "localizationNoise"}}
      self.tal_http.send_http_command_put(comm_const.BEOZONE_SHAPE_TESTONE, data)
      time.sleep(5)

  def get_software_version(self):
    """
    Get a software version
    We only have BNR for getting the software version of the Core .
    """
    version = self.tal_http.get_software_version()
    self.logger.info(version)

  def get_power_state(self):
    """
    Get a power state.
    We only have BNr for getting the power state of the Core.

    """
    state = self.tal_http.get_power_state()
    self.logger.info(state)
    self.assertEqual(state, comm_const.POWER_STATE_ON, "The power state is %s" % state)

  def verify_soundwall_information(self):
    """
    Get the soundwall related information
    It verifies the information about the a2b status is ready and error message is not there.
    """
    info = self.tal_http.send_http_command_get(comm_const.BEOZONE_SHAPE_INFO)
    self.logger.info(info)
    a2b_status = info["soundwallInformation"]["a2bStatus"]
    error_message = info["soundwallInformation"]["errorMessage"]

    self.assertEqual(a2b_status, "ready", "The A2B is not ready it is %s" % a2b_status)
    self.assertEqual(error_message, "", "The error has occured and the error message is %s" % error_message)

  def play_source(self):
    """
    Play the source
    STEPS:
    1) sets the Active source as DEEZER.
    2)plays the source
    3)pause the source.
    """
    self.logger.info("****  play the source*****")
    # self.tal_http.set_active_source(comm_const.SourceJidPrefix.DEEZER)
    self.tal_http.set_active_source(comm_const.SourceJidPrefix.DEEZER)
    time.sleep(4)
    self.tal_http.stream_play()
    time.sleep(15)
    self.tal_http.stream_pause()
    self.logger.info("***Deezer source is playing*****")


  def configure_soundwall_oneAmplifiertile(self):
    """
    Configuring the soundwall for one amplifier tile for intergation server.
    design ID: "TYW5FUS8LT63"
    """
    self.logger.info("**** Configure the soundwall****")
    data = {
    "soundwallConfiguration": "{\r\n  \"id\": \"f63a3cd5211149869a0dedef0770320e\",\r\n  \"name\": \"SoundMode test\",\r\n  \"accountId\": \"410b7da986e14b8eb3eeb0b3a44bb41b\",\r\n  \"created\": \"2017-09-05T11:36:59.17944Z\",\r\n  \"updated\": \"2017-09-05T11:40:54.1836083Z\",\r\n  \"settingsUpdated\": \"0001-01-01T00:00:00\",\r\n  \"countTiles\": 6,\r\n  \"countAmplifierTiles\": 1,\r\n  \"countSpeakerTiles\": 2,\r\n  \"background\": {\r\n    \"isDark\": false\r\n  },\r\n  \"tiles\": [\r\n    {\r\n      \"type\": \"Damper\",\r\n      \"coordinateX\": 0,\r\n      \"coordinateY\": 0,\r\n      \"colorId\": 210,\r\n      \"soundSettings\": {\r\n        \"wooferCalibration\": 0,\r\n        \"twCalibration\": 0,\r\n        \"soundModes\": []\r\n      }\r\n    },\r\n    {\r\n      \"type\": \"Speaker\",\r\n      \"coordinateX\": 0,\r\n      \"coordinateY\": 2,\r\n      \"colorId\": 210,\r\n      \"friendlyName\": \"A.1\",\r\n      \"soundSettings\": {\r\n        \"amplifierTileIndex\": 1,\r\n        \"speakerTileIndex\": 1,\r\n        \"wooferCalibration\": 1,\r\n        \"twCalibration\": 1,\r\n        \"soundModes\": [\r\n          {\r\n            \"name\": \"mode1\",\r\n            \"leftGain\": 1.414213562373095,\r\n            \"rightGain\": 0,\r\n            \"leftDelay\": 0,\r\n            \"rightDelay\": 0,\r\n            \"calibration\": 1\r\n          },\r\n          {\r\n            \"name\": \"mode2\",\r\n            \"leftGain\": 1.414213562373095,\r\n            \"rightGain\": 0,\r\n            \"leftDelay\": 0,\r\n            \"rightDelay\": 0,\r\n            \"calibration\": 1\r\n          }\r\n        ]\r\n      }\r\n    },\r\n    {\r\n      \"type\": \"Core\",\r\n      \"coordinateX\": 1,\r\n      \"coordinateY\": 1,\r\n      \"colorId\": 210,\r\n      \"soundSettings\": {\r\n        \"wooferCalibration\": 0,\r\n        \"twCalibration\": 0,\r\n        \"soundModes\": []\r\n      }\r\n    },\r\n    {\r\n      \"type\": \"Damper\",\r\n      \"coordinateX\": 1,\r\n      \"coordinateY\": 3,\r\n      \"colorId\": 210,\r\n      \"soundSettings\": {\r\n        \"wooferCalibration\": 0,\r\n        \"twCalibration\": 0,\r\n        \"soundModes\": []\r\n      }\r\n    },\r\n    {\r\n      \"type\": \"Amplifier\",\r\n      \"coordinateX\": 2,\r\n      \"coordinateY\": 2,\r\n      \"colorId\": 210,\r\n      \"friendlyName\": \"A\",\r\n      \"soundSettings\": {\r\n        \"amplifierTileIndex\": 1,\r\n        \"wooferCalibration\": 0,\r\n        \"twCalibration\": 0,\r\n        \"soundModes\": []\r\n      }\r\n    },\r\n    {\r\n      \"type\": \"Speaker\",\r\n      \"coordinateX\": 3,\r\n      \"coordinateY\": 3,\r\n      \"colorId\": 210,\r\n      \"friendlyName\": \"A.2\",\r\n      \"soundSettings\": {\r\n        \"amplifierTileIndex\": 1,\r\n        \"speakerTileIndex\": 2,\r\n        \"wooferCalibration\": 1,\r\n        \"twCalibration\": 1,\r\n        \"soundModes\": [\r\n          {\r\n            \"name\": \"mode1\",\r\n            \"leftGain\": 0,\r\n            \"rightGain\": 1.414213562373095,\r\n            \"leftDelay\": 0,\r\n            \"rightDelay\": 0,\r\n            \"calibration\": 1\r\n          },\r\n          {\r\n            \"name\": \"mode2\",\r\n            \"leftGain\": 0,\r\n            \"rightGain\": 1.414213562373095,\r\n            \"leftDelay\": 0,\r\n            \"rightDelay\": 0,\r\n            \"calibration\": 1\r\n          }\r\n        ]\r\n      }\r\n    }\r\n  ],\r\n  \"eqFilter\": {\r\n    \"bassGain\": 1,\r\n    \"roomEqFilter\": [\r\n      0.9968389646552135,\r\n      -1.960200807161509,\r\n      0.9640124246201754,\r\n      -1.9600666123875912,\r\n      0.9609855840493068,\r\n      1.0005706658184732,\r\n      -1.9939432953020313,\r\n      0.9933974269530557,\r\n      -1.9939469164047827,\r\n      0.9939644716687773,\r\n      0.9534676840901293,\r\n      -1.8665970994905425,\r\n      0.9167601985897721,\r\n      -1.9663396546332812,\r\n      0.9701163846082411,\r\n      1.0451635155000303,\r\n      -2.06704779248714,\r\n      1.0221290521945758,\r\n      -1.9622230449897105,\r\n      0.962450872034261,\r\n      1.1300060463239738,\r\n      0.31628376506026473,\r\n      0.23307640778573394,\r\n      0.5082594884033438,\r\n      0.21684646162291327,\r\n      0.8050917230312478,\r\n      -1.2147481048526863,\r\n      0.504722483158733,\r\n      -1.678969748721998,\r\n      0.7720220886889949,\r\n      1,\r\n      0,\r\n      0,\r\n      0,\r\n      0,\r\n      1,\r\n      0,\r\n      0,\r\n      0,\r\n      0,\r\n      1,\r\n      0,\r\n      0,\r\n      0,\r\n      0,\r\n      1,\r\n      0,\r\n      0,\r\n      0,\r\n      0,\r\n      1,\r\n      0,\r\n      0,\r\n      0,\r\n      0,\r\n      1,\r\n      0,\r\n      0,\r\n      0,\r\n      0\r\n    ]\r\n  },\r\n  \"soundModes\": [],\r\n  \"installationInfo\": {\r\n    \"shortCables\": 1,\r\n    \"longCables\": 1,\r\n    \"customCables\": 0,\r\n    \"numberOfConnectionRails\": 8\r\n  },\r\n  \"algorithmInfo\": {\r\n    \"version\": \"24-Aug-2017 11:20:05\"\r\n  },\r\n  \"readOnlyToken\": \"WXTY8WHXPUYEVAZXWS\",\r\n  \"readWriteToken\": \"TYW5FUS8LT63\"\r\n}"
    }
    self.tal_http.send_http_command_put(comm_const.BEOZONE_SHAPE_CONFIG, data)

  def setup_flow(self, numberoftile="onetile"):
    """
    Configures the soundwall
    STEPS:
    1)perform the Factory reset
    2)verifies the state is Init
    3)configure the soundwall using design ID
    4)verify the state is complete after configure the soundwall
    5)verify the testtone on all speakers
    6)verify the soundwall information for not having any Error messages.
    7)play source for some 10 seconds.

    """
    self.logger.info("*****Factory reset of the product*******")
    self.tal_http.send_http_command_put(comm_const.BEODEVICE_FACTORY_RESET, {"factoryReset": {"initiate": True}})

    time.sleep(20)
    self.logger.info("*******Verify the state before configuring*******")
    self.verify_soundwall_configured(state="init")

    self.logger.info("****Configure the soundwall****")
    self.configure_soundwall_oneAmplifiertile()

    self.logger.info("******verify the state after configuring")
    self.verify_soundwall_configured(state="complete")

    self.logger.info("*******verify the testtone for all the connected speakers**********")
    self.verify_testtone_for_all_speakers()
    time.sleep(5)

    self.logger.info("*********verify the soundwall information after configuration.********")
    self.verify_soundwall_information()
    self.play_source()


if __name__ == '__main__':
  from BTE.src.TestRunner import BeoTestRunner
  from BTE.src.CommonTestClasses import BeoTestResult

  test_case_arguments = ""
  result = BeoTestResult()
  target_name = {"ASE_EZ3_SoundWall_lyngby": {}}
  test_id = None
  test_module_name = "Shape.src.testshape"
  test_class_name = "Firsttimesetup"
  test_case_names = {
      # "testsample",
     # "verify_soundwall_configured"
      # "verify_total_nodes"
      # "get_software_version",
      # "get_power_state",
      "verify_testtone_for_all_speakers",
      # "get_soundwall_information",
      # "configure_soundwall_for_oneAmplifier",
      # "play_source",
      # "setup_flow"
  }
  test_case_known_error = None
  test_case_setup = None
  test_case_script = None
  test_case_cleanup = None

  for test_case_name in test_case_names:
    tr = BeoTestRunner(result, target_name, test_id, test_module_name, test_class_name, test_case_name, test_case_arguments,
                     test_case_setup, test_case_script, test_case_cleanup, local_run=False)
    tr.run()
