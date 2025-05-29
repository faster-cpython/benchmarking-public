# Results vs. 3.13.0

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: linux-aarch64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.064x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 294 ms: 1.06x faster                                                     |
| html5lib       | 65.6 ms                                                  | 59.3 ms: 1.11x faster                                                    |
| sphinx         | 1.20 sec                                                 | 1.13 sec: 1.06x faster                                                   |
| Geometric mean | (ref)                                                    | 1.06x faster                                                             |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 472 ms: 1.40x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 480 ms: 1.38x faster                                                     |
| async_tree_none            | 504 ms                                                   | 387 ms: 1.30x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 904 ms: 1.29x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 376 ms: 1.29x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 908 ms: 1.25x faster                                                     |
| async_generators           | 500 ms                                                   | 419 ms: 1.19x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 739 ms: 1.08x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 758 ms: 1.04x faster                                                     |
| Geometric mean             | (ref)                                                    | 1.20x faster                                                             |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 82.9 ms: 1.16x faster                                                    |
| pidigits       | 238 ms                                                   | 303 ms: 1.27x slower                                                     |
| Geometric mean | (ref)                                                    | 1.02x slower                                                             |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 134 ms                                                   | 120 ms: 1.11x faster                                                     |
| regex_effbot   | 5.10 ms                                                  | 4.62 ms: 1.10x faster                                                    |
| regex_dna      | 263 ms                                                   | 250 ms: 1.05x faster                                                     |
| regex_v8       | 32.5 ms                                                  | 34.5 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                    | 1.05x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|--------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_generate | 118 ms                                                   | 103 ms: 1.15x faster                                                     |
| xml_etree_process  | 82.1 ms                                                  | 74.6 ms: 1.10x faster                                                    |
| tomli_loads        | 2.67 sec                                                 | 2.46 sec: 1.09x faster                                                   |
| json_loads         | 32.8 us                                                  | 36.5 us: 1.11x slower                                                    |
| Geometric mean     | (ref)                                                    | 1.02x faster                                                             |

Benchmark hidden because not significant (5): unpickle_pure_python, xml_etree_iterparse, pickle_pure_python, xml_etree_parse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 9.30 ms: 1.06x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.04x slower                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text    | 28.6 ms                                                  | 25.7 ms: 1.11x faster                                                    |
| genshi_xml     | 61.6 ms                                                  | 58.8 ms: 1.05x faster                                                    |
| Geometric mean | (ref)                                                    | 1.04x faster                                                             |

Benchmark hidden because not significant (2): mako, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy                   | 479 us                                                   | 316 us: 1.51x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 35.4 us: 1.50x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 472 ms: 1.40x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 480 ms: 1.38x faster                                                     |
| spectral_norm              | 143 ms                                                   | 109 ms: 1.31x faster                                                     |
| async_tree_none            | 504 ms                                                   | 387 ms: 1.30x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 904 ms: 1.29x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 376 ms: 1.29x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 908 ms: 1.25x faster                                                     |
| deepcopy_reduce            | 4.24 us                                                  | 3.39 us: 1.25x faster                                                    |
| scimark_fft                | 463 ms                                                   | 375 ms: 1.23x faster                                                     |
| go                         | 164 ms                                                   | 133 ms: 1.23x faster                                                     |
| async_generators           | 500 ms                                                   | 419 ms: 1.19x faster                                                     |
| float                      | 95.8 ms                                                  | 82.9 ms: 1.16x faster                                                    |
| xml_etree_generate         | 118 ms                                                   | 103 ms: 1.15x faster                                                     |
| pathlib                    | 24.3 ms                                                  | 21.2 ms: 1.15x faster                                                    |
| logging_silent             | 135 ns                                                   | 118 ns: 1.14x faster                                                     |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 5.83 ms: 1.14x faster                                                    |
| scimark_monte_carlo        | 87.8 ms                                                  | 77.1 ms: 1.14x faster                                                    |
| bpe_tokeniser              | 6.02 sec                                                 | 5.33 sec: 1.13x faster                                                   |
| pylint                     | 345 ms                                                   | 306 ms: 1.13x faster                                                     |
| scimark_sor                | 164 ms                                                   | 147 ms: 1.12x faster                                                     |
| coverage                   | 106 ms                                                   | 94.4 ms: 1.12x faster                                                    |
| regex_compile              | 134 ms                                                   | 120 ms: 1.11x faster                                                     |
| genshi_text                | 28.6 ms                                                  | 25.7 ms: 1.11x faster                                                    |
| html5lib                   | 65.6 ms                                                  | 59.3 ms: 1.11x faster                                                    |
| regex_effbot               | 5.10 ms                                                  | 4.62 ms: 1.10x faster                                                    |
| xml_etree_process          | 82.1 ms                                                  | 74.6 ms: 1.10x faster                                                    |
| logging_format             | 8.10 us                                                  | 7.37 us: 1.10x faster                                                    |
| richards                   | 54.5 ms                                                  | 49.6 ms: 1.10x faster                                                    |
| sympy_sum                  | 151 ms                                                   | 138 ms: 1.09x faster                                                     |
| pyflate                    | 582 ms                                                   | 532 ms: 1.09x faster                                                     |
| telco                      | 10.5 ms                                                  | 9.57 ms: 1.09x faster                                                    |
| richards_super             | 60.8 ms                                                  | 55.7 ms: 1.09x faster                                                    |
| generators                 | 40.3 ms                                                  | 37.0 ms: 1.09x faster                                                    |
| typing_runtime_protocols   | 197 us                                                   | 181 us: 1.09x faster                                                     |
| tomli_loads                | 2.67 sec                                                 | 2.46 sec: 1.09x faster                                                   |
| sqlglot_optimize           | 65.2 ms                                                  | 60.1 ms: 1.08x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 739 ms: 1.08x faster                                                     |
| comprehensions             | 20.8 us                                                  | 19.4 us: 1.07x faster                                                    |
| mdp                        | 3.45 sec                                                 | 3.23 sec: 1.07x faster                                                   |
| pycparser                  | 1.34 sec                                                 | 1.26 sec: 1.07x faster                                                   |
| nqueens                    | 105 ms                                                   | 98.3 ms: 1.07x faster                                                    |
| k_core                     | 2.99 sec                                                 | 2.80 sec: 1.07x faster                                                   |
| sphinx                     | 1.20 sec                                                 | 1.13 sec: 1.06x faster                                                   |
| logging_simple             | 7.25 us                                                  | 6.81 us: 1.06x faster                                                    |
| 2to3                       | 313 ms                                                   | 294 ms: 1.06x faster                                                     |
| sqlglot_parse              | 1.43 ms                                                  | 1.35 ms: 1.06x faster                                                    |
| bench_thread_pool          | 1.34 ms                                                  | 1.26 ms: 1.06x faster                                                    |
| sqlglot_normalize          | 131 ms                                                   | 125 ms: 1.05x faster                                                     |
| regex_dna                  | 263 ms                                                   | 250 ms: 1.05x faster                                                     |
| pprint_pformat             | 1.99 sec                                                 | 1.89 sec: 1.05x faster                                                   |
| genshi_xml                 | 61.6 ms                                                  | 58.8 ms: 1.05x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 758 ms: 1.04x faster                                                     |
| python_startup_no_site     | 8.79 ms                                                  | 9.30 ms: 1.06x slower                                                    |
| regex_v8                   | 32.5 ms                                                  | 34.5 ms: 1.06x slower                                                    |
| create_gc_cycles           | 3.39 ms                                                  | 3.70 ms: 1.09x slower                                                    |
| json_loads                 | 32.8 us                                                  | 36.5 us: 1.11x slower                                                    |
| gc_traversal               | 5.92 ms                                                  | 6.82 ms: 1.15x slower                                                    |
| pidigits                   | 238 ms                                                   | 303 ms: 1.27x slower                                                     |
| subparsers                 | 20.3 ms                                                  | 26.0 ms: 1.28x slower                                                    |
| many_optionals             | 626 us                                                   | 808 us: 1.29x slower                                                     |
| bench_mp_pool              | 8.07 ms                                                  | 7.51 sec: 930.38x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.00x slower                                                             |

Benchmark hidden because not significant (32): sqlglot_transpile, thrift, sqlalchemy_imperative, scimark_lu, unpickle_pure_python, xml_etree_iterparse, chaos, nbody, sqlalchemy_declarative, sympy_expand, deltablue, sympy_integrate, pprint_safe_repr, coroutines, hexiom, connected_components, meteor_contest, mako, django_template, shortest_path, sqlite_synth, asyncio_websockets, raytrace, docutils, sympy_str, pickle_pure_python, python_startup, xml_etree_parse, fannkuch, json, json_dumps, crypto_pyaes
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20250208-3.14.0a4+-29f8a67-CLANG/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: dulwich_log

- Geometric mean (including insignificant results): 1.064x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.06x