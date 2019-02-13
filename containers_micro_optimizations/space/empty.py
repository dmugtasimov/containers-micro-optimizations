from containers_micro_optimizations.utils import Spacemeter


spacemeter = Spacemeter()
spacemeter.measure('tuple', ())
spacemeter.measure('list', [])
spacemeter.measure('dict', {})
spacemeter.measure('set', set())
spacemeter.measure('frozenset', frozenset())

print('\n'.join(spacemeter.table()))
