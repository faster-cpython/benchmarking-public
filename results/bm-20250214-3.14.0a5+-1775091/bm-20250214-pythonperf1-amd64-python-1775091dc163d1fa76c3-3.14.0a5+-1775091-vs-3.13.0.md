# Results vs. 3.13.0

- fork: python
- ref: 1775091dc163d1fa76c3
- machine: windows-amd64
- commit hash: 1775091
- commit date: 2025-02-14
- overall geometric mean: 1.017x faster
- HPT reliability: 99.73%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250214-pythonperf1-amd64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 221 ms: 1.03x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.64 sec: 1.07x slower                                                      |
| sphinx         | 617 ms                                                      | 642 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250214-pythonperf1-amd64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 218 ms: 1.29x faster                                                        |
| async_tree_io              | 513 ms                                                      | 415 ms: 1.24x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 412 ms: 1.21x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 222 ms: 1.19x faster                                                        |
| async_tree_none            | 219 ms                                                      | 190 ms: 1.15x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 178 ms: 1.13x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 343 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 343 ms: 1.11x faster                                                        |
| async_generators           | 223 ms                                                      | 219 ms: 1.02x faster                                                        |
| coroutines                 | 12.5 ms                                                     | 13.3 ms: 1.06x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.12x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250214-pythonperf1-amd64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 44.7 ms: 1.14x faster                                                       |
| pidigits       | 146 ms                                                      | 150 ms: 1.03x slower                                                        |
| nbody          | 66.3 ms                                                     | 69.7 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250214-pythonperf1-amd64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.3 ms: 1.67x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.46 ms: 1.16x faster                                                       |
| regex_dna      | 115 ms                                                      | 115 ms: 1.00x faster                                                        |
| regex_compile  | 80.7 ms                                                     | 84.2 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250214-pythonperf1-amd64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 90.2 ms: 1.02x faster                                                       |
| json_loads           | 15.1 us                                                     | 15.4 us: 1.02x slower                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.0 ms: 1.04x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 56.5 ms: 1.06x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 6.69 ms: 1.08x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 39.8 ms: 1.09x slower                                                       |
| unpickle_pure_python | 130 us                                                      | 143 us: 1.10x slower                                                        |
| pickle_pure_python   | 186 us                                                      | 221 us: 1.19x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.06x slower                                                                |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250214-pythonperf1-amd64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.9 ms                                                     | 18.8 ms: 1.11x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.06x slower                                                                |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250214-pythonperf1-amd64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.63 ms: 1.01x slower                                                       |
| genshi_xml      | 33.9 ms                                                     | 36.5 ms: 1.08x slower                                                       |
| genshi_text     | 15.2 ms                                                     | 17.0 ms: 1.12x slower                                                       |
| django_template | 20.3 ms                                                     | 25.1 ms: 1.24x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.11x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250214-pythonperf1-amd64-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 510 us: 16.60x faster                                                       |
| pathlib                    | 75.3 ms                                                     | 29.4 ms: 2.56x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 14.3 ms: 1.67x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 218 ms: 1.29x faster                                                        |
| async_tree_io              | 513 ms                                                      | 415 ms: 1.24x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 412 ms: 1.21x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 222 ms: 1.19x faster                                                        |
| deepcopy                   | 223 us                                                      | 188 us: 1.19x faster                                                        |
| deepcopy_memo              | 23.1 us                                                     | 19.5 us: 1.18x faster                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.46 ms: 1.16x faster                                                       |
| async_tree_none            | 219 ms                                                      | 190 ms: 1.15x faster                                                        |
| float                      | 50.8 ms                                                     | 44.7 ms: 1.14x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 178 ms: 1.13x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 343 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 343 ms: 1.11x faster                                                        |
| json                       | 3.30 ms                                                     | 3.10 ms: 1.06x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.91 us: 1.06x faster                                                       |
| spectral_norm              | 63.4 ms                                                     | 60.6 ms: 1.05x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.66 ms: 1.04x faster                                                       |
| shortest_path              | 355 ms                                                      | 347 ms: 1.02x faster                                                        |
| xml_etree_parse            | 92.2 ms                                                     | 90.2 ms: 1.02x faster                                                       |
| async_generators           | 223 ms                                                      | 219 ms: 1.02x faster                                                        |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.57 ms: 1.01x faster                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.85 sec: 1.01x faster                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.57 us: 1.01x faster                                                       |
| regex_dna                  | 115 ms                                                      | 115 ms: 1.00x faster                                                        |
| go                         | 84.7 ms                                                     | 84.4 ms: 1.00x faster                                                       |
| connected_components       | 320 ms                                                      | 322 ms: 1.01x slower                                                        |
| mako                       | 6.56 ms                                                     | 6.63 ms: 1.01x slower                                                       |
| json_loads                 | 15.1 us                                                     | 15.4 us: 1.02x slower                                                       |
| pidigits                   | 146 ms                                                      | 150 ms: 1.03x slower                                                        |
| dulwich_log                | 40.1 ms                                                     | 41.2 ms: 1.03x slower                                                       |
| 2to3                       | 215 ms                                                      | 221 ms: 1.03x slower                                                        |
| mdp                        | 1.43 sec                                                    | 1.48 sec: 1.03x slower                                                      |
| bench_thread_pool          | 810 us                                                      | 837 us: 1.03x slower                                                        |
| generators                 | 19.0 ms                                                     | 19.6 ms: 1.03x slower                                                       |
| coverage                   | 45.3 ms                                                     | 46.9 ms: 1.03x slower                                                       |
| sympy_expand               | 286 ms                                                      | 297 ms: 1.04x slower                                                        |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.0 ms: 1.04x slower                                                       |
| sphinx                     | 617 ms                                                      | 642 ms: 1.04x slower                                                        |
| pycparser                  | 695 ms                                                      | 724 ms: 1.04x slower                                                        |
| regex_compile              | 80.7 ms                                                     | 84.2 ms: 1.04x slower                                                       |
| sympy_str                  | 167 ms                                                      | 174 ms: 1.05x slower                                                        |
| sympy_sum                  | 85.2 ms                                                     | 89.2 ms: 1.05x slower                                                       |
| nbody                      | 66.3 ms                                                     | 69.7 ms: 1.05x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 57.5 ns: 1.05x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 75.8 ms: 1.05x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 59.9 ms: 1.06x slower                                                       |
| pyflate                    | 283 ms                                                      | 299 ms: 1.06x slower                                                        |
| xml_etree_generate         | 53.5 ms                                                     | 56.5 ms: 1.06x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.3 ms: 1.06x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.2 ms: 1.07x slower                                                       |
| scimark_fft                | 175 ms                                                      | 188 ms: 1.07x slower                                                        |
| docutils                   | 1.53 sec                                                    | 1.64 sec: 1.07x slower                                                      |
| typing_runtime_protocols   | 103 us                                                      | 111 us: 1.08x slower                                                        |
| genshi_xml                 | 33.9 ms                                                     | 36.5 ms: 1.08x slower                                                       |
| comprehensions             | 10.4 us                                                     | 11.2 us: 1.08x slower                                                       |
| sqlglot_optimize           | 32.5 ms                                                     | 35.1 ms: 1.08x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 6.69 ms: 1.08x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.25 us: 1.08x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 49.6 ms: 1.09x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.19 ms: 1.09x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 39.8 ms: 1.09x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.76 us: 1.10x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.07 sec: 1.10x slower                                                      |
| chaos                      | 37.9 ms                                                     | 41.7 ms: 1.10x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 83.9 ms: 1.10x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 62.0 ms: 1.10x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 143 us: 1.10x slower                                                        |
| python_startup_no_site     | 16.9 ms                                                     | 18.8 ms: 1.11x slower                                                       |
| pprint_safe_repr           | 485 ms                                                      | 539 ms: 1.11x slower                                                        |
| sqlglot_normalize          | 172 ms                                                      | 191 ms: 1.12x slower                                                        |
| fannkuch                   | 252 ms                                                      | 281 ms: 1.12x slower                                                        |
| genshi_text                | 15.2 ms                                                     | 17.0 ms: 1.12x slower                                                       |
| richards                   | 26.3 ms                                                     | 29.4 ms: 1.12x slower                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 45.7 ms: 1.12x slower                                                       |
| richards_super             | 29.8 ms                                                     | 33.4 ms: 1.12x slower                                                       |
| sqlglot_transpile          | 953 us                                                      | 1.08 ms: 1.13x slower                                                       |
| sqlglot_parse              | 764 us                                                      | 870 us: 1.14x slower                                                        |
| deltablue                  | 1.89 ms                                                     | 2.16 ms: 1.14x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 221 us: 1.19x slower                                                        |
| many_optionals             | 361 us                                                      | 432 us: 1.20x slower                                                        |
| django_template            | 20.3 ms                                                     | 25.1 ms: 1.24x slower                                                       |
| raytrace                   | 153 ms                                                      | 194 ms: 1.26x slower                                                        |
| subparsers                 | 10.9 ms                                                     | 16.5 ms: 1.52x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (9): pylint, create_gc_cycles, bench_mp_pool, tomli_loads, python_startup, k_core, asyncio_websockets, gc_traversal, html5lib
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http

- Geometric mean (including insignificant results): 1.017x faster

# HPT report

- Reliability score: 99.73% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown