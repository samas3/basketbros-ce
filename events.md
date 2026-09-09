"time_quarter", { time: number, quarter: number }

"start_quarter", { quarter: number }

"update", { guy: Guy }

"taunt", { guy: Guy, type: number }

"jump", { guy: Guy }

"punch", { from: Guy, to: Guy, success: boolean }
ret { success: boolean }

"shoot", { guy: Guy, point: number }
ret { point: number }

"point", { guy: Guy, point: number }

"timer", { time: number, quarter: number }

"block", { from: Guy, to: Guy }

"releaseshot", { guy: Guy }

"jump", { guy: Guy }

"endgame", { }
ret { end: boolean }

"sideout", { guy: Guy }

"start_game", { }

"post_game", { winner: Guy }