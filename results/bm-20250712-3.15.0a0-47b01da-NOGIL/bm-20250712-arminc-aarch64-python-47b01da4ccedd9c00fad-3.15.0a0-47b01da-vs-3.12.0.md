# Results vs. 3.12.0

- fork: python
- ref: 47b01da4ccedd9c00fad
- machine: linux-aarch64
- commit hash: 47b01da
- commit date: 2025-07-12
- overall geometric mean: 1.089x slower
- HPT reliability: 99.73%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 349 ms: 1.13x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.19 sec: 1.07x slower                                                  |
| html5lib       | 65.1 ms                                                               | 70.2 ms: 1.08x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.09x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 854 ms: 1.64x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 459 ms: 1.61x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 875 ms: 1.61x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 487 ms: 1.59x faster                                                    |
| async_tree_none            | 624 ms                                                                | 407 ms: 1.53x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 378 ms: 1.53x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 643 ms: 1.37x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 683 ms: 1.34x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.53x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 232 ms: 1.00x faster                                                    |
| float          | 92.1 ms                                                               | 95.6 ms: 1.04x slower                                                   |
| nbody          | 105 ms                                                                | 181 ms: 1.73x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.21x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.94 ms: 1.18x faster                                                   |
| regex_v8       | 28.3 ms                                                               | 26.0 ms: 1.09x faster                                                   |
| regex_dna      | 254 ms                                                                | 237 ms: 1.07x faster                                                    |
| regex_compile  | 137 ms                                                                | 149 ms: 1.09x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_iterparse  | 150 ms                                                                | 133 ms: 1.13x faster                                                    |
| xml_etree_parse      | 195 ms                                                                | 183 ms: 1.07x faster                                                    |
| pickle_dict          | 37.3 us                                                               | 38.4 us: 1.03x slower                                                   |
| pickle_list          | 5.25 us                                                               | 5.65 us: 1.08x slower                                                   |
| tomli_loads          | 2.59 sec                                                              | 2.87 sec: 1.11x slower                                                  |
| unpickle             | 18.5 us                                                               | 20.4 us: 1.11x slower                                                   |
| unpickle_list        | 6.17 us                                                               | 6.94 us: 1.12x slower                                                   |
| pickle               | 13.4 us                                                               | 15.7 us: 1.17x slower                                                   |
| unpickle_pure_python | 260 us                                                                | 303 us: 1.17x slower                                                    |
| json_loads           | 30.7 us                                                               | 36.5 us: 1.19x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 14.8 ms: 1.21x slower                                                   |
| pickle_pure_python   | 365 us                                                                | 450 us: 1.23x slower                                                    |
| xml_etree_generate   | 112 ms                                                                | 140 ms: 1.25x slower                                                    |
| xml_etree_process    | 79.0 ms                                                               | 101 ms: 1.28x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.12x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 12.1 ms: 1.45x slower                                                   |
| python_startup         | 11.4 ms                                                               | 20.0 ms: 1.76x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.60x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 75.2 ms: 1.24x slower                                                   |
| django_template | 40.7 ms                                                               | 51.3 ms: 1.26x slower                                                   |
| genshi_text     | 27.4 ms                                                               | 35.2 ms: 1.28x slower                                                   |
| mako            | 12.9 ms                                                               | 21.1 ms: 1.64x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.35x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.92 sec: 1.77x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 854 ms: 1.64x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 459 ms: 1.61x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 875 ms: 1.61x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 487 ms: 1.59x faster                                                    |
| gc_traversal               | 4.40 ms                                                               | 2.87 ms: 1.53x faster                                                   |
| async_tree_none            | 624 ms                                                                | 407 ms: 1.53x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 378 ms: 1.53x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 643 ms: 1.37x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 683 ms: 1.34x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 3.94 ms: 1.18x faster                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 133 ms: 1.13x faster                                                    |
| deepcopy                   | 446 us                                                                | 394 us: 1.13x faster                                                    |
| sqlite_synth               | 3.77 us                                                               | 3.39 us: 1.11x faster                                                   |
| generators                 | 43.5 ms                                                               | 39.8 ms: 1.09x faster                                                   |
| regex_v8                   | 28.3 ms                                                               | 26.0 ms: 1.09x faster                                                   |
| regex_dna                  | 254 ms                                                                | 237 ms: 1.07x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 46.5 us: 1.07x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 183 ms: 1.07x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 23.0 ms: 1.07x faster                                                   |
| dulwich_log                | 62.0 ms                                                               | 59.5 ms: 1.04x faster                                                   |
| go                         | 157 ms                                                                | 153 ms: 1.03x faster                                                    |
| pidigits                   | 233 ms                                                                | 232 ms: 1.00x faster                                                    |
| asyncio_websockets         | 658 ms                                                                | 667 ms: 1.01x slower                                                    |
| pickle_dict                | 37.3 us                                                               | 38.4 us: 1.03x slower                                                   |
| async_generators           | 491 ms                                                                | 505 ms: 1.03x slower                                                    |
| float                      | 92.1 ms                                                               | 95.6 ms: 1.04x slower                                                   |
| coroutines                 | 29.0 ms                                                               | 30.4 ms: 1.05x slower                                                   |
| pylint                     | 355 ms                                                                | 374 ms: 1.05x slower                                                    |
| pyflate                    | 559 ms                                                                | 592 ms: 1.06x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.19 sec: 1.07x slower                                                  |
| logging_simple             | 7.63 us                                                               | 8.21 us: 1.07x slower                                                   |
| pickle_list                | 5.25 us                                                               | 5.65 us: 1.08x slower                                                   |
| html5lib                   | 65.1 ms                                                               | 70.2 ms: 1.08x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 1.36 sec: 1.08x slower                                                  |
| deepcopy_reduce            | 4.10 us                                                               | 4.45 us: 1.09x slower                                                   |
| regex_compile              | 137 ms                                                                | 149 ms: 1.09x slower                                                    |
| logging_format             | 8.34 us                                                               | 9.07 us: 1.09x slower                                                   |
| scimark_sor                | 150 ms                                                                | 163 ms: 1.09x slower                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.87 sec: 1.11x slower                                                  |
| unpickle                   | 18.5 us                                                               | 20.4 us: 1.11x slower                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.42 sec: 1.11x slower                                                  |
| spectral_norm              | 131 ms                                                                | 145 ms: 1.11x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 7.81 ms: 1.12x slower                                                   |
| unpickle_list              | 6.17 us                                                               | 6.94 us: 1.12x slower                                                   |
| logging_silent             | 127 ns                                                                | 143 ns: 1.12x slower                                                    |
| chaos                      | 71.4 ms                                                               | 80.5 ms: 1.13x slower                                                   |
| scimark_fft                | 418 ms                                                                | 473 ms: 1.13x slower                                                    |
| json                       | 5.54 ms                                                               | 6.26 ms: 1.13x slower                                                   |
| 2to3                       | 308 ms                                                                | 349 ms: 1.13x slower                                                    |
| raytrace                   | 353 ms                                                                | 401 ms: 1.13x slower                                                    |
| deltablue                  | 4.12 ms                                                               | 4.68 ms: 1.14x slower                                                   |
| pprint_safe_repr           | 916 ms                                                                | 1.05 sec: 1.15x slower                                                  |
| pprint_pformat             | 1.88 sec                                                              | 2.17 sec: 1.15x slower                                                  |
| sympy_integrate            | 21.6 ms                                                               | 25.0 ms: 1.16x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.24 ms: 1.17x slower                                                   |
| pickle                     | 13.4 us                                                               | 15.7 us: 1.17x slower                                                   |
| unpickle_pure_python       | 260 us                                                                | 303 us: 1.17x slower                                                    |
| sympy_sum                  | 154 ms                                                                | 183 ms: 1.18x slower                                                    |
| json_loads                 | 30.7 us                                                               | 36.5 us: 1.19x slower                                                   |
| sympy_str                  | 280 ms                                                                | 333 ms: 1.19x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 14.8 ms: 1.21x slower                                                   |
| nqueens                    | 99.2 ms                                                               | 121 ms: 1.22x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.56 ms: 1.22x slower                                                   |
| meteor_contest             | 112 ms                                                                | 137 ms: 1.22x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 450 us: 1.23x slower                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 105 ms: 1.24x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 107 ms: 1.24x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 75.2 ms: 1.24x slower                                                   |
| xml_etree_generate         | 112 ms                                                                | 140 ms: 1.25x slower                                                    |
| django_template            | 40.7 ms                                                               | 51.3 ms: 1.26x slower                                                   |
| thrift                     | 937 us                                                                | 1.19 ms: 1.27x slower                                                   |
| genshi_text                | 27.4 ms                                                               | 35.2 ms: 1.28x slower                                                   |
| xml_etree_process          | 79.0 ms                                                               | 101 ms: 1.28x slower                                                    |
| sympy_expand               | 454 ms                                                                | 586 ms: 1.29x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 189 ms: 1.30x slower                                                    |
| fannkuch                   | 443 ms                                                                | 597 ms: 1.35x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 246 us: 1.36x slower                                                    |
| richards                   | 50.9 ms                                                               | 69.8 ms: 1.37x slower                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.81 ms: 1.39x slower                                                   |
| richards_super             | 58.5 ms                                                               | 82.0 ms: 1.40x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 12.1 ms: 1.45x slower                                                   |
| coverage                   | 87.3 ms                                                               | 142 ms: 1.62x slower                                                    |
| mako                       | 12.9 ms                                                               | 21.1 ms: 1.64x slower                                                   |
| nbody                      | 105 ms                                                                | 181 ms: 1.73x slower                                                    |
| python_startup             | 11.4 ms                                                               | 20.0 ms: 1.76x slower                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 65.2 ms: 9.24x slower                                                   |
| telco                      | 8.51 ms                                                               | 190 ms: 22.31x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.13x slower                                                            |

Benchmark hidden because not significant (2): comprehensions, asyncio_tcp
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250712-3.15.0a0-47b01da-NOGIL/bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.089x slower

# HPT report

- Reliability score: 99.73% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.32x