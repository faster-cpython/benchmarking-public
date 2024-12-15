# Results vs. 3.12.0

- fork: python
- ref: 0ac40acec045c4ce780c
- machine: linux-aarch64
- commit hash: 0ac40ac
- commit date: 2024-12-14
- overall geometric mean: 1.294x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x slower
- Memory change: 1.24x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 472 ms: 1.53x slower                                                     |
| docutils       | 2.98 sec                                                              | 3.83 sec: 1.28x slower                                                   |
| html5lib       | 65.1 ms                                                               | 117 ms: 1.80x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.52x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|---------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg          | 1.40 sec                                                              | 1.29 sec: 1.09x faster                                                   |
| async_tree_io             | 1.41 sec                                                              | 1.30 sec: 1.09x faster                                                   |
| async_tree_memoization_tg | 740 ms                                                                | 687 ms: 1.08x faster                                                     |
| async_tree_none           | 624 ms                                                                | 587 ms: 1.06x faster                                                     |
| async_tree_memoization    | 777 ms                                                                | 735 ms: 1.06x faster                                                     |
| Geometric mean            | (ref)                                                                 | 1.05x faster                                                             |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 105 ms                                                                | 193 ms: 1.84x slower                                                     |
| float          | 92.1 ms                                                               | 194 ms: 2.11x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.58x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.31 ms: 1.08x faster                                                    |
| regex_dna      | 254 ms                                                                | 273 ms: 1.07x slower                                                     |
| regex_v8       | 28.3 ms                                                               | 33.9 ms: 1.20x slower                                                    |
| regex_compile  | 137 ms                                                                | 201 ms: 1.47x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.15x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_iterparse  | 150 ms                                                                | 138 ms: 1.09x faster                                                     |
| xml_etree_parse      | 195 ms                                                                | 183 ms: 1.06x faster                                                     |
| json_loads           | 30.7 us                                                               | 36.8 us: 1.20x slower                                                    |
| xml_etree_generate   | 112 ms                                                                | 144 ms: 1.29x slower                                                     |
| tomli_loads          | 2.59 sec                                                              | 3.59 sec: 1.38x slower                                                   |
| xml_etree_process    | 79.0 ms                                                               | 113 ms: 1.44x slower                                                     |
| json_dumps           | 12.3 ms                                                               | 18.8 ms: 1.53x slower                                                    |
| unpickle_pure_python | 260 us                                                                | 460 us: 1.77x slower                                                     |
| pickle_pure_python   | 365 us                                                                | 702 us: 1.92x slower                                                     |
| Geometric mean       | (ref)                                                                 | 1.34x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 12.7 ms: 1.52x slower                                                    |
| python_startup         | 11.4 ms                                                               | 21.5 ms: 1.89x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.69x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 85.6 ms: 1.41x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 42.4 ms: 1.54x slower                                                    |
| django_template | 40.7 ms                                                               | 66.9 ms: 1.64x slower                                                    |
| mako            | 12.9 ms                                                               | 25.7 ms: 1.99x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.64x slower                                                             |

All benchmarks:
===============

| Benchmark                 | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|---------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg          | 1.40 sec                                                              | 1.29 sec: 1.09x faster                                                   |
| xml_etree_iterparse       | 150 ms                                                                | 138 ms: 1.09x faster                                                     |
| async_tree_io             | 1.41 sec                                                              | 1.30 sec: 1.09x faster                                                   |
| async_tree_memoization_tg | 740 ms                                                                | 687 ms: 1.08x faster                                                     |
| regex_effbot              | 4.64 ms                                                               | 4.31 ms: 1.08x faster                                                    |
| xml_etree_parse           | 195 ms                                                                | 183 ms: 1.06x faster                                                     |
| async_tree_none           | 624 ms                                                                | 587 ms: 1.06x faster                                                     |
| async_tree_memoization    | 777 ms                                                                | 735 ms: 1.06x faster                                                     |
| pathlib                   | 24.5 ms                                                               | 24.8 ms: 1.01x slower                                                    |
| sqlite_synth              | 3.77 us                                                               | 3.97 us: 1.05x slower                                                    |
| asyncio_websockets        | 658 ms                                                                | 696 ms: 1.06x slower                                                     |
| regex_dna                 | 254 ms                                                                | 273 ms: 1.07x slower                                                     |
| gc_traversal              | 4.40 ms                                                               | 5.03 ms: 1.14x slower                                                    |
| coroutines                | 29.0 ms                                                               | 33.8 ms: 1.16x slower                                                    |
| json                      | 5.54 ms                                                               | 6.57 ms: 1.19x slower                                                    |
| deepcopy_memo             | 49.6 us                                                               | 59.2 us: 1.19x slower                                                    |
| regex_v8                  | 28.3 ms                                                               | 33.9 ms: 1.20x slower                                                    |
| mdp                       | 3.41 sec                                                              | 4.09 sec: 1.20x slower                                                   |
| json_loads                | 30.7 us                                                               | 36.8 us: 1.20x slower                                                    |
| deepcopy_reduce           | 4.10 us                                                               | 4.94 us: 1.21x slower                                                    |
| scimark_fft               | 418 ms                                                                | 507 ms: 1.21x slower                                                     |
| spectral_norm             | 131 ms                                                                | 160 ms: 1.22x slower                                                     |
| docutils                  | 2.98 sec                                                              | 3.83 sec: 1.28x slower                                                   |
| xml_etree_generate        | 112 ms                                                                | 144 ms: 1.29x slower                                                     |
| async_generators          | 491 ms                                                                | 635 ms: 1.29x slower                                                     |
| generators                | 43.5 ms                                                               | 56.6 ms: 1.30x slower                                                    |
| pylint                    | 355 ms                                                                | 463 ms: 1.31x slower                                                     |
| scimark_sparse_mat_mult   | 6.19 ms                                                               | 8.17 ms: 1.32x slower                                                    |
| nqueens                   | 99.2 ms                                                               | 137 ms: 1.38x slower                                                     |
| tomli_loads               | 2.59 sec                                                              | 3.59 sec: 1.38x slower                                                   |
| meteor_contest            | 112 ms                                                                | 158 ms: 1.41x slower                                                     |
| genshi_xml                | 60.6 ms                                                               | 85.6 ms: 1.41x slower                                                    |
| telco                     | 8.51 ms                                                               | 12.1 ms: 1.42x slower                                                    |
| crypto_pyaes              | 86.6 ms                                                               | 123 ms: 1.42x slower                                                     |
| xml_etree_process         | 79.0 ms                                                               | 113 ms: 1.44x slower                                                     |
| sqlglot_optimize          | 61.3 ms                                                               | 89.1 ms: 1.45x slower                                                    |
| regex_compile             | 137 ms                                                                | 201 ms: 1.47x slower                                                     |
| dulwich_log               | 62.0 ms                                                               | 91.1 ms: 1.47x slower                                                    |
| sqlglot_normalize         | 126 ms                                                                | 189 ms: 1.50x slower                                                     |
| pprint_safe_repr          | 916 ms                                                                | 1.38 sec: 1.51x slower                                                   |
| pprint_pformat            | 1.88 sec                                                              | 2.84 sec: 1.51x slower                                                   |
| python_startup_no_site    | 8.37 ms                                                               | 12.7 ms: 1.52x slower                                                    |
| json_dumps                | 12.3 ms                                                               | 18.8 ms: 1.53x slower                                                    |
| comprehensions            | 25.4 us                                                               | 38.9 us: 1.53x slower                                                    |
| 2to3                      | 308 ms                                                                | 472 ms: 1.53x slower                                                     |
| create_gc_cycles          | 1.92 ms                                                               | 2.95 ms: 1.54x slower                                                    |
| sympy_integrate           | 21.6 ms                                                               | 33.2 ms: 1.54x slower                                                    |
| genshi_text               | 27.4 ms                                                               | 42.4 ms: 1.54x slower                                                    |
| bench_thread_pool         | 1.31 ms                                                               | 2.03 ms: 1.55x slower                                                    |
| pycparser                 | 1.26 sec                                                              | 1.95 sec: 1.55x slower                                                   |
| logging_simple            | 7.63 us                                                               | 12.0 us: 1.57x slower                                                    |
| fannkuch                  | 443 ms                                                                | 698 ms: 1.57x slower                                                     |
| sqlalchemy_declarative    | 157 ms                                                                | 248 ms: 1.58x slower                                                     |
| logging_format            | 8.34 us                                                               | 13.3 us: 1.60x slower                                                    |
| django_template           | 40.7 ms                                                               | 66.9 ms: 1.64x slower                                                    |
| pyflate                   | 559 ms                                                                | 925 ms: 1.65x slower                                                     |
| sympy_str                 | 280 ms                                                                | 465 ms: 1.66x slower                                                     |
| typing_runtime_protocols  | 181 us                                                                | 305 us: 1.69x slower                                                     |
| coverage                  | 87.3 ms                                                               | 147 ms: 1.69x slower                                                     |
| sqlalchemy_imperative     | 16.7 ms                                                               | 28.4 ms: 1.71x slower                                                    |
| thrift                    | 937 us                                                                | 1.61 ms: 1.71x slower                                                    |
| unpickle_pure_python      | 260 us                                                                | 460 us: 1.77x slower                                                     |
| html5lib                  | 65.1 ms                                                               | 117 ms: 1.80x slower                                                     |
| scimark_lu                | 146 ms                                                                | 268 ms: 1.84x slower                                                     |
| nbody                     | 105 ms                                                                | 193 ms: 1.84x slower                                                     |
| mypy2                     | 873 ms                                                                | 1.65 sec: 1.89x slower                                                   |
| python_startup            | 11.4 ms                                                               | 21.5 ms: 1.89x slower                                                    |
| sympy_sum                 | 154 ms                                                                | 293 ms: 1.90x slower                                                     |
| pickle_pure_python        | 365 us                                                                | 702 us: 1.92x slower                                                     |
| sympy_expand              | 454 ms                                                                | 873 ms: 1.93x slower                                                     |
| scimark_monte_carlo       | 85.1 ms                                                               | 166 ms: 1.95x slower                                                     |
| hexiom                    | 6.98 ms                                                               | 13.7 ms: 1.96x slower                                                    |
| chaos                     | 71.4 ms                                                               | 142 ms: 1.98x slower                                                     |
| mako                      | 12.9 ms                                                               | 25.7 ms: 1.99x slower                                                    |
| richards_super            | 58.5 ms                                                               | 121 ms: 2.06x slower                                                     |
| scimark_sor               | 150 ms                                                                | 313 ms: 2.09x slower                                                     |
| raytrace                  | 353 ms                                                                | 739 ms: 2.09x slower                                                     |
| float                     | 92.1 ms                                                               | 194 ms: 2.11x slower                                                     |
| logging_silent            | 127 ns                                                                | 270 ns: 2.13x slower                                                     |
| sqlglot_transpile         | 1.83 ms                                                               | 3.97 ms: 2.17x slower                                                    |
| richards                  | 50.9 ms                                                               | 115 ms: 2.26x slower                                                     |
| sqlglot_parse             | 1.46 ms                                                               | 3.34 ms: 2.28x slower                                                    |
| go                        | 157 ms                                                                | 378 ms: 2.40x slower                                                     |
| deltablue                 | 4.12 ms                                                               | 12.2 ms: 2.97x slower                                                    |
| bench_mp_pool             | 7.05 ms                                                               | 62.8 ms: 8.91x slower                                                    |
| Geometric mean            | (ref)                                                                 | 1.48x slower                                                             |

Benchmark hidden because not significant (5): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, deepcopy, async_tree_none_tg, pidigits
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20241214-3.14.0a2+-0ac40ac-NOGIL/bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.294x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.33x
- 95% likely to have a slowdown of 1.30x
- 99% likely to have a slowdown of 1.27x

# Memory
- memory change: 1.24x