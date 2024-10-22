# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: fix_unsafe_refcounti
- machine: linux-aarch64
- commit hash: 8278d07
- commit date: 2024-10-12
- overall geometric mean: 1.05x slower
- HPT reliability: 99.87%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-arminc-aarch64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 293 ms: 1.04x faster                                                              |
| docutils       | 2.91 sec                                                 | 3.03 sec: 1.04x slower                                                            |
| html5lib       | 64.3 ms                                                  | 63.2 ms: 1.02x faster                                                             |
| tornado_http   | 131 ms                                                   | 126 ms: 1.04x faster                                                              |
| Geometric mean | (ref)                                                    | 1.01x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-arminc-aarch64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 550 ms: 1.18x faster                                                              |
| async_tree_none            | 493 ms                                                   | 422 ms: 1.17x faster                                                              |
| async_tree_memoization     | 626 ms                                                   | 551 ms: 1.14x faster                                                              |
| async_tree_none_tg         | 467 ms                                                   | 419 ms: 1.12x faster                                                              |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 709 ms: 1.08x faster                                                              |
| async_generators           | 496 ms                                                   | 475 ms: 1.04x faster                                                              |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 710 ms: 1.04x faster                                                              |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.20 sec: 1.01x slower                                                            |
| coroutines                 | 28.2 ms                                                  | 28.6 ms: 1.01x slower                                                             |
| async_tree_io_tg           | 1.09 sec                                                 | 1.13 sec: 1.04x slower                                                            |
| async_tree_io              | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                                            |
| Geometric mean             | (ref)                                                    | 1.05x faster                                                                      |

Benchmark hidden because not significant (2): asyncio_tcp, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-arminc-aarch64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 94.4 ms                                                  | 93.9 ms: 1.00x faster                                                             |
| Geometric mean | (ref)                                                    | 1.00x faster                                                                      |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-arminc-aarch64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 128 ms                                                   | 125 ms: 1.03x faster                                                              |
| regex_v8       | 31.5 ms                                                  | 31.0 ms: 1.02x faster                                                             |
| regex_effbot   | 4.87 ms                                                  | 4.97 ms: 1.02x slower                                                             |
| regex_dna      | 246 ms                                                   | 254 ms: 1.03x slower                                                              |
| Geometric mean | (ref)                                                    | 1.00x slower                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-arminc-aarch64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|--------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| unpickle           | 20.2 us                                                  | 19.4 us: 1.04x faster                                                             |
| unpickle_list      | 6.65 us                                                  | 6.51 us: 1.02x faster                                                             |
| pickle_list        | 5.34 us                                                  | 5.23 us: 1.02x faster                                                             |
| json_loads         | 31.4 us                                                  | 31.2 us: 1.01x faster                                                             |
| pickle_pure_python | 359 us                                                   | 358 us: 1.00x faster                                                              |
| tomli_loads        | 2.53 sec                                                 | 2.65 sec: 1.05x slower                                                            |
| json_dumps         | 13.4 ms                                                  | 14.7 ms: 1.10x slower                                                             |
| Geometric mean     | (ref)                                                    | 1.00x slower                                                                      |

Benchmark hidden because not significant (7): xml_etree_process, pickle_dict, xml_etree_generate, xml_etree_parse, xml_etree_iterparse, unpickle_pure_python, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-arminc-aarch64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                             |
| python_startup_no_site | 8.75 ms                                                  | 8.61 ms: 1.02x faster                                                             |
| Geometric mean         | (ref)                                                    | 1.02x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-arminc-aarch64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_text    | 27.7 ms                                                  | 27.2 ms: 1.02x faster                                                             |
| mako           | 13.3 ms                                                  | 13.6 ms: 1.02x slower                                                             |
| Geometric mean | (ref)                                                    | 1.00x slower                                                                      |

Benchmark hidden because not significant (2): genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-arminc-aarch64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| deepcopy                   | 451 us                                                   | 330 us: 1.37x faster                                                              |
| deepcopy_memo              | 51.0 us                                                  | 38.0 us: 1.34x faster                                                             |
| async_tree_memoization_tg  | 649 ms                                                   | 550 ms: 1.18x faster                                                              |
| go                         | 163 ms                                                   | 138 ms: 1.18x faster                                                              |
| deepcopy_reduce            | 4.07 us                                                  | 3.46 us: 1.18x faster                                                             |
| async_tree_none            | 493 ms                                                   | 422 ms: 1.17x faster                                                              |
| async_tree_memoization     | 626 ms                                                   | 551 ms: 1.14x faster                                                              |
| async_tree_none_tg         | 467 ms                                                   | 419 ms: 1.12x faster                                                              |
| generators                 | 37.8 ms                                                  | 34.6 ms: 1.09x faster                                                             |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 709 ms: 1.08x faster                                                              |
| pathlib                    | 22.4 ms                                                  | 21.4 ms: 1.05x faster                                                             |
| async_generators           | 496 ms                                                   | 475 ms: 1.04x faster                                                              |
| 2to3                       | 306 ms                                                   | 293 ms: 1.04x faster                                                              |
| tornado_http               | 131 ms                                                   | 126 ms: 1.04x faster                                                              |
| telco                      | 9.73 ms                                                  | 9.35 ms: 1.04x faster                                                             |
| unpickle                   | 20.2 us                                                  | 19.4 us: 1.04x faster                                                             |
| scimark_lu                 | 139 ms                                                   | 134 ms: 1.04x faster                                                              |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 710 ms: 1.04x faster                                                              |
| scimark_fft                | 447 ms                                                   | 432 ms: 1.04x faster                                                              |
| bpe_tokeniser              | 5.90 sec                                                 | 5.70 sec: 1.04x faster                                                            |
| logging_silent             | 135 ns                                                   | 131 ns: 1.03x faster                                                              |
| regex_compile              | 128 ms                                                   | 125 ms: 1.03x faster                                                              |
| meteor_contest             | 113 ms                                                   | 110 ms: 1.03x faster                                                              |
| unpack_sequence            | 57.2 ns                                                  | 55.8 ns: 1.02x faster                                                             |
| unpickle_list              | 6.65 us                                                  | 6.51 us: 1.02x faster                                                             |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 6.44 ms: 1.02x faster                                                             |
| python_startup             | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                             |
| thrift                     | 946 us                                                   | 926 us: 1.02x faster                                                              |
| pprint_safe_repr           | 926 ms                                                   | 908 ms: 1.02x faster                                                              |
| pickle_list                | 5.34 us                                                  | 5.23 us: 1.02x faster                                                             |
| scimark_monte_carlo        | 83.8 ms                                                  | 82.3 ms: 1.02x faster                                                             |
| html5lib                   | 64.3 ms                                                  | 63.2 ms: 1.02x faster                                                             |
| richards                   | 53.5 ms                                                  | 52.6 ms: 1.02x faster                                                             |
| pycparser                  | 1.26 sec                                                 | 1.24 sec: 1.02x faster                                                            |
| sympy_sum                  | 143 ms                                                   | 141 ms: 1.02x faster                                                              |
| genshi_text                | 27.7 ms                                                  | 27.2 ms: 1.02x faster                                                             |
| regex_v8                   | 31.5 ms                                                  | 31.0 ms: 1.02x faster                                                             |
| python_startup_no_site     | 8.75 ms                                                  | 8.61 ms: 1.02x faster                                                             |
| richards_super             | 60.3 ms                                                  | 59.4 ms: 1.02x faster                                                             |
| crypto_pyaes               | 82.7 ms                                                  | 81.4 ms: 1.02x faster                                                             |
| hexiom                     | 7.13 ms                                                  | 7.03 ms: 1.01x faster                                                             |
| spectral_norm              | 141 ms                                                   | 139 ms: 1.01x faster                                                              |
| pprint_pformat             | 1.90 sec                                                 | 1.88 sec: 1.01x faster                                                            |
| mdp                        | 3.36 sec                                                 | 3.33 sec: 1.01x faster                                                            |
| json_loads                 | 31.4 us                                                  | 31.2 us: 1.01x faster                                                             |
| float                      | 94.4 ms                                                  | 93.9 ms: 1.00x faster                                                             |
| pickle_pure_python         | 359 us                                                   | 358 us: 1.00x faster                                                              |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.20 sec: 1.01x slower                                                            |
| coroutines                 | 28.2 ms                                                  | 28.6 ms: 1.01x slower                                                             |
| chaos                      | 68.8 ms                                                  | 69.6 ms: 1.01x slower                                                             |
| json                       | 5.61 ms                                                  | 5.69 ms: 1.01x slower                                                             |
| comprehensions             | 20.4 us                                                  | 20.7 us: 1.02x slower                                                             |
| sqlglot_parse              | 1.38 ms                                                  | 1.41 ms: 1.02x slower                                                             |
| deltablue                  | 3.85 ms                                                  | 3.93 ms: 1.02x slower                                                             |
| logging_simple             | 7.04 us                                                  | 7.19 us: 1.02x slower                                                             |
| regex_effbot               | 4.87 ms                                                  | 4.97 ms: 1.02x slower                                                             |
| mako                       | 13.3 ms                                                  | 13.6 ms: 1.02x slower                                                             |
| fannkuch                   | 452 ms                                                   | 464 ms: 1.03x slower                                                              |
| sqlite_synth               | 3.84 us                                                  | 3.95 us: 1.03x slower                                                             |
| regex_dna                  | 246 ms                                                   | 254 ms: 1.03x slower                                                              |
| async_tree_io_tg           | 1.09 sec                                                 | 1.13 sec: 1.04x slower                                                            |
| docutils                   | 2.91 sec                                                 | 3.03 sec: 1.04x slower                                                            |
| pyflate                    | 556 ms                                                   | 580 ms: 1.04x slower                                                              |
| async_tree_io              | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                                            |
| raytrace                   | 298 ms                                                   | 312 ms: 1.05x slower                                                              |
| tomli_loads                | 2.53 sec                                                 | 2.65 sec: 1.05x slower                                                            |
| json_dumps                 | 13.4 ms                                                  | 14.7 ms: 1.10x slower                                                             |
| create_gc_cycles           | 2.12 ms                                                  | 2.39 ms: 1.12x slower                                                             |
| gc_traversal               | 4.53 ms                                                  | 5.22 ms: 1.15x slower                                                             |
| bench_mp_pool              | 7.30 ms                                                  | 5.94 sec: 813.47x slower                                                          |
| Geometric mean             | (ref)                                                    | 1.05x slower                                                                      |

Benchmark hidden because not significant (26): logging_format, xml_etree_process, pickle_dict, asyncio_tcp, sqlglot_normalize, xml_etree_generate, coverage, scimark_sor, nbody, sympy_str, xml_etree_parse, xml_etree_iterparse, unpickle_pure_python, sqlglot_transpile, sqlglot_optimize, sympy_integrate, pidigits, bench_thread_pool, genshi_xml, asyncio_websockets, sympy_expand, pickle, nqueens, django_template, typing_runtime_protocols, pylint
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241012-3.14.0a0-8278d07/bm-20241012-arminc-aarch64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07.json: dulwich_log

# HPT report

- Reliability score: 99.87% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x