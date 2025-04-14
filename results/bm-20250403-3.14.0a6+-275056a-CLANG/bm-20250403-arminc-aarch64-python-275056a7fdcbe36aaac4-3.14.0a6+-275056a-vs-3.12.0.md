# Results vs. 3.12.0

- fork: python
- ref: 275056a7fdcbe36aaac4
- machine: linux-aarch64
- commit hash: 275056a
- commit date: 2025-04-03
- overall geometric mean: 1.084x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250403-arminc-aarch64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 288 ms: 1.07x faster                                                     |
| docutils       | 2.98 sec                                                              | 2.90 sec: 1.03x faster                                                   |
| html5lib       | 65.1 ms                                                               | 59.5 ms: 1.09x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250403-arminc-aarch64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 455 ms: 1.71x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 456 ms: 1.62x faster                                                     |
| async_tree_none            | 624 ms                                                                | 387 ms: 1.61x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 884 ms: 1.60x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 883 ms: 1.59x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 370 ms: 1.56x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 721 ms: 1.26x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 706 ms: 1.25x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.52x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250403-arminc-aarch64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 84.1 ms: 1.10x faster                                                    |
| nbody          | 105 ms                                                                | 124 ms: 1.19x slower                                                     |
| pidigits       | 233 ms                                                                | 294 ms: 1.26x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.11x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250403-arminc-aarch64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 124 ms: 1.11x faster                                                     |
| regex_effbot   | 4.64 ms                                                               | 4.24 ms: 1.09x faster                                                    |
| regex_dna      | 254 ms                                                                | 239 ms: 1.06x faster                                                     |
| regex_v8       | 28.3 ms                                                               | 30.1 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.05x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250403-arminc-aarch64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 2.59 sec                                                              | 2.32 sec: 1.12x faster                                                   |
| xml_etree_generate   | 112 ms                                                                | 104 ms: 1.08x faster                                                     |
| xml_etree_process    | 79.0 ms                                                               | 74.0 ms: 1.07x faster                                                    |
| unpickle_pure_python | 260 us                                                                | 249 us: 1.05x faster                                                     |
| xml_etree_parse      | 195 ms                                                                | 207 ms: 1.06x slower                                                     |
| json_loads           | 30.7 us                                                               | 33.2 us: 1.08x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 14.2 ms: 1.15x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                             |

Benchmark hidden because not significant (2): xml_etree_iterparse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250403-arminc-aarch64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 10.2 ms: 1.22x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.2 ms: 1.43x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.32x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250403-arminc-aarch64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 27.4 ms                                                               | 25.5 ms: 1.08x faster                                                    |
| django_template | 40.7 ms                                                               | 38.4 ms: 1.06x faster                                                    |
| genshi_xml      | 60.6 ms                                                               | 57.8 ms: 1.05x faster                                                    |
| mako            | 12.9 ms                                                               | 13.8 ms: 1.07x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.03x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250403-arminc-aarch64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.61 sec: 2.12x faster                                                   |
| async_tree_memoization     | 777 ms                                                                | 455 ms: 1.71x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 456 ms: 1.62x faster                                                     |
| async_tree_none            | 624 ms                                                                | 387 ms: 1.61x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 884 ms: 1.60x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 883 ms: 1.59x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 370 ms: 1.56x faster                                                     |
| deepcopy                   | 446 us                                                                | 311 us: 1.43x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 35.4 us: 1.40x faster                                                    |
| comprehensions             | 25.4 us                                                               | 19.8 us: 1.28x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 721 ms: 1.26x faster                                                     |
| deepcopy_reduce            | 4.10 us                                                               | 3.25 us: 1.26x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 706 ms: 1.25x faster                                                     |
| generators                 | 43.5 ms                                                               | 35.4 ms: 1.23x faster                                                    |
| go                         | 157 ms                                                                | 129 ms: 1.22x faster                                                     |
| dulwich_log                | 62.0 ms                                                               | 51.3 ms: 1.21x faster                                                    |
| async_generators           | 491 ms                                                                | 409 ms: 1.20x faster                                                     |
| pylint                     | 355 ms                                                                | 301 ms: 1.18x faster                                                     |
| pathlib                    | 24.5 ms                                                               | 21.6 ms: 1.14x faster                                                    |
| raytrace                   | 353 ms                                                                | 313 ms: 1.13x faster                                                     |
| logging_silent             | 127 ns                                                                | 113 ns: 1.13x faster                                                     |
| logging_format             | 8.34 us                                                               | 7.44 us: 1.12x faster                                                    |
| logging_simple             | 7.63 us                                                               | 6.82 us: 1.12x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.32 sec: 1.12x faster                                                   |
| regex_compile              | 137 ms                                                                | 124 ms: 1.11x faster                                                     |
| deltablue                  | 4.12 ms                                                               | 3.75 ms: 1.10x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 141 ms: 1.10x faster                                                     |
| float                      | 92.1 ms                                                               | 84.1 ms: 1.10x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.24 ms: 1.09x faster                                                    |
| html5lib                   | 65.1 ms                                                               | 59.5 ms: 1.09x faster                                                    |
| spectral_norm              | 131 ms                                                                | 120 ms: 1.09x faster                                                     |
| chaos                      | 71.4 ms                                                               | 65.8 ms: 1.08x faster                                                    |
| sympy_integrate            | 21.6 ms                                                               | 20.0 ms: 1.08x faster                                                    |
| xml_etree_generate         | 112 ms                                                                | 104 ms: 1.08x faster                                                     |
| genshi_text                | 27.4 ms                                                               | 25.5 ms: 1.08x faster                                                    |
| richards_super             | 58.5 ms                                                               | 54.3 ms: 1.08x faster                                                    |
| sympy_str                  | 280 ms                                                                | 260 ms: 1.08x faster                                                     |
| pyflate                    | 559 ms                                                                | 520 ms: 1.07x faster                                                     |
| sqlalchemy_declarative     | 157 ms                                                                | 147 ms: 1.07x faster                                                     |
| 2to3                       | 308 ms                                                                | 288 ms: 1.07x faster                                                     |
| scimark_monte_carlo        | 85.1 ms                                                               | 79.7 ms: 1.07x faster                                                    |
| xml_etree_process          | 79.0 ms                                                               | 74.0 ms: 1.07x faster                                                    |
| regex_dna                  | 254 ms                                                                | 239 ms: 1.06x faster                                                     |
| django_template            | 40.7 ms                                                               | 38.4 ms: 1.06x faster                                                    |
| scimark_fft                | 418 ms                                                                | 397 ms: 1.05x faster                                                     |
| genshi_xml                 | 60.6 ms                                                               | 57.8 ms: 1.05x faster                                                    |
| scimark_sor                | 150 ms                                                                | 143 ms: 1.05x faster                                                     |
| richards                   | 50.9 ms                                                               | 48.6 ms: 1.05x faster                                                    |
| sqlalchemy_imperative      | 16.7 ms                                                               | 15.9 ms: 1.05x faster                                                    |
| unpickle_pure_python       | 260 us                                                                | 249 us: 1.05x faster                                                     |
| pycparser                  | 1.26 sec                                                              | 1.20 sec: 1.04x faster                                                   |
| coroutines                 | 29.0 ms                                                               | 27.9 ms: 1.04x faster                                                    |
| docutils                   | 2.98 sec                                                              | 2.90 sec: 1.03x faster                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 84.8 ms: 1.02x faster                                                    |
| pprint_safe_repr           | 916 ms                                                                | 902 ms: 1.02x faster                                                     |
| pprint_pformat             | 1.88 sec                                                              | 1.86 sec: 1.01x faster                                                   |
| hexiom                     | 6.98 ms                                                               | 6.99 ms: 1.00x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 671 ms: 1.02x slower                                                     |
| typing_runtime_protocols   | 181 us                                                                | 184 us: 1.02x slower                                                     |
| meteor_contest             | 112 ms                                                                | 114 ms: 1.02x slower                                                     |
| json                       | 5.54 ms                                                               | 5.79 ms: 1.04x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.48 ms: 1.05x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 30.1 ms: 1.06x slower                                                    |
| xml_etree_parse            | 195 ms                                                                | 207 ms: 1.06x slower                                                     |
| mako                       | 12.9 ms                                                               | 13.8 ms: 1.07x slower                                                    |
| json_loads                 | 30.7 us                                                               | 33.2 us: 1.08x slower                                                    |
| coverage                   | 87.3 ms                                                               | 95.0 ms: 1.09x slower                                                    |
| fannkuch                   | 443 ms                                                                | 484 ms: 1.09x slower                                                     |
| telco                      | 8.51 ms                                                               | 9.44 ms: 1.11x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 14.2 ms: 1.15x slower                                                    |
| nbody                      | 105 ms                                                                | 124 ms: 1.19x slower                                                     |
| python_startup_no_site     | 8.37 ms                                                               | 10.2 ms: 1.22x slower                                                    |
| pidigits                   | 233 ms                                                                | 294 ms: 1.26x slower                                                     |
| python_startup             | 11.4 ms                                                               | 16.2 ms: 1.43x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.52 ms: 1.48x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.53 ms: 1.84x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 2.23 sec: 315.91x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                             |

Benchmark hidden because not significant (7): scimark_lu, sqlite_synth, sympy_expand, xml_etree_iterparse, bench_thread_pool, nqueens, pickle_pure_python
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250403-3.14.0a6+-275056a-CLANG/bm-20250403-arminc-aarch64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.084x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.09x