# Results vs. 3.13.0

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: linux-aarch64
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.061x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 300 ms: 1.04x faster                                                     |
| docutils       | 2.96 sec                                                 | 3.01 sec: 1.02x slower                                                   |
| html5lib       | 65.6 ms                                                  | 59.9 ms: 1.09x faster                                                    |
| sphinx         | 1.20 sec                                                 | 1.13 sec: 1.07x faster                                                   |
| Geometric mean | (ref)                                                    | 1.05x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 467 ms: 1.42x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 475 ms: 1.40x faster                                                     |
| async_tree_none            | 504 ms                                                   | 383 ms: 1.32x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 377 ms: 1.29x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 912 ms: 1.28x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 904 ms: 1.26x faster                                                     |
| async_generators           | 500 ms                                                   | 415 ms: 1.21x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 735 ms: 1.09x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 745 ms: 1.06x faster                                                     |
| Geometric mean             | (ref)                                                    | 1.20x faster                                                             |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 86.3 ms: 1.11x faster                                                    |
| pidigits       | 238 ms                                                   | 306 ms: 1.28x slower                                                     |
| Geometric mean | (ref)                                                    | 1.05x slower                                                             |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.35 ms: 1.17x faster                                                    |
| regex_compile  | 134 ms                                                   | 123 ms: 1.09x faster                                                     |
| regex_dna      | 263 ms                                                   | 250 ms: 1.05x faster                                                     |
| regex_v8       | 32.5 ms                                                  | 34.2 ms: 1.05x slower                                                    |
| Geometric mean | (ref)                                                    | 1.06x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark         | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_process | 82.1 ms                                                  | 74.8 ms: 1.10x faster                                                    |
| tomli_loads       | 2.67 sec                                                 | 2.47 sec: 1.08x faster                                                   |
| json_loads        | 32.8 us                                                  | 35.4 us: 1.08x slower                                                    |
| Geometric mean    | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (6): xml_etree_generate, unpickle_pure_python, xml_etree_iterparse, json_dumps, pickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 9.09 ms: 1.03x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.03x slower                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text    | 28.6 ms                                                  | 26.9 ms: 1.06x faster                                                    |
| Geometric mean | (ref)                                                    | 1.03x faster                                                             |

Benchmark hidden because not significant (3): django_template, genshi_xml, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy                   | 479 us                                                   | 318 us: 1.51x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 35.6 us: 1.49x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 467 ms: 1.42x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 475 ms: 1.40x faster                                                     |
| async_tree_none            | 504 ms                                                   | 383 ms: 1.32x faster                                                     |
| deepcopy_reduce            | 4.24 us                                                  | 3.28 us: 1.30x faster                                                    |
| spectral_norm              | 143 ms                                                   | 111 ms: 1.29x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 377 ms: 1.29x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 912 ms: 1.28x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 904 ms: 1.26x faster                                                     |
| async_generators           | 500 ms                                                   | 415 ms: 1.21x faster                                                     |
| scimark_fft                | 463 ms                                                   | 386 ms: 1.20x faster                                                     |
| logging_silent             | 135 ns                                                   | 112 ns: 1.20x faster                                                     |
| go                         | 164 ms                                                   | 138 ms: 1.19x faster                                                     |
| regex_effbot               | 5.10 ms                                                  | 4.35 ms: 1.17x faster                                                    |
| scimark_monte_carlo        | 87.8 ms                                                  | 76.8 ms: 1.14x faster                                                    |
| scimark_sor                | 164 ms                                                   | 144 ms: 1.14x faster                                                     |
| telco                      | 10.5 ms                                                  | 9.22 ms: 1.13x faster                                                    |
| richards                   | 54.5 ms                                                  | 48.5 ms: 1.12x faster                                                    |
| coverage                   | 106 ms                                                   | 94.0 ms: 1.12x faster                                                    |
| pylint                     | 345 ms                                                   | 311 ms: 1.11x faster                                                     |
| float                      | 95.8 ms                                                  | 86.3 ms: 1.11x faster                                                    |
| bpe_tokeniser              | 6.02 sec                                                 | 5.42 sec: 1.11x faster                                                   |
| richards_super             | 60.8 ms                                                  | 55.0 ms: 1.11x faster                                                    |
| pyflate                    | 582 ms                                                   | 527 ms: 1.10x faster                                                     |
| xml_etree_process          | 82.1 ms                                                  | 74.8 ms: 1.10x faster                                                    |
| html5lib                   | 65.6 ms                                                  | 59.9 ms: 1.09x faster                                                    |
| sympy_sum                  | 151 ms                                                   | 139 ms: 1.09x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 735 ms: 1.09x faster                                                     |
| sqlglot_transpile          | 1.84 ms                                                  | 1.69 ms: 1.09x faster                                                    |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 6.12 ms: 1.09x faster                                                    |
| pathlib                    | 24.3 ms                                                  | 22.4 ms: 1.09x faster                                                    |
| regex_compile              | 134 ms                                                   | 123 ms: 1.09x faster                                                     |
| logging_format             | 8.10 us                                                  | 7.49 us: 1.08x faster                                                    |
| thrift                     | 1.01 ms                                                  | 937 us: 1.08x faster                                                     |
| tomli_loads                | 2.67 sec                                                 | 2.47 sec: 1.08x faster                                                   |
| generators                 | 40.3 ms                                                  | 37.5 ms: 1.08x faster                                                    |
| sphinx                     | 1.20 sec                                                 | 1.13 sec: 1.07x faster                                                   |
| comprehensions             | 20.8 us                                                  | 19.5 us: 1.07x faster                                                    |
| nqueens                    | 105 ms                                                   | 98.6 ms: 1.06x faster                                                    |
| genshi_text                | 28.6 ms                                                  | 26.9 ms: 1.06x faster                                                    |
| sqlalchemy_declarative     | 154 ms                                                   | 145 ms: 1.06x faster                                                     |
| typing_runtime_protocols   | 197 us                                                   | 186 us: 1.06x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 745 ms: 1.06x faster                                                     |
| chaos                      | 70.7 ms                                                  | 66.8 ms: 1.06x faster                                                    |
| k_core                     | 2.99 sec                                                 | 2.83 sec: 1.06x faster                                                   |
| mdp                        | 3.45 sec                                                 | 3.27 sec: 1.05x faster                                                   |
| bench_thread_pool          | 1.34 ms                                                  | 1.27 ms: 1.05x faster                                                    |
| pycparser                  | 1.34 sec                                                 | 1.28 sec: 1.05x faster                                                   |
| regex_dna                  | 263 ms                                                   | 250 ms: 1.05x faster                                                     |
| hexiom                     | 7.34 ms                                                  | 7.04 ms: 1.04x faster                                                    |
| 2to3                       | 313 ms                                                   | 300 ms: 1.04x faster                                                     |
| pprint_pformat             | 1.99 sec                                                 | 1.92 sec: 1.03x faster                                                   |
| pprint_safe_repr           | 962 ms                                                   | 934 ms: 1.03x faster                                                     |
| connected_components       | 547 ms                                                   | 535 ms: 1.02x faster                                                     |
| docutils                   | 2.96 sec                                                 | 3.01 sec: 1.02x slower                                                   |
| python_startup_no_site     | 8.79 ms                                                  | 9.09 ms: 1.03x slower                                                    |
| regex_v8                   | 32.5 ms                                                  | 34.2 ms: 1.05x slower                                                    |
| json_loads                 | 32.8 us                                                  | 35.4 us: 1.08x slower                                                    |
| create_gc_cycles           | 3.39 ms                                                  | 3.88 ms: 1.15x slower                                                    |
| gc_traversal               | 5.92 ms                                                  | 6.87 ms: 1.16x slower                                                    |
| pidigits                   | 238 ms                                                   | 306 ms: 1.28x slower                                                     |
| subparsers                 | 20.3 ms                                                  | 26.2 ms: 1.29x slower                                                    |
| many_optionals             | 626 us                                                   | 844 us: 1.35x slower                                                     |
| bench_mp_pool              | 8.07 ms                                                  | 6.84 sec: 848.37x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.01x slower                                                             |

Benchmark hidden because not significant (30): xml_etree_generate, sqlglot_optimize, logging_simple, sqlglot_normalize, unpickle_pure_python, sqlglot_parse, sympy_integrate, coroutines, xml_etree_iterparse, django_template, genshi_xml, sympy_expand, mako, deltablue, nbody, raytrace, scimark_lu, sqlalchemy_imperative, asyncio_websockets, shortest_path, sqlite_synth, json_dumps, python_startup, crypto_pyaes, meteor_contest, sympy_str, fannkuch, json, pickle_pure_python, xml_etree_parse
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (9) of results/bm-20250222-3.14.0a5+-5ec4bf8-CLANG/bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.061x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.06x