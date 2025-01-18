# Results vs. 3.12.0

- fork: kumaraditya303
- ref: gc
- machine: linux-x86_64
- commit hash: e537b8b
- commit date: 2025-01-17
- overall geometric mean: 1.035x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 309 ms: 1.13x slower                                         |
| docutils       | 2.77 sec                                               | 2.83 sec: 1.02x slower                                       |
| Geometric mean | (ref)                                                  | 1.07x slower                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 542 ms: 2.18x faster                                         |
| async_tree_io              | 1.16 sec                                               | 597 ms: 1.93x faster                                         |
| async_tree_none_tg         | 450 ms                                                 | 235 ms: 1.91x faster                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.82x faster                                         |
| async_tree_none            | 472 ms                                                 | 290 ms: 1.63x faster                                         |
| async_tree_memoization     | 578 ms                                                 | 367 ms: 1.57x faster                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 466 ms: 1.56x faster                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 522 ms: 1.39x faster                                         |
| Geometric mean             | (ref)                                                  | 1.73x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 84.7 ms                                                | 78.2 ms: 1.08x faster                                        |
| pidigits       | 187 ms                                                 | 190 ms: 1.01x slower                                         |
| nbody          | 97.0 ms                                                | 141 ms: 1.46x slower                                         |
| Geometric mean | (ref)                                                  | 1.11x slower                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.36 ms: 1.07x faster                                        |
| regex_compile  | 148 ms                                                 | 149 ms: 1.00x slower                                         |
| regex_dna      | 212 ms                                                 | 222 ms: 1.05x slower                                         |
| regex_v8       | 23.1 ms                                                | 24.8 ms: 1.07x slower                                        |
| Geometric mean | (ref)                                                  | 1.01x slower                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| xml_etree_iterparse  | 107 ms                                                 | 96.2 ms: 1.11x faster                                        |
| xml_etree_parse      | 159 ms                                                 | 149 ms: 1.07x faster                                         |
| tomli_loads          | 2.33 sec                                               | 2.41 sec: 1.03x slower                                       |
| xml_etree_generate   | 89.2 ms                                                | 96.1 ms: 1.08x slower                                        |
| xml_etree_process    | 61.7 ms                                                | 68.0 ms: 1.10x slower                                        |
| unpickle_pure_python | 230 us                                                 | 256 us: 1.11x slower                                         |
| json_loads           | 28.5 us                                                | 31.8 us: 1.11x slower                                        |
| pickle_pure_python   | 324 us                                                 | 368 us: 1.14x slower                                         |
| json_dumps           | 10.4 ms                                                | 12.7 ms: 1.23x slower                                        |
| Geometric mean       | (ref)                                                  | 1.07x slower                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 9.35 ms: 1.35x slower                                        |
| python_startup         | 9.55 ms                                                | 15.0 ms: 1.57x slower                                        |
| Geometric mean         | (ref)                                                  | 1.46x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 41.7 ms: 1.21x slower                                        |
| mako            | 11.9 ms                                                | 16.2 ms: 1.36x slower                                        |
| Geometric mean  | (ref)                                                  | 1.28x slower                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 542 ms: 2.18x faster                                         |
| async_tree_io              | 1.16 sec                                               | 597 ms: 1.93x faster                                         |
| async_tree_none_tg         | 450 ms                                                 | 235 ms: 1.91x faster                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.82x faster                                         |
| async_tree_none            | 472 ms                                                 | 290 ms: 1.63x faster                                         |
| async_tree_memoization     | 578 ms                                                 | 367 ms: 1.57x faster                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 466 ms: 1.56x faster                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 522 ms: 1.39x faster                                         |
| deepcopy                   | 371 us                                                 | 311 us: 1.19x faster                                         |
| pathlib                    | 19.3 ms                                                | 16.4 ms: 1.18x faster                                        |
| xml_etree_iterparse        | 107 ms                                                 | 96.2 ms: 1.11x faster                                        |
| float                      | 84.7 ms                                                | 78.2 ms: 1.08x faster                                        |
| regex_effbot               | 3.61 ms                                                | 3.36 ms: 1.07x faster                                        |
| xml_etree_parse            | 159 ms                                                 | 149 ms: 1.07x faster                                         |
| comprehensions             | 21.8 us                                                | 20.8 us: 1.05x faster                                        |
| async_generators           | 463 ms                                                 | 445 ms: 1.04x faster                                         |
| sqlite_synth               | 2.83 us                                                | 2.73 us: 1.04x faster                                        |
| deepcopy_reduce            | 3.35 us                                                | 3.26 us: 1.03x faster                                        |
| deepcopy_memo              | 40.7 us                                                | 39.7 us: 1.02x faster                                        |
| generators                 | 31.2 ms                                                | 31.1 ms: 1.01x faster                                        |
| dulwich_log                | 68.5 ms                                                | 68.7 ms: 1.00x slower                                        |
| regex_compile              | 148 ms                                                 | 149 ms: 1.00x slower                                         |
| go                         | 139 ms                                                 | 141 ms: 1.01x slower                                         |
| pidigits                   | 187 ms                                                 | 190 ms: 1.01x slower                                         |
| docutils                   | 2.77 sec                                               | 2.83 sec: 1.02x slower                                       |
| tomli_loads                | 2.33 sec                                               | 2.41 sec: 1.03x slower                                       |
| spectral_norm              | 115 ms                                                 | 119 ms: 1.04x slower                                         |
| mdp                        | 2.63 sec                                               | 2.74 sec: 1.04x slower                                       |
| logging_simple             | 6.46 us                                                | 6.73 us: 1.04x slower                                        |
| sympy_sum                  | 169 ms                                                 | 177 ms: 1.05x slower                                         |
| regex_dna                  | 212 ms                                                 | 222 ms: 1.05x slower                                         |
| logging_format             | 7.23 us                                                | 7.58 us: 1.05x slower                                        |
| sympy_str                  | 300 ms                                                 | 319 ms: 1.06x slower                                         |
| json                       | 5.26 ms                                                | 5.60 ms: 1.07x slower                                        |
| regex_v8                   | 23.1 ms                                                | 24.8 ms: 1.07x slower                                        |
| xml_etree_generate         | 89.2 ms                                                | 96.1 ms: 1.08x slower                                        |
| scimark_sor                | 129 ms                                                 | 139 ms: 1.08x slower                                         |
| sqlglot_normalize          | 110 ms                                                 | 120 ms: 1.09x slower                                         |
| pprint_safe_repr           | 776 ms                                                 | 852 ms: 1.10x slower                                         |
| coroutines                 | 23.2 ms                                                | 25.5 ms: 1.10x slower                                        |
| xml_etree_process          | 61.7 ms                                                | 68.0 ms: 1.10x slower                                        |
| pyflate                    | 482 ms                                                 | 532 ms: 1.10x slower                                         |
| sympy_expand               | 478 ms                                                 | 527 ms: 1.10x slower                                         |
| sqlalchemy_imperative      | 18.7 ms                                                | 20.6 ms: 1.10x slower                                        |
| crypto_pyaes               | 81.9 ms                                                | 90.4 ms: 1.10x slower                                        |
| sqlalchemy_declarative     | 147 ms                                                 | 162 ms: 1.11x slower                                         |
| sympy_integrate            | 21.4 ms                                                | 23.7 ms: 1.11x slower                                        |
| chaos                      | 67.0 ms                                                | 74.5 ms: 1.11x slower                                        |
| unpickle_pure_python       | 230 us                                                 | 256 us: 1.11x slower                                         |
| sqlglot_optimize           | 54.8 ms                                                | 61.1 ms: 1.11x slower                                        |
| json_loads                 | 28.5 us                                                | 31.8 us: 1.11x slower                                        |
| scimark_fft                | 382 ms                                                 | 426 ms: 1.12x slower                                         |
| pprint_pformat             | 1.57 sec                                               | 1.75 sec: 1.12x slower                                       |
| 2to3                       | 274 ms                                                 | 309 ms: 1.13x slower                                         |
| pickle_pure_python         | 324 us                                                 | 368 us: 1.14x slower                                         |
| raytrace                   | 312 ms                                                 | 356 ms: 1.14x slower                                         |
| sqlglot_transpile          | 1.68 ms                                                | 1.93 ms: 1.14x slower                                        |
| logging_silent             | 104 ns                                                 | 120 ns: 1.15x slower                                         |
| create_gc_cycles           | 1.48 ms                                                | 1.71 ms: 1.16x slower                                        |
| scimark_monte_carlo        | 75.1 ms                                                | 87.2 ms: 1.16x slower                                        |
| sqlglot_parse              | 1.36 ms                                                | 1.59 ms: 1.16x slower                                        |
| richards                   | 45.8 ms                                                | 54.0 ms: 1.18x slower                                        |
| meteor_contest             | 112 ms                                                 | 133 ms: 1.18x slower                                         |
| nqueens                    | 83.3 ms                                                | 100 ms: 1.20x slower                                         |
| gc_traversal               | 3.79 ms                                                | 4.56 ms: 1.20x slower                                        |
| django_template            | 34.6 ms                                                | 41.7 ms: 1.21x slower                                        |
| scimark_lu                 | 118 ms                                                 | 142 ms: 1.21x slower                                         |
| hexiom                     | 6.41 ms                                                | 7.76 ms: 1.21x slower                                        |
| json_dumps                 | 10.4 ms                                                | 12.7 ms: 1.23x slower                                        |
| fannkuch                   | 417 ms                                                 | 516 ms: 1.24x slower                                         |
| richards_super             | 51.5 ms                                                | 64.3 ms: 1.25x slower                                        |
| deltablue                  | 3.72 ms                                                | 4.72 ms: 1.27x slower                                        |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 6.45 ms: 1.28x slower                                        |
| telco                      | 7.10 ms                                                | 9.09 ms: 1.28x slower                                        |
| typing_runtime_protocols   | 158 us                                                 | 211 us: 1.33x slower                                         |
| python_startup_no_site     | 6.94 ms                                                | 9.35 ms: 1.35x slower                                        |
| mako                       | 11.9 ms                                                | 16.2 ms: 1.36x slower                                        |
| nbody                      | 97.0 ms                                                | 141 ms: 1.46x slower                                         |
| coverage                   | 72.7 ms                                                | 108 ms: 1.49x slower                                         |
| python_startup             | 9.55 ms                                                | 15.0 ms: 1.57x slower                                        |
| bench_mp_pool              | 24.0 ms                                                | 89.3 ms: 3.72x slower                                        |
| bench_thread_pool          | 842 us                                                 | 3.49 ms: 4.15x slower                                        |
| Geometric mean             | (ref)                                                  | 1.07x slower                                                 |

Benchmark hidden because not significant (2): asyncio_websockets, pycparser
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250117-3.14.0a4+-e537b8b-NOGIL/bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.035x slower

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.30x