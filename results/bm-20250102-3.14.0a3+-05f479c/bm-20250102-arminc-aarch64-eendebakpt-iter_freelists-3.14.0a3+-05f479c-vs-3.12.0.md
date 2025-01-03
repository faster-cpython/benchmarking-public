# Results vs. 3.12.0

- fork: eendebakpt
- ref: iter_freelists
- machine: linux-aarch64
- commit hash: 05f479c
- commit date: 2025-01-02
- overall geometric mean: 1.036x faster
- HPT reliability: 99.76%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (3): 2to3, docutils, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250102-arminc-aarch64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 383 ms: 1.63x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 873 ms: 1.62x faster                                                   |
| async_tree_memoization     | 777 ms                                                                | 486 ms: 1.60x faster                                                   |
| async_tree_io_tg           | 1.40 sec                                                              | 885 ms: 1.59x faster                                                   |
| async_tree_memoization_tg  | 740 ms                                                                | 467 ms: 1.59x faster                                                   |
| async_tree_none_tg         | 577 ms                                                                | 378 ms: 1.53x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 671 ms: 1.36x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 656 ms: 1.35x faster                                                   |
| Geometric mean             | (ref)                                                                 | 1.53x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250102-arminc-aarch64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 240 ms: 1.03x slower                                                   |
| nbody          | 105 ms                                                                | 121 ms: 1.15x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                           |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250102-arminc-aarch64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.03 ms: 1.15x faster                                                  |
| regex_compile  | 137 ms                                                                | 128 ms: 1.07x faster                                                   |
| regex_dna      | 254 ms                                                                | 248 ms: 1.03x faster                                                   |
| regex_v8       | 28.3 ms                                                               | 32.5 ms: 1.15x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250102-arminc-aarch64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|---------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 180 ms: 1.08x faster                                                   |
| xml_etree_iterparse | 150 ms                                                                | 143 ms: 1.05x faster                                                   |
| json_loads          | 30.7 us                                                               | 32.3 us: 1.05x slower                                                  |
| pickle_pure_python  | 365 us                                                                | 399 us: 1.09x slower                                                   |
| json_dumps          | 12.3 ms                                                               | 14.7 ms: 1.20x slower                                                  |
| Geometric mean      | (ref)                                                                 | 1.03x slower                                                           |

Benchmark hidden because not significant (4): tomli_loads, unpickle_pure_python, xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250102-arminc-aarch64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.91 ms: 1.06x slower                                                  |
| python_startup         | 11.4 ms                                                               | 16.4 ms: 1.44x slower                                                  |
| Geometric mean         | (ref)                                                                 | 1.24x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250102-arminc-aarch64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako           | 12.9 ms                                                               | 14.5 ms: 1.13x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                           |

Benchmark hidden because not significant (3): django_template, genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250102-arminc-aarch64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 383 ms: 1.63x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 873 ms: 1.62x faster                                                   |
| async_tree_memoization     | 777 ms                                                                | 486 ms: 1.60x faster                                                   |
| async_tree_io_tg           | 1.40 sec                                                              | 885 ms: 1.59x faster                                                   |
| async_tree_memoization_tg  | 740 ms                                                                | 467 ms: 1.59x faster                                                   |
| async_tree_none_tg         | 577 ms                                                                | 378 ms: 1.53x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 671 ms: 1.36x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 656 ms: 1.35x faster                                                   |
| deepcopy                   | 446 us                                                                | 345 us: 1.29x faster                                                   |
| comprehensions             | 25.4 us                                                               | 21.1 us: 1.20x faster                                                  |
| deepcopy_memo              | 49.6 us                                                               | 41.5 us: 1.20x faster                                                  |
| generators                 | 43.5 ms                                                               | 36.6 ms: 1.19x faster                                                  |
| regex_effbot               | 4.64 ms                                                               | 4.03 ms: 1.15x faster                                                  |
| pylint                     | 355 ms                                                                | 312 ms: 1.14x faster                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 3.65 us: 1.12x faster                                                  |
| pathlib                    | 24.5 ms                                                               | 21.9 ms: 1.12x faster                                                  |
| xml_etree_parse            | 195 ms                                                                | 180 ms: 1.08x faster                                                   |
| go                         | 157 ms                                                                | 146 ms: 1.08x faster                                                   |
| regex_compile              | 137 ms                                                                | 128 ms: 1.07x faster                                                   |
| raytrace                   | 353 ms                                                                | 330 ms: 1.07x faster                                                   |
| sympy_sum                  | 154 ms                                                                | 144 ms: 1.07x faster                                                   |
| sympy_str                  | 280 ms                                                                | 262 ms: 1.07x faster                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 143 ms: 1.05x faster                                                   |
| logging_format             | 8.34 us                                                               | 7.93 us: 1.05x faster                                                  |
| deltablue                  | 4.12 ms                                                               | 3.95 ms: 1.04x faster                                                  |
| scimark_lu                 | 146 ms                                                                | 140 ms: 1.04x faster                                                   |
| logging_simple             | 7.63 us                                                               | 7.37 us: 1.04x faster                                                  |
| regex_dna                  | 254 ms                                                                | 248 ms: 1.03x faster                                                   |
| sympy_integrate            | 21.6 ms                                                               | 21.1 ms: 1.02x faster                                                  |
| sqlglot_normalize          | 126 ms                                                                | 124 ms: 1.01x faster                                                   |
| richards                   | 50.9 ms                                                               | 52.3 ms: 1.03x slower                                                  |
| pycparser                  | 1.26 sec                                                              | 1.29 sec: 1.03x slower                                                 |
| pidigits                   | 233 ms                                                                | 240 ms: 1.03x slower                                                   |
| json                       | 5.54 ms                                                               | 5.79 ms: 1.05x slower                                                  |
| json_loads                 | 30.7 us                                                               | 32.3 us: 1.05x slower                                                  |
| pyflate                    | 559 ms                                                                | 590 ms: 1.05x slower                                                   |
| sqlite_synth               | 3.77 us                                                               | 4.00 us: 1.06x slower                                                  |
| pprint_safe_repr           | 916 ms                                                                | 972 ms: 1.06x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 2.00 sec: 1.06x slower                                                 |
| python_startup_no_site     | 8.37 ms                                                               | 8.91 ms: 1.06x slower                                                  |
| hexiom                     | 6.98 ms                                                               | 7.45 ms: 1.07x slower                                                  |
| fannkuch                   | 443 ms                                                                | 480 ms: 1.08x slower                                                   |
| scimark_sor                | 150 ms                                                                | 162 ms: 1.08x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 399 us: 1.09x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 202 us: 1.12x slower                                                   |
| logging_silent             | 127 ns                                                                | 142 ns: 1.12x slower                                                   |
| mako                       | 12.9 ms                                                               | 14.5 ms: 1.13x slower                                                  |
| telco                      | 8.51 ms                                                               | 9.70 ms: 1.14x slower                                                  |
| regex_v8                   | 28.3 ms                                                               | 32.5 ms: 1.15x slower                                                  |
| nbody                      | 105 ms                                                                | 121 ms: 1.15x slower                                                   |
| coverage                   | 87.3 ms                                                               | 102 ms: 1.17x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 14.7 ms: 1.20x slower                                                  |
| mypy2                      | 873 ms                                                                | 1.05 sec: 1.21x slower                                                 |
| python_startup             | 11.4 ms                                                               | 16.4 ms: 1.44x slower                                                  |
| gc_traversal               | 4.40 ms                                                               | 7.03 ms: 1.60x slower                                                  |
| create_gc_cycles           | 1.92 ms                                                               | 3.53 ms: 1.84x slower                                                  |
| bench_mp_pool              | 7.05 ms                                                               | 5.00 sec: 708.19x slower                                               |
| Geometric mean             | (ref)                                                                 | 1.06x slower                                                           |

Benchmark hidden because not significant (33): sqlalchemy_declarative, dulwich_log, crypto_pyaes, sqlalchemy_imperative, float, 2to3, sqlglot_parse, sqlglot_transpile, spectral_norm, tomli_loads, mdp, sqlglot_optimize, thrift, coroutines, docutils, django_template, scimark_monte_carlo, unpickle_pure_python, async_generators, scimark_fft, chaos, bench_thread_pool, xml_etree_process, sympy_expand, genshi_text, xml_etree_generate, asyncio_websockets, html5lib, nqueens, meteor_contest, scimark_sparse_mat_mult, genshi_xml, richards_super
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (8) of results/bm-20250102-3.14.0a3+-05f479c/bm-20250102-arminc-aarch64-eendebakpt-iter_freelists-3.14.0a3+-05f479c.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.036x faster

# HPT report

- Reliability score: 99.76% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x