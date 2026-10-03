import requests
import json

# API 配置
BASE_URL = "https://zcxjames.top:56387"

def register_player(name):
    """注册新玩家"""
    url = f"{BASE_URL}/new"
    data = {"name": name}
    try:
        response = requests.post(url, json=data)
        result = response.json()
        if response.status_code == 200:
            print(f"✓ 玩家 '{name}' 注册成功")
            return True
        else:
            print(f"✗ 注册失败: {result.get('error', '未知错误')}")
            return False
    except Exception as e:
        print(f"✗ 请求失败: {str(e)}")
        return False

def record_match(name1, name2, char1, char2, winner):
    """记录比赛"""
    url = f"{BASE_URL}/play"
    data = {
        "name1": name1,
        "name2": name2,
        "char1": char1,
        "char2": char2,
        "winner": winner
    }
    try:
        response = requests.post(url, json=data)
        result = response.json()
        if response.status_code == 200:
            print(f"✓ 比赛记录成功")
            return True
        else:
            print(f"✗ 记录失败: {result.get('error', '未知错误')}")
            return False
    except Exception as e:
        print(f"✗ 请求失败: {str(e)}")
        return False

def main():
    print("=" * 50)
    print("BasketBros CE - 比赛数据导入工具")
    print("=" * 50)
    print()
    
    match_count = 0
    
    while True:
        print(f"\n--- 第 {match_count + 1} 场比赛 ---")
        
        # 获取输入
        name1 = input("请输入玩家1姓名 (输入 'q' 退出): ").strip()
        if name1.lower() == 'q':
            break
        
        name2 = input("请输入玩家2姓名: ").strip()
        if not name2:
            print("✗ 玩家2姓名不能为空")
            continue
        
        char1 = input("请输入玩家1使用的角色: ").strip()
        if not char1:
            print("✗ 角色1不能为空")
            continue
        
        char2 = input("请输入玩家2使用的角色: ").strip()
        if not char2:
            print("✗ 角色2不能为空")
            continue
        
        # 获取获胜者
        while True:
            winner_input = input("请输入获胜者 (1=玩家1, 2=玩家2): ").strip()
            if winner_input in ['1', '2']:
                winner = int(winner_input)
                break
            else:
                print("✗ 请输入 1 或 2")
        
        # 确认信息
        winner_name = name1 if winner == 1 else name2
        print(f"\n确认信息:")
        print(f"  玩家1: {name1} (角色: {char1})")
        print(f"  玩家2: {name2} (角色: {char2})")
        print(f"  获胜者: {winner_name}")
        
        confirm = input("\n确认上传? (y/n): ").strip().lower()
        if confirm != 'y':
            print("已取消上传")
            continue
        
        # 尝试注册玩家（如果不存在）
        register_player(name1)
        register_player(name2)
        
        # 上传比赛数据
        if record_match(name1, name2, char1, char2, winner):
            match_count += 1
            print(f"✓ 已成功上传 {match_count} 场比赛")
        
        print("-" * 50)
    
    print(f"\n{'=' * 50}")
    print(f"导入完成！共上传 {match_count} 场比赛")
    print(f"{'=' * 50}")

if __name__ == "__main__":
    main()
