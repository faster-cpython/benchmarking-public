# Results vs. 3.13.0

- fork: zooba
- ref: gh_134923
- machine: windows-amd64
- commit hash: 25f01a3
- commit date: 2025-05-30
- overall geometric mean: 1.016x slower
- HPT reliability: 76.67%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250530-pythonperf1-amd64-zooba-gh_134923-3.15.0a0-25f01a3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 222 ms: 1.03x slower                                           |
| docutils       | 1.53 sec                                                    | 1.61 sec: 1.05x slower                                         |
| sphinx         | 617 ms                                                      | 637 ms: 1.03x slower                                           |
| Geometric mean | (ref)                                                       | 1.03x slower                                                   |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250530-pythonperf1-amd64-zooba-gh_134923-3.15.0a0-25f01a3 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 158 ms: 1.90x faster                                           |
| async_tree_memoization_tg  | 281 ms                                                      | 207 ms: 1.35x faster                                           |
| async_tree_memoization     | 265 ms                                                      | 204 ms: 1.30x faster                                           |
| async_tree_io              | 513 ms                                                      | 395 ms: 1.30x faster                                           |
| async_tree_none            | 219 ms                                                      | 170 ms: 1.29x faster                                           |
| async_tree_io_tg           | 497 ms                                                      | 389 ms: 1.28x faster                                           |
| async_tree_none_tg         | 200 ms                                                      | 170 ms: 1.18x faster                                           |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 329 ms: 1.16x faster                                           |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 340 ms: 1.12x faster                                           |
| async_generators           | 223 ms                                                      | 232 ms: 1.04x slower                                           |
| coroutines                 | 12.5 ms                                                     | 13.8 ms: 1.10x slower                                          |
| Geometric mean             | (ref)                                                       | 1.23x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250530-pythonperf1-amd64-zooba-gh_134923-3.15.0a0-25f01a3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 44.8 ms: 1.13x faster                                          |
| nbody          | 66.3 ms                                                     | 62.6 ms: 1.06x faster                                          |
| pidigits       | 146 ms                                                      | 148 ms: 1.01x slower                                           |
| Geometric mean | (ref)                                                       | 1.06x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250530-pythonperf1-amd64-zooba-gh_134923-3.15.0a0-25f01a3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.0 ms: 1.70x faster                                          |
| regex_effbot   | 1.69 ms                                                     | 1.57 ms: 1.08x faster                                          |
| regex_compile  | 80.7 ms                                                     | 78.7 ms: 1.03x faster                                          |
| regex_dna      | 115 ms                                                      | 121 ms: 1.05x slower                                           |
| Geometric mean | (ref)                                                       | 1.16x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250530-pythonperf1-amd64-zooba-gh_134923-3.15.0a0-25f01a3 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 89.0 ms: 1.04x faster                                          |
| tomli_loads          | 1.37 sec                                                    | 1.33 sec: 1.03x faster                                         |
| unpickle_pure_python | 130 us                                                      | 133 us: 1.03x slower                                           |
| xml_etree_iterparse  | 60.5 ms                                                     | 62.9 ms: 1.04x slower                                          |
| xml_etree_generate   | 53.5 ms                                                     | 55.9 ms: 1.05x slower                                          |
| xml_etree_process    | 36.5 ms                                                     | 38.8 ms: 1.06x slower                                          |
| pickle_pure_python   | 186 us                                                      | 215 us: 1.15x slower                                           |
| Geometric mean       | (ref)                                                       | 1.03x slower                                                   |

Benchmark hidden because not significant (2): json_loads, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250530-pythonperf1-amd64-zooba-gh_134923-3.15.0a0-25f01a3 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.9 ms: 1.06x slower                                          |
| python_startup_no_site | 16.9 ms                                                     | 19.2 ms: 1.14x slower                                          |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250530-pythonperf1-amd64-zooba-gh_134923-3.15.0a0-25f01a3 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------:|
| genshi_text     | 15.2 ms                                                     | 15.1 ms: 1.01x faster                                          |
| django_template | 20.3 ms                                                     | 24.4 ms: 1.20x slower                                          |
| Geometric mean  | (ref)                                                       | 1.04x slower                                                   |

Benchmark hidden because not significant (2): genshi_xml, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250530-pythonperf1-amd64-zooba-gh_134923-3.15.0a0-25f01a3 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 31.8 ms: 2.37x faster                                          |
| asyncio_websockets         | 300 ms                                                      | 158 ms: 1.90x faster                                           |
| mdp                        | 1.43 sec                                                    | 788 ms: 1.82x faster                                           |
| regex_v8                   | 23.8 ms                                                     | 14.0 ms: 1.70x faster                                          |
| async_tree_memoization_tg  | 281 ms                                                      | 207 ms: 1.35x faster                                           |
| async_tree_memoization     | 265 ms                                                      | 204 ms: 1.30x faster                                           |
| deepcopy                   | 223 us                                                      | 172 us: 1.30x faster                                           |
| async_tree_io              | 513 ms                                                      | 395 ms: 1.30x faster                                           |
| async_tree_none            | 219 ms                                                      | 170 ms: 1.29x faster                                           |
| async_tree_io_tg           | 497 ms                                                      | 389 ms: 1.28x faster                                           |
| deepcopy_memo              | 23.1 us                                                     | 18.1 us: 1.27x faster                                          |
| async_tree_none_tg         | 200 ms                                                      | 170 ms: 1.18x faster                                           |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 329 ms: 1.16x faster                                           |
| go                         | 84.7 ms                                                     | 74.2 ms: 1.14x faster                                          |
| spectral_norm              | 63.4 ms                                                     | 55.7 ms: 1.14x faster                                          |
| float                      | 50.8 ms                                                     | 44.8 ms: 1.13x faster                                          |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 340 ms: 1.12x faster                                           |
| deepcopy_reduce            | 2.02 us                                                     | 1.87 us: 1.08x faster                                          |
| regex_effbot               | 1.69 ms                                                     | 1.57 ms: 1.08x faster                                          |
| telco                      | 4.85 ms                                                     | 4.55 ms: 1.07x faster                                          |
| nbody                      | 66.3 ms                                                     | 62.6 ms: 1.06x faster                                          |
| json                       | 3.30 ms                                                     | 3.16 ms: 1.05x faster                                          |
| scimark_monte_carlo        | 40.7 ms                                                     | 39.2 ms: 1.04x faster                                          |
| xml_etree_parse            | 92.2 ms                                                     | 89.0 ms: 1.04x faster                                          |
| tomli_loads                | 1.37 sec                                                    | 1.33 sec: 1.03x faster                                         |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.53 ms: 1.03x faster                                          |
| regex_compile              | 80.7 ms                                                     | 78.7 ms: 1.03x faster                                          |
| typing_runtime_protocols   | 103 us                                                      | 101 us: 1.02x faster                                           |
| meteor_contest             | 72.0 ms                                                     | 70.4 ms: 1.02x faster                                          |
| fannkuch                   | 252 ms                                                      | 247 ms: 1.02x faster                                           |
| scimark_sor                | 76.2 ms                                                     | 74.7 ms: 1.02x faster                                          |
| sympy_integrate            | 12.3 ms                                                     | 12.2 ms: 1.01x faster                                          |
| bpe_tokeniser              | 2.87 sec                                                    | 2.85 sec: 1.01x faster                                         |
| genshi_text                | 15.2 ms                                                     | 15.1 ms: 1.01x faster                                          |
| scimark_fft                | 175 ms                                                      | 174 ms: 1.01x faster                                           |
| sympy_expand               | 286 ms                                                      | 288 ms: 1.01x slower                                           |
| pidigits                   | 146 ms                                                      | 148 ms: 1.01x slower                                           |
| comprehensions             | 10.4 us                                                     | 10.5 us: 1.01x slower                                          |
| crypto_pyaes               | 45.6 ms                                                     | 46.1 ms: 1.01x slower                                          |
| shortest_path              | 355 ms                                                      | 360 ms: 1.01x slower                                           |
| richards                   | 26.3 ms                                                     | 26.7 ms: 1.02x slower                                          |
| scimark_lu                 | 56.7 ms                                                     | 57.7 ms: 1.02x slower                                          |
| dulwich_log                | 40.1 ms                                                     | 40.9 ms: 1.02x slower                                          |
| generators                 | 19.0 ms                                                     | 19.4 ms: 1.02x slower                                          |
| sympy_sum                  | 85.2 ms                                                     | 86.9 ms: 1.02x slower                                          |
| hexiom                     | 3.84 ms                                                     | 3.93 ms: 1.02x slower                                          |
| richards_super             | 29.8 ms                                                     | 30.5 ms: 1.02x slower                                          |
| unpickle_pure_python       | 130 us                                                      | 133 us: 1.03x slower                                           |
| 2to3                       | 215 ms                                                      | 222 ms: 1.03x slower                                           |
| sphinx                     | 617 ms                                                      | 637 ms: 1.03x slower                                           |
| connected_components       | 320 ms                                                      | 330 ms: 1.03x slower                                           |
| chaos                      | 37.9 ms                                                     | 39.1 ms: 1.03x slower                                          |
| bench_thread_pool          | 810 us                                                      | 842 us: 1.04x slower                                           |
| xml_etree_iterparse        | 60.5 ms                                                     | 62.9 ms: 1.04x slower                                          |
| async_generators           | 223 ms                                                      | 232 ms: 1.04x slower                                           |
| xml_etree_generate         | 53.5 ms                                                     | 55.9 ms: 1.05x slower                                          |
| docutils                   | 1.53 sec                                                    | 1.61 sec: 1.05x slower                                         |
| regex_dna                  | 115 ms                                                      | 121 ms: 1.05x slower                                           |
| python_startup             | 24.4 ms                                                     | 25.9 ms: 1.06x slower                                          |
| xml_etree_process          | 36.5 ms                                                     | 38.8 ms: 1.06x slower                                          |
| create_gc_cycles           | 1.22 ms                                                     | 1.31 ms: 1.07x slower                                          |
| logging_simple             | 5.77 us                                                     | 6.20 us: 1.07x slower                                          |
| logging_format             | 6.18 us                                                     | 6.69 us: 1.08x slower                                          |
| gc_traversal               | 1.96 ms                                                     | 2.13 ms: 1.08x slower                                          |
| nqueens                    | 56.1 ms                                                     | 61.2 ms: 1.09x slower                                          |
| coroutines                 | 12.5 ms                                                     | 13.8 ms: 1.10x slower                                          |
| bench_mp_pool              | 84.2 ms                                                     | 94.1 ms: 1.12x slower                                          |
| deltablue                  | 1.89 ms                                                     | 2.14 ms: 1.13x slower                                          |
| pprint_safe_repr           | 485 ms                                                      | 549 ms: 1.13x slower                                           |
| python_startup_no_site     | 16.9 ms                                                     | 19.2 ms: 1.14x slower                                          |
| pprint_pformat             | 977 ms                                                      | 1.12 sec: 1.15x slower                                         |
| pickle_pure_python         | 186 us                                                      | 215 us: 1.15x slower                                           |
| many_optionals             | 361 us                                                      | 433 us: 1.20x slower                                           |
| django_template            | 20.3 ms                                                     | 24.4 ms: 1.20x slower                                          |
| raytrace                   | 153 ms                                                      | 185 ms: 1.20x slower                                           |
| subparsers                 | 10.9 ms                                                     | 17.1 ms: 1.57x slower                                          |
| logging_silent             | 54.6 ns                                                     | 317 ns: 5.81x slower                                           |
| coverage                   | 45.3 ms                                                     | 293 ms: 6.47x slower                                           |
| thrift                     | 8.47 ms                                                     | 93.1 ms: 10.99x slower                                         |
| Geometric mean             | (ref)                                                       | 1.03x slower                                                   |

Benchmark hidden because not significant (11): pylint, genshi_xml, mako, json_loads, sqlite_synth, json_dumps, sympy_str, pyflate, pycparser, k_core, html5lib
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250530-3.15.0a0-25f01a3/bm-20250530-pythonperf1-amd64-zooba-gh_134923-3.15.0a0-25f01a3.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.016x slower

# HPT report

- Reliability score: 76.67% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown