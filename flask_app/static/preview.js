var inputs = document.getElementsByTagName('input');

var speed = 2;
var vx = speed;
var vy = speed;

function create_box() {
	var newbox = document.createElement('div');
	
	newbox.setAttribute('id', 'box');

	newbox.style.height = inputs['box_height'].value + 'px';
	newbox.style.width = inputs['box_width'].value + 'px';
	newbox.style.backgroundColor = inputs['box_background_color'].value;
	newbox.style.backgroundImage = inputs['box_gradient'].value;
	newbox.style.borderWidth = inputs['box_border_width'].value + 'px';
	newbox.style.borderStyle = 'solid';
	newbox.style.borderColor = inputs['box_border_color'].value;
	newbox.style.borderRadius = inputs['box_radius'].value + 'px';
	newbox.style.position = 'absolute';
	newbox.style.top = 200 + 'px';
	newbox.style.left = 710 + 'px';

	document.getElementById('create_ballbox').appendChild(newbox);

	return newbox
}

function randomTop() {
	return Math.floor(Math.random(0) * ((inputs['box_height'].value - inputs['box_border_width'].value) - (inputs['ball_size'].value - inputs['ball_border_width'].value + 50))) + 'px';
}

function randomLeft() {
	return Math.floor(Math.random(0) * ((inputs['box_width'].value - inputs['box_border_width'].value) - (inputs['ball_size'].value - inputs['ball_border_width'].value + 50))) + 'px';
}

function create_ball(num) {
	var amount = [];

	if (num <= 0 || isNaN(num)) {
		num = 1;
	}
	
	for (var i = 0; i < num; i++) {

		var newball = document.createElement('div');
		newball.setAttribute('id', 'ball');

		newball.style.height = inputs['ball_size'].value + 'px';
		newball.style.width = inputs['ball_size'].value + 'px';
		newball.style.backgroundColor = inputs['ball_background_color'].value;
		newball.style.backgroundImage = inputs['ball_gradient'].value;
		newball.style.borderWidth = inputs['ball_border_width'].value + 'px';
		newball.style.borderStyle = 'solid';
		newball.style.borderColor = inputs['ball_border_color'].value;
		newball.style.borderRadius = 50 + 'px';
		newball.style.position = 'absolute';
		newball.style.top = randomTop();
		newball.style.left = randomLeft();
		
		document.getElementById('box').appendChild(newball);
		amount.push([newball, vx, vy, speed]);
	}

	console.log(amount);

	return amount
}

function not_a_number(number) {
	if (isNaN(number)) {
		number = 0;
	}

	return number
}

function moveBall() {
	var box_height = parseInt(new_box.style.height);
	var box_width = parseInt(new_box.style.width);
	var box_border_width = parseInt(new_box.style.borderWidth);
	
	box_height = not_a_number(box_height);
	box_width = not_a_number(box_width);
	box_border_width = not_a_number(box_border_width);


	for (var i = 0; i < new_ball.length; i++) {
		var ball_size = parseInt(new_ball[i][0].style.height);
		var ball_border_width = parseInt(new_ball[i][0].style.borderWidth);
		var ball_left = parseInt(new_ball[i][0].style.left);
		var ball_top = parseInt(new_ball[i][0].style.top);

		ball_size = not_a_number(ball_size);
		ball_border_width = not_a_number(ball_border_width);

		ball_left += new_ball[i][1];
		ball_top += new_ball[i][2];
		
		new_ball[i][0].style.top = ball_top + 'px';
		new_ball[i][0].style.left = ball_left + 'px';
		
		
		if (ball_left > (box_width - ball_border_width - box_border_width) - ball_size) {
			new_ball[i][1] = -new_ball[i][1];
		}

		if (ball_left < 0) {
			new_ball[i][1] = new_ball[i][3];
		}

		if (ball_top > (box_height - ball_border_width - box_border_width) - ball_size) {
			new_ball[i][2] = -new_ball[i][2];
		}

		if (ball_top < 0) {
			new_ball[i][2] = new_ball[i][3];
		}
	}

	requestAnimationFrame(moveBall);
}

var buttonClicked = false;
function preview() {
	var box = document.getElementById('box');
	var ball = document.getElementById('ball');

    if (buttonClicked == true) {
        box.remove();
        ball.remove();
        buttonClicked = false;
        new_box = create_box();
		new_ball = create_ball(inputs['ball_amount'].value);
		buttonClicked = true;
    } else {
        buttonClicked = true;
		new_box = create_box();
		new_ball = create_ball(inputs['ball_amount'].value);
		moveBall();
    }
}