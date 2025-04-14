# Results vs. 3.12.0

- fork: faster-cpython
- ref: c_recursion_limit
- machine: linux-aarch64
- commit hash: 21366c3
- commit date: 2025-02-17
- overall geometric mean: 1.032x faster
- HPT reliability: 99.62%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250217-arminc-aarch64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| docutils       | 2.98 sec                                                              | 3.03 sec: 1.01x slower                                                          |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250217-arminc-aarch64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 403 ms: 1.55x faster                                                            |
| async_tree_memoization     | 777 ms                                                                | 504 ms: 1.54x faster                                                            |
| async_tree_io              | 1.41 sec                                                              | 936 ms: 1.51x faster                                                            |
| async_tree_memoization_tg  | 740 ms                                                                | 499 ms: 1.48x faster                                                            |
| async_tree_io_tg           | 1.40 sec                                                              | 948 ms: 1.48x faster                                                            |
| async_tree_none_tg         | 577 ms                                                                | 403 ms: 1.43x faster                                                            |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 690 ms: 1.32x faster                                                            |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 682 ms: 1.30x faster                                                            |
| Geometric mean             | (ref)                                                                 | 1.45x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250217-arminc-aarch64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 86.2 ms: 1.07x faster                                                           |
| pidigits       | 233 ms                                                                | 240 ms: 1.03x slower                                                            |
| nbody          | 105 ms                                                                | 120 ms: 1.15x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250217-arminc-aarch64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.09 ms: 1.14x faster                                                           |
| regex_compile  | 137 ms                                                                | 125 ms: 1.09x faster                                                            |
| regex_dna      | 254 ms                                                                | 244 ms: 1.04x faster                                                            |
| regex_v8       | 28.3 ms                                                               | 32.0 ms: 1.13x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250217-arminc-aarch64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle_pure_python | 260 us                                                                | 268 us: 1.03x slower                                                            |
| xml_etree_process    | 79.0 ms                                                               | 83.0 ms: 1.05x slower                                                           |
| pickle_pure_python   | 365 us                                                                | 393 us: 1.08x slower                                                            |
| json_loads           | 30.7 us                                                               | 34.6 us: 1.13x slower                                                           |
| json_dumps           | 12.3 ms                                                               | 15.0 ms: 1.22x slower                                                           |
| Geometric mean       | (ref)                                                                 | 1.06x slower                                                                    |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_iterparse, tomli_loads, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250217-arminc-aarch64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.12 ms: 1.09x slower                                                           |
| python_startup         | 11.4 ms                                                               | 16.6 ms: 1.46x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.26x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250217-arminc-aarch64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                               | 26.9 ms: 1.02x faster                                                           |
| mako           | 12.9 ms                                                               | 13.8 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                                    |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250217-arminc-aarch64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 403 ms: 1.55x faster                                                            |
| async_tree_memoization     | 777 ms                                                                | 504 ms: 1.54x faster                                                            |
| async_tree_io              | 1.41 sec                                                              | 936 ms: 1.51x faster                                                            |
| async_tree_memoization_tg  | 740 ms                                                                | 499 ms: 1.48x faster                                                            |
| async_tree_io_tg           | 1.40 sec                                                              | 948 ms: 1.48x faster                                                            |
| async_tree_none_tg         | 577 ms                                                                | 403 ms: 1.43x faster                                                            |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 690 ms: 1.32x faster                                                            |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 682 ms: 1.30x faster                                                            |
| deepcopy                   | 446 us                                                                | 346 us: 1.29x faster                                                            |
| deepcopy_memo              | 49.6 us                                                               | 40.5 us: 1.22x faster                                                           |
| generators                 | 43.5 ms                                                               | 36.3 ms: 1.20x faster                                                           |
| comprehensions             | 25.4 us                                                               | 21.6 us: 1.18x faster                                                           |
| regex_effbot               | 4.64 ms                                                               | 4.09 ms: 1.14x faster                                                           |
| deepcopy_reduce            | 4.10 us                                                               | 3.66 us: 1.12x faster                                                           |
| regex_compile              | 137 ms                                                                | 125 ms: 1.09x faster                                                            |
| pathlib                    | 24.5 ms                                                               | 22.5 ms: 1.09x faster                                                           |
| spectral_norm              | 131 ms                                                                | 121 ms: 1.08x faster                                                            |
| pylint                     | 355 ms                                                                | 329 ms: 1.08x faster                                                            |
| raytrace                   | 353 ms                                                                | 328 ms: 1.08x faster                                                            |
| sqlalchemy_imperative      | 16.7 ms                                                               | 15.5 ms: 1.08x faster                                                           |
| go                         | 157 ms                                                                | 146 ms: 1.08x faster                                                            |
| async_generators           | 491 ms                                                                | 458 ms: 1.07x faster                                                            |
| float                      | 92.1 ms                                                               | 86.2 ms: 1.07x faster                                                           |
| logging_format             | 8.34 us                                                               | 7.83 us: 1.07x faster                                                           |
| logging_simple             | 7.63 us                                                               | 7.22 us: 1.06x faster                                                           |
| sympy_sum                  | 154 ms                                                                | 147 ms: 1.05x faster                                                            |
| sqlalchemy_declarative     | 157 ms                                                                | 150 ms: 1.05x faster                                                            |
| chaos                      | 71.4 ms                                                               | 68.3 ms: 1.05x faster                                                           |
| deltablue                  | 4.12 ms                                                               | 3.96 ms: 1.04x faster                                                           |
| regex_dna                  | 254 ms                                                                | 244 ms: 1.04x faster                                                            |
| genshi_text                | 27.4 ms                                                               | 26.9 ms: 1.02x faster                                                           |
| docutils                   | 2.98 sec                                                              | 3.03 sec: 1.01x slower                                                          |
| mdp                        | 3.41 sec                                                              | 3.47 sec: 1.02x slower                                                          |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.30 ms: 1.02x slower                                                           |
| meteor_contest             | 112 ms                                                                | 115 ms: 1.02x slower                                                            |
| asyncio_websockets         | 658 ms                                                                | 675 ms: 1.03x slower                                                            |
| pidigits                   | 233 ms                                                                | 240 ms: 1.03x slower                                                            |
| unpickle_pure_python       | 260 us                                                                | 268 us: 1.03x slower                                                            |
| pycparser                  | 1.26 sec                                                              | 1.30 sec: 1.04x slower                                                          |
| sqlglot_normalize          | 126 ms                                                                | 131 ms: 1.04x slower                                                            |
| xml_etree_process          | 79.0 ms                                                               | 83.0 ms: 1.05x slower                                                           |
| scimark_sor                | 150 ms                                                                | 157 ms: 1.05x slower                                                            |
| thrift                     | 937 us                                                                | 986 us: 1.05x slower                                                            |
| sympy_expand               | 454 ms                                                                | 478 ms: 1.05x slower                                                            |
| pprint_safe_repr           | 916 ms                                                                | 974 ms: 1.06x slower                                                            |
| pprint_pformat             | 1.88 sec                                                              | 2.01 sec: 1.07x slower                                                          |
| mako                       | 12.9 ms                                                               | 13.8 ms: 1.07x slower                                                           |
| pickle_pure_python         | 365 us                                                                | 393 us: 1.08x slower                                                            |
| json                       | 5.54 ms                                                               | 6.02 ms: 1.09x slower                                                           |
| python_startup_no_site     | 8.37 ms                                                               | 9.12 ms: 1.09x slower                                                           |
| sqlite_synth               | 3.77 us                                                               | 4.11 us: 1.09x slower                                                           |
| hexiom                     | 6.98 ms                                                               | 7.62 ms: 1.09x slower                                                           |
| fannkuch                   | 443 ms                                                                | 496 ms: 1.12x slower                                                            |
| logging_silent             | 127 ns                                                                | 142 ns: 1.12x slower                                                            |
| json_loads                 | 30.7 us                                                               | 34.6 us: 1.13x slower                                                           |
| typing_runtime_protocols   | 181 us                                                                | 204 us: 1.13x slower                                                            |
| regex_v8                   | 28.3 ms                                                               | 32.0 ms: 1.13x slower                                                           |
| nbody                      | 105 ms                                                                | 120 ms: 1.15x slower                                                            |
| coverage                   | 87.3 ms                                                               | 104 ms: 1.19x slower                                                            |
| telco                      | 8.51 ms                                                               | 10.1 ms: 1.19x slower                                                           |
| json_dumps                 | 12.3 ms                                                               | 15.0 ms: 1.22x slower                                                           |
| python_startup             | 11.4 ms                                                               | 16.6 ms: 1.46x slower                                                           |
| gc_traversal               | 4.40 ms                                                               | 6.89 ms: 1.57x slower                                                           |
| create_gc_cycles           | 1.92 ms                                                               | 3.57 ms: 1.86x slower                                                           |
| bench_mp_pool              | 7.05 ms                                                               | 7.19 sec: 1018.97x slower                                                       |
| Geometric mean             | (ref)                                                                 | 1.07x slower                                                                    |

Benchmark hidden because not significant (24): xml_etree_parse, dulwich_log, html5lib, sqlglot_parse, bench_thread_pool, scimark_lu, xml_etree_iterparse, tomli_loads, coroutines, 2to3, sympy_str, sqlglot_transpile, scimark_monte_carlo, pyflate, sympy_integrate, scimark_fft, django_template, crypto_pyaes, richards, richards_super, sqlglot_optimize, genshi_xml, nqueens, xml_etree_generate
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20250217-3.14.0a5+-21366c3/bm-20250217-arminc-aarch64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.032x faster

# HPT report

- Reliability score: 99.62% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x