# Results vs. 3.12.0

- fork: python
- ref: v3.13.1
- machine: linux-aarch64
- commit hash: 0671451
- commit date: 2024-12-03
- overall geometric mean: 1.017x slower
- HPT reliability: 71.47%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241203-arminc-aarch64-python-v3.13.1-3.13.1-0671451 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 319 ms: 1.04x slower                                     |
| chameleon      | 8.81 ms                                                               | 9.41 ms: 1.07x slower                                    |
| docutils       | 2.98 sec                                                              | 2.95 sec: 1.01x faster                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                             |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241203-arminc-aarch64-python-v3.13.1-3.13.1-0671451 |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| async_tree_io              | 1.41 sec                                                              | 1.16 sec: 1.21x faster                                   |
| async_tree_none            | 624 ms                                                                | 517 ms: 1.21x faster                                     |
| async_tree_none_tg         | 577 ms                                                                | 479 ms: 1.20x faster                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 1.18 sec: 1.19x faster                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 766 ms: 1.19x faster                                     |
| async_tree_memoization     | 777 ms                                                                | 664 ms: 1.17x faster                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 653 ms: 1.13x faster                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 825 ms: 1.07x faster                                     |
| Geometric mean             | (ref)                                                                 | 1.17x faster                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241203-arminc-aarch64-python-v3.13.1-3.13.1-0671451 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| float          | 92.1 ms                                                               | 97.4 ms: 1.06x slower                                    |
| nbody          | 105 ms                                                                | 121 ms: 1.16x slower                                     |
| Geometric mean | (ref)                                                                 | 1.08x slower                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241203-arminc-aarch64-python-v3.13.1-3.13.1-0671451 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.06 ms: 1.14x faster                                    |
| regex_compile  | 137 ms                                                                | 131 ms: 1.05x faster                                     |
| regex_dna      | 254 ms                                                                | 266 ms: 1.05x slower                                     |
| regex_v8       | 28.3 ms                                                               | 33.0 ms: 1.17x slower                                    |
| Geometric mean | (ref)                                                                 | 1.00x slower                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241203-arminc-aarch64-python-v3.13.1-3.13.1-0671451 |
|--------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| tomli_loads        | 2.59 sec                                                              | 2.65 sec: 1.02x slower                                   |
| pickle_pure_python | 365 us                                                                | 375 us: 1.03x slower                                     |
| xml_etree_generate | 112 ms                                                                | 116 ms: 1.03x slower                                     |
| xml_etree_process  | 79.0 ms                                                               | 84.5 ms: 1.07x slower                                    |
| json_loads         | 30.7 us                                                               | 34.3 us: 1.12x slower                                    |
| json_dumps         | 12.3 ms                                                               | 14.2 ms: 1.16x slower                                    |
| Geometric mean     | (ref)                                                                 | 1.05x slower                                             |

Benchmark hidden because not significant (3): unpickle_pure_python, xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241203-arminc-aarch64-python-v3.13.1-3.13.1-0671451 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.86 ms: 1.06x slower                                    |
| python_startup         | 11.4 ms                                                               | 16.0 ms: 1.41x slower                                    |
| Geometric mean         | (ref)                                                                 | 1.22x slower                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241203-arminc-aarch64-python-v3.13.1-3.13.1-0671451 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| genshi_xml     | 60.6 ms                                                               | 62.5 ms: 1.03x slower                                    |
| mako           | 12.9 ms                                                               | 14.1 ms: 1.10x slower                                    |
| genshi_text    | 27.4 ms                                                               | 30.3 ms: 1.11x slower                                    |
| Geometric mean | (ref)                                                                 | 1.06x slower                                             |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241203-arminc-aarch64-python-v3.13.1-3.13.1-0671451 |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| async_tree_io              | 1.41 sec                                                              | 1.16 sec: 1.21x faster                                   |
| async_tree_none            | 624 ms                                                                | 517 ms: 1.21x faster                                     |
| async_tree_none_tg         | 577 ms                                                                | 479 ms: 1.20x faster                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 1.18 sec: 1.19x faster                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 766 ms: 1.19x faster                                     |
| comprehensions             | 25.4 us                                                               | 21.6 us: 1.17x faster                                    |
| async_tree_memoization     | 777 ms                                                                | 664 ms: 1.17x faster                                     |
| raytrace                   | 353 ms                                                                | 304 ms: 1.16x faster                                     |
| regex_effbot               | 4.64 ms                                                               | 4.06 ms: 1.14x faster                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 653 ms: 1.13x faster                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 825 ms: 1.07x faster                                     |
| regex_compile              | 137 ms                                                                | 131 ms: 1.05x faster                                     |
| sympy_str                  | 280 ms                                                                | 267 ms: 1.05x faster                                     |
| sympy_sum                  | 154 ms                                                                | 148 ms: 1.04x faster                                     |
| docutils                   | 2.98 sec                                                              | 2.95 sec: 1.01x faster                                   |
| mdp                        | 3.41 sec                                                              | 3.46 sec: 1.01x slower                                   |
| tomli_loads                | 2.59 sec                                                              | 2.65 sec: 1.02x slower                                   |
| pickle_pure_python         | 365 us                                                                | 375 us: 1.03x slower                                     |
| asyncio_websockets         | 658 ms                                                                | 677 ms: 1.03x slower                                     |
| genshi_xml                 | 60.6 ms                                                               | 62.5 ms: 1.03x slower                                    |
| xml_etree_generate         | 112 ms                                                                | 116 ms: 1.03x slower                                     |
| 2to3                       | 308 ms                                                                | 319 ms: 1.04x slower                                     |
| regex_dna                  | 254 ms                                                                | 266 ms: 1.05x slower                                     |
| sqlglot_normalize          | 126 ms                                                                | 132 ms: 1.05x slower                                     |
| pycparser                  | 1.26 sec                                                              | 1.32 sec: 1.05x slower                                   |
| async_generators           | 491 ms                                                                | 517 ms: 1.05x slower                                     |
| hexiom                     | 6.98 ms                                                               | 7.38 ms: 1.06x slower                                    |
| float                      | 92.1 ms                                                               | 97.4 ms: 1.06x slower                                    |
| python_startup_no_site     | 8.37 ms                                                               | 8.86 ms: 1.06x slower                                    |
| richards_super             | 58.5 ms                                                               | 61.9 ms: 1.06x slower                                    |
| go                         | 157 ms                                                                | 167 ms: 1.06x slower                                     |
| sympy_expand               | 454 ms                                                                | 481 ms: 1.06x slower                                     |
| chameleon                  | 8.81 ms                                                               | 9.41 ms: 1.07x slower                                    |
| richards                   | 50.9 ms                                                               | 54.4 ms: 1.07x slower                                    |
| deepcopy                   | 446 us                                                                | 476 us: 1.07x slower                                     |
| pprint_pformat             | 1.88 sec                                                              | 2.01 sec: 1.07x slower                                   |
| xml_etree_process          | 79.0 ms                                                               | 84.5 ms: 1.07x slower                                    |
| deepcopy_memo              | 49.6 us                                                               | 53.4 us: 1.08x slower                                    |
| json                       | 5.54 ms                                                               | 5.97 ms: 1.08x slower                                    |
| pprint_safe_repr           | 916 ms                                                                | 987 ms: 1.08x slower                                     |
| fannkuch                   | 443 ms                                                                | 482 ms: 1.09x slower                                     |
| meteor_contest             | 112 ms                                                                | 122 ms: 1.09x slower                                     |
| mako                       | 12.9 ms                                                               | 14.1 ms: 1.10x slower                                    |
| pyflate                    | 559 ms                                                                | 614 ms: 1.10x slower                                     |
| thrift                     | 937 us                                                                | 1.03 ms: 1.10x slower                                    |
| logging_silent             | 127 ns                                                                | 140 ns: 1.10x slower                                     |
| genshi_text                | 27.4 ms                                                               | 30.3 ms: 1.11x slower                                    |
| typing_runtime_protocols   | 181 us                                                                | 200 us: 1.11x slower                                     |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.87 ms: 1.11x slower                                    |
| json_loads                 | 30.7 us                                                               | 34.3 us: 1.12x slower                                    |
| gunicorn                   | 1.14 ms                                                               | 1.27 ms: 1.12x slower                                    |
| spectral_norm              | 131 ms                                                                | 147 ms: 1.13x slower                                     |
| scimark_fft                | 418 ms                                                                | 472 ms: 1.13x slower                                     |
| sqlite_synth               | 3.77 us                                                               | 4.30 us: 1.14x slower                                    |
| scimark_sor                | 150 ms                                                                | 171 ms: 1.14x slower                                     |
| nbody                      | 105 ms                                                                | 121 ms: 1.16x slower                                     |
| json_dumps                 | 12.3 ms                                                               | 14.2 ms: 1.16x slower                                    |
| regex_v8                   | 28.3 ms                                                               | 33.0 ms: 1.17x slower                                    |
| coverage                   | 87.3 ms                                                               | 104 ms: 1.19x slower                                     |
| bench_mp_pool              | 7.05 ms                                                               | 8.56 ms: 1.21x slower                                    |
| telco                      | 8.51 ms                                                               | 10.8 ms: 1.27x slower                                    |
| gc_traversal               | 4.40 ms                                                               | 5.97 ms: 1.36x slower                                    |
| python_startup             | 11.4 ms                                                               | 16.0 ms: 1.41x slower                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.42 ms: 1.78x slower                                    |
| Geometric mean             | (ref)                                                                 | 1.04x slower                                             |

Benchmark hidden because not significant (27): generators, sqlalchemy_imperative, tornado_http, logging_simple, logging_format, deltablue, pathlib, crypto_pyaes, sqlglot_parse, scimark_lu, chaos, sqlalchemy_declarative, bench_thread_pool, sympy_integrate, unpickle_pure_python, pylint, nqueens, xml_etree_iterparse, sqlglot_transpile, pidigits, html5lib, django_template, xml_etree_parse, scimark_monte_carlo, deepcopy_reduce, coroutines, sqlglot_optimize
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
Ignored benchmarks (9) of results/bm-20241203-3.13.1-0671451/bm-20241203-arminc-aarch64-python-v3.13.1-3.13.1-0671451.json: bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.017x slower

# HPT report

- Reliability score: 71.47% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x