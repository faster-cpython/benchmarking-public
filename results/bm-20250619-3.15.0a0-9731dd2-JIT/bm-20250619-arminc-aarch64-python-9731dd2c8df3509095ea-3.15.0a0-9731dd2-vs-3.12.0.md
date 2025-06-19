# Results vs. 3.12.0

- fork: python
- ref: 9731dd2c8df3509095ea
- machine: linux-aarch64
- commit hash: 9731dd2
- commit date: 2025-06-19
- overall geometric mean: 1.042x faster
- HPT reliability: 99.17%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250619-arminc-aarch64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 312 ms: 1.01x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.09 sec: 1.04x slower                                                  |
| html5lib       | 65.1 ms                                                               | 63.1 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250619-arminc-aarch64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 472 ms: 1.65x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 899 ms: 1.57x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 474 ms: 1.56x faster                                                    |
| async_tree_none            | 624 ms                                                                | 399 ms: 1.56x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 918 ms: 1.53x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 383 ms: 1.51x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 665 ms: 1.37x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 660 ms: 1.34x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.51x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250619-arminc-aarch64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 83.4 ms: 1.10x faster                                                   |
| pidigits       | 233 ms                                                                | 238 ms: 1.02x slower                                                    |
| nbody          | 105 ms                                                                | 125 ms: 1.19x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250619-arminc-aarch64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.93 ms: 1.18x faster                                                   |
| regex_dna      | 254 ms                                                                | 225 ms: 1.13x faster                                                    |
| regex_compile  | 137 ms                                                                | 122 ms: 1.12x faster                                                    |
| regex_v8       | 28.3 ms                                                               | 27.4 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.12x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250619-arminc-aarch64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 |
|---------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads         | 2.59 sec                                                              | 2.32 sec: 1.12x faster                                                  |
| xml_etree_parse     | 195 ms                                                                | 178 ms: 1.09x faster                                                    |
| xml_etree_iterparse | 150 ms                                                                | 144 ms: 1.05x faster                                                    |
| json_loads          | 30.7 us                                                               | 32.3 us: 1.05x slower                                                   |
| pickle_pure_python  | 365 us                                                                | 405 us: 1.11x slower                                                    |
| json_dumps          | 12.3 ms                                                               | 13.8 ms: 1.12x slower                                                   |
| Geometric mean      | (ref)                                                                 | 1.00x faster                                                            |

Benchmark hidden because not significant (3): unpickle_pure_python, xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250619-arminc-aarch64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.69 ms: 1.04x slower                                                   |
| python_startup         | 11.4 ms                                                               | 15.2 ms: 1.33x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.18x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250619-arminc-aarch64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 40.5 ms: 1.00x faster                                                   |
| mako            | 12.9 ms                                                               | 13.2 ms: 1.02x slower                                                   |
| genshi_xml      | 60.6 ms                                                               | 63.9 ms: 1.06x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250619-arminc-aarch64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.68 sec: 2.03x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 472 ms: 1.65x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 899 ms: 1.57x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 474 ms: 1.56x faster                                                    |
| async_tree_none            | 624 ms                                                                | 399 ms: 1.56x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 918 ms: 1.53x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 383 ms: 1.51x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 665 ms: 1.37x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 660 ms: 1.34x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 37.4 us: 1.33x faster                                                   |
| deepcopy                   | 446 us                                                                | 342 us: 1.30x faster                                                    |
| generators                 | 43.5 ms                                                               | 36.0 ms: 1.21x faster                                                   |
| regex_effbot               | 4.64 ms                                                               | 3.93 ms: 1.18x faster                                                   |
| comprehensions             | 25.4 us                                                               | 22.4 us: 1.13x faster                                                   |
| regex_dna                  | 254 ms                                                                | 225 ms: 1.13x faster                                                    |
| regex_compile              | 137 ms                                                                | 122 ms: 1.12x faster                                                    |
| richards_super             | 58.5 ms                                                               | 52.1 ms: 1.12x faster                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 3.66 us: 1.12x faster                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.32 sec: 1.12x faster                                                  |
| pylint                     | 355 ms                                                                | 318 ms: 1.11x faster                                                    |
| richards                   | 50.9 ms                                                               | 46.0 ms: 1.11x faster                                                   |
| float                      | 92.1 ms                                                               | 83.4 ms: 1.10x faster                                                   |
| pathlib                    | 24.5 ms                                                               | 22.3 ms: 1.10x faster                                                   |
| dulwich_log                | 62.0 ms                                                               | 56.5 ms: 1.10x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 178 ms: 1.09x faster                                                    |
| spectral_norm              | 131 ms                                                                | 121 ms: 1.08x faster                                                    |
| deltablue                  | 4.12 ms                                                               | 3.87 ms: 1.06x faster                                                   |
| raytrace                   | 353 ms                                                                | 335 ms: 1.05x faster                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 144 ms: 1.05x faster                                                    |
| scimark_sor                | 150 ms                                                                | 143 ms: 1.04x faster                                                    |
| regex_v8                   | 28.3 ms                                                               | 27.4 ms: 1.04x faster                                                   |
| scimark_fft                | 418 ms                                                                | 405 ms: 1.03x faster                                                    |
| sympy_integrate            | 21.6 ms                                                               | 20.9 ms: 1.03x faster                                                   |
| pyflate                    | 559 ms                                                                | 542 ms: 1.03x faster                                                    |
| html5lib                   | 65.1 ms                                                               | 63.1 ms: 1.03x faster                                                   |
| async_generators           | 491 ms                                                                | 476 ms: 1.03x faster                                                    |
| django_template            | 40.7 ms                                                               | 40.5 ms: 1.00x faster                                                   |
| logging_format             | 8.34 us                                                               | 8.38 us: 1.00x slower                                                   |
| logging_simple             | 7.63 us                                                               | 7.72 us: 1.01x slower                                                   |
| 2to3                       | 308 ms                                                                | 312 ms: 1.01x slower                                                    |
| meteor_contest             | 112 ms                                                                | 113 ms: 1.01x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 668 ms: 1.02x slower                                                    |
| mako                       | 12.9 ms                                                               | 13.2 ms: 1.02x slower                                                   |
| thrift                     | 937 us                                                                | 958 us: 1.02x slower                                                    |
| pidigits                   | 233 ms                                                                | 238 ms: 1.02x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.09 sec: 1.04x slower                                                  |
| json                       | 5.54 ms                                                               | 5.75 ms: 1.04x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.69 ms: 1.04x slower                                                   |
| scimark_lu                 | 146 ms                                                                | 153 ms: 1.05x slower                                                    |
| json_loads                 | 30.7 us                                                               | 32.3 us: 1.05x slower                                                   |
| genshi_xml                 | 60.6 ms                                                               | 63.9 ms: 1.06x slower                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 91.9 ms: 1.06x slower                                                   |
| hexiom                     | 6.98 ms                                                               | 7.43 ms: 1.06x slower                                                   |
| fannkuch                   | 443 ms                                                                | 477 ms: 1.08x slower                                                    |
| sympy_expand               | 454 ms                                                                | 493 ms: 1.09x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.38 sec: 1.09x slower                                                  |
| pickle_pure_python         | 365 us                                                                | 405 us: 1.11x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.8 ms: 1.12x slower                                                   |
| telco                      | 8.51 ms                                                               | 9.55 ms: 1.12x slower                                                   |
| coverage                   | 87.3 ms                                                               | 101 ms: 1.15x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.19 ms: 1.16x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 210 us: 1.16x slower                                                    |
| nbody                      | 105 ms                                                                | 125 ms: 1.19x slower                                                    |
| python_startup             | 11.4 ms                                                               | 15.2 ms: 1.33x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 2.61 sec: 1.39x slower                                                  |
| pprint_safe_repr           | 916 ms                                                                | 1.27 sec: 1.39x slower                                                  |
| gc_traversal               | 4.40 ms                                                               | 6.88 ms: 1.57x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 3.82 ms: 1.99x slower                                                   |
| logging_silent             | 127 ns                                                                | 647 ns: 5.10x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.02x faster                                                            |

Benchmark hidden because not significant (12): sympy_sum, chaos, scimark_monte_carlo, unpickle_pure_python, xml_etree_generate, sympy_str, xml_etree_process, coroutines, go, genshi_text, sqlite_synth, nqueens
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250619-3.15.0a0-9731dd2-JIT/bm-20250619-arminc-aarch64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.042x faster

# HPT report

- Reliability score: 99.17% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.12x