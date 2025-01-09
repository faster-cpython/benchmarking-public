# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: tail_call
- machine: linux-aarch64
- commit hash: f1d3190
- commit date: 2025-01-07
- overall geometric mean: 1.069x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250107-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 293 ms: 1.05x faster                                                    |
| html5lib       | 65.1 ms                                                               | 60.6 ms: 1.07x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.04x faster                                                            |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250107-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 446 ms: 1.66x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 848 ms: 1.66x faster                                                    |
| async_tree_none            | 624 ms                                                                | 377 ms: 1.66x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 472 ms: 1.65x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 869 ms: 1.62x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 361 ms: 1.60x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 728 ms: 1.25x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 722 ms: 1.22x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.53x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250107-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 83.8 ms: 1.10x faster                                                   |
| pidigits       | 233 ms                                                                | 307 ms: 1.32x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.08x slower                                                            |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250107-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 127 ms: 1.08x faster                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.38 ms: 1.06x faster                                                   |
| regex_v8       | 28.3 ms                                                               | 34.4 ms: 1.21x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250107-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.59 sec                                                              | 2.41 sec: 1.08x faster                                                  |
| xml_etree_generate   | 112 ms                                                                | 107 ms: 1.05x faster                                                    |
| unpickle_pure_python | 260 us                                                                | 248 us: 1.05x faster                                                    |
| json_loads           | 30.7 us                                                               | 33.1 us: 1.08x slower                                                   |
| xml_etree_parse      | 195 ms                                                                | 211 ms: 1.08x slower                                                    |
| pickle_pure_python   | 365 us                                                                | 399 us: 1.09x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 14.6 ms: 1.19x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.03x slower                                                            |

Benchmark hidden because not significant (2): xml_etree_process, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250107-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.09 ms: 1.09x slower                                                   |
| python_startup         | 11.4 ms                                                               | 16.3 ms: 1.44x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.25x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250107-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 38.8 ms: 1.05x faster                                                   |
| mako            | 12.9 ms                                                               | 14.2 ms: 1.10x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250107-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 446 ms: 1.66x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 848 ms: 1.66x faster                                                    |
| async_tree_none            | 624 ms                                                                | 377 ms: 1.66x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 472 ms: 1.65x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 869 ms: 1.62x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 361 ms: 1.60x faster                                                    |
| deepcopy                   | 446 us                                                                | 315 us: 1.41x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 36.9 us: 1.35x faster                                                   |
| comprehensions             | 25.4 us                                                               | 20.0 us: 1.27x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 728 ms: 1.25x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 722 ms: 1.22x faster                                                    |
| generators                 | 43.5 ms                                                               | 35.8 ms: 1.21x faster                                                   |
| spectral_norm              | 131 ms                                                                | 109 ms: 1.20x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.41 us: 1.20x faster                                                   |
| go                         | 157 ms                                                                | 131 ms: 1.20x faster                                                    |
| pylint                     | 355 ms                                                                | 299 ms: 1.19x faster                                                    |
| raytrace                   | 353 ms                                                                | 302 ms: 1.17x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 21.1 ms: 1.17x faster                                                   |
| scimark_fft                | 418 ms                                                                | 363 ms: 1.15x faster                                                    |
| scimark_lu                 | 146 ms                                                                | 127 ms: 1.15x faster                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 74.7 ms: 1.14x faster                                                   |
| logging_simple             | 7.63 us                                                               | 6.71 us: 1.14x faster                                                   |
| logging_format             | 8.34 us                                                               | 7.48 us: 1.12x faster                                                   |
| sqlglot_parse              | 1.46 ms                                                               | 1.31 ms: 1.11x faster                                                   |
| float                      | 92.1 ms                                                               | 83.8 ms: 1.10x faster                                                   |
| chaos                      | 71.4 ms                                                               | 65.0 ms: 1.10x faster                                                   |
| deltablue                  | 4.12 ms                                                               | 3.80 ms: 1.08x faster                                                   |
| scimark_sor                | 150 ms                                                                | 138 ms: 1.08x faster                                                    |
| regex_compile              | 137 ms                                                                | 127 ms: 1.08x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.41 sec: 1.08x faster                                                  |
| sympy_sum                  | 154 ms                                                                | 144 ms: 1.08x faster                                                    |
| richards_super             | 58.5 ms                                                               | 54.4 ms: 1.08x faster                                                   |
| logging_silent             | 127 ns                                                                | 118 ns: 1.07x faster                                                    |
| html5lib                   | 65.1 ms                                                               | 60.6 ms: 1.07x faster                                                   |
| sympy_str                  | 280 ms                                                                | 261 ms: 1.07x faster                                                    |
| sqlalchemy_declarative     | 157 ms                                                                | 147 ms: 1.07x faster                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 1.72 ms: 1.07x faster                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 5.84 ms: 1.06x faster                                                   |
| regex_effbot               | 4.64 ms                                                               | 4.38 ms: 1.06x faster                                                   |
| async_generators           | 491 ms                                                                | 465 ms: 1.05x faster                                                    |
| 2to3                       | 308 ms                                                                | 293 ms: 1.05x faster                                                    |
| xml_etree_generate         | 112 ms                                                                | 107 ms: 1.05x faster                                                    |
| pyflate                    | 559 ms                                                                | 533 ms: 1.05x faster                                                    |
| django_template            | 40.7 ms                                                               | 38.8 ms: 1.05x faster                                                   |
| unpickle_pure_python       | 260 us                                                                | 248 us: 1.05x faster                                                    |
| mdp                        | 3.41 sec                                                              | 3.27 sec: 1.04x faster                                                  |
| sympy_integrate            | 21.6 ms                                                               | 20.7 ms: 1.04x faster                                                   |
| asyncio_websockets         | 658 ms                                                                | 680 ms: 1.03x slower                                                    |
| meteor_contest             | 112 ms                                                                | 117 ms: 1.04x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 1.97 sec: 1.05x slower                                                  |
| json                       | 5.54 ms                                                               | 5.81 ms: 1.05x slower                                                   |
| pprint_safe_repr           | 916 ms                                                                | 971 ms: 1.06x slower                                                    |
| json_loads                 | 30.7 us                                                               | 33.1 us: 1.08x slower                                                   |
| telco                      | 8.51 ms                                                               | 9.18 ms: 1.08x slower                                                   |
| xml_etree_parse            | 195 ms                                                                | 211 ms: 1.08x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 9.09 ms: 1.09x slower                                                   |
| sqlite_synth               | 3.77 us                                                               | 4.10 us: 1.09x slower                                                   |
| fannkuch                   | 443 ms                                                                | 482 ms: 1.09x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 399 us: 1.09x slower                                                    |
| coverage                   | 87.3 ms                                                               | 96.1 ms: 1.10x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 199 us: 1.10x slower                                                    |
| mako                       | 12.9 ms                                                               | 14.2 ms: 1.10x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 14.6 ms: 1.19x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 34.4 ms: 1.21x slower                                                   |
| pidigits                   | 233 ms                                                                | 307 ms: 1.32x slower                                                    |
| python_startup             | 11.4 ms                                                               | 16.3 ms: 1.44x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 6.87 ms: 1.56x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 3.82 ms: 1.99x slower                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 4.51 sec: 639.92x slower                                                |
| Geometric mean             | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (20): richards, dulwich_log, sqlalchemy_imperative, bench_thread_pool, sqlglot_normalize, pycparser, genshi_text, xml_etree_process, genshi_xml, coroutines, crypto_pyaes, docutils, xml_etree_iterparse, nqueens, sympy_expand, thrift, sqlglot_optimize, hexiom, nbody, regex_dna
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20250107-3.14.0a3+-f1d3190-CLANG/bm-20250107-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.069x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.08x