# Results vs. 3.12.0

- fork: python
- ref: v3.14.0a5
- machine: linux-aarch64
- commit hash: 3ae9101
- commit date: 2025-02-11
- overall geometric mean: 1.005x faster
- HPT reliability: 80.30%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250211-arminc-aarch64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 319 ms: 1.04x slower                                         |
| docutils       | 2.98 sec                                                              | 3.26 sec: 1.09x slower                                       |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                 |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250211-arminc-aarch64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 401 ms: 1.56x faster                                         |
| async_tree_memoization     | 777 ms                                                                | 513 ms: 1.51x faster                                         |
| async_tree_io              | 1.41 sec                                                              | 936 ms: 1.51x faster                                         |
| async_tree_io_tg           | 1.40 sec                                                              | 933 ms: 1.51x faster                                         |
| async_tree_memoization_tg  | 740 ms                                                                | 505 ms: 1.47x faster                                         |
| async_tree_none_tg         | 577 ms                                                                | 399 ms: 1.45x faster                                         |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 701 ms: 1.30x faster                                         |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 679 ms: 1.30x faster                                         |
| Geometric mean             | (ref)                                                                 | 1.45x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250211-arminc-aarch64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 86.9 ms: 1.06x faster                                        |
| pidigits       | 233 ms                                                                | 242 ms: 1.04x slower                                         |
| nbody          | 105 ms                                                                | 125 ms: 1.19x slower                                         |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250211-arminc-aarch64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.10 ms: 1.13x faster                                        |
| regex_compile  | 137 ms                                                                | 125 ms: 1.09x faster                                         |
| regex_v8       | 28.3 ms                                                               | 33.3 ms: 1.18x slower                                        |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                 |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250211-arminc-aarch64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| tomli_loads          | 2.59 sec                                                              | 2.48 sec: 1.04x faster                                       |
| xml_etree_parse      | 195 ms                                                                | 188 ms: 1.04x faster                                         |
| unpickle_pure_python | 260 us                                                                | 275 us: 1.06x slower                                         |
| json_loads           | 30.7 us                                                               | 34.5 us: 1.12x slower                                        |
| pickle_pure_python   | 365 us                                                                | 426 us: 1.17x slower                                         |
| json_dumps           | 12.3 ms                                                               | 14.4 ms: 1.18x slower                                        |
| Geometric mean       | (ref)                                                                 | 1.05x slower                                                 |

Benchmark hidden because not significant (3): xml_etree_iterparse, xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250211-arminc-aarch64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.04 ms: 1.08x slower                                        |
| python_startup         | 11.4 ms                                                               | 16.4 ms: 1.45x slower                                        |
| Geometric mean         | (ref)                                                                 | 1.25x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250211-arminc-aarch64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 39.4 ms: 1.03x faster                                        |
| mako            | 12.9 ms                                                               | 13.7 ms: 1.06x slower                                        |
| genshi_text     | 27.4 ms                                                               | 30.0 ms: 1.09x slower                                        |
| genshi_xml      | 60.6 ms                                                               | 66.9 ms: 1.10x slower                                        |
| Geometric mean  | (ref)                                                                 | 1.06x slower                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250211-arminc-aarch64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 401 ms: 1.56x faster                                         |
| async_tree_memoization     | 777 ms                                                                | 513 ms: 1.51x faster                                         |
| async_tree_io              | 1.41 sec                                                              | 936 ms: 1.51x faster                                         |
| async_tree_io_tg           | 1.40 sec                                                              | 933 ms: 1.51x faster                                         |
| async_tree_memoization_tg  | 740 ms                                                                | 505 ms: 1.47x faster                                         |
| async_tree_none_tg         | 577 ms                                                                | 399 ms: 1.45x faster                                         |
| deepcopy                   | 446 us                                                                | 341 us: 1.30x faster                                         |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 701 ms: 1.30x faster                                         |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 679 ms: 1.30x faster                                         |
| deepcopy_memo              | 49.6 us                                                               | 39.3 us: 1.26x faster                                        |
| generators                 | 43.5 ms                                                               | 37.1 ms: 1.17x faster                                        |
| deepcopy_reduce            | 4.10 us                                                               | 3.58 us: 1.15x faster                                        |
| regex_effbot               | 4.64 ms                                                               | 4.10 ms: 1.13x faster                                        |
| spectral_norm              | 131 ms                                                                | 118 ms: 1.11x faster                                         |
| regex_compile              | 137 ms                                                                | 125 ms: 1.09x faster                                         |
| pylint                     | 355 ms                                                                | 327 ms: 1.09x faster                                         |
| pathlib                    | 24.5 ms                                                               | 22.7 ms: 1.08x faster                                        |
| logging_simple             | 7.63 us                                                               | 7.08 us: 1.08x faster                                        |
| logging_format             | 8.34 us                                                               | 7.77 us: 1.07x faster                                        |
| sqlalchemy_imperative      | 16.7 ms                                                               | 15.6 ms: 1.07x faster                                        |
| float                      | 92.1 ms                                                               | 86.9 ms: 1.06x faster                                        |
| sqlalchemy_declarative     | 157 ms                                                                | 150 ms: 1.05x faster                                         |
| tomli_loads                | 2.59 sec                                                              | 2.48 sec: 1.04x faster                                       |
| raytrace                   | 353 ms                                                                | 338 ms: 1.04x faster                                         |
| chaos                      | 71.4 ms                                                               | 68.5 ms: 1.04x faster                                        |
| xml_etree_parse            | 195 ms                                                                | 188 ms: 1.04x faster                                         |
| comprehensions             | 25.4 us                                                               | 24.5 us: 1.04x faster                                        |
| sympy_sum                  | 154 ms                                                                | 149 ms: 1.03x faster                                         |
| django_template            | 40.7 ms                                                               | 39.4 ms: 1.03x faster                                        |
| sqlglot_normalize          | 126 ms                                                                | 128 ms: 1.02x slower                                         |
| bench_thread_pool          | 1.31 ms                                                               | 1.35 ms: 1.03x slower                                        |
| 2to3                       | 308 ms                                                                | 319 ms: 1.04x slower                                         |
| pyflate                    | 559 ms                                                                | 580 ms: 1.04x slower                                         |
| scimark_sor                | 150 ms                                                                | 155 ms: 1.04x slower                                         |
| pidigits                   | 233 ms                                                                | 242 ms: 1.04x slower                                         |
| thrift                     | 937 us                                                                | 978 us: 1.04x slower                                         |
| mdp                        | 3.41 sec                                                              | 3.57 sec: 1.05x slower                                       |
| go                         | 157 ms                                                                | 165 ms: 1.05x slower                                         |
| mako                       | 12.9 ms                                                               | 13.7 ms: 1.06x slower                                        |
| unpickle_pure_python       | 260 us                                                                | 275 us: 1.06x slower                                         |
| sqlglot_parse              | 1.46 ms                                                               | 1.56 ms: 1.07x slower                                        |
| sqlite_synth               | 3.77 us                                                               | 4.07 us: 1.08x slower                                        |
| python_startup_no_site     | 8.37 ms                                                               | 9.04 ms: 1.08x slower                                        |
| json                       | 5.54 ms                                                               | 6.06 ms: 1.09x slower                                        |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.77 ms: 1.09x slower                                        |
| docutils                   | 2.98 sec                                                              | 3.26 sec: 1.09x slower                                       |
| genshi_text                | 27.4 ms                                                               | 30.0 ms: 1.09x slower                                        |
| sympy_expand               | 454 ms                                                                | 497 ms: 1.10x slower                                         |
| logging_silent             | 127 ns                                                                | 140 ns: 1.10x slower                                         |
| genshi_xml                 | 60.6 ms                                                               | 66.9 ms: 1.10x slower                                        |
| crypto_pyaes               | 86.6 ms                                                               | 96.3 ms: 1.11x slower                                        |
| dulwich_log                | 62.0 ms                                                               | 69.2 ms: 1.12x slower                                        |
| sqlglot_optimize           | 61.3 ms                                                               | 68.6 ms: 1.12x slower                                        |
| json_loads                 | 30.7 us                                                               | 34.5 us: 1.12x slower                                        |
| coverage                   | 87.3 ms                                                               | 98.2 ms: 1.12x slower                                        |
| telco                      | 8.51 ms                                                               | 9.68 ms: 1.14x slower                                        |
| pycparser                  | 1.26 sec                                                              | 1.43 sec: 1.14x slower                                       |
| meteor_contest             | 112 ms                                                                | 129 ms: 1.16x slower                                         |
| pickle_pure_python         | 365 us                                                                | 426 us: 1.17x slower                                         |
| regex_v8                   | 28.3 ms                                                               | 33.3 ms: 1.18x slower                                        |
| json_dumps                 | 12.3 ms                                                               | 14.4 ms: 1.18x slower                                        |
| nbody                      | 105 ms                                                                | 125 ms: 1.19x slower                                         |
| typing_runtime_protocols   | 181 us                                                                | 218 us: 1.21x slower                                         |
| nqueens                    | 99.2 ms                                                               | 122 ms: 1.23x slower                                         |
| fannkuch                   | 443 ms                                                                | 548 ms: 1.24x slower                                         |
| hexiom                     | 6.98 ms                                                               | 8.94 ms: 1.28x slower                                        |
| pprint_pformat             | 1.88 sec                                                              | 2.72 sec: 1.44x slower                                       |
| pprint_safe_repr           | 916 ms                                                                | 1.32 sec: 1.44x slower                                       |
| python_startup             | 11.4 ms                                                               | 16.4 ms: 1.45x slower                                        |
| gc_traversal               | 4.40 ms                                                               | 6.85 ms: 1.56x slower                                        |
| create_gc_cycles           | 1.92 ms                                                               | 3.64 ms: 1.90x slower                                        |
| bench_mp_pool              | 7.05 ms                                                               | 3.45 sec: 488.66x slower                                     |
| Geometric mean             | (ref)                                                                 | 1.09x slower                                                 |

Benchmark hidden because not significant (17): xml_etree_iterparse, scimark_lu, html5lib, async_generators, scimark_monte_carlo, scimark_fft, xml_etree_process, richards_super, coroutines, xml_etree_generate, deltablue, asyncio_websockets, sympy_str, regex_dna, sympy_integrate, sqlglot_transpile, richards
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20250211-3.14.0a5-3ae9101-JIT/bm-20250211-arminc-aarch64-python-v3.14.0a5-3.14.0a5-3ae9101.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.005x faster

# HPT report

- Reliability score: 80.30% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x