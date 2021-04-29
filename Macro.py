(function() {
	'use strict';

	var canvas = null;
	var ejectorLoop = null;
	var keysHold = {};
	var topPlayers = [];
	var copiedName = '';

	$(document).ready(function() {
		canvas = document.getElementById('canvas');
		hookKeys();
		canvasModding();
	});

	function hookKeys() {
		$(document).on('keyup', function(e) {
			var key = e.which || e.keyCode;
			keysHold[key] = false;
			if(key == 87) { // key W
				clearInterval(ejectorLoop);
				ejectorLoop = null;
			}
			else if(key >= 37 && key <= 40 || key >= 73 && key <= 76) handleMovementKeys();
		});

		$(document).on('keydown', function(e) {
			var key = e.which || e.keyCode;
			var spKeys = e.ctrlKey || e.altKey || e.shiftKey;
			console.log('DEBUG: keydown ' + key);
			if(!document.getElementById('overlays') && !spKeys) {
				if(!keysHold[key]) {
					if(key == 87) { // key W
						if(!ejectorLoop) {
							ejectorLoop = setInterval(function() {
								window.onkeydown({ keyCode: 87 });
								window.onkeyup({ keyCode: 87 });
							}, 10);
						}
					}
					else if(key == 82) { // key R
						setIntervalX(function() {
							window.onkeydown({ keyCode: 87 }); // key W
							window.onkeyup({ keyCode: 87 });
						}, 120, 7);
					}
					else if(key == 84) { // key T
						setIntervalX(function() {
							window.onkeydown({ keyCode: 32 });  // key SPACE
							window.onkeyup({ keyCode: 32 });
						}, 60, 4);
					}
					else if(key == 83) { // key S
						var mEv = new MouseEvent('mousemove', { 'clientX': window.innerWidth / 2, 'clientY': window.innerHeight / 2 });
						canvas.dispatchEvent(mEv);
					}
				}
				keysHold[key] = true;
				if(key >= 37 && key <= 40 || key >= 73 && key <= 76) handleMovementKeys();
			}
			if(key >= 48 && key <= 57 && !spKeys && document.activeElement.tagName.toUpperCase() != 'INPUT') { // keys 0-9
				var playerPos = key == 48 ? 9 : key - 49;
				if(topPlayers[playerPos] !== undefined) {
					var newName = topPlayers[playerPos];
					//$('#nick').val(newName).change();
					window.prompt("Press CTRL+C to copy", newName);
				}
			}
		});
	}

	function handleMovementKeys() {
		var left = keysHold[37] || keysHold[74], up = keysHold[38] || keysHold[73], right = keysHold[39] || keysHold[76], down = keysHold[40] || keysHold[75];
		var point = [ window.innerWidth / 2, window.innerHeight / 2 ];
		if(left) point[0] -= 1000;
		if(up) point[1] -= 1000;
		if(right) point[0] += 1000;
		if(down) point[1] += 1000;
		canvas.dispatchEvent(new MouseEvent('mousemove', { 'clientX': point[0], 'clientY': point[1] }));
	}

	function setIntervalX(callback, delay, repetitions) {
		var x = 0;
		var intervalID = window.setInterval(function () {
			callback();
			if(++x === repetitions) window.clearInterval(intervalID);
		}, delay);
	}

	

})();
