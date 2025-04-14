# Results vs. 3.13.0

- fork: faster-cpython
- ref: trashcan_in_dealloc
- machine: windows-amd64
- commit hash: 3514aa1
- commit date: 2025-04-09
- overall geometric mean: 1.043x faster
- HPT reliability: 58.24%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 218 ms: 1.01x slower                                                                 |
| docutils       | 1.53 sec                                                    | 1.65 sec: 1.08x slower                                                               |
| sphinx         | 617 ms                                                      | 639 ms: 1.04x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                         |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 159 ms: 1.89x faster                                                                 |
| async_tree_memoization_tg  | 281 ms                                                      | 207 ms: 1.35x faster                                                                 |
| async_tree_memoization     | 265 ms                                                      | 203 ms: 1.30x faster                                                                 |
| async_tree_io_tg           | 497 ms                                                      | 394 ms: 1.26x faster                                                                 |
| async_tree_io              | 513 ms                                                      | 409 ms: 1.25x faster                                                                 |
| async_tree_none            | 219 ms                                                      | 178 ms: 1.23x faster                                                                 |
| async_tree_none_tg         | 200 ms                                                      | 168 ms: 1.19x faster                                                                 |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 329 ms: 1.16x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 336 ms: 1.14x faster                                                                 |
| async_generators           | 223 ms                                                      | 227 ms: 1.02x slower                                                                 |
| coroutines                 | 12.5 ms                                                     | 13.9 ms: 1.11x slower                                                                |
| Geometric mean             | (ref)                                                       | 1.22x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 42.2 ms: 1.21x faster                                                                |
| nbody          | 66.3 ms                                                     | 61.3 ms: 1.08x faster                                                                |
| pidigits       | 146 ms                                                      | 148 ms: 1.01x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.4 ms: 1.66x faster                                                                |
| regex_effbot   | 1.69 ms                                                     | 1.45 ms: 1.17x faster                                                                |
| regex_compile  | 80.7 ms                                                     | 78.5 ms: 1.03x faster                                                                |
| regex_dna      | 115 ms                                                      | 116 ms: 1.01x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 90.0 ms: 1.02x faster                                                                |
| tomli_loads          | 1.37 sec                                                    | 1.36 sec: 1.01x faster                                                               |
| json_loads           | 15.1 us                                                     | 14.9 us: 1.01x faster                                                                |
| unpickle_pure_python | 130 us                                                      | 132 us: 1.02x slower                                                                 |
| xml_etree_generate   | 53.5 ms                                                     | 54.8 ms: 1.03x slower                                                                |
| xml_etree_process    | 36.5 ms                                                     | 38.8 ms: 1.06x slower                                                                |
| xml_etree_iterparse  | 60.5 ms                                                     | 64.4 ms: 1.06x slower                                                                |
| json_dumps           | 6.19 ms                                                     | 6.73 ms: 1.09x slower                                                                |
| pickle_pure_python   | 186 us                                                      | 208 us: 1.12x slower                                                                 |
| Geometric mean       | (ref)                                                       | 1.04x slower                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.3 ms: 1.04x slower                                                                |
| python_startup_no_site | 16.9 ms                                                     | 19.7 ms: 1.16x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| genshi_xml      | 33.9 ms                                                     | 32.7 ms: 1.04x faster                                                                |
| genshi_text     | 15.2 ms                                                     | 14.9 ms: 1.02x faster                                                                |
| mako            | 6.56 ms                                                     | 6.65 ms: 1.01x slower                                                                |
| django_template | 20.3 ms                                                     | 23.9 ms: 1.18x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.03x slower                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 28.4 ms: 2.65x faster                                                                |
| asyncio_websockets         | 300 ms                                                      | 159 ms: 1.89x faster                                                                 |
| mdp                        | 1.43 sec                                                    | 782 ms: 1.83x faster                                                                 |
| regex_v8                   | 23.8 ms                                                     | 14.4 ms: 1.66x faster                                                                |
| async_tree_memoization_tg  | 281 ms                                                      | 207 ms: 1.35x faster                                                                 |
| deepcopy                   | 223 us                                                      | 169 us: 1.32x faster                                                                 |
| async_tree_memoization     | 265 ms                                                      | 203 ms: 1.30x faster                                                                 |
| deepcopy_memo              | 23.1 us                                                     | 18.2 us: 1.27x faster                                                                |
| async_tree_io_tg           | 497 ms                                                      | 394 ms: 1.26x faster                                                                 |
| async_tree_io              | 513 ms                                                      | 409 ms: 1.25x faster                                                                 |
| async_tree_none            | 219 ms                                                      | 178 ms: 1.23x faster                                                                 |
| float                      | 50.8 ms                                                     | 42.2 ms: 1.21x faster                                                                |
| async_tree_none_tg         | 200 ms                                                      | 168 ms: 1.19x faster                                                                 |
| spectral_norm              | 63.4 ms                                                     | 53.7 ms: 1.18x faster                                                                |
| regex_effbot               | 1.69 ms                                                     | 1.45 ms: 1.17x faster                                                                |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 329 ms: 1.16x faster                                                                 |
| deepcopy_reduce            | 2.02 us                                                     | 1.77 us: 1.14x faster                                                                |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 336 ms: 1.14x faster                                                                 |
| go                         | 84.7 ms                                                     | 75.8 ms: 1.12x faster                                                                |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.41 ms: 1.08x faster                                                                |
| nbody                      | 66.3 ms                                                     | 61.3 ms: 1.08x faster                                                                |
| scimark_monte_carlo        | 40.7 ms                                                     | 37.8 ms: 1.08x faster                                                                |
| telco                      | 4.85 ms                                                     | 4.61 ms: 1.05x faster                                                                |
| scimark_sor                | 76.2 ms                                                     | 72.7 ms: 1.05x faster                                                                |
| json                       | 3.30 ms                                                     | 3.15 ms: 1.05x faster                                                                |
| genshi_xml                 | 33.9 ms                                                     | 32.7 ms: 1.04x faster                                                                |
| scimark_fft                | 175 ms                                                      | 169 ms: 1.03x faster                                                                 |
| regex_compile              | 80.7 ms                                                     | 78.5 ms: 1.03x faster                                                                |
| xml_etree_parse            | 92.2 ms                                                     | 90.0 ms: 1.02x faster                                                                |
| genshi_text                | 15.2 ms                                                     | 14.9 ms: 1.02x faster                                                                |
| chaos                      | 37.9 ms                                                     | 37.4 ms: 1.01x faster                                                                |
| tomli_loads                | 1.37 sec                                                    | 1.36 sec: 1.01x faster                                                               |
| json_loads                 | 15.1 us                                                     | 14.9 us: 1.01x faster                                                                |
| shortest_path              | 355 ms                                                      | 352 ms: 1.01x faster                                                                 |
| logging_silent             | 54.6 ns                                                     | 54.2 ns: 1.01x faster                                                                |
| bpe_tokeniser              | 2.87 sec                                                    | 2.88 sec: 1.00x slower                                                               |
| sympy_integrate            | 12.3 ms                                                     | 12.4 ms: 1.00x slower                                                                |
| meteor_contest             | 72.0 ms                                                     | 72.5 ms: 1.01x slower                                                                |
| fannkuch                   | 252 ms                                                      | 254 ms: 1.01x slower                                                                 |
| regex_dna                  | 115 ms                                                      | 116 ms: 1.01x slower                                                                 |
| pidigits                   | 146 ms                                                      | 148 ms: 1.01x slower                                                                 |
| dulwich_log                | 40.1 ms                                                     | 40.5 ms: 1.01x slower                                                                |
| typing_runtime_protocols   | 103 us                                                      | 104 us: 1.01x slower                                                                 |
| sympy_expand               | 286 ms                                                      | 289 ms: 1.01x slower                                                                 |
| 2to3                       | 215 ms                                                      | 218 ms: 1.01x slower                                                                 |
| connected_components       | 320 ms                                                      | 324 ms: 1.01x slower                                                                 |
| sympy_str                  | 167 ms                                                      | 169 ms: 1.01x slower                                                                 |
| mako                       | 6.56 ms                                                     | 6.65 ms: 1.01x slower                                                                |
| hexiom                     | 3.84 ms                                                     | 3.90 ms: 1.01x slower                                                                |
| pyflate                    | 283 ms                                                      | 287 ms: 1.02x slower                                                                 |
| pprint_safe_repr           | 485 ms                                                      | 493 ms: 1.02x slower                                                                 |
| unpickle_pure_python       | 130 us                                                      | 132 us: 1.02x slower                                                                 |
| richards                   | 26.3 ms                                                     | 26.7 ms: 1.02x slower                                                                |
| async_generators           | 223 ms                                                      | 227 ms: 1.02x slower                                                                 |
| sympy_sum                  | 85.2 ms                                                     | 87.2 ms: 1.02x slower                                                                |
| xml_etree_generate         | 53.5 ms                                                     | 54.8 ms: 1.03x slower                                                                |
| crypto_pyaes               | 45.6 ms                                                     | 46.8 ms: 1.03x slower                                                                |
| richards_super             | 29.8 ms                                                     | 30.6 ms: 1.03x slower                                                                |
| bench_mp_pool              | 84.2 ms                                                     | 86.8 ms: 1.03x slower                                                                |
| sphinx                     | 617 ms                                                      | 639 ms: 1.04x slower                                                                 |
| pprint_pformat             | 977 ms                                                      | 1.01 sec: 1.04x slower                                                               |
| python_startup             | 24.4 ms                                                     | 25.3 ms: 1.04x slower                                                                |
| bench_thread_pool          | 810 us                                                      | 843 us: 1.04x slower                                                                 |
| nqueens                    | 56.1 ms                                                     | 59.3 ms: 1.06x slower                                                                |
| logging_simple             | 5.77 us                                                     | 6.12 us: 1.06x slower                                                                |
| xml_etree_process          | 36.5 ms                                                     | 38.8 ms: 1.06x slower                                                                |
| xml_etree_iterparse        | 60.5 ms                                                     | 64.4 ms: 1.06x slower                                                                |
| gc_traversal               | 1.96 ms                                                     | 2.10 ms: 1.07x slower                                                                |
| logging_format             | 6.18 us                                                     | 6.64 us: 1.08x slower                                                                |
| docutils                   | 1.53 sec                                                    | 1.65 sec: 1.08x slower                                                               |
| json_dumps                 | 6.19 ms                                                     | 6.73 ms: 1.09x slower                                                                |
| comprehensions             | 10.4 us                                                     | 11.5 us: 1.11x slower                                                                |
| deltablue                  | 1.89 ms                                                     | 2.11 ms: 1.11x slower                                                                |
| coroutines                 | 12.5 ms                                                     | 13.9 ms: 1.11x slower                                                                |
| pickle_pure_python         | 186 us                                                      | 208 us: 1.12x slower                                                                 |
| raytrace                   | 153 ms                                                      | 173 ms: 1.13x slower                                                                 |
| coverage                   | 45.3 ms                                                     | 51.3 ms: 1.13x slower                                                                |
| python_startup_no_site     | 16.9 ms                                                     | 19.7 ms: 1.16x slower                                                                |
| django_template            | 20.3 ms                                                     | 23.9 ms: 1.18x slower                                                                |
| many_optionals             | 361 us                                                      | 427 us: 1.18x slower                                                                 |
| subparsers                 | 10.9 ms                                                     | 15.6 ms: 1.43x slower                                                                |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                                         |

Benchmark hidden because not significant (8): pylint, html5lib, k_core, generators, create_gc_cycles, scimark_lu, sqlite_synth, pycparser
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250409-3.14.0a7+-3514aa1/bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.043x faster

# HPT report

- Reliability score: 58.24% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown