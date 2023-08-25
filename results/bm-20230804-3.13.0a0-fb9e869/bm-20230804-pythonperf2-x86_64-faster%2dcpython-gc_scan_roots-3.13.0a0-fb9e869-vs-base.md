
# Results vs. base

- fork: faster-cpython
- ref: gc_scan_roots
- machine: linux-x86_64
- commit hash: fb9e869
- commit date: 2023-08-04
- overall geometric mean: 1.01x slower
- HPT reliability: 98.57%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230804-pythonperf2-x86_64-python-2ba7c7f7b151ff56cf12-3.13.0a0-2ba7c7f | bm-20230804-pythonperf2-x86_64-faster%2dcpython-gc_scan_roots-3.13.0a0-fb9e869 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| docutils       | 2.92 sec                                                                    | 2.98 sec: 1.02x slower                                                         |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230804-pythonperf2-x86_64-python-2ba7c7f7b151ff56cf12-3.13.0a0-2ba7c7f | bm-20230804-pythonperf2-x86_64-faster%2dcpython-gc_scan_roots-3.13.0a0-fb9e869 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 260 ms                                                                      | 260 ms: 1.00x faster                                                           |
| nbody          | 89.2 ms                                                                     | 90.2 ms: 1.01x slower                                                          |
| float          | 80.7 ms                                                                     | 81.9 ms: 1.02x slower                                                          |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230804-pythonperf2-x86_64-python-2ba7c7f7b151ff56cf12-3.13.0a0-2ba7c7f | bm-20230804-pythonperf2-x86_64-faster%2dcpython-gc_scan_roots-3.13.0a0-fb9e869 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                                     | 3.47 ms: 1.08x faster                                                          |
| regex_compile  | 149 ms                                                                      | 150 ms: 1.01x slower                                                           |
| regex_dna      | 242 ms                                                                      | 245 ms: 1.01x slower                                                           |
| regex_v8       | 23.6 ms                                                                     | 24.3 ms: 1.03x slower                                                          |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20230804-pythonperf2-x86_64-python-2ba7c7f7b151ff56cf12-3.13.0a0-2ba7c7f | bm-20230804-pythonperf2-x86_64-faster%2dcpython-gc_scan_roots-3.13.0a0-fb9e869 |
|--------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_parse    | 152 ms                                                                      | 146 ms: 1.04x faster                                                           |
| pickle_pure_python | 323 us                                                                      | 318 us: 1.02x faster                                                           |
| json_dumps         | 10.4 ms                                                                     | 10.3 ms: 1.01x faster                                                          |
| unpickle           | 14.7 us                                                                     | 14.5 us: 1.01x faster                                                          |
| unpickle_list      | 4.69 us                                                                     | 4.67 us: 1.00x faster                                                          |
| pickle_dict        | 32.6 us                                                                     | 32.9 us: 1.01x slower                                                          |
| xml_etree_generate | 86.5 ms                                                                     | 87.2 ms: 1.01x slower                                                          |
| xml_etree_process  | 59.1 ms                                                                     | 60.4 ms: 1.02x slower                                                          |
| tomli_loads        | 2.29 sec                                                                    | 2.34 sec: 1.02x slower                                                         |
| json_loads         | 24.5 us                                                                     | 25.2 us: 1.03x slower                                                          |
| Geometric mean     | (ref)                                                                       | 1.00x slower                                                                   |

Benchmark hidden because not significant (4): xml_etree_iterparse, pickle_list, pickle, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230804-pythonperf2-x86_64-python-2ba7c7f7b151ff56cf12-3.13.0a0-2ba7c7f | bm-20230804-pythonperf2-x86_64-faster%2dcpython-gc_scan_roots-3.13.0a0-fb9e869 |
|------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 11.6 ms                                                                     | 11.6 ms: 1.01x slower                                                          |
| python_startup_no_site | 8.63 ms                                                                     | 8.68 ms: 1.01x slower                                                          |
| Geometric mean         | (ref)                                                                       | 1.01x slower                                                                   |

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20230804-pythonperf2-x86_64-python-2ba7c7f7b151ff56cf12-3.13.0a0-2ba7c7f | bm-20230804-pythonperf2-x86_64-faster%2dcpython-gc_scan_roots-3.13.0a0-fb9e869 |
|--------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot             | 3.77 ms                                                                     | 3.47 ms: 1.08x faster                                                          |
| xml_etree_parse          | 152 ms                                                                      | 146 ms: 1.04x faster                                                           |
| logging_silent           | 101 ns                                                                      | 98.3 ns: 1.03x faster                                                          |
| sqlite_synth             | 2.76 us                                                                     | 2.70 us: 1.02x faster                                                          |
| logging_simple           | 6.87 us                                                                     | 6.76 us: 1.02x faster                                                          |
| pickle_pure_python       | 323 us                                                                      | 318 us: 1.02x faster                                                           |
| meteor_contest           | 131 ms                                                                      | 129 ms: 1.01x faster                                                           |
| asyncio_tcp              | 373 ms                                                                      | 369 ms: 1.01x faster                                                           |
| mdp                      | 2.58 sec                                                                    | 2.55 sec: 1.01x faster                                                         |
| json_dumps               | 10.4 ms                                                                     | 10.3 ms: 1.01x faster                                                          |
| coverage                 | 88.4 ms                                                                     | 87.5 ms: 1.01x faster                                                          |
| crypto_pyaes             | 73.6 ms                                                                     | 72.9 ms: 1.01x faster                                                          |
| chaos                    | 62.5 ms                                                                     | 62.0 ms: 1.01x faster                                                          |
| unpickle                 | 14.7 us                                                                     | 14.5 us: 1.01x faster                                                          |
| richards                 | 55.2 ms                                                                     | 54.9 ms: 1.01x faster                                                          |
| logging_format           | 7.45 us                                                                     | 7.40 us: 1.01x faster                                                          |
| spectral_norm            | 97.6 ms                                                                     | 96.9 ms: 1.01x faster                                                          |
| sqlglot_normalize        | 118 ms                                                                      | 118 ms: 1.01x faster                                                           |
| fannkuch                 | 395 ms                                                                      | 393 ms: 1.01x faster                                                           |
| dulwich_log              | 69.1 ms                                                                     | 68.7 ms: 1.01x faster                                                          |
| deepcopy                 | 387 us                                                                      | 385 us: 1.01x faster                                                           |
| unpickle_list            | 4.69 us                                                                     | 4.67 us: 1.00x faster                                                          |
| pidigits                 | 260 ms                                                                      | 260 ms: 1.00x faster                                                           |
| deltablue                | 3.70 ms                                                                     | 3.72 ms: 1.00x slower                                                          |
| hexiom                   | 6.48 ms                                                                     | 6.51 ms: 1.00x slower                                                          |
| python_startup           | 11.6 ms                                                                     | 11.6 ms: 1.01x slower                                                          |
| regex_compile            | 149 ms                                                                      | 150 ms: 1.01x slower                                                           |
| python_startup_no_site   | 8.63 ms                                                                     | 8.68 ms: 1.01x slower                                                          |
| sqlglot_transpile        | 1.84 ms                                                                     | 1.85 ms: 1.01x slower                                                          |
| pickle_dict              | 32.6 us                                                                     | 32.9 us: 1.01x slower                                                          |
| xml_etree_generate       | 86.5 ms                                                                     | 87.2 ms: 1.01x slower                                                          |
| richards_super           | 61.7 ms                                                                     | 62.2 ms: 1.01x slower                                                          |
| dask                     | 588 ms                                                                      | 594 ms: 1.01x slower                                                           |
| scimark_monte_carlo      | 68.2 ms                                                                     | 68.9 ms: 1.01x slower                                                          |
| deepcopy_memo            | 37.9 us                                                                     | 38.3 us: 1.01x slower                                                          |
| regex_dna                | 242 ms                                                                      | 245 ms: 1.01x slower                                                           |
| deepcopy_reduce          | 3.45 us                                                                     | 3.49 us: 1.01x slower                                                          |
| async_tree_none          | 474 ms                                                                      | 479 ms: 1.01x slower                                                           |
| pathlib                  | 19.4 ms                                                                     | 19.6 ms: 1.01x slower                                                          |
| async_tree_memoization   | 569 ms                                                                      | 575 ms: 1.01x slower                                                           |
| generators               | 36.7 ms                                                                     | 37.1 ms: 1.01x slower                                                          |
| nbody                    | 89.2 ms                                                                     | 90.2 ms: 1.01x slower                                                          |
| scimark_sor              | 144 ms                                                                      | 146 ms: 1.01x slower                                                           |
| nqueens                  | 91.2 ms                                                                     | 92.3 ms: 1.01x slower                                                          |
| pycparser                | 1.33 sec                                                                    | 1.34 sec: 1.01x slower                                                         |
| comprehensions           | 22.2 us                                                                     | 22.5 us: 1.01x slower                                                          |
| float                    | 80.7 ms                                                                     | 81.9 ms: 1.02x slower                                                          |
| async_tree_io            | 1.09 sec                                                                    | 1.11 sec: 1.02x slower                                                         |
| docutils                 | 2.92 sec                                                                    | 2.98 sec: 1.02x slower                                                         |
| xml_etree_process        | 59.1 ms                                                                     | 60.4 ms: 1.02x slower                                                          |
| tomli_loads              | 2.29 sec                                                                    | 2.34 sec: 1.02x slower                                                         |
| raytrace                 | 275 ms                                                                      | 282 ms: 1.02x slower                                                           |
| json_loads               | 24.5 us                                                                     | 25.2 us: 1.03x slower                                                          |
| json                     | 5.12 ms                                                                     | 5.26 ms: 1.03x slower                                                          |
| regex_v8                 | 23.6 ms                                                                     | 24.3 ms: 1.03x slower                                                          |
| typing_runtime_protocols | 152 us                                                                      | 156 us: 1.03x slower                                                           |
| create_gc_cycles         | 1.67 ms                                                                     | 1.73 ms: 1.03x slower                                                          |
| scimark_sparse_mat_mult  | 4.21 ms                                                                     | 4.41 ms: 1.05x slower                                                          |
| gc_traversal             | 3.54 ms                                                                     | 4.08 ms: 1.15x slower                                                          |
| unpack_sequence          | 49.6 ns                                                                     | 59.7 ns: 1.20x slower                                                          |
| Geometric mean           | (ref)                                                                       | 1.01x slower                                                                   |

Benchmark hidden because not significant (22): bench_thread_pool, tornado_http, xml_etree_iterparse, mako, pickle_list, pickle, pyflate, sqlglot_optimize, scimark_lu, asyncio_tcp_ssl, pprint_safe_repr, telco, mypy2, async_generators, go, pprint_pformat, sqlglot_parse, scimark_fft, async_tree_cpu_io_mixed, unpickle_pure_python, coroutines, bench_mp_pool


# HPT report

- Reliability score: 98.57% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
