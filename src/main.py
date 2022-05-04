from dependencies import *
from settings import *
from bird import *
from pipe import *
from base import *
	
def main(genomes, config):
	global GEN
	GEN += 1
	nets = []
	ge = []
	birds = []

	for _, g in genomes:
		net = neat.nn.FeedForwardNetwork.create(g, config)
		nets.append(net)
		birds.append(Bird(230,350))
		g.fitness = 0
		ge.append(g)

	base = Base(730)
	pipes = [Pipe(550)]
	win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
	clock = pygame.time.Clock()
	score = 0

	isRunning = True
	while isRunning:
		clock.tick(30)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				isRunning = False
				pygame.quit()
				quit()
		
		pipe_ind = 0
		if len(birds) > 0:
			if len(pipes) > 1 and birds[0].x > pipes[0].x + pipes[0].PIPE_TOP.get_width():
				pipe_ind = 1
		else:
			run = False
			break

		for x, bird in enumerate(birds):
			bird.move()
			ge[x].fitness += 0.01
			output = nets[birds.index(bird)].activate((bird.y, abs(bird.y - pipes[pipe_ind].height), abs(bird.y - pipes[pipe_ind].bottom)))
			if output[0] > 0.5:
				bird.jump()

		add_pipe = False
		remove = []
		for pipe in pipes:
			for x, bird  in enumerate(birds):
				if pipe.collide(bird):
					ge[x].fitness -= 0.05
					birds.pop(x)
					nets.pop(x)
					ge.pop(x)

				if not pipe.passed and pipe.x < bird.x:
					pipe.passed = True
					add_pipe = True

			if pipe.x + pipe.PIPE_TOP.get_width() < 0:
				remove.append(pipe)

			pipe.move()

		if add_pipe:
			score += 1
			for g in ge:
				g.fitness += 0.01
			pipes.append(Pipe(550))

		for r in remove:
			pipes.remove(r)

		for x, bird in enumerate(birds):
			if bird.y + bird.img.get_height() > 730 or bird.y < 0:
				birds.pop(x)
				nets.pop(x)
				ge.pop(x)

		base.move()
		draw_window(win, birds, pipes, base, score, GEN)

def run(config_path):
	config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
				  neat.DefaultSpeciesSet, neat.DefaultStagnation,
				  config_path)

	p = neat.Population(config)

	p.add_reporter(neat.StdOutReporter(True))
	stats = neat.StatisticsReporter()
	p.add_reporter(stats)

	winner = p.run(main,50)

if __name__ == "__main__":
	local_dir = os.path.dirname(__file__)
	config_path = os.path.join(local_dir, "config.txt")
	run(config_path)