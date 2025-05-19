# Results vs. 3.12.0

- fork: python
- ref: 605022aeb69ae19cae1c
- machine: linux-aarch64
- commit hash: 605022a
- commit date: 2025-05-19
- overall geometric mean: 1.033x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250519-arminc-aarch64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| html5lib       | 65.1 ms                                                               | 62.1 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                            |

Benchmark hidden because not significant (2): 2to3, docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250519-arminc-aarch64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 470 ms: 1.65x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 465 ms: 1.59x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 888 ms: 1.59x faster                                                    |
| async_tree_none            | 624 ms                                                                | 395 ms: 1.58x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 910 ms: 1.54x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 376 ms: 1.53x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 663 ms: 1.38x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 656 ms: 1.35x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.52x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250519-arminc-aarch64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 86.9 ms: 1.06x faster                                                   |
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 122 ms: 1.16x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250519-arminc-aarch64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.81 ms: 1.22x faster                                                   |
| regex_compile  | 137 ms                                                                | 123 ms: 1.12x faster                                                    |
| regex_dna      | 254 ms                                                                | 236 ms: 1.08x faster                                                    |
| regex_v8       | 28.3 ms                                                               | 27.9 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.10x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250519-arminc-aarch64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|---------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 179 ms: 1.09x faster                                                    |
| tomli_loads         | 2.59 sec                                                              | 2.43 sec: 1.07x faster                                                  |
| xml_etree_iterparse | 150 ms                                                                | 143 ms: 1.06x faster                                                    |
| xml_etree_process   | 79.0 ms                                                               | 79.2 ms: 1.00x slower                                                   |
| json_dumps          | 12.3 ms                                                               | 13.4 ms: 1.09x slower                                                   |
| pickle_pure_python  | 365 us                                                                | 400 us: 1.10x slower                                                    |
| json_loads          | 30.7 us                                                               | 35.2 us: 1.15x slower                                                   |
| Geometric mean      | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (2): xml_etree_generate, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250519-arminc-aarch64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.64 ms: 1.03x slower                                                   |
| python_startup         | 11.4 ms                                                               | 15.1 ms: 1.33x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.17x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250519-arminc-aarch64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 12.9 ms                                                               | 14.0 ms: 1.08x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (3): django_template, genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250519-arminc-aarch64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.65 sec: 2.07x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 470 ms: 1.65x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 465 ms: 1.59x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 888 ms: 1.59x faster                                                    |
| async_tree_none            | 624 ms                                                                | 395 ms: 1.58x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 910 ms: 1.54x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 376 ms: 1.53x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 663 ms: 1.38x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 656 ms: 1.35x faster                                                    |
| deepcopy                   | 446 us                                                                | 336 us: 1.32x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 37.7 us: 1.32x faster                                                   |
| regex_effbot               | 4.64 ms                                                               | 3.81 ms: 1.22x faster                                                   |
| generators                 | 43.5 ms                                                               | 36.3 ms: 1.20x faster                                                   |
| comprehensions             | 25.4 us                                                               | 21.2 us: 1.19x faster                                                   |
| go                         | 157 ms                                                                | 132 ms: 1.19x faster                                                    |
| dulwich_log                | 62.0 ms                                                               | 53.2 ms: 1.17x faster                                                   |
| pylint                     | 355 ms                                                                | 313 ms: 1.13x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.66 us: 1.12x faster                                                   |
| regex_compile              | 137 ms                                                                | 123 ms: 1.12x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 179 ms: 1.09x faster                                                    |
| deltablue                  | 4.12 ms                                                               | 3.79 ms: 1.09x faster                                                   |
| sympy_sum                  | 154 ms                                                                | 143 ms: 1.08x faster                                                    |
| regex_dna                  | 254 ms                                                                | 236 ms: 1.08x faster                                                    |
| raytrace                   | 353 ms                                                                | 328 ms: 1.08x faster                                                    |
| async_generators           | 491 ms                                                                | 456 ms: 1.08x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.43 sec: 1.07x faster                                                  |
| pathlib                    | 24.5 ms                                                               | 23.1 ms: 1.06x faster                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 80.2 ms: 1.06x faster                                                   |
| float                      | 92.1 ms                                                               | 86.9 ms: 1.06x faster                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 143 ms: 1.06x faster                                                    |
| sympy_integrate            | 21.6 ms                                                               | 20.6 ms: 1.05x faster                                                   |
| pyflate                    | 559 ms                                                                | 532 ms: 1.05x faster                                                    |
| html5lib                   | 65.1 ms                                                               | 62.1 ms: 1.05x faster                                                   |
| spectral_norm              | 131 ms                                                                | 128 ms: 1.02x faster                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 84.7 ms: 1.02x faster                                                   |
| regex_v8                   | 28.3 ms                                                               | 27.9 ms: 1.02x faster                                                   |
| pprint_pformat             | 1.88 sec                                                              | 1.85 sec: 1.02x faster                                                  |
| xml_etree_process          | 79.0 ms                                                               | 79.2 ms: 1.00x slower                                                   |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| sympy_expand               | 454 ms                                                                | 468 ms: 1.03x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 8.64 ms: 1.03x slower                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.35 ms: 1.03x slower                                                   |
| scimark_fft                | 418 ms                                                                | 439 ms: 1.05x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 3.97 us: 1.05x slower                                                   |
| fannkuch                   | 443 ms                                                                | 467 ms: 1.05x slower                                                    |
| mako                       | 12.9 ms                                                               | 14.0 ms: 1.08x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 13.4 ms: 1.09x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 400 us: 1.10x slower                                                    |
| json                       | 5.54 ms                                                               | 6.07 ms: 1.10x slower                                                   |
| telco                      | 8.51 ms                                                               | 9.39 ms: 1.10x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 202 us: 1.12x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.00 ms: 1.13x slower                                                   |
| json_loads                 | 30.7 us                                                               | 35.2 us: 1.15x slower                                                   |
| nbody                      | 105 ms                                                                | 122 ms: 1.16x slower                                                    |
| python_startup             | 11.4 ms                                                               | 15.1 ms: 1.33x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 7.17 ms: 1.63x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 3.95 ms: 2.06x slower                                                   |
| logging_silent             | 127 ns                                                                | 612 ns: 4.82x slower                                                    |
| coverage                   | 87.3 ms                                                               | 559 ms: 6.40x slower                                                    |
| thrift                     | 937 us                                                                | 194 ms: 207.13x slower                                                  |
| bench_mp_pool              | 7.05 ms                                                               | 2.60 sec: 368.63x slower                                                |
| Geometric mean             | (ref)                                                                 | 1.14x slower                                                            |

Benchmark hidden because not significant (22): django_template, chaos, sympy_str, 2to3, pycparser, scimark_sor, xml_etree_generate, richards_super, pprint_safe_repr, docutils, hexiom, scimark_lu, logging_format, logging_simple, unpickle_pure_python, genshi_text, nqueens, asyncio_websockets, richards, genshi_xml, meteor_contest, coroutines
Ignored benchmarks (19) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250519-3.15.0a0-605022a/bm-20250519-arminc-aarch64-python-605022aeb69ae19cae1c-3.15.0a0-605022a.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.033x slower

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.08x