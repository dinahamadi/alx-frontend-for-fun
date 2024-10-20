#include "../inc/maze.h"
int findAvailablePositions(GameState *state, Position *positions, int maxPositions) {
    int availableCount = 0;
    
    // Traverse the map to find walkable spaces (0)
    for (int y = 0; y < MAP_HEIGHT; y++) {
        for (int x = 0; x < MAP_WIDTH; x++) {
            if (state->worldMap[y][x] == 0 && availableCount < maxPositions) {
                positions[availableCount].x = x;
                positions[availableCount].y = y;
                availableCount++;
            }
        }
    }
    
    return availableCount; // Return how many positions were found
}

void shufflePositions(Position *positions, int count)
{
	for (int i = count - 1; i > 0; i--) {
		int j = rand() % (i + 1);
		Position temp = positions[i];
		positions[i] = positions[j];
		positions[j] = temp;
	}
}


void placeEnemies(GameState *state, Position *availablePositions, int availableCount, SDL_Renderer *renderer) {
    if (state->enemyCount > availableCount) {
	    state->enemyCount = availableCount; // Adjust enemy count to available positions
    }

    shufflePositions(availablePositions, availableCount); // Randomize positions

    // Assign enemies to random positions
    for (int i = 0; i < state->enemyCount; i++) {
	    state->enemies[i].posX = availablePositions[i].x + 0.5f; // Slight offset to center enemy
	    state->enemies[i].posY = availablePositions[i].y + 0.5f;
	    state->enemies[i].isAlive = 0;

	    // Load the enemy texture, passing the renderer
	    state->enemies[i].texture = loadEnemyTexture(renderer);
	    if (state->enemies[i].texture == NULL) {
		    fprintf(stderr, "Failed to load texture for enemy %d\n", i + 1);
	    }
    }
}


SDL_Texture* loadEnemyTexture(SDL_Renderer *renderer) {
	SDL_Surface *surface;
	const char *enemyTextureFile = "img/enemy.png"; // Modify if you have different textures

	surface = IMG_Load(enemyTextureFile);
	if (surface == NULL) {
		fprintf(stderr, "Failed to load enemy texture: %s\n", IMG_GetError());
		return (NULL);
	}
	SDL_Texture *enemyTexture = SDL_CreateTextureFromSurface(renderer, surface);
	SDL_FreeSurface(surface);

	if (enemyTexture == NULL) {
		fprintf(stderr, "Failed to create enemy texture from surface: %s\n", SDL_GetError());
	}

	return (enemyTexture);
}

