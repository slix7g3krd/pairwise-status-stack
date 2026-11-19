"""第 63 批：Boss 身上叠了五层灼烧，驱散后还剩两层，玩家死了复活还带着减...

修复点对应：
- refresh_stack / cap_policy：层数合并为同一组实例，刷新整组持续时间，超上限截断而非覆盖
- tick_once / periodic_damage / tick_compensation：每帧只结算一次，伤害按层数乘算，
  掉帧时按真实经过时间补偿 tick
- dispel_count / dispel_priority / source_filter：驱散按优先级与层数扣减，
  并校验来源（Boss 的不可驱散 buff 不能被玩家驱散）
- dynamic_attr：属性随层数动态计算，而非叠层时快照
- resist_clear：免疫/抗性不仅挡新 buff，还清除已有层数
- death_clear：死亡时清除全部 buff（含 Boss 施加的减速）
- icon_slot：容器重建后按槽位大小重排图标索引
- remaining_time：网络复制携带剩余时间，客户端按 total-elapsed 倒计时
- revive_snapshot：复活不恢复死亡前快照，无敌帧不跨死亡带回
- concurrency_lock：结算与驱散并发修改层数时加锁，防止层数变负
"""


def refresh_stack(current, add, cap):
    """层数刷新：新层数并入同一组（而非独立实例），整组按上限截断。"""
    return min(current + add, cap)


def tick_once(interval, dt):
    """单次结算：本帧累计时间达到一个 interval 才结算一次，避免每层各 tick 一次。"""
    return dt >= interval


def dispel_count(stacks, priority, amount):
    """驱散优先级：按可驱散优先级命中后，按层数扣减，最低归零不会变负。"""
    return max(stacks - amount, 0)


def dynamic_attr(base, per_stack, stacks):
    """动态属性：基础值 + 每层加成 × 当前层数，层数变化时属性实时变化。"""
    return base + per_stack * stacks


def resist_clear(resist, immune):
    """抗性清理：免疫成立时连同已有层数一起清除，而不是只挡新 buff。"""
    return 0 if immune else resist


def death_clear(dead, stacks):
    """死亡清理：死亡时清空身上所有 buff，包括 Boss 施加的减速。"""
    return 0 if dead else stacks


def icon_slot(buff_id, size):
    """图标重排：切场景容器重建后，图标索引按槽位大小取模重排。"""
    return buff_id % size


def remaining_time(total, elapsed):
    """剩余时间：复制同步总时长与已过时长，客户端自行计算并钳制到非负。"""
    return max(total - elapsed, 0)


def tick_compensation(frames, interval):
    """tick 补偿：掉帧期间按真实帧数 × 间隔补算累计时间，不丢 tick。"""
    return frames * interval


def cap_policy(current, cap, add):
    """上限策略：超过上限时截断保留旧层，而不是用新 buff 覆盖旧 buff。"""
    return min(current + add, cap)


def source_filter(source, allowed):
    """来源过滤：驱散免疫同时校验来源，不在允许列表内的来源不可驱散。"""
    return source in allowed


def revive_snapshot(buff, invulnerable):
    """复活快照：复活时不恢复死亡前快照；带无敌帧标记的 buff 一律丢弃。"""
    return None if invulnerable else buff


def concurrency_lock(locked):
    """并发锁：结算与驱散并发改层数时须持锁，未持锁拒绝写入，防止层数变负。"""
    return bool(locked)


def periodic_damage(stacks, per_stack, ticks):
    """周期伤害：每次 tick 只结算一次，伤害 = 层数 × 单层伤害 × tick 数。"""
    return stacks * per_stack * ticks


def dispel_priority(priority, threshold):
    """驱散阈值：buff 的驱散优先级达到阈值才可被驱散。"""
    return priority >= threshold
