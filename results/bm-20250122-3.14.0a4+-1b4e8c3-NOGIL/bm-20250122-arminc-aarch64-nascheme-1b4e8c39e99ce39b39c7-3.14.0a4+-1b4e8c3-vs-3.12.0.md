# Results vs. 3.12.0

- fork: nascheme
- ref: 1b4e8c39e99ce39b39c7
- machine: linux-aarch64
- commit hash: 1b4e8c3
- commit date: 2025-01-22
- overall geometric mean: 1.134x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x slower
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250122-arminc-aarch64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 382 ms: 1.24x slower                                                       |
| docutils       | 2.98 sec                                                              | 3.38 sec: 1.13x slower                                                     |
| html5lib       | 65.1 ms                                                               | 79.2 ms: 1.22x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.20x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250122-arminc-aarch64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 917 ms: 1.53x faster                                                       |
| async_tree_memoization_tg  | 740 ms                                                                | 484 ms: 1.53x faster                                                       |
| async_tree_io              | 1.41 sec                                                              | 952 ms: 1.48x faster                                                       |
| async_tree_none_tg         | 577 ms                                                                | 389 ms: 1.48x faster                                                       |
| async_tree_none            | 624 ms                                                                | 430 ms: 1.45x faster                                                       |
| async_tree_memoization     | 777 ms                                                                | 545 ms: 1.42x faster                                                       |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 682 ms: 1.30x faster                                                       |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 721 ms: 1.27x faster                                                       |
| Geometric mean             | (ref)                                                                 | 1.43x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250122-arminc-aarch64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 102 ms: 1.11x slower                                                       |
| nbody          | 105 ms                                                                | 188 ms: 1.80x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.26x slower                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250122-arminc-aarch64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.11 ms: 1.13x faster                                                      |
| regex_v8       | 28.3 ms                                                               | 31.9 ms: 1.12x slower                                                      |
| regex_compile  | 137 ms                                                                | 162 ms: 1.18x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                               |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250122-arminc-aarch64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 260 us                                                                | 315 us: 1.21x slower                                                       |
| json_loads           | 30.7 us                                                               | 37.6 us: 1.23x slower                                                      |
| tomli_loads          | 2.59 sec                                                              | 3.18 sec: 1.23x slower                                                     |
| pickle_pure_python   | 365 us                                                                | 480 us: 1.32x slower                                                       |
| json_dumps           | 12.3 ms                                                               | 16.9 ms: 1.38x slower                                                      |
| Geometric mean       | (ref)                                                                 | 1.27x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250122-arminc-aarch64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 12.3 ms: 1.47x slower                                                      |
| python_startup         | 11.4 ms                                                               | 20.4 ms: 1.80x slower                                                      |
| Geometric mean         | (ref)                                                                 | 1.62x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250122-arminc-aarch64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 77.9 ms: 1.29x slower                                                      |
| genshi_text     | 27.4 ms                                                               | 38.5 ms: 1.40x slower                                                      |
| django_template | 40.7 ms                                                               | 57.2 ms: 1.41x slower                                                      |
| mako            | 12.9 ms                                                               | 23.3 ms: 1.80x slower                                                      |
| Geometric mean  | (ref)                                                                 | 1.46x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250122-arminc-aarch64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 917 ms: 1.53x faster                                                       |
| async_tree_memoization_tg  | 740 ms                                                                | 484 ms: 1.53x faster                                                       |
| async_tree_io              | 1.41 sec                                                              | 952 ms: 1.48x faster                                                       |
| async_tree_none_tg         | 577 ms                                                                | 389 ms: 1.48x faster                                                       |
| async_tree_none            | 624 ms                                                                | 430 ms: 1.45x faster                                                       |
| async_tree_memoization     | 777 ms                                                                | 545 ms: 1.42x faster                                                       |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 682 ms: 1.30x faster                                                       |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 721 ms: 1.27x faster                                                       |
| regex_effbot               | 4.64 ms                                                               | 4.11 ms: 1.13x faster                                                      |
| pathlib                    | 24.5 ms                                                               | 23.2 ms: 1.06x faster                                                      |
| asyncio_websockets         | 658 ms                                                                | 686 ms: 1.04x slower                                                       |
| async_generators           | 491 ms                                                                | 533 ms: 1.09x slower                                                       |
| deepcopy_memo              | 49.6 us                                                               | 54.1 us: 1.09x slower                                                      |
| pylint                     | 355 ms                                                                | 392 ms: 1.10x slower                                                       |
| float                      | 92.1 ms                                                               | 102 ms: 1.11x slower                                                       |
| comprehensions             | 25.4 us                                                               | 28.2 us: 1.11x slower                                                      |
| regex_v8                   | 28.3 ms                                                               | 31.9 ms: 1.12x slower                                                      |
| spectral_norm              | 131 ms                                                                | 148 ms: 1.13x slower                                                       |
| deepcopy_reduce            | 4.10 us                                                               | 4.65 us: 1.13x slower                                                      |
| docutils                   | 2.98 sec                                                              | 3.38 sec: 1.13x slower                                                     |
| mdp                        | 3.41 sec                                                              | 3.87 sec: 1.13x slower                                                     |
| coroutines                 | 29.0 ms                                                               | 33.3 ms: 1.15x slower                                                      |
| go                         | 157 ms                                                                | 181 ms: 1.15x slower                                                       |
| json                       | 5.54 ms                                                               | 6.41 ms: 1.16x slower                                                      |
| pycparser                  | 1.26 sec                                                              | 1.46 sec: 1.16x slower                                                     |
| scimark_fft                | 418 ms                                                                | 490 ms: 1.17x slower                                                       |
| regex_compile              | 137 ms                                                                | 162 ms: 1.18x slower                                                       |
| dulwich_log                | 62.0 ms                                                               | 73.2 ms: 1.18x slower                                                      |
| logging_simple             | 7.63 us                                                               | 9.06 us: 1.19x slower                                                      |
| create_gc_cycles           | 1.92 ms                                                               | 2.29 ms: 1.19x slower                                                      |
| scimark_sor                | 150 ms                                                                | 179 ms: 1.20x slower                                                       |
| pyflate                    | 559 ms                                                                | 674 ms: 1.21x slower                                                       |
| unpickle_pure_python       | 260 us                                                                | 315 us: 1.21x slower                                                       |
| raytrace                   | 353 ms                                                                | 429 ms: 1.21x slower                                                       |
| logging_format             | 8.34 us                                                               | 10.2 us: 1.22x slower                                                      |
| html5lib                   | 65.1 ms                                                               | 79.2 ms: 1.22x slower                                                      |
| json_loads                 | 30.7 us                                                               | 37.6 us: 1.23x slower                                                      |
| tomli_loads                | 2.59 sec                                                              | 3.18 sec: 1.23x slower                                                     |
| gc_traversal               | 4.40 ms                                                               | 5.41 ms: 1.23x slower                                                      |
| logging_silent             | 127 ns                                                                | 157 ns: 1.24x slower                                                       |
| 2to3                       | 308 ms                                                                | 382 ms: 1.24x slower                                                       |
| chaos                      | 71.4 ms                                                               | 89.8 ms: 1.26x slower                                                      |
| pprint_safe_repr           | 916 ms                                                                | 1.15 sec: 1.26x slower                                                     |
| pprint_pformat             | 1.88 sec                                                              | 2.38 sec: 1.26x slower                                                     |
| sqlglot_normalize          | 126 ms                                                                | 159 ms: 1.27x slower                                                       |
| genshi_xml                 | 60.6 ms                                                               | 77.9 ms: 1.29x slower                                                      |
| sympy_sum                  | 154 ms                                                                | 199 ms: 1.29x slower                                                       |
| sqlalchemy_declarative     | 157 ms                                                                | 203 ms: 1.29x slower                                                       |
| sqlglot_optimize           | 61.3 ms                                                               | 79.3 ms: 1.29x slower                                                      |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 8.12 ms: 1.31x slower                                                      |
| sympy_str                  | 280 ms                                                                | 368 ms: 1.32x slower                                                       |
| pickle_pure_python         | 365 us                                                                | 480 us: 1.32x slower                                                       |
| sympy_integrate            | 21.6 ms                                                               | 28.5 ms: 1.32x slower                                                      |
| sqlglot_transpile          | 1.83 ms                                                               | 2.41 ms: 1.32x slower                                                      |
| scimark_lu                 | 146 ms                                                                | 192 ms: 1.32x slower                                                       |
| sympy_expand               | 454 ms                                                                | 605 ms: 1.33x slower                                                       |
| crypto_pyaes               | 86.6 ms                                                               | 116 ms: 1.34x slower                                                       |
| sqlalchemy_imperative      | 16.7 ms                                                               | 22.4 ms: 1.34x slower                                                      |
| nqueens                    | 99.2 ms                                                               | 134 ms: 1.35x slower                                                       |
| scimark_monte_carlo        | 85.1 ms                                                               | 117 ms: 1.37x slower                                                       |
| meteor_contest             | 112 ms                                                                | 154 ms: 1.37x slower                                                       |
| sqlglot_parse              | 1.46 ms                                                               | 2.02 ms: 1.38x slower                                                      |
| json_dumps                 | 12.3 ms                                                               | 16.9 ms: 1.38x slower                                                      |
| telco                      | 8.51 ms                                                               | 11.7 ms: 1.38x slower                                                      |
| hexiom                     | 6.98 ms                                                               | 9.64 ms: 1.38x slower                                                      |
| thrift                     | 937 us                                                                | 1.30 ms: 1.39x slower                                                      |
| genshi_text                | 27.4 ms                                                               | 38.5 ms: 1.40x slower                                                      |
| django_template            | 40.7 ms                                                               | 57.2 ms: 1.41x slower                                                      |
| bench_thread_pool          | 1.31 ms                                                               | 1.89 ms: 1.45x slower                                                      |
| richards                   | 50.9 ms                                                               | 74.4 ms: 1.46x slower                                                      |
| python_startup_no_site     | 8.37 ms                                                               | 12.3 ms: 1.47x slower                                                      |
| coverage                   | 87.3 ms                                                               | 129 ms: 1.48x slower                                                       |
| deltablue                  | 4.12 ms                                                               | 6.10 ms: 1.48x slower                                                      |
| richards_super             | 58.5 ms                                                               | 87.2 ms: 1.49x slower                                                      |
| fannkuch                   | 443 ms                                                                | 680 ms: 1.53x slower                                                       |
| typing_runtime_protocols   | 181 us                                                                | 282 us: 1.56x slower                                                       |
| python_startup             | 11.4 ms                                                               | 20.4 ms: 1.80x slower                                                      |
| nbody                      | 105 ms                                                                | 188 ms: 1.80x slower                                                       |
| mako                       | 12.9 ms                                                               | 23.3 ms: 1.80x slower                                                      |
| bench_mp_pool              | 7.05 ms                                                               | 59.2 ms: 8.40x slower                                                      |
| Geometric mean             | (ref)                                                                 | 1.21x slower                                                               |

Benchmark hidden because not significant (5): deepcopy, sqlite_synth, pidigits, regex_dna, generators
Ignored benchmarks (17) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list, xml_etree_generate, xml_etree_iterparse, xml_etree_parse, xml_etree_process
Ignored benchmarks (7) of results/bm-20250122-3.14.0a4+-1b4e8c3-NOGIL/bm-20250122-arminc-aarch64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.134x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.14x
- 95% likely to have a slowdown of 1.14x
- 99% likely to have a slowdown of 1.12x

# Memory
- memory change: 1.26x