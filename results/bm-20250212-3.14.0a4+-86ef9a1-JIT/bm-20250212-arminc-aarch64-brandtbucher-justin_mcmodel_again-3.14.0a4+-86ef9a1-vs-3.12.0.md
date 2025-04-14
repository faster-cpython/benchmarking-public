# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_mcmodel_again
- machine: linux-aarch64
- commit hash: 86ef9a1
- commit date: 2025-02-12
- overall geometric mean: 1.003x slower
- HPT reliability: 67.02%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250212-arminc-aarch64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 319 ms: 1.03x slower                                                           |
| docutils       | 2.98 sec                                                              | 3.23 sec: 1.08x slower                                                         |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                                   |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250212-arminc-aarch64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 414 ms: 1.51x faster                                                           |
| async_tree_memoization     | 777 ms                                                                | 518 ms: 1.50x faster                                                           |
| async_tree_io_tg           | 1.40 sec                                                              | 947 ms: 1.48x faster                                                           |
| async_tree_io              | 1.41 sec                                                              | 958 ms: 1.47x faster                                                           |
| async_tree_memoization_tg  | 740 ms                                                                | 512 ms: 1.44x faster                                                           |
| async_tree_none_tg         | 577 ms                                                                | 409 ms: 1.41x faster                                                           |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 701 ms: 1.30x faster                                                           |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 690 ms: 1.28x faster                                                           |
| Geometric mean             | (ref)                                                                 | 1.42x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250212-arminc-aarch64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 85.0 ms: 1.08x faster                                                          |
| nbody          | 105 ms                                                                | 132 ms: 1.26x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.06x slower                                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250212-arminc-aarch64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.02 ms: 1.15x faster                                                          |
| regex_compile  | 137 ms                                                                | 130 ms: 1.06x faster                                                           |
| regex_v8       | 28.3 ms                                                               | 31.8 ms: 1.12x slower                                                          |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                                   |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250212-arminc-aarch64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 180 ms: 1.09x faster                                                           |
| tomli_loads          | 2.59 sec                                                              | 2.55 sec: 1.02x faster                                                         |
| xml_etree_process    | 79.0 ms                                                               | 81.8 ms: 1.04x slower                                                          |
| unpickle_pure_python | 260 us                                                                | 284 us: 1.09x slower                                                           |
| pickle_pure_python   | 365 us                                                                | 411 us: 1.13x slower                                                           |
| json_loads           | 30.7 us                                                               | 35.9 us: 1.17x slower                                                          |
| json_dumps           | 12.3 ms                                                               | 14.8 ms: 1.21x slower                                                          |
| Geometric mean       | (ref)                                                                 | 1.06x slower                                                                   |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250212-arminc-aarch64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.15 ms: 1.09x slower                                                          |
| python_startup         | 11.4 ms                                                               | 16.6 ms: 1.46x slower                                                          |
| Geometric mean         | (ref)                                                                 | 1.27x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250212-arminc-aarch64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                               | 29.5 ms: 1.07x slower                                                          |
| genshi_xml     | 60.6 ms                                                               | 65.9 ms: 1.09x slower                                                          |
| mako           | 12.9 ms                                                               | 14.3 ms: 1.11x slower                                                          |
| Geometric mean | (ref)                                                                 | 1.07x slower                                                                   |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250212-arminc-aarch64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 414 ms: 1.51x faster                                                           |
| async_tree_memoization     | 777 ms                                                                | 518 ms: 1.50x faster                                                           |
| async_tree_io_tg           | 1.40 sec                                                              | 947 ms: 1.48x faster                                                           |
| async_tree_io              | 1.41 sec                                                              | 958 ms: 1.47x faster                                                           |
| async_tree_memoization_tg  | 740 ms                                                                | 512 ms: 1.44x faster                                                           |
| async_tree_none_tg         | 577 ms                                                                | 409 ms: 1.41x faster                                                           |
| deepcopy                   | 446 us                                                                | 339 us: 1.31x faster                                                           |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 701 ms: 1.30x faster                                                           |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 690 ms: 1.28x faster                                                           |
| deepcopy_memo              | 49.6 us                                                               | 40.0 us: 1.24x faster                                                          |
| generators                 | 43.5 ms                                                               | 37.1 ms: 1.17x faster                                                          |
| regex_effbot               | 4.64 ms                                                               | 4.02 ms: 1.15x faster                                                          |
| deepcopy_reduce            | 4.10 us                                                               | 3.64 us: 1.13x faster                                                          |
| pylint                     | 355 ms                                                                | 325 ms: 1.09x faster                                                           |
| xml_etree_parse            | 195 ms                                                                | 180 ms: 1.09x faster                                                           |
| float                      | 92.1 ms                                                               | 85.0 ms: 1.08x faster                                                          |
| spectral_norm              | 131 ms                                                                | 123 ms: 1.06x faster                                                           |
| regex_compile              | 137 ms                                                                | 130 ms: 1.06x faster                                                           |
| pathlib                    | 24.5 ms                                                               | 23.3 ms: 1.05x faster                                                          |
| raytrace                   | 353 ms                                                                | 335 ms: 1.05x faster                                                           |
| logging_format             | 8.34 us                                                               | 7.92 us: 1.05x faster                                                          |
| logging_simple             | 7.63 us                                                               | 7.27 us: 1.05x faster                                                          |
| comprehensions             | 25.4 us                                                               | 24.4 us: 1.04x faster                                                          |
| scimark_lu                 | 146 ms                                                                | 140 ms: 1.04x faster                                                           |
| sqlalchemy_declarative     | 157 ms                                                                | 152 ms: 1.04x faster                                                           |
| chaos                      | 71.4 ms                                                               | 68.9 ms: 1.04x faster                                                          |
| thrift                     | 937 us                                                                | 919 us: 1.02x faster                                                           |
| tomli_loads                | 2.59 sec                                                              | 2.55 sec: 1.02x faster                                                         |
| asyncio_websockets         | 658 ms                                                                | 673 ms: 1.02x slower                                                           |
| dulwich_log                | 62.0 ms                                                               | 64.1 ms: 1.03x slower                                                          |
| 2to3                       | 308 ms                                                                | 319 ms: 1.03x slower                                                           |
| xml_etree_process          | 79.0 ms                                                               | 81.8 ms: 1.04x slower                                                          |
| pyflate                    | 559 ms                                                                | 580 ms: 1.04x slower                                                           |
| richards                   | 50.9 ms                                                               | 53.0 ms: 1.04x slower                                                          |
| sqlglot_transpile          | 1.83 ms                                                               | 1.90 ms: 1.04x slower                                                          |
| mdp                        | 3.41 sec                                                              | 3.56 sec: 1.04x slower                                                         |
| sqlite_synth               | 3.77 us                                                               | 3.99 us: 1.06x slower                                                          |
| sqlglot_normalize          | 126 ms                                                                | 134 ms: 1.07x slower                                                           |
| genshi_text                | 27.4 ms                                                               | 29.5 ms: 1.07x slower                                                          |
| sqlglot_parse              | 1.46 ms                                                               | 1.58 ms: 1.08x slower                                                          |
| docutils                   | 2.98 sec                                                              | 3.23 sec: 1.08x slower                                                         |
| scimark_sor                | 150 ms                                                                | 162 ms: 1.08x slower                                                           |
| genshi_xml                 | 60.6 ms                                                               | 65.9 ms: 1.09x slower                                                          |
| sqlglot_optimize           | 61.3 ms                                                               | 66.9 ms: 1.09x slower                                                          |
| unpickle_pure_python       | 260 us                                                                | 284 us: 1.09x slower                                                           |
| python_startup_no_site     | 8.37 ms                                                               | 9.15 ms: 1.09x slower                                                          |
| go                         | 157 ms                                                                | 173 ms: 1.10x slower                                                           |
| logging_silent             | 127 ns                                                                | 140 ns: 1.10x slower                                                           |
| json                       | 5.54 ms                                                               | 6.13 ms: 1.11x slower                                                          |
| mako                       | 12.9 ms                                                               | 14.3 ms: 1.11x slower                                                          |
| sympy_expand               | 454 ms                                                                | 503 ms: 1.11x slower                                                           |
| regex_v8                   | 28.3 ms                                                               | 31.8 ms: 1.12x slower                                                          |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.95 ms: 1.12x slower                                                          |
| pickle_pure_python         | 365 us                                                                | 411 us: 1.13x slower                                                           |
| meteor_contest             | 112 ms                                                                | 126 ms: 1.13x slower                                                           |
| pycparser                  | 1.26 sec                                                              | 1.43 sec: 1.14x slower                                                         |
| crypto_pyaes               | 86.6 ms                                                               | 98.7 ms: 1.14x slower                                                          |
| coverage                   | 87.3 ms                                                               | 101 ms: 1.15x slower                                                           |
| json_loads                 | 30.7 us                                                               | 35.9 us: 1.17x slower                                                          |
| telco                      | 8.51 ms                                                               | 9.96 ms: 1.17x slower                                                          |
| json_dumps                 | 12.3 ms                                                               | 14.8 ms: 1.21x slower                                                          |
| typing_runtime_protocols   | 181 us                                                                | 220 us: 1.22x slower                                                           |
| fannkuch                   | 443 ms                                                                | 544 ms: 1.23x slower                                                           |
| nbody                      | 105 ms                                                                | 132 ms: 1.26x slower                                                           |
| nqueens                    | 99.2 ms                                                               | 127 ms: 1.28x slower                                                           |
| hexiom                     | 6.98 ms                                                               | 9.15 ms: 1.31x slower                                                          |
| python_startup             | 11.4 ms                                                               | 16.6 ms: 1.46x slower                                                          |
| pprint_pformat             | 1.88 sec                                                              | 2.77 sec: 1.47x slower                                                         |
| pprint_safe_repr           | 916 ms                                                                | 1.35 sec: 1.47x slower                                                         |
| gc_traversal               | 4.40 ms                                                               | 6.93 ms: 1.58x slower                                                          |
| create_gc_cycles           | 1.92 ms                                                               | 3.72 ms: 1.94x slower                                                          |
| bench_mp_pool              | 7.05 ms                                                               | 2.14 sec: 303.05x slower                                                       |
| Geometric mean             | (ref)                                                                 | 1.09x slower                                                                   |

Benchmark hidden because not significant (17): xml_etree_iterparse, html5lib, regex_dna, coroutines, async_generators, scimark_monte_carlo, deltablue, pidigits, sympy_integrate, sympy_sum, scimark_fft, django_template, sqlalchemy_imperative, sympy_str, xml_etree_generate, bench_thread_pool, richards_super
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20250212-3.14.0a4+-86ef9a1-JIT/bm-20250212-arminc-aarch64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.003x slower

# HPT report

- Reliability score: 67.02% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x