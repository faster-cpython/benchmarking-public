
# Results vs. base

- fork: faster-cpython
- ref: incremental_gc
- machine: linux-x86_64
- commit hash: 4591b30
- commit date: 2023-08-11
- overall geometric mean: 1.03x slower
- HPT reliability: 72.84%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-4591b30 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 2.65 sec                                                              | 2.52 sec: 1.05x faster                                                    |
| tornado_http   | 95.7 ms                                                               | 103 ms: 1.08x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-4591b30 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                                | 189 ms: 1.06x faster                                                      |
| nbody          | 92.4 ms                                                               | 90.0 ms: 1.03x faster                                                     |
| float          | 79.2 ms                                                               | 110 ms: 1.39x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.08x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-4591b30 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.54 ms                                                               | 3.59 ms: 1.02x slower                                                     |
| regex_v8       | 21.9 ms                                                               | 22.3 ms: 1.02x slower                                                     |
| regex_dna      | 208 ms                                                                | 215 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                              |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-4591b30 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 299 us                                                                | 294 us: 1.02x faster                                                      |
| json_loads           | 25.7 us                                                               | 25.3 us: 1.01x faster                                                     |
| pickle_dict          | 31.7 us                                                               | 31.6 us: 1.00x faster                                                     |
| unpickle_pure_python | 212 us                                                                | 213 us: 1.00x slower                                                      |
| json_dumps           | 9.71 ms                                                               | 9.75 ms: 1.00x slower                                                     |
| pickle_list          | 4.51 us                                                               | 4.54 us: 1.01x slower                                                     |
| unpickle             | 14.9 us                                                               | 15.6 us: 1.05x slower                                                     |
| xml_etree_generate   | 83.4 ms                                                               | 93.5 ms: 1.12x slower                                                     |
| xml_etree_parse      | 152 ms                                                                | 570 ms: 3.74x slower                                                      |
| xml_etree_iterparse  | 103 ms                                                                | 516 ms: 5.00x slower                                                      |
| Geometric mean       | (ref)                                                                 | 1.24x slower                                                              |

Benchmark hidden because not significant (4): unpickle_list, pickle, tomli_loads, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-4591b30 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.83 ms                                                               | 6.89 ms: 1.01x slower                                                     |
| python_startup         | 9.33 ms                                                               | 9.47 ms: 1.01x slower                                                     |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-4591b30 |
|-----------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 11.0 ms                                                               | 10.9 ms: 1.01x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-4591b30 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io            | 1.19 sec                                                              | 700 ms: 1.70x faster                                                      |
| async_tree_none          | 478 ms                                                                | 340 ms: 1.41x faster                                                      |
| async_tree_memoization   | 586 ms                                                                | 431 ms: 1.36x faster                                                      |
| async_tree_cpu_io_mixed  | 720 ms                                                                | 586 ms: 1.23x faster                                                      |
| gc_traversal             | 4.29 ms                                                               | 3.68 ms: 1.17x faster                                                     |
| pidigits                 | 201 ms                                                                | 189 ms: 1.06x faster                                                      |
| docutils                 | 2.65 sec                                                              | 2.52 sec: 1.05x faster                                                    |
| create_gc_cycles         | 1.49 ms                                                               | 1.43 ms: 1.04x faster                                                     |
| unpack_sequence          | 42.2 ns                                                               | 40.7 ns: 1.04x faster                                                     |
| pycparser                | 1.15 sec                                                              | 1.11 sec: 1.04x faster                                                    |
| spectral_norm            | 107 ms                                                                | 104 ms: 1.03x faster                                                      |
| richards                 | 47.8 ms                                                               | 46.5 ms: 1.03x faster                                                     |
| logging_silent           | 106 ns                                                                | 103 ns: 1.03x faster                                                      |
| nbody                    | 92.4 ms                                                               | 90.0 ms: 1.03x faster                                                     |
| pickle_pure_python       | 299 us                                                                | 294 us: 1.02x faster                                                      |
| nqueens                  | 80.8 ms                                                               | 79.5 ms: 1.02x faster                                                     |
| pyflate                  | 446 ms                                                                | 438 ms: 1.02x faster                                                      |
| coverage                 | 95.0 ms                                                               | 93.5 ms: 1.02x faster                                                     |
| richards_super           | 54.2 ms                                                               | 53.3 ms: 1.02x faster                                                     |
| crypto_pyaes             | 70.0 ms                                                               | 68.9 ms: 1.02x faster                                                     |
| fannkuch                 | 394 ms                                                                | 388 ms: 1.01x faster                                                      |
| json_loads               | 25.7 us                                                               | 25.3 us: 1.01x faster                                                     |
| mako                     | 11.0 ms                                                               | 10.9 ms: 1.01x faster                                                     |
| pprint_safe_repr         | 716 ms                                                                | 710 ms: 1.01x faster                                                      |
| chaos                    | 58.9 ms                                                               | 58.4 ms: 1.01x faster                                                     |
| deepcopy_reduce          | 3.21 us                                                               | 3.19 us: 1.01x faster                                                     |
| deepcopy_memo            | 38.4 us                                                               | 38.1 us: 1.01x faster                                                     |
| hexiom                   | 6.02 ms                                                               | 5.98 ms: 1.01x faster                                                     |
| asyncio_tcp              | 483 ms                                                                | 480 ms: 1.01x faster                                                      |
| meteor_contest           | 106 ms                                                                | 106 ms: 1.00x faster                                                      |
| asyncio_tcp_ssl          | 1.79 sec                                                              | 1.79 sec: 1.00x faster                                                    |
| pickle_dict              | 31.7 us                                                               | 31.6 us: 1.00x faster                                                     |
| sqlglot_parse            | 1.29 ms                                                               | 1.30 ms: 1.00x slower                                                     |
| unpickle_pure_python     | 212 us                                                                | 213 us: 1.00x slower                                                      |
| json_dumps               | 9.71 ms                                                               | 9.75 ms: 1.00x slower                                                     |
| pickle_list              | 4.51 us                                                               | 4.54 us: 1.01x slower                                                     |
| sqlglot_normalize        | 105 ms                                                                | 106 ms: 1.01x slower                                                      |
| scimark_fft              | 358 ms                                                                | 361 ms: 1.01x slower                                                      |
| python_startup_no_site   | 6.83 ms                                                               | 6.89 ms: 1.01x slower                                                     |
| typing_runtime_protocols | 145 us                                                                | 147 us: 1.01x slower                                                      |
| logging_simple           | 5.88 us                                                               | 5.94 us: 1.01x slower                                                     |
| pathlib                  | 18.5 ms                                                               | 18.7 ms: 1.01x slower                                                     |
| python_startup           | 9.33 ms                                                               | 9.47 ms: 1.01x slower                                                     |
| regex_effbot             | 3.54 ms                                                               | 3.59 ms: 1.02x slower                                                     |
| go                       | 137 ms                                                                | 139 ms: 1.02x slower                                                      |
| sqlglot_optimize         | 52.8 ms                                                               | 53.8 ms: 1.02x slower                                                     |
| coroutines               | 21.6 ms                                                               | 22.0 ms: 1.02x slower                                                     |
| regex_v8                 | 21.9 ms                                                               | 22.3 ms: 1.02x slower                                                     |
| scimark_lu               | 110 ms                                                                | 113 ms: 1.02x slower                                                      |
| mdp                      | 2.53 sec                                                              | 2.59 sec: 1.02x slower                                                    |
| raytrace                 | 266 ms                                                                | 272 ms: 1.03x slower                                                      |
| scimark_sparse_mat_mult  | 4.57 ms                                                               | 4.71 ms: 1.03x slower                                                     |
| telco                    | 7.80 ms                                                               | 8.04 ms: 1.03x slower                                                     |
| generators               | 27.8 ms                                                               | 28.7 ms: 1.03x slower                                                     |
| sqlglot_transpile        | 1.61 ms                                                               | 1.66 ms: 1.04x slower                                                     |
| regex_dna                | 208 ms                                                                | 215 ms: 1.04x slower                                                      |
| deltablue                | 3.20 ms                                                               | 3.33 ms: 1.04x slower                                                     |
| unpickle                 | 14.9 us                                                               | 15.6 us: 1.05x slower                                                     |
| tornado_http             | 95.7 ms                                                               | 103 ms: 1.08x slower                                                      |
| xml_etree_generate       | 83.4 ms                                                               | 93.5 ms: 1.12x slower                                                     |
| mypy2                    | 337 ms                                                                | 444 ms: 1.32x slower                                                      |
| float                    | 79.2 ms                                                               | 110 ms: 1.39x slower                                                      |
| xml_etree_parse          | 152 ms                                                                | 570 ms: 3.74x slower                                                      |
| xml_etree_iterparse      | 103 ms                                                                | 516 ms: 5.00x slower                                                      |
| Geometric mean           | (ref)                                                                 | 1.03x slower                                                              |

Benchmark hidden because not significant (18): unpickle_list, json, scimark_sor, scimark_monte_carlo, logging_format, regex_compile, comprehensions, deepcopy, pprint_pformat, pickle, bench_thread_pool, dulwich_log, dask, async_generators, bench_mp_pool, tomli_loads, xml_etree_process, sqlite_synth


# HPT report

- Reliability score: 72.84% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
