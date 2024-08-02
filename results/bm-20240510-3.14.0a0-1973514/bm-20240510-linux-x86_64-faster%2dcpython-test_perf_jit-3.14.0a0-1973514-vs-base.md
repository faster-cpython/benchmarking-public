# Results vs. base

- fork: faster-cpython
- ref: test_perf_jit
- machine: linux-x86_64
- commit hash: 1973514
- commit date: 2024-05-10
- overall geometric mean: 1.01x slower
- HPT reliability: 99.57%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240509-linux-x86_64-python-35b5eaa176a5bae8a0ca-3.14.0a0-35b5eaa | bm-20240510-linux-x86_64-faster%2dcpython-test_perf_jit-3.14.0a0-1973514 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| chameleon      | 6.87 ms                                                               | 6.94 ms: 1.01x slower                                                    |
| docutils       | 2.80 sec                                                              | 2.81 sec: 1.00x slower                                                   |
| html5lib       | 67.0 ms                                                               | 66.6 ms: 1.01x faster                                                    |
| tornado_http   | 93.7 ms                                                               | 94.5 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                             |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_none, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240509-linux-x86_64-python-35b5eaa176a5bae8a0ca-3.14.0a0-35b5eaa | bm-20240510-linux-x86_64-faster%2dcpython-test_perf_jit-3.14.0a0-1973514 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 88.6 ms                                                               | 90.1 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                             |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240509-linux-x86_64-python-35b5eaa176a5bae8a0ca-3.14.0a0-35b5eaa | bm-20240510-linux-x86_64-faster%2dcpython-test_perf_jit-3.14.0a0-1973514 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 223 ms                                                                | 220 ms: 1.01x faster                                                     |
| regex_compile  | 134 ms                                                                | 136 ms: 1.01x slower                                                     |
| regex_effbot   | 3.67 ms                                                               | 3.73 ms: 1.02x slower                                                    |
| regex_v8       | 24.6 ms                                                               | 25.9 ms: 1.05x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240509-linux-x86_64-python-35b5eaa176a5bae8a0ca-3.14.0a0-35b5eaa | bm-20240510-linux-x86_64-faster%2dcpython-test_perf_jit-3.14.0a0-1973514 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps           | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                                    |
| json_loads           | 28.9 us                                                               | 28.8 us: 1.00x faster                                                    |
| pickle_dict          | 33.9 us                                                               | 34.0 us: 1.00x slower                                                    |
| pickle_pure_python   | 305 us                                                                | 306 us: 1.00x slower                                                     |
| tomli_loads          | 2.06 sec                                                              | 2.08 sec: 1.01x slower                                                   |
| unpickle_pure_python | 217 us                                                                | 221 us: 1.02x slower                                                     |
| xml_etree_process    | 60.6 ms                                                               | 61.8 ms: 1.02x slower                                                    |
| unpickle             | 15.9 us                                                               | 16.2 us: 1.02x slower                                                    |
| xml_etree_generate   | 87.4 ms                                                               | 89.5 ms: 1.02x slower                                                    |
| pickle_list          | 5.20 us                                                               | 5.63 us: 1.08x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                             |

Benchmark hidden because not significant (4): pickle, xml_etree_iterparse, unpickle_list, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240509-linux-x86_64-python-35b5eaa176a5bae8a0ca-3.14.0a0-35b5eaa | bm-20240510-linux-x86_64-faster%2dcpython-test_perf_jit-3.14.0a0-1973514 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup | 10.4 ms                                                               | 10.4 ms: 1.00x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                             |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240509-linux-x86_64-python-35b5eaa176a5bae8a0ca-3.14.0a0-35b5eaa | bm-20240510-linux-x86_64-faster%2dcpython-test_perf_jit-3.14.0a0-1973514 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 23.4 ms                                                               | 23.1 ms: 1.02x faster                                                    |
| genshi_xml      | 50.9 ms                                                               | 50.6 ms: 1.01x faster                                                    |
| django_template | 33.8 ms                                                               | 35.1 ms: 1.04x slower                                                    |
| mako            | 10.6 ms                                                               | 11.3 ms: 1.07x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                             |

All benchmarks:
===============

| Benchmark                | bm-20240509-linux-x86_64-python-35b5eaa176a5bae8a0ca-3.14.0a0-35b5eaa | bm-20240510-linux-x86_64-faster%2dcpython-test_perf_jit-3.14.0a0-1973514 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| scimark_sor              | 131 ms                                                                | 126 ms: 1.04x faster                                                     |
| deepcopy_reduce          | 3.31 us                                                               | 3.22 us: 1.03x faster                                                    |
| pycparser                | 1.20 sec                                                              | 1.17 sec: 1.02x faster                                                   |
| mdp                      | 2.63 sec                                                              | 2.58 sec: 1.02x faster                                                   |
| coroutines               | 23.6 ms                                                               | 23.2 ms: 1.02x faster                                                    |
| thrift                   | 819 us                                                                | 805 us: 1.02x faster                                                     |
| genshi_text              | 23.4 ms                                                               | 23.1 ms: 1.02x faster                                                    |
| regex_dna                | 223 ms                                                                | 220 ms: 1.01x faster                                                     |
| json_dumps               | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                                    |
| scimark_sparse_mat_mult  | 5.17 ms                                                               | 5.12 ms: 1.01x faster                                                    |
| spectral_norm            | 114 ms                                                                | 114 ms: 1.01x faster                                                     |
| coverage                 | 93.4 ms                                                               | 92.7 ms: 1.01x faster                                                    |
| logging_simple           | 5.68 us                                                               | 5.64 us: 1.01x faster                                                    |
| meteor_contest           | 110 ms                                                                | 109 ms: 1.01x faster                                                     |
| html5lib                 | 67.0 ms                                                               | 66.6 ms: 1.01x faster                                                    |
| genshi_xml               | 50.9 ms                                                               | 50.6 ms: 1.01x faster                                                    |
| json_loads               | 28.9 us                                                               | 28.8 us: 1.00x faster                                                    |
| asyncio_tcp_ssl          | 1.85 sec                                                              | 1.84 sec: 1.00x faster                                                   |
| deepcopy                 | 366 us                                                                | 364 us: 1.00x faster                                                     |
| comprehensions           | 16.5 us                                                               | 16.6 us: 1.00x slower                                                    |
| pickle_dict              | 33.9 us                                                               | 34.0 us: 1.00x slower                                                    |
| asyncio_tcp              | 505 ms                                                                | 506 ms: 1.00x slower                                                     |
| docutils                 | 2.80 sec                                                              | 2.81 sec: 1.00x slower                                                   |
| python_startup           | 10.4 ms                                                               | 10.4 ms: 1.00x slower                                                    |
| pickle_pure_python       | 305 us                                                                | 306 us: 1.00x slower                                                     |
| sqlglot_normalize        | 110 ms                                                                | 110 ms: 1.00x slower                                                     |
| dulwich_log              | 65.6 ms                                                               | 65.9 ms: 1.00x slower                                                    |
| chaos                    | 60.0 ms                                                               | 60.4 ms: 1.01x slower                                                    |
| richards_super           | 53.8 ms                                                               | 54.2 ms: 1.01x slower                                                    |
| pprint_safe_repr         | 766 ms                                                                | 771 ms: 1.01x slower                                                     |
| generators               | 29.4 ms                                                               | 29.6 ms: 1.01x slower                                                    |
| scimark_lu               | 116 ms                                                                | 117 ms: 1.01x slower                                                     |
| sqlglot_optimize         | 54.8 ms                                                               | 55.2 ms: 1.01x slower                                                    |
| tornado_http             | 93.7 ms                                                               | 94.5 ms: 1.01x slower                                                    |
| sqlglot_parse            | 1.29 ms                                                               | 1.31 ms: 1.01x slower                                                    |
| async_generators         | 448 ms                                                                | 452 ms: 1.01x slower                                                     |
| deltablue                | 3.24 ms                                                               | 3.27 ms: 1.01x slower                                                    |
| tomli_loads              | 2.06 sec                                                              | 2.08 sec: 1.01x slower                                                   |
| chameleon                | 6.87 ms                                                               | 6.94 ms: 1.01x slower                                                    |
| regex_compile            | 134 ms                                                                | 136 ms: 1.01x slower                                                     |
| nqueens                  | 81.0 ms                                                               | 81.9 ms: 1.01x slower                                                    |
| sqlglot_transpile        | 1.60 ms                                                               | 1.62 ms: 1.01x slower                                                    |
| typing_runtime_protocols | 165 us                                                                | 167 us: 1.01x slower                                                     |
| raytrace                 | 265 ms                                                                | 268 ms: 1.01x slower                                                     |
| scimark_fft              | 372 ms                                                                | 377 ms: 1.01x slower                                                     |
| regex_effbot             | 3.67 ms                                                               | 3.73 ms: 1.02x slower                                                    |
| nbody                    | 88.6 ms                                                               | 90.1 ms: 1.02x slower                                                    |
| json                     | 5.44 ms                                                               | 5.53 ms: 1.02x slower                                                    |
| crypto_pyaes             | 73.9 ms                                                               | 75.2 ms: 1.02x slower                                                    |
| unpickle_pure_python     | 217 us                                                                | 221 us: 1.02x slower                                                     |
| xml_etree_process        | 60.6 ms                                                               | 61.8 ms: 1.02x slower                                                    |
| unpickle                 | 15.9 us                                                               | 16.2 us: 1.02x slower                                                    |
| pyflate                  | 474 ms                                                                | 484 ms: 1.02x slower                                                     |
| xml_etree_generate       | 87.4 ms                                                               | 89.5 ms: 1.02x slower                                                    |
| fannkuch                 | 398 ms                                                                | 407 ms: 1.02x slower                                                     |
| hexiom                   | 6.11 ms                                                               | 6.29 ms: 1.03x slower                                                    |
| django_template          | 33.8 ms                                                               | 35.1 ms: 1.04x slower                                                    |
| regex_v8                 | 24.6 ms                                                               | 25.9 ms: 1.05x slower                                                    |
| gc_traversal             | 3.62 ms                                                               | 3.82 ms: 1.06x slower                                                    |
| mako                     | 10.6 ms                                                               | 11.3 ms: 1.07x slower                                                    |
| pickle_list              | 5.20 us                                                               | 5.63 us: 1.08x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.01x slower                                                             |

Benchmark hidden because not significant (37): flaskblogging, dask, async_tree_cpu_io_mixed_tg, richards, deepcopy_memo, bench_thread_pool, pickle, 2to3, logging_format, sympy_integrate, async_tree_cpu_io_mixed, pylint, sympy_sum, go, pidigits, pprint_pformat, async_tree_none_tg, float, pathlib, python_startup_no_site, create_gc_cycles, logging_silent, asyncio_websockets, sympy_str, xml_etree_iterparse, sqlite_synth, async_tree_none, telco, unpickle_list, bench_mp_pool, scimark_monte_carlo, xml_etree_parse, async_tree_io, sympy_expand, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg

# HPT report

- Reliability score: 99.57% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x