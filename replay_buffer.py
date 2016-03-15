from collections import deque
import random


class ReplayBuffer(object):

    def __init__(self, capacity):
        self.memory = deque(maxlen=capacity)

    def append(self, state, action, reward, next_state=None, next_action=None,
               is_state_terminal=False):
        """Append a transition to this replay buffer
        Args:
          state: s_t
          action: a_t
          reward: r_t
          next_state: s_{t+1} (can be None if terminal)
          next_action: a_{t+1} (can be None for off-policy algorithms)
          is_state_terminal (bool)
        """
        self.memory.append(dict(state=state, action=action, reward=reward,
                                next_state=next_state, next_action=next_action,
                                is_state_terminal=is_state_terminal))

    def sample(self, n):
        """Sample n unique samples from this replay buffer
        """
        assert len(self.memory) > 0
        return random.sample(self.memory, n)

    def __len__(self):
        return len(self.memory)
