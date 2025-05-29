# Results vs. 3.13.0

- fork: python
- ref: 2fd09b011031f3c00c34
- machine: linux-aarch64
- commit hash: 2fd09b0
- commit date: 2025-05-24
- overall geometric mean: 1.025x slower
- HPT reliability: 99.92%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 301 ms: 1.04x faster                                                    |
| docutils       | 2.96 sec                                                 | 3.00 sec: 1.01x slower                                                  |
| html5lib       | 65.6 ms                                                  | 62.1 ms: 1.06x faster                                                   |
| sphinx         | 1.20 sec                                                 | 1.15 sec: 1.04x faster                                                  |
| Geometric mean | (ref)                                                    | 1.03x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 450 ms: 1.47x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 457 ms: 1.45x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 364 ms: 1.33x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 867 ms: 1.31x faster                                                    |
| async_tree_none            | 504 ms                                                   | 386 ms: 1.30x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 893 ms: 1.30x faster                                                    |
| async_generators           | 500 ms                                                   | 417 ms: 1.20x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 713 ms: 1.12x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 723 ms: 1.09x faster                                                    |
| Geometric mean             | (ref)                                                    | 1.22x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 87.6 ms: 1.09x faster                                                   |
| nbody          | 118 ms                                                   | 129 ms: 1.09x slower                                                    |
| pidigits       | 238 ms                                                   | 293 ms: 1.23x slower                                                    |
| Geometric mean | (ref)                                                    | 1.07x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.58 ms: 1.11x faster                                                   |
| regex_compile  | 134 ms                                                   | 120 ms: 1.11x faster                                                    |
| regex_dna      | 263 ms                                                   | 240 ms: 1.10x faster                                                    |
| Geometric mean | (ref)                                                    | 1.09x faster                                                            |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.67 sec                                                 | 2.37 sec: 1.13x faster                                                  |
| xml_etree_generate   | 118 ms                                                   | 107 ms: 1.11x faster                                                    |
| xml_etree_process    | 82.1 ms                                                  | 76.1 ms: 1.08x faster                                                   |
| json_dumps           | 14.2 ms                                                  | 13.2 ms: 1.07x faster                                                   |
| xml_etree_iterparse  | 159 ms                                                   | 149 ms: 1.07x faster                                                    |
| unpickle_pure_python | 265 us                                                   | 249 us: 1.06x faster                                                    |
| xml_etree_parse      | 203 ms                                                   | 209 ms: 1.03x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (2): pickle_pure_python, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 16.0 ms                                                  | 15.2 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text    | 28.6 ms                                                  | 26.9 ms: 1.06x faster                                                   |
| genshi_xml     | 61.6 ms                                                  | 60.5 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.67 sec: 2.07x faster                                                  |
| deepcopy                   | 479 us                                                   | 318 us: 1.51x faster                                                    |
| deepcopy_memo              | 53.0 us                                                  | 35.8 us: 1.48x faster                                                   |
| async_tree_memoization_tg  | 663 ms                                                   | 450 ms: 1.47x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 457 ms: 1.45x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 364 ms: 1.33x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 867 ms: 1.31x faster                                                    |
| async_tree_none            | 504 ms                                                   | 386 ms: 1.30x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 893 ms: 1.30x faster                                                    |
| deepcopy_reduce            | 4.24 us                                                  | 3.37 us: 1.26x faster                                                   |
| go                         | 164 ms                                                   | 132 ms: 1.25x faster                                                    |
| async_generators           | 500 ms                                                   | 417 ms: 1.20x faster                                                    |
| spectral_norm              | 143 ms                                                   | 120 ms: 1.20x faster                                                    |
| scimark_fft                | 463 ms                                                   | 402 ms: 1.15x faster                                                    |
| scimark_monte_carlo        | 87.8 ms                                                  | 76.6 ms: 1.15x faster                                                   |
| scimark_sor                | 164 ms                                                   | 143 ms: 1.14x faster                                                    |
| bpe_tokeniser              | 6.02 sec                                                 | 5.28 sec: 1.14x faster                                                  |
| pyflate                    | 582 ms                                                   | 515 ms: 1.13x faster                                                    |
| tomli_loads                | 2.67 sec                                                 | 2.37 sec: 1.13x faster                                                  |
| generators                 | 40.3 ms                                                  | 35.8 ms: 1.12x faster                                                   |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 713 ms: 1.12x faster                                                    |
| richards                   | 54.5 ms                                                  | 48.8 ms: 1.12x faster                                                   |
| pathlib                    | 24.3 ms                                                  | 21.8 ms: 1.12x faster                                                   |
| regex_effbot               | 5.10 ms                                                  | 4.58 ms: 1.11x faster                                                   |
| richards_super             | 60.8 ms                                                  | 54.7 ms: 1.11x faster                                                   |
| regex_compile              | 134 ms                                                   | 120 ms: 1.11x faster                                                    |
| xml_etree_generate         | 118 ms                                                   | 107 ms: 1.11x faster                                                    |
| telco                      | 10.5 ms                                                  | 9.46 ms: 1.11x faster                                                   |
| regex_dna                  | 263 ms                                                   | 240 ms: 1.10x faster                                                    |
| scimark_lu                 | 146 ms                                                   | 134 ms: 1.09x faster                                                    |
| float                      | 95.8 ms                                                  | 87.6 ms: 1.09x faster                                                   |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 723 ms: 1.09x faster                                                    |
| k_core                     | 2.99 sec                                                 | 2.74 sec: 1.09x faster                                                  |
| pycparser                  | 1.34 sec                                                 | 1.25 sec: 1.08x faster                                                  |
| xml_etree_process          | 82.1 ms                                                  | 76.1 ms: 1.08x faster                                                   |
| json_dumps                 | 14.2 ms                                                  | 13.2 ms: 1.07x faster                                                   |
| sympy_integrate            | 21.4 ms                                                  | 20.0 ms: 1.07x faster                                                   |
| pylint                     | 345 ms                                                   | 324 ms: 1.07x faster                                                    |
| xml_etree_iterparse        | 159 ms                                                   | 149 ms: 1.07x faster                                                    |
| genshi_text                | 28.6 ms                                                  | 26.9 ms: 1.06x faster                                                   |
| unpickle_pure_python       | 265 us                                                   | 249 us: 1.06x faster                                                    |
| html5lib                   | 65.6 ms                                                  | 62.1 ms: 1.06x faster                                                   |
| python_startup             | 16.0 ms                                                  | 15.2 ms: 1.05x faster                                                   |
| chaos                      | 70.7 ms                                                  | 67.3 ms: 1.05x faster                                                   |
| sqlite_synth               | 4.08 us                                                  | 3.90 us: 1.05x faster                                                   |
| sphinx                     | 1.20 sec                                                 | 1.15 sec: 1.04x faster                                                  |
| 2to3                       | 313 ms                                                   | 301 ms: 1.04x faster                                                    |
| sympy_str                  | 265 ms                                                   | 259 ms: 1.02x faster                                                    |
| genshi_xml                 | 61.6 ms                                                  | 60.5 ms: 1.02x faster                                                   |
| docutils                   | 2.96 sec                                                 | 3.00 sec: 1.01x slower                                                  |
| shortest_path              | 565 ms                                                   | 576 ms: 1.02x slower                                                    |
| connected_components       | 547 ms                                                   | 560 ms: 1.02x slower                                                    |
| xml_etree_parse            | 203 ms                                                   | 209 ms: 1.03x slower                                                    |
| logging_simple             | 7.25 us                                                  | 7.50 us: 1.03x slower                                                   |
| pprint_pformat             | 1.99 sec                                                 | 2.10 sec: 1.06x slower                                                  |
| pprint_safe_repr           | 962 ms                                                   | 1.03 sec: 1.07x slower                                                  |
| nbody                      | 118 ms                                                   | 129 ms: 1.09x slower                                                    |
| create_gc_cycles           | 3.39 ms                                                  | 3.82 ms: 1.12x slower                                                   |
| gc_traversal               | 5.92 ms                                                  | 6.81 ms: 1.15x slower                                                   |
| pidigits                   | 238 ms                                                   | 293 ms: 1.23x slower                                                    |
| many_optionals             | 626 us                                                   | 878 us: 1.40x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 29.1 ms: 1.43x slower                                                   |
| logging_silent             | 135 ns                                                   | 596 ns: 4.43x slower                                                    |
| coverage                   | 106 ms                                                   | 526 ms: 4.98x slower                                                    |
| thrift                     | 1.01 ms                                                  | 194 ms: 191.90x slower                                                  |
| bench_mp_pool              | 8.07 ms                                                  | 3.87 sec: 479.76x slower                                                |
| Geometric mean             | (ref)                                                    | 1.10x slower                                                            |

Benchmark hidden because not significant (23): hexiom, sympy_sum, nqueens, comprehensions, regex_v8, typing_runtime_protocols, meteor_contest, sympy_expand, deltablue, json, bench_thread_pool, django_template, crypto_pyaes, asyncio_websockets, scimark_sparse_mat_mult, python_startup_no_site, fannkuch, mako, logging_format, raytrace, pickle_pure_python, json_loads, coroutines
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250524-3.15.0a0-2fd09b0-CLANG/bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.025x slower

# HPT report

- Reliability score: 99.92% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.10x