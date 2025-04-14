# Results vs. 3.12.0

- fork: python
- ref: 359c7dde3bb074e02968
- machine: linux-aarch64
- commit hash: 359c7dd
- commit date: 2025-02-16
- overall geometric mean: 1.037x faster
- HPT reliability: 99.90%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| html5lib       | 65.1 ms                                                               | 62.1 ms: 1.05x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                             |

Benchmark hidden because not significant (2): 2to3, docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 401 ms: 1.55x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 502 ms: 1.55x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 489 ms: 1.52x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 936 ms: 1.50x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 942 ms: 1.50x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 403 ms: 1.43x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 686 ms: 1.33x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 684 ms: 1.29x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.46x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 88.3 ms: 1.04x faster                                                    |
| nbody          | 105 ms                                                                | 121 ms: 1.16x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.17 ms: 1.11x faster                                                    |
| regex_compile  | 137 ms                                                                | 129 ms: 1.07x faster                                                     |
| regex_dna      | 254 ms                                                                | 267 ms: 1.05x slower                                                     |
| regex_v8       | 28.3 ms                                                               | 32.7 ms: 1.15x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 184 ms: 1.06x faster                                                     |
| xml_etree_iterparse  | 150 ms                                                                | 145 ms: 1.04x faster                                                     |
| unpickle_pure_python | 260 us                                                                | 263 us: 1.01x slower                                                     |
| unpickle_list        | 6.17 us                                                               | 6.44 us: 1.04x slower                                                    |
| xml_etree_process    | 79.0 ms                                                               | 83.2 ms: 1.05x slower                                                    |
| pickle_dict          | 37.3 us                                                               | 39.5 us: 1.06x slower                                                    |
| pickle_pure_python   | 365 us                                                                | 409 us: 1.12x slower                                                     |
| pickle_list          | 5.25 us                                                               | 6.06 us: 1.15x slower                                                    |
| json_loads           | 30.7 us                                                               | 36.5 us: 1.19x slower                                                    |
| pickle               | 13.4 us                                                               | 16.3 us: 1.21x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 15.2 ms: 1.24x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.06x slower                                                             |

Benchmark hidden because not significant (3): unpickle, tomli_loads, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.08 ms: 1.08x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.3 ms: 1.43x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.25x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 39.0 ms: 1.04x faster                                                    |
| mako            | 12.9 ms                                                               | 14.1 ms: 1.10x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                             |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 401 ms: 1.55x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 502 ms: 1.55x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 489 ms: 1.52x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 936 ms: 1.50x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 942 ms: 1.50x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 403 ms: 1.43x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 686 ms: 1.33x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 684 ms: 1.29x faster                                                     |
| deepcopy                   | 446 us                                                                | 345 us: 1.29x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 41.0 us: 1.21x faster                                                    |
| comprehensions             | 25.4 us                                                               | 21.2 us: 1.20x faster                                                    |
| generators                 | 43.5 ms                                                               | 36.7 ms: 1.18x faster                                                    |
| pylint                     | 355 ms                                                                | 305 ms: 1.16x faster                                                     |
| go                         | 157 ms                                                                | 141 ms: 1.12x faster                                                     |
| sqlalchemy_imperative      | 16.7 ms                                                               | 15.0 ms: 1.11x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.17 ms: 1.11x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.71 us: 1.10x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 22.4 ms: 1.09x faster                                                    |
| raytrace                   | 353 ms                                                                | 325 ms: 1.09x faster                                                     |
| async_generators           | 491 ms                                                                | 454 ms: 1.08x faster                                                     |
| sympy_sum                  | 154 ms                                                                | 144 ms: 1.07x faster                                                     |
| sqlalchemy_declarative     | 157 ms                                                                | 147 ms: 1.07x faster                                                     |
| regex_compile              | 137 ms                                                                | 129 ms: 1.07x faster                                                     |
| spectral_norm              | 131 ms                                                                | 123 ms: 1.06x faster                                                     |
| xml_etree_parse            | 195 ms                                                                | 184 ms: 1.06x faster                                                     |
| logging_simple             | 7.63 us                                                               | 7.25 us: 1.05x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.96 us: 1.05x faster                                                    |
| html5lib                   | 65.1 ms                                                               | 62.1 ms: 1.05x faster                                                    |
| float                      | 92.1 ms                                                               | 88.3 ms: 1.04x faster                                                    |
| django_template            | 40.7 ms                                                               | 39.0 ms: 1.04x faster                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 145 ms: 1.04x faster                                                     |
| scimark_lu                 | 146 ms                                                                | 141 ms: 1.03x faster                                                     |
| asyncio_tcp                | 566 ms                                                                | 550 ms: 1.03x faster                                                     |
| unpickle_pure_python       | 260 us                                                                | 263 us: 1.01x slower                                                     |
| mdp                        | 3.41 sec                                                              | 3.46 sec: 1.01x slower                                                   |
| richards                   | 50.9 ms                                                               | 52.1 ms: 1.02x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 674 ms: 1.02x slower                                                     |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.24 sec: 1.03x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 1.29 sec: 1.03x slower                                                   |
| sympy_expand               | 454 ms                                                                | 466 ms: 1.03x slower                                                     |
| unpickle_list              | 6.17 us                                                               | 6.44 us: 1.04x slower                                                    |
| regex_dna                  | 254 ms                                                                | 267 ms: 1.05x slower                                                     |
| pprint_pformat             | 1.88 sec                                                              | 1.98 sec: 1.05x slower                                                   |
| xml_etree_process          | 79.0 ms                                                               | 83.2 ms: 1.05x slower                                                    |
| pyflate                    | 559 ms                                                                | 590 ms: 1.05x slower                                                     |
| pickle_dict                | 37.3 us                                                               | 39.5 us: 1.06x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 969 ms: 1.06x slower                                                     |
| hexiom                     | 6.98 ms                                                               | 7.47 ms: 1.07x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 4.07 us: 1.08x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 9.08 ms: 1.08x slower                                                    |
| json                       | 5.54 ms                                                               | 6.06 ms: 1.09x slower                                                    |
| logging_silent             | 127 ns                                                                | 139 ns: 1.09x slower                                                     |
| mako                       | 12.9 ms                                                               | 14.1 ms: 1.10x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 201 us: 1.11x slower                                                     |
| fannkuch                   | 443 ms                                                                | 494 ms: 1.11x slower                                                     |
| telco                      | 8.51 ms                                                               | 9.51 ms: 1.12x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 409 us: 1.12x slower                                                     |
| coverage                   | 87.3 ms                                                               | 99.5 ms: 1.14x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 32.7 ms: 1.15x slower                                                    |
| pickle_list                | 5.25 us                                                               | 6.06 us: 1.15x slower                                                    |
| nbody                      | 105 ms                                                                | 121 ms: 1.16x slower                                                     |
| json_loads                 | 30.7 us                                                               | 36.5 us: 1.19x slower                                                    |
| pickle                     | 13.4 us                                                               | 16.3 us: 1.21x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 15.2 ms: 1.24x slower                                                    |
| python_startup             | 11.4 ms                                                               | 16.3 ms: 1.43x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 7.03 ms: 1.60x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.57 ms: 1.86x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 5.29 sec: 749.66x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.06x slower                                                             |

Benchmark hidden because not significant (28): unpickle, chaos, deltablue, crypto_pyaes, dulwich_log, 2to3, sympy_str, tomli_loads, genshi_text, sqlglot_optimize, bench_thread_pool, sympy_integrate, scimark_fft, xml_etree_generate, sqlglot_parse, docutils, sqlglot_normalize, thrift, coroutines, nqueens, sqlglot_transpile, genshi_xml, scimark_monte_carlo, meteor_contest, scimark_sparse_mat_mult, scimark_sor, pidigits, richards_super
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
Ignored benchmarks (8) of results/bm-20250216-3.14.0a5+-359c7dd/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.037x faster

# HPT report

- Reliability score: 99.90% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x