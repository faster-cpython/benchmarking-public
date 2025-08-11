# Results vs. 3.13.0

- fork: python
- ref: 046a4e39b3f8ac5cb13e
- machine: windows-amd64
- commit hash: 046a4e3
- commit date: 2025-08-09
- overall geometric mean: 1.066x slower
- HPT reliability: 99.94%
- HPT 99th percentile: 1.06x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 225 ms: 1.04x slower                                                       |
| docutils       | 1.53 sec                                                    | 2.79 sec: 1.82x slower                                                     |
| html5lib       | 38.2 ms                                                     | 40.4 ms: 1.06x slower                                                      |
| sphinx         | 617 ms                                                      | 667 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                       | 1.22x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 138 ms: 2.17x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 328 ms: 1.52x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 190 ms: 1.47x faster                                                       |
| async_tree_io              | 513 ms                                                      | 352 ms: 1.46x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 148 ms: 1.35x faster                                                       |
| async_tree_none            | 219 ms                                                      | 171 ms: 1.28x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 210 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 303 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 325 ms: 1.17x faster                                                       |
| async_generators           | 223 ms                                                      | 256 ms: 1.15x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 15.3 ms: 1.23x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.29x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 45.8 ms: 1.11x faster                                                      |
| pidigits       | 146 ms                                                      | 136 ms: 1.08x faster                                                       |
| nbody          | 66.3 ms                                                     | 85.0 ms: 1.28x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.1 ms: 1.82x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.61 ms: 1.05x faster                                                      |
| regex_dna      | 115 ms                                                      | 113 ms: 1.02x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 93.6 ms: 1.16x slower                                                      |
| Geometric mean | (ref)                                                       | 1.14x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 60.5 ms                                                     | 57.4 ms: 1.05x faster                                                      |
| json_dumps           | 6.19 ms                                                     | 5.89 ms: 1.05x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 89.4 ms: 1.03x faster                                                      |
| json_loads           | 15.1 us                                                     | 15.6 us: 1.03x slower                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 61.9 ms: 1.16x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 44.3 ms: 1.21x slower                                                      |
| unpickle_pure_python | 130 us                                                      | 160 us: 1.23x slower                                                       |
| pickle_pure_python   | 186 us                                                      | 237 us: 1.28x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 2.67 sec: 1.95x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.16x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.5 ms: 1.09x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.8 ms: 1.17x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 33.9 ms                                                     | 41.4 ms: 1.22x slower                                                      |
| django_template | 20.3 ms                                                     | 26.9 ms: 1.32x slower                                                      |
| genshi_text     | 15.2 ms                                                     | 20.2 ms: 1.33x slower                                                      |
| mako            | 6.56 ms                                                     | 9.93 ms: 1.51x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.34x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 567 us: 14.92x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 138 ms: 2.17x faster                                                       |
| pathlib                    | 75.3 ms                                                     | 36.1 ms: 2.09x faster                                                      |
| regex_v8                   | 23.8 ms                                                     | 13.1 ms: 1.82x faster                                                      |
| gc_traversal               | 1.96 ms                                                     | 1.20 ms: 1.63x faster                                                      |
| async_tree_io_tg           | 497 ms                                                      | 328 ms: 1.52x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 190 ms: 1.47x faster                                                       |
| async_tree_io              | 513 ms                                                      | 352 ms: 1.46x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 148 ms: 1.35x faster                                                       |
| async_tree_none            | 219 ms                                                      | 171 ms: 1.28x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 210 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 303 ms: 1.26x faster                                                       |
| mdp                        | 1.43 sec                                                    | 1.15 sec: 1.25x faster                                                     |
| create_gc_cycles           | 1.22 ms                                                     | 1.02 ms: 1.20x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 325 ms: 1.17x faster                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.36 us: 1.17x faster                                                      |
| float                      | 50.8 ms                                                     | 45.8 ms: 1.11x faster                                                      |
| pidigits                   | 146 ms                                                      | 136 ms: 1.08x faster                                                       |
| json                       | 3.30 ms                                                     | 3.06 ms: 1.08x faster                                                      |
| deepcopy                   | 223 us                                                      | 207 us: 1.08x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 21.5 us: 1.07x faster                                                      |
| bench_mp_pool              | 84.2 ms                                                     | 79.2 ms: 1.06x faster                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 57.4 ms: 1.05x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.61 ms: 1.05x faster                                                      |
| json_dumps                 | 6.19 ms                                                     | 5.89 ms: 1.05x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 89.4 ms: 1.03x faster                                                      |
| regex_dna                  | 115 ms                                                      | 113 ms: 1.02x faster                                                       |
| json_loads                 | 15.1 us                                                     | 15.6 us: 1.03x slower                                                      |
| 2to3                       | 215 ms                                                      | 225 ms: 1.04x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 41.9 ms: 1.05x slower                                                      |
| html5lib                   | 38.2 ms                                                     | 40.4 ms: 1.06x slower                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 2.14 us: 1.06x slower                                                      |
| pycparser                  | 695 ms                                                      | 738 ms: 1.06x slower                                                       |
| telco                      | 4.85 ms                                                     | 5.19 ms: 1.07x slower                                                      |
| sphinx                     | 617 ms                                                      | 667 ms: 1.08x slower                                                       |
| python_startup             | 24.4 ms                                                     | 26.5 ms: 1.09x slower                                                      |
| go                         | 84.7 ms                                                     | 92.3 ms: 1.09x slower                                                      |
| sympy_str                  | 167 ms                                                      | 187 ms: 1.12x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 61.4 ns: 1.12x slower                                                      |
| sympy_sum                  | 85.2 ms                                                     | 95.8 ms: 1.12x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 14.0 ms: 1.13x slower                                                      |
| pyflate                    | 283 ms                                                      | 321 ms: 1.13x slower                                                       |
| sympy_expand               | 286 ms                                                      | 325 ms: 1.14x slower                                                       |
| async_generators           | 223 ms                                                      | 256 ms: 1.15x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.65 us: 1.15x slower                                                      |
| logging_format             | 6.18 us                                                     | 7.14 us: 1.16x slower                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 61.9 ms: 1.16x slower                                                      |
| regex_compile              | 80.7 ms                                                     | 93.6 ms: 1.16x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 65.8 ms: 1.16x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 567 ms: 1.17x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 19.8 ms: 1.17x slower                                                      |
| comprehensions             | 10.4 us                                                     | 12.2 us: 1.18x slower                                                      |
| scimark_sor                | 76.2 ms                                                     | 90.3 ms: 1.18x slower                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 3.09 ms: 1.19x slower                                                      |
| meteor_contest             | 72.0 ms                                                     | 85.6 ms: 1.19x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 44.3 ms: 1.21x slower                                                      |
| spectral_norm              | 63.4 ms                                                     | 77.1 ms: 1.22x slower                                                      |
| genshi_xml                 | 33.9 ms                                                     | 41.4 ms: 1.22x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 15.3 ms: 1.23x slower                                                      |
| unpickle_pure_python       | 130 us                                                      | 160 us: 1.23x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.74 ms: 1.23x slower                                                      |
| scimark_fft                | 175 ms                                                      | 217 ms: 1.24x slower                                                       |
| chaos                      | 37.9 ms                                                     | 47.0 ms: 1.24x slower                                                      |
| generators                 | 19.0 ms                                                     | 23.6 ms: 1.24x slower                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 50.7 ms: 1.24x slower                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 57.1 ms: 1.25x slower                                                      |
| fannkuch                   | 252 ms                                                      | 316 ms: 1.26x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 237 us: 1.28x slower                                                       |
| richards                   | 26.3 ms                                                     | 33.5 ms: 1.28x slower                                                      |
| nbody                      | 66.3 ms                                                     | 85.0 ms: 1.28x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.45 ms: 1.29x slower                                                      |
| typing_runtime_protocols   | 103 us                                                      | 134 us: 1.30x slower                                                       |
| richards_super             | 29.8 ms                                                     | 39.1 ms: 1.31x slower                                                      |
| django_template            | 20.3 ms                                                     | 26.9 ms: 1.32x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 74.7 ms: 1.33x slower                                                      |
| genshi_text                | 15.2 ms                                                     | 20.2 ms: 1.33x slower                                                      |
| bench_thread_pool          | 810 us                                                      | 1.09 ms: 1.34x slower                                                      |
| raytrace                   | 153 ms                                                      | 208 ms: 1.36x slower                                                       |
| coverage                   | 45.3 ms                                                     | 66.6 ms: 1.47x slower                                                      |
| mako                       | 6.56 ms                                                     | 9.93 ms: 1.51x slower                                                      |
| k_core                     | 1.70 sec                                                    | 2.62 sec: 1.54x slower                                                     |
| many_optionals             | 361 us                                                      | 607 us: 1.68x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.69 sec: 1.73x slower                                                     |
| shortest_path              | 355 ms                                                      | 632 ms: 1.78x slower                                                       |
| docutils                   | 1.53 sec                                                    | 2.79 sec: 1.82x slower                                                     |
| bpe_tokeniser              | 2.87 sec                                                    | 5.38 sec: 1.87x slower                                                     |
| connected_components       | 320 ms                                                      | 606 ms: 1.89x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 2.67 sec: 1.95x slower                                                     |
| subparsers                 | 10.9 ms                                                     | 34.5 ms: 3.18x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.07x slower                                                               |

Benchmark hidden because not significant (1): pylint
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250809-3.15.0a0-046a4e3-NOGIL/bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.066x slower

# HPT report

- Reliability score: 99.94% likely to be slow
- 90% likely to have a slowdown of 1.09x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: unknown