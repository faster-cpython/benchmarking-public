# Results vs. 3.12.0

- fork: python
- ref: 79b7cab50a3292a1c014
- machine: linux-aarch64
- commit hash: 79b7cab
- commit date: 2024-12-07
- overall geometric mean: 1.293x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x slower
- Memory change: 1.24x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 468 ms: 1.52x slower                                                     |
| docutils       | 2.98 sec                                                              | 3.77 sec: 1.26x slower                                                   |
| html5lib       | 65.1 ms                                                               | 118 ms: 1.81x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.51x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|---------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization    | 777 ms                                                                | 708 ms: 1.10x faster                                                     |
| async_tree_io_tg          | 1.40 sec                                                              | 1.30 sec: 1.08x faster                                                   |
| async_tree_io             | 1.41 sec                                                              | 1.31 sec: 1.07x faster                                                   |
| async_tree_memoization_tg | 740 ms                                                                | 693 ms: 1.07x faster                                                     |
| async_tree_none           | 624 ms                                                                | 592 ms: 1.05x faster                                                     |
| Geometric mean            | (ref)                                                                 | 1.05x faster                                                             |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 105 ms                                                                | 183 ms: 1.75x slower                                                     |
| float          | 92.1 ms                                                               | 198 ms: 2.15x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.55x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.99 ms: 1.16x faster                                                    |
| regex_v8       | 28.3 ms                                                               | 34.0 ms: 1.20x slower                                                    |
| regex_compile  | 137 ms                                                                | 203 ms: 1.48x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.12x slower                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 181 ms: 1.08x faster                                                     |
| xml_etree_iterparse  | 150 ms                                                                | 141 ms: 1.06x faster                                                     |
| json_loads           | 30.7 us                                                               | 37.1 us: 1.21x slower                                                    |
| xml_etree_generate   | 112 ms                                                                | 144 ms: 1.29x slower                                                     |
| tomli_loads          | 2.59 sec                                                              | 3.69 sec: 1.42x slower                                                   |
| xml_etree_process    | 79.0 ms                                                               | 116 ms: 1.47x slower                                                     |
| json_dumps           | 12.3 ms                                                               | 19.3 ms: 1.57x slower                                                    |
| unpickle_pure_python | 260 us                                                                | 459 us: 1.76x slower                                                     |
| pickle_pure_python   | 365 us                                                                | 668 us: 1.83x slower                                                     |
| Geometric mean       | (ref)                                                                 | 1.34x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 12.8 ms: 1.52x slower                                                    |
| python_startup         | 11.4 ms                                                               | 21.6 ms: 1.90x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.70x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 84.5 ms: 1.40x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 43.3 ms: 1.58x slower                                                    |
| django_template | 40.7 ms                                                               | 68.5 ms: 1.68x slower                                                    |
| mako            | 12.9 ms                                                               | 26.3 ms: 2.04x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.66x slower                                                             |

All benchmarks:
===============

| Benchmark                 | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|---------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot              | 4.64 ms                                                               | 3.99 ms: 1.16x faster                                                    |
| async_tree_memoization    | 777 ms                                                                | 708 ms: 1.10x faster                                                     |
| async_tree_io_tg          | 1.40 sec                                                              | 1.30 sec: 1.08x faster                                                   |
| xml_etree_parse           | 195 ms                                                                | 181 ms: 1.08x faster                                                     |
| async_tree_io             | 1.41 sec                                                              | 1.31 sec: 1.07x faster                                                   |
| async_tree_memoization_tg | 740 ms                                                                | 693 ms: 1.07x faster                                                     |
| xml_etree_iterparse       | 150 ms                                                                | 141 ms: 1.06x faster                                                     |
| async_tree_none           | 624 ms                                                                | 592 ms: 1.05x faster                                                     |
| asyncio_websockets        | 658 ms                                                                | 687 ms: 1.05x slower                                                     |
| sqlite_synth              | 3.77 us                                                               | 4.08 us: 1.08x slower                                                    |
| pathlib                   | 24.5 ms                                                               | 26.6 ms: 1.08x slower                                                    |
| gc_traversal              | 4.40 ms                                                               | 5.06 ms: 1.15x slower                                                    |
| coroutines                | 29.0 ms                                                               | 33.4 ms: 1.15x slower                                                    |
| json                      | 5.54 ms                                                               | 6.55 ms: 1.18x slower                                                    |
| deepcopy_memo             | 49.6 us                                                               | 58.8 us: 1.19x slower                                                    |
| regex_v8                  | 28.3 ms                                                               | 34.0 ms: 1.20x slower                                                    |
| mdp                       | 3.41 sec                                                              | 4.10 sec: 1.20x slower                                                   |
| deepcopy_reduce           | 4.10 us                                                               | 4.94 us: 1.21x slower                                                    |
| json_loads                | 30.7 us                                                               | 37.1 us: 1.21x slower                                                    |
| docutils                  | 2.98 sec                                                              | 3.77 sec: 1.26x slower                                                   |
| scimark_fft               | 418 ms                                                                | 536 ms: 1.28x slower                                                     |
| xml_etree_generate        | 112 ms                                                                | 144 ms: 1.29x slower                                                     |
| spectral_norm             | 131 ms                                                                | 168 ms: 1.29x slower                                                     |
| generators                | 43.5 ms                                                               | 56.4 ms: 1.30x slower                                                    |
| async_generators          | 491 ms                                                                | 637 ms: 1.30x slower                                                     |
| scimark_sparse_mat_mult   | 6.19 ms                                                               | 8.23 ms: 1.33x slower                                                    |
| pylint                    | 355 ms                                                                | 480 ms: 1.35x slower                                                     |
| crypto_pyaes              | 86.6 ms                                                               | 118 ms: 1.37x slower                                                     |
| telco                     | 8.51 ms                                                               | 11.8 ms: 1.39x slower                                                    |
| genshi_xml                | 60.6 ms                                                               | 84.5 ms: 1.40x slower                                                    |
| nqueens                   | 99.2 ms                                                               | 138 ms: 1.40x slower                                                     |
| meteor_contest            | 112 ms                                                                | 158 ms: 1.41x slower                                                     |
| tomli_loads               | 2.59 sec                                                              | 3.69 sec: 1.42x slower                                                   |
| sqlglot_normalize         | 126 ms                                                                | 179 ms: 1.42x slower                                                     |
| dulwich_log               | 62.0 ms                                                               | 88.9 ms: 1.43x slower                                                    |
| xml_etree_process         | 79.0 ms                                                               | 116 ms: 1.47x slower                                                     |
| regex_compile             | 137 ms                                                                | 203 ms: 1.48x slower                                                     |
| pprint_safe_repr          | 916 ms                                                                | 1.36 sec: 1.48x slower                                                   |
| pprint_pformat            | 1.88 sec                                                              | 2.80 sec: 1.49x slower                                                   |
| sqlglot_optimize          | 61.3 ms                                                               | 92.2 ms: 1.50x slower                                                    |
| sympy_integrate           | 21.6 ms                                                               | 32.6 ms: 1.51x slower                                                    |
| 2to3                      | 308 ms                                                                | 468 ms: 1.52x slower                                                     |
| pycparser                 | 1.26 sec                                                              | 1.91 sec: 1.52x slower                                                   |
| comprehensions            | 25.4 us                                                               | 38.7 us: 1.52x slower                                                    |
| python_startup_no_site    | 8.37 ms                                                               | 12.8 ms: 1.52x slower                                                    |
| bench_thread_pool         | 1.31 ms                                                               | 2.00 ms: 1.53x slower                                                    |
| create_gc_cycles          | 1.92 ms                                                               | 2.94 ms: 1.53x slower                                                    |
| fannkuch                  | 443 ms                                                                | 690 ms: 1.56x slower                                                     |
| coverage                  | 87.3 ms                                                               | 136 ms: 1.56x slower                                                     |
| typing_runtime_protocols  | 181 us                                                                | 284 us: 1.57x slower                                                     |
| json_dumps                | 12.3 ms                                                               | 19.3 ms: 1.57x slower                                                    |
| genshi_text               | 27.4 ms                                                               | 43.3 ms: 1.58x slower                                                    |
| sympy_str                 | 280 ms                                                                | 458 ms: 1.64x slower                                                     |
| pyflate                   | 559 ms                                                                | 927 ms: 1.66x slower                                                     |
| logging_format            | 8.34 us                                                               | 14.0 us: 1.68x slower                                                    |
| django_template           | 40.7 ms                                                               | 68.5 ms: 1.68x slower                                                    |
| thrift                    | 937 us                                                                | 1.60 ms: 1.70x slower                                                    |
| sqlalchemy_declarative    | 157 ms                                                                | 271 ms: 1.72x slower                                                     |
| logging_simple            | 7.63 us                                                               | 13.1 us: 1.72x slower                                                    |
| sqlalchemy_imperative     | 16.7 ms                                                               | 29.1 ms: 1.75x slower                                                    |
| nbody                     | 105 ms                                                                | 183 ms: 1.75x slower                                                     |
| unpickle_pure_python      | 260 us                                                                | 459 us: 1.76x slower                                                     |
| html5lib                  | 65.1 ms                                                               | 118 ms: 1.81x slower                                                     |
| pickle_pure_python        | 365 us                                                                | 668 us: 1.83x slower                                                     |
| hexiom                    | 6.98 ms                                                               | 12.8 ms: 1.84x slower                                                    |
| sympy_sum                 | 154 ms                                                                | 287 ms: 1.86x slower                                                     |
| scimark_lu                | 146 ms                                                                | 271 ms: 1.86x slower                                                     |
| sympy_expand              | 454 ms                                                                | 859 ms: 1.90x slower                                                     |
| python_startup            | 11.4 ms                                                               | 21.6 ms: 1.90x slower                                                    |
| chaos                     | 71.4 ms                                                               | 136 ms: 1.91x slower                                                     |
| scimark_monte_carlo       | 85.1 ms                                                               | 164 ms: 1.93x slower                                                     |
| mako                      | 12.9 ms                                                               | 26.3 ms: 2.04x slower                                                    |
| richards_super            | 58.5 ms                                                               | 119 ms: 2.04x slower                                                     |
| richards                  | 50.9 ms                                                               | 106 ms: 2.08x slower                                                     |
| raytrace                  | 353 ms                                                                | 736 ms: 2.08x slower                                                     |
| logging_silent            | 127 ns                                                                | 265 ns: 2.09x slower                                                     |
| scimark_sor               | 150 ms                                                                | 314 ms: 2.10x slower                                                     |
| float                     | 92.1 ms                                                               | 198 ms: 2.15x slower                                                     |
| sqlglot_transpile         | 1.83 ms                                                               | 3.96 ms: 2.17x slower                                                    |
| sqlglot_parse             | 1.46 ms                                                               | 3.38 ms: 2.31x slower                                                    |
| go                        | 157 ms                                                                | 373 ms: 2.37x slower                                                     |
| deltablue                 | 4.12 ms                                                               | 11.8 ms: 2.87x slower                                                    |
| bench_mp_pool             | 7.05 ms                                                               | 66.8 ms: 9.47x slower                                                    |
| Geometric mean            | (ref)                                                                 | 1.48x slower                                                             |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, pidigits, async_tree_none_tg, deepcopy, regex_dna
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20241207-3.14.0a2+-79b7cab-NOGIL/bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.293x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.33x
- 95% likely to have a slowdown of 1.30x
- 99% likely to have a slowdown of 1.26x

# Memory
- memory change: 1.24x