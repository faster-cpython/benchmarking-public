# Results vs. 3.13.0

- fork: python
- ref: v3.14.0a5
- machine: windows-amd64
- commit hash: 3ae9101
- commit date: 2025-02-11
- overall geometric mean: 1.025x faster
- HPT reliability: 83.14%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-pythonperf1-amd64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 222 ms: 1.03x slower                                            |
| docutils       | 1.53 sec                                                    | 1.75 sec: 1.15x slower                                          |
| sphinx         | 617 ms                                                      | 661 ms: 1.07x slower                                            |
| Geometric mean | (ref)                                                       | 1.06x slower                                                    |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-pythonperf1-amd64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 217 ms: 1.29x faster                                            |
| async_tree_io              | 513 ms                                                      | 417 ms: 1.23x faster                                            |
| async_tree_memoization     | 265 ms                                                      | 224 ms: 1.18x faster                                            |
| async_tree_io_tg           | 497 ms                                                      | 424 ms: 1.17x faster                                            |
| async_tree_none            | 219 ms                                                      | 189 ms: 1.16x faster                                            |
| async_tree_none_tg         | 200 ms                                                      | 177 ms: 1.13x faster                                            |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 343 ms: 1.12x faster                                            |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 341 ms: 1.11x faster                                            |
| asyncio_websockets         | 300 ms                                                      | 304 ms: 1.01x slower                                            |
| async_generators           | 223 ms                                                      | 251 ms: 1.13x slower                                            |
| coroutines                 | 12.5 ms                                                     | 14.9 ms: 1.19x slower                                           |
| Geometric mean             | (ref)                                                       | 1.09x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-pythonperf1-amd64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 60.5 ms: 1.10x faster                                           |
| float          | 50.8 ms                                                     | 48.4 ms: 1.05x faster                                           |
| pidigits       | 146 ms                                                      | 150 ms: 1.02x slower                                            |
| Geometric mean | (ref)                                                       | 1.04x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-pythonperf1-amd64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.7 ms: 1.63x faster                                           |
| regex_effbot   | 1.69 ms                                                     | 1.42 ms: 1.19x faster                                           |
| regex_dna      | 115 ms                                                      | 114 ms: 1.01x faster                                            |
| Geometric mean | (ref)                                                       | 1.18x faster                                                    |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-pythonperf1-amd64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.18 sec: 1.16x faster                                          |
| unpickle_pure_python | 130 us                                                      | 115 us: 1.13x faster                                            |
| xml_etree_generate   | 53.5 ms                                                     | 51.1 ms: 1.05x faster                                           |
| xml_etree_parse      | 92.2 ms                                                     | 90.5 ms: 1.02x faster                                           |
| xml_etree_process    | 36.5 ms                                                     | 36.7 ms: 1.01x slower                                           |
| xml_etree_iterparse  | 60.5 ms                                                     | 61.0 ms: 1.01x slower                                           |
| json_loads           | 15.1 us                                                     | 16.2 us: 1.07x slower                                           |
| json_dumps           | 6.19 ms                                                     | 6.66 ms: 1.08x slower                                           |
| pickle_pure_python   | 186 us                                                      | 211 us: 1.13x slower                                            |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-pythonperf1-amd64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.1 ms: 1.03x slower                                           |
| python_startup_no_site | 16.9 ms                                                     | 18.9 ms: 1.12x slower                                           |
| Geometric mean         | (ref)                                                       | 1.07x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-pythonperf1-amd64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.26 ms: 1.25x faster                                           |
| genshi_xml      | 33.9 ms                                                     | 36.4 ms: 1.07x slower                                           |
| genshi_text     | 15.2 ms                                                     | 16.7 ms: 1.09x slower                                           |
| django_template | 20.3 ms                                                     | 25.5 ms: 1.26x slower                                           |
| Geometric mean  | (ref)                                                       | 1.04x slower                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-pythonperf1-amd64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 498 us: 16.99x faster                                           |
| pathlib                    | 75.3 ms                                                     | 29.5 ms: 2.56x faster                                           |
| regex_v8                   | 23.8 ms                                                     | 14.7 ms: 1.63x faster                                           |
| async_tree_memoization_tg  | 281 ms                                                      | 217 ms: 1.29x faster                                            |
| mako                       | 6.56 ms                                                     | 5.26 ms: 1.25x faster                                           |
| async_tree_io              | 513 ms                                                      | 417 ms: 1.23x faster                                            |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.15 ms: 1.21x faster                                           |
| deepcopy                   | 223 us                                                      | 188 us: 1.19x faster                                            |
| regex_effbot               | 1.69 ms                                                     | 1.42 ms: 1.19x faster                                           |
| scimark_fft                | 175 ms                                                      | 148 ms: 1.19x faster                                            |
| async_tree_memoization     | 265 ms                                                      | 224 ms: 1.18x faster                                            |
| async_tree_io_tg           | 497 ms                                                      | 424 ms: 1.17x faster                                            |
| tomli_loads                | 1.37 sec                                                    | 1.18 sec: 1.16x faster                                          |
| async_tree_none            | 219 ms                                                      | 189 ms: 1.16x faster                                            |
| unpickle_pure_python       | 130 us                                                      | 115 us: 1.13x faster                                            |
| async_tree_none_tg         | 200 ms                                                      | 177 ms: 1.13x faster                                            |
| bpe_tokeniser              | 2.87 sec                                                    | 2.57 sec: 1.12x faster                                          |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 343 ms: 1.12x faster                                            |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 341 ms: 1.11x faster                                            |
| telco                      | 4.85 ms                                                     | 4.39 ms: 1.10x faster                                           |
| fannkuch                   | 252 ms                                                      | 229 ms: 1.10x faster                                            |
| nbody                      | 66.3 ms                                                     | 60.5 ms: 1.10x faster                                           |
| deepcopy_memo              | 23.1 us                                                     | 21.3 us: 1.08x faster                                           |
| k_core                     | 1.70 sec                                                    | 1.61 sec: 1.06x faster                                          |
| float                      | 50.8 ms                                                     | 48.4 ms: 1.05x faster                                           |
| xml_etree_generate         | 53.5 ms                                                     | 51.1 ms: 1.05x faster                                           |
| sqlite_synth               | 1.59 us                                                     | 1.53 us: 1.04x faster                                           |
| deepcopy_reduce            | 2.02 us                                                     | 1.97 us: 1.02x faster                                           |
| connected_components       | 320 ms                                                      | 313 ms: 1.02x faster                                            |
| shortest_path              | 355 ms                                                      | 348 ms: 1.02x faster                                            |
| pyflate                    | 283 ms                                                      | 278 ms: 1.02x faster                                            |
| xml_etree_parse            | 92.2 ms                                                     | 90.5 ms: 1.02x faster                                           |
| spectral_norm              | 63.4 ms                                                     | 62.3 ms: 1.02x faster                                           |
| create_gc_cycles           | 1.22 ms                                                     | 1.21 ms: 1.01x faster                                           |
| dulwich_log                | 40.1 ms                                                     | 39.8 ms: 1.01x faster                                           |
| regex_dna                  | 115 ms                                                      | 114 ms: 1.01x faster                                            |
| crypto_pyaes               | 45.6 ms                                                     | 45.9 ms: 1.01x slower                                           |
| xml_etree_process          | 36.5 ms                                                     | 36.7 ms: 1.01x slower                                           |
| xml_etree_iterparse        | 60.5 ms                                                     | 61.0 ms: 1.01x slower                                           |
| asyncio_websockets         | 300 ms                                                      | 304 ms: 1.01x slower                                            |
| pprint_pformat             | 977 ms                                                      | 995 ms: 1.02x slower                                            |
| pidigits                   | 146 ms                                                      | 150 ms: 1.02x slower                                            |
| python_startup             | 24.4 ms                                                     | 25.1 ms: 1.03x slower                                           |
| 2to3                       | 215 ms                                                      | 222 ms: 1.03x slower                                            |
| go                         | 84.7 ms                                                     | 88.1 ms: 1.04x slower                                           |
| pprint_safe_repr           | 485 ms                                                      | 506 ms: 1.04x slower                                            |
| sympy_str                  | 167 ms                                                      | 175 ms: 1.05x slower                                            |
| mdp                        | 1.43 sec                                                    | 1.51 sec: 1.05x slower                                          |
| sympy_sum                  | 85.2 ms                                                     | 90.1 ms: 1.06x slower                                           |
| bench_thread_pool          | 810 us                                                      | 858 us: 1.06x slower                                            |
| sympy_expand               | 286 ms                                                      | 303 ms: 1.06x slower                                            |
| coverage                   | 45.3 ms                                                     | 48.2 ms: 1.06x slower                                           |
| typing_runtime_protocols   | 103 us                                                      | 110 us: 1.07x slower                                            |
| meteor_contest             | 72.0 ms                                                     | 77.0 ms: 1.07x slower                                           |
| sphinx                     | 617 ms                                                      | 661 ms: 1.07x slower                                            |
| json_loads                 | 15.1 us                                                     | 16.2 us: 1.07x slower                                           |
| genshi_xml                 | 33.9 ms                                                     | 36.4 ms: 1.07x slower                                           |
| generators                 | 19.0 ms                                                     | 20.4 ms: 1.08x slower                                           |
| json_dumps                 | 6.19 ms                                                     | 6.66 ms: 1.08x slower                                           |
| genshi_text                | 15.2 ms                                                     | 16.7 ms: 1.09x slower                                           |
| sqlglot_parse              | 764 us                                                      | 839 us: 1.10x slower                                            |
| comprehensions             | 10.4 us                                                     | 11.5 us: 1.11x slower                                           |
| logging_format             | 6.18 us                                                     | 6.88 us: 1.11x slower                                           |
| chaos                      | 37.9 ms                                                     | 42.2 ms: 1.12x slower                                           |
| python_startup_no_site     | 16.9 ms                                                     | 18.9 ms: 1.12x slower                                           |
| nqueens                    | 56.1 ms                                                     | 63.0 ms: 1.12x slower                                           |
| sqlglot_transpile          | 953 us                                                      | 1.07 ms: 1.12x slower                                           |
| sympy_integrate            | 12.3 ms                                                     | 13.8 ms: 1.12x slower                                           |
| logging_simple             | 5.77 us                                                     | 6.48 us: 1.12x slower                                           |
| async_generators           | 223 ms                                                      | 251 ms: 1.13x slower                                            |
| pickle_pure_python         | 186 us                                                      | 211 us: 1.13x slower                                            |
| scimark_monte_carlo        | 40.7 ms                                                     | 46.6 ms: 1.14x slower                                           |
| docutils                   | 1.53 sec                                                    | 1.75 sec: 1.15x slower                                          |
| sqlglot_optimize           | 32.5 ms                                                     | 37.3 ms: 1.15x slower                                           |
| scimark_lu                 | 56.7 ms                                                     | 66.1 ms: 1.17x slower                                           |
| hexiom                     | 3.84 ms                                                     | 4.54 ms: 1.18x slower                                           |
| sqlglot_normalize          | 172 ms                                                      | 203 ms: 1.18x slower                                            |
| coroutines                 | 12.5 ms                                                     | 14.9 ms: 1.19x slower                                           |
| logging_silent             | 54.6 ns                                                     | 66.1 ns: 1.21x slower                                           |
| scimark_sor                | 76.2 ms                                                     | 92.5 ms: 1.21x slower                                           |
| richards_super             | 29.8 ms                                                     | 36.2 ms: 1.22x slower                                           |
| many_optionals             | 361 us                                                      | 442 us: 1.22x slower                                            |
| richards                   | 26.3 ms                                                     | 32.5 ms: 1.24x slower                                           |
| django_template            | 20.3 ms                                                     | 25.5 ms: 1.26x slower                                           |
| deltablue                  | 1.89 ms                                                     | 2.42 ms: 1.28x slower                                           |
| raytrace                   | 153 ms                                                      | 208 ms: 1.36x slower                                            |
| subparsers                 | 10.9 ms                                                     | 16.0 ms: 1.48x slower                                           |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                    |

Benchmark hidden because not significant (7): json, pylint, html5lib, bench_mp_pool, regex_compile, gc_traversal, pycparser
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http

- Geometric mean (including insignificant results): 1.025x faster

# HPT report

- Reliability score: 83.14% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown