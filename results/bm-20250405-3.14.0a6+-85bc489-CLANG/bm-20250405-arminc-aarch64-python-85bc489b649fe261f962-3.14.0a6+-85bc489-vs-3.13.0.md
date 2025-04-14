# Results vs. 3.13.0

- fork: python
- ref: 85bc489b649fe261f962
- machine: linux-aarch64
- commit hash: 85bc489
- commit date: 2025-04-05
- overall geometric mean: 1.080x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250405-arminc-aarch64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 288 ms: 1.09x faster                                                     |
| docutils       | 2.96 sec                                                 | 2.91 sec: 1.02x faster                                                   |
| html5lib       | 65.6 ms                                                  | 58.3 ms: 1.12x faster                                                    |
| sphinx         | 1.20 sec                                                 | 1.11 sec: 1.09x faster                                                   |
| Geometric mean | (ref)                                                    | 1.08x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250405-arminc-aarch64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 664 ms                                                   | 446 ms: 1.49x faster                                                     |
| async_tree_memoization_tg  | 663 ms                                                   | 445 ms: 1.49x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 860 ms: 1.35x faster                                                     |
| async_tree_none            | 504 ms                                                   | 375 ms: 1.34x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 362 ms: 1.34x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 862 ms: 1.32x faster                                                     |
| async_generators           | 500 ms                                                   | 409 ms: 1.22x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 698 ms: 1.15x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 715 ms: 1.10x faster                                                     |
| Geometric mean             | (ref)                                                    | 1.25x faster                                                             |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250405-arminc-aarch64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 84.2 ms: 1.14x faster                                                    |
| nbody          | 118 ms                                                   | 130 ms: 1.10x slower                                                     |
| pidigits       | 238 ms                                                   | 290 ms: 1.22x slower                                                     |
| Geometric mean | (ref)                                                    | 1.05x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250405-arminc-aarch64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.30 ms: 1.19x faster                                                    |
| regex_compile  | 134 ms                                                   | 121 ms: 1.10x faster                                                     |
| regex_dna      | 263 ms                                                   | 245 ms: 1.07x faster                                                     |
| regex_v8       | 32.5 ms                                                  | 30.4 ms: 1.07x faster                                                    |
| Geometric mean | (ref)                                                    | 1.11x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250405-arminc-aarch64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads         | 2.67 sec                                                 | 2.33 sec: 1.15x faster                                                   |
| xml_etree_generate  | 118 ms                                                   | 105 ms: 1.13x faster                                                     |
| xml_etree_process   | 82.1 ms                                                  | 75.9 ms: 1.08x faster                                                    |
| xml_etree_iterparse | 159 ms                                                   | 150 ms: 1.06x faster                                                     |
| Geometric mean      | (ref)                                                    | 1.05x faster                                                             |

Benchmark hidden because not significant (5): unpickle_pure_python, json_dumps, pickle_pure_python, xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250405-arminc-aarch64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 10.2 ms: 1.16x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.08x slower                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250405-arminc-aarch64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 28.6 ms                                                  | 25.6 ms: 1.12x faster                                                    |
| genshi_xml      | 61.6 ms                                                  | 58.4 ms: 1.05x faster                                                    |
| django_template | 39.4 ms                                                  | 38.0 ms: 1.04x faster                                                    |
| Geometric mean  | (ref)                                                    | 1.05x faster                                                             |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250405-arminc-aarch64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.61 sec: 2.14x faster                                                   |
| deepcopy                   | 479 us                                                   | 299 us: 1.60x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 446 ms: 1.49x faster                                                     |
| async_tree_memoization_tg  | 663 ms                                                   | 445 ms: 1.49x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 35.9 us: 1.47x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 860 ms: 1.35x faster                                                     |
| async_tree_none            | 504 ms                                                   | 375 ms: 1.34x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 362 ms: 1.34x faster                                                     |
| deepcopy_reduce            | 4.24 us                                                  | 3.20 us: 1.33x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 862 ms: 1.32x faster                                                     |
| go                         | 164 ms                                                   | 131 ms: 1.26x faster                                                     |
| async_generators           | 500 ms                                                   | 409 ms: 1.22x faster                                                     |
| spectral_norm              | 143 ms                                                   | 119 ms: 1.21x faster                                                     |
| logging_silent             | 135 ns                                                   | 111 ns: 1.21x faster                                                     |
| regex_effbot               | 5.10 ms                                                  | 4.30 ms: 1.19x faster                                                    |
| scimark_sor                | 164 ms                                                   | 139 ms: 1.18x faster                                                     |
| telco                      | 10.5 ms                                                  | 8.88 ms: 1.18x faster                                                    |
| scimark_fft                | 463 ms                                                   | 400 ms: 1.16x faster                                                     |
| pylint                     | 345 ms                                                   | 300 ms: 1.15x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 698 ms: 1.15x faster                                                     |
| tomli_loads                | 2.67 sec                                                 | 2.33 sec: 1.15x faster                                                   |
| bpe_tokeniser              | 6.02 sec                                                 | 5.27 sec: 1.14x faster                                                   |
| pathlib                    | 24.3 ms                                                  | 21.3 ms: 1.14x faster                                                    |
| float                      | 95.8 ms                                                  | 84.2 ms: 1.14x faster                                                    |
| richards                   | 54.5 ms                                                  | 48.1 ms: 1.13x faster                                                    |
| xml_etree_generate         | 118 ms                                                   | 105 ms: 1.13x faster                                                     |
| html5lib                   | 65.6 ms                                                  | 58.3 ms: 1.12x faster                                                    |
| generators                 | 40.3 ms                                                  | 35.9 ms: 1.12x faster                                                    |
| scimark_monte_carlo        | 87.8 ms                                                  | 78.4 ms: 1.12x faster                                                    |
| coverage                   | 106 ms                                                   | 94.4 ms: 1.12x faster                                                    |
| genshi_text                | 28.6 ms                                                  | 25.6 ms: 1.12x faster                                                    |
| sympy_sum                  | 151 ms                                                   | 135 ms: 1.12x faster                                                     |
| logging_format             | 8.10 us                                                  | 7.27 us: 1.12x faster                                                    |
| pyflate                    | 582 ms                                                   | 526 ms: 1.11x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 715 ms: 1.10x faster                                                     |
| regex_compile              | 134 ms                                                   | 121 ms: 1.10x faster                                                     |
| sympy_integrate            | 21.4 ms                                                  | 19.5 ms: 1.10x faster                                                    |
| pycparser                  | 1.34 sec                                                 | 1.23 sec: 1.10x faster                                                   |
| logging_simple             | 7.25 us                                                  | 6.62 us: 1.09x faster                                                    |
| sphinx                     | 1.20 sec                                                 | 1.11 sec: 1.09x faster                                                   |
| 2to3                       | 313 ms                                                   | 288 ms: 1.09x faster                                                     |
| richards_super             | 60.8 ms                                                  | 56.0 ms: 1.09x faster                                                    |
| k_core                     | 2.99 sec                                                 | 2.76 sec: 1.08x faster                                                   |
| xml_etree_process          | 82.1 ms                                                  | 75.9 ms: 1.08x faster                                                    |
| scimark_lu                 | 146 ms                                                   | 135 ms: 1.08x faster                                                     |
| regex_dna                  | 263 ms                                                   | 245 ms: 1.07x faster                                                     |
| chaos                      | 70.7 ms                                                  | 65.9 ms: 1.07x faster                                                    |
| regex_v8                   | 32.5 ms                                                  | 30.4 ms: 1.07x faster                                                    |
| pprint_pformat             | 1.99 sec                                                 | 1.86 sec: 1.07x faster                                                   |
| deltablue                  | 3.97 ms                                                  | 3.73 ms: 1.06x faster                                                    |
| sqlite_synth               | 4.08 us                                                  | 3.84 us: 1.06x faster                                                    |
| xml_etree_iterparse        | 159 ms                                                   | 150 ms: 1.06x faster                                                     |
| pprint_safe_repr           | 962 ms                                                   | 910 ms: 1.06x faster                                                     |
| typing_runtime_protocols   | 197 us                                                   | 187 us: 1.05x faster                                                     |
| genshi_xml                 | 61.6 ms                                                  | 58.4 ms: 1.05x faster                                                    |
| sympy_expand               | 472 ms                                                   | 452 ms: 1.05x faster                                                     |
| django_template            | 39.4 ms                                                  | 38.0 ms: 1.04x faster                                                    |
| docutils                   | 2.96 sec                                                 | 2.91 sec: 1.02x faster                                                   |
| shortest_path              | 565 ms                                                   | 576 ms: 1.02x slower                                                     |
| connected_components       | 547 ms                                                   | 561 ms: 1.03x slower                                                     |
| nbody                      | 118 ms                                                   | 130 ms: 1.10x slower                                                     |
| create_gc_cycles           | 3.39 ms                                                  | 3.76 ms: 1.11x slower                                                    |
| gc_traversal               | 5.92 ms                                                  | 6.58 ms: 1.11x slower                                                    |
| python_startup_no_site     | 8.79 ms                                                  | 10.2 ms: 1.16x slower                                                    |
| pidigits                   | 238 ms                                                   | 290 ms: 1.22x slower                                                     |
| subparsers                 | 20.3 ms                                                  | 25.2 ms: 1.24x slower                                                    |
| many_optionals             | 626 us                                                   | 810 us: 1.29x slower                                                     |
| bench_mp_pool              | 8.07 ms                                                  | 2.87 sec: 355.72x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.02x faster                                                             |

Benchmark hidden because not significant (22): unpickle_pure_python, coroutines, sqlalchemy_declarative, comprehensions, json_dumps, hexiom, nqueens, sympy_str, bench_thread_pool, asyncio_websockets, pickle_pure_python, scimark_sparse_mat_mult, mako, meteor_contest, python_startup, xml_etree_parse, json, crypto_pyaes, raytrace, fannkuch, sqlalchemy_imperative, json_loads
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (13) of results/bm-20250405-3.14.0a6+-85bc489-CLANG/bm-20250405-arminc-aarch64-python-85bc489b649fe261f962-3.14.0a6+-85bc489.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.080x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.07x