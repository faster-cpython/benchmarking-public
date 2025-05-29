# Results vs. 3.13.0

- fork: python
- ref: 359c7dde3bb074e02968
- machine: linux-aarch64
- commit hash: 359c7dd
- commit date: 2025-02-16
- overall geometric mean: 1.049x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 302 ms: 1.04x faster                                                     |
| docutils       | 2.96 sec                                                 | 3.00 sec: 1.01x slower                                                   |
| html5lib       | 65.6 ms                                                  | 60.2 ms: 1.09x faster                                                    |
| sphinx         | 1.20 sec                                                 | 1.14 sec: 1.05x faster                                                   |
| Geometric mean | (ref)                                                    | 1.04x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 485 ms: 1.37x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 497 ms: 1.33x faster                                                     |
| async_tree_none            | 504 ms                                                   | 394 ms: 1.28x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 930 ms: 1.25x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 390 ms: 1.24x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 927 ms: 1.23x faster                                                     |
| async_generators           | 500 ms                                                   | 425 ms: 1.18x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 755 ms: 1.06x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 755 ms: 1.05x faster                                                     |
| Geometric mean             | (ref)                                                    | 1.18x faster                                                             |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 88.0 ms: 1.09x faster                                                    |
| pidigits       | 238 ms                                                   | 305 ms: 1.28x slower                                                     |
| Geometric mean | (ref)                                                    | 1.05x slower                                                             |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.81 ms: 1.06x faster                                                    |
| regex_v8       | 32.5 ms                                                  | 34.6 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (2): regex_compile, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|--------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_generate | 118 ms                                                   | 108 ms: 1.10x faster                                                     |
| xml_etree_process  | 82.1 ms                                                  | 75.5 ms: 1.09x faster                                                    |
| tomli_loads        | 2.67 sec                                                 | 2.49 sec: 1.07x faster                                                   |
| xml_etree_parse    | 203 ms                                                   | 212 ms: 1.05x slower                                                     |
| Geometric mean     | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (5): xml_etree_iterparse, unpickle_pure_python, json_dumps, json_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 16.5 ms: 1.03x slower                                                    |
| python_startup_no_site | 8.79 ms                                                  | 9.12 ms: 1.04x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.03x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text    | 28.6 ms                                                  | 27.0 ms: 1.06x faster                                                    |
| Geometric mean | (ref)                                                    | 1.02x faster                                                             |

Benchmark hidden because not significant (3): django_template, genshi_xml, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy                   | 479 us                                                   | 320 us: 1.49x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 36.5 us: 1.45x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 485 ms: 1.37x faster                                                     |
| spectral_norm              | 143 ms                                                   | 107 ms: 1.34x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 497 ms: 1.33x faster                                                     |
| async_tree_none            | 504 ms                                                   | 394 ms: 1.28x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 930 ms: 1.25x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 390 ms: 1.24x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 927 ms: 1.23x faster                                                     |
| scimark_fft                | 463 ms                                                   | 383 ms: 1.21x faster                                                     |
| go                         | 164 ms                                                   | 136 ms: 1.21x faster                                                     |
| deepcopy_reduce            | 4.24 us                                                  | 3.60 us: 1.18x faster                                                    |
| async_generators           | 500 ms                                                   | 425 ms: 1.18x faster                                                     |
| scimark_sor                | 164 ms                                                   | 142 ms: 1.16x faster                                                     |
| logging_silent             | 135 ns                                                   | 118 ns: 1.14x faster                                                     |
| pathlib                    | 24.3 ms                                                  | 21.4 ms: 1.14x faster                                                    |
| telco                      | 10.5 ms                                                  | 9.25 ms: 1.13x faster                                                    |
| bpe_tokeniser              | 6.02 sec                                                 | 5.39 sec: 1.12x faster                                                   |
| coverage                   | 106 ms                                                   | 94.9 ms: 1.11x faster                                                    |
| generators                 | 40.3 ms                                                  | 36.6 ms: 1.10x faster                                                    |
| xml_etree_generate         | 118 ms                                                   | 108 ms: 1.10x faster                                                     |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 6.09 ms: 1.09x faster                                                    |
| html5lib                   | 65.6 ms                                                  | 60.2 ms: 1.09x faster                                                    |
| float                      | 95.8 ms                                                  | 88.0 ms: 1.09x faster                                                    |
| xml_etree_process          | 82.1 ms                                                  | 75.5 ms: 1.09x faster                                                    |
| pylint                     | 345 ms                                                   | 318 ms: 1.09x faster                                                     |
| richards                   | 54.5 ms                                                  | 50.5 ms: 1.08x faster                                                    |
| sympy_sum                  | 151 ms                                                   | 140 ms: 1.08x faster                                                     |
| pyflate                    | 582 ms                                                   | 541 ms: 1.08x faster                                                     |
| tomli_loads                | 2.67 sec                                                 | 2.49 sec: 1.07x faster                                                   |
| k_core                     | 2.99 sec                                                 | 2.79 sec: 1.07x faster                                                   |
| logging_format             | 8.10 us                                                  | 7.60 us: 1.07x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 755 ms: 1.06x faster                                                     |
| regex_effbot               | 5.10 ms                                                  | 4.81 ms: 1.06x faster                                                    |
| comprehensions             | 20.8 us                                                  | 19.6 us: 1.06x faster                                                    |
| typing_runtime_protocols   | 197 us                                                   | 186 us: 1.06x faster                                                     |
| sqlalchemy_declarative     | 154 ms                                                   | 145 ms: 1.06x faster                                                     |
| genshi_text                | 28.6 ms                                                  | 27.0 ms: 1.06x faster                                                    |
| chaos                      | 70.7 ms                                                  | 67.0 ms: 1.06x faster                                                    |
| nqueens                    | 105 ms                                                   | 99.6 ms: 1.05x faster                                                    |
| sphinx                     | 1.20 sec                                                 | 1.14 sec: 1.05x faster                                                   |
| mdp                        | 3.45 sec                                                 | 3.28 sec: 1.05x faster                                                   |
| pycparser                  | 1.34 sec                                                 | 1.28 sec: 1.05x faster                                                   |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 755 ms: 1.05x faster                                                     |
| 2to3                       | 313 ms                                                   | 302 ms: 1.04x faster                                                     |
| pprint_pformat             | 1.99 sec                                                 | 1.95 sec: 1.02x faster                                                   |
| docutils                   | 2.96 sec                                                 | 3.00 sec: 1.01x slower                                                   |
| python_startup             | 16.0 ms                                                  | 16.5 ms: 1.03x slower                                                    |
| python_startup_no_site     | 8.79 ms                                                  | 9.12 ms: 1.04x slower                                                    |
| xml_etree_parse            | 203 ms                                                   | 212 ms: 1.05x slower                                                     |
| crypto_pyaes               | 84.9 ms                                                  | 89.4 ms: 1.05x slower                                                    |
| regex_v8                   | 32.5 ms                                                  | 34.6 ms: 1.06x slower                                                    |
| create_gc_cycles           | 3.39 ms                                                  | 3.86 ms: 1.14x slower                                                    |
| gc_traversal               | 5.92 ms                                                  | 6.76 ms: 1.14x slower                                                    |
| pidigits                   | 238 ms                                                   | 305 ms: 1.28x slower                                                     |
| subparsers                 | 20.3 ms                                                  | 26.6 ms: 1.31x slower                                                    |
| many_optionals             | 626 us                                                   | 870 us: 1.39x slower                                                     |
| bench_mp_pool              | 8.07 ms                                                  | 4.43 sec: 548.46x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.02x slower                                                             |

Benchmark hidden because not significant (37): scimark_monte_carlo, thrift, sqlglot_optimize, bench_thread_pool, logging_simple, richards_super, sqlglot_transpile, sympy_integrate, sqlglot_normalize, regex_compile, scimark_lu, hexiom, coroutines, django_template, sqlalchemy_imperative, nbody, sympy_expand, xml_etree_iterparse, genshi_xml, deltablue, unpickle_pure_python, asyncio_websockets, meteor_contest, sqlglot_parse, regex_dna, shortest_path, sqlite_synth, pprint_safe_repr, connected_components, json, mako, json_dumps, sympy_str, raytrace, fannkuch, json_loads, pickle_pure_python
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (9) of results/bm-20250216-3.14.0a5+-359c7dd-CLANG/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.049x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.06x