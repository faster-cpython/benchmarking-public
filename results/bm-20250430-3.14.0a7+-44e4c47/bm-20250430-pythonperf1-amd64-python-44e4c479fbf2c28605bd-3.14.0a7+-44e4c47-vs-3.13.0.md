# Results vs. 3.13.0

- fork: python
- ref: 44e4c479fbf2c28605bd
- machine: windows-amd64
- commit hash: 44e4c47
- commit date: 2025-04-30
- overall geometric mean: 1.032x faster
- HPT reliability: 78.04%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-pythonperf1-amd64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 219 ms: 1.02x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.64 sec: 1.07x slower                                                      |
| html5lib       | 38.2 ms                                                     | 37.4 ms: 1.02x faster                                                       |
| sphinx         | 617 ms                                                      | 643 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-pythonperf1-amd64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 160 ms: 1.87x faster                                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 208 ms: 1.35x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 206 ms: 1.29x faster                                                        |
| async_tree_io              | 513 ms                                                      | 412 ms: 1.25x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 401 ms: 1.24x faster                                                        |
| async_tree_none            | 219 ms                                                      | 181 ms: 1.21x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 171 ms: 1.17x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 337 ms: 1.13x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 344 ms: 1.11x faster                                                        |
| async_generators           | 223 ms                                                      | 228 ms: 1.02x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.6 ms: 1.09x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.21x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-pythonperf1-amd64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 43.5 ms: 1.17x faster                                                       |
| nbody          | 66.3 ms                                                     | 62.9 ms: 1.05x faster                                                       |
| pidigits       | 146 ms                                                      | 149 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-pythonperf1-amd64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.8 ms: 1.61x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.46 ms: 1.16x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 79.8 ms: 1.01x faster                                                       |
| regex_dna      | 115 ms                                                      | 121 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-pythonperf1-amd64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 89.6 ms: 1.03x faster                                                       |
| json_loads           | 15.1 us                                                     | 15.3 us: 1.01x slower                                                       |
| unpickle_pure_python | 130 us                                                      | 132 us: 1.01x slower                                                        |
| xml_etree_iterparse  | 60.5 ms                                                     | 62.7 ms: 1.04x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 55.9 ms: 1.05x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 39.3 ms: 1.08x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 6.83 ms: 1.10x slower                                                       |
| pickle_pure_python   | 186 us                                                      | 209 us: 1.12x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.04x slower                                                                |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-pythonperf1-amd64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.5 ms: 1.09x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 19.8 ms: 1.17x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-pythonperf1-amd64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 15.2 ms                                                     | 15.0 ms: 1.02x faster                                                       |
| mako            | 6.56 ms                                                     | 6.49 ms: 1.01x faster                                                       |
| django_template | 20.3 ms                                                     | 24.2 ms: 1.19x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.04x slower                                                                |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-pythonperf1-amd64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 32.6 ms: 2.31x faster                                                       |
| asyncio_websockets         | 300 ms                                                      | 160 ms: 1.87x faster                                                        |
| mdp                        | 1.43 sec                                                    | 790 ms: 1.81x faster                                                        |
| regex_v8                   | 23.8 ms                                                     | 14.8 ms: 1.61x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 208 ms: 1.35x faster                                                        |
| deepcopy                   | 223 us                                                      | 172 us: 1.30x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 206 ms: 1.29x faster                                                        |
| deepcopy_memo              | 23.1 us                                                     | 18.4 us: 1.25x faster                                                       |
| async_tree_io              | 513 ms                                                      | 412 ms: 1.25x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 401 ms: 1.24x faster                                                        |
| async_tree_none            | 219 ms                                                      | 181 ms: 1.21x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 171 ms: 1.17x faster                                                        |
| float                      | 50.8 ms                                                     | 43.5 ms: 1.17x faster                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.46 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 337 ms: 1.13x faster                                                        |
| deepcopy_reduce            | 2.02 us                                                     | 1.82 us: 1.11x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 344 ms: 1.11x faster                                                        |
| spectral_norm              | 63.4 ms                                                     | 57.2 ms: 1.11x faster                                                       |
| go                         | 84.7 ms                                                     | 76.3 ms: 1.11x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.60 ms: 1.05x faster                                                       |
| nbody                      | 66.3 ms                                                     | 62.9 ms: 1.05x faster                                                       |
| json                       | 3.30 ms                                                     | 3.14 ms: 1.05x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.50 ms: 1.04x faster                                                       |
| pyflate                    | 283 ms                                                      | 272 ms: 1.04x faster                                                        |
| xml_etree_parse            | 92.2 ms                                                     | 89.6 ms: 1.03x faster                                                       |
| scimark_sor                | 76.2 ms                                                     | 74.4 ms: 1.02x faster                                                       |
| html5lib                   | 38.2 ms                                                     | 37.4 ms: 1.02x faster                                                       |
| scimark_lu                 | 56.7 ms                                                     | 55.7 ms: 1.02x faster                                                       |
| genshi_text                | 15.2 ms                                                     | 15.0 ms: 1.02x faster                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.56 us: 1.01x faster                                                       |
| mako                       | 6.56 ms                                                     | 6.49 ms: 1.01x faster                                                       |
| regex_compile              | 80.7 ms                                                     | 79.8 ms: 1.01x faster                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.85 sec: 1.01x faster                                                      |
| fannkuch                   | 252 ms                                                      | 250 ms: 1.01x faster                                                        |
| scimark_fft                | 175 ms                                                      | 174 ms: 1.01x faster                                                        |
| meteor_contest             | 72.0 ms                                                     | 72.2 ms: 1.00x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 55.1 ns: 1.01x slower                                                       |
| json_loads                 | 15.1 us                                                     | 15.3 us: 1.01x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 132 us: 1.01x slower                                                        |
| sympy_integrate            | 12.3 ms                                                     | 12.5 ms: 1.01x slower                                                       |
| pprint_safe_repr           | 485 ms                                                      | 491 ms: 1.01x slower                                                        |
| pidigits                   | 146 ms                                                      | 149 ms: 1.01x slower                                                        |
| 2to3                       | 215 ms                                                      | 219 ms: 1.02x slower                                                        |
| shortest_path              | 355 ms                                                      | 362 ms: 1.02x slower                                                        |
| chaos                      | 37.9 ms                                                     | 38.7 ms: 1.02x slower                                                       |
| sympy_expand               | 286 ms                                                      | 293 ms: 1.02x slower                                                        |
| async_generators           | 223 ms                                                      | 228 ms: 1.02x slower                                                        |
| sympy_str                  | 167 ms                                                      | 171 ms: 1.02x slower                                                        |
| create_gc_cycles           | 1.22 ms                                                     | 1.25 ms: 1.02x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.01 sec: 1.03x slower                                                      |
| richards                   | 26.3 ms                                                     | 27.0 ms: 1.03x slower                                                       |
| generators                 | 19.0 ms                                                     | 19.6 ms: 1.03x slower                                                       |
| richards_super             | 29.8 ms                                                     | 30.7 ms: 1.03x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 3.97 ms: 1.03x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 88.1 ms: 1.03x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 62.7 ms: 1.04x slower                                                       |
| connected_components       | 320 ms                                                      | 332 ms: 1.04x slower                                                        |
| sphinx                     | 617 ms                                                      | 643 ms: 1.04x slower                                                        |
| xml_etree_generate         | 53.5 ms                                                     | 55.9 ms: 1.05x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 42.0 ms: 1.05x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 47.8 ms: 1.05x slower                                                       |
| regex_dna                  | 115 ms                                                      | 121 ms: 1.05x slower                                                        |
| typing_runtime_protocols   | 103 us                                                      | 109 us: 1.06x slower                                                        |
| gc_traversal               | 1.96 ms                                                     | 2.08 ms: 1.06x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 860 us: 1.06x slower                                                        |
| logging_simple             | 5.77 us                                                     | 6.16 us: 1.07x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.64 sec: 1.07x slower                                                      |
| bench_mp_pool              | 84.2 ms                                                     | 90.0 ms: 1.07x slower                                                       |
| comprehensions             | 10.4 us                                                     | 11.1 us: 1.07x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 60.2 ms: 1.07x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 39.3 ms: 1.08x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.65 us: 1.08x slower                                                       |
| python_startup             | 24.4 ms                                                     | 26.5 ms: 1.09x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.6 ms: 1.09x slower                                                       |
| coverage                   | 45.3 ms                                                     | 49.3 ms: 1.09x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.08 ms: 1.10x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 6.83 ms: 1.10x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 209 us: 1.12x slower                                                        |
| raytrace                   | 153 ms                                                      | 178 ms: 1.16x slower                                                        |
| python_startup_no_site     | 16.9 ms                                                     | 19.8 ms: 1.17x slower                                                       |
| many_optionals             | 361 us                                                      | 422 us: 1.17x slower                                                        |
| django_template            | 20.3 ms                                                     | 24.2 ms: 1.19x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 16.0 ms: 1.48x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (6): pylint, genshi_xml, scimark_monte_carlo, tomli_loads, k_core, pycparser
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250430-3.14.0a7+-44e4c47/bm-20250430-pythonperf1-amd64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.032x faster

# HPT report

- Reliability score: 78.04% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown