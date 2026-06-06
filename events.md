"time_quarter", { time: number, quarter: number }

"start_quarter", { quarter: number }

"update", { guy: Guy }

"taunt", { guy: Guy, type: ? }

"jump", { guy: Guy }

"punch", { from: Guy, to: Guy, success: boolean }
ret { success: boolean }

"shoot", { guy: Guy, critical: boolean, point: number }
ret { point: number, critical: boolean }

"point", { guy: Guy, point: number, critical: boolean }

"timer", { time: number, quarter: number }

"block", { from: Guy, to: Guy }

"releaseshot", { guy: Guy, ball: Ball }

"jump", { guy: Guy }

"endgame", { }
ret { end: boolean }

"sideout", { guy: Guy }

"start_game", { }

"post_game", { winner: Guy }