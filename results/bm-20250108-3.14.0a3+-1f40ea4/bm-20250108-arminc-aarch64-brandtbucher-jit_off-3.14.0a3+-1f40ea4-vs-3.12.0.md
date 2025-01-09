# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_off
- machine: linux-aarch64
- commit hash: 1f40ea4
- commit date: 2025-01-08
- overall geometric mean: 1.034x faster
- HPT reliability: 99.95%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (3): 2to3, docutils, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250108-arminc-aarch64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 381 ms: 1.64x faster                                              |
| async_tree_memoization     | 777 ms                                                                | 492 ms: 1.58x faster                                              |
| async_tree_io              | 1.41 sec                                                              | 895 ms: 1.58x faster                                              |
| async_tree_io_tg           | 1.40 sec                                                              | 893 ms: 1.57x faster                                              |
| async_tree_memoization_tg  | 740 ms                                                                | 474 ms: 1.56x faster                                              |
| async_tree_none_tg         | 577 ms                                                                | 381 ms: 1.51x faster                                              |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 677 ms: 1.35x faster                                              |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 664 ms: 1.33x faster                                              |
| Geometric mean             | (ref)                                                                 | 1.51x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250108-arminc-aarch64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| nbody          | 105 ms                                                                | 123 ms: 1.18x slower                                              |
| Geometric mean | (ref)                                                                 | 1.06x slower                                                      |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250108-arminc-aarch64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.91 ms: 1.19x faster                                             |
| regex_compile  | 137 ms                                                                | 126 ms: 1.09x faster                                              |
| regex_dna      | 254 ms                                                                | 244 ms: 1.04x faster                                              |
| regex_v8       | 28.3 ms                                                               | 32.2 ms: 1.14x slower                                             |
| Geometric mean | (ref)                                                                 | 1.04x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250108-arminc-aarch64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|--------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| xml_etree_parse    | 195 ms                                                                | 176 ms: 1.11x faster                                              |
| tomli_loads        | 2.59 sec                                                              | 2.56 sec: 1.01x faster                                            |
| xml_etree_process  | 79.0 ms                                                               | 83.0 ms: 1.05x slower                                             |
| xml_etree_generate | 112 ms                                                                | 118 ms: 1.06x slower                                              |
| pickle_pure_python | 365 us                                                                | 397 us: 1.09x slower                                              |
| json_dumps         | 12.3 ms                                                               | 14.7 ms: 1.20x slower                                             |
| Geometric mean     | (ref)                                                                 | 1.03x slower                                                      |

Benchmark hidden because not significant (3): xml_etree_iterparse, unpickle_pure_python, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250108-arminc-aarch64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.07 ms: 1.08x slower                                             |
| python_startup         | 11.4 ms                                                               | 16.5 ms: 1.45x slower                                             |
| Geometric mean         | (ref)                                                                 | 1.25x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250108-arminc-aarch64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_xml     | 60.6 ms                                                               | 63.6 ms: 1.05x slower                                             |
| mako           | 12.9 ms                                                               | 14.2 ms: 1.10x slower                                             |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                      |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250108-arminc-aarch64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 381 ms: 1.64x faster                                              |
| async_tree_memoization     | 777 ms                                                                | 492 ms: 1.58x faster                                              |
| async_tree_io              | 1.41 sec                                                              | 895 ms: 1.58x faster                                              |
| async_tree_io_tg           | 1.40 sec                                                              | 893 ms: 1.57x faster                                              |
| async_tree_memoization_tg  | 740 ms                                                                | 474 ms: 1.56x faster                                              |
| async_tree_none_tg         | 577 ms                                                                | 381 ms: 1.51x faster                                              |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 677 ms: 1.35x faster                                              |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 664 ms: 1.33x faster                                              |
| deepcopy                   | 446 us                                                                | 355 us: 1.25x faster                                              |
| comprehensions             | 25.4 us                                                               | 21.0 us: 1.21x faster                                             |
| generators                 | 43.5 ms                                                               | 36.5 ms: 1.19x faster                                             |
| deepcopy_memo              | 49.6 us                                                               | 41.7 us: 1.19x faster                                             |
| regex_effbot               | 4.64 ms                                                               | 3.91 ms: 1.19x faster                                             |
| pylint                     | 355 ms                                                                | 312 ms: 1.14x faster                                              |
| xml_etree_parse            | 195 ms                                                                | 176 ms: 1.11x faster                                              |
| deepcopy_reduce            | 4.10 us                                                               | 3.72 us: 1.10x faster                                             |
| pathlib                    | 24.5 ms                                                               | 22.6 ms: 1.09x faster                                             |
| regex_compile              | 137 ms                                                                | 126 ms: 1.09x faster                                              |
| raytrace                   | 353 ms                                                                | 325 ms: 1.09x faster                                              |
| go                         | 157 ms                                                                | 147 ms: 1.07x faster                                              |
| sympy_sum                  | 154 ms                                                                | 146 ms: 1.06x faster                                              |
| scimark_lu                 | 146 ms                                                                | 139 ms: 1.05x faster                                              |
| sqlalchemy_declarative     | 157 ms                                                                | 150 ms: 1.05x faster                                              |
| regex_dna                  | 254 ms                                                                | 244 ms: 1.04x faster                                              |
| crypto_pyaes               | 86.6 ms                                                               | 83.5 ms: 1.04x faster                                             |
| sqlglot_transpile          | 1.83 ms                                                               | 1.77 ms: 1.03x faster                                             |
| tomli_loads                | 2.59 sec                                                              | 2.56 sec: 1.01x faster                                            |
| asyncio_websockets         | 658 ms                                                                | 671 ms: 1.02x slower                                              |
| richards_super             | 58.5 ms                                                               | 60.1 ms: 1.03x slower                                             |
| sqlglot_optimize           | 61.3 ms                                                               | 63.2 ms: 1.03x slower                                             |
| scimark_sor                | 150 ms                                                                | 156 ms: 1.04x slower                                              |
| pprint_safe_repr           | 916 ms                                                                | 958 ms: 1.05x slower                                              |
| genshi_xml                 | 60.6 ms                                                               | 63.6 ms: 1.05x slower                                             |
| xml_etree_process          | 79.0 ms                                                               | 83.0 ms: 1.05x slower                                             |
| xml_etree_generate         | 112 ms                                                                | 118 ms: 1.06x slower                                              |
| pprint_pformat             | 1.88 sec                                                              | 1.99 sec: 1.06x slower                                            |
| nqueens                    | 99.2 ms                                                               | 106 ms: 1.06x slower                                              |
| sympy_expand               | 454 ms                                                                | 487 ms: 1.07x slower                                              |
| hexiom                     | 6.98 ms                                                               | 7.51 ms: 1.08x slower                                             |
| logging_silent             | 127 ns                                                                | 137 ns: 1.08x slower                                              |
| python_startup_no_site     | 8.37 ms                                                               | 9.07 ms: 1.08x slower                                             |
| pickle_pure_python         | 365 us                                                                | 397 us: 1.09x slower                                              |
| sqlite_synth               | 3.77 us                                                               | 4.10 us: 1.09x slower                                             |
| mako                       | 12.9 ms                                                               | 14.2 ms: 1.10x slower                                             |
| fannkuch                   | 443 ms                                                                | 489 ms: 1.10x slower                                              |
| regex_v8                   | 28.3 ms                                                               | 32.2 ms: 1.14x slower                                             |
| telco                      | 8.51 ms                                                               | 9.82 ms: 1.15x slower                                             |
| typing_runtime_protocols   | 181 us                                                                | 209 us: 1.16x slower                                              |
| nbody                      | 105 ms                                                                | 123 ms: 1.18x slower                                              |
| json_dumps                 | 12.3 ms                                                               | 14.7 ms: 1.20x slower                                             |
| coverage                   | 87.3 ms                                                               | 106 ms: 1.22x slower                                              |
| python_startup             | 11.4 ms                                                               | 16.5 ms: 1.45x slower                                             |
| gc_traversal               | 4.40 ms                                                               | 6.96 ms: 1.58x slower                                             |
| create_gc_cycles           | 1.92 ms                                                               | 3.62 ms: 1.89x slower                                             |
| bench_mp_pool              | 7.05 ms                                                               | 5.05 sec: 715.99x slower                                          |
| Geometric mean             | (ref)                                                                 | 1.06x slower                                                      |

Benchmark hidden because not significant (34): xml_etree_iterparse, logging_simple, deltablue, html5lib, float, dulwich_log, logging_format, sqlalchemy_imperative, json, genshi_text, 2to3, spectral_norm, scimark_monte_carlo, mdp, sqlglot_parse, thrift, docutils, scimark_sparse_mat_mult, pyflate, pycparser, unpickle_pure_python, sympy_integrate, bench_thread_pool, sympy_str, scimark_fft, coroutines, async_generators, sqlglot_normalize, chaos, pidigits, django_template, richards, json_loads, meteor_contest
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20250108-3.14.0a3+-1f40ea4/bm-20250108-arminc-aarch64-brandtbucher-jit_off-3.14.0a3+-1f40ea4.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.034x faster

# HPT report

- Reliability score: 99.95% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x