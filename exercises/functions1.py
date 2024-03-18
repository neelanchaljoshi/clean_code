from datetime import datetime, timedelta


class FunctionExample1:
    """
    ## Original function that we have seen in the slides
    """

    def update_time(self, new_time: datetime) -> list:
        self.current_time = new_time
        return self

    def dir_path(self, start: datetime) -> str:
        # Dummy Function for demonstration purposes
        return start.strftime('%Y_%M_%D_%H')

    def data_paths(self, start: datetime, stop: datetime = None) -> list:
        paths = [self.dir_path(start)]
        if stop is not None:
            one_hour = timedelta(hours=1)
            interim = start + one_hour
            while interim.hour <= stop.hour or interim.day < stop.day:
                paths.append(self.dir_path(interim))
                interim += one_hour
        return paths
    
    # My Solution
    def get_data_path_list(self, start_time: datetime, stop_time: datetime = None) -> list:
        path_list = [self.dir_path(start_time)]
        self.update_time(start_time)
        if start_time == stop_time:
            return path_list
        while self.time <= stop_time:
            path_list.append(self.dir_path(self.current_time))
            self.update_time(self.current_time + timedelta(hours=1))
        return path_list
