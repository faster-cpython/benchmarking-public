
# Results vs. base

- fork: faster-cpython
- ref: incremental_gc
- machine: linux-x86_64
- commit hash: a8834d3
- commit date: 2023-08-12
- overall geometric mean: 1.04x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-a8834d3 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 2.65 sec                                                              | 2.37 sec: 1.12x faster                                                    |
| tornado_http   | 95.7 ms                                                               | 94.0 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-a8834d3 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 79.2 ms                                                               | 70.9 ms: 1.12x faster                                                     |
| nbody          | 92.4 ms                                                               | 88.3 ms: 1.05x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.05x faster                                                              |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-a8834d3 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.54 ms                                                               | 3.43 ms: 1.03x faster                                                     |
| regex_dna      | 208 ms                                                                | 204 ms: 1.02x faster                                                      |
| regex_compile  | 137 ms                                                                | 136 ms: 1.01x faster                                                      |
| regex_v8       | 21.9 ms                                                               | 21.7 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-a8834d3 |
|---------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_iterparse | 103 ms                                                                | 94.1 ms: 1.10x faster                                                     |
| xml_etree_parse     | 152 ms                                                                | 139 ms: 1.09x faster                                                      |
| xml_etree_process   | 58.1 ms                                                               | 56.0 ms: 1.04x faster                                                     |
| xml_etree_generate  | 83.4 ms                                                               | 80.5 ms: 1.04x faster                                                     |
| unpickle            | 14.9 us                                                               | 14.7 us: 1.01x faster                                                     |
| pickle_dict         | 31.7 us                                                               | 31.6 us: 1.00x faster                                                     |
| json_dumps          | 9.71 ms                                                               | 9.76 ms: 1.00x slower                                                     |
| tomli_loads         | 2.29 sec                                                              | 2.31 sec: 1.01x slower                                                    |
| pickle              | 10.7 us                                                               | 10.8 us: 1.01x slower                                                     |
| Geometric mean      | (ref)                                                                 | 1.02x faster                                                              |

Benchmark hidden because not significant (5): pickle_pure_python, unpickle_pure_python, pickle_list, json_loads, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-a8834d3 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 9.33 ms                                                               | 9.27 ms: 1.01x faster                                                     |
| python_startup_no_site | 6.83 ms                                                               | 6.80 ms: 1.00x faster                                                     |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-a8834d3 |
|-----------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 11.0 ms                                                               | 10.7 ms: 1.02x faster                                                     |

All benchmarks:
===============

| Benchmark               | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-a8834d3 |
|-------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io           | 1.19 sec                                                              | 565 ms: 2.11x faster                                                      |
| async_tree_none         | 478 ms                                                                | 276 ms: 1.73x faster                                                      |
| async_tree_memoization  | 586 ms                                                                | 343 ms: 1.71x faster                                                      |
| async_tree_cpu_io_mixed | 720 ms                                                                | 505 ms: 1.42x faster                                                      |
| gc_traversal            | 4.29 ms                                                               | 3.68 ms: 1.17x faster                                                     |
| float                   | 79.2 ms                                                               | 70.9 ms: 1.12x faster                                                     |
| docutils                | 2.65 sec                                                              | 2.37 sec: 1.12x faster                                                    |
| xml_etree_iterparse     | 103 ms                                                                | 94.1 ms: 1.10x faster                                                     |
| xml_etree_parse         | 152 ms                                                                | 139 ms: 1.09x faster                                                      |
| dask                    | 520 ms                                                                | 486 ms: 1.07x faster                                                      |
| async_generators        | 447 ms                                                                | 426 ms: 1.05x faster                                                      |
| nbody                   | 92.4 ms                                                               | 88.3 ms: 1.05x faster                                                     |
| create_gc_cycles        | 1.49 ms                                                               | 1.42 ms: 1.04x faster                                                     |
| logging_silent          | 106 ns                                                                | 101 ns: 1.04x faster                                                      |
| xml_etree_process       | 58.1 ms                                                               | 56.0 ms: 1.04x faster                                                     |
| xml_etree_generate      | 83.4 ms                                                               | 80.5 ms: 1.04x faster                                                     |
| regex_effbot            | 3.54 ms                                                               | 3.43 ms: 1.03x faster                                                     |
| deepcopy_memo           | 38.4 us                                                               | 37.4 us: 1.03x faster                                                     |
| pycparser               | 1.15 sec                                                              | 1.12 sec: 1.03x faster                                                    |
| mako                    | 11.0 ms                                                               | 10.7 ms: 1.02x faster                                                     |
| scimark_monte_carlo     | 68.0 ms                                                               | 66.4 ms: 1.02x faster                                                     |
| coverage                | 95.0 ms                                                               | 92.9 ms: 1.02x faster                                                     |
| deltablue               | 3.20 ms                                                               | 3.13 ms: 1.02x faster                                                     |
| deepcopy_reduce         | 3.21 us                                                               | 3.15 us: 1.02x faster                                                     |
| richards_super          | 54.2 ms                                                               | 53.2 ms: 1.02x faster                                                     |
| tornado_http            | 95.7 ms                                                               | 94.0 ms: 1.02x faster                                                     |
| regex_dna               | 208 ms                                                                | 204 ms: 1.02x faster                                                      |
| fannkuch                | 394 ms                                                                | 388 ms: 1.02x faster                                                      |
| unpickle                | 14.9 us                                                               | 14.7 us: 1.01x faster                                                     |
| scimark_sor             | 121 ms                                                                | 119 ms: 1.01x faster                                                      |
| sqlglot_parse           | 1.29 ms                                                               | 1.27 ms: 1.01x faster                                                     |
| dulwich_log             | 66.4 ms                                                               | 65.7 ms: 1.01x faster                                                     |
| richards                | 47.8 ms                                                               | 47.4 ms: 1.01x faster                                                     |
| crypto_pyaes            | 70.0 ms                                                               | 69.3 ms: 1.01x faster                                                     |
| sqlglot_transpile       | 1.61 ms                                                               | 1.59 ms: 1.01x faster                                                     |
| sqlglot_normalize       | 105 ms                                                                | 104 ms: 1.01x faster                                                      |
| pathlib                 | 18.5 ms                                                               | 18.4 ms: 1.01x faster                                                     |
| python_startup          | 9.33 ms                                                               | 9.27 ms: 1.01x faster                                                     |
| regex_compile           | 137 ms                                                                | 136 ms: 1.01x faster                                                      |
| regex_v8                | 21.9 ms                                                               | 21.7 ms: 1.01x faster                                                     |
| sqlglot_optimize        | 52.8 ms                                                               | 52.5 ms: 1.01x faster                                                     |
| python_startup_no_site  | 6.83 ms                                                               | 6.80 ms: 1.00x faster                                                     |
| pickle_dict             | 31.7 us                                                               | 31.6 us: 1.00x faster                                                     |
| chaos                   | 58.9 ms                                                               | 58.7 ms: 1.00x faster                                                     |
| go                      | 137 ms                                                                | 137 ms: 1.00x faster                                                      |
| asyncio_tcp_ssl         | 1.79 sec                                                              | 1.78 sec: 1.00x faster                                                    |
| pprint_pformat          | 1.46 sec                                                              | 1.47 sec: 1.00x slower                                                    |
| mypy2                   | 337 ms                                                                | 338 ms: 1.00x slower                                                      |
| json_dumps              | 9.71 ms                                                               | 9.76 ms: 1.00x slower                                                     |
| raytrace                | 266 ms                                                                | 267 ms: 1.01x slower                                                      |
| asyncio_tcp             | 483 ms                                                                | 486 ms: 1.01x slower                                                      |
| pprint_safe_repr        | 716 ms                                                                | 722 ms: 1.01x slower                                                      |
| tomli_loads             | 2.29 sec                                                              | 2.31 sec: 1.01x slower                                                    |
| pickle                  | 10.7 us                                                               | 10.8 us: 1.01x slower                                                     |
| generators              | 27.8 ms                                                               | 28.2 ms: 1.01x slower                                                     |
| scimark_lu              | 110 ms                                                                | 112 ms: 1.01x slower                                                      |
| pyflate                 | 446 ms                                                                | 453 ms: 1.02x slower                                                      |
| telco                   | 7.80 ms                                                               | 7.94 ms: 1.02x slower                                                     |
| sqlite_synth            | 2.73 us                                                               | 2.80 us: 1.02x slower                                                     |
| coroutines              | 21.6 ms                                                               | 22.2 ms: 1.03x slower                                                     |
| scimark_sparse_mat_mult | 4.57 ms                                                               | 4.79 ms: 1.05x slower                                                     |
| mdp                     | 2.53 sec                                                              | 2.72 sec: 1.07x slower                                                    |
| unpack_sequence         | 42.2 ns                                                               | 46.1 ns: 1.09x slower                                                     |
| Geometric mean          | (ref)                                                                 | 1.04x faster                                                              |

Benchmark hidden because not significant (19): pickle_pure_python, nqueens, logging_format, deepcopy, bench_mp_pool, pidigits, hexiom, spectral_norm, meteor_contest, logging_simple, comprehensions, scimark_fft, typing_runtime_protocols, unpickle_pure_python, bench_thread_pool, pickle_list, json_loads, unpickle_list, json


# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
