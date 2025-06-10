# Results vs. 3.12.0

- fork: python
- ref: main
- machine: linux-aarch64
- commit hash: 0f866cb
- commit date: 2025-06-10
- overall geometric mean: 1.046x slower
- HPT reliability: 97.10%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250610-arminc-aarch64-python-main-3.15.0a0-0f866cb |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 312 ms: 1.01x slower                                    |
| docutils       | 2.98 sec                                                              | 3.09 sec: 1.03x slower                                  |
| html5lib       | 65.1 ms                                                               | 63.2 ms: 1.03x faster                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250610-arminc-aarch64-python-main-3.15.0a0-0f866cb |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 478 ms: 1.62x faster                                    |
| async_tree_io              | 1.41 sec                                                              | 897 ms: 1.57x faster                                    |
| async_tree_none            | 624 ms                                                                | 400 ms: 1.56x faster                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 476 ms: 1.56x faster                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 925 ms: 1.52x faster                                    |
| async_tree_none_tg         | 577 ms                                                                | 385 ms: 1.50x faster                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 666 ms: 1.37x faster                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 669 ms: 1.32x faster                                    |
| Geometric mean             | (ref)                                                                 | 1.50x faster                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250610-arminc-aarch64-python-main-3.15.0a0-0f866cb |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------:|
| float          | 92.1 ms                                                               | 82.8 ms: 1.11x faster                                   |
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                    |
| nbody          | 105 ms                                                                | 119 ms: 1.14x slower                                    |
| Geometric mean | (ref)                                                                 | 1.01x slower                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250610-arminc-aarch64-python-main-3.15.0a0-0f866cb |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.02 ms: 1.15x faster                                   |
| regex_dna      | 254 ms                                                                | 223 ms: 1.14x faster                                    |
| regex_compile  | 137 ms                                                                | 122 ms: 1.13x faster                                    |
| regex_v8       | 28.3 ms                                                               | 27.1 ms: 1.04x faster                                   |
| Geometric mean | (ref)                                                                 | 1.12x faster                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250610-arminc-aarch64-python-main-3.15.0a0-0f866cb |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------:|
| tomli_loads          | 2.59 sec                                                              | 2.37 sec: 1.10x faster                                  |
| xml_etree_parse      | 195 ms                                                                | 179 ms: 1.09x faster                                    |
| xml_etree_iterparse  | 150 ms                                                                | 143 ms: 1.05x faster                                    |
| unpickle_pure_python | 260 us                                                                | 248 us: 1.05x faster                                    |
| pickle_pure_python   | 365 us                                                                | 388 us: 1.06x slower                                    |
| json_loads           | 30.7 us                                                               | 32.7 us: 1.07x slower                                   |
| json_dumps           | 12.3 ms                                                               | 13.9 ms: 1.13x slower                                   |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                            |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250610-arminc-aarch64-python-main-3.15.0a0-0f866cb |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.62 ms: 1.03x slower                                   |
| python_startup         | 11.4 ms                                                               | 15.1 ms: 1.33x slower                                   |
| Geometric mean         | (ref)                                                                 | 1.17x slower                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250610-arminc-aarch64-python-main-3.15.0a0-0f866cb |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------:|
| genshi_text     | 27.4 ms                                                               | 27.7 ms: 1.01x slower                                   |
| django_template | 40.7 ms                                                               | 41.7 ms: 1.03x slower                                   |
| genshi_xml      | 60.6 ms                                                               | 63.4 ms: 1.05x slower                                   |
| mako            | 12.9 ms                                                               | 13.6 ms: 1.05x slower                                   |
| Geometric mean  | (ref)                                                                 | 1.03x slower                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250610-arminc-aarch64-python-main-3.15.0a0-0f866cb |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.68 sec: 2.03x faster                                  |
| async_tree_memoization     | 777 ms                                                                | 478 ms: 1.62x faster                                    |
| async_tree_io              | 1.41 sec                                                              | 897 ms: 1.57x faster                                    |
| async_tree_none            | 624 ms                                                                | 400 ms: 1.56x faster                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 476 ms: 1.56x faster                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 925 ms: 1.52x faster                                    |
| async_tree_none_tg         | 577 ms                                                                | 385 ms: 1.50x faster                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 666 ms: 1.37x faster                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 669 ms: 1.32x faster                                    |
| deepcopy_memo              | 49.6 us                                                               | 38.2 us: 1.30x faster                                   |
| deepcopy                   | 446 us                                                                | 345 us: 1.29x faster                                    |
| generators                 | 43.5 ms                                                               | 35.9 ms: 1.21x faster                                   |
| regex_effbot               | 4.64 ms                                                               | 4.02 ms: 1.15x faster                                   |
| richards_super             | 58.5 ms                                                               | 51.1 ms: 1.14x faster                                   |
| richards                   | 50.9 ms                                                               | 44.7 ms: 1.14x faster                                   |
| regex_dna                  | 254 ms                                                                | 223 ms: 1.14x faster                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.63 us: 1.13x faster                                   |
| regex_compile              | 137 ms                                                                | 122 ms: 1.13x faster                                    |
| comprehensions             | 25.4 us                                                               | 22.7 us: 1.12x faster                                   |
| float                      | 92.1 ms                                                               | 82.8 ms: 1.11x faster                                   |
| dulwich_log                | 62.0 ms                                                               | 55.8 ms: 1.11x faster                                   |
| pylint                     | 355 ms                                                                | 322 ms: 1.10x faster                                    |
| tomli_loads                | 2.59 sec                                                              | 2.37 sec: 1.10x faster                                  |
| xml_etree_parse            | 195 ms                                                                | 179 ms: 1.09x faster                                    |
| xml_etree_iterparse        | 150 ms                                                                | 143 ms: 1.05x faster                                    |
| raytrace                   | 353 ms                                                                | 336 ms: 1.05x faster                                    |
| unpickle_pure_python       | 260 us                                                                | 248 us: 1.05x faster                                    |
| pathlib                    | 24.5 ms                                                               | 23.5 ms: 1.04x faster                                   |
| regex_v8                   | 28.3 ms                                                               | 27.1 ms: 1.04x faster                                   |
| deltablue                  | 4.12 ms                                                               | 3.97 ms: 1.04x faster                                   |
| async_generators           | 491 ms                                                                | 475 ms: 1.03x faster                                    |
| sympy_integrate            | 21.6 ms                                                               | 21.0 ms: 1.03x faster                                   |
| html5lib                   | 65.1 ms                                                               | 63.2 ms: 1.03x faster                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 82.9 ms: 1.03x faster                                   |
| pyflate                    | 559 ms                                                                | 549 ms: 1.02x faster                                    |
| sqlite_synth               | 3.77 us                                                               | 3.71 us: 1.02x faster                                   |
| logging_simple             | 7.63 us                                                               | 7.57 us: 1.01x faster                                   |
| genshi_text                | 27.4 ms                                                               | 27.7 ms: 1.01x slower                                   |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                    |
| go                         | 157 ms                                                                | 159 ms: 1.01x slower                                    |
| 2to3                       | 308 ms                                                                | 312 ms: 1.01x slower                                    |
| asyncio_websockets         | 658 ms                                                                | 666 ms: 1.01x slower                                    |
| coroutines                 | 29.0 ms                                                               | 29.4 ms: 1.01x slower                                   |
| nqueens                    | 99.2 ms                                                               | 101 ms: 1.02x slower                                    |
| json                       | 5.54 ms                                                               | 5.67 ms: 1.02x slower                                   |
| django_template            | 40.7 ms                                                               | 41.7 ms: 1.03x slower                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.62 ms: 1.03x slower                                   |
| docutils                   | 2.98 sec                                                              | 3.09 sec: 1.03x slower                                  |
| genshi_xml                 | 60.6 ms                                                               | 63.4 ms: 1.05x slower                                   |
| mako                       | 12.9 ms                                                               | 13.6 ms: 1.05x slower                                   |
| scimark_lu                 | 146 ms                                                                | 154 ms: 1.06x slower                                    |
| pickle_pure_python         | 365 us                                                                | 388 us: 1.06x slower                                    |
| json_loads                 | 30.7 us                                                               | 32.7 us: 1.07x slower                                   |
| crypto_pyaes               | 86.6 ms                                                               | 92.8 ms: 1.07x slower                                   |
| hexiom                     | 6.98 ms                                                               | 7.49 ms: 1.07x slower                                   |
| sympy_expand               | 454 ms                                                                | 490 ms: 1.08x slower                                    |
| fannkuch                   | 443 ms                                                                | 483 ms: 1.09x slower                                    |
| telco                      | 8.51 ms                                                               | 9.45 ms: 1.11x slower                                   |
| pycparser                  | 1.26 sec                                                              | 1.40 sec: 1.11x slower                                  |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.93 ms: 1.12x slower                                   |
| json_dumps                 | 12.3 ms                                                               | 13.9 ms: 1.13x slower                                   |
| nbody                      | 105 ms                                                                | 119 ms: 1.14x slower                                    |
| typing_runtime_protocols   | 181 us                                                                | 205 us: 1.14x slower                                    |
| python_startup             | 11.4 ms                                                               | 15.1 ms: 1.33x slower                                   |
| pprint_safe_repr           | 916 ms                                                                | 1.25 sec: 1.36x slower                                  |
| pprint_pformat             | 1.88 sec                                                              | 2.58 sec: 1.37x slower                                  |
| gc_traversal               | 4.40 ms                                                               | 7.06 ms: 1.61x slower                                   |
| create_gc_cycles           | 1.92 ms                                                               | 3.76 ms: 1.96x slower                                   |
| logging_silent             | 127 ns                                                                | 606 ns: 4.78x slower                                    |
| coverage                   | 87.3 ms                                                               | 554 ms: 6.34x slower                                    |
| thrift                     | 937 us                                                                | 191 ms: 203.38x slower                                  |
| Geometric mean             | (ref)                                                                 | 1.07x slower                                            |

Benchmark hidden because not significant (10): scimark_sor, xml_etree_generate, chaos, sympy_sum, logging_format, xml_etree_process, scimark_fft, sympy_str, spectral_norm, meteor_contest
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250610-3.15.0a0-0f866cb-JIT/bm-20250610-arminc-aarch64-python-main-3.15.0a0-0f866cb.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.046x slower

# HPT report

- Reliability score: 97.10% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.11x