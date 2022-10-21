from brainflow.board_shim import BoardShim, BrainFlowInputParams, LogLevels, BoardIds

import time

class Stream:
    """
    For streaming from biosensing devices.

    Visit https://brainflow.readthedocs.io/en/stable/SupportedBoards.html for more info
    on boardIDs
    """
    def __init__(self, port, boardID=-1):
        BoardShim.enable_dev_board_logger()

        self.port = port

        params = BrainFlowInputParams()
        params.serial_port = self.port
        self.board = BoardShim(board_id=boardID, input_params=params)
    
    def startStream(self, inf=False, streamParams='streaming_board://225.1.1.1:6677', duration=20):
        """
        Starts streaming from a board
        
        :param inf: 
            Boolean to determine if we want to run until exited or for a set amount of time
        
        :param streamParams: 
            parameter to stream data from brainflow, supported vals: "file://%file_name%:w", "file://%file_name%:a", "streaming_board://%multicast_group_ip%:%port%". Range for multicast addresses is from "224.0.0.0" to "239.255.255.255"
        
        :param duration: 
            The amount of time to stream from the board if inf is False

        """
        self.board.prepare_session()
        self.board.start_stream(45000, streamParams)

        if not inf:
            self.stop(delay=duration)

    def startLocal(self, inf=False, duration=20):
        """
        Starts the board locally

        :param inf: Boolean to determine if we want to run until exited or for a set amount of time
        :param duration: The amount of time to stream from the board if inf is False
        """
        self.board.prepare_session()
        self.board.start_stream(45000, None)

        if not inf:
            self.stop(delay=duration)

    def stop(self, delay=0):
        '''
        Stops the stream of EEG data from the board and releases the session
        @param delay: The amount fo seconds to delay  stopping the board by
        '''
        if delay > 0:
            BoardShim.log_message(LogLevels.LEVEL_INFO.value,
                                  'start sleeping in the main thread')
        time.sleep(delay)
        self.board.stop_stream()
        self.board.release_session()