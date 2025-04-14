# Results vs. 3.13.0

- fork: zooba
- ref: gh_91349
- machine: windows-amd64
- commit hash: 548daa7
- commit date: 2025-03-19
- overall geometric mean: 1.001x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-pythonperf1-amd64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 230 ms: 1.07x slower                                           |
| docutils       | 1.53 sec                                                    | 1.71 sec: 1.12x slower                                         |
| html5lib       | 38.2 ms                                                     | 41.8 ms: 1.10x slower                                          |
| sphinx         | 617 ms                                                      | 673 ms: 1.09x slower                                           |
| Geometric mean | (ref)                                                       | 1.09x slower                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-pythonperf1-amd64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 156 ms: 1.93x faster                                           |
| async_tree_memoization_tg  | 281 ms                                                      | 218 ms: 1.29x faster                                           |
| async_tree_io              | 513 ms                                                      | 430 ms: 1.19x faster                                           |
| async_tree_io_tg           | 497 ms                                                      | 418 ms: 1.19x faster                                           |
| async_tree_memoization     | 265 ms                                                      | 224 ms: 1.18x faster                                           |
| async_tree_none            | 219 ms                                                      | 192 ms: 1.14x faster                                           |
| async_tree_none_tg         | 200 ms                                                      | 180 ms: 1.11x faster                                           |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 346 ms: 1.11x faster                                           |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 347 ms: 1.10x faster                                           |
| async_generators           | 223 ms                                                      | 232 ms: 1.04x slower                                           |
| coroutines                 | 12.5 ms                                                     | 13.5 ms: 1.08x slower                                          |
| Geometric mean             | (ref)                                                       | 1.17x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-pythonperf1-amd64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 46.8 ms: 1.09x faster                                          |
| pidigits       | 146 ms                                                      | 149 ms: 1.02x slower                                           |
| nbody          | 66.3 ms                                                     | 72.9 ms: 1.10x slower                                          |
| Geometric mean | (ref)                                                       | 1.01x slower                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-pythonperf1-amd64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.9 ms: 1.71x faster                                          |
| regex_effbot   | 1.69 ms                                                     | 1.44 ms: 1.18x faster                                          |
| regex_dna      | 115 ms                                                      | 117 ms: 1.02x slower                                           |
| regex_compile  | 80.7 ms                                                     | 89.0 ms: 1.10x slower                                          |
| Geometric mean | (ref)                                                       | 1.16x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-pythonperf1-amd64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 90.3 ms: 1.02x faster                                          |
| json_loads           | 15.1 us                                                     | 15.4 us: 1.02x slower                                          |
| xml_etree_iterparse  | 60.5 ms                                                     | 65.3 ms: 1.08x slower                                          |
| tomli_loads          | 1.37 sec                                                    | 1.49 sec: 1.09x slower                                         |
| xml_etree_generate   | 53.5 ms                                                     | 58.9 ms: 1.10x slower                                          |
| json_dumps           | 6.19 ms                                                     | 6.99 ms: 1.13x slower                                          |
| xml_etree_process    | 36.5 ms                                                     | 42.3 ms: 1.16x slower                                          |
| unpickle_pure_python | 130 us                                                      | 152 us: 1.17x slower                                           |
| pickle_pure_python   | 186 us                                                      | 236 us: 1.27x slower                                           |
| Geometric mean       | (ref)                                                       | 1.11x slower                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-pythonperf1-amd64-zooba-gh_91349-3.14.0a6+-548daa7 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.4 ms: 1.08x slower                                          |
| python_startup_no_site | 16.9 ms                                                     | 20.4 ms: 1.21x slower                                          |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-pythonperf1-amd64-zooba-gh_91349-3.14.0a6+-548daa7 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.86 ms: 1.05x slower                                          |
| genshi_xml      | 33.9 ms                                                     | 38.1 ms: 1.12x slower                                          |
| genshi_text     | 15.2 ms                                                     | 17.3 ms: 1.14x slower                                          |
| django_template | 20.3 ms                                                     | 26.7 ms: 1.31x slower                                          |
| Geometric mean  | (ref)                                                       | 1.15x slower                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250319-pythonperf1-amd64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 541 us: 15.66x faster                                          |
| pathlib                    | 75.3 ms                                                     | 32.8 ms: 2.29x faster                                          |
| asyncio_websockets         | 300 ms                                                      | 156 ms: 1.93x faster                                           |
| regex_v8                   | 23.8 ms                                                     | 13.9 ms: 1.71x faster                                          |
| async_tree_memoization_tg  | 281 ms                                                      | 218 ms: 1.29x faster                                           |
| deepcopy                   | 223 us                                                      | 187 us: 1.20x faster                                           |
| async_tree_io              | 513 ms                                                      | 430 ms: 1.19x faster                                           |
| async_tree_io_tg           | 497 ms                                                      | 418 ms: 1.19x faster                                           |
| async_tree_memoization     | 265 ms                                                      | 224 ms: 1.18x faster                                           |
| regex_effbot               | 1.69 ms                                                     | 1.44 ms: 1.18x faster                                          |
| deepcopy_memo              | 23.1 us                                                     | 19.7 us: 1.17x faster                                          |
| async_tree_none            | 219 ms                                                      | 192 ms: 1.14x faster                                           |
| async_tree_none_tg         | 200 ms                                                      | 180 ms: 1.11x faster                                           |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 346 ms: 1.11x faster                                           |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 347 ms: 1.10x faster                                           |
| spectral_norm              | 63.4 ms                                                     | 57.9 ms: 1.10x faster                                          |
| float                      | 50.8 ms                                                     | 46.8 ms: 1.09x faster                                          |
| json                       | 3.30 ms                                                     | 3.11 ms: 1.06x faster                                          |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.55 ms: 1.02x faster                                          |
| xml_etree_parse            | 92.2 ms                                                     | 90.3 ms: 1.02x faster                                          |
| deepcopy_reduce            | 2.02 us                                                     | 2.00 us: 1.01x faster                                          |
| json_loads                 | 15.1 us                                                     | 15.4 us: 1.02x slower                                          |
| generators                 | 19.0 ms                                                     | 19.3 ms: 1.02x slower                                          |
| regex_dna                  | 115 ms                                                      | 117 ms: 1.02x slower                                           |
| pidigits                   | 146 ms                                                      | 149 ms: 1.02x slower                                           |
| shortest_path              | 355 ms                                                      | 364 ms: 1.03x slower                                           |
| telco                      | 4.85 ms                                                     | 5.03 ms: 1.04x slower                                          |
| async_generators           | 223 ms                                                      | 232 ms: 1.04x slower                                           |
| k_core                     | 1.70 sec                                                    | 1.77 sec: 1.04x slower                                         |
| mako                       | 6.56 ms                                                     | 6.86 ms: 1.05x slower                                          |
| gc_traversal               | 1.96 ms                                                     | 2.08 ms: 1.06x slower                                          |
| bench_mp_pool              | 84.2 ms                                                     | 89.3 ms: 1.06x slower                                          |
| connected_components       | 320 ms                                                      | 341 ms: 1.07x slower                                           |
| bpe_tokeniser              | 2.87 sec                                                    | 3.06 sec: 1.07x slower                                         |
| 2to3                       | 215 ms                                                      | 230 ms: 1.07x slower                                           |
| go                         | 84.7 ms                                                     | 90.4 ms: 1.07x slower                                          |
| scimark_fft                | 175 ms                                                      | 187 ms: 1.07x slower                                           |
| sympy_sum                  | 85.2 ms                                                     | 91.1 ms: 1.07x slower                                          |
| bench_thread_pool          | 810 us                                                      | 869 us: 1.07x slower                                           |
| mdp                        | 1.43 sec                                                    | 1.54 sec: 1.07x slower                                         |
| dulwich_log                | 40.1 ms                                                     | 43.1 ms: 1.07x slower                                          |
| sympy_str                  | 167 ms                                                      | 179 ms: 1.07x slower                                           |
| scimark_monte_carlo        | 40.7 ms                                                     | 43.9 ms: 1.08x slower                                          |
| sympy_expand               | 286 ms                                                      | 308 ms: 1.08x slower                                           |
| coroutines                 | 12.5 ms                                                     | 13.5 ms: 1.08x slower                                          |
| xml_etree_iterparse        | 60.5 ms                                                     | 65.3 ms: 1.08x slower                                          |
| meteor_contest             | 72.0 ms                                                     | 77.8 ms: 1.08x slower                                          |
| scimark_lu                 | 56.7 ms                                                     | 61.4 ms: 1.08x slower                                          |
| coverage                   | 45.3 ms                                                     | 49.1 ms: 1.08x slower                                          |
| logging_silent             | 54.6 ns                                                     | 59.2 ns: 1.08x slower                                          |
| python_startup             | 24.4 ms                                                     | 26.4 ms: 1.08x slower                                          |
| sympy_integrate            | 12.3 ms                                                     | 13.4 ms: 1.09x slower                                          |
| tomli_loads                | 1.37 sec                                                    | 1.49 sec: 1.09x slower                                         |
| sphinx                     | 617 ms                                                      | 673 ms: 1.09x slower                                           |
| fannkuch                   | 252 ms                                                      | 275 ms: 1.09x slower                                           |
| html5lib                   | 38.2 ms                                                     | 41.8 ms: 1.10x slower                                          |
| crypto_pyaes               | 45.6 ms                                                     | 49.9 ms: 1.10x slower                                          |
| nbody                      | 66.3 ms                                                     | 72.9 ms: 1.10x slower                                          |
| pycparser                  | 695 ms                                                      | 765 ms: 1.10x slower                                           |
| regex_compile              | 80.7 ms                                                     | 89.0 ms: 1.10x slower                                          |
| typing_runtime_protocols   | 103 us                                                      | 114 us: 1.10x slower                                           |
| xml_etree_generate         | 53.5 ms                                                     | 58.9 ms: 1.10x slower                                          |
| scimark_sor                | 76.2 ms                                                     | 84.7 ms: 1.11x slower                                          |
| docutils                   | 1.53 sec                                                    | 1.71 sec: 1.12x slower                                         |
| genshi_xml                 | 33.9 ms                                                     | 38.1 ms: 1.12x slower                                          |
| json_dumps                 | 6.19 ms                                                     | 6.99 ms: 1.13x slower                                          |
| pprint_safe_repr           | 485 ms                                                      | 548 ms: 1.13x slower                                           |
| pyflate                    | 283 ms                                                      | 321 ms: 1.13x slower                                           |
| genshi_text                | 15.2 ms                                                     | 17.3 ms: 1.14x slower                                          |
| richards_super             | 29.8 ms                                                     | 33.9 ms: 1.14x slower                                          |
| pprint_pformat             | 977 ms                                                      | 1.11 sec: 1.14x slower                                         |
| logging_simple             | 5.77 us                                                     | 6.66 us: 1.15x slower                                          |
| xml_etree_process          | 36.5 ms                                                     | 42.3 ms: 1.16x slower                                          |
| hexiom                     | 3.84 ms                                                     | 4.48 ms: 1.17x slower                                          |
| logging_format             | 6.18 us                                                     | 7.22 us: 1.17x slower                                          |
| comprehensions             | 10.4 us                                                     | 12.1 us: 1.17x slower                                          |
| richards                   | 26.3 ms                                                     | 30.8 ms: 1.17x slower                                          |
| chaos                      | 37.9 ms                                                     | 44.4 ms: 1.17x slower                                          |
| unpickle_pure_python       | 130 us                                                      | 152 us: 1.17x slower                                           |
| deltablue                  | 1.89 ms                                                     | 2.28 ms: 1.20x slower                                          |
| nqueens                    | 56.1 ms                                                     | 67.8 ms: 1.21x slower                                          |
| python_startup_no_site     | 16.9 ms                                                     | 20.4 ms: 1.21x slower                                          |
| many_optionals             | 361 us                                                      | 442 us: 1.22x slower                                           |
| pickle_pure_python         | 186 us                                                      | 236 us: 1.27x slower                                           |
| django_template            | 20.3 ms                                                     | 26.7 ms: 1.31x slower                                          |
| raytrace                   | 153 ms                                                      | 204 ms: 1.33x slower                                           |
| subparsers                 | 10.9 ms                                                     | 16.8 ms: 1.55x slower                                          |
| Geometric mean             | (ref)                                                       | 1.00x slower                                                   |

Benchmark hidden because not significant (3): pylint, create_gc_cycles, sqlite_synth
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250319-3.14.0a6+-548daa7/bm-20250319-pythonperf1-amd64-zooba-gh_91349-3.14.0a6+-548daa7.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown