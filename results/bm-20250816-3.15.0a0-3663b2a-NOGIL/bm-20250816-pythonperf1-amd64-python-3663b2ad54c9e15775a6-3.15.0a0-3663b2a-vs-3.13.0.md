# Results vs. 3.13.0

- fork: python
- ref: 3663b2ad54c9e15775a6
- machine: windows-amd64
- commit hash: 3663b2a
- commit date: 2025-08-16
- overall geometric mean: 1.048x slower
- HPT reliability: 99.92%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 224 ms: 1.04x slower                                                       |
| docutils       | 1.53 sec                                                    | 2.79 sec: 1.82x slower                                                     |
| html5lib       | 38.2 ms                                                     | 39.2 ms: 1.03x slower                                                      |
| sphinx         | 617 ms                                                      | 642 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.19x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 146 ms: 2.06x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 322 ms: 1.54x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 187 ms: 1.50x faster                                                       |
| async_tree_io              | 513 ms                                                      | 344 ms: 1.49x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 145 ms: 1.38x faster                                                       |
| async_tree_none            | 219 ms                                                      | 168 ms: 1.31x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 207 ms: 1.28x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 304 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 326 ms: 1.17x faster                                                       |
| async_generators           | 223 ms                                                      | 258 ms: 1.16x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 15.4 ms: 1.23x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.29x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 45.6 ms: 1.11x faster                                                      |
| pidigits       | 146 ms                                                      | 134 ms: 1.09x faster                                                       |
| nbody          | 66.3 ms                                                     | 83.1 ms: 1.25x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.4 ms: 1.78x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.55 ms: 1.10x faster                                                      |
| regex_dna      | 115 ms                                                      | 113 ms: 1.02x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 92.6 ms: 1.15x slower                                                      |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 6.19 ms                                                     | 5.86 ms: 1.06x faster                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 57.7 ms: 1.05x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 90.4 ms: 1.02x faster                                                      |
| json_loads           | 15.1 us                                                     | 15.5 us: 1.02x slower                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 63.1 ms: 1.18x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 44.4 ms: 1.22x slower                                                      |
| unpickle_pure_python | 130 us                                                      | 159 us: 1.22x slower                                                       |
| pickle_pure_python   | 186 us                                                      | 235 us: 1.26x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 2.42 sec: 1.77x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.15x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.4 ms: 1.04x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.1 ms: 1.13x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.08x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 33.9 ms                                                     | 40.7 ms: 1.20x slower                                                      |
| genshi_text     | 15.2 ms                                                     | 19.4 ms: 1.27x slower                                                      |
| django_template | 20.3 ms                                                     | 27.2 ms: 1.34x slower                                                      |
| mako            | 6.56 ms                                                     | 9.92 ms: 1.51x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.33x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 571 us: 14.84x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 28.7 ms: 2.63x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 146 ms: 2.06x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 13.4 ms: 1.78x faster                                                      |
| gc_traversal               | 1.96 ms                                                     | 1.14 ms: 1.72x faster                                                      |
| async_tree_io_tg           | 497 ms                                                      | 322 ms: 1.54x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 187 ms: 1.50x faster                                                       |
| async_tree_io              | 513 ms                                                      | 344 ms: 1.49x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 145 ms: 1.38x faster                                                       |
| mdp                        | 1.43 sec                                                    | 1.05 sec: 1.36x faster                                                     |
| async_tree_none            | 219 ms                                                      | 168 ms: 1.31x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 207 ms: 1.28x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 304 ms: 1.26x faster                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 982 us: 1.25x faster                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.34 us: 1.19x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 326 ms: 1.17x faster                                                       |
| float                      | 50.8 ms                                                     | 45.6 ms: 1.11x faster                                                      |
| deepcopy_memo              | 23.1 us                                                     | 21.0 us: 1.10x faster                                                      |
| json                       | 3.30 ms                                                     | 3.00 ms: 1.10x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.55 ms: 1.10x faster                                                      |
| pidigits                   | 146 ms                                                      | 134 ms: 1.09x faster                                                       |
| deepcopy                   | 223 us                                                      | 205 us: 1.09x faster                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 77.5 ms: 1.09x faster                                                      |
| json_dumps                 | 6.19 ms                                                     | 5.86 ms: 1.06x faster                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 57.7 ms: 1.05x faster                                                      |
| regex_dna                  | 115 ms                                                      | 113 ms: 1.02x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 90.4 ms: 1.02x faster                                                      |
| dulwich_log                | 40.1 ms                                                     | 40.8 ms: 1.02x slower                                                      |
| json_loads                 | 15.1 us                                                     | 15.5 us: 1.02x slower                                                      |
| html5lib                   | 38.2 ms                                                     | 39.2 ms: 1.03x slower                                                      |
| telco                      | 4.85 ms                                                     | 5.03 ms: 1.04x slower                                                      |
| 2to3                       | 215 ms                                                      | 224 ms: 1.04x slower                                                       |
| sphinx                     | 617 ms                                                      | 642 ms: 1.04x slower                                                       |
| python_startup             | 24.4 ms                                                     | 25.4 ms: 1.04x slower                                                      |
| go                         | 84.7 ms                                                     | 91.5 ms: 1.08x slower                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 2.19 us: 1.08x slower                                                      |
| pyflate                    | 283 ms                                                      | 309 ms: 1.09x slower                                                       |
| sympy_expand               | 286 ms                                                      | 316 ms: 1.11x slower                                                       |
| sympy_str                  | 167 ms                                                      | 187 ms: 1.12x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 95.5 ms: 1.12x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 13.9 ms: 1.13x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 19.1 ms: 1.13x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 64.0 ms: 1.13x slower                                                      |
| logging_format             | 6.18 us                                                     | 7.00 us: 1.13x slower                                                      |
| scimark_sor                | 76.2 ms                                                     | 86.4 ms: 1.13x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 62.0 ns: 1.14x slower                                                      |
| logging_simple             | 5.77 us                                                     | 6.58 us: 1.14x slower                                                      |
| regex_compile              | 80.7 ms                                                     | 92.6 ms: 1.15x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 560 ms: 1.16x slower                                                       |
| async_generators           | 223 ms                                                      | 258 ms: 1.16x slower                                                       |
| comprehensions             | 10.4 us                                                     | 12.1 us: 1.17x slower                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 3.07 ms: 1.18x slower                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 63.1 ms: 1.18x slower                                                      |
| fannkuch                   | 252 ms                                                      | 299 ms: 1.19x slower                                                       |
| generators                 | 19.0 ms                                                     | 22.5 ms: 1.19x slower                                                      |
| chaos                      | 37.9 ms                                                     | 45.2 ms: 1.19x slower                                                      |
| meteor_contest             | 72.0 ms                                                     | 85.9 ms: 1.19x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.59 ms: 1.19x slower                                                      |
| genshi_xml                 | 33.9 ms                                                     | 40.7 ms: 1.20x slower                                                      |
| scimark_fft                | 175 ms                                                      | 211 ms: 1.21x slower                                                       |
| spectral_norm              | 63.4 ms                                                     | 76.9 ms: 1.21x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 44.4 ms: 1.22x slower                                                      |
| unpickle_pure_python       | 130 us                                                      | 159 us: 1.22x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 15.4 ms: 1.23x slower                                                      |
| typing_runtime_protocols   | 103 us                                                      | 127 us: 1.23x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 56.2 ms: 1.23x slower                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 50.9 ms: 1.25x slower                                                      |
| nbody                      | 66.3 ms                                                     | 83.1 ms: 1.25x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 235 us: 1.26x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 19.4 ms: 1.27x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 72.1 ms: 1.28x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.44 ms: 1.29x slower                                                      |
| richards                   | 26.3 ms                                                     | 34.1 ms: 1.30x slower                                                      |
| bench_thread_pool          | 810 us                                                      | 1.06 ms: 1.31x slower                                                      |
| richards_super             | 29.8 ms                                                     | 39.9 ms: 1.34x slower                                                      |
| django_template            | 20.3 ms                                                     | 27.2 ms: 1.34x slower                                                      |
| raytrace                   | 153 ms                                                      | 207 ms: 1.35x slower                                                       |
| coverage                   | 45.3 ms                                                     | 67.7 ms: 1.49x slower                                                      |
| mako                       | 6.56 ms                                                     | 9.92 ms: 1.51x slower                                                      |
| k_core                     | 1.70 sec                                                    | 2.60 sec: 1.53x slower                                                     |
| pprint_pformat             | 977 ms                                                      | 1.63 sec: 1.67x slower                                                     |
| many_optionals             | 361 us                                                      | 608 us: 1.68x slower                                                       |
| shortest_path              | 355 ms                                                      | 607 ms: 1.71x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 2.42 sec: 1.77x slower                                                     |
| docutils                   | 1.53 sec                                                    | 2.79 sec: 1.82x slower                                                     |
| connected_components       | 320 ms                                                      | 583 ms: 1.82x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 5.33 sec: 1.86x slower                                                     |
| subparsers                 | 10.9 ms                                                     | 34.0 ms: 3.13x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.05x slower                                                               |

Benchmark hidden because not significant (2): pylint, pycparser
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250816-3.15.0a0-3663b2a-NOGIL/bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.048x slower

# HPT report

- Reliability score: 99.92% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown