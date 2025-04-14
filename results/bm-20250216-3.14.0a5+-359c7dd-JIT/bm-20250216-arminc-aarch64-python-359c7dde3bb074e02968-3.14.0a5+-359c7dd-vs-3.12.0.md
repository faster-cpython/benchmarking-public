# Results vs. 3.12.0

- fork: python
- ref: 359c7dde3bb074e02968
- machine: linux-aarch64
- commit hash: 359c7dd
- commit date: 2025-02-16
- overall geometric mean: 1.002x faster
- HPT reliability: 72.22%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 322 ms: 1.05x slower                                                     |
| docutils       | 2.98 sec                                                              | 3.23 sec: 1.08x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                             |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 411 ms: 1.52x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 514 ms: 1.51x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 941 ms: 1.49x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 948 ms: 1.49x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 509 ms: 1.46x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 405 ms: 1.43x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 704 ms: 1.30x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 690 ms: 1.28x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.43x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 88.8 ms: 1.04x faster                                                    |
| pidigits       | 233 ms                                                                | 242 ms: 1.04x slower                                                     |
| nbody          | 105 ms                                                                | 124 ms: 1.19x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.06x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.92 ms: 1.18x faster                                                    |
| regex_compile  | 137 ms                                                                | 127 ms: 1.08x faster                                                     |
| regex_dna      | 254 ms                                                                | 246 ms: 1.03x faster                                                     |
| regex_v8       | 28.3 ms                                                               | 32.8 ms: 1.16x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 182 ms: 1.07x faster                                                     |
| tomli_loads          | 2.59 sec                                                              | 2.50 sec: 1.04x faster                                                   |
| xml_etree_process    | 79.0 ms                                                               | 83.9 ms: 1.06x slower                                                    |
| unpickle_list        | 6.17 us                                                               | 6.59 us: 1.07x slower                                                    |
| unpickle_pure_python | 260 us                                                                | 282 us: 1.08x slower                                                     |
| pickle_dict          | 37.3 us                                                               | 41.1 us: 1.10x slower                                                    |
| json_loads           | 30.7 us                                                               | 34.7 us: 1.13x slower                                                    |
| pickle_pure_python   | 365 us                                                                | 416 us: 1.14x slower                                                     |
| pickle_list          | 5.25 us                                                               | 6.07 us: 1.16x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 14.9 ms: 1.21x slower                                                    |
| pickle               | 13.4 us                                                               | 16.9 us: 1.26x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.08x slower                                                             |

Benchmark hidden because not significant (3): unpickle, xml_etree_iterparse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.11 ms: 1.09x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.4 ms: 1.44x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.25x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako           | 12.9 ms                                                               | 14.1 ms: 1.09x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                             |

Benchmark hidden because not significant (3): genshi_text, django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 411 ms: 1.52x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 514 ms: 1.51x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 941 ms: 1.49x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 948 ms: 1.49x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 509 ms: 1.46x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 405 ms: 1.43x faster                                                     |
| deepcopy                   | 446 us                                                                | 341 us: 1.31x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 704 ms: 1.30x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 690 ms: 1.28x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 40.5 us: 1.23x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 3.92 ms: 1.18x faster                                                    |
| generators                 | 43.5 ms                                                               | 37.0 ms: 1.18x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.60 us: 1.14x faster                                                    |
| pylint                     | 355 ms                                                                | 319 ms: 1.11x faster                                                     |
| regex_compile              | 137 ms                                                                | 127 ms: 1.08x faster                                                     |
| spectral_norm              | 131 ms                                                                | 121 ms: 1.08x faster                                                     |
| pathlib                    | 24.5 ms                                                               | 22.8 ms: 1.08x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 182 ms: 1.07x faster                                                     |
| logging_format             | 8.34 us                                                               | 7.80 us: 1.07x faster                                                    |
| raytrace                   | 353 ms                                                                | 333 ms: 1.06x faster                                                     |
| logging_simple             | 7.63 us                                                               | 7.25 us: 1.05x faster                                                    |
| scimark_lu                 | 146 ms                                                                | 140 ms: 1.04x faster                                                     |
| tomli_loads                | 2.59 sec                                                              | 2.50 sec: 1.04x faster                                                   |
| float                      | 92.1 ms                                                               | 88.8 ms: 1.04x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 149 ms: 1.03x faster                                                     |
| comprehensions             | 25.4 us                                                               | 24.6 us: 1.03x faster                                                    |
| regex_dna                  | 254 ms                                                                | 246 ms: 1.03x faster                                                     |
| sqlalchemy_imperative      | 16.7 ms                                                               | 16.3 ms: 1.02x faster                                                    |
| thrift                     | 937 us                                                                | 942 us: 1.01x slower                                                     |
| mdp                        | 3.41 sec                                                              | 3.46 sec: 1.01x slower                                                   |
| deltablue                  | 4.12 ms                                                               | 4.18 ms: 1.02x slower                                                    |
| go                         | 157 ms                                                                | 160 ms: 1.02x slower                                                     |
| asyncio_websockets         | 658 ms                                                                | 673 ms: 1.02x slower                                                     |
| dulwich_log                | 62.0 ms                                                               | 64.5 ms: 1.04x slower                                                    |
| pidigits                   | 233 ms                                                                | 242 ms: 1.04x slower                                                     |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.28 sec: 1.04x slower                                                   |
| sqlite_synth               | 3.77 us                                                               | 3.93 us: 1.04x slower                                                    |
| scimark_sor                | 150 ms                                                                | 156 ms: 1.04x slower                                                     |
| sqlglot_normalize          | 126 ms                                                                | 131 ms: 1.05x slower                                                     |
| 2to3                       | 308 ms                                                                | 322 ms: 1.05x slower                                                     |
| scimark_fft                | 418 ms                                                                | 438 ms: 1.05x slower                                                     |
| richards                   | 50.9 ms                                                               | 53.9 ms: 1.06x slower                                                    |
| xml_etree_process          | 79.0 ms                                                               | 83.9 ms: 1.06x slower                                                    |
| logging_silent             | 127 ns                                                                | 135 ns: 1.07x slower                                                     |
| sqlglot_transpile          | 1.83 ms                                                               | 1.95 ms: 1.07x slower                                                    |
| richards_super             | 58.5 ms                                                               | 62.4 ms: 1.07x slower                                                    |
| unpickle_list              | 6.17 us                                                               | 6.59 us: 1.07x slower                                                    |
| json                       | 5.54 ms                                                               | 5.92 ms: 1.07x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 106 ms: 1.07x slower                                                     |
| sympy_integrate            | 21.6 ms                                                               | 23.2 ms: 1.07x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.23 sec: 1.08x slower                                                   |
| unpickle_pure_python       | 260 us                                                                | 282 us: 1.08x slower                                                     |
| sqlglot_optimize           | 61.3 ms                                                               | 66.6 ms: 1.09x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 9.11 ms: 1.09x slower                                                    |
| mako                       | 12.9 ms                                                               | 14.1 ms: 1.09x slower                                                    |
| pickle_dict                | 37.3 us                                                               | 41.1 us: 1.10x slower                                                    |
| sympy_expand               | 454 ms                                                                | 500 ms: 1.10x slower                                                     |
| sqlglot_parse              | 1.46 ms                                                               | 1.64 ms: 1.12x slower                                                    |
| meteor_contest             | 112 ms                                                                | 126 ms: 1.13x slower                                                     |
| json_loads                 | 30.7 us                                                               | 34.7 us: 1.13x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 416 us: 1.14x slower                                                     |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.07 ms: 1.14x slower                                                    |
| telco                      | 8.51 ms                                                               | 9.74 ms: 1.14x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.45 sec: 1.15x slower                                                   |
| pickle_list                | 5.25 us                                                               | 6.07 us: 1.16x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 32.8 ms: 1.16x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 101 ms: 1.17x slower                                                     |
| coverage                   | 87.3 ms                                                               | 103 ms: 1.18x slower                                                     |
| nbody                      | 105 ms                                                                | 124 ms: 1.19x slower                                                     |
| json_dumps                 | 12.3 ms                                                               | 14.9 ms: 1.21x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 222 us: 1.23x slower                                                     |
| hexiom                     | 6.98 ms                                                               | 8.60 ms: 1.23x slower                                                    |
| fannkuch                   | 443 ms                                                                | 552 ms: 1.24x slower                                                     |
| pickle                     | 13.4 us                                                               | 16.9 us: 1.26x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 1.27 sec: 1.38x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 2.64 sec: 1.40x slower                                                   |
| python_startup             | 11.4 ms                                                               | 16.4 ms: 1.44x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.98 ms: 1.59x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.72 ms: 1.94x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 2.72 sec: 385.28x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.09x slower                                                             |

Benchmark hidden because not significant (16): unpickle, sqlalchemy_declarative, chaos, async_generators, asyncio_tcp, html5lib, xml_etree_iterparse, genshi_text, pyflate, scimark_monte_carlo, sympy_str, coroutines, xml_etree_generate, django_template, genshi_xml, bench_thread_pool
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
Ignored benchmarks (8) of results/bm-20250216-3.14.0a5+-359c7dd-JIT/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.002x faster

# HPT report

- Reliability score: 72.22% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x