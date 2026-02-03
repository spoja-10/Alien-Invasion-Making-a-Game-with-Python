# TODO: Finish Alien Invasion Game Project

## Step 1: Update settings.py
- Add alien_speed, fleet_drop_speed, fleet_direction, alien_points, ship_limit, and score initialization.

## Step 2: Update alien.py
- Add self.settings = ai_game.settings in __init__.
- Add update() method to move aliens horizontally.
- Add check_edges() method to detect if alien is at screen edge.

## Step 3: Update alien_invasion.py
- Add self.score = 0 and self.stats (basic) in __init__.
- Modify _create_fleet to create a full grid of aliens using _create_alien helper.
- Add self._update_aliens() in run_game loop.
- Define _update_aliens() to update aliens, check edges, check collisions with ship, and check bottom.
- Define _check_fleet_edges(), _change_fleet_direction(), _check_aliens_bottom(), _ship_hit().
- Update _update_bullets() to include collision detection with aliens and score increment.
- Add logic to create new fleet when all aliens are destroyed.

## Step 4: Test the game
- Run alien_invasion.py to ensure the game works with moving fleet, collisions, and basic game over.
