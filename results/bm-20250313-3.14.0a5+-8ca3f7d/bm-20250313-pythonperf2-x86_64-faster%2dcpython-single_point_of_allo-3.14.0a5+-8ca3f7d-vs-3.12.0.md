# Results vs. 3.12.0

- fork: faster-cpython
- ref: single_point_of_allo
- machine: linux-x86_64
- commit hash: 8ca3f7d
- commit date: 2025-03-13
- overall geometric mean: 1.026x slower
- HPT reliability: 99.49%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250313-pythonperf2-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-8ca3f7d |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 309 ms: 1.08x slower                                                                   |
| docutils       | 2.87 sec                                                     | 3.05 sec: 1.06x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.07x slower                                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250313-pythonperf2-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-8ca3f7d |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_io              | 1.04 sec                                                     | 665 ms: 1.57x faster                                                                   |
| async_tree_io_tg           | 1.05 sec                                                     | 673 ms: 1.56x faster                                                                   |
| async_tree_none            | 452 ms                                                       | 297 ms: 1.52x faster                                                                   |
| async_tree_none_tg         | 431 ms                                                       | 287 ms: 1.50x faster                                                                   |
| async_tree_memoization_tg  | 540 ms                                                       | 366 ms: 1.48x faster                                                                   |
| async_tree_memoization     | 544 ms                                                       | 377 ms: 1.44x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 528 ms: 1.32x faster                                                                   |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 541 ms: 1.29x faster                                                                   |
| Geometric mean             | (ref)                                                        | 1.46x faster                                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250313-pythonperf2-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-8ca3f7d |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 255 ms: 1.04x faster                                                                   |
| nbody          | 88.0 ms                                                      | 119 ms: 1.35x slower                                                                   |
| Geometric mean | (ref)                                                        | 1.09x slower                                                                           |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250313-pythonperf2-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-8ca3f7d |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.10 ms: 1.15x faster                                                                  |
| regex_dna      | 239 ms                                                       | 236 ms: 1.01x faster                                                                   |
| regex_v8       | 23.6 ms                                                      | 23.9 ms: 1.01x slower                                                                  |
| regex_compile  | 144 ms                                                       | 148 ms: 1.02x slower                                                                   |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250313-pythonperf2-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-8ca3f7d |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| xml_etree_parse      | 144 ms                                                       | 139 ms: 1.03x faster                                                                   |
| xml_etree_generate   | 86.1 ms                                                      | 89.2 ms: 1.04x slower                                                                  |
| xml_etree_process    | 58.4 ms                                                      | 61.7 ms: 1.06x slower                                                                  |
| unpickle_pure_python | 210 us                                                       | 222 us: 1.06x slower                                                                   |
| pickle_pure_python   | 318 us                                                       | 345 us: 1.08x slower                                                                   |
| tomli_loads          | 2.16 sec                                                     | 2.41 sec: 1.12x slower                                                                 |
| json_dumps           | 10.2 ms                                                      | 12.2 ms: 1.19x slower                                                                  |
| json_loads           | 24.4 us                                                      | 29.1 us: 1.19x slower                                                                  |
| Geometric mean       | (ref)                                                        | 1.08x slower                                                                           |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250313-pythonperf2-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-8ca3f7d |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 10.6 ms: 1.22x slower                                                                  |
| python_startup         | 11.6 ms                                                      | 16.5 ms: 1.42x slower                                                                  |
| Geometric mean         | (ref)                                                        | 1.32x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250313-pythonperf2-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-8ca3f7d |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 39.2 ms: 1.03x slower                                                                  |
| mako            | 10.0 ms                                                      | 11.1 ms: 1.11x slower                                                                  |
| Geometric mean  | (ref)                                                        | 1.07x slower                                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250313-pythonperf2-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-8ca3f7d |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_io              | 1.04 sec                                                     | 665 ms: 1.57x faster                                                                   |
| async_tree_io_tg           | 1.05 sec                                                     | 673 ms: 1.56x faster                                                                   |
| async_tree_none            | 452 ms                                                       | 297 ms: 1.52x faster                                                                   |
| async_tree_none_tg         | 431 ms                                                       | 287 ms: 1.50x faster                                                                   |
| async_tree_memoization_tg  | 540 ms                                                       | 366 ms: 1.48x faster                                                                   |
| async_tree_memoization     | 544 ms                                                       | 377 ms: 1.44x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 528 ms: 1.32x faster                                                                   |
| generators                 | 37.4 ms                                                      | 28.4 ms: 1.32x faster                                                                  |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 541 ms: 1.29x faster                                                                   |
| deepcopy_memo              | 36.8 us                                                      | 29.7 us: 1.24x faster                                                                  |
| deepcopy                   | 368 us                                                       | 306 us: 1.20x faster                                                                   |
| regex_effbot               | 3.57 ms                                                      | 3.10 ms: 1.15x faster                                                                  |
| comprehensions             | 21.9 us                                                      | 19.1 us: 1.15x faster                                                                  |
| go                         | 150 ms                                                       | 137 ms: 1.09x faster                                                                   |
| coroutines                 | 23.0 ms                                                      | 21.2 ms: 1.09x faster                                                                  |
| pathlib                    | 18.9 ms                                                      | 17.9 ms: 1.05x faster                                                                  |
| pidigits                   | 265 ms                                                       | 255 ms: 1.04x faster                                                                   |
| xml_etree_parse            | 144 ms                                                       | 139 ms: 1.03x faster                                                                   |
| sqlalchemy_declarative     | 159 ms                                                       | 155 ms: 1.03x faster                                                                   |
| deepcopy_reduce            | 3.37 us                                                      | 3.29 us: 1.03x faster                                                                  |
| regex_dna                  | 239 ms                                                       | 236 ms: 1.01x faster                                                                   |
| regex_v8                   | 23.6 ms                                                      | 23.9 ms: 1.01x slower                                                                  |
| mdp                        | 2.57 sec                                                     | 2.61 sec: 1.01x slower                                                                 |
| meteor_contest             | 128 ms                                                       | 130 ms: 1.02x slower                                                                   |
| scimark_monte_carlo        | 69.0 ms                                                      | 70.3 ms: 1.02x slower                                                                  |
| sympy_sum                  | 162 ms                                                       | 166 ms: 1.02x slower                                                                   |
| logging_format             | 7.48 us                                                      | 7.66 us: 1.02x slower                                                                  |
| regex_compile              | 144 ms                                                       | 148 ms: 1.02x slower                                                                   |
| sympy_integrate            | 23.9 ms                                                      | 24.6 ms: 1.03x slower                                                                  |
| django_template            | 38.2 ms                                                      | 39.2 ms: 1.03x slower                                                                  |
| xml_etree_generate         | 86.1 ms                                                      | 89.2 ms: 1.04x slower                                                                  |
| sqlalchemy_imperative      | 18.7 ms                                                      | 19.5 ms: 1.04x slower                                                                  |
| scimark_lu                 | 98.8 ms                                                      | 103 ms: 1.04x slower                                                                   |
| pprint_pformat             | 1.65 sec                                                     | 1.72 sec: 1.04x slower                                                                 |
| logging_simple             | 6.71 us                                                      | 7.00 us: 1.04x slower                                                                  |
| pprint_safe_repr           | 807 ms                                                       | 848 ms: 1.05x slower                                                                   |
| richards                   | 45.7 ms                                                      | 48.3 ms: 1.06x slower                                                                  |
| bench_thread_pool          | 950 us                                                       | 1.00 ms: 1.06x slower                                                                  |
| xml_etree_process          | 58.4 ms                                                      | 61.7 ms: 1.06x slower                                                                  |
| unpickle_pure_python       | 210 us                                                       | 222 us: 1.06x slower                                                                   |
| docutils                   | 2.87 sec                                                     | 3.05 sec: 1.06x slower                                                                 |
| richards_super             | 51.3 ms                                                      | 54.7 ms: 1.07x slower                                                                  |
| crypto_pyaes               | 80.3 ms                                                      | 85.9 ms: 1.07x slower                                                                  |
| sympy_str                  | 302 ms                                                       | 324 ms: 1.07x slower                                                                   |
| pycparser                  | 1.23 sec                                                     | 1.33 sec: 1.07x slower                                                                 |
| hexiom                     | 5.96 ms                                                      | 6.40 ms: 1.07x slower                                                                  |
| sqlite_synth               | 2.77 us                                                      | 3.00 us: 1.08x slower                                                                  |
| pickle_pure_python         | 318 us                                                       | 345 us: 1.08x slower                                                                   |
| 2to3                       | 285 ms                                                       | 309 ms: 1.08x slower                                                                   |
| raytrace                   | 298 ms                                                       | 324 ms: 1.09x slower                                                                   |
| deltablue                  | 3.24 ms                                                      | 3.58 ms: 1.11x slower                                                                  |
| mako                       | 10.0 ms                                                      | 11.1 ms: 1.11x slower                                                                  |
| chaos                      | 64.0 ms                                                      | 71.1 ms: 1.11x slower                                                                  |
| tomli_loads                | 2.16 sec                                                     | 2.41 sec: 1.12x slower                                                                 |
| scimark_fft                | 301 ms                                                       | 340 ms: 1.13x slower                                                                   |
| spectral_norm              | 91.6 ms                                                      | 104 ms: 1.13x slower                                                                   |
| scimark_sor                | 109 ms                                                       | 123 ms: 1.13x slower                                                                   |
| logging_silent             | 94.4 ns                                                      | 107 ns: 1.13x slower                                                                   |
| json                       | 5.12 ms                                                      | 5.81 ms: 1.13x slower                                                                  |
| pyflate                    | 439 ms                                                       | 502 ms: 1.14x slower                                                                   |
| nqueens                    | 89.9 ms                                                      | 104 ms: 1.15x slower                                                                   |
| sympy_expand               | 484 ms                                                       | 566 ms: 1.17x slower                                                                   |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.99 ms: 1.19x slower                                                                  |
| json_dumps                 | 10.2 ms                                                      | 12.2 ms: 1.19x slower                                                                  |
| json_loads                 | 24.4 us                                                      | 29.1 us: 1.19x slower                                                                  |
| telco                      | 6.96 ms                                                      | 8.39 ms: 1.21x slower                                                                  |
| coverage                   | 66.7 ms                                                      | 80.7 ms: 1.21x slower                                                                  |
| python_startup_no_site     | 8.64 ms                                                      | 10.6 ms: 1.22x slower                                                                  |
| async_generators           | 390 ms                                                       | 491 ms: 1.26x slower                                                                   |
| fannkuch                   | 350 ms                                                       | 453 ms: 1.29x slower                                                                   |
| nbody                      | 88.0 ms                                                      | 119 ms: 1.35x slower                                                                   |
| typing_runtime_protocols   | 152 us                                                       | 205 us: 1.35x slower                                                                   |
| python_startup             | 11.6 ms                                                      | 16.5 ms: 1.42x slower                                                                  |
| create_gc_cycles           | 1.59 ms                                                      | 2.73 ms: 1.71x slower                                                                  |
| gc_traversal               | 3.48 ms                                                      | 6.32 ms: 1.82x slower                                                                  |
| bench_mp_pool              | 4.76 ms                                                      | 1.57 sec: 329.80x slower                                                               |
| Geometric mean             | (ref)                                                        | 1.11x slower                                                                           |

Benchmark hidden because not significant (4): dulwich_log, asyncio_websockets, float, xml_etree_iterparse
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250313-3.14.0a5+-8ca3f7d/bm-20250313-pythonperf2-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-8ca3f7d.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.026x slower

# HPT report

- Reliability score: 99.49% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.05x