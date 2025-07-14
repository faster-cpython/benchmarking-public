# Results vs. 3.13.0

- fork: python
- ref: 47b01da4ccedd9c00fad
- machine: linux-aarch64
- commit hash: 47b01da
- commit date: 2025-07-12
- overall geometric mean: 1.012x faster
- HPT reliability: 98.21%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.14 sec: 1.06x slower                                                  |
| html5lib       | 65.6 ms                                                  | 64.0 ms: 1.02x faster                                                   |
| sphinx         | 1.20 sec                                                 | 1.16 sec: 1.03x faster                                                  |
| Geometric mean | (ref)                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 480 ms: 1.38x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 491 ms: 1.35x faster                                                    |
| async_tree_none            | 504 ms                                                   | 389 ms: 1.30x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 898 ms: 1.27x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 920 ms: 1.27x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 386 ms: 1.26x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 665 ms: 1.20x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 676 ms: 1.17x faster                                                    |
| async_generators           | 500 ms                                                   | 479 ms: 1.04x faster                                                    |
| Geometric mean             | (ref)                                                    | 1.20x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 82.8 ms: 1.16x faster                                                   |
| nbody          | 118 ms                                                   | 129 ms: 1.09x slower                                                    |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.89 ms: 1.31x faster                                                   |
| regex_v8       | 32.5 ms                                                  | 27.0 ms: 1.20x faster                                                   |
| regex_dna      | 263 ms                                                   | 222 ms: 1.18x faster                                                    |
| regex_compile  | 134 ms                                                   | 125 ms: 1.07x faster                                                    |
| Geometric mean | (ref)                                                    | 1.19x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads         | 2.67 sec                                                 | 2.30 sec: 1.16x faster                                                  |
| xml_etree_generate  | 118 ms                                                   | 106 ms: 1.11x faster                                                    |
| xml_etree_parse     | 203 ms                                                   | 183 ms: 1.11x faster                                                    |
| xml_etree_iterparse | 159 ms                                                   | 144 ms: 1.11x faster                                                    |
| xml_etree_process   | 82.1 ms                                                  | 76.0 ms: 1.08x faster                                                   |
| pickle_pure_python  | 374 us                                                   | 406 us: 1.09x slower                                                    |
| Geometric mean      | (ref)                                                    | 1.06x faster                                                            |

Benchmark hidden because not significant (3): json_dumps, unpickle_pure_python, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 16.0 ms                                                  | 15.2 ms: 1.06x faster                                                   |
| Geometric mean | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 14.0 ms                                                  | 12.9 ms: 1.08x faster                                                   |
| genshi_xml     | 61.6 ms                                                  | 63.6 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.68 sec: 2.05x faster                                                  |
| deepcopy                   | 479 us                                                   | 324 us: 1.48x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 480 ms: 1.38x faster                                                    |
| deepcopy_memo              | 53.0 us                                                  | 39.0 us: 1.36x faster                                                   |
| async_tree_memoization     | 664 ms                                                   | 491 ms: 1.35x faster                                                    |
| regex_effbot               | 5.10 ms                                                  | 3.89 ms: 1.31x faster                                                   |
| async_tree_none            | 504 ms                                                   | 389 ms: 1.30x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 898 ms: 1.27x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 920 ms: 1.27x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 386 ms: 1.26x faster                                                    |
| richards                   | 54.5 ms                                                  | 44.8 ms: 1.22x faster                                                   |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 665 ms: 1.20x faster                                                    |
| regex_v8                   | 32.5 ms                                                  | 27.0 ms: 1.20x faster                                                   |
| regex_dna                  | 263 ms                                                   | 222 ms: 1.18x faster                                                    |
| spectral_norm              | 143 ms                                                   | 121 ms: 1.18x faster                                                    |
| richards_super             | 60.8 ms                                                  | 51.7 ms: 1.18x faster                                                   |
| deepcopy_reduce            | 4.24 us                                                  | 3.61 us: 1.18x faster                                                   |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 676 ms: 1.17x faster                                                    |
| tomli_loads                | 2.67 sec                                                 | 2.30 sec: 1.16x faster                                                  |
| float                      | 95.8 ms                                                  | 82.8 ms: 1.16x faster                                                   |
| scimark_sor                | 164 ms                                                   | 144 ms: 1.14x faster                                                    |
| generators                 | 40.3 ms                                                  | 35.5 ms: 1.13x faster                                                   |
| scimark_fft                | 463 ms                                                   | 410 ms: 1.13x faster                                                    |
| sqlite_synth               | 4.08 us                                                  | 3.66 us: 1.12x faster                                                   |
| bpe_tokeniser              | 6.02 sec                                                 | 5.41 sec: 1.11x faster                                                  |
| xml_etree_generate         | 118 ms                                                   | 106 ms: 1.11x faster                                                    |
| xml_etree_parse            | 203 ms                                                   | 183 ms: 1.11x faster                                                    |
| xml_etree_iterparse        | 159 ms                                                   | 144 ms: 1.11x faster                                                    |
| mako                       | 14.0 ms                                                  | 12.9 ms: 1.08x faster                                                   |
| xml_etree_process          | 82.1 ms                                                  | 76.0 ms: 1.08x faster                                                   |
| regex_compile              | 134 ms                                                   | 125 ms: 1.07x faster                                                    |
| pylint                     | 345 ms                                                   | 323 ms: 1.07x faster                                                    |
| k_core                     | 2.99 sec                                                 | 2.82 sec: 1.06x faster                                                  |
| python_startup             | 16.0 ms                                                  | 15.2 ms: 1.06x faster                                                   |
| pyflate                    | 582 ms                                                   | 550 ms: 1.06x faster                                                    |
| go                         | 164 ms                                                   | 155 ms: 1.06x faster                                                    |
| thrift                     | 1.01 ms                                                  | 958 us: 1.05x faster                                                    |
| logging_format             | 8.10 us                                                  | 7.72 us: 1.05x faster                                                   |
| async_generators           | 500 ms                                                   | 479 ms: 1.04x faster                                                    |
| sphinx                     | 1.20 sec                                                 | 1.16 sec: 1.03x faster                                                  |
| html5lib                   | 65.6 ms                                                  | 64.0 ms: 1.02x faster                                                   |
| djangocms                  | 66.2 us                                                  | 65.0 us: 1.02x faster                                                   |
| connected_components       | 547 ms                                                   | 562 ms: 1.03x slower                                                    |
| genshi_xml                 | 61.6 ms                                                  | 63.6 ms: 1.03x slower                                                   |
| comprehensions             | 20.8 us                                                  | 21.7 us: 1.04x slower                                                   |
| sympy_str                  | 265 ms                                                   | 277 ms: 1.04x slower                                                    |
| sympy_expand               | 472 ms                                                   | 495 ms: 1.05x slower                                                    |
| shortest_path              | 565 ms                                                   | 593 ms: 1.05x slower                                                    |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 7.00 ms: 1.05x slower                                                   |
| crypto_pyaes               | 84.9 ms                                                  | 89.5 ms: 1.05x slower                                                   |
| docutils                   | 2.96 sec                                                 | 3.14 sec: 1.06x slower                                                  |
| typing_runtime_protocols   | 197 us                                                   | 213 us: 1.08x slower                                                    |
| raytrace                   | 310 ms                                                   | 336 ms: 1.08x slower                                                    |
| pickle_pure_python         | 374 us                                                   | 406 us: 1.09x slower                                                    |
| nbody                      | 118 ms                                                   | 129 ms: 1.09x slower                                                    |
| create_gc_cycles           | 3.39 ms                                                  | 3.77 ms: 1.11x slower                                                   |
| gc_traversal               | 5.92 ms                                                  | 6.82 ms: 1.15x slower                                                   |
| pprint_pformat             | 1.99 sec                                                 | 2.35 sec: 1.18x slower                                                  |
| pprint_safe_repr           | 962 ms                                                   | 1.20 sec: 1.25x slower                                                  |
| many_optionals             | 626 us                                                   | 824 us: 1.31x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 29.2 ms: 1.44x slower                                                   |
| telco                      | 10.5 ms                                                  | 165 ms: 15.79x slower                                                   |
| bench_mp_pool              | 8.07 ms                                                  | 1.25 sec: 154.59x slower                                                |
| Geometric mean             | (ref)                                                    | 1.03x slower                                                            |

Benchmark hidden because not significant (27): scimark_monte_carlo, json_dumps, unpickle_pure_python, nqueens, pathlib, genshi_text, json, logging_simple, meteor_contest, fannkuch, chaos, sympy_integrate, python_startup_no_site, logging_silent, coverage, pidigits, asyncio_websockets, coroutines, deltablue, 2to3, json_loads, sympy_sum, pycparser, django_template, hexiom, bench_thread_pool, scimark_lu
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250712-3.15.0a0-47b01da-JIT/bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.012x faster

# HPT report

- Reliability score: 98.21% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.10x