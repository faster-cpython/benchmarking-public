# Results vs. 3.12.0

- fork: mdboom
- ref: aa_test_2025
- machine: linux-aarch64
- commit hash: 4844db8
- commit date: 2025-01-21
- overall geometric mean: 1.036x faster
- HPT reliability: 99.66%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| html5lib       | 65.1 ms                                                               | 63.0 ms: 1.03x faster                                            |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                     |

Benchmark hidden because not significant (2): 2to3, docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 379 ms: 1.64x faster                                             |
| async_tree_memoization     | 777 ms                                                                | 483 ms: 1.61x faster                                             |
| async_tree_io              | 1.41 sec                                                              | 887 ms: 1.59x faster                                             |
| async_tree_io_tg           | 1.40 sec                                                              | 889 ms: 1.58x faster                                             |
| async_tree_memoization_tg  | 740 ms                                                                | 477 ms: 1.55x faster                                             |
| async_tree_none_tg         | 577 ms                                                                | 378 ms: 1.52x faster                                             |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 672 ms: 1.36x faster                                             |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 661 ms: 1.34x faster                                             |
| Geometric mean             | (ref)                                                                 | 1.52x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 85.7 ms: 1.07x faster                                            |
| pidigits       | 233 ms                                                                | 242 ms: 1.04x slower                                             |
| nbody          | 105 ms                                                                | 122 ms: 1.16x slower                                             |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.06 ms: 1.14x faster                                            |
| regex_compile  | 137 ms                                                                | 128 ms: 1.07x faster                                             |
| regex_v8       | 28.3 ms                                                               | 32.8 ms: 1.16x slower                                            |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                     |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 183 ms: 1.07x faster                                             |
| xml_etree_iterparse  | 150 ms                                                                | 144 ms: 1.04x faster                                             |
| json_loads           | 30.7 us                                                               | 33.0 us: 1.07x slower                                            |
| xml_etree_process    | 79.0 ms                                                               | 85.8 ms: 1.09x slower                                            |
| unpickle_pure_python | 260 us                                                                | 285 us: 1.10x slower                                             |
| pickle_pure_python   | 365 us                                                                | 410 us: 1.12x slower                                             |
| json_dumps           | 12.3 ms                                                               | 14.6 ms: 1.19x slower                                            |
| Geometric mean       | (ref)                                                                 | 1.05x slower                                                     |

Benchmark hidden because not significant (2): tomli_loads, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.06 ms: 1.08x slower                                            |
| python_startup         | 11.4 ms                                                               | 16.2 ms: 1.43x slower                                            |
| Geometric mean         | (ref)                                                                 | 1.24x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako           | 12.9 ms                                                               | 14.3 ms: 1.11x slower                                            |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                     |

Benchmark hidden because not significant (3): django_template, genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 379 ms: 1.64x faster                                             |
| async_tree_memoization     | 777 ms                                                                | 483 ms: 1.61x faster                                             |
| async_tree_io              | 1.41 sec                                                              | 887 ms: 1.59x faster                                             |
| async_tree_io_tg           | 1.40 sec                                                              | 889 ms: 1.58x faster                                             |
| async_tree_memoization_tg  | 740 ms                                                                | 477 ms: 1.55x faster                                             |
| async_tree_none_tg         | 577 ms                                                                | 378 ms: 1.52x faster                                             |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 672 ms: 1.36x faster                                             |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 661 ms: 1.34x faster                                             |
| deepcopy                   | 446 us                                                                | 356 us: 1.25x faster                                             |
| generators                 | 43.5 ms                                                               | 35.9 ms: 1.21x faster                                            |
| comprehensions             | 25.4 us                                                               | 21.0 us: 1.21x faster                                            |
| deepcopy_memo              | 49.6 us                                                               | 41.3 us: 1.20x faster                                            |
| regex_effbot               | 4.64 ms                                                               | 4.06 ms: 1.14x faster                                            |
| deepcopy_reduce            | 4.10 us                                                               | 3.66 us: 1.12x faster                                            |
| raytrace                   | 353 ms                                                                | 316 ms: 1.12x faster                                             |
| async_generators           | 491 ms                                                                | 446 ms: 1.10x faster                                             |
| go                         | 157 ms                                                                | 144 ms: 1.09x faster                                             |
| pylint                     | 355 ms                                                                | 326 ms: 1.09x faster                                             |
| sympy_sum                  | 154 ms                                                                | 142 ms: 1.09x faster                                             |
| pathlib                    | 24.5 ms                                                               | 22.6 ms: 1.09x faster                                            |
| float                      | 92.1 ms                                                               | 85.7 ms: 1.07x faster                                            |
| regex_compile              | 137 ms                                                                | 128 ms: 1.07x faster                                             |
| sqlalchemy_declarative     | 157 ms                                                                | 147 ms: 1.07x faster                                             |
| xml_etree_parse            | 195 ms                                                                | 183 ms: 1.07x faster                                             |
| deltablue                  | 4.12 ms                                                               | 3.87 ms: 1.06x faster                                            |
| spectral_norm              | 131 ms                                                                | 125 ms: 1.05x faster                                             |
| xml_etree_iterparse        | 150 ms                                                                | 144 ms: 1.04x faster                                             |
| html5lib                   | 65.1 ms                                                               | 63.0 ms: 1.03x faster                                            |
| sqlglot_normalize          | 126 ms                                                                | 127 ms: 1.01x slower                                             |
| scimark_sor                | 150 ms                                                                | 152 ms: 1.02x slower                                             |
| pycparser                  | 1.26 sec                                                              | 1.29 sec: 1.03x slower                                           |
| pidigits                   | 233 ms                                                                | 242 ms: 1.04x slower                                             |
| meteor_contest             | 112 ms                                                                | 117 ms: 1.05x slower                                             |
| sympy_expand               | 454 ms                                                                | 478 ms: 1.05x slower                                             |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.53 ms: 1.05x slower                                            |
| nqueens                    | 99.2 ms                                                               | 105 ms: 1.06x slower                                             |
| sqlglot_optimize           | 61.3 ms                                                               | 64.9 ms: 1.06x slower                                            |
| pprint_safe_repr           | 916 ms                                                                | 976 ms: 1.07x slower                                             |
| hexiom                     | 6.98 ms                                                               | 7.44 ms: 1.07x slower                                            |
| pprint_pformat             | 1.88 sec                                                              | 2.01 sec: 1.07x slower                                           |
| logging_silent             | 127 ns                                                                | 136 ns: 1.07x slower                                             |
| json                       | 5.54 ms                                                               | 5.95 ms: 1.07x slower                                            |
| json_loads                 | 30.7 us                                                               | 33.0 us: 1.07x slower                                            |
| sqlite_synth               | 3.77 us                                                               | 4.06 us: 1.08x slower                                            |
| python_startup_no_site     | 8.37 ms                                                               | 9.06 ms: 1.08x slower                                            |
| xml_etree_process          | 79.0 ms                                                               | 85.8 ms: 1.09x slower                                            |
| unpickle_pure_python       | 260 us                                                                | 285 us: 1.10x slower                                             |
| mako                       | 12.9 ms                                                               | 14.3 ms: 1.11x slower                                            |
| fannkuch                   | 443 ms                                                                | 492 ms: 1.11x slower                                             |
| pickle_pure_python         | 365 us                                                                | 410 us: 1.12x slower                                             |
| telco                      | 8.51 ms                                                               | 9.64 ms: 1.13x slower                                            |
| coverage                   | 87.3 ms                                                               | 99.6 ms: 1.14x slower                                            |
| typing_runtime_protocols   | 181 us                                                                | 207 us: 1.14x slower                                             |
| regex_v8                   | 28.3 ms                                                               | 32.8 ms: 1.16x slower                                            |
| nbody                      | 105 ms                                                                | 122 ms: 1.16x slower                                             |
| json_dumps                 | 12.3 ms                                                               | 14.6 ms: 1.19x slower                                            |
| python_startup             | 11.4 ms                                                               | 16.2 ms: 1.43x slower                                            |
| gc_traversal               | 4.40 ms                                                               | 6.74 ms: 1.53x slower                                            |
| create_gc_cycles           | 1.92 ms                                                               | 3.64 ms: 1.90x slower                                            |
| bench_mp_pool              | 7.05 ms                                                               | 4.70 sec: 666.68x slower                                         |
| Geometric mean             | (ref)                                                                 | 1.06x slower                                                     |

Benchmark hidden because not significant (29): sqlalchemy_imperative, scimark_lu, chaos, logging_format, logging_simple, sqlglot_transpile, crypto_pyaes, django_template, dulwich_log, regex_dna, sympy_str, tomli_loads, richards_super, 2to3, sqlglot_parse, scimark_fft, mdp, docutils, xml_etree_generate, sympy_integrate, richards, pyflate, asyncio_websockets, bench_thread_pool, scimark_monte_carlo, genshi_xml, coroutines, thrift, genshi_text
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20250121-3.14.0a4+-4844db8/bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.036x faster

# HPT report

- Reliability score: 99.66% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x