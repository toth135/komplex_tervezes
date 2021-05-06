import matplotlib.pyplot as plt


class ParkingLot:

    def plot_parking_lot(self):

        # line points for parking lot plotting
        plt_verticals_1 = [[(5, 4), (5, 10)]]
        plt_verticals_2 = [[(8, 4), (8, 10)]]
        plt_verticals_3 = [[(11, 4), (11, 10)]]
        plt_verticals_4 = [[(14, 4), (14, 10)]]
        plt_verticals_5 = [[(17, 4), (17, 10)]]
        plt_verticals_6 = [[(20, 4), (20, 10)]]
        plt_verticals_7 = [[(23, 4), (23, 10)]]

        plt_verticals_8 = [[(5, 17), (5, 23)]]
        plt_verticals_9 = [[(8, 17), (8, 23)]]
        plt_verticals_10 = [[(11, 17), (11, 23)]]
        plt_verticals_11 = [[(14, 17), (14, 23)]]
        plt_verticals_12 = [[(17, 17), (17, 23)]]
        plt_verticals_13 = [[(20, 17), (20, 23)]]
        plt_verticals_14 = [[(23, 17), (23, 23)]]

        plt_horizontals_1 = [[(5, 7), (23, 7)]]
        plt_horizontals_2 = [[(5, 20), (23, 20)]]

        # plot all the lines one by one to avoid connecting the lines by their endpoints
        for p in plt_verticals_1:
            plt.plot([v[0] for v in p], [v[1] for v in p], 'k-')

        for p in plt_verticals_2:
            plt.plot([v[0] for v in p], [v[1] for v in p], 'k-')

        for p in plt_verticals_3:
            plt.plot([v[0] for v in p], [v[1] for v in p], 'k-')

        for p in plt_verticals_4:
            plt.plot([v[0] for v in p], [v[1] for v in p], 'k-')

        for p in plt_verticals_5:
            plt.plot([v[0] for v in p], [v[1] for v in p], 'k-')

        for p in plt_verticals_6:
            plt.plot([v[0] for v in p], [v[1] for v in p], 'k-')

        for p in plt_verticals_7:
            plt.plot([v[0] for v in p], [v[1] for v in p], 'k-')

        for p in plt_verticals_8:
            plt.plot([v[0] for v in p], [v[1] for v in p], 'k-')

        for p in plt_verticals_9:
            plt.plot([v[0] for v in p], [v[1] for v in p], 'k-')

        for p in plt_verticals_10:
            plt.plot([v[0] for v in p], [v[1] for v in p], 'k-')

        for p in plt_verticals_11:
            plt.plot([v[0] for v in p], [v[1] for v in p], 'k-')

        for p in plt_verticals_12:
            plt.plot([v[0] for v in p], [v[1] for v in p], 'k-')

        for p in plt_verticals_13:
            plt.plot([v[0] for v in p], [v[1] for v in p], 'k-')

        for p in plt_verticals_14:
            plt.plot([v[0] for v in p], [v[1] for v in p], 'k-')

        for p in plt_horizontals_1:
            plt.plot([v[0] for v in p], [v[1] for v in p], 'k-')

        for p in plt_horizontals_2:
            plt.plot([v[0] for v in p], [v[1] for v in p], 'k-')
