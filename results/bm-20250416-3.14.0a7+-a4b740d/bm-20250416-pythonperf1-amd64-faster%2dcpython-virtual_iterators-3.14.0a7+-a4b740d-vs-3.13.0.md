# Results vs. 3.13.0

- fork: faster-cpython
- ref: virtual_iterators
- machine: windows-amd64
- commit hash: a4b740d
- commit date: 2025-04-16
- overall geometric mean: 1.030x faster
- HPT reliability: 87.81%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250416-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 217 ms: 1.01x slower                                                               |
| docutils       | 1.53 sec                                                    | 1.64 sec: 1.07x slower                                                             |
| html5lib       | 38.2 ms                                                     | 39.4 ms: 1.03x slower                                                              |
| sphinx         | 617 ms                                                      | 636 ms: 1.03x slower                                                               |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250416-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 161 ms: 1.87x faster                                                               |
| async_tree_memoization_tg  | 281 ms                                                      | 214 ms: 1.31x faster                                                               |
| async_tree_memoization     | 265 ms                                                      | 208 ms: 1.27x faster                                                               |
| async_tree_io              | 513 ms                                                      | 413 ms: 1.24x faster                                                               |
| async_tree_io_tg           | 497 ms                                                      | 405 ms: 1.23x faster                                                               |
| async_tree_none            | 219 ms                                                      | 182 ms: 1.21x faster                                                               |
| async_tree_none_tg         | 200 ms                                                      | 173 ms: 1.16x faster                                                               |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 331 ms: 1.15x faster                                                               |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 340 ms: 1.13x faster                                                               |
| async_generators           | 223 ms                                                      | 221 ms: 1.01x faster                                                               |
| coroutines                 | 12.5 ms                                                     | 13.7 ms: 1.10x slower                                                              |
| Geometric mean             | (ref)                                                       | 1.21x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250416-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 43.3 ms: 1.17x faster                                                              |
| nbody          | 66.3 ms                                                     | 63.0 ms: 1.05x faster                                                              |
| pidigits       | 146 ms                                                      | 149 ms: 1.01x slower                                                               |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250416-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.2 ms: 1.68x faster                                                              |
| regex_effbot   | 1.69 ms                                                     | 1.43 ms: 1.18x faster                                                              |
| regex_dna      | 115 ms                                                      | 116 ms: 1.01x slower                                                               |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                       |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250416-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 90.8 ms: 1.01x faster                                                              |
| json_loads           | 15.1 us                                                     | 14.9 us: 1.01x faster                                                              |
| tomli_loads          | 1.37 sec                                                    | 1.39 sec: 1.01x slower                                                             |
| xml_etree_generate   | 53.5 ms                                                     | 55.4 ms: 1.04x slower                                                              |
| json_dumps           | 6.19 ms                                                     | 6.58 ms: 1.06x slower                                                              |
| xml_etree_process    | 36.5 ms                                                     | 38.9 ms: 1.07x slower                                                              |
| unpickle_pure_python | 130 us                                                      | 139 us: 1.07x slower                                                               |
| xml_etree_iterparse  | 60.5 ms                                                     | 65.4 ms: 1.08x slower                                                              |
| pickle_pure_python   | 186 us                                                      | 212 us: 1.14x slower                                                               |
| Geometric mean       | (ref)                                                       | 1.05x slower                                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250416-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.4 ms: 1.08x slower                                                              |
| python_startup_no_site | 16.9 ms                                                     | 20.5 ms: 1.21x slower                                                              |
| Geometric mean         | (ref)                                                       | 1.15x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250416-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.66 ms: 1.02x slower                                                              |
| genshi_text     | 15.2 ms                                                     | 15.5 ms: 1.02x slower                                                              |
| django_template | 20.3 ms                                                     | 24.4 ms: 1.20x slower                                                              |
| Geometric mean  | (ref)                                                       | 1.06x slower                                                                       |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250416-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 32.2 ms: 2.34x faster                                                              |
| asyncio_websockets         | 300 ms                                                      | 161 ms: 1.87x faster                                                               |
| mdp                        | 1.43 sec                                                    | 769 ms: 1.86x faster                                                               |
| regex_v8                   | 23.8 ms                                                     | 14.2 ms: 1.68x faster                                                              |
| async_tree_memoization_tg  | 281 ms                                                      | 214 ms: 1.31x faster                                                               |
| deepcopy                   | 223 us                                                      | 171 us: 1.30x faster                                                               |
| async_tree_memoization     | 265 ms                                                      | 208 ms: 1.27x faster                                                               |
| deepcopy_memo              | 23.1 us                                                     | 18.5 us: 1.25x faster                                                              |
| async_tree_io              | 513 ms                                                      | 413 ms: 1.24x faster                                                               |
| async_tree_io_tg           | 497 ms                                                      | 405 ms: 1.23x faster                                                               |
| async_tree_none            | 219 ms                                                      | 182 ms: 1.21x faster                                                               |
| regex_effbot               | 1.69 ms                                                     | 1.43 ms: 1.18x faster                                                              |
| float                      | 50.8 ms                                                     | 43.3 ms: 1.17x faster                                                              |
| async_tree_none_tg         | 200 ms                                                      | 173 ms: 1.16x faster                                                               |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 331 ms: 1.15x faster                                                               |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 340 ms: 1.13x faster                                                               |
| deepcopy_reduce            | 2.02 us                                                     | 1.82 us: 1.11x faster                                                              |
| spectral_norm              | 63.4 ms                                                     | 57.9 ms: 1.10x faster                                                              |
| json                       | 3.30 ms                                                     | 3.05 ms: 1.08x faster                                                              |
| go                         | 84.7 ms                                                     | 78.4 ms: 1.08x faster                                                              |
| telco                      | 4.85 ms                                                     | 4.59 ms: 1.06x faster                                                              |
| nbody                      | 66.3 ms                                                     | 63.0 ms: 1.05x faster                                                              |
| sqlite_synth               | 1.59 us                                                     | 1.54 us: 1.03x faster                                                              |
| scimark_monte_carlo        | 40.7 ms                                                     | 39.9 ms: 1.02x faster                                                              |
| typing_runtime_protocols   | 103 us                                                      | 101 us: 1.02x faster                                                               |
| xml_etree_parse            | 92.2 ms                                                     | 90.8 ms: 1.01x faster                                                              |
| json_loads                 | 15.1 us                                                     | 14.9 us: 1.01x faster                                                              |
| meteor_contest             | 72.0 ms                                                     | 71.2 ms: 1.01x faster                                                              |
| async_generators           | 223 ms                                                      | 221 ms: 1.01x faster                                                               |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.59 ms: 1.01x faster                                                              |
| regex_dna                  | 115 ms                                                      | 116 ms: 1.01x slower                                                               |
| scimark_sor                | 76.2 ms                                                     | 76.8 ms: 1.01x slower                                                              |
| 2to3                       | 215 ms                                                      | 217 ms: 1.01x slower                                                               |
| tomli_loads                | 1.37 sec                                                    | 1.39 sec: 1.01x slower                                                             |
| pidigits                   | 146 ms                                                      | 149 ms: 1.01x slower                                                               |
| mako                       | 6.56 ms                                                     | 6.66 ms: 1.02x slower                                                              |
| pprint_safe_repr           | 485 ms                                                      | 492 ms: 1.02x slower                                                               |
| genshi_text                | 15.2 ms                                                     | 15.5 ms: 1.02x slower                                                              |
| fannkuch                   | 252 ms                                                      | 257 ms: 1.02x slower                                                               |
| create_gc_cycles           | 1.22 ms                                                     | 1.25 ms: 1.02x slower                                                              |
| chaos                      | 37.9 ms                                                     | 38.6 ms: 1.02x slower                                                              |
| pprint_pformat             | 977 ms                                                      | 997 ms: 1.02x slower                                                               |
| bpe_tokeniser              | 2.87 sec                                                    | 2.94 sec: 1.02x slower                                                             |
| shortest_path              | 355 ms                                                      | 364 ms: 1.03x slower                                                               |
| sphinx                     | 617 ms                                                      | 636 ms: 1.03x slower                                                               |
| pycparser                  | 695 ms                                                      | 717 ms: 1.03x slower                                                               |
| html5lib                   | 38.2 ms                                                     | 39.4 ms: 1.03x slower                                                              |
| comprehensions             | 10.4 us                                                     | 10.7 us: 1.03x slower                                                              |
| xml_etree_generate         | 53.5 ms                                                     | 55.4 ms: 1.04x slower                                                              |
| crypto_pyaes               | 45.6 ms                                                     | 47.5 ms: 1.04x slower                                                              |
| hexiom                     | 3.84 ms                                                     | 4.02 ms: 1.05x slower                                                              |
| scimark_lu                 | 56.7 ms                                                     | 59.5 ms: 1.05x slower                                                              |
| connected_components       | 320 ms                                                      | 336 ms: 1.05x slower                                                               |
| bench_mp_pool              | 84.2 ms                                                     | 88.8 ms: 1.05x slower                                                              |
| generators                 | 19.0 ms                                                     | 20.1 ms: 1.06x slower                                                              |
| gc_traversal               | 1.96 ms                                                     | 2.08 ms: 1.06x slower                                                              |
| nqueens                    | 56.1 ms                                                     | 59.6 ms: 1.06x slower                                                              |
| json_dumps                 | 6.19 ms                                                     | 6.58 ms: 1.06x slower                                                              |
| dulwich_log                | 40.1 ms                                                     | 42.6 ms: 1.06x slower                                                              |
| richards_super             | 29.8 ms                                                     | 31.6 ms: 1.06x slower                                                              |
| xml_etree_process          | 36.5 ms                                                     | 38.9 ms: 1.07x slower                                                              |
| richards                   | 26.3 ms                                                     | 28.1 ms: 1.07x slower                                                              |
| unpickle_pure_python       | 130 us                                                      | 139 us: 1.07x slower                                                               |
| bench_thread_pool          | 810 us                                                      | 869 us: 1.07x slower                                                               |
| docutils                   | 1.53 sec                                                    | 1.64 sec: 1.07x slower                                                             |
| coverage                   | 45.3 ms                                                     | 48.8 ms: 1.08x slower                                                              |
| xml_etree_iterparse        | 60.5 ms                                                     | 65.4 ms: 1.08x slower                                                              |
| python_startup             | 24.4 ms                                                     | 26.4 ms: 1.08x slower                                                              |
| logging_simple             | 5.77 us                                                     | 6.25 us: 1.08x slower                                                              |
| coroutines                 | 12.5 ms                                                     | 13.7 ms: 1.10x slower                                                              |
| logging_format             | 6.18 us                                                     | 6.79 us: 1.10x slower                                                              |
| pickle_pure_python         | 186 us                                                      | 212 us: 1.14x slower                                                               |
| raytrace                   | 153 ms                                                      | 176 ms: 1.15x slower                                                               |
| deltablue                  | 1.89 ms                                                     | 2.19 ms: 1.16x slower                                                              |
| many_optionals             | 361 us                                                      | 423 us: 1.17x slower                                                               |
| django_template            | 20.3 ms                                                     | 24.4 ms: 1.20x slower                                                              |
| python_startup_no_site     | 16.9 ms                                                     | 20.5 ms: 1.21x slower                                                              |
| subparsers                 | 10.9 ms                                                     | 15.7 ms: 1.45x slower                                                              |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                                       |

Benchmark hidden because not significant (6): pyflate, scimark_fft, logging_silent, regex_compile, k_core, genshi_xml
Ignored benchmarks (16) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250416-3.14.0a7+-a4b740d/bm-20250416-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.030x faster

# HPT report

- Reliability score: 87.81% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown