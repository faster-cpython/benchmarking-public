# Results vs. 3.12.0

- fork: diegorusso
- ref: fplt
- machine: linux-aarch64
- commit hash: 707b019
- commit date: 2025-01-22
- overall geometric mean: 1.047x slower
- HPT reliability: 99.79%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250122-arminc-aarch64-diegorusso-fplt-3.14.0a4+-707b019 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 325 ms: 1.06x slower                                         |
| docutils       | 2.98 sec                                                              | 3.25 sec: 1.09x slower                                       |
| html5lib       | 65.1 ms                                                               | 73.4 ms: 1.13x slower                                        |
| Geometric mean | (ref)                                                                 | 1.09x slower                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250122-arminc-aarch64-diegorusso-fplt-3.14.0a4+-707b019 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 397 ms: 1.57x faster                                         |
| async_tree_io              | 1.41 sec                                                              | 905 ms: 1.56x faster                                         |
| async_tree_memoization     | 777 ms                                                                | 500 ms: 1.55x faster                                         |
| async_tree_memoization_tg  | 740 ms                                                                | 478 ms: 1.55x faster                                         |
| async_tree_io_tg           | 1.40 sec                                                              | 908 ms: 1.55x faster                                         |
| async_tree_none_tg         | 577 ms                                                                | 390 ms: 1.48x faster                                         |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 685 ms: 1.33x faster                                         |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 669 ms: 1.32x faster                                         |
| Geometric mean             | (ref)                                                                 | 1.49x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250122-arminc-aarch64-diegorusso-fplt-3.14.0a4+-707b019 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 246 ms: 1.06x slower                                         |
| nbody          | 105 ms                                                                | 132 ms: 1.26x slower                                         |
| Geometric mean | (ref)                                                                 | 1.09x slower                                                 |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250122-arminc-aarch64-diegorusso-fplt-3.14.0a4+-707b019 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.09 ms: 1.13x faster                                        |
| regex_compile  | 137 ms                                                                | 148 ms: 1.08x slower                                         |
| regex_v8       | 28.3 ms                                                               | 32.6 ms: 1.15x slower                                        |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                 |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250122-arminc-aarch64-diegorusso-fplt-3.14.0a4+-707b019 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 179 ms: 1.09x faster                                         |
| xml_etree_iterparse  | 150 ms                                                                | 143 ms: 1.05x faster                                         |
| tomli_loads          | 2.59 sec                                                              | 2.64 sec: 1.02x slower                                       |
| json_loads           | 30.7 us                                                               | 33.0 us: 1.07x slower                                        |
| xml_etree_process    | 79.0 ms                                                               | 86.8 ms: 1.10x slower                                        |
| unpickle_pure_python | 260 us                                                                | 290 us: 1.11x slower                                         |
| pickle_pure_python   | 365 us                                                                | 430 us: 1.18x slower                                         |
| json_dumps           | 12.3 ms                                                               | 14.5 ms: 1.18x slower                                        |
| Geometric mean       | (ref)                                                                 | 1.06x slower                                                 |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250122-arminc-aarch64-diegorusso-fplt-3.14.0a4+-707b019 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.04 ms: 1.08x slower                                        |
| python_startup         | 11.4 ms                                                               | 16.4 ms: 1.44x slower                                        |
| Geometric mean         | (ref)                                                                 | 1.25x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250122-arminc-aarch64-diegorusso-fplt-3.14.0a4+-707b019 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 14.5 ms: 1.12x slower                                        |
| genshi_text     | 27.4 ms                                                               | 33.3 ms: 1.22x slower                                        |
| django_template | 40.7 ms                                                               | 49.5 ms: 1.22x slower                                        |
| genshi_xml      | 60.6 ms                                                               | 83.7 ms: 1.38x slower                                        |
| Geometric mean  | (ref)                                                                 | 1.23x slower                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250122-arminc-aarch64-diegorusso-fplt-3.14.0a4+-707b019 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 397 ms: 1.57x faster                                         |
| async_tree_io              | 1.41 sec                                                              | 905 ms: 1.56x faster                                         |
| async_tree_memoization     | 777 ms                                                                | 500 ms: 1.55x faster                                         |
| async_tree_memoization_tg  | 740 ms                                                                | 478 ms: 1.55x faster                                         |
| async_tree_io_tg           | 1.40 sec                                                              | 908 ms: 1.55x faster                                         |
| async_tree_none_tg         | 577 ms                                                                | 390 ms: 1.48x faster                                         |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 685 ms: 1.33x faster                                         |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 669 ms: 1.32x faster                                         |
| deepcopy_memo              | 49.6 us                                                               | 42.8 us: 1.16x faster                                        |
| deepcopy                   | 446 us                                                                | 388 us: 1.15x faster                                         |
| regex_effbot               | 4.64 ms                                                               | 4.09 ms: 1.13x faster                                        |
| xml_etree_parse            | 195 ms                                                                | 179 ms: 1.09x faster                                         |
| pathlib                    | 24.5 ms                                                               | 22.9 ms: 1.07x faster                                        |
| xml_etree_iterparse        | 150 ms                                                                | 143 ms: 1.05x faster                                         |
| sqlalchemy_declarative     | 157 ms                                                                | 152 ms: 1.04x faster                                         |
| tomli_loads                | 2.59 sec                                                              | 2.64 sec: 1.02x slower                                       |
| asyncio_websockets         | 658 ms                                                                | 673 ms: 1.02x slower                                         |
| deltablue                  | 4.12 ms                                                               | 4.23 ms: 1.03x slower                                        |
| mdp                        | 3.41 sec                                                              | 3.56 sec: 1.04x slower                                       |
| sympy_sum                  | 154 ms                                                                | 163 ms: 1.06x slower                                         |
| 2to3                       | 308 ms                                                                | 325 ms: 1.06x slower                                         |
| pidigits                   | 233 ms                                                                | 246 ms: 1.06x slower                                         |
| bench_thread_pool          | 1.31 ms                                                               | 1.39 ms: 1.06x slower                                        |
| scimark_sor                | 150 ms                                                                | 159 ms: 1.06x slower                                         |
| sqlglot_transpile          | 1.83 ms                                                               | 1.96 ms: 1.07x slower                                        |
| sqlite_synth               | 3.77 us                                                               | 4.05 us: 1.07x slower                                        |
| json_loads                 | 30.7 us                                                               | 33.0 us: 1.07x slower                                        |
| regex_compile              | 137 ms                                                                | 148 ms: 1.08x slower                                         |
| python_startup_no_site     | 8.37 ms                                                               | 9.04 ms: 1.08x slower                                        |
| logging_simple             | 7.63 us                                                               | 8.25 us: 1.08x slower                                        |
| sympy_str                  | 280 ms                                                                | 303 ms: 1.08x slower                                         |
| pyflate                    | 559 ms                                                                | 607 ms: 1.09x slower                                         |
| logging_format             | 8.34 us                                                               | 9.07 us: 1.09x slower                                        |
| docutils                   | 2.98 sec                                                              | 3.25 sec: 1.09x slower                                       |
| json                       | 5.54 ms                                                               | 6.03 ms: 1.09x slower                                        |
| scimark_fft                | 418 ms                                                                | 457 ms: 1.09x slower                                         |
| thrift                     | 937 us                                                                | 1.03 ms: 1.09x slower                                        |
| xml_etree_process          | 79.0 ms                                                               | 86.8 ms: 1.10x slower                                        |
| crypto_pyaes               | 86.6 ms                                                               | 95.5 ms: 1.10x slower                                        |
| spectral_norm              | 131 ms                                                                | 144 ms: 1.10x slower                                         |
| meteor_contest             | 112 ms                                                                | 124 ms: 1.11x slower                                         |
| scimark_lu                 | 146 ms                                                                | 162 ms: 1.11x slower                                         |
| scimark_monte_carlo        | 85.1 ms                                                               | 94.8 ms: 1.11x slower                                        |
| unpickle_pure_python       | 260 us                                                                | 290 us: 1.11x slower                                         |
| sqlglot_parse              | 1.46 ms                                                               | 1.63 ms: 1.12x slower                                        |
| sympy_integrate            | 21.6 ms                                                               | 24.1 ms: 1.12x slower                                        |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.95 ms: 1.12x slower                                        |
| mako                       | 12.9 ms                                                               | 14.5 ms: 1.12x slower                                        |
| html5lib                   | 65.1 ms                                                               | 73.4 ms: 1.13x slower                                        |
| sqlglot_normalize          | 126 ms                                                                | 143 ms: 1.14x slower                                         |
| sqlglot_optimize           | 61.3 ms                                                               | 70.0 ms: 1.14x slower                                        |
| sympy_expand               | 454 ms                                                                | 518 ms: 1.14x slower                                         |
| dulwich_log                | 62.0 ms                                                               | 71.2 ms: 1.15x slower                                        |
| regex_v8                   | 28.3 ms                                                               | 32.6 ms: 1.15x slower                                        |
| pickle_pure_python         | 365 us                                                                | 430 us: 1.18x slower                                         |
| json_dumps                 | 12.3 ms                                                               | 14.5 ms: 1.18x slower                                        |
| go                         | 157 ms                                                                | 186 ms: 1.18x slower                                         |
| logging_silent             | 127 ns                                                                | 151 ns: 1.19x slower                                         |
| telco                      | 8.51 ms                                                               | 10.2 ms: 1.20x slower                                        |
| coverage                   | 87.3 ms                                                               | 105 ms: 1.20x slower                                         |
| fannkuch                   | 443 ms                                                                | 532 ms: 1.20x slower                                         |
| richards_super             | 58.5 ms                                                               | 70.2 ms: 1.20x slower                                        |
| genshi_text                | 27.4 ms                                                               | 33.3 ms: 1.22x slower                                        |
| django_template            | 40.7 ms                                                               | 49.5 ms: 1.22x slower                                        |
| chaos                      | 71.4 ms                                                               | 88.2 ms: 1.24x slower                                        |
| pycparser                  | 1.26 sec                                                              | 1.56 sec: 1.24x slower                                       |
| typing_runtime_protocols   | 181 us                                                                | 225 us: 1.24x slower                                         |
| nbody                      | 105 ms                                                                | 132 ms: 1.26x slower                                         |
| nqueens                    | 99.2 ms                                                               | 129 ms: 1.30x slower                                         |
| generators                 | 43.5 ms                                                               | 56.7 ms: 1.30x slower                                        |
| genshi_xml                 | 60.6 ms                                                               | 83.7 ms: 1.38x slower                                        |
| hexiom                     | 6.98 ms                                                               | 9.92 ms: 1.42x slower                                        |
| pprint_pformat             | 1.88 sec                                                              | 2.69 sec: 1.43x slower                                       |
| python_startup             | 11.4 ms                                                               | 16.4 ms: 1.44x slower                                        |
| pprint_safe_repr           | 916 ms                                                                | 1.35 sec: 1.47x slower                                       |
| richards                   | 50.9 ms                                                               | 76.4 ms: 1.50x slower                                        |
| gc_traversal               | 4.40 ms                                                               | 6.95 ms: 1.58x slower                                        |
| create_gc_cycles           | 1.92 ms                                                               | 3.69 ms: 1.92x slower                                        |
| bench_mp_pool              | 7.05 ms                                                               | 1.36 sec: 192.59x slower                                     |
| Geometric mean             | (ref)                                                                 | 1.14x slower                                                 |

Benchmark hidden because not significant (10): pylint, float, deepcopy_reduce, raytrace, comprehensions, async_generators, coroutines, xml_etree_generate, regex_dna, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20250122-3.14.0a4+-707b019-JIT/bm-20250122-arminc-aarch64-diegorusso-fplt-3.14.0a4+-707b019.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.047x slower

# HPT report

- Reliability score: 99.79% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.05x