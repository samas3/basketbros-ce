// BasketBros CE - Client API Module
// 客户端 API 调用封装，用于与后端服务器通信

const API_BASE_URL = 'https://zcxjames.top:56387';

/**
 * 通用请求函数
 * @param {string} endpoint - API 端点
 * @param {string} method - HTTP 方法 (GET, POST)
 * @param {Object} data - 请求数据
 * @returns {Promise<Object>} 响应数据
 */
async function apiRequest(endpoint, method = 'GET', data = null) {
    const url = `${API_BASE_URL}${endpoint}`;
    
    const options = {
        method: method,
        headers: {
            'Content-Type': 'application/json'
        }
    };
    
    if (data && method === 'POST') {
        options.body = JSON.stringify(data);
    }
    
    try {
        const response = await fetch(url, options);
        const result = await response.json();
        
        if (!response.ok) {
            throw new Error(result.error || `HTTP error! status: ${response.status}`);
        }
        
        return result;
    } catch (error) {
        console.error('API Request Error:', error);
        throw error;
    }
}

/**
 * 🔹 Player Management - 玩家管理
 */

/**
 * 注册新玩家
 * @param {string} name - 玩家名称
 * @returns {Promise<Object>} { message: "添加成功" }
 */
async function registerPlayer(name) {
    return await apiRequest('/new', 'POST', { name });
}

/**
 * 🔹 Match Recording - 比赛记录
 */

/**
 * 记录比赛并更新分数
 * @param {Object} matchData - 比赛数据
 * @param {string} matchData.name1 - 玩家1名称
 * @param {string} matchData.name2 - 玩家2名称
 * @param {string} matchData.char1 - 玩家1角色
 * @param {string} matchData.char2 - 玩家2角色
 * @param {number} matchData.winner - 获胜者 (1 或 2)
 * @returns {Promise<Object>} { message: "对局已记录" }
 */
async function recordMatch(matchData) {
    const { name1, name2, char1, char2, winner } = matchData;
    
    // 验证必要字段
    if (!name1 || !name2 || !char1 || !char2 || !winner) {
        throw new Error('缺少必要字段');
    }
    
    if (winner !== 1 && winner !== 2) {
        throw new Error('winner必须为1或2');
    }
    
    return await apiRequest('/play', 'POST', {
        name1,
        name2,
        char1,
        char2,
        winner
    });
}

/**
 * 🔹 Score & Stats Queries - 分数与统计查询
 */

/**
 * 获取所有玩家分数
 * @returns {Promise<Object>} { "PlayerA": 112, "PlayerB": 94, ... }
 */
async function getScores() {
    return await apiRequest('/scores', 'GET');
}

/**
 * 获取比赛场数
 * @returns {Promise<Object>} { "matches": 123 }
 */
async function getMatches() {
    return await apiRequest('/matches', 'GET');
}

/**
 * 获取角色胜率
 * @returns {Promise<Object>} { "Jar Tougger": 0.6321, "CD Player": 0.4800, ... }
 */
async function getRates() {
    return await apiRequest('/rates', 'GET');
}

/**
 * 🔹 Admin Utilities - 管理工具
 */

/**
 * 手动设置玩家分数
 * @param {string} name - 玩家名称
 * @param {number} score - 分数
 * @returns {Promise<Object>} { message: "修改成功" }
 */
async function setScore(name, score) {
    if (!name || score === undefined) {
        throw new Error('缺少name或score');
    }
    
    return await apiRequest('/set', 'POST', { name, score });
}

// 封装为全局对象
const BasketBrosAPI = {
    apiRequest,
    registerPlayer,
    recordMatch,
    getScores,
    getRates,
    setScore,
    getMatches
};
