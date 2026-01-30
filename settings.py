class Settings:
    """A class to store all settings for alien Invasion"""

    def __init__(self):
        """Initialise the game's settings."""
        # Screen Settings 
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship Settings
        self.ship_speed = 1.5

        # Bullet Settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien Settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1  # 1 represents right; -1 represents left

        # Scoring
        self.alien_points = 50
        self.ship_limit = 3



        
