# Results vs. 3.12.0

- fork: python
- ref: a852c7bdd48979218a0c
- machine: linux-aarch64
- commit hash: a852c7b
- commit date: 2025-07-26
- overall geometric mean: 1.036x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 301 ms: 1.02x faster                                                    |
| html5lib       | 65.1 ms                                                               | 61.5 ms: 1.06x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                            |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 459 ms: 1.69x faster                                                    |
| async_tree_none            | 624 ms                                                                | 381 ms: 1.64x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 866 ms: 1.63x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 456 ms: 1.62x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 900 ms: 1.56x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 373 ms: 1.54x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 655 ms: 1.39x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 646 ms: 1.37x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.55x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 85.6 ms: 1.08x faster                                                   |
| pidigits       | 233 ms                                                                | 237 ms: 1.02x slower                                                    |
| nbody          | 105 ms                                                                | 125 ms: 1.19x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.83 ms: 1.21x faster                                                   |
| regex_dna      | 254 ms                                                                | 223 ms: 1.14x faster                                                    |
| regex_compile  | 137 ms                                                                | 124 ms: 1.11x faster                                                    |
| regex_v8       | 28.3 ms                                                               | 27.2 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.12x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|---------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 180 ms: 1.08x faster                                                    |
| tomli_loads         | 2.59 sec                                                              | 2.44 sec: 1.06x faster                                                  |
| xml_etree_iterparse | 150 ms                                                                | 142 ms: 1.06x faster                                                    |
| xml_etree_generate  | 112 ms                                                                | 113 ms: 1.01x slower                                                    |
| xml_etree_process   | 79.0 ms                                                               | 80.1 ms: 1.01x slower                                                   |
| unpickle_list       | 6.17 us                                                               | 6.59 us: 1.07x slower                                                   |
| pickle_pure_python  | 365 us                                                                | 391 us: 1.07x slower                                                    |
| json_loads          | 30.7 us                                                               | 33.1 us: 1.08x slower                                                   |
| pickle_list         | 5.25 us                                                               | 5.71 us: 1.09x slower                                                   |
| json_dumps          | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                   |
| pickle              | 13.4 us                                                               | 15.6 us: 1.17x slower                                                   |
| Geometric mean      | (ref)                                                                 | 1.03x slower                                                            |

Benchmark hidden because not significant (3): unpickle, unpickle_pure_python, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.54 ms: 1.02x slower                                                   |
| python_startup         | 11.4 ms                                                               | 15.0 ms: 1.32x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.16x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 39.2 ms: 1.04x faster                                                   |
| mako            | 12.9 ms                                                               | 13.7 ms: 1.06x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.64 sec: 2.08x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 459 ms: 1.69x faster                                                    |
| async_tree_none            | 624 ms                                                                | 381 ms: 1.64x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 866 ms: 1.63x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 456 ms: 1.62x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 900 ms: 1.56x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 373 ms: 1.54x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 655 ms: 1.39x faster                                                    |
| deepcopy                   | 446 us                                                                | 325 us: 1.37x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 646 ms: 1.37x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 37.4 us: 1.33x faster                                                   |
| comprehensions             | 25.4 us                                                               | 19.8 us: 1.28x faster                                                   |
| go                         | 157 ms                                                                | 126 ms: 1.25x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 3.83 ms: 1.21x faster                                                   |
| generators                 | 43.5 ms                                                               | 35.9 ms: 1.21x faster                                                   |
| dulwich_log                | 62.0 ms                                                               | 51.3 ms: 1.21x faster                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 3.56 us: 1.15x faster                                                   |
| regex_dna                  | 254 ms                                                                | 223 ms: 1.14x faster                                                    |
| pylint                     | 355 ms                                                                | 316 ms: 1.12x faster                                                    |
| logging_simple             | 7.63 us                                                               | 6.86 us: 1.11x faster                                                   |
| regex_compile              | 137 ms                                                                | 124 ms: 1.11x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.57 us: 1.10x faster                                                   |
| sympy_integrate            | 21.6 ms                                                               | 19.9 ms: 1.09x faster                                                   |
| async_generators           | 491 ms                                                                | 453 ms: 1.08x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 180 ms: 1.08x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 22.7 ms: 1.08x faster                                                   |
| raytrace                   | 353 ms                                                                | 327 ms: 1.08x faster                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 78.8 ms: 1.08x faster                                                   |
| float                      | 92.1 ms                                                               | 85.6 ms: 1.08x faster                                                   |
| pyflate                    | 559 ms                                                                | 527 ms: 1.06x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.44 sec: 1.06x faster                                                  |
| spectral_norm              | 131 ms                                                                | 123 ms: 1.06x faster                                                    |
| html5lib                   | 65.1 ms                                                               | 61.5 ms: 1.06x faster                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 142 ms: 1.06x faster                                                    |
| chaos                      | 71.4 ms                                                               | 67.7 ms: 1.05x faster                                                   |
| sympy_sum                  | 154 ms                                                                | 147 ms: 1.05x faster                                                    |
| regex_v8                   | 28.3 ms                                                               | 27.2 ms: 1.04x faster                                                   |
| scimark_sor                | 150 ms                                                                | 143 ms: 1.04x faster                                                    |
| asyncio_tcp                | 566 ms                                                                | 545 ms: 1.04x faster                                                    |
| django_template            | 40.7 ms                                                               | 39.2 ms: 1.04x faster                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 83.6 ms: 1.04x faster                                                   |
| pprint_pformat             | 1.88 sec                                                              | 1.82 sec: 1.03x faster                                                  |
| deltablue                  | 4.12 ms                                                               | 3.99 ms: 1.03x faster                                                   |
| pprint_safe_repr           | 916 ms                                                                | 894 ms: 1.02x faster                                                    |
| hexiom                     | 6.98 ms                                                               | 6.81 ms: 1.02x faster                                                   |
| 2to3                       | 308 ms                                                                | 301 ms: 1.02x faster                                                    |
| xml_etree_generate         | 112 ms                                                                | 113 ms: 1.01x slower                                                    |
| xml_etree_process          | 79.0 ms                                                               | 80.1 ms: 1.01x slower                                                   |
| thrift                     | 937 us                                                                | 954 us: 1.02x slower                                                    |
| pidigits                   | 233 ms                                                                | 237 ms: 1.02x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 671 ms: 1.02x slower                                                    |
| coroutines                 | 29.0 ms                                                               | 29.6 ms: 1.02x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.54 ms: 1.02x slower                                                   |
| fannkuch                   | 443 ms                                                                | 463 ms: 1.04x slower                                                    |
| richards                   | 50.9 ms                                                               | 53.2 ms: 1.04x slower                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.37 ms: 1.04x slower                                                   |
| sympy_expand               | 454 ms                                                                | 476 ms: 1.05x slower                                                    |
| json                       | 5.54 ms                                                               | 5.84 ms: 1.05x slower                                                   |
| mako                       | 12.9 ms                                                               | 13.7 ms: 1.06x slower                                                   |
| scimark_lu                 | 146 ms                                                                | 155 ms: 1.07x slower                                                    |
| unpickle_list              | 6.17 us                                                               | 6.59 us: 1.07x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 391 us: 1.07x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 194 us: 1.07x slower                                                    |
| json_loads                 | 30.7 us                                                               | 33.1 us: 1.08x slower                                                   |
| pickle_list                | 5.25 us                                                               | 5.71 us: 1.09x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.19 ms: 1.16x slower                                                   |
| pickle                     | 13.4 us                                                               | 15.6 us: 1.17x slower                                                   |
| coverage                   | 87.3 ms                                                               | 102 ms: 1.17x slower                                                    |
| nbody                      | 105 ms                                                                | 125 ms: 1.19x slower                                                    |
| python_startup             | 11.4 ms                                                               | 15.0 ms: 1.32x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 6.78 ms: 1.54x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 3.76 ms: 1.96x slower                                                   |
| telco                      | 8.51 ms                                                               | 163 ms: 19.18x slower                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 2.17 sec: 307.55x slower                                                |
| Geometric mean             | (ref)                                                                 | 1.04x slower                                                            |

Benchmark hidden because not significant (15): sympy_str, meteor_contest, nqueens, pycparser, unpickle, docutils, sqlite_synth, asyncio_tcp_ssl, richards_super, scimark_fft, unpickle_pure_python, pickle_dict, genshi_text, genshi_xml, logging_silent
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.036x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.11x