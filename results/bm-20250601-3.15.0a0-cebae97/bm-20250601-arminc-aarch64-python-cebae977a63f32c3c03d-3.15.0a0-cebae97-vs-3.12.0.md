# Results vs. 3.12.0

- fork: python
- ref: cebae977a63f32c3c03d
- machine: linux-aarch64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.058x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| html5lib       | 65.1 ms                                                               | 62.3 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                            |

Benchmark hidden because not significant (2): 2to3, docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 470 ms: 1.65x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 870 ms: 1.62x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 464 ms: 1.59x faster                                                    |
| async_tree_none            | 624 ms                                                                | 394 ms: 1.58x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 905 ms: 1.55x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 372 ms: 1.55x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 665 ms: 1.37x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 650 ms: 1.36x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.53x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 86.1 ms: 1.07x faster                                                   |
| pidigits       | 233 ms                                                                | 237 ms: 1.02x slower                                                    |
| nbody          | 105 ms                                                                | 120 ms: 1.15x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.92 ms: 1.18x faster                                                   |
| regex_dna      | 254 ms                                                                | 227 ms: 1.12x faster                                                    |
| regex_compile  | 137 ms                                                                | 123 ms: 1.11x faster                                                    |
| regex_v8       | 28.3 ms                                                               | 26.8 ms: 1.06x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.12x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|---------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 182 ms: 1.07x faster                                                    |
| xml_etree_iterparse | 150 ms                                                                | 143 ms: 1.05x faster                                                    |
| tomli_loads         | 2.59 sec                                                              | 2.47 sec: 1.05x faster                                                  |
| xml_etree_process   | 79.0 ms                                                               | 79.9 ms: 1.01x slower                                                   |
| pickle_pure_python  | 365 us                                                                | 384 us: 1.05x slower                                                    |
| json_loads          | 30.7 us                                                               | 32.5 us: 1.06x slower                                                   |
| json_dumps          | 12.3 ms                                                               | 13.6 ms: 1.11x slower                                                   |
| Geometric mean      | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (2): xml_etree_generate, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.71 ms: 1.04x slower                                                   |
| python_startup         | 11.4 ms                                                               | 15.2 ms: 1.33x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.18x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml     | 60.6 ms                                                               | 60.3 ms: 1.01x faster                                                   |
| mako           | 12.9 ms                                                               | 13.9 ms: 1.08x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.68 sec: 2.03x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 470 ms: 1.65x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 870 ms: 1.62x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 464 ms: 1.59x faster                                                    |
| async_tree_none            | 624 ms                                                                | 394 ms: 1.58x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 905 ms: 1.55x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 372 ms: 1.55x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 665 ms: 1.37x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 650 ms: 1.36x faster                                                    |
| deepcopy                   | 446 us                                                                | 331 us: 1.35x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 38.2 us: 1.30x faster                                                   |
| comprehensions             | 25.4 us                                                               | 20.7 us: 1.23x faster                                                   |
| go                         | 157 ms                                                                | 130 ms: 1.21x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 3.92 ms: 1.18x faster                                                   |
| generators                 | 43.5 ms                                                               | 36.8 ms: 1.18x faster                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 3.55 us: 1.15x faster                                                   |
| dulwich_log                | 62.0 ms                                                               | 54.0 ms: 1.15x faster                                                   |
| pylint                     | 355 ms                                                                | 317 ms: 1.12x faster                                                    |
| regex_dna                  | 254 ms                                                                | 227 ms: 1.12x faster                                                    |
| regex_compile              | 137 ms                                                                | 123 ms: 1.11x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 22.5 ms: 1.09x faster                                                   |
| raytrace                   | 353 ms                                                                | 328 ms: 1.08x faster                                                    |
| async_generators           | 491 ms                                                                | 458 ms: 1.07x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 182 ms: 1.07x faster                                                    |
| float                      | 92.1 ms                                                               | 86.1 ms: 1.07x faster                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 79.7 ms: 1.07x faster                                                   |
| sympy_integrate            | 21.6 ms                                                               | 20.4 ms: 1.06x faster                                                   |
| regex_v8                   | 28.3 ms                                                               | 26.8 ms: 1.06x faster                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 143 ms: 1.05x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.47 sec: 1.05x faster                                                  |
| pyflate                    | 559 ms                                                                | 533 ms: 1.05x faster                                                    |
| sympy_str                  | 280 ms                                                                | 267 ms: 1.05x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 147 ms: 1.05x faster                                                    |
| html5lib                   | 65.1 ms                                                               | 62.3 ms: 1.04x faster                                                   |
| genshi_xml                 | 60.6 ms                                                               | 60.3 ms: 1.01x faster                                                   |
| xml_etree_process          | 79.0 ms                                                               | 79.9 ms: 1.01x slower                                                   |
| asyncio_websockets         | 658 ms                                                                | 668 ms: 1.02x slower                                                    |
| pidigits                   | 233 ms                                                                | 237 ms: 1.02x slower                                                    |
| scimark_fft                | 418 ms                                                                | 433 ms: 1.03x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 8.71 ms: 1.04x slower                                                   |
| richards                   | 50.9 ms                                                               | 53.1 ms: 1.04x slower                                                   |
| json                       | 5.54 ms                                                               | 5.81 ms: 1.05x slower                                                   |
| fannkuch                   | 443 ms                                                                | 466 ms: 1.05x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 384 us: 1.05x slower                                                    |
| json_loads                 | 30.7 us                                                               | 32.5 us: 1.06x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 194 us: 1.08x slower                                                    |
| mako                       | 12.9 ms                                                               | 13.9 ms: 1.08x slower                                                   |
| thrift                     | 937 us                                                                | 1.01 ms: 1.08x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 2.04 sec: 1.09x slower                                                  |
| pprint_safe_repr           | 916 ms                                                                | 1.01 sec: 1.10x slower                                                  |
| json_dumps                 | 12.3 ms                                                               | 13.6 ms: 1.11x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.92 ms: 1.12x slower                                                   |
| telco                      | 8.51 ms                                                               | 9.74 ms: 1.15x slower                                                   |
| nbody                      | 105 ms                                                                | 120 ms: 1.15x slower                                                    |
| coverage                   | 87.3 ms                                                               | 102 ms: 1.17x slower                                                    |
| python_startup             | 11.4 ms                                                               | 15.2 ms: 1.33x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 6.90 ms: 1.57x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 3.80 ms: 1.98x slower                                                   |
| logging_silent             | 127 ns                                                                | 623 ns: 4.91x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.03x faster                                                            |

Benchmark hidden because not significant (22): deltablue, crypto_pyaes, django_template, chaos, scimark_sor, 2to3, spectral_norm, docutils, pycparser, richards_super, genshi_text, logging_simple, sqlite_synth, logging_format, nqueens, xml_etree_generate, sympy_expand, hexiom, meteor_contest, coroutines, unpickle_pure_python, scimark_lu
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250601-3.15.0a0-cebae97/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.058x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.09x