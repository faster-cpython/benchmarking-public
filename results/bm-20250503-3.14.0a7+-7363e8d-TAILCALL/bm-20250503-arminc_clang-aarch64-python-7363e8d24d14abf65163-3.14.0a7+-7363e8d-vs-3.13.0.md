# Results vs. 3.13.0

- fork: python
- ref: 7363e8d24d14abf65163
- machine: linux-aarch64
- commit hash: 7363e8d
- commit date: 2025-05-03
- overall geometric mean: 1.069x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 294 ms: 1.07x faster                                                     |
| html5lib       | 65.6 ms                                                  | 58.3 ms: 1.12x faster                                                    |
| sphinx         | 1.20 sec                                                 | 1.12 sec: 1.07x faster                                                   |
| Geometric mean | (ref)                                                    | 1.06x faster                                                             |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 447 ms: 1.48x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 452 ms: 1.47x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 357 ms: 1.36x faster                                                     |
| async_tree_none            | 504 ms                                                   | 372 ms: 1.36x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 861 ms: 1.35x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 865 ms: 1.32x faster                                                     |
| async_generators           | 500 ms                                                   | 434 ms: 1.15x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 706 ms: 1.13x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 723 ms: 1.09x faster                                                     |
| Geometric mean             | (ref)                                                    | 1.24x faster                                                             |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 86.4 ms: 1.11x faster                                                    |
| nbody          | 118 ms                                                   | 128 ms: 1.08x slower                                                     |
| pidigits       | 238 ms                                                   | 292 ms: 1.23x slower                                                     |
| Geometric mean | (ref)                                                    | 1.06x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 134 ms                                                   | 120 ms: 1.11x faster                                                     |
| regex_effbot   | 5.10 ms                                                  | 4.59 ms: 1.11x faster                                                    |
| regex_dna      | 263 ms                                                   | 247 ms: 1.06x faster                                                     |
| Geometric mean | (ref)                                                    | 1.07x faster                                                             |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads         | 2.67 sec                                                 | 2.35 sec: 1.14x faster                                                   |
| xml_etree_generate  | 118 ms                                                   | 107 ms: 1.10x faster                                                     |
| xml_etree_process   | 82.1 ms                                                  | 76.5 ms: 1.07x faster                                                    |
| xml_etree_iterparse | 159 ms                                                   | 148 ms: 1.07x faster                                                     |
| json_loads          | 32.8 us                                                  | 34.9 us: 1.06x slower                                                    |
| Geometric mean      | (ref)                                                    | 1.04x faster                                                             |

Benchmark hidden because not significant (4): unpickle_pure_python, pickle_pure_python, xml_etree_parse, json_dumps

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text    | 28.6 ms                                                  | 25.8 ms: 1.11x faster                                                    |
| genshi_xml     | 61.6 ms                                                  | 58.3 ms: 1.06x faster                                                    |
| Geometric mean | (ref)                                                    | 1.04x faster                                                             |

Benchmark hidden because not significant (2): mako, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.62 sec: 2.13x faster                                                   |
| deepcopy                   | 479 us                                                   | 312 us: 1.54x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 35.2 us: 1.51x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 447 ms: 1.48x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 452 ms: 1.47x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 357 ms: 1.36x faster                                                     |
| async_tree_none            | 504 ms                                                   | 372 ms: 1.36x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 861 ms: 1.35x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 865 ms: 1.32x faster                                                     |
| deepcopy_reduce            | 4.24 us                                                  | 3.25 us: 1.31x faster                                                    |
| go                         | 164 ms                                                   | 129 ms: 1.27x faster                                                     |
| spectral_norm              | 143 ms                                                   | 122 ms: 1.17x faster                                                     |
| logging_silent             | 135 ns                                                   | 116 ns: 1.16x faster                                                     |
| async_generators           | 500 ms                                                   | 434 ms: 1.15x faster                                                     |
| bpe_tokeniser              | 6.02 sec                                                 | 5.26 sec: 1.14x faster                                                   |
| scimark_sor                | 164 ms                                                   | 143 ms: 1.14x faster                                                     |
| scimark_fft                | 463 ms                                                   | 406 ms: 1.14x faster                                                     |
| tomli_loads                | 2.67 sec                                                 | 2.35 sec: 1.14x faster                                                   |
| pathlib                    | 24.3 ms                                                  | 21.4 ms: 1.13x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 706 ms: 1.13x faster                                                     |
| telco                      | 10.5 ms                                                  | 9.24 ms: 1.13x faster                                                    |
| html5lib                   | 65.6 ms                                                  | 58.3 ms: 1.12x faster                                                    |
| regex_compile              | 134 ms                                                   | 120 ms: 1.11x faster                                                     |
| pylint                     | 345 ms                                                   | 311 ms: 1.11x faster                                                     |
| regex_effbot               | 5.10 ms                                                  | 4.59 ms: 1.11x faster                                                    |
| pyflate                    | 582 ms                                                   | 524 ms: 1.11x faster                                                     |
| genshi_text                | 28.6 ms                                                  | 25.8 ms: 1.11x faster                                                    |
| float                      | 95.8 ms                                                  | 86.4 ms: 1.11x faster                                                    |
| richards_super             | 60.8 ms                                                  | 54.9 ms: 1.11x faster                                                    |
| xml_etree_generate         | 118 ms                                                   | 107 ms: 1.10x faster                                                     |
| pycparser                  | 1.34 sec                                                 | 1.23 sec: 1.10x faster                                                   |
| scimark_monte_carlo        | 87.8 ms                                                  | 80.3 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 723 ms: 1.09x faster                                                     |
| sympy_sum                  | 151 ms                                                   | 138 ms: 1.09x faster                                                     |
| sympy_integrate            | 21.4 ms                                                  | 19.7 ms: 1.09x faster                                                    |
| richards                   | 54.5 ms                                                  | 50.2 ms: 1.09x faster                                                    |
| generators                 | 40.3 ms                                                  | 37.2 ms: 1.08x faster                                                    |
| chaos                      | 70.7 ms                                                  | 65.5 ms: 1.08x faster                                                    |
| xml_etree_process          | 82.1 ms                                                  | 76.5 ms: 1.07x faster                                                    |
| coverage                   | 106 ms                                                   | 98.5 ms: 1.07x faster                                                    |
| sphinx                     | 1.20 sec                                                 | 1.12 sec: 1.07x faster                                                   |
| xml_etree_iterparse        | 159 ms                                                   | 148 ms: 1.07x faster                                                     |
| k_core                     | 2.99 sec                                                 | 2.80 sec: 1.07x faster                                                   |
| 2to3                       | 313 ms                                                   | 294 ms: 1.07x faster                                                     |
| comprehensions             | 20.8 us                                                  | 19.6 us: 1.06x faster                                                    |
| logging_format             | 8.10 us                                                  | 7.61 us: 1.06x faster                                                    |
| regex_dna                  | 263 ms                                                   | 247 ms: 1.06x faster                                                     |
| pprint_pformat             | 1.99 sec                                                 | 1.88 sec: 1.06x faster                                                   |
| genshi_xml                 | 61.6 ms                                                  | 58.3 ms: 1.06x faster                                                    |
| hexiom                     | 7.34 ms                                                  | 6.96 ms: 1.06x faster                                                    |
| deltablue                  | 3.97 ms                                                  | 3.77 ms: 1.05x faster                                                    |
| logging_simple             | 7.25 us                                                  | 6.90 us: 1.05x faster                                                    |
| sympy_expand               | 472 ms                                                   | 453 ms: 1.04x faster                                                     |
| pprint_safe_repr           | 962 ms                                                   | 923 ms: 1.04x faster                                                     |
| sqlite_synth               | 4.08 us                                                  | 3.94 us: 1.04x faster                                                    |
| shortest_path              | 565 ms                                                   | 580 ms: 1.03x slower                                                     |
| connected_components       | 547 ms                                                   | 572 ms: 1.05x slower                                                     |
| json_loads                 | 32.8 us                                                  | 34.9 us: 1.06x slower                                                    |
| nbody                      | 118 ms                                                   | 128 ms: 1.08x slower                                                     |
| create_gc_cycles           | 3.39 ms                                                  | 3.75 ms: 1.11x slower                                                    |
| gc_traversal               | 5.92 ms                                                  | 6.76 ms: 1.14x slower                                                    |
| pidigits                   | 238 ms                                                   | 292 ms: 1.23x slower                                                     |
| subparsers                 | 20.3 ms                                                  | 27.5 ms: 1.35x slower                                                    |
| many_optionals             | 626 us                                                   | 855 us: 1.36x slower                                                     |
| bench_mp_pool              | 8.07 ms                                                  | 2.64 sec: 326.82x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (25): scimark_lu, sqlalchemy_declarative, unpickle_pure_python, nqueens, sympy_str, bench_thread_pool, sqlalchemy_imperative, json, python_startup_no_site, asyncio_websockets, coroutines, pickle_pure_python, regex_v8, mako, django_template, docutils, xml_etree_parse, typing_runtime_protocols, python_startup, crypto_pyaes, meteor_contest, scimark_sparse_mat_mult, json_dumps, fannkuch, raytrace
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (13) of results/bm-20250503-3.14.0a7+-7363e8d-CLANG/bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.069x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.07x