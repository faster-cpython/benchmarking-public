# Results vs. base

- fork: faster-cpython
- ref: deferred_rc_overhead
- machine: linux-x86_64
- commit hash: f748355
- commit date: 2024-05-31
- overall geometric mean: 1.00x faster
- HPT reliability: 96.72%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240529-linux-x86_64-python-1f481fd3275dbc12a88c-3.14.0a0-1f481fd | bm-20240531-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-f748355 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 268 ms                                                                | 270 ms: 1.01x slower                                                            |
| html5lib       | 68.2 ms                                                               | 67.4 ms: 1.01x faster                                                           |
| tornado_http   | 93.4 ms                                                               | 93.9 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_io, async_tree_none, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240529-linux-x86_64-python-1f481fd3275dbc12a88c-3.14.0a0-1f481fd | bm-20240531-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-f748355 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.2 ms                                                               | 79.5 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240529-linux-x86_64-python-1f481fd3275dbc12a88c-3.14.0a0-1f481fd | bm-20240531-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-f748355 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 3.70 ms                                                               | 3.62 ms: 1.02x faster                                                           |
| regex_dna      | 232 ms                                                                | 228 ms: 1.02x faster                                                            |
| regex_compile  | 135 ms                                                                | 134 ms: 1.00x faster                                                            |
| regex_v8       | 24.4 ms                                                               | 26.0 ms: 1.06x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240529-linux-x86_64-python-1f481fd3275dbc12a88c-3.14.0a0-1f481fd | bm-20240531-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-f748355 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_process    | 61.6 ms                                                               | 60.3 ms: 1.02x faster                                                           |
| xml_etree_generate   | 88.6 ms                                                               | 87.1 ms: 1.02x faster                                                           |
| unpickle_list        | 5.50 us                                                               | 5.41 us: 1.02x faster                                                           |
| json_dumps           | 10.7 ms                                                               | 10.6 ms: 1.01x faster                                                           |
| pickle_dict          | 36.3 us                                                               | 35.9 us: 1.01x faster                                                           |
| json_loads           | 29.0 us                                                               | 28.8 us: 1.01x faster                                                           |
| pickle               | 12.1 us                                                               | 12.0 us: 1.01x faster                                                           |
| pickle_pure_python   | 305 us                                                                | 303 us: 1.01x faster                                                            |
| unpickle_pure_python | 216 us                                                                | 218 us: 1.01x slower                                                            |
| tomli_loads          | 2.15 sec                                                              | 2.18 sec: 1.01x slower                                                          |
| pickle_list          | 5.18 us                                                               | 5.30 us: 1.02x slower                                                           |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_iterparse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240529-linux-x86_64-python-1f481fd3275dbc12a88c-3.14.0a0-1f481fd | bm-20240531-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-f748355 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                                           |
| python_startup_no_site | 7.12 ms                                                               | 7.07 ms: 1.01x faster                                                           |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240529-linux-x86_64-python-1f481fd3275dbc12a88c-3.14.0a0-1f481fd | bm-20240531-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-f748355 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 23.9 ms                                                               | 23.3 ms: 1.03x faster                                                           |
| genshi_xml      | 51.4 ms                                                               | 50.6 ms: 1.02x faster                                                           |
| django_template | 35.1 ms                                                               | 35.3 ms: 1.01x slower                                                           |
| mako            | 11.2 ms                                                               | 11.7 ms: 1.04x slower                                                           |
| Geometric mean  | (ref)                                                                 | 1.00x slower                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20240529-linux-x86_64-python-1f481fd3275dbc12a88c-3.14.0a0-1f481fd | bm-20240531-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-f748355 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| gc_traversal             | 3.97 ms                                                               | 3.59 ms: 1.11x faster                                                           |
| mdp                      | 2.79 sec                                                              | 2.58 sec: 1.08x faster                                                          |
| coroutines               | 23.9 ms                                                               | 22.6 ms: 1.06x faster                                                           |
| generators               | 29.3 ms                                                               | 27.8 ms: 1.05x faster                                                           |
| pyflate                  | 486 ms                                                                | 467 ms: 1.04x faster                                                            |
| logging_silent           | 100 ns                                                                | 97.2 ns: 1.03x faster                                                           |
| typing_runtime_protocols | 170 us                                                                | 165 us: 1.03x faster                                                            |
| genshi_text              | 23.9 ms                                                               | 23.3 ms: 1.03x faster                                                           |
| regex_effbot             | 3.70 ms                                                               | 3.62 ms: 1.02x faster                                                           |
| xml_etree_process        | 61.6 ms                                                               | 60.3 ms: 1.02x faster                                                           |
| regex_dna                | 232 ms                                                                | 228 ms: 1.02x faster                                                            |
| genshi_xml               | 51.4 ms                                                               | 50.6 ms: 1.02x faster                                                           |
| thrift                   | 814 us                                                                | 801 us: 1.02x faster                                                            |
| xml_etree_generate       | 88.6 ms                                                               | 87.1 ms: 1.02x faster                                                           |
| unpickle_list            | 5.50 us                                                               | 5.41 us: 1.02x faster                                                           |
| html5lib                 | 68.2 ms                                                               | 67.4 ms: 1.01x faster                                                           |
| json_dumps               | 10.7 ms                                                               | 10.6 ms: 1.01x faster                                                           |
| deepcopy_memo            | 39.7 us                                                               | 39.3 us: 1.01x faster                                                           |
| pickle_dict              | 36.3 us                                                               | 35.9 us: 1.01x faster                                                           |
| json_loads               | 29.0 us                                                               | 28.8 us: 1.01x faster                                                           |
| python_startup           | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                                           |
| pickle                   | 12.1 us                                                               | 12.0 us: 1.01x faster                                                           |
| python_startup_no_site   | 7.12 ms                                                               | 7.07 ms: 1.01x faster                                                           |
| pickle_pure_python       | 305 us                                                                | 303 us: 1.01x faster                                                            |
| asyncio_tcp_ssl          | 1.85 sec                                                              | 1.84 sec: 1.01x faster                                                          |
| coverage                 | 92.7 ms                                                               | 92.3 ms: 1.00x faster                                                           |
| regex_compile            | 135 ms                                                                | 134 ms: 1.00x faster                                                            |
| sympy_integrate          | 20.3 ms                                                               | 20.4 ms: 1.00x slower                                                           |
| tornado_http             | 93.4 ms                                                               | 93.9 ms: 1.01x slower                                                           |
| comprehensions           | 16.8 us                                                               | 16.8 us: 1.01x slower                                                           |
| logging_format           | 6.27 us                                                               | 6.31 us: 1.01x slower                                                           |
| sqlglot_parse            | 1.31 ms                                                               | 1.32 ms: 1.01x slower                                                           |
| sqlglot_transpile        | 1.61 ms                                                               | 1.62 ms: 1.01x slower                                                           |
| chaos                    | 60.5 ms                                                               | 60.9 ms: 1.01x slower                                                           |
| django_template          | 35.1 ms                                                               | 35.3 ms: 1.01x slower                                                           |
| raytrace                 | 263 ms                                                                | 265 ms: 1.01x slower                                                            |
| sqlglot_optimize         | 54.7 ms                                                               | 55.1 ms: 1.01x slower                                                           |
| deepcopy_reduce          | 3.29 us                                                               | 3.31 us: 1.01x slower                                                           |
| bench_thread_pool        | 824 us                                                                | 830 us: 1.01x slower                                                            |
| 2to3                     | 268 ms                                                                | 270 ms: 1.01x slower                                                            |
| dulwich_log              | 65.2 ms                                                               | 65.8 ms: 1.01x slower                                                           |
| unpickle_pure_python     | 216 us                                                                | 218 us: 1.01x slower                                                            |
| richards                 | 48.5 ms                                                               | 49.1 ms: 1.01x slower                                                           |
| deltablue                | 3.23 ms                                                               | 3.27 ms: 1.01x slower                                                           |
| hexiom                   | 6.13 ms                                                               | 6.21 ms: 1.01x slower                                                           |
| sqlglot_normalize        | 109 ms                                                                | 110 ms: 1.01x slower                                                            |
| tomli_loads              | 2.15 sec                                                              | 2.18 sec: 1.01x slower                                                          |
| pprint_pformat           | 1.52 sec                                                              | 1.54 sec: 1.01x slower                                                          |
| meteor_contest           | 109 ms                                                                | 111 ms: 1.02x slower                                                            |
| asyncio_tcp              | 497 ms                                                                | 505 ms: 1.02x slower                                                            |
| scimark_monte_carlo      | 69.0 ms                                                               | 70.1 ms: 1.02x slower                                                           |
| pprint_safe_repr         | 740 ms                                                                | 752 ms: 1.02x slower                                                            |
| float                    | 78.2 ms                                                               | 79.5 ms: 1.02x slower                                                           |
| scimark_sor              | 123 ms                                                                | 126 ms: 1.02x slower                                                            |
| async_generators         | 439 ms                                                                | 447 ms: 1.02x slower                                                            |
| richards_super           | 54.2 ms                                                               | 55.2 ms: 1.02x slower                                                           |
| go                       | 143 ms                                                                | 146 ms: 1.02x slower                                                            |
| crypto_pyaes             | 74.3 ms                                                               | 75.9 ms: 1.02x slower                                                           |
| pickle_list              | 5.18 us                                                               | 5.30 us: 1.02x slower                                                           |
| spectral_norm            | 113 ms                                                                | 116 ms: 1.03x slower                                                            |
| fannkuch                 | 393 ms                                                                | 406 ms: 1.03x slower                                                            |
| nqueens                  | 79.7 ms                                                               | 82.4 ms: 1.03x slower                                                           |
| mako                     | 11.2 ms                                                               | 11.7 ms: 1.04x slower                                                           |
| pycparser                | 1.16 sec                                                              | 1.21 sec: 1.05x slower                                                          |
| regex_v8                 | 24.4 ms                                                               | 26.0 ms: 1.06x slower                                                           |
| Geometric mean           | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (30): async_tree_io_tg, xml_etree_parse, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, xml_etree_iterparse, scimark_sparse_mat_mult, sympy_expand, deepcopy, telco, logging_simple, async_tree_none_tg, json, create_gc_cycles, scimark_fft, sympy_sum, asyncio_websockets, pidigits, bench_mp_pool, pylint, pathlib, scimark_lu, sqlite_synth, docutils, async_tree_cpu_io_mixed, nbody, async_tree_io, sympy_str, unpickle, async_tree_none, async_tree_memoization
Ignored benchmarks (1) of results/bm-20240529-3.14.0a0-1f481fd/bm-20240529-linux-x86_64-python-1f481fd3275dbc12a88c-3.14.0a0-1f481fd.json: dask

# HPT report

- Reliability score: 96.72% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x