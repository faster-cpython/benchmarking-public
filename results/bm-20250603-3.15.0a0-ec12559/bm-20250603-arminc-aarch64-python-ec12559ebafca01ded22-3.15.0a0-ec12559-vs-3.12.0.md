# Results vs. 3.12.0

- fork: python
- ref: ec12559ebafca01ded22
- machine: linux-aarch64
- commit hash: ec12559
- commit date: 2025-06-03
- overall geometric mean: 1.028x slower
- HPT reliability: 99.91%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250603-arminc-aarch64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 300 ms: 1.03x faster                                                    |
| docutils       | 2.98 sec                                                              | 2.91 sec: 1.02x faster                                                  |
| html5lib       | 65.1 ms                                                               | 60.8 ms: 1.07x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.04x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250603-arminc-aarch64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 465 ms: 1.67x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 870 ms: 1.62x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 464 ms: 1.59x faster                                                    |
| async_tree_none            | 624 ms                                                                | 394 ms: 1.58x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 373 ms: 1.55x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 909 ms: 1.55x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 659 ms: 1.38x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 649 ms: 1.36x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.53x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250603-arminc-aarch64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 86.8 ms: 1.06x faster                                                   |
| pidigits       | 233 ms                                                                | 239 ms: 1.03x slower                                                    |
| nbody          | 105 ms                                                                | 119 ms: 1.14x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250603-arminc-aarch64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.80 ms: 1.22x faster                                                   |
| regex_compile  | 137 ms                                                                | 124 ms: 1.11x faster                                                    |
| regex_dna      | 254 ms                                                                | 235 ms: 1.08x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.09x faster                                                            |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250603-arminc-aarch64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|---------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 181 ms: 1.08x faster                                                    |
| xml_etree_iterparse | 150 ms                                                                | 142 ms: 1.06x faster                                                    |
| tomli_loads         | 2.59 sec                                                              | 2.50 sec: 1.04x faster                                                  |
| xml_etree_process   | 79.0 ms                                                               | 79.5 ms: 1.01x slower                                                   |
| json_loads          | 30.7 us                                                               | 33.0 us: 1.08x slower                                                   |
| pickle_pure_python  | 365 us                                                                | 395 us: 1.08x slower                                                    |
| json_dumps          | 12.3 ms                                                               | 13.6 ms: 1.11x slower                                                   |
| Geometric mean      | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (2): xml_etree_generate, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250603-arminc-aarch64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.62 ms: 1.03x slower                                                   |
| python_startup         | 11.4 ms                                                               | 15.1 ms: 1.33x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.17x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250603-arminc-aarch64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml     | 60.6 ms                                                               | 62.3 ms: 1.03x slower                                                   |
| mako           | 12.9 ms                                                               | 13.7 ms: 1.06x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250603-arminc-aarch64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.68 sec: 2.03x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 465 ms: 1.67x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 870 ms: 1.62x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 464 ms: 1.59x faster                                                    |
| async_tree_none            | 624 ms                                                                | 394 ms: 1.58x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 373 ms: 1.55x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 909 ms: 1.55x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 659 ms: 1.38x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 649 ms: 1.36x faster                                                    |
| deepcopy                   | 446 us                                                                | 330 us: 1.35x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 38.2 us: 1.30x faster                                                   |
| comprehensions             | 25.4 us                                                               | 20.4 us: 1.25x faster                                                   |
| generators                 | 43.5 ms                                                               | 35.6 ms: 1.22x faster                                                   |
| regex_effbot               | 4.64 ms                                                               | 3.80 ms: 1.22x faster                                                   |
| go                         | 157 ms                                                                | 129 ms: 1.22x faster                                                    |
| dulwich_log                | 62.0 ms                                                               | 52.3 ms: 1.19x faster                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 3.60 us: 1.14x faster                                                   |
| pylint                     | 355 ms                                                                | 318 ms: 1.12x faster                                                    |
| regex_compile              | 137 ms                                                                | 124 ms: 1.11x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 22.6 ms: 1.09x faster                                                   |
| sympy_sum                  | 154 ms                                                                | 143 ms: 1.08x faster                                                    |
| regex_dna                  | 254 ms                                                                | 235 ms: 1.08x faster                                                    |
| raytrace                   | 353 ms                                                                | 327 ms: 1.08x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 181 ms: 1.08x faster                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 79.0 ms: 1.08x faster                                                   |
| sympy_integrate            | 21.6 ms                                                               | 20.2 ms: 1.07x faster                                                   |
| html5lib                   | 65.1 ms                                                               | 60.8 ms: 1.07x faster                                                   |
| sympy_str                  | 280 ms                                                                | 262 ms: 1.07x faster                                                    |
| async_generators           | 491 ms                                                                | 461 ms: 1.06x faster                                                    |
| float                      | 92.1 ms                                                               | 86.8 ms: 1.06x faster                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 142 ms: 1.06x faster                                                    |
| scimark_sor                | 150 ms                                                                | 144 ms: 1.04x faster                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 83.4 ms: 1.04x faster                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.50 sec: 1.04x faster                                                  |
| chaos                      | 71.4 ms                                                               | 69.1 ms: 1.03x faster                                                   |
| 2to3                       | 308 ms                                                                | 300 ms: 1.03x faster                                                    |
| docutils                   | 2.98 sec                                                              | 2.91 sec: 1.02x faster                                                  |
| pyflate                    | 559 ms                                                                | 550 ms: 1.02x faster                                                    |
| xml_etree_process          | 79.0 ms                                                               | 79.5 ms: 1.01x slower                                                   |
| logging_simple             | 7.63 us                                                               | 7.69 us: 1.01x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 1.28 sec: 1.02x slower                                                  |
| logging_format             | 8.34 us                                                               | 8.49 us: 1.02x slower                                                   |
| asyncio_websockets         | 658 ms                                                                | 669 ms: 1.02x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 3.86 us: 1.02x slower                                                   |
| pidigits                   | 233 ms                                                                | 239 ms: 1.03x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 62.3 ms: 1.03x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.62 ms: 1.03x slower                                                   |
| sympy_expand               | 454 ms                                                                | 469 ms: 1.03x slower                                                    |
| scimark_fft                | 418 ms                                                                | 435 ms: 1.04x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 152 ms: 1.04x slower                                                    |
| json                       | 5.54 ms                                                               | 5.79 ms: 1.05x slower                                                   |
| fannkuch                   | 443 ms                                                                | 465 ms: 1.05x slower                                                    |
| mako                       | 12.9 ms                                                               | 13.7 ms: 1.06x slower                                                   |
| json_loads                 | 30.7 us                                                               | 33.0 us: 1.08x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 2.03 sec: 1.08x slower                                                  |
| telco                      | 8.51 ms                                                               | 9.18 ms: 1.08x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 395 us: 1.08x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 196 us: 1.09x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 1.00 sec: 1.09x slower                                                  |
| json_dumps                 | 12.3 ms                                                               | 13.6 ms: 1.11x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.95 ms: 1.12x slower                                                   |
| nbody                      | 105 ms                                                                | 119 ms: 1.14x slower                                                    |
| python_startup             | 11.4 ms                                                               | 15.1 ms: 1.33x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 6.97 ms: 1.59x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 3.68 ms: 1.92x slower                                                   |
| logging_silent             | 127 ns                                                                | 639 ns: 5.04x slower                                                    |
| coverage                   | 87.3 ms                                                               | 555 ms: 6.35x slower                                                    |
| thrift                     | 937 us                                                                | 197 ms: 210.16x slower                                                  |
| Geometric mean             | (ref)                                                                 | 1.06x slower                                                            |

Benchmark hidden because not significant (13): deltablue, genshi_text, spectral_norm, xml_etree_generate, hexiom, django_template, nqueens, unpickle_pure_python, richards_super, regex_v8, meteor_contest, coroutines, richards
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250603-3.15.0a0-ec12559/bm-20250603-arminc-aarch64-python-ec12559ebafca01ded22-3.15.0a0-ec12559.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.028x slower

# HPT report

- Reliability score: 99.91% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.09x