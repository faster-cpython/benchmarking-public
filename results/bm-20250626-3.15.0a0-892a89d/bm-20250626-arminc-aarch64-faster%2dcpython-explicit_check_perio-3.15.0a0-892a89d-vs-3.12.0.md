# Results vs. 3.12.0

- fork: faster-cpython
- ref: explicit_check_perio
- machine: linux-aarch64
- commit hash: 892a89d
- commit date: 2025-06-26
- overall geometric mean: 1.056x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250626-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| html5lib       | 65.1 ms                                                               | 62.9 ms: 1.03x faster                                                             |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                      |

Benchmark hidden because not significant (2): 2to3, docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250626-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 471 ms: 1.65x faster                                                              |
| async_tree_memoization_tg  | 740 ms                                                                | 467 ms: 1.59x faster                                                              |
| async_tree_none            | 624 ms                                                                | 394 ms: 1.58x faster                                                              |
| async_tree_io              | 1.41 sec                                                              | 901 ms: 1.57x faster                                                              |
| async_tree_io_tg           | 1.40 sec                                                              | 908 ms: 1.55x faster                                                              |
| async_tree_none_tg         | 577 ms                                                                | 380 ms: 1.52x faster                                                              |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 664 ms: 1.37x faster                                                              |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 648 ms: 1.36x faster                                                              |
| Geometric mean             | (ref)                                                                 | 1.52x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250626-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 87.3 ms: 1.05x faster                                                             |
| pidigits       | 233 ms                                                                | 238 ms: 1.02x slower                                                              |
| nbody          | 105 ms                                                                | 122 ms: 1.17x slower                                                              |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250626-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.92 ms: 1.18x faster                                                             |
| regex_dna      | 254 ms                                                                | 220 ms: 1.16x faster                                                              |
| regex_compile  | 137 ms                                                                | 123 ms: 1.11x faster                                                              |
| regex_v8       | 28.3 ms                                                               | 27.1 ms: 1.05x faster                                                             |
| Geometric mean | (ref)                                                                 | 1.12x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250626-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|---------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 182 ms: 1.07x faster                                                              |
| xml_etree_iterparse | 150 ms                                                                | 141 ms: 1.06x faster                                                              |
| tomli_loads         | 2.59 sec                                                              | 2.47 sec: 1.05x faster                                                            |
| xml_etree_generate  | 112 ms                                                                | 111 ms: 1.01x faster                                                              |
| json_loads          | 30.7 us                                                               | 32.4 us: 1.06x slower                                                             |
| pickle_pure_python  | 365 us                                                                | 387 us: 1.06x slower                                                              |
| json_dumps          | 12.3 ms                                                               | 13.7 ms: 1.12x slower                                                             |
| Geometric mean      | (ref)                                                                 | 1.01x slower                                                                      |

Benchmark hidden because not significant (2): unpickle_pure_python, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250626-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.62 ms: 1.03x slower                                                             |
| python_startup         | 11.4 ms                                                               | 15.1 ms: 1.33x slower                                                             |
| Geometric mean         | (ref)                                                                 | 1.17x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250626-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                               | 26.6 ms: 1.03x faster                                                             |
| mako           | 12.9 ms                                                               | 14.3 ms: 1.11x slower                                                             |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                                      |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250626-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.68 sec: 2.04x faster                                                            |
| async_tree_memoization     | 777 ms                                                                | 471 ms: 1.65x faster                                                              |
| async_tree_memoization_tg  | 740 ms                                                                | 467 ms: 1.59x faster                                                              |
| async_tree_none            | 624 ms                                                                | 394 ms: 1.58x faster                                                              |
| async_tree_io              | 1.41 sec                                                              | 901 ms: 1.57x faster                                                              |
| async_tree_io_tg           | 1.40 sec                                                              | 908 ms: 1.55x faster                                                              |
| async_tree_none_tg         | 577 ms                                                                | 380 ms: 1.52x faster                                                              |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 664 ms: 1.37x faster                                                              |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 648 ms: 1.36x faster                                                              |
| deepcopy                   | 446 us                                                                | 341 us: 1.31x faster                                                              |
| deepcopy_memo              | 49.6 us                                                               | 38.3 us: 1.30x faster                                                             |
| comprehensions             | 25.4 us                                                               | 20.1 us: 1.26x faster                                                             |
| go                         | 157 ms                                                                | 127 ms: 1.24x faster                                                              |
| dulwich_log                | 62.0 ms                                                               | 52.4 ms: 1.18x faster                                                             |
| regex_effbot               | 4.64 ms                                                               | 3.92 ms: 1.18x faster                                                             |
| generators                 | 43.5 ms                                                               | 37.2 ms: 1.17x faster                                                             |
| regex_dna                  | 254 ms                                                                | 220 ms: 1.16x faster                                                              |
| deepcopy_reduce            | 4.10 us                                                               | 3.58 us: 1.15x faster                                                             |
| pylint                     | 355 ms                                                                | 316 ms: 1.12x faster                                                              |
| regex_compile              | 137 ms                                                                | 123 ms: 1.11x faster                                                              |
| async_generators           | 491 ms                                                                | 452 ms: 1.09x faster                                                              |
| xml_etree_parse            | 195 ms                                                                | 182 ms: 1.07x faster                                                              |
| spectral_norm              | 131 ms                                                                | 122 ms: 1.07x faster                                                              |
| xml_etree_iterparse        | 150 ms                                                                | 141 ms: 1.06x faster                                                              |
| pathlib                    | 24.5 ms                                                               | 23.1 ms: 1.06x faster                                                             |
| raytrace                   | 353 ms                                                                | 332 ms: 1.06x faster                                                              |
| float                      | 92.1 ms                                                               | 87.3 ms: 1.05x faster                                                             |
| tomli_loads                | 2.59 sec                                                              | 2.47 sec: 1.05x faster                                                            |
| sympy_sum                  | 154 ms                                                                | 148 ms: 1.05x faster                                                              |
| regex_v8                   | 28.3 ms                                                               | 27.1 ms: 1.05x faster                                                             |
| pyflate                    | 559 ms                                                                | 537 ms: 1.04x faster                                                              |
| sympy_integrate            | 21.6 ms                                                               | 20.8 ms: 1.04x faster                                                             |
| html5lib                   | 65.1 ms                                                               | 62.9 ms: 1.03x faster                                                             |
| scimark_monte_carlo        | 85.1 ms                                                               | 82.2 ms: 1.03x faster                                                             |
| chaos                      | 71.4 ms                                                               | 69.3 ms: 1.03x faster                                                             |
| genshi_text                | 27.4 ms                                                               | 26.6 ms: 1.03x faster                                                             |
| xml_etree_generate         | 112 ms                                                                | 111 ms: 1.01x faster                                                              |
| logging_format             | 8.34 us                                                               | 8.38 us: 1.00x slower                                                             |
| sqlite_synth               | 3.77 us                                                               | 3.79 us: 1.01x slower                                                             |
| asyncio_websockets         | 658 ms                                                                | 671 ms: 1.02x slower                                                              |
| pidigits                   | 233 ms                                                                | 238 ms: 1.02x slower                                                              |
| coroutines                 | 29.0 ms                                                               | 29.7 ms: 1.03x slower                                                             |
| json                       | 5.54 ms                                                               | 5.69 ms: 1.03x slower                                                             |
| python_startup_no_site     | 8.37 ms                                                               | 8.62 ms: 1.03x slower                                                             |
| scimark_fft                | 418 ms                                                                | 433 ms: 1.03x slower                                                              |
| sympy_expand               | 454 ms                                                                | 471 ms: 1.04x slower                                                              |
| thrift                     | 937 us                                                                | 983 us: 1.05x slower                                                              |
| json_loads                 | 30.7 us                                                               | 32.4 us: 1.06x slower                                                             |
| pickle_pure_python         | 365 us                                                                | 387 us: 1.06x slower                                                              |
| richards_super             | 58.5 ms                                                               | 62.1 ms: 1.06x slower                                                             |
| scimark_lu                 | 146 ms                                                                | 155 ms: 1.06x slower                                                              |
| fannkuch                   | 443 ms                                                                | 477 ms: 1.08x slower                                                              |
| typing_runtime_protocols   | 181 us                                                                | 197 us: 1.09x slower                                                              |
| richards                   | 50.9 ms                                                               | 56.3 ms: 1.11x slower                                                             |
| pprint_pformat             | 1.88 sec                                                              | 2.08 sec: 1.11x slower                                                            |
| mako                       | 12.9 ms                                                               | 14.3 ms: 1.11x slower                                                             |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.87 ms: 1.11x slower                                                             |
| json_dumps                 | 12.3 ms                                                               | 13.7 ms: 1.12x slower                                                             |
| pprint_safe_repr           | 916 ms                                                                | 1.03 sec: 1.12x slower                                                            |
| telco                      | 8.51 ms                                                               | 9.61 ms: 1.13x slower                                                             |
| nbody                      | 105 ms                                                                | 122 ms: 1.17x slower                                                              |
| coverage                   | 87.3 ms                                                               | 102 ms: 1.17x slower                                                              |
| python_startup             | 11.4 ms                                                               | 15.1 ms: 1.33x slower                                                             |
| gc_traversal               | 4.40 ms                                                               | 6.83 ms: 1.55x slower                                                             |
| create_gc_cycles           | 1.92 ms                                                               | 3.77 ms: 1.97x slower                                                             |
| logging_silent             | 127 ns                                                                | 650 ns: 5.13x slower                                                              |
| Geometric mean             | (ref)                                                                 | 1.03x faster                                                                      |

Benchmark hidden because not significant (15): django_template, crypto_pyaes, deltablue, nqueens, scimark_sor, pycparser, sympy_str, 2to3, meteor_contest, docutils, hexiom, genshi_xml, unpickle_pure_python, logging_simple, xml_etree_process
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250626-3.15.0a0-892a89d/bm-20250626-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.056x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.10x