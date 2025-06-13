# Results vs. 3.12.0

- fork: python
- ref: afc5ab6cce9d7095b99c
- machine: linux-aarch64
- commit hash: afc5ab6
- commit date: 2025-06-13
- overall geometric mean: 1.025x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250613-arminc-aarch64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 302 ms: 1.02x faster                                                    |
| docutils       | 2.98 sec                                                              | 2.89 sec: 1.03x faster                                                  |
| html5lib       | 65.1 ms                                                               | 61.0 ms: 1.07x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.04x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250613-arminc-aarch64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 472 ms: 1.65x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 463 ms: 1.60x faster                                                    |
| async_tree_none            | 624 ms                                                                | 394 ms: 1.58x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 903 ms: 1.55x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 908 ms: 1.55x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 379 ms: 1.52x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 657 ms: 1.39x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 649 ms: 1.36x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.52x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250613-arminc-aarch64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 85.6 ms: 1.08x faster                                                   |
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 124 ms: 1.19x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250613-arminc-aarch64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.84 ms: 1.21x faster                                                   |
| regex_dna      | 254 ms                                                                | 225 ms: 1.13x faster                                                    |
| regex_compile  | 137 ms                                                                | 124 ms: 1.11x faster                                                    |
| regex_v8       | 28.3 ms                                                               | 26.3 ms: 1.08x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.13x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250613-arminc-aarch64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|---------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 181 ms: 1.08x faster                                                    |
| xml_etree_iterparse | 150 ms                                                                | 141 ms: 1.06x faster                                                    |
| tomli_loads         | 2.59 sec                                                              | 2.48 sec: 1.05x faster                                                  |
| xml_etree_generate  | 112 ms                                                                | 110 ms: 1.02x faster                                                    |
| pickle_pure_python  | 365 us                                                                | 383 us: 1.05x slower                                                    |
| json_loads          | 30.7 us                                                               | 32.4 us: 1.06x slower                                                   |
| json_dumps          | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                   |
| Geometric mean      | (ref)                                                                 | 1.00x slower                                                            |

Benchmark hidden because not significant (2): unpickle_pure_python, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250613-arminc-aarch64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.63 ms: 1.03x slower                                                   |
| python_startup         | 11.4 ms                                                               | 15.0 ms: 1.32x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.17x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250613-arminc-aarch64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 39.2 ms: 1.04x faster                                                   |
| mako            | 12.9 ms                                                               | 13.8 ms: 1.07x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250613-arminc-aarch64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.69 sec: 2.02x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 472 ms: 1.65x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 463 ms: 1.60x faster                                                    |
| async_tree_none            | 624 ms                                                                | 394 ms: 1.58x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 903 ms: 1.55x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 908 ms: 1.55x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 379 ms: 1.52x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 657 ms: 1.39x faster                                                    |
| deepcopy                   | 446 us                                                                | 325 us: 1.37x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 649 ms: 1.36x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 37.9 us: 1.31x faster                                                   |
| comprehensions             | 25.4 us                                                               | 20.2 us: 1.26x faster                                                   |
| generators                 | 43.5 ms                                                               | 35.2 ms: 1.24x faster                                                   |
| dulwich_log                | 62.0 ms                                                               | 50.3 ms: 1.23x faster                                                   |
| go                         | 157 ms                                                                | 128 ms: 1.23x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 3.84 ms: 1.21x faster                                                   |
| pylint                     | 355 ms                                                                | 313 ms: 1.13x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.63 us: 1.13x faster                                                   |
| regex_dna                  | 254 ms                                                                | 225 ms: 1.13x faster                                                    |
| regex_compile              | 137 ms                                                                | 124 ms: 1.11x faster                                                    |
| async_generators           | 491 ms                                                                | 447 ms: 1.10x faster                                                    |
| raytrace                   | 353 ms                                                                | 326 ms: 1.08x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 143 ms: 1.08x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 181 ms: 1.08x faster                                                    |
| regex_v8                   | 28.3 ms                                                               | 26.3 ms: 1.08x faster                                                   |
| float                      | 92.1 ms                                                               | 85.6 ms: 1.08x faster                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 79.3 ms: 1.07x faster                                                   |
| html5lib                   | 65.1 ms                                                               | 61.0 ms: 1.07x faster                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 141 ms: 1.06x faster                                                    |
| pyflate                    | 559 ms                                                                | 525 ms: 1.06x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 23.1 ms: 1.06x faster                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 82.7 ms: 1.05x faster                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.48 sec: 1.05x faster                                                  |
| sympy_integrate            | 21.6 ms                                                               | 20.8 ms: 1.04x faster                                                   |
| django_template            | 40.7 ms                                                               | 39.2 ms: 1.04x faster                                                   |
| docutils                   | 2.98 sec                                                              | 2.89 sec: 1.03x faster                                                  |
| pycparser                  | 1.26 sec                                                              | 1.23 sec: 1.03x faster                                                  |
| 2to3                       | 308 ms                                                                | 302 ms: 1.02x faster                                                    |
| xml_etree_generate         | 112 ms                                                                | 110 ms: 1.02x faster                                                    |
| logging_simple             | 7.63 us                                                               | 7.50 us: 1.02x faster                                                   |
| logging_format             | 8.34 us                                                               | 8.27 us: 1.01x faster                                                   |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 148 ms: 1.02x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 672 ms: 1.02x slower                                                    |
| json                       | 5.54 ms                                                               | 5.67 ms: 1.02x slower                                                   |
| sympy_expand               | 454 ms                                                                | 465 ms: 1.03x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 8.63 ms: 1.03x slower                                                   |
| scimark_fft                | 418 ms                                                                | 438 ms: 1.05x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 383 us: 1.05x slower                                                    |
| json_loads                 | 30.7 us                                                               | 32.4 us: 1.06x slower                                                   |
| mako                       | 12.9 ms                                                               | 13.8 ms: 1.07x slower                                                   |
| fannkuch                   | 443 ms                                                                | 477 ms: 1.08x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 197 us: 1.09x slower                                                    |
| telco                      | 8.51 ms                                                               | 9.31 ms: 1.09x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 2.07 sec: 1.10x slower                                                  |
| json_dumps                 | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                   |
| pprint_safe_repr           | 916 ms                                                                | 1.02 sec: 1.11x slower                                                  |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.99 ms: 1.13x slower                                                   |
| nbody                      | 105 ms                                                                | 124 ms: 1.19x slower                                                    |
| python_startup             | 11.4 ms                                                               | 15.0 ms: 1.32x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 6.86 ms: 1.56x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 3.71 ms: 1.93x slower                                                   |
| logging_silent             | 127 ns                                                                | 629 ns: 4.96x slower                                                    |
| coverage                   | 87.3 ms                                                               | 545 ms: 6.24x slower                                                    |
| thrift                     | 937 us                                                                | 194 ms: 206.80x slower                                                  |
| Geometric mean             | (ref)                                                                 | 1.05x slower                                                            |

Benchmark hidden because not significant (16): deltablue, sympy_str, spectral_norm, scimark_sor, chaos, meteor_contest, sqlite_synth, genshi_text, unpickle_pure_python, xml_etree_process, nqueens, genshi_xml, hexiom, richards_super, coroutines, richards
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250613-3.15.0a0-afc5ab6/bm-20250613-arminc-aarch64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.025x slower

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.10x