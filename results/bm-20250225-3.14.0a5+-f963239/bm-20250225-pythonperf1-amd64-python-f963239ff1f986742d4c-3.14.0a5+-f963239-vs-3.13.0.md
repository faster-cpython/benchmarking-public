# Results vs. 3.13.0

- fork: python
- ref: f963239ff1f986742d4c
- machine: windows-amd64
- commit hash: f963239
- commit date: 2025-02-25
- overall geometric mean: 1.003x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-pythonperf1-amd64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 227 ms: 1.06x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.68 sec: 1.10x slower                                                      |
| html5lib       | 38.2 ms                                                     | 40.8 ms: 1.07x slower                                                       |
| sphinx         | 617 ms                                                      | 658 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                       | 1.07x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-pythonperf1-amd64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 216 ms: 1.30x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 410 ms: 1.21x faster                                                        |
| async_tree_io              | 513 ms                                                      | 423 ms: 1.21x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 224 ms: 1.18x faster                                                        |
| async_tree_none            | 219 ms                                                      | 187 ms: 1.17x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 176 ms: 1.13x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 339 ms: 1.12x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 343 ms: 1.12x faster                                                        |
| async_generators           | 223 ms                                                      | 226 ms: 1.02x slower                                                        |
| asyncio_websockets         | 300 ms                                                      | 318 ms: 1.06x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.5 ms: 1.08x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.11x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-pythonperf1-amd64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 47.8 ms: 1.06x faster                                                       |
| pidigits       | 146 ms                                                      | 152 ms: 1.04x slower                                                        |
| nbody          | 66.3 ms                                                     | 74.1 ms: 1.12x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-pythonperf1-amd64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.5 ms: 1.76x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.42 ms: 1.19x faster                                                       |
| regex_dna      | 115 ms                                                      | 112 ms: 1.02x faster                                                        |
| regex_compile  | 80.7 ms                                                     | 88.2 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-pythonperf1-amd64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.7 us: 1.03x faster                                                       |
| xml_etree_parse      | 92.2 ms                                                     | 91.2 ms: 1.01x faster                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.7 ms: 1.05x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.47 sec: 1.07x slower                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 58.7 ms: 1.10x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 41.5 ms: 1.14x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 7.05 ms: 1.14x slower                                                       |
| unpickle_pure_python | 130 us                                                      | 155 us: 1.20x slower                                                        |
| pickle_pure_python   | 186 us                                                      | 237 us: 1.27x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.10x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-pythonperf1-amd64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.1 ms: 1.07x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 19.8 ms: 1.17x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-pythonperf1-amd64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.86 ms: 1.04x slower                                                       |
| genshi_xml      | 33.9 ms                                                     | 36.3 ms: 1.07x slower                                                       |
| genshi_text     | 15.2 ms                                                     | 16.5 ms: 1.08x slower                                                       |
| django_template | 20.3 ms                                                     | 25.1 ms: 1.24x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.11x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-pythonperf1-amd64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 507 us: 16.71x faster                                                       |
| pathlib                    | 75.3 ms                                                     | 32.1 ms: 2.35x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 13.5 ms: 1.76x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 216 ms: 1.30x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 410 ms: 1.21x faster                                                        |
| async_tree_io              | 513 ms                                                      | 423 ms: 1.21x faster                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.42 ms: 1.19x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 224 ms: 1.18x faster                                                        |
| deepcopy                   | 223 us                                                      | 190 us: 1.18x faster                                                        |
| async_tree_none            | 219 ms                                                      | 187 ms: 1.17x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 176 ms: 1.13x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 339 ms: 1.12x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 343 ms: 1.12x faster                                                        |
| deepcopy_memo              | 23.1 us                                                     | 21.0 us: 1.10x faster                                                       |
| float                      | 50.8 ms                                                     | 47.8 ms: 1.06x faster                                                       |
| json                       | 3.30 ms                                                     | 3.14 ms: 1.05x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.94 us: 1.04x faster                                                       |
| spectral_norm              | 63.4 ms                                                     | 61.5 ms: 1.03x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.7 us: 1.03x faster                                                       |
| regex_dna                  | 115 ms                                                      | 112 ms: 1.02x faster                                                        |
| xml_etree_parse            | 92.2 ms                                                     | 91.2 ms: 1.01x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.89 ms: 1.01x slower                                                       |
| shortest_path              | 355 ms                                                      | 359 ms: 1.01x slower                                                        |
| async_generators           | 223 ms                                                      | 226 ms: 1.02x slower                                                        |
| generators                 | 19.0 ms                                                     | 19.3 ms: 1.02x slower                                                       |
| k_core                     | 1.70 sec                                                    | 1.73 sec: 1.02x slower                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.25 ms: 1.02x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 106 us: 1.03x slower                                                        |
| connected_components       | 320 ms                                                      | 329 ms: 1.03x slower                                                        |
| bpe_tokeniser              | 2.87 sec                                                    | 2.96 sec: 1.03x slower                                                      |
| coverage                   | 45.3 ms                                                     | 46.8 ms: 1.03x slower                                                       |
| pidigits                   | 146 ms                                                      | 152 ms: 1.04x slower                                                        |
| mako                       | 6.56 ms                                                     | 6.86 ms: 1.04x slower                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.72 ms: 1.05x slower                                                       |
| go                         | 84.7 ms                                                     | 88.6 ms: 1.05x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 2.06 ms: 1.05x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.7 ms: 1.05x slower                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 88.7 ms: 1.05x slower                                                       |
| sympy_str                  | 167 ms                                                      | 176 ms: 1.06x slower                                                        |
| 2to3                       | 215 ms                                                      | 227 ms: 1.06x slower                                                        |
| sympy_expand               | 286 ms                                                      | 302 ms: 1.06x slower                                                        |
| asyncio_websockets         | 300 ms                                                      | 318 ms: 1.06x slower                                                        |
| pycparser                  | 695 ms                                                      | 738 ms: 1.06x slower                                                        |
| sympy_sum                  | 85.2 ms                                                     | 90.5 ms: 1.06x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 864 us: 1.07x slower                                                        |
| sphinx                     | 617 ms                                                      | 658 ms: 1.07x slower                                                        |
| html5lib                   | 38.2 ms                                                     | 40.8 ms: 1.07x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 76.9 ms: 1.07x slower                                                       |
| python_startup             | 24.4 ms                                                     | 26.1 ms: 1.07x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.47 sec: 1.07x slower                                                      |
| genshi_xml                 | 33.9 ms                                                     | 36.3 ms: 1.07x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.5 ms: 1.08x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 43.4 ms: 1.08x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 16.5 ms: 1.08x slower                                                       |
| regex_compile              | 80.7 ms                                                     | 88.2 ms: 1.09x slower                                                       |
| comprehensions             | 10.4 us                                                     | 11.3 us: 1.09x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.5 ms: 1.10x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 50.0 ms: 1.10x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.68 sec: 1.10x slower                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 58.7 ms: 1.10x slower                                                       |
| scimark_fft                | 175 ms                                                      | 192 ms: 1.10x slower                                                        |
| pyflate                    | 283 ms                                                      | 315 ms: 1.11x slower                                                        |
| nbody                      | 66.3 ms                                                     | 74.1 ms: 1.12x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.53 us: 1.13x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 63.6 ms: 1.13x slower                                                       |
| logging_format             | 6.18 us                                                     | 7.03 us: 1.14x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 41.5 ms: 1.14x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 7.05 ms: 1.14x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.38 ms: 1.14x slower                                                       |
| mdp                        | 1.43 sec                                                    | 1.64 sec: 1.14x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 558 ms: 1.15x slower                                                        |
| chaos                      | 37.9 ms                                                     | 43.6 ms: 1.15x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.13 sec: 1.15x slower                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 47.1 ms: 1.16x slower                                                       |
| richards                   | 26.3 ms                                                     | 30.7 ms: 1.17x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 19.8 ms: 1.17x slower                                                       |
| fannkuch                   | 252 ms                                                      | 296 ms: 1.18x slower                                                        |
| scimark_lu                 | 56.7 ms                                                     | 66.9 ms: 1.18x slower                                                       |
| richards_super             | 29.8 ms                                                     | 35.1 ms: 1.18x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 91.0 ms: 1.19x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 65.2 ns: 1.19x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 155 us: 1.20x slower                                                        |
| many_optionals             | 361 us                                                      | 438 us: 1.21x slower                                                        |
| deltablue                  | 1.89 ms                                                     | 2.29 ms: 1.21x slower                                                       |
| django_template            | 20.3 ms                                                     | 25.1 ms: 1.24x slower                                                       |
| raytrace                   | 153 ms                                                      | 191 ms: 1.24x slower                                                        |
| pickle_pure_python         | 186 us                                                      | 237 us: 1.27x slower                                                        |
| subparsers                 | 10.9 ms                                                     | 16.1 ms: 1.48x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (2): pylint, sqlite_synth
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250225-3.14.0a5+-f963239/bm-20250225-pythonperf1-amd64-python-f963239ff1f986742d4c-3.14.0a5+-f963239.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.003x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown