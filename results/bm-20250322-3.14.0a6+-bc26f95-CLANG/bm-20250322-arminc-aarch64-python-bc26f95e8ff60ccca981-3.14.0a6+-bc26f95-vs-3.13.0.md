# Results vs. 3.13.0

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: linux-aarch64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.062x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 290 ms: 1.08x faster                                                     |
| html5lib       | 65.6 ms                                                  | 59.3 ms: 1.11x faster                                                    |
| sphinx         | 1.20 sec                                                 | 1.12 sec: 1.07x faster                                                   |
| Geometric mean | (ref)                                                    | 1.06x faster                                                             |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 459 ms: 1.44x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 465 ms: 1.43x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 362 ms: 1.34x faster                                                     |
| async_tree_none            | 504 ms                                                   | 382 ms: 1.32x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 899 ms: 1.30x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 884 ms: 1.29x faster                                                     |
| async_generators           | 500 ms                                                   | 416 ms: 1.20x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 707 ms: 1.13x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 728 ms: 1.08x faster                                                     |
| Geometric mean             | (ref)                                                    | 1.23x faster                                                             |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 85.6 ms: 1.12x faster                                                    |
| pidigits       | 238 ms                                                   | 293 ms: 1.23x slower                                                     |
| Geometric mean | (ref)                                                    | 1.03x slower                                                             |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.12 ms: 1.24x faster                                                    |
| regex_dna      | 263 ms                                                   | 239 ms: 1.10x faster                                                     |
| regex_compile  | 134 ms                                                   | 123 ms: 1.09x faster                                                     |
| regex_v8       | 32.5 ms                                                  | 30.6 ms: 1.06x faster                                                    |
| Geometric mean | (ref)                                                    | 1.12x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_generate  | 118 ms                                                   | 104 ms: 1.14x faster                                                     |
| tomli_loads         | 2.67 sec                                                 | 2.35 sec: 1.13x faster                                                   |
| xml_etree_process   | 82.1 ms                                                  | 74.7 ms: 1.10x faster                                                    |
| xml_etree_iterparse | 159 ms                                                   | 150 ms: 1.06x faster                                                     |
| Geometric mean      | (ref)                                                    | 1.05x faster                                                             |

Benchmark hidden because not significant (5): unpickle_pure_python, pickle_pure_python, json_dumps, xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 10.2 ms: 1.16x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.08x slower                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text    | 28.6 ms                                                  | 26.4 ms: 1.08x faster                                                    |
| genshi_xml     | 61.6 ms                                                  | 58.6 ms: 1.05x faster                                                    |
| Geometric mean | (ref)                                                    | 1.04x faster                                                             |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy                   | 479 us                                                   | 310 us: 1.55x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 35.5 us: 1.49x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 459 ms: 1.44x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 465 ms: 1.43x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 362 ms: 1.34x faster                                                     |
| async_tree_none            | 504 ms                                                   | 382 ms: 1.32x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 899 ms: 1.30x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 884 ms: 1.29x faster                                                     |
| deepcopy_reduce            | 4.24 us                                                  | 3.34 us: 1.27x faster                                                    |
| regex_effbot               | 5.10 ms                                                  | 4.12 ms: 1.24x faster                                                    |
| spectral_norm              | 143 ms                                                   | 117 ms: 1.23x faster                                                     |
| go                         | 164 ms                                                   | 135 ms: 1.21x faster                                                     |
| async_generators           | 500 ms                                                   | 416 ms: 1.20x faster                                                     |
| scimark_fft                | 463 ms                                                   | 395 ms: 1.17x faster                                                     |
| logging_silent             | 135 ns                                                   | 116 ns: 1.16x faster                                                     |
| pylint                     | 345 ms                                                   | 301 ms: 1.15x faster                                                     |
| scimark_sor                | 164 ms                                                   | 144 ms: 1.14x faster                                                     |
| pathlib                    | 24.3 ms                                                  | 21.3 ms: 1.14x faster                                                    |
| scimark_monte_carlo        | 87.8 ms                                                  | 77.2 ms: 1.14x faster                                                    |
| xml_etree_generate         | 118 ms                                                   | 104 ms: 1.14x faster                                                     |
| tomli_loads                | 2.67 sec                                                 | 2.35 sec: 1.13x faster                                                   |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 707 ms: 1.13x faster                                                     |
| bpe_tokeniser              | 6.02 sec                                                 | 5.37 sec: 1.12x faster                                                   |
| float                      | 95.8 ms                                                  | 85.6 ms: 1.12x faster                                                    |
| generators                 | 40.3 ms                                                  | 36.2 ms: 1.11x faster                                                    |
| thrift                     | 1.01 ms                                                  | 910 us: 1.11x faster                                                     |
| telco                      | 10.5 ms                                                  | 9.43 ms: 1.11x faster                                                    |
| html5lib                   | 65.6 ms                                                  | 59.3 ms: 1.11x faster                                                    |
| coverage                   | 106 ms                                                   | 95.7 ms: 1.10x faster                                                    |
| richards                   | 54.5 ms                                                  | 49.5 ms: 1.10x faster                                                    |
| xml_etree_process          | 82.1 ms                                                  | 74.7 ms: 1.10x faster                                                    |
| regex_dna                  | 263 ms                                                   | 239 ms: 1.10x faster                                                     |
| pyflate                    | 582 ms                                                   | 530 ms: 1.10x faster                                                     |
| regex_compile              | 134 ms                                                   | 123 ms: 1.09x faster                                                     |
| richards_super             | 60.8 ms                                                  | 56.0 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 728 ms: 1.08x faster                                                     |
| genshi_text                | 28.6 ms                                                  | 26.4 ms: 1.08x faster                                                    |
| logging_format             | 8.10 us                                                  | 7.50 us: 1.08x faster                                                    |
| 2to3                       | 313 ms                                                   | 290 ms: 1.08x faster                                                     |
| k_core                     | 2.99 sec                                                 | 2.77 sec: 1.08x faster                                                   |
| mdp                        | 3.45 sec                                                 | 3.19 sec: 1.08x faster                                                   |
| pycparser                  | 1.34 sec                                                 | 1.25 sec: 1.08x faster                                                   |
| sphinx                     | 1.20 sec                                                 | 1.12 sec: 1.07x faster                                                   |
| pprint_pformat             | 1.99 sec                                                 | 1.86 sec: 1.07x faster                                                   |
| regex_v8                   | 32.5 ms                                                  | 30.6 ms: 1.06x faster                                                    |
| xml_etree_iterparse        | 159 ms                                                   | 150 ms: 1.06x faster                                                     |
| sqlalchemy_declarative     | 154 ms                                                   | 145 ms: 1.06x faster                                                     |
| pprint_safe_repr           | 962 ms                                                   | 908 ms: 1.06x faster                                                     |
| nqueens                    | 105 ms                                                   | 99.2 ms: 1.06x faster                                                    |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 6.31 ms: 1.05x faster                                                    |
| logging_simple             | 7.25 us                                                  | 6.89 us: 1.05x faster                                                    |
| genshi_xml                 | 61.6 ms                                                  | 58.6 ms: 1.05x faster                                                    |
| sqlite_synth               | 4.08 us                                                  | 3.91 us: 1.04x faster                                                    |
| shortest_path              | 565 ms                                                   | 582 ms: 1.03x slower                                                     |
| connected_components       | 547 ms                                                   | 566 ms: 1.04x slower                                                     |
| crypto_pyaes               | 84.9 ms                                                  | 88.3 ms: 1.04x slower                                                    |
| fannkuch                   | 478 ms                                                   | 502 ms: 1.05x slower                                                     |
| create_gc_cycles           | 3.39 ms                                                  | 3.68 ms: 1.08x slower                                                    |
| gc_traversal               | 5.92 ms                                                  | 6.51 ms: 1.10x slower                                                    |
| python_startup_no_site     | 8.79 ms                                                  | 10.2 ms: 1.16x slower                                                    |
| pidigits                   | 238 ms                                                   | 293 ms: 1.23x slower                                                     |
| subparsers                 | 20.3 ms                                                  | 25.9 ms: 1.27x slower                                                    |
| many_optionals             | 626 us                                                   | 820 us: 1.31x slower                                                     |
| bench_mp_pool              | 8.07 ms                                                  | 3.25 sec: 402.54x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (27): sympy_integrate, scimark_lu, coroutines, typing_runtime_protocols, sympy_sum, bench_thread_pool, sympy_expand, chaos, django_template, sqlalchemy_imperative, comprehensions, unpickle_pure_python, json, hexiom, asyncio_websockets, deltablue, docutils, meteor_contest, nbody, pickle_pure_python, python_startup, mako, raytrace, json_dumps, xml_etree_parse, json_loads, sympy_str
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250322-3.14.0a6+-bc26f95-CLANG/bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.062x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.06x