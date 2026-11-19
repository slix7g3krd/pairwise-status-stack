"""第 63 批：Boss 身上叠了五层灼烧，驱散后还剩两层，玩家死了复活还带着减..."""

def refresh_stack(current, add, cap):
    """层数刷新。"""
    raise NotImplementedError("TODO: refresh_stack")

def tick_once(interval, dt):
    """单次结算。"""
    raise NotImplementedError("TODO: tick_once")

def dispel_count(stacks, priority, amount):
    """驱散优先级。"""
    raise NotImplementedError("TODO: dispel_count")

def dynamic_attr(base, per_stack, stacks):
    """动态属性。"""
    raise NotImplementedError("TODO: dynamic_attr")

def resist_clear(resist, immune):
    """抗性清理。"""
    raise NotImplementedError("TODO: resist_clear")

def death_clear(dead, stacks):
    """死亡清理。"""
    raise NotImplementedError("TODO: death_clear")

def icon_slot(buff_id, size):
    """图标重排。"""
    raise NotImplementedError("TODO: icon_slot")

def remaining_time(total, elapsed):
    """剩余时间。"""
    raise NotImplementedError("TODO: remaining_time")

def tick_compensation(frames, interval):
    """tick 补偿。"""
    raise NotImplementedError("TODO: tick_compensation")

def cap_policy(current, cap, add):
    """上限策略。"""
    raise NotImplementedError("TODO: cap_policy")

def source_filter(source, allowed):
    """来源过滤。"""
    raise NotImplementedError("TODO: source_filter")

def revive_snapshot(buff, invulnerable):
    """复活快照。"""
    raise NotImplementedError("TODO: revive_snapshot")

def concurrency_lock(locked):
    """并发锁。"""
    raise NotImplementedError("TODO: concurrency_lock")

def periodic_damage(stacks, per_stack, ticks):
    """周期伤害。"""
    raise NotImplementedError("TODO: periodic_damage")

def dispel_priority(priority, threshold):
    """驱散阈值。"""
    raise NotImplementedError("TODO: dispel_priority")
