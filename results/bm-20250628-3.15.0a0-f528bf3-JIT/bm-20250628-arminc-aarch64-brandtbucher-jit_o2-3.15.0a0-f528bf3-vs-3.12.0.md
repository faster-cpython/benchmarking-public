# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_o2
- machine: linux-aarch64
- commit hash: f528bf3
- commit date: 2025-06-28
- overall geometric mean: 1.049x faster
- HPT reliability: 98.96%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250628-arminc-aarch64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 312 ms: 1.01x slower                                            |
| docutils       | 2.98 sec                                                              | 3.11 sec: 1.04x slower                                          |
| html5lib       | 65.1 ms                                                               | 62.9 ms: 1.03x faster                                           |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250628-arminc-aarch64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 470 ms: 1.65x faster                                            |
| async_tree_io              | 1.41 sec                                                              | 898 ms: 1.57x faster                                            |
| async_tree_none            | 624 ms                                                                | 397 ms: 1.57x faster                                            |
| async_tree_memoization_tg  | 740 ms                                                                | 478 ms: 1.55x faster                                            |
| async_tree_io_tg           | 1.40 sec                                                              | 924 ms: 1.52x faster                                            |
| async_tree_none_tg         | 577 ms                                                                | 385 ms: 1.50x faster                                            |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 664 ms: 1.37x faster                                            |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 666 ms: 1.33x faster                                            |
| Geometric mean             | (ref)                                                                 | 1.50x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250628-arminc-aarch64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 83.4 ms: 1.10x faster                                           |
| pidigits       | 233 ms                                                                | 238 ms: 1.02x slower                                            |
| nbody          | 105 ms                                                                | 128 ms: 1.23x slower                                            |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250628-arminc-aarch64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.94 ms: 1.18x faster                                           |
| regex_dna      | 254 ms                                                                | 226 ms: 1.13x faster                                            |
| regex_compile  | 137 ms                                                                | 125 ms: 1.10x faster                                            |
| regex_v8       | 28.3 ms                                                               | 26.6 ms: 1.06x faster                                           |
| Geometric mean | (ref)                                                                 | 1.12x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250628-arminc-aarch64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|---------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| tomli_loads         | 2.59 sec                                                              | 2.33 sec: 1.11x faster                                          |
| xml_etree_parse     | 195 ms                                                                | 178 ms: 1.10x faster                                            |
| xml_etree_iterparse | 150 ms                                                                | 144 ms: 1.05x faster                                            |
| xml_etree_process   | 79.0 ms                                                               | 77.2 ms: 1.02x faster                                           |
| pickle_pure_python  | 365 us                                                                | 390 us: 1.07x slower                                            |
| json_loads          | 30.7 us                                                               | 32.8 us: 1.07x slower                                           |
| json_dumps          | 12.3 ms                                                               | 13.6 ms: 1.11x slower                                           |
| Geometric mean      | (ref)                                                                 | 1.01x faster                                                    |

Benchmark hidden because not significant (2): xml_etree_generate, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250628-arminc-aarch64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.63 ms: 1.03x slower                                           |
| python_startup         | 11.4 ms                                                               | 15.1 ms: 1.33x slower                                           |
| Geometric mean         | (ref)                                                                 | 1.17x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250628-arminc-aarch64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                               | 27.7 ms: 1.01x slower                                           |
| mako           | 12.9 ms                                                               | 13.2 ms: 1.02x slower                                           |
| genshi_xml     | 60.6 ms                                                               | 64.0 ms: 1.06x slower                                           |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                    |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250628-arminc-aarch64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.65 sec: 2.06x faster                                          |
| async_tree_memoization     | 777 ms                                                                | 470 ms: 1.65x faster                                            |
| async_tree_io              | 1.41 sec                                                              | 898 ms: 1.57x faster                                            |
| async_tree_none            | 624 ms                                                                | 397 ms: 1.57x faster                                            |
| async_tree_memoization_tg  | 740 ms                                                                | 478 ms: 1.55x faster                                            |
| async_tree_io_tg           | 1.40 sec                                                              | 924 ms: 1.52x faster                                            |
| async_tree_none_tg         | 577 ms                                                                | 385 ms: 1.50x faster                                            |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 664 ms: 1.37x faster                                            |
| deepcopy_memo              | 49.6 us                                                               | 37.4 us: 1.33x faster                                           |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 666 ms: 1.33x faster                                            |
| deepcopy                   | 446 us                                                                | 339 us: 1.31x faster                                            |
| regex_effbot               | 4.64 ms                                                               | 3.94 ms: 1.18x faster                                           |
| generators                 | 43.5 ms                                                               | 37.1 ms: 1.17x faster                                           |
| comprehensions             | 25.4 us                                                               | 21.8 us: 1.16x faster                                           |
| regex_dna                  | 254 ms                                                                | 226 ms: 1.13x faster                                            |
| tomli_loads                | 2.59 sec                                                              | 2.33 sec: 1.11x faster                                          |
| deepcopy_reduce            | 4.10 us                                                               | 3.71 us: 1.11x faster                                           |
| float                      | 92.1 ms                                                               | 83.4 ms: 1.10x faster                                           |
| xml_etree_parse            | 195 ms                                                                | 178 ms: 1.10x faster                                            |
| regex_compile              | 137 ms                                                                | 125 ms: 1.10x faster                                            |
| richards                   | 50.9 ms                                                               | 46.5 ms: 1.10x faster                                           |
| pylint                     | 355 ms                                                                | 323 ms: 1.10x faster                                            |
| dulwich_log                | 62.0 ms                                                               | 56.7 ms: 1.09x faster                                           |
| richards_super             | 58.5 ms                                                               | 53.5 ms: 1.09x faster                                           |
| spectral_norm              | 131 ms                                                                | 121 ms: 1.08x faster                                            |
| logging_simple             | 7.63 us                                                               | 7.12 us: 1.07x faster                                           |
| deltablue                  | 4.12 ms                                                               | 3.86 ms: 1.07x faster                                           |
| regex_v8                   | 28.3 ms                                                               | 26.6 ms: 1.06x faster                                           |
| logging_format             | 8.34 us                                                               | 7.86 us: 1.06x faster                                           |
| pathlib                    | 24.5 ms                                                               | 23.2 ms: 1.06x faster                                           |
| raytrace                   | 353 ms                                                                | 335 ms: 1.05x faster                                            |
| pyflate                    | 559 ms                                                                | 532 ms: 1.05x faster                                            |
| xml_etree_iterparse        | 150 ms                                                                | 144 ms: 1.05x faster                                            |
| scimark_monte_carlo        | 85.1 ms                                                               | 81.7 ms: 1.04x faster                                           |
| sympy_sum                  | 154 ms                                                                | 149 ms: 1.04x faster                                            |
| html5lib                   | 65.1 ms                                                               | 62.9 ms: 1.03x faster                                           |
| chaos                      | 71.4 ms                                                               | 69.1 ms: 1.03x faster                                           |
| xml_etree_process          | 79.0 ms                                                               | 77.2 ms: 1.02x faster                                           |
| scimark_fft                | 418 ms                                                                | 409 ms: 1.02x faster                                            |
| meteor_contest             | 112 ms                                                                | 113 ms: 1.01x slower                                            |
| genshi_text                | 27.4 ms                                                               | 27.7 ms: 1.01x slower                                           |
| 2to3                       | 308 ms                                                                | 312 ms: 1.01x slower                                            |
| sqlite_synth               | 3.77 us                                                               | 3.83 us: 1.02x slower                                           |
| logging_silent             | 127 ns                                                                | 129 ns: 1.02x slower                                            |
| json                       | 5.54 ms                                                               | 5.63 ms: 1.02x slower                                           |
| asyncio_websockets         | 658 ms                                                                | 670 ms: 1.02x slower                                            |
| mako                       | 12.9 ms                                                               | 13.2 ms: 1.02x slower                                           |
| pidigits                   | 233 ms                                                                | 238 ms: 1.02x slower                                            |
| python_startup_no_site     | 8.37 ms                                                               | 8.63 ms: 1.03x slower                                           |
| docutils                   | 2.98 sec                                                              | 3.11 sec: 1.04x slower                                          |
| genshi_xml                 | 60.6 ms                                                               | 64.0 ms: 1.06x slower                                           |
| fannkuch                   | 443 ms                                                                | 473 ms: 1.07x slower                                            |
| pickle_pure_python         | 365 us                                                                | 390 us: 1.07x slower                                            |
| json_loads                 | 30.7 us                                                               | 32.8 us: 1.07x slower                                           |
| hexiom                     | 6.98 ms                                                               | 7.56 ms: 1.08x slower                                           |
| scimark_lu                 | 146 ms                                                                | 158 ms: 1.08x slower                                            |
| sympy_expand               | 454 ms                                                                | 498 ms: 1.10x slower                                            |
| crypto_pyaes               | 86.6 ms                                                               | 95.2 ms: 1.10x slower                                           |
| pycparser                  | 1.26 sec                                                              | 1.39 sec: 1.11x slower                                          |
| json_dumps                 | 12.3 ms                                                               | 13.6 ms: 1.11x slower                                           |
| telco                      | 8.51 ms                                                               | 9.50 ms: 1.12x slower                                           |
| typing_runtime_protocols   | 181 us                                                                | 206 us: 1.14x slower                                            |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.15 ms: 1.15x slower                                           |
| coverage                   | 87.3 ms                                                               | 102 ms: 1.16x slower                                            |
| pprint_pformat             | 1.88 sec                                                              | 2.30 sec: 1.22x slower                                          |
| nbody                      | 105 ms                                                                | 128 ms: 1.23x slower                                            |
| pprint_safe_repr           | 916 ms                                                                | 1.13 sec: 1.24x slower                                          |
| python_startup             | 11.4 ms                                                               | 15.1 ms: 1.33x slower                                           |
| gc_traversal               | 4.40 ms                                                               | 6.80 ms: 1.55x slower                                           |
| create_gc_cycles           | 1.92 ms                                                               | 3.65 ms: 1.90x slower                                           |
| Geometric mean             | (ref)                                                                 | 1.04x faster                                                    |

Benchmark hidden because not significant (11): scimark_sor, xml_etree_generate, sympy_integrate, unpickle_pure_python, async_generators, django_template, sympy_str, go, thrift, nqueens, coroutines
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250628-3.15.0a0-f528bf3-JIT/bm-20250628-arminc-aarch64-brandtbucher-jit_o2-3.15.0a0-f528bf3.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.049x faster

# HPT report

- Reliability score: 98.96% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.12x