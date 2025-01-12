# Results vs. 3.13.0

- fork: python
- ref: 22a442181d5f1ac496da
- machine: linux-aarch64
- commit hash: 22a4421
- commit date: 2025-01-11
- overall geometric mean: 1.021x slower
- HPT reliability: 90.36%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.24 sec: 1.09x slower                                                   |
| html5lib       | 65.6 ms                                                  | 68.9 ms: 1.05x slower                                                    |
| sphinx         | 1.20 sec                                                 | 1.27 sec: 1.06x slower                                                   |
| Geometric mean | (ref)                                                    | 1.05x slower                                                             |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 482 ms: 1.37x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 518 ms: 1.28x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 918 ms: 1.27x faster                                                     |
| async_tree_none            | 504 ms                                                   | 406 ms: 1.24x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 390 ms: 1.24x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 921 ms: 1.24x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 675 ms: 1.19x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 700 ms: 1.13x faster                                                     |
| async_generators           | 500 ms                                                   | 521 ms: 1.04x slower                                                     |
| Geometric mean             | (ref)                                                    | 1.17x faster                                                             |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): float, nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.08 ms: 1.25x faster                                                    |
| Geometric mean | (ref)                                                    | 1.04x faster                                                             |

Benchmark hidden because not significant (3): regex_v8, regex_dna, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 179 ms: 1.13x faster                                                     |
| xml_etree_iterparse | 159 ms                                                   | 143 ms: 1.11x faster                                                     |
| tomli_loads         | 2.67 sec                                                 | 2.53 sec: 1.05x faster                                                   |
| pickle_pure_python  | 374 us                                                   | 403 us: 1.08x slower                                                     |
| Geometric mean      | (ref)                                                    | 1.03x faster                                                             |

Benchmark hidden because not significant (5): json_loads, xml_etree_generate, xml_etree_process, unpickle_pure_python, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 9.09 ms: 1.03x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.02x slower                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 14.0 ms                                                  | 13.3 ms: 1.05x faster                                                    |
| genshi_text     | 28.6 ms                                                  | 33.1 ms: 1.16x slower                                                    |
| django_template | 39.4 ms                                                  | 47.0 ms: 1.19x slower                                                    |
| genshi_xml      | 61.6 ms                                                  | 83.7 ms: 1.36x slower                                                    |
| Geometric mean  | (ref)                                                    | 1.16x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 482 ms: 1.37x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 39.0 us: 1.36x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 518 ms: 1.28x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 918 ms: 1.27x faster                                                     |
| regex_effbot               | 5.10 ms                                                  | 4.08 ms: 1.25x faster                                                    |
| async_tree_none            | 504 ms                                                   | 406 ms: 1.24x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 390 ms: 1.24x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 921 ms: 1.24x faster                                                     |
| deepcopy                   | 479 us                                                   | 402 us: 1.19x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 675 ms: 1.19x faster                                                     |
| xml_etree_parse            | 203 ms                                                   | 179 ms: 1.13x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 700 ms: 1.13x faster                                                     |
| xml_etree_iterparse        | 159 ms                                                   | 143 ms: 1.11x faster                                                     |
| scimark_fft                | 463 ms                                                   | 420 ms: 1.10x faster                                                     |
| telco                      | 10.5 ms                                                  | 9.69 ms: 1.08x faster                                                    |
| pathlib                    | 24.3 ms                                                  | 22.9 ms: 1.06x faster                                                    |
| deepcopy_reduce            | 4.24 us                                                  | 4.00 us: 1.06x faster                                                    |
| tomli_loads                | 2.67 sec                                                 | 2.53 sec: 1.05x faster                                                   |
| mako                       | 14.0 ms                                                  | 13.3 ms: 1.05x faster                                                    |
| bpe_tokeniser              | 6.02 sec                                                 | 5.78 sec: 1.04x faster                                                   |
| k_core                     | 2.99 sec                                                 | 2.91 sec: 1.03x faster                                                   |
| shortest_path              | 565 ms                                                   | 581 ms: 1.03x slower                                                     |
| mdp                        | 3.45 sec                                                 | 3.55 sec: 1.03x slower                                                   |
| python_startup_no_site     | 8.79 ms                                                  | 9.09 ms: 1.03x slower                                                    |
| async_generators           | 500 ms                                                   | 521 ms: 1.04x slower                                                     |
| html5lib                   | 65.6 ms                                                  | 68.9 ms: 1.05x slower                                                    |
| scimark_lu                 | 146 ms                                                   | 154 ms: 1.05x slower                                                     |
| sphinx                     | 1.20 sec                                                 | 1.27 sec: 1.06x slower                                                   |
| sympy_sum                  | 151 ms                                                   | 160 ms: 1.06x slower                                                     |
| sqlglot_normalize          | 131 ms                                                   | 139 ms: 1.06x slower                                                     |
| pyflate                    | 582 ms                                                   | 619 ms: 1.06x slower                                                     |
| logging_format             | 8.10 us                                                  | 8.63 us: 1.06x slower                                                    |
| meteor_contest             | 117 ms                                                   | 125 ms: 1.07x slower                                                     |
| create_gc_cycles           | 3.39 ms                                                  | 3.64 ms: 1.07x slower                                                    |
| sqlalchemy_imperative      | 16.1 ms                                                  | 17.4 ms: 1.08x slower                                                    |
| pickle_pure_python         | 374 us                                                   | 403 us: 1.08x slower                                                     |
| fannkuch                   | 478 ms                                                   | 517 ms: 1.08x slower                                                     |
| sqlglot_transpile          | 1.84 ms                                                  | 2.00 ms: 1.09x slower                                                    |
| pycparser                  | 1.34 sec                                                 | 1.46 sec: 1.09x slower                                                   |
| sympy_integrate            | 21.4 ms                                                  | 23.4 ms: 1.09x slower                                                    |
| docutils                   | 2.96 sec                                                 | 3.24 sec: 1.09x slower                                                   |
| sqlglot_parse              | 1.43 ms                                                  | 1.57 ms: 1.09x slower                                                    |
| sympy_expand               | 472 ms                                                   | 518 ms: 1.10x slower                                                     |
| logging_simple             | 7.25 us                                                  | 8.04 us: 1.11x slower                                                    |
| logging_silent             | 135 ns                                                   | 150 ns: 1.11x slower                                                     |
| deltablue                  | 3.97 ms                                                  | 4.42 ms: 1.11x slower                                                    |
| typing_runtime_protocols   | 197 us                                                   | 220 us: 1.12x slower                                                     |
| crypto_pyaes               | 84.9 ms                                                  | 95.1 ms: 1.12x slower                                                    |
| sympy_str                  | 265 ms                                                   | 305 ms: 1.15x slower                                                     |
| genshi_text                | 28.6 ms                                                  | 33.1 ms: 1.16x slower                                                    |
| gc_traversal               | 5.92 ms                                                  | 6.95 ms: 1.17x slower                                                    |
| raytrace                   | 310 ms                                                   | 366 ms: 1.18x slower                                                     |
| django_template            | 39.4 ms                                                  | 47.0 ms: 1.19x slower                                                    |
| comprehensions             | 20.8 us                                                  | 24.9 us: 1.20x slower                                                    |
| nqueens                    | 105 ms                                                   | 129 ms: 1.23x slower                                                     |
| chaos                      | 70.7 ms                                                  | 87.0 ms: 1.23x slower                                                    |
| generators                 | 40.3 ms                                                  | 50.8 ms: 1.26x slower                                                    |
| pprint_safe_repr           | 962 ms                                                   | 1.23 sec: 1.28x slower                                                   |
| hexiom                     | 7.34 ms                                                  | 9.47 ms: 1.29x slower                                                    |
| pprint_pformat             | 1.99 sec                                                 | 2.57 sec: 1.29x slower                                                   |
| subparsers                 | 20.3 ms                                                  | 26.6 ms: 1.31x slower                                                    |
| many_optionals             | 626 us                                                   | 851 us: 1.36x slower                                                     |
| genshi_xml                 | 61.6 ms                                                  | 83.7 ms: 1.36x slower                                                    |
| bench_mp_pool              | 8.07 ms                                                  | 1.33 sec: 164.76x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.08x slower                                                             |

Benchmark hidden because not significant (31): json_loads, json, float, nbody, scimark_monte_carlo, coverage, xml_etree_generate, scimark_sparse_mat_mult, asyncio_websockets, pylint, xml_etree_process, pidigits, scimark_sor, regex_v8, unpickle_pure_python, connected_components, coroutines, bench_thread_pool, python_startup, regex_dna, richards, 2to3, go, spectral_norm, richards_super, thrift, json_dumps, sqlite_synth, sqlalchemy_declarative, regex_compile, sqlglot_optimize
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (9) of results/bm-20250111-3.14.0a3+-22a4421-JIT/bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.021x slower

# HPT report

- Reliability score: 90.36% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.04x