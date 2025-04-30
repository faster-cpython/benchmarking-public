# Results vs. 3.13.0

- fork: faster-cpython
- ref: virtual_iterators
- machine: windows-amd64
- commit hash: cad1946
- commit date: 2025-04-30
- overall geometric mean: 1.030x faster
- HPT reliability: 84.88%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 220 ms: 1.02x slower                                                               |
| docutils       | 1.53 sec                                                    | 1.65 sec: 1.08x slower                                                             |
| html5lib       | 38.2 ms                                                     | 38.9 ms: 1.02x slower                                                              |
| sphinx         | 617 ms                                                      | 639 ms: 1.04x slower                                                               |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 157 ms: 1.91x faster                                                               |
| async_tree_memoization_tg  | 281 ms                                                      | 210 ms: 1.34x faster                                                               |
| async_tree_memoization     | 265 ms                                                      | 207 ms: 1.28x faster                                                               |
| async_tree_io              | 513 ms                                                      | 409 ms: 1.25x faster                                                               |
| async_tree_io_tg           | 497 ms                                                      | 400 ms: 1.24x faster                                                               |
| async_tree_none            | 219 ms                                                      | 180 ms: 1.22x faster                                                               |
| async_tree_none_tg         | 200 ms                                                      | 171 ms: 1.17x faster                                                               |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 334 ms: 1.14x faster                                                               |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 344 ms: 1.11x faster                                                               |
| async_generators           | 223 ms                                                      | 232 ms: 1.04x slower                                                               |
| coroutines                 | 12.5 ms                                                     | 13.6 ms: 1.09x slower                                                              |
| Geometric mean             | (ref)                                                       | 1.21x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 44.0 ms: 1.16x faster                                                              |
| nbody          | 66.3 ms                                                     | 63.7 ms: 1.04x faster                                                              |
| pidigits       | 146 ms                                                      | 149 ms: 1.02x slower                                                               |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.2 ms: 1.68x faster                                                              |
| regex_effbot   | 1.69 ms                                                     | 1.45 ms: 1.17x faster                                                              |
| regex_dna      | 115 ms                                                      | 121 ms: 1.05x slower                                                               |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                       |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 88.7 ms: 1.04x faster                                                              |
| json_loads           | 15.1 us                                                     | 15.4 us: 1.02x slower                                                              |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.6 ms: 1.05x slower                                                              |
| xml_etree_generate   | 53.5 ms                                                     | 56.4 ms: 1.05x slower                                                              |
| unpickle_pure_python | 130 us                                                      | 139 us: 1.07x slower                                                               |
| xml_etree_process    | 36.5 ms                                                     | 39.7 ms: 1.09x slower                                                              |
| json_dumps           | 6.19 ms                                                     | 6.96 ms: 1.12x slower                                                              |
| pickle_pure_python   | 186 us                                                      | 212 us: 1.14x slower                                                               |
| Geometric mean       | (ref)                                                       | 1.06x slower                                                                       |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.2 ms: 1.07x slower                                                              |
| python_startup_no_site | 16.9 ms                                                     | 19.7 ms: 1.16x slower                                                              |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| genshi_text     | 15.2 ms                                                     | 14.7 ms: 1.03x faster                                                              |
| django_template | 20.3 ms                                                     | 24.4 ms: 1.20x slower                                                              |
| Geometric mean  | (ref)                                                       | 1.03x slower                                                                       |

Benchmark hidden because not significant (2): genshi_xml, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 32.1 ms: 2.35x faster                                                              |
| asyncio_websockets         | 300 ms                                                      | 157 ms: 1.91x faster                                                               |
| mdp                        | 1.43 sec                                                    | 777 ms: 1.84x faster                                                               |
| regex_v8                   | 23.8 ms                                                     | 14.2 ms: 1.68x faster                                                              |
| async_tree_memoization_tg  | 281 ms                                                      | 210 ms: 1.34x faster                                                               |
| deepcopy                   | 223 us                                                      | 167 us: 1.33x faster                                                               |
| async_tree_memoization     | 265 ms                                                      | 207 ms: 1.28x faster                                                               |
| deepcopy_memo              | 23.1 us                                                     | 18.2 us: 1.27x faster                                                              |
| async_tree_io              | 513 ms                                                      | 409 ms: 1.25x faster                                                               |
| async_tree_io_tg           | 497 ms                                                      | 400 ms: 1.24x faster                                                               |
| async_tree_none            | 219 ms                                                      | 180 ms: 1.22x faster                                                               |
| async_tree_none_tg         | 200 ms                                                      | 171 ms: 1.17x faster                                                               |
| regex_effbot               | 1.69 ms                                                     | 1.45 ms: 1.17x faster                                                              |
| float                      | 50.8 ms                                                     | 44.0 ms: 1.16x faster                                                              |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 334 ms: 1.14x faster                                                               |
| spectral_norm              | 63.4 ms                                                     | 57.0 ms: 1.11x faster                                                              |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 344 ms: 1.11x faster                                                               |
| deepcopy_reduce            | 2.02 us                                                     | 1.84 us: 1.10x faster                                                              |
| go                         | 84.7 ms                                                     | 77.3 ms: 1.10x faster                                                              |
| json                       | 3.30 ms                                                     | 3.08 ms: 1.07x faster                                                              |
| telco                      | 4.85 ms                                                     | 4.61 ms: 1.05x faster                                                              |
| nbody                      | 66.3 ms                                                     | 63.7 ms: 1.04x faster                                                              |
| xml_etree_parse            | 92.2 ms                                                     | 88.7 ms: 1.04x faster                                                              |
| genshi_text                | 15.2 ms                                                     | 14.7 ms: 1.03x faster                                                              |
| typing_runtime_protocols   | 103 us                                                      | 100 us: 1.03x faster                                                               |
| pyflate                    | 283 ms                                                      | 276 ms: 1.03x faster                                                               |
| meteor_contest             | 72.0 ms                                                     | 70.7 ms: 1.02x faster                                                              |
| scimark_sor                | 76.2 ms                                                     | 75.7 ms: 1.01x faster                                                              |
| scimark_monte_carlo        | 40.7 ms                                                     | 40.5 ms: 1.01x faster                                                              |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.61 ms: 1.00x slower                                                              |
| bpe_tokeniser              | 2.87 sec                                                    | 2.90 sec: 1.01x slower                                                             |
| logging_silent             | 54.6 ns                                                     | 55.4 ns: 1.01x slower                                                              |
| generators                 | 19.0 ms                                                     | 19.3 ms: 1.01x slower                                                              |
| json_loads                 | 15.1 us                                                     | 15.4 us: 1.02x slower                                                              |
| pidigits                   | 146 ms                                                      | 149 ms: 1.02x slower                                                               |
| html5lib                   | 38.2 ms                                                     | 38.9 ms: 1.02x slower                                                              |
| shortest_path              | 355 ms                                                      | 362 ms: 1.02x slower                                                               |
| pprint_safe_repr           | 485 ms                                                      | 494 ms: 1.02x slower                                                               |
| 2to3                       | 215 ms                                                      | 220 ms: 1.02x slower                                                               |
| comprehensions             | 10.4 us                                                     | 10.6 us: 1.02x slower                                                              |
| create_gc_cycles           | 1.22 ms                                                     | 1.26 ms: 1.03x slower                                                              |
| hexiom                     | 3.84 ms                                                     | 3.95 ms: 1.03x slower                                                              |
| pprint_pformat             | 977 ms                                                      | 1.00 sec: 1.03x slower                                                             |
| chaos                      | 37.9 ms                                                     | 39.1 ms: 1.03x slower                                                              |
| sphinx                     | 617 ms                                                      | 639 ms: 1.04x slower                                                               |
| connected_components       | 320 ms                                                      | 333 ms: 1.04x slower                                                               |
| async_generators           | 223 ms                                                      | 232 ms: 1.04x slower                                                               |
| dulwich_log                | 40.1 ms                                                     | 42.0 ms: 1.05x slower                                                              |
| richards                   | 26.3 ms                                                     | 27.5 ms: 1.05x slower                                                              |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.6 ms: 1.05x slower                                                              |
| regex_dna                  | 115 ms                                                      | 121 ms: 1.05x slower                                                               |
| crypto_pyaes               | 45.6 ms                                                     | 47.9 ms: 1.05x slower                                                              |
| xml_etree_generate         | 53.5 ms                                                     | 56.4 ms: 1.05x slower                                                              |
| richards_super             | 29.8 ms                                                     | 31.4 ms: 1.06x slower                                                              |
| gc_traversal               | 1.96 ms                                                     | 2.08 ms: 1.06x slower                                                              |
| bench_thread_pool          | 810 us                                                      | 864 us: 1.07x slower                                                               |
| unpickle_pure_python       | 130 us                                                      | 139 us: 1.07x slower                                                               |
| bench_mp_pool              | 84.2 ms                                                     | 90.2 ms: 1.07x slower                                                              |
| nqueens                    | 56.1 ms                                                     | 60.2 ms: 1.07x slower                                                              |
| scimark_fft                | 175 ms                                                      | 188 ms: 1.07x slower                                                               |
| python_startup             | 24.4 ms                                                     | 26.2 ms: 1.07x slower                                                              |
| docutils                   | 1.53 sec                                                    | 1.65 sec: 1.08x slower                                                             |
| coroutines                 | 12.5 ms                                                     | 13.6 ms: 1.09x slower                                                              |
| xml_etree_process          | 36.5 ms                                                     | 39.7 ms: 1.09x slower                                                              |
| logging_simple             | 5.77 us                                                     | 6.30 us: 1.09x slower                                                              |
| logging_format             | 6.18 us                                                     | 6.83 us: 1.11x slower                                                              |
| scimark_lu                 | 56.7 ms                                                     | 62.8 ms: 1.11x slower                                                              |
| json_dumps                 | 6.19 ms                                                     | 6.96 ms: 1.12x slower                                                              |
| coverage                   | 45.3 ms                                                     | 51.2 ms: 1.13x slower                                                              |
| pickle_pure_python         | 186 us                                                      | 212 us: 1.14x slower                                                               |
| raytrace                   | 153 ms                                                      | 176 ms: 1.15x slower                                                               |
| many_optionals             | 361 us                                                      | 420 us: 1.16x slower                                                               |
| deltablue                  | 1.89 ms                                                     | 2.20 ms: 1.16x slower                                                              |
| python_startup_no_site     | 16.9 ms                                                     | 19.7 ms: 1.16x slower                                                              |
| django_template            | 20.3 ms                                                     | 24.4 ms: 1.20x slower                                                              |
| subparsers                 | 10.9 ms                                                     | 15.7 ms: 1.45x slower                                                              |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                                       |

Benchmark hidden because not significant (8): genshi_xml, regex_compile, mako, sqlite_synth, fannkuch, k_core, tomli_loads, pycparser
Ignored benchmarks (16) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250430-3.14.0a7+-cad1946/bm-20250430-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.030x faster

# HPT report

- Reliability score: 84.88% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown