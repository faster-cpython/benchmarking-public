
# Results vs. base

- fork: faster-cpython
- ref: incremental_gc
- machine: linux-x86_64
- commit hash: 58901ff
- commit date: 2023-08-12
- overall geometric mean: 1.04x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-58901ff |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 2.65 sec                                                              | 2.39 sec: 1.11x faster                                                    |
| tornado_http   | 95.7 ms                                                               | 93.5 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-58901ff |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 79.2 ms                                                               | 71.9 ms: 1.10x faster                                                     |
| pidigits       | 201 ms                                                                | 189 ms: 1.06x faster                                                      |
| nbody          | 92.4 ms                                                               | 89.8 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-58901ff |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.54 ms                                                               | 3.46 ms: 1.02x faster                                                     |
| regex_compile  | 137 ms                                                                | 136 ms: 1.01x faster                                                      |
| regex_dna      | 208 ms                                                                | 210 ms: 1.01x slower                                                      |
| regex_v8       | 21.9 ms                                                               | 22.7 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-58901ff |
|---------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_iterparse | 103 ms                                                                | 93.8 ms: 1.10x faster                                                     |
| xml_etree_parse     | 152 ms                                                                | 141 ms: 1.08x faster                                                      |
| xml_etree_process   | 58.1 ms                                                               | 56.4 ms: 1.03x faster                                                     |
| xml_etree_generate  | 83.4 ms                                                               | 80.9 ms: 1.03x faster                                                     |
| pickle              | 10.7 us                                                               | 10.4 us: 1.03x faster                                                     |
| pickle_dict         | 31.7 us                                                               | 30.9 us: 1.03x faster                                                     |
| pickle_pure_python  | 299 us                                                                | 294 us: 1.02x faster                                                      |
| json_dumps          | 9.71 ms                                                               | 9.75 ms: 1.00x slower                                                     |
| unpickle_list       | 4.94 us                                                               | 5.08 us: 1.03x slower                                                     |
| Geometric mean      | (ref)                                                                 | 1.02x faster                                                              |

Benchmark hidden because not significant (5): tomli_loads, json_loads, unpickle_pure_python, pickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-58901ff |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 9.33 ms                                                               | 9.28 ms: 1.01x faster                                                     |
| python_startup_no_site | 6.83 ms                                                               | 6.81 ms: 1.00x faster                                                     |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-58901ff |
|-----------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 11.0 ms                                                               | 10.8 ms: 1.02x faster                                                     |

All benchmarks:
===============

| Benchmark               | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-58901ff |
|-------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io           | 1.19 sec                                                              | 561 ms: 2.13x faster                                                      |
| async_tree_none         | 478 ms                                                                | 276 ms: 1.73x faster                                                      |
| async_tree_memoization  | 586 ms                                                                | 342 ms: 1.71x faster                                                      |
| async_tree_cpu_io_mixed | 720 ms                                                                | 503 ms: 1.43x faster                                                      |
| gc_traversal            | 4.29 ms                                                               | 3.78 ms: 1.13x faster                                                     |
| docutils                | 2.65 sec                                                              | 2.39 sec: 1.11x faster                                                    |
| float                   | 79.2 ms                                                               | 71.9 ms: 1.10x faster                                                     |
| xml_etree_iterparse     | 103 ms                                                                | 93.8 ms: 1.10x faster                                                     |
| xml_etree_parse         | 152 ms                                                                | 141 ms: 1.08x faster                                                      |
| pidigits                | 201 ms                                                                | 189 ms: 1.06x faster                                                      |
| dask                    | 520 ms                                                                | 489 ms: 1.06x faster                                                      |
| pycparser               | 1.15 sec                                                              | 1.09 sec: 1.06x faster                                                    |
| logging_silent          | 106 ns                                                                | 101 ns: 1.05x faster                                                      |
| async_generators        | 447 ms                                                                | 426 ms: 1.05x faster                                                      |
| create_gc_cycles        | 1.49 ms                                                               | 1.43 ms: 1.04x faster                                                     |
| xml_etree_process       | 58.1 ms                                                               | 56.4 ms: 1.03x faster                                                     |
| xml_etree_generate      | 83.4 ms                                                               | 80.9 ms: 1.03x faster                                                     |
| pickle                  | 10.7 us                                                               | 10.4 us: 1.03x faster                                                     |
| nbody                   | 92.4 ms                                                               | 89.8 ms: 1.03x faster                                                     |
| pickle_dict             | 31.7 us                                                               | 30.9 us: 1.03x faster                                                     |
| deltablue               | 3.20 ms                                                               | 3.12 ms: 1.03x faster                                                     |
| tornado_http            | 95.7 ms                                                               | 93.5 ms: 1.02x faster                                                     |
| coverage                | 95.0 ms                                                               | 92.8 ms: 1.02x faster                                                     |
| regex_effbot            | 3.54 ms                                                               | 3.46 ms: 1.02x faster                                                     |
| deepcopy_memo           | 38.4 us                                                               | 37.7 us: 1.02x faster                                                     |
| pickle_pure_python      | 299 us                                                                | 294 us: 1.02x faster                                                      |
| hexiom                  | 6.02 ms                                                               | 5.93 ms: 1.02x faster                                                     |
| mako                    | 11.0 ms                                                               | 10.8 ms: 1.02x faster                                                     |
| comprehensions          | 20.4 us                                                               | 20.1 us: 1.01x faster                                                     |
| scimark_monte_carlo     | 68.0 ms                                                               | 67.1 ms: 1.01x faster                                                     |
| nqueens                 | 80.8 ms                                                               | 79.9 ms: 1.01x faster                                                     |
| sqlglot_parse           | 1.29 ms                                                               | 1.28 ms: 1.01x faster                                                     |
| sqlglot_normalize       | 105 ms                                                                | 104 ms: 1.01x faster                                                      |
| crypto_pyaes            | 70.0 ms                                                               | 69.4 ms: 1.01x faster                                                     |
| richards_super          | 54.2 ms                                                               | 53.8 ms: 1.01x faster                                                     |
| dulwich_log             | 66.4 ms                                                               | 65.9 ms: 1.01x faster                                                     |
| sqlglot_transpile       | 1.61 ms                                                               | 1.59 ms: 1.01x faster                                                     |
| python_startup          | 9.33 ms                                                               | 9.28 ms: 1.01x faster                                                     |
| regex_compile           | 137 ms                                                                | 136 ms: 1.01x faster                                                      |
| asyncio_tcp_ssl         | 1.79 sec                                                              | 1.78 sec: 1.00x faster                                                    |
| fannkuch                | 394 ms                                                                | 392 ms: 1.00x faster                                                      |
| sqlglot_optimize        | 52.8 ms                                                               | 52.6 ms: 1.00x faster                                                     |
| python_startup_no_site  | 6.83 ms                                                               | 6.81 ms: 1.00x faster                                                     |
| asyncio_tcp             | 483 ms                                                                | 485 ms: 1.00x slower                                                      |
| json_dumps              | 9.71 ms                                                               | 9.75 ms: 1.00x slower                                                     |
| go                      | 137 ms                                                                | 138 ms: 1.00x slower                                                      |
| mypy2                   | 337 ms                                                                | 338 ms: 1.00x slower                                                      |
| raytrace                | 266 ms                                                                | 267 ms: 1.01x slower                                                      |
| pprint_pformat          | 1.46 sec                                                              | 1.47 sec: 1.01x slower                                                    |
| pathlib                 | 18.5 ms                                                               | 18.7 ms: 1.01x slower                                                     |
| richards                | 47.8 ms                                                               | 48.2 ms: 1.01x slower                                                     |
| generators              | 27.8 ms                                                               | 28.1 ms: 1.01x slower                                                     |
| meteor_contest          | 106 ms                                                                | 107 ms: 1.01x slower                                                      |
| spectral_norm           | 107 ms                                                                | 108 ms: 1.01x slower                                                      |
| regex_dna               | 208 ms                                                                | 210 ms: 1.01x slower                                                      |
| telco                   | 7.80 ms                                                               | 7.92 ms: 1.02x slower                                                     |
| unpickle_list           | 4.94 us                                                               | 5.08 us: 1.03x slower                                                     |
| coroutines              | 21.6 ms                                                               | 22.3 ms: 1.03x slower                                                     |
| scimark_sparse_mat_mult | 4.57 ms                                                               | 4.74 ms: 1.04x slower                                                     |
| regex_v8                | 21.9 ms                                                               | 22.7 ms: 1.04x slower                                                     |
| unpack_sequence         | 42.2 ns                                                               | 46.2 ns: 1.10x slower                                                     |
| Geometric mean          | (ref)                                                                 | 1.04x faster                                                              |

Benchmark hidden because not significant (21): scimark_sor, json, tomli_loads, scimark_fft, json_loads, deepcopy, logging_format, pprint_safe_repr, scimark_lu, unpickle_pure_python, bench_mp_pool, bench_thread_pool, pickle_list, mdp, pyflate, chaos, logging_simple, typing_runtime_protocols, deepcopy_reduce, sqlite_synth, unpickle


# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
