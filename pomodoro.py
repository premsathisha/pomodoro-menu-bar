import rumps

class PomodoroTimerApp(rumps.App):
    def __init__(self):

        self.default_work = 25 * 60
        self.break_duration = 5 * 60
        self.work_duration = self.default_work
        self.remaining = self.work_duration

        self.is_running = False
        self.is_break = False
        self.timer_thread = None

        self.menu = [
            rumps.MenuItem("Start", callback=self.start_timer),
            rumps.MenuItem("Pause", callback=self.pause_timer),
            rumps.MenuItem("Reset", callback=self.reset_timer),
            rumps.MenuItem("Set Timer", callback=None, dimensions=(160, 30)),
            None,
            rumps.MenuItem("Status: Ready", callback=None)
        ]
