
# Results vs. base

- fork: faster-cpython
- ref: tweak_ints_monitorin
- machine: linux-x86_64
- commit hash: 0ccd3bb
- commit date: 2023-08-05
- overall geometric mean: 1.00x slower
- HPT reliability: 88.93%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230805-linux-x86_64-faster%2dcpython-tweak_ints_monitorin-3.13.0a0-0ccd3bb |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| docutils       | 2.65 sec                                                              | 2.66 sec: 1.00x slower                                                          |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230805-linux-x86_64-faster%2dcpython-tweak_ints_monitorin-3.13.0a0-0ccd3bb |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                                | 200 ms: 1.00x faster                                                            |
| float          | 79.2 ms                                                               | 81.1 ms: 1.02x slower                                                           |
| nbody          | 92.4 ms                                                               | 95.7 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230805-linux-x86_64-faster%2dcpython-tweak_ints_monitorin-3.13.0a0-0ccd3bb |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 21.9 ms                                                               | 21.7 ms: 1.00x faster                                                           |
| regex_compile  | 137 ms                                                                | 137 ms: 1.00x faster                                                            |
| regex_effbot   | 3.54 ms                                                               | 3.61 ms: 1.02x slower                                                           |
| regex_dna      | 208 ms                                                                | 213 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230805-linux-x86_64-faster%2dcpython-tweak_ints_monitorin-3.13.0a0-0ccd3bb |
|---------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle_list       | 4.94 us                                                               | 4.85 us: 1.02x faster                                                           |
| pickle_pure_python  | 299 us                                                                | 296 us: 1.01x faster                                                            |
| xml_etree_iterparse | 103 ms                                                                | 103 ms: 1.01x faster                                                            |
| xml_etree_process   | 58.1 ms                                                               | 57.8 ms: 1.01x faster                                                           |
| xml_etree_generate  | 83.4 ms                                                               | 83.6 ms: 1.00x slower                                                           |
| json_dumps          | 9.71 ms                                                               | 9.81 ms: 1.01x slower                                                           |
| tomli_loads         | 2.29 sec                                                              | 2.32 sec: 1.01x slower                                                          |
| pickle_dict         | 31.7 us                                                               | 32.3 us: 1.02x slower                                                           |
| pickle              | 10.7 us                                                               | 10.9 us: 1.02x slower                                                           |
| pickle_list         | 4.51 us                                                               | 4.79 us: 1.06x slower                                                           |
| Geometric mean      | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (4): unpickle, xml_etree_parse, unpickle_pure_python, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230805-linux-x86_64-faster%2dcpython-tweak_ints_monitorin-3.13.0a0-0ccd3bb |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 9.33 ms                                                               | 9.38 ms: 1.00x slower                                                           |
| python_startup_no_site | 6.83 ms                                                               | 6.86 ms: 1.00x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230805-linux-x86_64-faster%2dcpython-tweak_ints_monitorin-3.13.0a0-0ccd3bb |
|-----------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako      | 11.0 ms                                                               | 10.9 ms: 1.01x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c | bm-20230805-linux-x86_64-faster%2dcpython-tweak_ints_monitorin-3.13.0a0-0ccd3bb |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| gc_traversal             | 4.29 ms                                                               | 3.94 ms: 1.09x faster                                                           |
| typing_runtime_protocols | 145 us                                                                | 142 us: 1.03x faster                                                            |
| unpickle_list            | 4.94 us                                                               | 4.85 us: 1.02x faster                                                           |
| fannkuch                 | 394 ms                                                                | 389 ms: 1.01x faster                                                            |
| nqueens                  | 80.8 ms                                                               | 79.8 ms: 1.01x faster                                                           |
| pickle_pure_python       | 299 us                                                                | 296 us: 1.01x faster                                                            |
| deepcopy_reduce          | 3.21 us                                                               | 3.18 us: 1.01x faster                                                           |
| mako                     | 11.0 ms                                                               | 10.9 ms: 1.01x faster                                                           |
| pyflate                  | 446 ms                                                                | 442 ms: 1.01x faster                                                            |
| dulwich_log              | 66.4 ms                                                               | 65.8 ms: 1.01x faster                                                           |
| xml_etree_iterparse      | 103 ms                                                                | 103 ms: 1.01x faster                                                            |
| deltablue                | 3.20 ms                                                               | 3.18 ms: 1.01x faster                                                           |
| coverage                 | 95.0 ms                                                               | 94.3 ms: 1.01x faster                                                           |
| sqlglot_normalize        | 105 ms                                                                | 105 ms: 1.01x faster                                                            |
| xml_etree_process        | 58.1 ms                                                               | 57.8 ms: 1.01x faster                                                           |
| async_tree_io            | 1.19 sec                                                              | 1.19 sec: 1.01x faster                                                          |
| comprehensions           | 20.4 us                                                               | 20.3 us: 1.01x faster                                                           |
| regex_v8                 | 21.9 ms                                                               | 21.7 ms: 1.00x faster                                                           |
| deepcopy                 | 356 us                                                                | 354 us: 1.00x faster                                                            |
| sqlglot_optimize         | 52.8 ms                                                               | 52.6 ms: 1.00x faster                                                           |
| asyncio_tcp              | 483 ms                                                                | 482 ms: 1.00x faster                                                            |
| regex_compile            | 137 ms                                                                | 137 ms: 1.00x faster                                                            |
| asyncio_tcp_ssl          | 1.79 sec                                                              | 1.79 sec: 1.00x faster                                                          |
| pidigits                 | 201 ms                                                                | 200 ms: 1.00x faster                                                            |
| xml_etree_generate       | 83.4 ms                                                               | 83.6 ms: 1.00x slower                                                           |
| docutils                 | 2.65 sec                                                              | 2.66 sec: 1.00x slower                                                          |
| raytrace                 | 266 ms                                                                | 266 ms: 1.00x slower                                                            |
| mypy2                    | 337 ms                                                                | 338 ms: 1.00x slower                                                            |
| go                       | 137 ms                                                                | 138 ms: 1.00x slower                                                            |
| python_startup           | 9.33 ms                                                               | 9.38 ms: 1.00x slower                                                           |
| python_startup_no_site   | 6.83 ms                                                               | 6.86 ms: 1.00x slower                                                           |
| chaos                    | 58.9 ms                                                               | 59.2 ms: 1.01x slower                                                           |
| unpack_sequence          | 42.2 ns                                                               | 42.4 ns: 1.01x slower                                                           |
| crypto_pyaes             | 70.0 ms                                                               | 70.3 ms: 1.01x slower                                                           |
| pycparser                | 1.15 sec                                                              | 1.16 sec: 1.01x slower                                                          |
| async_generators         | 447 ms                                                                | 450 ms: 1.01x slower                                                            |
| hexiom                   | 6.02 ms                                                               | 6.07 ms: 1.01x slower                                                           |
| scimark_sor              | 121 ms                                                                | 122 ms: 1.01x slower                                                            |
| sqlglot_parse            | 1.29 ms                                                               | 1.30 ms: 1.01x slower                                                           |
| async_tree_none          | 478 ms                                                                | 483 ms: 1.01x slower                                                            |
| scimark_lu               | 110 ms                                                                | 111 ms: 1.01x slower                                                            |
| json_dumps               | 9.71 ms                                                               | 9.81 ms: 1.01x slower                                                           |
| tomli_loads              | 2.29 sec                                                              | 2.32 sec: 1.01x slower                                                          |
| scimark_sparse_mat_mult  | 4.57 ms                                                               | 4.65 ms: 1.02x slower                                                           |
| create_gc_cycles         | 1.49 ms                                                               | 1.51 ms: 1.02x slower                                                           |
| regex_effbot             | 3.54 ms                                                               | 3.61 ms: 1.02x slower                                                           |
| pickle_dict              | 31.7 us                                                               | 32.3 us: 1.02x slower                                                           |
| coroutines               | 21.6 ms                                                               | 22.0 ms: 1.02x slower                                                           |
| spectral_norm            | 107 ms                                                                | 109 ms: 1.02x slower                                                            |
| json                     | 4.82 ms                                                               | 4.92 ms: 1.02x slower                                                           |
| pickle                   | 10.7 us                                                               | 10.9 us: 1.02x slower                                                           |
| generators               | 27.8 ms                                                               | 28.4 ms: 1.02x slower                                                           |
| float                    | 79.2 ms                                                               | 81.1 ms: 1.02x slower                                                           |
| logging_simple           | 5.88 us                                                               | 6.02 us: 1.02x slower                                                           |
| regex_dna                | 208 ms                                                                | 213 ms: 1.02x slower                                                            |
| logging_format           | 6.45 us                                                               | 6.68 us: 1.03x slower                                                           |
| nbody                    | 92.4 ms                                                               | 95.7 ms: 1.04x slower                                                           |
| scimark_fft              | 358 ms                                                                | 372 ms: 1.04x slower                                                            |
| pickle_list              | 4.51 us                                                               | 4.79 us: 1.06x slower                                                           |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (23): deepcopy_memo, richards_super, meteor_contest, unpickle, xml_etree_parse, pprint_safe_repr, tornado_http, sqlite_synth, dask, bench_mp_pool, bench_thread_pool, mdp, telco, unpickle_pure_python, pprint_pformat, logging_silent, json_loads, scimark_monte_carlo, pathlib, richards, async_tree_memoization, async_tree_cpu_io_mixed, sqlglot_transpile


# HPT report

- Reliability score: 88.93% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
