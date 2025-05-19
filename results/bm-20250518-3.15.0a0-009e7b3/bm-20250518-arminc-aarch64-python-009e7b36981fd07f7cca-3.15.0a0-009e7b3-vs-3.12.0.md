# Results vs. 3.12.0

- fork: python
- ref: 009e7b36981fd07f7cca
- machine: linux-aarch64
- commit hash: 009e7b3
- commit date: 2025-05-18
- overall geometric mean: 1.028x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 299 ms: 1.03x faster                                                    |
| docutils       | 2.98 sec                                                              | 2.94 sec: 1.02x faster                                                  |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                            |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 461 ms: 1.68x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 868 ms: 1.63x faster                                                    |
| async_tree_none            | 624 ms                                                                | 392 ms: 1.59x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 467 ms: 1.59x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 903 ms: 1.55x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 373 ms: 1.55x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 649 ms: 1.41x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 654 ms: 1.35x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.54x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 86.4 ms: 1.07x faster                                                   |
| pidigits       | 233 ms                                                                | 238 ms: 1.02x slower                                                    |
| nbody          | 105 ms                                                                | 122 ms: 1.16x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.82 ms: 1.22x faster                                                   |
| regex_compile  | 137 ms                                                                | 122 ms: 1.12x faster                                                    |
| regex_dna      | 254 ms                                                                | 231 ms: 1.10x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.11x faster                                                            |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|---------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 178 ms: 1.10x faster                                                    |
| xml_etree_iterparse | 150 ms                                                                | 141 ms: 1.07x faster                                                    |
| tomli_loads         | 2.59 sec                                                              | 2.44 sec: 1.06x faster                                                  |
| unpickle            | 18.5 us                                                               | 18.2 us: 1.02x faster                                                   |
| xml_etree_process   | 79.0 ms                                                               | 79.3 ms: 1.00x slower                                                   |
| unpickle_list       | 6.17 us                                                               | 6.45 us: 1.05x slower                                                   |
| pickle_pure_python  | 365 us                                                                | 382 us: 1.05x slower                                                    |
| pickle_dict         | 37.3 us                                                               | 39.4 us: 1.06x slower                                                   |
| pickle_list         | 5.25 us                                                               | 5.58 us: 1.06x slower                                                   |
| json_dumps          | 12.3 ms                                                               | 13.6 ms: 1.11x slower                                                   |
| pickle              | 13.4 us                                                               | 15.2 us: 1.13x slower                                                   |
| json_loads          | 30.7 us                                                               | 36.0 us: 1.17x slower                                                   |
| Geometric mean      | (ref)                                                                 | 1.03x slower                                                            |

Benchmark hidden because not significant (2): unpickle_pure_python, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.62 ms: 1.03x slower                                                   |
| python_startup         | 11.4 ms                                                               | 15.1 ms: 1.33x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.17x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                               | 26.7 ms: 1.03x faster                                                   |
| mako           | 12.9 ms                                                               | 13.9 ms: 1.08x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                            |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.65 sec: 2.07x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 461 ms: 1.68x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 868 ms: 1.63x faster                                                    |
| async_tree_none            | 624 ms                                                                | 392 ms: 1.59x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 467 ms: 1.59x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 903 ms: 1.55x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 373 ms: 1.55x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 649 ms: 1.41x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 654 ms: 1.35x faster                                                    |
| deepcopy                   | 446 us                                                                | 333 us: 1.34x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 38.0 us: 1.31x faster                                                   |
| regex_effbot               | 4.64 ms                                                               | 3.82 ms: 1.22x faster                                                   |
| go                         | 157 ms                                                                | 131 ms: 1.20x faster                                                    |
| comprehensions             | 25.4 us                                                               | 21.2 us: 1.20x faster                                                   |
| generators                 | 43.5 ms                                                               | 37.5 ms: 1.16x faster                                                   |
| pylint                     | 355 ms                                                                | 307 ms: 1.16x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.58 us: 1.15x faster                                                   |
| dulwich_log                | 62.0 ms                                                               | 54.7 ms: 1.13x faster                                                   |
| regex_compile              | 137 ms                                                                | 122 ms: 1.12x faster                                                    |
| deltablue                  | 4.12 ms                                                               | 3.74 ms: 1.10x faster                                                   |
| regex_dna                  | 254 ms                                                                | 231 ms: 1.10x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 178 ms: 1.10x faster                                                    |
| raytrace                   | 353 ms                                                                | 322 ms: 1.10x faster                                                    |
| async_generators           | 491 ms                                                                | 449 ms: 1.09x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 22.8 ms: 1.07x faster                                                   |
| sympy_integrate            | 21.6 ms                                                               | 20.2 ms: 1.07x faster                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 141 ms: 1.07x faster                                                    |
| float                      | 92.1 ms                                                               | 86.4 ms: 1.07x faster                                                   |
| pyflate                    | 559 ms                                                                | 525 ms: 1.06x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.44 sec: 1.06x faster                                                  |
| sympy_sum                  | 154 ms                                                                | 147 ms: 1.05x faster                                                    |
| asyncio_tcp                | 566 ms                                                                | 539 ms: 1.05x faster                                                    |
| sympy_str                  | 280 ms                                                                | 270 ms: 1.04x faster                                                    |
| 2to3                       | 308 ms                                                                | 299 ms: 1.03x faster                                                    |
| genshi_text                | 27.4 ms                                                               | 26.7 ms: 1.03x faster                                                   |
| pprint_pformat             | 1.88 sec                                                              | 1.85 sec: 1.02x faster                                                  |
| unpickle                   | 18.5 us                                                               | 18.2 us: 1.02x faster                                                   |
| docutils                   | 2.98 sec                                                              | 2.94 sec: 1.02x faster                                                  |
| pprint_safe_repr           | 916 ms                                                                | 905 ms: 1.01x faster                                                    |
| richards                   | 50.9 ms                                                               | 50.5 ms: 1.01x faster                                                   |
| logging_format             | 8.34 us                                                               | 8.27 us: 1.01x faster                                                   |
| xml_etree_process          | 79.0 ms                                                               | 79.3 ms: 1.00x slower                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.20 sec: 1.01x slower                                                  |
| coroutines                 | 29.0 ms                                                               | 29.5 ms: 1.02x slower                                                   |
| asyncio_websockets         | 658 ms                                                                | 669 ms: 1.02x slower                                                    |
| meteor_contest             | 112 ms                                                                | 114 ms: 1.02x slower                                                    |
| pidigits                   | 233 ms                                                                | 238 ms: 1.02x slower                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.35 ms: 1.03x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.62 ms: 1.03x slower                                                   |
| sympy_expand               | 454 ms                                                                | 469 ms: 1.03x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 3.94 us: 1.04x slower                                                   |
| unpickle_list              | 6.17 us                                                               | 6.45 us: 1.05x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 382 us: 1.05x slower                                                    |
| scimark_fft                | 418 ms                                                                | 439 ms: 1.05x slower                                                    |
| fannkuch                   | 443 ms                                                                | 466 ms: 1.05x slower                                                    |
| pickle_dict                | 37.3 us                                                               | 39.4 us: 1.06x slower                                                   |
| pickle_list                | 5.25 us                                                               | 5.58 us: 1.06x slower                                                   |
| mako                       | 12.9 ms                                                               | 13.9 ms: 1.08x slower                                                   |
| json                       | 5.54 ms                                                               | 6.11 ms: 1.10x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 13.6 ms: 1.11x slower                                                   |
| telco                      | 8.51 ms                                                               | 9.57 ms: 1.12x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 203 us: 1.13x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.99 ms: 1.13x slower                                                   |
| pickle                     | 13.4 us                                                               | 15.2 us: 1.13x slower                                                   |
| nbody                      | 105 ms                                                                | 122 ms: 1.16x slower                                                    |
| json_loads                 | 30.7 us                                                               | 36.0 us: 1.17x slower                                                   |
| python_startup             | 11.4 ms                                                               | 15.1 ms: 1.33x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 6.82 ms: 1.55x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 3.76 ms: 1.96x slower                                                   |
| logging_silent             | 127 ns                                                                | 604 ns: 4.76x slower                                                    |
| coverage                   | 87.3 ms                                                               | 548 ms: 6.28x slower                                                    |
| thrift                     | 937 us                                                                | 197 ms: 209.99x slower                                                  |
| bench_mp_pool              | 7.05 ms                                                               | 4.22 sec: 598.53x slower                                                |
| Geometric mean             | (ref)                                                                 | 1.13x slower                                                            |

Benchmark hidden because not significant (17): html5lib, django_template, scimark_monte_carlo, scimark_sor, richards_super, chaos, logging_simple, crypto_pyaes, spectral_norm, genshi_xml, regex_v8, pycparser, unpickle_pure_python, scimark_lu, xml_etree_generate, nqueens, hexiom
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250518-3.15.0a0-009e7b3/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.028x slower

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.09x