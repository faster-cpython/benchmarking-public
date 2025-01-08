# Results vs. 3.12.0

- fork: brandtbucher
- ref: nojit
- machine: linux-aarch64
- commit hash: f098037
- commit date: 2025-01-07
- overall geometric mean: 1.033x faster
- HPT reliability: 96.07%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| docutils       | 2.98 sec                                                              | 3.03 sec: 1.01x slower                                          |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                    |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 375 ms: 1.66x faster                                            |
| async_tree_memoization     | 777 ms                                                                | 490 ms: 1.59x faster                                            |
| async_tree_io              | 1.41 sec                                                              | 890 ms: 1.59x faster                                            |
| async_tree_io_tg           | 1.40 sec                                                              | 901 ms: 1.56x faster                                            |
| async_tree_memoization_tg  | 740 ms                                                                | 478 ms: 1.55x faster                                            |
| async_tree_none_tg         | 577 ms                                                                | 382 ms: 1.51x faster                                            |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 672 ms: 1.36x faster                                            |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 667 ms: 1.33x faster                                            |
| Geometric mean             | (ref)                                                                 | 1.51x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 246 ms: 1.06x slower                                            |
| nbody          | 105 ms                                                                | 125 ms: 1.20x slower                                            |
| Geometric mean | (ref)                                                                 | 1.08x slower                                                    |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.06 ms: 1.14x faster                                           |
| regex_compile  | 137 ms                                                                | 129 ms: 1.06x faster                                            |
| regex_dna      | 254 ms                                                                | 245 ms: 1.04x faster                                            |
| regex_v8       | 28.3 ms                                                               | 32.8 ms: 1.16x slower                                           |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|---------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 180 ms: 1.08x faster                                            |
| xml_etree_iterparse | 150 ms                                                                | 143 ms: 1.05x faster                                            |
| xml_etree_generate  | 112 ms                                                                | 115 ms: 1.03x slower                                            |
| json_loads          | 30.7 us                                                               | 32.5 us: 1.06x slower                                           |
| xml_etree_process   | 79.0 ms                                                               | 85.6 ms: 1.08x slower                                           |
| pickle_pure_python  | 365 us                                                                | 400 us: 1.09x slower                                            |
| json_dumps          | 12.3 ms                                                               | 14.4 ms: 1.18x slower                                           |
| Geometric mean      | (ref)                                                                 | 1.04x slower                                                    |

Benchmark hidden because not significant (2): tomli_loads, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.01 ms: 1.08x slower                                           |
| python_startup         | 11.4 ms                                                               | 16.2 ms: 1.43x slower                                           |
| Geometric mean         | (ref)                                                                 | 1.24x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| genshi_xml     | 60.6 ms                                                               | 62.8 ms: 1.04x slower                                           |
| mako           | 12.9 ms                                                               | 14.3 ms: 1.11x slower                                           |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                    |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 375 ms: 1.66x faster                                            |
| async_tree_memoization     | 777 ms                                                                | 490 ms: 1.59x faster                                            |
| async_tree_io              | 1.41 sec                                                              | 890 ms: 1.59x faster                                            |
| async_tree_io_tg           | 1.40 sec                                                              | 901 ms: 1.56x faster                                            |
| async_tree_memoization_tg  | 740 ms                                                                | 478 ms: 1.55x faster                                            |
| async_tree_none_tg         | 577 ms                                                                | 382 ms: 1.51x faster                                            |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 672 ms: 1.36x faster                                            |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 667 ms: 1.33x faster                                            |
| deepcopy                   | 446 us                                                                | 342 us: 1.30x faster                                            |
| deepcopy_memo              | 49.6 us                                                               | 41.2 us: 1.20x faster                                           |
| comprehensions             | 25.4 us                                                               | 21.2 us: 1.20x faster                                           |
| generators                 | 43.5 ms                                                               | 36.9 ms: 1.18x faster                                           |
| pylint                     | 355 ms                                                                | 307 ms: 1.16x faster                                            |
| regex_effbot               | 4.64 ms                                                               | 4.06 ms: 1.14x faster                                           |
| pathlib                    | 24.5 ms                                                               | 21.7 ms: 1.13x faster                                           |
| deepcopy_reduce            | 4.10 us                                                               | 3.67 us: 1.12x faster                                           |
| go                         | 157 ms                                                                | 144 ms: 1.09x faster                                            |
| xml_etree_parse            | 195 ms                                                                | 180 ms: 1.08x faster                                            |
| sympy_sum                  | 154 ms                                                                | 143 ms: 1.08x faster                                            |
| raytrace                   | 353 ms                                                                | 329 ms: 1.07x faster                                            |
| regex_compile              | 137 ms                                                                | 129 ms: 1.06x faster                                            |
| logging_simple             | 7.63 us                                                               | 7.19 us: 1.06x faster                                           |
| scimark_lu                 | 146 ms                                                                | 138 ms: 1.06x faster                                            |
| xml_etree_iterparse        | 150 ms                                                                | 143 ms: 1.05x faster                                            |
| sqlalchemy_imperative      | 16.7 ms                                                               | 15.9 ms: 1.05x faster                                           |
| sqlalchemy_declarative     | 157 ms                                                                | 151 ms: 1.04x faster                                            |
| deltablue                  | 4.12 ms                                                               | 3.96 ms: 1.04x faster                                           |
| regex_dna                  | 254 ms                                                                | 245 ms: 1.04x faster                                            |
| sympy_str                  | 280 ms                                                                | 272 ms: 1.03x faster                                            |
| json                       | 5.54 ms                                                               | 5.49 ms: 1.01x faster                                           |
| richards_super             | 58.5 ms                                                               | 58.1 ms: 1.01x faster                                           |
| richards                   | 50.9 ms                                                               | 51.6 ms: 1.01x slower                                           |
| docutils                   | 2.98 sec                                                              | 3.03 sec: 1.01x slower                                          |
| sqlglot_optimize           | 61.3 ms                                                               | 62.4 ms: 1.02x slower                                           |
| xml_etree_generate         | 112 ms                                                                | 115 ms: 1.03x slower                                            |
| pycparser                  | 1.26 sec                                                              | 1.29 sec: 1.03x slower                                          |
| meteor_contest             | 112 ms                                                                | 115 ms: 1.03x slower                                            |
| asyncio_websockets         | 658 ms                                                                | 678 ms: 1.03x slower                                            |
| genshi_xml                 | 60.6 ms                                                               | 62.8 ms: 1.04x slower                                           |
| thrift                     | 937 us                                                                | 972 us: 1.04x slower                                            |
| scimark_fft                | 418 ms                                                                | 435 ms: 1.04x slower                                            |
| sqlglot_normalize          | 126 ms                                                                | 131 ms: 1.05x slower                                            |
| sympy_expand               | 454 ms                                                                | 474 ms: 1.05x slower                                            |
| pprint_safe_repr           | 916 ms                                                                | 958 ms: 1.05x slower                                            |
| pprint_pformat             | 1.88 sec                                                              | 1.99 sec: 1.06x slower                                          |
| hexiom                     | 6.98 ms                                                               | 7.37 ms: 1.06x slower                                           |
| pidigits                   | 233 ms                                                                | 246 ms: 1.06x slower                                            |
| json_loads                 | 30.7 us                                                               | 32.5 us: 1.06x slower                                           |
| nqueens                    | 99.2 ms                                                               | 105 ms: 1.06x slower                                            |
| scimark_sor                | 150 ms                                                                | 159 ms: 1.06x slower                                            |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.67 ms: 1.08x slower                                           |
| python_startup_no_site     | 8.37 ms                                                               | 9.01 ms: 1.08x slower                                           |
| fannkuch                   | 443 ms                                                                | 478 ms: 1.08x slower                                            |
| xml_etree_process          | 79.0 ms                                                               | 85.6 ms: 1.08x slower                                           |
| pickle_pure_python         | 365 us                                                                | 400 us: 1.09x slower                                            |
| logging_silent             | 127 ns                                                                | 140 ns: 1.10x slower                                            |
| mako                       | 12.9 ms                                                               | 14.3 ms: 1.11x slower                                           |
| typing_runtime_protocols   | 181 us                                                                | 203 us: 1.12x slower                                            |
| sqlite_synth               | 3.77 us                                                               | 4.30 us: 1.14x slower                                           |
| coverage                   | 87.3 ms                                                               | 100 ms: 1.15x slower                                            |
| regex_v8                   | 28.3 ms                                                               | 32.8 ms: 1.16x slower                                           |
| telco                      | 8.51 ms                                                               | 9.97 ms: 1.17x slower                                           |
| json_dumps                 | 12.3 ms                                                               | 14.4 ms: 1.18x slower                                           |
| mypy2                      | 873 ms                                                                | 1.05 sec: 1.20x slower                                          |
| nbody                      | 105 ms                                                                | 125 ms: 1.20x slower                                            |
| python_startup             | 11.4 ms                                                               | 16.2 ms: 1.43x slower                                           |
| gc_traversal               | 4.40 ms                                                               | 6.91 ms: 1.57x slower                                           |
| create_gc_cycles           | 1.92 ms                                                               | 3.71 ms: 1.94x slower                                           |
| bench_mp_pool              | 7.05 ms                                                               | 3.47 sec: 491.85x slower                                        |
| Geometric mean             | (ref)                                                                 | 1.06x slower                                                    |

Benchmark hidden because not significant (21): sqlglot_transpile, float, logging_format, spectral_norm, sqlglot_parse, bench_thread_pool, crypto_pyaes, html5lib, 2to3, mdp, chaos, scimark_monte_carlo, async_generators, tomli_loads, coroutines, dulwich_log, sympy_integrate, pyflate, genshi_text, unpickle_pure_python, django_template
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20250107-3.14.0a3+-f098037/bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.033x faster

# HPT report

- Reliability score: 96.07% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x