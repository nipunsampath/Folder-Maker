import os
import logging

logging.basicConfig(filename="log_file.log", level=logging.DEBUG, format="%(asctime)s:%(levelname)s:%(message)s")


class FolderOperations:
    SUCCESS = 100
    OSERROR = 200

    def __init__(self, name, number_of_seasons, number_of_episodes, path):
        self.series_name = name
        self.numberOfEpisodes = number_of_episodes
        self.numberOfSeasons = number_of_seasons
        self.path = path

    def make_episodes(self, path):
        """Creates a new directory for every episode in the season"""
        try:
            for episode in range(1, self.numberOfEpisodes + 1):
                os.mkdir(path + "/{:02d}".format(episode))
        except OSError as e:
            logging.debug(str(e))
            raise OSError

    def make_seasons(self, path):
        """Creates a new directory for every season """
        season_paths = []
        try:
            for season in range(1, self.numberOfSeasons + 1):
                season_path = path + "/Season %2d" % season
                os.mkdir(season_path)
                season_paths.append(season_path)
            return season_paths
        except OSError as e:
            logging.debug(str(e))
            raise OSError

    def make_series(self):
        """Creates a directory for the tv series with a directory for every episode"""
        series_path = self.path + "/" + self.series_name
        try:
            os.mkdir(series_path)
            paths = self.make_seasons(series_path)
            for path in paths:
                self.make_episodes(path)
            return FolderOperations.SUCCESS
        except OSError as e:
            logging.debug(str(e))
            return FolderOperations.OSERROR

    def make_series_without_episode_dir(self):
        """Creates a directory for the tv series with directories for seasons and a subtitle directory per each
        season """
        series_path = self.path + "/" + self.series_name
        try:
            os.mkdir(series_path)
            paths = self.make_seasons(series_path)
            for path in paths:
                self.make_subtitles_directory(path)

            return FolderOperations.SUCCESS
        except OSError as e:
            logging.debug(str(e))
            return FolderOperations.OSERROR

    def make_subtitles_directory(self, path):
        try:
            os.mkdir(path + "/Subtitles")
        except OSError as e:
            logging.debug(str(e))
            raise OSError

    def make_movie_directories(self, movies, need_subs):
        try:
            for movie in movies:
                movie_path = self.path + "/" + movie
                os.mkdir(movie_path)

                if need_subs:
                    self.make_subtitles_directory(movie_path)
            return FolderOperations.SUCCESS
        except OSError as e:
            logging.debug(str(e))
            return FolderOperations.OSERROR


if __name__ == "__main__":
    series_name = "Make Human23"
    number_of_seasons = 2
    number_of_episodes = 20
    folder_path = "D:/Projects/Python/Folder Maker/test"
    movies = ["Avengers", "Doctor who", "Pacific Rim"]

    driver = FolderOperations(None, None, None, folder_path)
    driver.make_movie_directories(movies, True)
