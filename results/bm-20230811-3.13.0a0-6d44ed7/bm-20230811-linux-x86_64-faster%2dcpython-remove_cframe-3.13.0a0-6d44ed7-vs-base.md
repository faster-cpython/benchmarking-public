
# Results vs. base

- fork: faster-cpython
- ref: remove_cframe
- machine: linux-x86_64
- commit hash: 6d44ed7
- commit date: 2023-08-11
- overall geometric mean: 1.00x faster
- HPT reliability: 98.57%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230816-linux-x86_64-python-42429d3b9adb8af1eadc-3.13.0a0-42429d3 | bm-20230811-linux-x86_64-faster%2dcpython-remove_cframe-3.13.0a0-6d44ed7 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 91.7 ms                                                               | 89.8 ms: 1.02x faster                                                    |
| float          | 80.6 ms                                                               | 79.6 ms: 1.01x faster                                                    |
| pidigits       | 201 ms                                                                | 201 ms: 1.00x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230816-linux-x86_64-python-42429d3b9adb8af1eadc-3.13.0a0-42429d3 | bm-20230811-linux-x86_64-faster%2dcpython-remove_cframe-3.13.0a0-6d44ed7 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 217 ms                                                                | 215 ms: 1.01x faster                                                     |
| regex_v8       | 22.9 ms                                                               | 23.1 ms: 1.01x slower                                                    |
| regex_effbot   | 3.66 ms                                                               | 3.79 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                             |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230816-linux-x86_64-python-42429d3b9adb8af1eadc-3.13.0a0-42429d3 | bm-20230811-linux-x86_64-faster%2dcpython-remove_cframe-3.13.0a0-6d44ed7 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle             | 14.9 us                                                               | 14.0 us: 1.06x faster                                                    |
| pickle_dict          | 33.0 us                                                               | 31.3 us: 1.06x faster                                                    |
| xml_etree_generate   | 84.6 ms                                                               | 83.0 ms: 1.02x faster                                                    |
| xml_etree_process    | 58.5 ms                                                               | 57.6 ms: 1.02x faster                                                    |
| pickle_list          | 4.63 us                                                               | 4.60 us: 1.01x faster                                                    |
| xml_etree_iterparse  | 103 ms                                                                | 102 ms: 1.01x faster                                                     |
| unpickle_pure_python | 213 us                                                                | 214 us: 1.00x slower                                                     |
| pickle_pure_python   | 298 us                                                                | 300 us: 1.00x slower                                                     |
| tomli_loads          | 2.11 sec                                                              | 2.12 sec: 1.01x slower                                                   |
| json_dumps           | 9.69 ms                                                               | 9.75 ms: 1.01x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                             |

Benchmark hidden because not significant (4): xml_etree_parse, pickle, unpickle_list, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230816-linux-x86_64-python-42429d3b9adb8af1eadc-3.13.0a0-42429d3 | bm-20230811-linux-x86_64-faster%2dcpython-remove_cframe-3.13.0a0-6d44ed7 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.84 ms                                                               | 6.82 ms: 1.00x faster                                                    |
| python_startup         | 9.35 ms                                                               | 9.33 ms: 1.00x faster                                                    |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230816-linux-x86_64-python-42429d3b9adb8af1eadc-3.13.0a0-42429d3 | bm-20230811-linux-x86_64-faster%2dcpython-remove_cframe-3.13.0a0-6d44ed7 |
|-----------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako      | 10.8 ms                                                               | 10.7 ms: 1.00x faster                                                    |

All benchmarks:
===============

| Benchmark                | bm-20230816-linux-x86_64-python-42429d3b9adb8af1eadc-3.13.0a0-42429d3 | bm-20230811-linux-x86_64-faster%2dcpython-remove_cframe-3.13.0a0-6d44ed7 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mdp                      | 2.73 sec                                                              | 2.56 sec: 1.07x faster                                                   |
| unpickle                 | 14.9 us                                                               | 14.0 us: 1.06x faster                                                    |
| pickle_dict              | 33.0 us                                                               | 31.3 us: 1.06x faster                                                    |
| unpack_sequence          | 43.9 ns                                                               | 41.8 ns: 1.05x faster                                                    |
| pycparser                | 1.20 sec                                                              | 1.15 sec: 1.04x faster                                                   |
| pprint_safe_repr         | 732 ms                                                                | 714 ms: 1.03x faster                                                     |
| logging_format           | 6.57 us                                                               | 6.42 us: 1.02x faster                                                    |
| fannkuch                 | 392 ms                                                                | 384 ms: 1.02x faster                                                     |
| nbody                    | 91.7 ms                                                               | 89.8 ms: 1.02x faster                                                    |
| xml_etree_generate       | 84.6 ms                                                               | 83.0 ms: 1.02x faster                                                    |
| sqlglot_parse            | 1.28 ms                                                               | 1.26 ms: 1.02x faster                                                    |
| xml_etree_process        | 58.5 ms                                                               | 57.6 ms: 1.02x faster                                                    |
| sqlglot_transpile        | 1.60 ms                                                               | 1.58 ms: 1.02x faster                                                    |
| deepcopy_memo            | 37.7 us                                                               | 37.1 us: 1.01x faster                                                    |
| telco                    | 8.05 ms                                                               | 7.94 ms: 1.01x faster                                                    |
| float                    | 80.6 ms                                                               | 79.6 ms: 1.01x faster                                                    |
| crypto_pyaes             | 68.5 ms                                                               | 67.7 ms: 1.01x faster                                                    |
| create_gc_cycles         | 1.49 ms                                                               | 1.47 ms: 1.01x faster                                                    |
| raytrace                 | 274 ms                                                                | 271 ms: 1.01x faster                                                     |
| pprint_pformat           | 1.49 sec                                                              | 1.47 sec: 1.01x faster                                                   |
| sqlglot_optimize         | 53.1 ms                                                               | 52.6 ms: 1.01x faster                                                    |
| sqlglot_normalize        | 106 ms                                                                | 105 ms: 1.01x faster                                                     |
| comprehensions           | 20.8 us                                                               | 20.7 us: 1.01x faster                                                    |
| pickle_list              | 4.63 us                                                               | 4.60 us: 1.01x faster                                                    |
| xml_etree_iterparse      | 103 ms                                                                | 102 ms: 1.01x faster                                                     |
| hexiom                   | 6.08 ms                                                               | 6.04 ms: 1.01x faster                                                    |
| regex_dna                | 217 ms                                                                | 215 ms: 1.01x faster                                                     |
| mako                     | 10.8 ms                                                               | 10.7 ms: 1.00x faster                                                    |
| bench_thread_pool        | 819 us                                                                | 815 us: 1.00x faster                                                     |
| asyncio_tcp              | 486 ms                                                                | 485 ms: 1.00x faster                                                     |
| python_startup_no_site   | 6.84 ms                                                               | 6.82 ms: 1.00x faster                                                    |
| python_startup           | 9.35 ms                                                               | 9.33 ms: 1.00x faster                                                    |
| pidigits                 | 201 ms                                                                | 201 ms: 1.00x faster                                                     |
| asyncio_tcp_ssl          | 1.79 sec                                                              | 1.79 sec: 1.00x slower                                                   |
| dulwich_log              | 65.6 ms                                                               | 65.9 ms: 1.00x slower                                                    |
| unpickle_pure_python     | 213 us                                                                | 214 us: 1.00x slower                                                     |
| pickle_pure_python       | 298 us                                                                | 300 us: 1.00x slower                                                     |
| tomli_loads              | 2.11 sec                                                              | 2.12 sec: 1.01x slower                                                   |
| regex_v8                 | 22.9 ms                                                               | 23.1 ms: 1.01x slower                                                    |
| json_dumps               | 9.69 ms                                                               | 9.75 ms: 1.01x slower                                                    |
| sqlite_synth             | 2.74 us                                                               | 2.76 us: 1.01x slower                                                    |
| scimark_sparse_mat_mult  | 4.85 ms                                                               | 4.88 ms: 1.01x slower                                                    |
| pyflate                  | 444 ms                                                                | 447 ms: 1.01x slower                                                     |
| chaos                    | 59.8 ms                                                               | 60.5 ms: 1.01x slower                                                    |
| go                       | 138 ms                                                                | 140 ms: 1.01x slower                                                     |
| nqueens                  | 80.3 ms                                                               | 81.6 ms: 1.02x slower                                                    |
| scimark_fft              | 349 ms                                                                | 354 ms: 1.02x slower                                                     |
| richards                 | 47.1 ms                                                               | 48.0 ms: 1.02x slower                                                    |
| logging_silent           | 102 ns                                                                | 105 ns: 1.02x slower                                                     |
| typing_runtime_protocols | 143 us                                                                | 148 us: 1.03x slower                                                     |
| regex_effbot             | 3.66 ms                                                               | 3.79 ms: 1.04x slower                                                    |
| scimark_lu               | 109 ms                                                                | 114 ms: 1.04x slower                                                     |
| gc_traversal             | 3.89 ms                                                               | 4.18 ms: 1.07x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.00x faster                                                             |

Benchmark hidden because not significant (29): dask, async_tree_cpu_io_mixed, json, xml_etree_parse, scimark_sor, pickle, async_tree_memoization, async_tree_io, generators, coverage, mypy2, deepcopy, logging_simple, tornado_http, unpickle_list, coroutines, spectral_norm, regex_compile, bench_mp_pool, async_tree_none, deepcopy_reduce, json_loads, async_generators, docutils, richards_super, meteor_contest, pathlib, scimark_monte_carlo, deltablue


# HPT report

- Reliability score: 98.57% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
