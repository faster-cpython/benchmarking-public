# Results vs. 3.13.0

- fork: faster-cpython
- ref: trashcan_in_dealloc
- machine: windows-amd64
- commit hash: 8aa20f2
- commit date: 2025-04-09
- overall geometric mean: 1.041x faster
- HPT reliability: 72.66%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 217 ms: 1.01x slower                                                                 |
| docutils       | 1.53 sec                                                    | 1.63 sec: 1.07x slower                                                               |
| sphinx         | 617 ms                                                      | 635 ms: 1.03x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                         |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 156 ms: 1.93x faster                                                                 |
| async_tree_memoization_tg  | 281 ms                                                      | 207 ms: 1.36x faster                                                                 |
| async_tree_memoization     | 265 ms                                                      | 203 ms: 1.31x faster                                                                 |
| async_tree_io_tg           | 497 ms                                                      | 393 ms: 1.26x faster                                                                 |
| async_tree_io              | 513 ms                                                      | 406 ms: 1.26x faster                                                                 |
| async_tree_none            | 219 ms                                                      | 177 ms: 1.24x faster                                                                 |
| async_tree_none_tg         | 200 ms                                                      | 168 ms: 1.19x faster                                                                 |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 328 ms: 1.16x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 336 ms: 1.14x faster                                                                 |
| async_generators           | 223 ms                                                      | 226 ms: 1.01x slower                                                                 |
| coroutines                 | 12.5 ms                                                     | 13.2 ms: 1.06x slower                                                                |
| Geometric mean             | (ref)                                                       | 1.23x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 41.9 ms: 1.21x faster                                                                |
| nbody          | 66.3 ms                                                     | 61.8 ms: 1.07x faster                                                                |
| pidigits       | 146 ms                                                      | 148 ms: 1.01x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.8 ms: 1.73x faster                                                                |
| regex_effbot   | 1.69 ms                                                     | 1.48 ms: 1.15x faster                                                                |
| regex_compile  | 80.7 ms                                                     | 79.2 ms: 1.02x faster                                                                |
| regex_dna      | 115 ms                                                      | 116 ms: 1.01x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.19x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 89.5 ms: 1.03x faster                                                                |
| tomli_loads          | 1.37 sec                                                    | 1.34 sec: 1.03x faster                                                               |
| unpickle_pure_python | 130 us                                                      | 131 us: 1.01x slower                                                                 |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.0 ms: 1.04x slower                                                                |
| xml_etree_generate   | 53.5 ms                                                     | 55.8 ms: 1.04x slower                                                                |
| xml_etree_process    | 36.5 ms                                                     | 39.3 ms: 1.08x slower                                                                |
| json_dumps           | 6.19 ms                                                     | 6.81 ms: 1.10x slower                                                                |
| pickle_pure_python   | 186 us                                                      | 207 us: 1.11x slower                                                                 |
| Geometric mean       | (ref)                                                       | 1.04x slower                                                                         |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.0 ms: 1.02x slower                                                                |
| python_startup_no_site | 16.9 ms                                                     | 19.5 ms: 1.16x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.09x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.50 ms: 1.01x faster                                                                |
| genshi_text     | 15.2 ms                                                     | 15.3 ms: 1.01x slower                                                                |
| django_template | 20.3 ms                                                     | 24.0 ms: 1.18x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.04x slower                                                                         |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 28.5 ms: 2.65x faster                                                                |
| asyncio_websockets         | 300 ms                                                      | 156 ms: 1.93x faster                                                                 |
| mdp                        | 1.43 sec                                                    | 797 ms: 1.80x faster                                                                 |
| regex_v8                   | 23.8 ms                                                     | 13.8 ms: 1.73x faster                                                                |
| async_tree_memoization_tg  | 281 ms                                                      | 207 ms: 1.36x faster                                                                 |
| async_tree_memoization     | 265 ms                                                      | 203 ms: 1.31x faster                                                                 |
| deepcopy                   | 223 us                                                      | 171 us: 1.31x faster                                                                 |
| deepcopy_memo              | 23.1 us                                                     | 17.8 us: 1.30x faster                                                                |
| async_tree_io_tg           | 497 ms                                                      | 393 ms: 1.26x faster                                                                 |
| async_tree_io              | 513 ms                                                      | 406 ms: 1.26x faster                                                                 |
| async_tree_none            | 219 ms                                                      | 177 ms: 1.24x faster                                                                 |
| float                      | 50.8 ms                                                     | 41.9 ms: 1.21x faster                                                                |
| async_tree_none_tg         | 200 ms                                                      | 168 ms: 1.19x faster                                                                 |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 328 ms: 1.16x faster                                                                 |
| regex_effbot               | 1.69 ms                                                     | 1.48 ms: 1.15x faster                                                                |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 336 ms: 1.14x faster                                                                 |
| go                         | 84.7 ms                                                     | 75.5 ms: 1.12x faster                                                                |
| deepcopy_reduce            | 2.02 us                                                     | 1.81 us: 1.12x faster                                                                |
| spectral_norm              | 63.4 ms                                                     | 58.0 ms: 1.09x faster                                                                |
| nbody                      | 66.3 ms                                                     | 61.8 ms: 1.07x faster                                                                |
| scimark_monte_carlo        | 40.7 ms                                                     | 38.1 ms: 1.07x faster                                                                |
| json                       | 3.30 ms                                                     | 3.16 ms: 1.05x faster                                                                |
| telco                      | 4.85 ms                                                     | 4.64 ms: 1.04x faster                                                                |
| scimark_sor                | 76.2 ms                                                     | 73.8 ms: 1.03x faster                                                                |
| xml_etree_parse            | 92.2 ms                                                     | 89.5 ms: 1.03x faster                                                                |
| tomli_loads                | 1.37 sec                                                    | 1.34 sec: 1.03x faster                                                               |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.55 ms: 1.02x faster                                                                |
| regex_compile              | 80.7 ms                                                     | 79.2 ms: 1.02x faster                                                                |
| fannkuch                   | 252 ms                                                      | 248 ms: 1.01x faster                                                                 |
| mako                       | 6.56 ms                                                     | 6.50 ms: 1.01x faster                                                                |
| generators                 | 19.0 ms                                                     | 18.8 ms: 1.01x faster                                                                |
| sqlite_synth               | 1.59 us                                                     | 1.58 us: 1.01x faster                                                                |
| meteor_contest             | 72.0 ms                                                     | 72.3 ms: 1.00x slower                                                                |
| genshi_text                | 15.2 ms                                                     | 15.3 ms: 1.01x slower                                                                |
| 2to3                       | 215 ms                                                      | 217 ms: 1.01x slower                                                                 |
| pidigits                   | 146 ms                                                      | 148 ms: 1.01x slower                                                                 |
| connected_components       | 320 ms                                                      | 323 ms: 1.01x slower                                                                 |
| regex_dna                  | 115 ms                                                      | 116 ms: 1.01x slower                                                                 |
| unpickle_pure_python       | 130 us                                                      | 131 us: 1.01x slower                                                                 |
| pprint_safe_repr           | 485 ms                                                      | 490 ms: 1.01x slower                                                                 |
| scimark_lu                 | 56.7 ms                                                     | 57.4 ms: 1.01x slower                                                                |
| async_generators           | 223 ms                                                      | 226 ms: 1.01x slower                                                                 |
| richards                   | 26.3 ms                                                     | 26.7 ms: 1.02x slower                                                                |
| sympy_integrate            | 12.3 ms                                                     | 12.5 ms: 1.02x slower                                                                |
| pyflate                    | 283 ms                                                      | 288 ms: 1.02x slower                                                                 |
| sympy_expand               | 286 ms                                                      | 291 ms: 1.02x slower                                                                 |
| bpe_tokeniser              | 2.87 sec                                                    | 2.93 sec: 1.02x slower                                                               |
| dulwich_log                | 40.1 ms                                                     | 41.0 ms: 1.02x slower                                                                |
| scimark_fft                | 175 ms                                                      | 179 ms: 1.02x slower                                                                 |
| python_startup             | 24.4 ms                                                     | 25.0 ms: 1.02x slower                                                                |
| sympy_str                  | 167 ms                                                      | 171 ms: 1.02x slower                                                                 |
| richards_super             | 29.8 ms                                                     | 30.5 ms: 1.03x slower                                                                |
| bench_mp_pool              | 84.2 ms                                                     | 86.4 ms: 1.03x slower                                                                |
| typing_runtime_protocols   | 103 us                                                      | 106 us: 1.03x slower                                                                 |
| sphinx                     | 617 ms                                                      | 635 ms: 1.03x slower                                                                 |
| pprint_pformat             | 977 ms                                                      | 1.01 sec: 1.03x slower                                                               |
| hexiom                     | 3.84 ms                                                     | 3.98 ms: 1.04x slower                                                                |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.0 ms: 1.04x slower                                                                |
| logging_simple             | 5.77 us                                                     | 6.01 us: 1.04x slower                                                                |
| bench_thread_pool          | 810 us                                                      | 844 us: 1.04x slower                                                                 |
| sympy_sum                  | 85.2 ms                                                     | 88.8 ms: 1.04x slower                                                                |
| crypto_pyaes               | 45.6 ms                                                     | 47.6 ms: 1.04x slower                                                                |
| xml_etree_generate         | 53.5 ms                                                     | 55.8 ms: 1.04x slower                                                                |
| logging_format             | 6.18 us                                                     | 6.51 us: 1.05x slower                                                                |
| coroutines                 | 12.5 ms                                                     | 13.2 ms: 1.06x slower                                                                |
| docutils                   | 1.53 sec                                                    | 1.63 sec: 1.07x slower                                                               |
| gc_traversal               | 1.96 ms                                                     | 2.10 ms: 1.07x slower                                                                |
| xml_etree_process          | 36.5 ms                                                     | 39.3 ms: 1.08x slower                                                                |
| nqueens                    | 56.1 ms                                                     | 60.6 ms: 1.08x slower                                                                |
| comprehensions             | 10.4 us                                                     | 11.3 us: 1.09x slower                                                                |
| coverage                   | 45.3 ms                                                     | 49.8 ms: 1.10x slower                                                                |
| json_dumps                 | 6.19 ms                                                     | 6.81 ms: 1.10x slower                                                                |
| pickle_pure_python         | 186 us                                                      | 207 us: 1.11x slower                                                                 |
| deltablue                  | 1.89 ms                                                     | 2.11 ms: 1.11x slower                                                                |
| raytrace                   | 153 ms                                                      | 174 ms: 1.13x slower                                                                 |
| python_startup_no_site     | 16.9 ms                                                     | 19.5 ms: 1.16x slower                                                                |
| many_optionals             | 361 us                                                      | 427 us: 1.18x slower                                                                 |
| django_template            | 20.3 ms                                                     | 24.0 ms: 1.18x slower                                                                |
| subparsers                 | 10.9 ms                                                     | 15.8 ms: 1.46x slower                                                                |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                                         |

Benchmark hidden because not significant (10): pylint, k_core, genshi_xml, shortest_path, chaos, html5lib, logging_silent, json_loads, create_gc_cycles, pycparser
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250409-3.14.0a7+-8aa20f2/bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.041x faster

# HPT report

- Reliability score: 72.66% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown