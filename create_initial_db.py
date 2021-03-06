"""Functionality for standing up the inital database using historical data.

This module should be run as main once when initializing the app. It builds
the games table in the database using all data from the 2015-16 and 2016-17
seasons as well as every game that has been completed as of the day before
runtime in the 2017-18 season. Because this requires many API pulls this
process will take several hours.
"""
from app import db
from develop import dataPullProcessFunctions as dppf
from app.models import Game
import logging


def build_db():
    """Creates initial database with historical data.

    Builds database with full data from 2015-2016 and 2016-2017 seasons, as
    well as data up through the day of code execution from the 2017-2018
    season.

    Args:
        None

    Returns:
        None
    """
    db.drop_all()
    db.create_all()
    logging.info('Database created.')
    schedule2015 = dppf.schedule('2015-2016-regular', None)
    logging.debug('2015-16 season data retrieved, adding to database.')
    for game in schedule2015.games:
        game_stats = Game(date=game['date'],
                          season=schedule2015.season,
                          opponent=game['opponent'],
                          home_away=game['home/away'],
                          lbj_days_rest=game['days_rest'],
                          lbj_2pt_pct=game['season_2pt_pct'],
                          lbj_3pt_pct=game['season_3pt_pct'],
                          lbj_ft_pct=game['season_ft_pct'],
                          lbj_2pt_mpg=game['season_2ptpg'],
                          lbj_3pt_mpg=game['season_3ptpg'],
                          lbj_ft_mpg=game['season_ftpg'],
                          lbj_rbs_pgm=game['season_rpg'],
                          lbj_ast_pgm=game['season_apg'],
                          lbj_plusminpg=game['season_plusminpg'],
                          opp_def_eff=game['opp_def_eff'],
                          opp_off_eff=game['opp_off_eff'],
                          cavsWins=game['cavsWins'],
                          cavsLosses=game['cavsLosses'],
                          oppWins=game['OPPW'],
                          oppLosses=game['OPPL'],
                          lbj_games_missed=game['gamesMissed'])
        try:
            game_stats.pts = game['lbj_pts']
            game_stats.rbs = game['lbj_rbs']
            game_stats.ast = game['lbj_ast']
            game_stats.lbj_DNP = game['DNP']
        except:
            game_stats.lbj_inactive = True
        db.session.add(game_stats)
        db.session.commit()
    logging.info('2015-16 season data added.')
    schedule2016 = dppf.schedule('2016-2017-regular', None)
    logging.debug('2016-17 season data retrieved, adding to database.')
    for game in schedule2016.games:
        game_stats = Game(date=game['date'],
                          season=schedule2016.season,
                          opponent=game['opponent'],
                          home_away=game['home/away'],
                          lbj_days_rest=game['days_rest'],
                          lbj_2pt_pct=game['season_2pt_pct'],
                          lbj_3pt_pct=game['season_3pt_pct'],
                          lbj_ft_pct=game['season_ft_pct'],
                          lbj_2pt_mpg=game['season_2ptpg'],
                          lbj_3pt_mpg=game['season_3ptpg'],
                          lbj_ft_mpg=game['season_ftpg'],
                          lbj_rbs_pgm=game['season_rpg'],
                          lbj_ast_pgm=game['season_apg'],
                          lbj_plusminpg=game['season_plusminpg'],
                          opp_def_eff=game['opp_def_eff'],
                          opp_off_eff=game['opp_off_eff'],
                          cavsWins=game['cavsWins'],
                          cavsLosses=game['cavsLosses'],
                          oppWins=game['OPPW'],
                          oppLosses=game['OPPL'],
                          lbj_games_missed=game['gamesMissed'])
        try:
            game_stats.pts = game['lbj_pts']
            game_stats.rbs = game['lbj_rbs']
            game_stats.ast = game['lbj_ast']
            game_stats.lbj_DNP = game['DNP']
        except:
            game_stats.lbj_inactive = True
        db.session.add(game_stats)
        db.session.commit()
    logging.info('2016-17 season data added.')
    schedule2017 = dppf.schedule('2017-2018-regular', 'until-yesterday')
    logging.debug('2017-18 season data through yesterday retrieved, adding to database.')
    for game in schedule2017.games:
        game_stats = Game(date=game['date'],
                          season=schedule2017.season,
                          opponent=game['opponent'],
                          home_away=game['home/away'],
                          lbj_days_rest=game['days_rest'],
                          lbj_2pt_pct=game['season_2pt_pct'],
                          lbj_3pt_pct=game['season_3pt_pct'],
                          lbj_ft_pct=game['season_ft_pct'],
                          lbj_2pt_mpg=game['season_2ptpg'],
                          lbj_3pt_mpg=game['season_3ptpg'],
                          lbj_ft_mpg=game['season_ftpg'],
                          lbj_rbs_pgm=game['season_rpg'],
                          lbj_ast_pgm=game['season_apg'],
                          lbj_plusminpg=game['season_plusminpg'],
                          opp_def_eff=game['opp_def_eff'],
                          opp_off_eff=game['opp_off_eff'],
                          cavsWins=game['cavsWins'],
                          cavsLosses=game['cavsLosses'],
                          oppWins=game['OPPW'],
                          oppLosses=game['OPPL'],
                          lbj_games_missed=game['gamesMissed'])
        try:
            game_stats.pts = game['lbj_pts']
            game_stats.rbs = game['lbj_rbs']
            game_stats.ast = game['lbj_ast']
            game_stats.lbj_DNP = game['DNP']
        except:
            game_stats.lbj_inactive = True
        db.session.add(game_stats)
        db.session.commit()
    logging.info('2017-18 season data added.')
    db.session.close()


if __name__ == "__main__":
    logging.basicConfig(filename="logs/initial_db_creation.log",
                        level=logging.DEBUG)
    build_db()
