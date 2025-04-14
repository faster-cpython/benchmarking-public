# Results vs. 3.12.0

- fork: diegorusso
- ref: aarch64_trampolines
- machine: linux-aarch64
- commit hash: efdef5f
- commit date: 2025-03-10
- overall geometric mean: 1.031x faster
- HPT reliability: 97.64%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250310-arminc-aarch64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 303 ms: 1.02x faster                                                        |
| docutils       | 2.98 sec                                                              | 3.10 sec: 1.04x slower                                                      |
| html5lib       | 65.1 ms                                                               | 61.9 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250310-arminc-aarch64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 471 ms: 1.65x faster                                                        |
| async_tree_none            | 624 ms                                                                | 381 ms: 1.64x faster                                                        |
| async_tree_io              | 1.41 sec                                                              | 885 ms: 1.59x faster                                                        |
| async_tree_io_tg           | 1.40 sec                                                              | 893 ms: 1.57x faster                                                        |
| async_tree_memoization_tg  | 740 ms                                                                | 475 ms: 1.56x faster                                                        |
| async_tree_none_tg         | 577 ms                                                                | 370 ms: 1.56x faster                                                        |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 657 ms: 1.39x faster                                                        |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 649 ms: 1.36x faster                                                        |
| Geometric mean             | (ref)                                                                 | 1.54x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250310-arminc-aarch64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 82.9 ms: 1.11x faster                                                       |
| nbody          | 105 ms                                                                | 122 ms: 1.17x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250310-arminc-aarch64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.89 ms: 1.19x faster                                                       |
| regex_compile  | 137 ms                                                                | 123 ms: 1.11x faster                                                        |
| regex_v8       | 28.3 ms                                                               | 28.2 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                 | 1.08x faster                                                                |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250310-arminc-aarch64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 177 ms: 1.10x faster                                                        |
| xml_etree_iterparse  | 150 ms                                                                | 141 ms: 1.07x faster                                                        |
| tomli_loads          | 2.59 sec                                                              | 2.45 sec: 1.06x faster                                                      |
| xml_etree_generate   | 112 ms                                                                | 107 ms: 1.05x faster                                                        |
| xml_etree_process    | 79.0 ms                                                               | 76.6 ms: 1.03x faster                                                       |
| unpickle_pure_python | 260 us                                                                | 282 us: 1.08x slower                                                        |
| pickle_pure_python   | 365 us                                                                | 398 us: 1.09x slower                                                        |
| json_dumps           | 12.3 ms                                                               | 13.7 ms: 1.12x slower                                                       |
| json_loads           | 30.7 us                                                               | 34.6 us: 1.13x slower                                                       |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250310-arminc-aarch64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 10.1 ms: 1.21x slower                                                       |
| python_startup         | 11.4 ms                                                               | 16.1 ms: 1.42x slower                                                       |
| Geometric mean         | (ref)                                                                 | 1.31x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250310-arminc-aarch64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 38.8 ms: 1.05x faster                                                       |
| genshi_text     | 27.4 ms                                                               | 26.6 ms: 1.03x faster                                                       |
| genshi_xml      | 60.6 ms                                                               | 61.0 ms: 1.01x slower                                                       |
| mako            | 12.9 ms                                                               | 13.7 ms: 1.06x slower                                                       |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250310-arminc-aarch64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 471 ms: 1.65x faster                                                        |
| async_tree_none            | 624 ms                                                                | 381 ms: 1.64x faster                                                        |
| async_tree_io              | 1.41 sec                                                              | 885 ms: 1.59x faster                                                        |
| async_tree_io_tg           | 1.40 sec                                                              | 893 ms: 1.57x faster                                                        |
| async_tree_memoization_tg  | 740 ms                                                                | 475 ms: 1.56x faster                                                        |
| async_tree_none_tg         | 577 ms                                                                | 370 ms: 1.56x faster                                                        |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 657 ms: 1.39x faster                                                        |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 649 ms: 1.36x faster                                                        |
| deepcopy                   | 446 us                                                                | 334 us: 1.33x faster                                                        |
| deepcopy_memo              | 49.6 us                                                               | 38.5 us: 1.29x faster                                                       |
| regex_effbot               | 4.64 ms                                                               | 3.89 ms: 1.19x faster                                                       |
| generators                 | 43.5 ms                                                               | 36.6 ms: 1.19x faster                                                       |
| deepcopy_reduce            | 4.10 us                                                               | 3.52 us: 1.16x faster                                                       |
| dulwich_log                | 62.0 ms                                                               | 53.5 ms: 1.16x faster                                                       |
| pylint                     | 355 ms                                                                | 313 ms: 1.13x faster                                                        |
| regex_compile              | 137 ms                                                                | 123 ms: 1.11x faster                                                        |
| float                      | 92.1 ms                                                               | 82.9 ms: 1.11x faster                                                       |
| pathlib                    | 24.5 ms                                                               | 22.1 ms: 1.11x faster                                                       |
| logging_simple             | 7.63 us                                                               | 6.90 us: 1.11x faster                                                       |
| xml_etree_parse            | 195 ms                                                                | 177 ms: 1.10x faster                                                        |
| raytrace                   | 353 ms                                                                | 320 ms: 1.10x faster                                                        |
| logging_format             | 8.34 us                                                               | 7.64 us: 1.09x faster                                                       |
| richards_super             | 58.5 ms                                                               | 54.0 ms: 1.08x faster                                                       |
| sqlalchemy_declarative     | 157 ms                                                                | 146 ms: 1.08x faster                                                        |
| async_generators           | 491 ms                                                                | 456 ms: 1.07x faster                                                        |
| chaos                      | 71.4 ms                                                               | 66.5 ms: 1.07x faster                                                       |
| sqlalchemy_imperative      | 16.7 ms                                                               | 15.5 ms: 1.07x faster                                                       |
| sympy_sum                  | 154 ms                                                                | 145 ms: 1.07x faster                                                        |
| xml_etree_iterparse        | 150 ms                                                                | 141 ms: 1.07x faster                                                        |
| tomli_loads                | 2.59 sec                                                              | 2.45 sec: 1.06x faster                                                      |
| html5lib                   | 65.1 ms                                                               | 61.9 ms: 1.05x faster                                                       |
| django_template            | 40.7 ms                                                               | 38.8 ms: 1.05x faster                                                       |
| xml_etree_generate         | 112 ms                                                                | 107 ms: 1.05x faster                                                        |
| richards                   | 50.9 ms                                                               | 49.0 ms: 1.04x faster                                                       |
| scimark_lu                 | 146 ms                                                                | 140 ms: 1.04x faster                                                        |
| deltablue                  | 4.12 ms                                                               | 3.97 ms: 1.04x faster                                                       |
| sympy_str                  | 280 ms                                                                | 270 ms: 1.04x faster                                                        |
| comprehensions             | 25.4 us                                                               | 24.6 us: 1.03x faster                                                       |
| genshi_text                | 27.4 ms                                                               | 26.6 ms: 1.03x faster                                                       |
| mdp                        | 3.41 sec                                                              | 3.31 sec: 1.03x faster                                                      |
| xml_etree_process          | 79.0 ms                                                               | 76.6 ms: 1.03x faster                                                       |
| sympy_integrate            | 21.6 ms                                                               | 21.2 ms: 1.02x faster                                                       |
| 2to3                       | 308 ms                                                                | 303 ms: 1.02x faster                                                        |
| regex_v8                   | 28.3 ms                                                               | 28.2 ms: 1.01x faster                                                       |
| sqlite_synth               | 3.77 us                                                               | 3.75 us: 1.01x faster                                                       |
| genshi_xml                 | 60.6 ms                                                               | 61.0 ms: 1.01x slower                                                       |
| pyflate                    | 559 ms                                                                | 566 ms: 1.01x slower                                                        |
| bench_thread_pool          | 1.31 ms                                                               | 1.33 ms: 1.02x slower                                                       |
| scimark_fft                | 418 ms                                                                | 428 ms: 1.02x slower                                                        |
| logging_silent             | 127 ns                                                                | 131 ns: 1.03x slower                                                        |
| docutils                   | 2.98 sec                                                              | 3.10 sec: 1.04x slower                                                      |
| sympy_expand               | 454 ms                                                                | 472 ms: 1.04x slower                                                        |
| scimark_monte_carlo        | 85.1 ms                                                               | 88.8 ms: 1.04x slower                                                       |
| json                       | 5.54 ms                                                               | 5.81 ms: 1.05x slower                                                       |
| spectral_norm              | 131 ms                                                                | 138 ms: 1.06x slower                                                        |
| mako                       | 12.9 ms                                                               | 13.7 ms: 1.06x slower                                                       |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.67 ms: 1.08x slower                                                       |
| meteor_contest             | 112 ms                                                                | 121 ms: 1.08x slower                                                        |
| unpickle_pure_python       | 260 us                                                                | 282 us: 1.08x slower                                                        |
| nqueens                    | 99.2 ms                                                               | 108 ms: 1.09x slower                                                        |
| pickle_pure_python         | 365 us                                                                | 398 us: 1.09x slower                                                        |
| pycparser                  | 1.26 sec                                                              | 1.37 sec: 1.09x slower                                                      |
| go                         | 157 ms                                                                | 174 ms: 1.11x slower                                                        |
| telco                      | 8.51 ms                                                               | 9.46 ms: 1.11x slower                                                       |
| json_dumps                 | 12.3 ms                                                               | 13.7 ms: 1.12x slower                                                       |
| crypto_pyaes               | 86.6 ms                                                               | 97.4 ms: 1.12x slower                                                       |
| json_loads                 | 30.7 us                                                               | 34.6 us: 1.13x slower                                                       |
| coverage                   | 87.3 ms                                                               | 98.7 ms: 1.13x slower                                                       |
| typing_runtime_protocols   | 181 us                                                                | 205 us: 1.13x slower                                                        |
| nbody                      | 105 ms                                                                | 122 ms: 1.17x slower                                                        |
| fannkuch                   | 443 ms                                                                | 521 ms: 1.17x slower                                                        |
| hexiom                     | 6.98 ms                                                               | 8.25 ms: 1.18x slower                                                       |
| python_startup_no_site     | 8.37 ms                                                               | 10.1 ms: 1.21x slower                                                       |
| pprint_safe_repr           | 916 ms                                                                | 1.23 sec: 1.34x slower                                                      |
| pprint_pformat             | 1.88 sec                                                              | 2.56 sec: 1.36x slower                                                      |
| python_startup             | 11.4 ms                                                               | 16.1 ms: 1.42x slower                                                       |
| gc_traversal               | 4.40 ms                                                               | 6.57 ms: 1.49x slower                                                       |
| create_gc_cycles           | 1.92 ms                                                               | 3.57 ms: 1.86x slower                                                       |
| bench_mp_pool              | 7.05 ms                                                               | 2.79 sec: 395.58x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.05x slower                                                                |

Benchmark hidden because not significant (6): coroutines, regex_dna, thrift, scimark_sor, asyncio_websockets, pidigits
Ignored benchmarks (17) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250310-3.14.0a5+-efdef5f-JIT/bm-20250310-arminc-aarch64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.031x faster

# HPT report

- Reliability score: 97.64% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x