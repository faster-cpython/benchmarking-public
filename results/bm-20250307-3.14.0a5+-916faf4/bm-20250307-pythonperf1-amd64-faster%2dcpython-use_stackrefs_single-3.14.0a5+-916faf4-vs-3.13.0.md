# Results vs. 3.13.0

- fork: faster-cpython
- ref: use_stackrefs_single
- machine: windows-amd64
- commit hash: 916faf4
- commit date: 2025-03-07
- overall geometric mean: 1.001x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-pythonperf1-amd64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 228 ms: 1.06x slower                                                                  |
| docutils       | 1.53 sec                                                    | 1.69 sec: 1.11x slower                                                                |
| html5lib       | 38.2 ms                                                     | 41.3 ms: 1.08x slower                                                                 |
| sphinx         | 617 ms                                                      | 655 ms: 1.06x slower                                                                  |
| Geometric mean | (ref)                                                       | 1.08x slower                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-pythonperf1-amd64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 217 ms: 1.29x faster                                                                  |
| async_tree_memoization     | 265 ms                                                      | 220 ms: 1.21x faster                                                                  |
| async_tree_io              | 513 ms                                                      | 426 ms: 1.20x faster                                                                  |
| async_tree_io_tg           | 497 ms                                                      | 416 ms: 1.20x faster                                                                  |
| async_tree_none            | 219 ms                                                      | 190 ms: 1.15x faster                                                                  |
| async_tree_none_tg         | 200 ms                                                      | 179 ms: 1.12x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 346 ms: 1.11x faster                                                                  |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 344 ms: 1.11x faster                                                                  |
| async_generators           | 223 ms                                                      | 228 ms: 1.02x slower                                                                  |
| asyncio_websockets         | 300 ms                                                      | 315 ms: 1.05x slower                                                                  |
| coroutines                 | 12.5 ms                                                     | 13.6 ms: 1.09x slower                                                                 |
| Geometric mean             | (ref)                                                       | 1.11x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-pythonperf1-amd64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 47.0 ms: 1.08x faster                                                                 |
| pidigits       | 146 ms                                                      | 152 ms: 1.04x slower                                                                  |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-pythonperf1-amd64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.6 ms: 1.63x faster                                                                 |
| regex_effbot   | 1.69 ms                                                     | 1.42 ms: 1.19x faster                                                                 |
| regex_dna      | 115 ms                                                      | 114 ms: 1.01x faster                                                                  |
| regex_compile  | 80.7 ms                                                     | 86.2 ms: 1.07x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-pythonperf1-amd64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.42 sec: 1.04x slower                                                                |
| xml_etree_generate   | 53.5 ms                                                     | 58.3 ms: 1.09x slower                                                                 |
| xml_etree_iterparse  | 60.5 ms                                                     | 66.1 ms: 1.09x slower                                                                 |
| json_dumps           | 6.19 ms                                                     | 6.95 ms: 1.12x slower                                                                 |
| unpickle_pure_python | 130 us                                                      | 148 us: 1.14x slower                                                                  |
| xml_etree_process    | 36.5 ms                                                     | 41.7 ms: 1.14x slower                                                                 |
| pickle_pure_python   | 186 us                                                      | 227 us: 1.22x slower                                                                  |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                                          |

Benchmark hidden because not significant (2): xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-pythonperf1-amd64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.1 ms: 1.07x slower                                                                 |
| python_startup_no_site | 16.9 ms                                                     | 19.7 ms: 1.16x slower                                                                 |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-pythonperf1-amd64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 7.04 ms: 1.07x slower                                                                 |
| genshi_xml      | 33.9 ms                                                     | 37.1 ms: 1.10x slower                                                                 |
| genshi_text     | 15.2 ms                                                     | 16.9 ms: 1.11x slower                                                                 |
| django_template | 20.3 ms                                                     | 26.2 ms: 1.29x slower                                                                 |
| Geometric mean  | (ref)                                                       | 1.14x slower                                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-pythonperf1-amd64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 522 us: 16.22x faster                                                                 |
| pathlib                    | 75.3 ms                                                     | 32.2 ms: 2.34x faster                                                                 |
| regex_v8                   | 23.8 ms                                                     | 14.6 ms: 1.63x faster                                                                 |
| async_tree_memoization_tg  | 281 ms                                                      | 217 ms: 1.29x faster                                                                  |
| deepcopy                   | 223 us                                                      | 184 us: 1.21x faster                                                                  |
| async_tree_memoization     | 265 ms                                                      | 220 ms: 1.21x faster                                                                  |
| async_tree_io              | 513 ms                                                      | 426 ms: 1.20x faster                                                                  |
| async_tree_io_tg           | 497 ms                                                      | 416 ms: 1.20x faster                                                                  |
| regex_effbot               | 1.69 ms                                                     | 1.42 ms: 1.19x faster                                                                 |
| deepcopy_memo              | 23.1 us                                                     | 19.4 us: 1.19x faster                                                                 |
| async_tree_none            | 219 ms                                                      | 190 ms: 1.15x faster                                                                  |
| spectral_norm              | 63.4 ms                                                     | 56.5 ms: 1.12x faster                                                                 |
| async_tree_none_tg         | 200 ms                                                      | 179 ms: 1.12x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 346 ms: 1.11x faster                                                                  |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 344 ms: 1.11x faster                                                                  |
| json                       | 3.30 ms                                                     | 3.01 ms: 1.10x faster                                                                 |
| float                      | 50.8 ms                                                     | 47.0 ms: 1.08x faster                                                                 |
| deepcopy_reduce            | 2.02 us                                                     | 1.97 us: 1.03x faster                                                                 |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.55 ms: 1.02x faster                                                                 |
| regex_dna                  | 115 ms                                                      | 114 ms: 1.01x faster                                                                  |
| create_gc_cycles           | 1.22 ms                                                     | 1.25 ms: 1.02x slower                                                                 |
| scimark_sor                | 76.2 ms                                                     | 77.9 ms: 1.02x slower                                                                 |
| telco                      | 4.85 ms                                                     | 4.96 ms: 1.02x slower                                                                 |
| async_generators           | 223 ms                                                      | 228 ms: 1.02x slower                                                                  |
| k_core                     | 1.70 sec                                                    | 1.74 sec: 1.03x slower                                                                |
| generators                 | 19.0 ms                                                     | 19.5 ms: 1.03x slower                                                                 |
| scimark_fft                | 175 ms                                                      | 180 ms: 1.03x slower                                                                  |
| go                         | 84.7 ms                                                     | 87.6 ms: 1.03x slower                                                                 |
| bpe_tokeniser              | 2.87 sec                                                    | 2.98 sec: 1.04x slower                                                                |
| tomli_loads                | 1.37 sec                                                    | 1.42 sec: 1.04x slower                                                                |
| pidigits                   | 146 ms                                                      | 152 ms: 1.04x slower                                                                  |
| gc_traversal               | 1.96 ms                                                     | 2.04 ms: 1.04x slower                                                                 |
| bench_mp_pool              | 84.2 ms                                                     | 87.7 ms: 1.04x slower                                                                 |
| coverage                   | 45.3 ms                                                     | 47.2 ms: 1.04x slower                                                                 |
| meteor_contest             | 72.0 ms                                                     | 75.6 ms: 1.05x slower                                                                 |
| asyncio_websockets         | 300 ms                                                      | 315 ms: 1.05x slower                                                                  |
| scimark_monte_carlo        | 40.7 ms                                                     | 43.1 ms: 1.06x slower                                                                 |
| shortest_path              | 355 ms                                                      | 376 ms: 1.06x slower                                                                  |
| 2to3                       | 215 ms                                                      | 228 ms: 1.06x slower                                                                  |
| sphinx                     | 617 ms                                                      | 655 ms: 1.06x slower                                                                  |
| sympy_str                  | 167 ms                                                      | 178 ms: 1.06x slower                                                                  |
| sympy_sum                  | 85.2 ms                                                     | 90.7 ms: 1.07x slower                                                                 |
| connected_components       | 320 ms                                                      | 341 ms: 1.07x slower                                                                  |
| regex_compile              | 80.7 ms                                                     | 86.2 ms: 1.07x slower                                                                 |
| sympy_expand               | 286 ms                                                      | 306 ms: 1.07x slower                                                                  |
| pycparser                  | 695 ms                                                      | 745 ms: 1.07x slower                                                                  |
| python_startup             | 24.4 ms                                                     | 26.1 ms: 1.07x slower                                                                 |
| mako                       | 6.56 ms                                                     | 7.04 ms: 1.07x slower                                                                 |
| scimark_lu                 | 56.7 ms                                                     | 61.0 ms: 1.07x slower                                                                 |
| logging_silent             | 54.6 ns                                                     | 58.7 ns: 1.08x slower                                                                 |
| typing_runtime_protocols   | 103 us                                                      | 111 us: 1.08x slower                                                                  |
| bench_thread_pool          | 810 us                                                      | 876 us: 1.08x slower                                                                  |
| html5lib                   | 38.2 ms                                                     | 41.3 ms: 1.08x slower                                                                 |
| pyflate                    | 283 ms                                                      | 306 ms: 1.08x slower                                                                  |
| crypto_pyaes               | 45.6 ms                                                     | 49.5 ms: 1.08x slower                                                                 |
| dulwich_log                | 40.1 ms                                                     | 43.5 ms: 1.08x slower                                                                 |
| coroutines                 | 12.5 ms                                                     | 13.6 ms: 1.09x slower                                                                 |
| sympy_integrate            | 12.3 ms                                                     | 13.4 ms: 1.09x slower                                                                 |
| fannkuch                   | 252 ms                                                      | 274 ms: 1.09x slower                                                                  |
| xml_etree_generate         | 53.5 ms                                                     | 58.3 ms: 1.09x slower                                                                 |
| xml_etree_iterparse        | 60.5 ms                                                     | 66.1 ms: 1.09x slower                                                                 |
| sqlglot_optimize           | 32.5 ms                                                     | 35.6 ms: 1.09x slower                                                                 |
| genshi_xml                 | 33.9 ms                                                     | 37.1 ms: 1.10x slower                                                                 |
| docutils                   | 1.53 sec                                                    | 1.69 sec: 1.11x slower                                                                |
| genshi_text                | 15.2 ms                                                     | 16.9 ms: 1.11x slower                                                                 |
| richards_super             | 29.8 ms                                                     | 33.1 ms: 1.11x slower                                                                 |
| richards                   | 26.3 ms                                                     | 29.2 ms: 1.11x slower                                                                 |
| chaos                      | 37.9 ms                                                     | 42.2 ms: 1.11x slower                                                                 |
| json_dumps                 | 6.19 ms                                                     | 6.95 ms: 1.12x slower                                                                 |
| mdp                        | 1.43 sec                                                    | 1.61 sec: 1.12x slower                                                                |
| logging_simple             | 5.77 us                                                     | 6.52 us: 1.13x slower                                                                 |
| pprint_safe_repr           | 485 ms                                                      | 548 ms: 1.13x slower                                                                  |
| pprint_pformat             | 977 ms                                                      | 1.11 sec: 1.13x slower                                                                |
| hexiom                     | 3.84 ms                                                     | 4.36 ms: 1.13x slower                                                                 |
| unpickle_pure_python       | 130 us                                                      | 148 us: 1.14x slower                                                                  |
| xml_etree_process          | 36.5 ms                                                     | 41.7 ms: 1.14x slower                                                                 |
| comprehensions             | 10.4 us                                                     | 11.8 us: 1.14x slower                                                                 |
| sqlglot_normalize          | 172 ms                                                      | 196 ms: 1.14x slower                                                                  |
| logging_format             | 6.18 us                                                     | 7.06 us: 1.14x slower                                                                 |
| python_startup_no_site     | 16.9 ms                                                     | 19.7 ms: 1.16x slower                                                                 |
| nqueens                    | 56.1 ms                                                     | 65.5 ms: 1.17x slower                                                                 |
| sqlglot_parse              | 764 us                                                      | 891 us: 1.17x slower                                                                  |
| sqlglot_transpile          | 953 us                                                      | 1.12 ms: 1.17x slower                                                                 |
| deltablue                  | 1.89 ms                                                     | 2.27 ms: 1.20x slower                                                                 |
| many_optionals             | 361 us                                                      | 436 us: 1.21x slower                                                                  |
| pickle_pure_python         | 186 us                                                      | 227 us: 1.22x slower                                                                  |
| raytrace                   | 153 ms                                                      | 194 ms: 1.27x slower                                                                  |
| django_template            | 20.3 ms                                                     | 26.2 ms: 1.29x slower                                                                 |
| subparsers                 | 10.9 ms                                                     | 16.6 ms: 1.53x slower                                                                 |
| Geometric mean             | (ref)                                                       | 1.00x slower                                                                          |

Benchmark hidden because not significant (5): pylint, xml_etree_parse, json_loads, sqlite_synth, nbody
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown