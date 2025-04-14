# Results vs. 3.12.0

- fork: diegorusso
- ref: remove_jumps_aarch64
- machine: linux-aarch64
- commit hash: 460d0d3
- commit date: 2025-03-10
- overall geometric mean: 1.056x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250310-arminc-aarch64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 300 ms: 1.03x faster                                                         |
| docutils       | 2.98 sec                                                              | 3.07 sec: 1.03x slower                                                       |
| html5lib       | 65.1 ms                                                               | 61.5 ms: 1.06x faster                                                        |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250310-arminc-aarch64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|----------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 465 ms: 1.67x faster                                                         |
| async_tree_none            | 624 ms                                                                | 380 ms: 1.64x faster                                                         |
| async_tree_io              | 1.41 sec                                                              | 870 ms: 1.62x faster                                                         |
| async_tree_io_tg           | 1.40 sec                                                              | 883 ms: 1.59x faster                                                         |
| async_tree_memoization_tg  | 740 ms                                                                | 471 ms: 1.57x faster                                                         |
| async_tree_none_tg         | 577 ms                                                                | 369 ms: 1.56x faster                                                         |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 652 ms: 1.40x faster                                                         |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 644 ms: 1.37x faster                                                         |
| Geometric mean             | (ref)                                                                 | 1.55x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250310-arminc-aarch64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 82.7 ms: 1.11x faster                                                        |
| nbody          | 105 ms                                                                | 117 ms: 1.12x slower                                                         |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250310-arminc-aarch64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.92 ms: 1.18x faster                                                        |
| regex_compile  | 137 ms                                                                | 122 ms: 1.13x faster                                                         |
| regex_dna      | 254 ms                                                                | 249 ms: 1.02x faster                                                         |
| regex_v8       | 28.3 ms                                                               | 28.0 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                                 | 1.08x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250310-arminc-aarch64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.59 sec                                                              | 2.31 sec: 1.12x faster                                                       |
| xml_etree_parse      | 195 ms                                                                | 175 ms: 1.11x faster                                                         |
| xml_etree_iterparse  | 150 ms                                                                | 142 ms: 1.06x faster                                                         |
| xml_etree_generate   | 112 ms                                                                | 108 ms: 1.04x faster                                                         |
| unpickle_pure_python | 260 us                                                                | 251 us: 1.04x faster                                                         |
| xml_etree_process    | 79.0 ms                                                               | 76.3 ms: 1.03x faster                                                        |
| pickle_pure_python   | 365 us                                                                | 392 us: 1.07x slower                                                         |
| json_loads           | 30.7 us                                                               | 34.1 us: 1.11x slower                                                        |
| json_dumps           | 12.3 ms                                                               | 14.2 ms: 1.16x slower                                                        |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250310-arminc-aarch64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 10.1 ms: 1.21x slower                                                        |
| python_startup         | 11.4 ms                                                               | 16.1 ms: 1.42x slower                                                        |
| Geometric mean         | (ref)                                                                 | 1.31x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250310-arminc-aarch64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 38.5 ms: 1.06x faster                                                        |
| genshi_text     | 27.4 ms                                                               | 26.5 ms: 1.04x faster                                                        |
| mako            | 12.9 ms                                                               | 12.5 ms: 1.03x faster                                                        |
| genshi_xml      | 60.6 ms                                                               | 60.0 ms: 1.01x faster                                                        |
| Geometric mean  | (ref)                                                                 | 1.03x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250310-arminc-aarch64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3 |
|----------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 465 ms: 1.67x faster                                                         |
| async_tree_none            | 624 ms                                                                | 380 ms: 1.64x faster                                                         |
| async_tree_io              | 1.41 sec                                                              | 870 ms: 1.62x faster                                                         |
| async_tree_io_tg           | 1.40 sec                                                              | 883 ms: 1.59x faster                                                         |
| async_tree_memoization_tg  | 740 ms                                                                | 471 ms: 1.57x faster                                                         |
| async_tree_none_tg         | 577 ms                                                                | 369 ms: 1.56x faster                                                         |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 652 ms: 1.40x faster                                                         |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 644 ms: 1.37x faster                                                         |
| deepcopy                   | 446 us                                                                | 330 us: 1.35x faster                                                         |
| deepcopy_memo              | 49.6 us                                                               | 37.6 us: 1.32x faster                                                        |
| generators                 | 43.5 ms                                                               | 35.7 ms: 1.22x faster                                                        |
| deepcopy_reduce            | 4.10 us                                                               | 3.42 us: 1.20x faster                                                        |
| regex_effbot               | 4.64 ms                                                               | 3.92 ms: 1.18x faster                                                        |
| dulwich_log                | 62.0 ms                                                               | 53.8 ms: 1.15x faster                                                        |
| pylint                     | 355 ms                                                                | 313 ms: 1.13x faster                                                         |
| richards_super             | 58.5 ms                                                               | 51.7 ms: 1.13x faster                                                        |
| regex_compile              | 137 ms                                                                | 122 ms: 1.13x faster                                                         |
| raytrace                   | 353 ms                                                                | 314 ms: 1.13x faster                                                         |
| tomli_loads                | 2.59 sec                                                              | 2.31 sec: 1.12x faster                                                       |
| richards                   | 50.9 ms                                                               | 45.7 ms: 1.11x faster                                                        |
| spectral_norm              | 131 ms                                                                | 117 ms: 1.11x faster                                                         |
| float                      | 92.1 ms                                                               | 82.7 ms: 1.11x faster                                                        |
| logging_simple             | 7.63 us                                                               | 6.86 us: 1.11x faster                                                        |
| xml_etree_parse            | 195 ms                                                                | 175 ms: 1.11x faster                                                         |
| logging_format             | 8.34 us                                                               | 7.57 us: 1.10x faster                                                        |
| sqlalchemy_declarative     | 157 ms                                                                | 145 ms: 1.09x faster                                                         |
| scimark_fft                | 418 ms                                                                | 385 ms: 1.09x faster                                                         |
| comprehensions             | 25.4 us                                                               | 23.4 us: 1.08x faster                                                        |
| deltablue                  | 4.12 ms                                                               | 3.81 ms: 1.08x faster                                                        |
| pathlib                    | 24.5 ms                                                               | 22.7 ms: 1.08x faster                                                        |
| sqlalchemy_imperative      | 16.7 ms                                                               | 15.5 ms: 1.07x faster                                                        |
| async_generators           | 491 ms                                                                | 458 ms: 1.07x faster                                                         |
| xml_etree_iterparse        | 150 ms                                                                | 142 ms: 1.06x faster                                                         |
| chaos                      | 71.4 ms                                                               | 67.4 ms: 1.06x faster                                                        |
| scimark_lu                 | 146 ms                                                                | 138 ms: 1.06x faster                                                         |
| html5lib                   | 65.1 ms                                                               | 61.5 ms: 1.06x faster                                                        |
| django_template            | 40.7 ms                                                               | 38.5 ms: 1.06x faster                                                        |
| sympy_sum                  | 154 ms                                                                | 147 ms: 1.05x faster                                                         |
| sympy_str                  | 280 ms                                                                | 268 ms: 1.04x faster                                                         |
| coroutines                 | 29.0 ms                                                               | 27.8 ms: 1.04x faster                                                        |
| xml_etree_generate         | 112 ms                                                                | 108 ms: 1.04x faster                                                         |
| sqlite_synth               | 3.77 us                                                               | 3.63 us: 1.04x faster                                                        |
| genshi_text                | 27.4 ms                                                               | 26.5 ms: 1.04x faster                                                        |
| unpickle_pure_python       | 260 us                                                                | 251 us: 1.04x faster                                                         |
| xml_etree_process          | 79.0 ms                                                               | 76.3 ms: 1.03x faster                                                        |
| pyflate                    | 559 ms                                                                | 540 ms: 1.03x faster                                                         |
| thrift                     | 937 us                                                                | 906 us: 1.03x faster                                                         |
| mdp                        | 3.41 sec                                                              | 3.30 sec: 1.03x faster                                                       |
| mako                       | 12.9 ms                                                               | 12.5 ms: 1.03x faster                                                        |
| 2to3                       | 308 ms                                                                | 300 ms: 1.03x faster                                                         |
| regex_dna                  | 254 ms                                                                | 249 ms: 1.02x faster                                                         |
| regex_v8                   | 28.3 ms                                                               | 28.0 ms: 1.01x faster                                                        |
| genshi_xml                 | 60.6 ms                                                               | 60.0 ms: 1.01x faster                                                        |
| go                         | 157 ms                                                                | 161 ms: 1.03x slower                                                         |
| sympy_expand               | 454 ms                                                                | 466 ms: 1.03x slower                                                         |
| docutils                   | 2.98 sec                                                              | 3.07 sec: 1.03x slower                                                       |
| fannkuch                   | 443 ms                                                                | 457 ms: 1.03x slower                                                         |
| bench_thread_pool          | 1.31 ms                                                               | 1.35 ms: 1.03x slower                                                        |
| nqueens                    | 99.2 ms                                                               | 102 ms: 1.03x slower                                                         |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.41 ms: 1.03x slower                                                        |
| logging_silent             | 127 ns                                                                | 132 ns: 1.04x slower                                                         |
| json                       | 5.54 ms                                                               | 5.80 ms: 1.05x slower                                                        |
| meteor_contest             | 112 ms                                                                | 118 ms: 1.05x slower                                                         |
| pycparser                  | 1.26 sec                                                              | 1.33 sec: 1.06x slower                                                       |
| pickle_pure_python         | 365 us                                                                | 392 us: 1.07x slower                                                         |
| crypto_pyaes               | 86.6 ms                                                               | 93.5 ms: 1.08x slower                                                        |
| telco                      | 8.51 ms                                                               | 9.24 ms: 1.09x slower                                                        |
| hexiom                     | 6.98 ms                                                               | 7.57 ms: 1.09x slower                                                        |
| json_loads                 | 30.7 us                                                               | 34.1 us: 1.11x slower                                                        |
| nbody                      | 105 ms                                                                | 117 ms: 1.12x slower                                                         |
| coverage                   | 87.3 ms                                                               | 97.5 ms: 1.12x slower                                                        |
| typing_runtime_protocols   | 181 us                                                                | 204 us: 1.13x slower                                                         |
| json_dumps                 | 12.3 ms                                                               | 14.2 ms: 1.16x slower                                                        |
| pprint_safe_repr           | 916 ms                                                                | 1.11 sec: 1.21x slower                                                       |
| python_startup_no_site     | 8.37 ms                                                               | 10.1 ms: 1.21x slower                                                        |
| pprint_pformat             | 1.88 sec                                                              | 2.31 sec: 1.23x slower                                                       |
| python_startup             | 11.4 ms                                                               | 16.1 ms: 1.42x slower                                                        |
| gc_traversal               | 4.40 ms                                                               | 6.57 ms: 1.49x slower                                                        |
| create_gc_cycles           | 1.92 ms                                                               | 3.73 ms: 1.95x slower                                                        |
| bench_mp_pool              | 7.05 ms                                                               | 2.82 sec: 399.94x slower                                                     |
| Geometric mean             | (ref)                                                                 | 1.02x slower                                                                 |

Benchmark hidden because not significant (5): scimark_monte_carlo, sympy_integrate, asyncio_websockets, scimark_sor, pidigits
Ignored benchmarks (17) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250310-3.14.0a5+-460d0d3-JIT/bm-20250310-arminc-aarch64-diegorusso-remove_jumps_aarch64-3.14.0a5+-460d0d3.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.056x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.06x