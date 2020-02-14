from multiprocessing import shared_memory
shm_a = shared_memory.SharedMemory(create=True, size=12)

