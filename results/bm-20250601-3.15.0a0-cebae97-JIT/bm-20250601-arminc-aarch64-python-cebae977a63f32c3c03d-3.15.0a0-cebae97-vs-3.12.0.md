# Results vs. 3.12.0

- fork: python
- ref: cebae977a63f32c3c03d
- machine: linux-aarch64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.488x faster
- HPT reliability: 99.83%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 312 ms: 1.01x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.11 sec: 1.04x slower                                                  |
| html5lib       | 65.1 ms                                                               | 61.9 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 475 ms: 1.64x faster                                                    |
| async_tree_none            | 624 ms                                                                | 398 ms: 1.57x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 914 ms: 1.54x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 481 ms: 1.54x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 914 ms: 1.54x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 381 ms: 1.51x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 678 ms: 1.35x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 666 ms: 1.33x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.50x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 85.8 ms: 1.07x faster                                                   |
| pidigits       | 233 ms                                                                | 236 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 119 ms: 1.14x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.03 ms: 1.15x faster                                                   |
| regex_dna      | 254 ms                                                                | 233 ms: 1.09x faster                                                    |
| regex_v8       | 28.3 ms                                                               | 27.7 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.09x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|---------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads         | 2.59 sec                                                              | 2.35 sec: 1.11x faster                                                  |
| xml_etree_parse     | 195 ms                                                                | 186 ms: 1.05x faster                                                    |
| xml_etree_iterparse | 150 ms                                                                | 148 ms: 1.02x faster                                                    |
| xml_etree_process   | 79.0 ms                                                               | 78.0 ms: 1.01x faster                                                   |
| json_loads          | 30.7 us                                                               | 32.0 us: 1.04x slower                                                   |
| pickle_pure_python  | 365 us                                                                | 390 us: 1.07x slower                                                    |
| json_dumps          | 12.3 ms                                                               | 13.3 ms: 1.09x slower                                                   |
| Geometric mean      | (ref)                                                                 | 1.00x faster                                                            |

Benchmark hidden because not significant (2): xml_etree_generate, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.56 ms: 1.02x slower                                                   |
| python_startup         | 11.4 ms                                                               | 15.0 ms: 1.32x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.16x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 12.9 ms                                                               | 13.1 ms: 1.02x slower                                                   |
| genshi_xml     | 60.6 ms                                                               | 64.0 ms: 1.06x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pprint_pformat             | 1.88 sec                                                              | 1.91 us: 985095.58x faster                                              |
| pprint_safe_repr           | 916 ms                                                                | 1.05 us: 871082.58x faster                                              |
| mdp                        | 3.41 sec                                                              | 1.69 sec: 2.02x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 475 ms: 1.64x faster                                                    |
| async_tree_none            | 624 ms                                                                | 398 ms: 1.57x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 914 ms: 1.54x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 481 ms: 1.54x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 914 ms: 1.54x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 381 ms: 1.51x faster                                                    |
| deepcopy                   | 446 us                                                                | 325 us: 1.37x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 678 ms: 1.35x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 666 ms: 1.33x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 37.8 us: 1.31x faster                                                   |
| generators                 | 43.5 ms                                                               | 36.1 ms: 1.20x faster                                                   |
| dulwich_log                | 62.0 ms                                                               | 53.3 ms: 1.16x faster                                                   |
| regex_effbot               | 4.64 ms                                                               | 4.03 ms: 1.15x faster                                                   |
| comprehensions             | 25.4 us                                                               | 22.5 us: 1.13x faster                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 3.65 us: 1.12x faster                                                   |
| richards                   | 50.9 ms                                                               | 45.4 ms: 1.12x faster                                                   |
| richards_super             | 58.5 ms                                                               | 52.5 ms: 1.11x faster                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.35 sec: 1.11x faster                                                  |
| pylint                     | 355 ms                                                                | 323 ms: 1.10x faster                                                    |
| regex_dna                  | 254 ms                                                                | 233 ms: 1.09x faster                                                    |
| float                      | 92.1 ms                                                               | 85.8 ms: 1.07x faster                                                   |
| deltablue                  | 4.12 ms                                                               | 3.86 ms: 1.07x faster                                                   |
| pathlib                    | 24.5 ms                                                               | 23.0 ms: 1.07x faster                                                   |
| raytrace                   | 353 ms                                                                | 332 ms: 1.06x faster                                                    |
| html5lib                   | 65.1 ms                                                               | 61.9 ms: 1.05x faster                                                   |
| pyflate                    | 559 ms                                                                | 532 ms: 1.05x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 186 ms: 1.05x faster                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 82.3 ms: 1.03x faster                                                   |
| regex_v8                   | 28.3 ms                                                               | 27.7 ms: 1.02x faster                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 148 ms: 1.02x faster                                                    |
| xml_etree_process          | 79.0 ms                                                               | 78.0 ms: 1.01x faster                                                   |
| logging_format             | 8.34 us                                                               | 8.26 us: 1.01x faster                                                   |
| go                         | 157 ms                                                                | 159 ms: 1.01x slower                                                    |
| 2to3                       | 308 ms                                                                | 312 ms: 1.01x slower                                                    |
| pidigits                   | 233 ms                                                                | 236 ms: 1.01x slower                                                    |
| mako                       | 12.9 ms                                                               | 13.1 ms: 1.02x slower                                                   |
| coroutines                 | 29.0 ms                                                               | 29.6 ms: 1.02x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.56 ms: 1.02x slower                                                   |
| asyncio_websockets         | 658 ms                                                                | 674 ms: 1.02x slower                                                    |
| json                       | 5.54 ms                                                               | 5.71 ms: 1.03x slower                                                   |
| json_loads                 | 30.7 us                                                               | 32.0 us: 1.04x slower                                                   |
| docutils                   | 2.98 sec                                                              | 3.11 sec: 1.04x slower                                                  |
| genshi_xml                 | 60.6 ms                                                               | 64.0 ms: 1.06x slower                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 91.9 ms: 1.06x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 390 us: 1.07x slower                                                    |
| thrift                     | 937 us                                                                | 1.00 ms: 1.07x slower                                                   |
| telco                      | 8.51 ms                                                               | 9.15 ms: 1.08x slower                                                   |
| nqueens                    | 99.2 ms                                                               | 107 ms: 1.08x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 7.54 ms: 1.08x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 13.3 ms: 1.09x slower                                                   |
| sympy_expand               | 454 ms                                                                | 494 ms: 1.09x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.39 sec: 1.10x slower                                                  |
| fannkuch                   | 443 ms                                                                | 493 ms: 1.11x slower                                                    |
| meteor_contest             | 112 ms                                                                | 125 ms: 1.11x slower                                                    |
| nbody                      | 105 ms                                                                | 119 ms: 1.14x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 206 us: 1.14x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.12 ms: 1.15x slower                                                   |
| coverage                   | 87.3 ms                                                               | 104 ms: 1.19x slower                                                    |
| python_startup             | 11.4 ms                                                               | 15.0 ms: 1.32x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 6.85 ms: 1.56x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 3.77 ms: 1.97x slower                                                   |
| logging_silent             | 127 ns                                                                | 610 ns: 4.81x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.44x faster                                                            |

Benchmark hidden because not significant (15): scimark_sor, sympy_integrate, sympy_sum, xml_etree_generate, async_generators, unpickle_pure_python, django_template, sqlite_synth, chaos, spectral_norm, genshi_text, scimark_fft, logging_simple, sympy_str, scimark_lu
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, regex_compile, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.488x faster

# HPT report

- Reliability score: 99.83% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x