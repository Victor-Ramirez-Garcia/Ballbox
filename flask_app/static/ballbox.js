var speed = 2;
var vx = speed;
var vy = speed;

var box = {
	height: 220,
	width: 622,
	backgroundColor: 'none',
	backgroundImage: 'none',
	borderWidth: 3,
	borderStyle: 'solid',
	borderColor: 'black',
	borderRadius: 10,
	position: 'absolute',
	top: 20,
	left: 30
}

var ball = {
	height: 40,
	width: 40,
	backgroundColor: 'blue',
	backgroundImage: 'none',
	borderWidth: 3,
	borderStyle: 'solid',
	borderColor: 'black',
	borderRadius: 50,
	position: 'absolute',
}

ball.top = Math.floor(Math.random(0) * ((box.height - box.borderWidth) - (ball.height - ball.borderWidth + ball.borderRadius)));
ball.left = Math.floor(Math.random(0) * ((box.width - box.borderWidth) - (ball.width - ball.borderWidth + ball.borderRadius)));

function create_box(box) {
	var newbox = document.createElement('div');
	
	newbox.style.height = box.height + 'px';
	newbox.style.width = box.width + 'px';
	newbox.style.backgroundColor = box.backgroundColor;
	newbox.style.backgroundImage = box.backgroundImage;
	newbox.style.borderWidth = box.borderWidth + 'px';
	newbox.style.borderStyle = box.borderStyle;
	newbox.style.borderColor = box.borderColor;
	newbox.style.borderRadius = box.borderRadius + 'px';
	newbox.style.position = box.position;
	newbox.style.top = box.top + 'px';
	newbox.style.left = box.left + 'px';

	document.getElementById('login_and_register').appendChild(newbox);

	return newbox
}

function create_ball(newball) {
	var newball = document.createElement('div');

	newball.style.height = ball.height + 'px';
	newball.style.width = ball.width + 'px';
	newball.style.backgroundColor = ball.backgroundColor;
	newball.style.backgroundImage = ball.backgroundImage;
	newball.style.borderWidth = ball.borderWidth + 'px';
	newball.style.borderStyle = ball.borderStyle;
	newball.style.borderColor = ball.borderColor;
	newball.style.borderRadius = ball.borderRadius + 'px';
	newball.style.position = ball.position;
	newball.style.top = ball.top + 'px';
	newball.style.left = ball.left + 'px';

	box1.appendChild(newball);

	return newball
}

box1 = create_box(box);

ball1 = create_ball(ball);

function moveBall() {
	ball.left += vx;
	ball.top += vy;
	ball1.style.left = ball.left + 'px';
	ball1.style.top = ball.top + 'px';
	
	if (ball.left > (box.width - ball.borderWidth) - ball.width) {
		vx = -vx;
	}

	if (ball.left < 0) {
		vx = speed;
	}

	if (ball.top > (box.height - ball.borderWidth) - ball.height) {
		vy = -vy;
	}

	if (ball.top < 0) {
		vy = speed;
	}
	
	requestAnimationFrame(moveBall);
}

moveBall();