
# Results vs. base

- fork: faster-cpython
- ref: no_untrack_dicts
- machine: linux-x86_64
- commit hash: f204b0a
- commit date: 2023-08-10
- overall geometric mean: 1.00x faster
- HPT reliability: 96.99%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230810-pythonperf2-x86_64-python-37d8b904f8b5b660f556-3.13.0a0-37d8b90 | bm-20230810-pythonperf2-x86_64-faster%2dcpython-no_untrack_dicts-3.13.0a0-f204b0a |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| docutils       | 2.94 sec                                                                    | 2.93 sec: 1.01x faster                                                            |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                      |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230810-pythonperf2-x86_64-python-37d8b904f8b5b660f556-3.13.0a0-37d8b90 | bm-20230810-pythonperf2-x86_64-faster%2dcpython-no_untrack_dicts-3.13.0a0-f204b0a |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pidigits       | 260 ms                                                                      | 259 ms: 1.00x faster                                                              |
| nbody          | 86.7 ms                                                                     | 87.8 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                      |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230810-pythonperf2-x86_64-python-37d8b904f8b5b660f556-3.13.0a0-37d8b90 | bm-20230810-pythonperf2-x86_64-faster%2dcpython-no_untrack_dicts-3.13.0a0-f204b0a |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 3.74 ms                                                                     | 3.62 ms: 1.03x faster                                                             |
| regex_compile  | 150 ms                                                                      | 149 ms: 1.01x faster                                                              |
| regex_v8       | 24.2 ms                                                                     | 24.2 ms: 1.00x slower                                                             |
| regex_dna      | 244 ms                                                                      | 252 ms: 1.03x slower                                                              |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20230810-pythonperf2-x86_64-python-37d8b904f8b5b660f556-3.13.0a0-37d8b90 | bm-20230810-pythonperf2-x86_64-faster%2dcpython-no_untrack_dicts-3.13.0a0-f204b0a |
|--------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| unpickle           | 15.0 us                                                                     | 14.7 us: 1.02x faster                                                             |
| pickle_pure_python | 321 us                                                                      | 315 us: 1.02x faster                                                              |
| pickle             | 10.3 us                                                                     | 10.2 us: 1.01x faster                                                             |
| pickle_dict        | 32.3 us                                                                     | 32.0 us: 1.01x faster                                                             |
| json_loads         | 25.6 us                                                                     | 25.5 us: 1.01x faster                                                             |
| xml_etree_parse    | 148 ms                                                                      | 147 ms: 1.01x faster                                                              |
| xml_etree_generate | 85.9 ms                                                                     | 87.1 ms: 1.01x slower                                                             |
| xml_etree_process  | 59.2 ms                                                                     | 60.4 ms: 1.02x slower                                                             |
| tomli_loads        | 2.24 sec                                                                    | 2.29 sec: 1.02x slower                                                            |
| unpickle_list      | 4.65 us                                                                     | 4.75 us: 1.02x slower                                                             |
| pickle_list        | 4.36 us                                                                     | 4.52 us: 1.04x slower                                                             |
| Geometric mean     | (ref)                                                                       | 1.00x slower                                                                      |

Benchmark hidden because not significant (3): unpickle_pure_python, json_dumps, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230810-pythonperf2-x86_64-python-37d8b904f8b5b660f556-3.13.0a0-37d8b90 | bm-20230810-pythonperf2-x86_64-faster%2dcpython-no_untrack_dicts-3.13.0a0-f204b0a |
|------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 8.63 ms                                                                     | 8.55 ms: 1.01x faster                                                             |
| python_startup         | 11.6 ms                                                                     | 11.5 ms: 1.01x faster                                                             |
| Geometric mean         | (ref)                                                                       | 1.01x faster                                                                      |

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20230810-pythonperf2-x86_64-python-37d8b904f8b5b660f556-3.13.0a0-37d8b90 | bm-20230810-pythonperf2-x86_64-faster%2dcpython-no_untrack_dicts-3.13.0a0-f204b0a |
|--------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| create_gc_cycles         | 1.64 ms                                                                     | 1.47 ms: 1.12x faster                                                             |
| async_tree_io            | 1.09 sec                                                                    | 1.04 sec: 1.05x faster                                                            |
| async_tree_none          | 471 ms                                                                      | 453 ms: 1.04x faster                                                              |
| regex_effbot             | 3.74 ms                                                                     | 3.62 ms: 1.03x faster                                                             |
| crypto_pyaes             | 76.3 ms                                                                     | 74.3 ms: 1.03x faster                                                             |
| async_tree_cpu_io_mixed  | 715 ms                                                                      | 698 ms: 1.03x faster                                                              |
| async_tree_memoization   | 548 ms                                                                      | 535 ms: 1.02x faster                                                              |
| json                     | 5.32 ms                                                                     | 5.20 ms: 1.02x faster                                                             |
| go                       | 177 ms                                                                      | 173 ms: 1.02x faster                                                              |
| richards_super           | 61.7 ms                                                                     | 60.4 ms: 1.02x faster                                                             |
| unpickle                 | 15.0 us                                                                     | 14.7 us: 1.02x faster                                                             |
| scimark_sparse_mat_mult  | 4.18 ms                                                                     | 4.10 ms: 1.02x faster                                                             |
| logging_simple           | 6.86 us                                                                     | 6.73 us: 1.02x faster                                                             |
| scimark_fft              | 307 ms                                                                      | 301 ms: 1.02x faster                                                              |
| async_generators         | 399 ms                                                                      | 392 ms: 1.02x faster                                                              |
| pickle_pure_python       | 321 us                                                                      | 315 us: 1.02x faster                                                              |
| pickle                   | 10.3 us                                                                     | 10.2 us: 1.01x faster                                                             |
| richards                 | 54.0 ms                                                                     | 53.5 ms: 1.01x faster                                                             |
| deepcopy_reduce          | 3.49 us                                                                     | 3.45 us: 1.01x faster                                                             |
| logging_format           | 7.43 us                                                                     | 7.36 us: 1.01x faster                                                             |
| regex_compile            | 150 ms                                                                      | 149 ms: 1.01x faster                                                              |
| dask                     | 592 ms                                                                      | 587 ms: 1.01x faster                                                              |
| python_startup_no_site   | 8.63 ms                                                                     | 8.55 ms: 1.01x faster                                                             |
| pycparser                | 1.34 sec                                                                    | 1.33 sec: 1.01x faster                                                            |
| nqueens                  | 91.4 ms                                                                     | 90.6 ms: 1.01x faster                                                             |
| sqlglot_normalize        | 118 ms                                                                      | 117 ms: 1.01x faster                                                              |
| meteor_contest           | 130 ms                                                                      | 129 ms: 1.01x faster                                                              |
| fannkuch                 | 392 ms                                                                      | 389 ms: 1.01x faster                                                              |
| pickle_dict              | 32.3 us                                                                     | 32.0 us: 1.01x faster                                                             |
| json_loads               | 25.6 us                                                                     | 25.5 us: 1.01x faster                                                             |
| xml_etree_parse          | 148 ms                                                                      | 147 ms: 1.01x faster                                                              |
| python_startup           | 11.6 ms                                                                     | 11.5 ms: 1.01x faster                                                             |
| pyflate                  | 516 ms                                                                      | 512 ms: 1.01x faster                                                              |
| docutils                 | 2.94 sec                                                                    | 2.93 sec: 1.01x faster                                                            |
| dulwich_log              | 69.0 ms                                                                     | 68.7 ms: 1.00x faster                                                             |
| sqlglot_optimize         | 59.6 ms                                                                     | 59.4 ms: 1.00x faster                                                             |
| pidigits                 | 260 ms                                                                      | 259 ms: 1.00x faster                                                              |
| comprehensions           | 22.4 us                                                                     | 22.3 us: 1.00x faster                                                             |
| regex_v8                 | 24.2 ms                                                                     | 24.2 ms: 1.00x slower                                                             |
| asyncio_tcp_ssl          | 1.58 sec                                                                    | 1.58 sec: 1.00x slower                                                            |
| sqlglot_parse            | 1.43 ms                                                                     | 1.44 ms: 1.00x slower                                                             |
| hexiom                   | 6.53 ms                                                                     | 6.57 ms: 1.01x slower                                                             |
| generators               | 36.2 ms                                                                     | 36.4 ms: 1.01x slower                                                             |
| logging_silent           | 97.7 ns                                                                     | 98.4 ns: 1.01x slower                                                             |
| sqlglot_transpile        | 1.83 ms                                                                     | 1.85 ms: 1.01x slower                                                             |
| coroutines               | 23.9 ms                                                                     | 24.1 ms: 1.01x slower                                                             |
| pathlib                  | 19.5 ms                                                                     | 19.7 ms: 1.01x slower                                                             |
| typing_runtime_protocols | 151 us                                                                      | 153 us: 1.01x slower                                                              |
| nbody                    | 86.7 ms                                                                     | 87.8 ms: 1.01x slower                                                             |
| scimark_sor              | 148 ms                                                                      | 150 ms: 1.01x slower                                                              |
| spectral_norm            | 91.7 ms                                                                     | 93.0 ms: 1.01x slower                                                             |
| xml_etree_generate       | 85.9 ms                                                                     | 87.1 ms: 1.01x slower                                                             |
| scimark_monte_carlo      | 71.2 ms                                                                     | 72.4 ms: 1.02x slower                                                             |
| mdp                      | 2.54 sec                                                                    | 2.58 sec: 1.02x slower                                                            |
| pprint_safe_repr         | 805 ms                                                                      | 820 ms: 1.02x slower                                                              |
| xml_etree_process        | 59.2 ms                                                                     | 60.4 ms: 1.02x slower                                                             |
| tomli_loads              | 2.24 sec                                                                    | 2.29 sec: 1.02x slower                                                            |
| pprint_pformat           | 1.64 sec                                                                    | 1.68 sec: 1.02x slower                                                            |
| unpickle_list            | 4.65 us                                                                     | 4.75 us: 1.02x slower                                                             |
| coverage                 | 79.6 ms                                                                     | 81.5 ms: 1.02x slower                                                             |
| regex_dna                | 244 ms                                                                      | 252 ms: 1.03x slower                                                              |
| scimark_lu               | 100 ms                                                                      | 104 ms: 1.03x slower                                                              |
| pickle_list              | 4.36 us                                                                     | 4.52 us: 1.04x slower                                                             |
| gc_traversal             | 3.50 ms                                                                     | 3.80 ms: 1.08x slower                                                             |
| unpack_sequence          | 53.1 ns                                                                     | 60.1 ns: 1.13x slower                                                             |
| Geometric mean           | (ref)                                                                       | 1.00x faster                                                                      |

Benchmark hidden because not significant (17): bench_thread_pool, mypy2, tornado_http, unpickle_pure_python, float, sqlite_synth, deltablue, chaos, asyncio_tcp, deepcopy_memo, json_dumps, raytrace, telco, mako, deepcopy, xml_etree_iterparse, bench_mp_pool


# HPT report

- Reliability score: 96.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
