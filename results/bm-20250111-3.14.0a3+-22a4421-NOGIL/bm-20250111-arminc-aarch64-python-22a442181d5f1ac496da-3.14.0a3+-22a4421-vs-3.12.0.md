# Results vs. 3.12.0

- fork: python
- ref: 22a442181d5f1ac496da
- machine: linux-aarch64
- commit hash: 22a4421
- commit date: 2025-01-11
- overall geometric mean: 1.242x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x slower
- Memory change: 1.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 458 ms: 1.49x slower                                                     |
| docutils       | 2.98 sec                                                              | 3.68 sec: 1.23x slower                                                   |
| html5lib       | 65.1 ms                                                               | 110 ms: 1.69x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.46x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 1.17 sec: 1.20x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 1.20 sec: 1.18x faster                                                   |
| async_tree_memoization_tg  | 740 ms                                                                | 631 ms: 1.17x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 666 ms: 1.17x faster                                                     |
| async_tree_none            | 624 ms                                                                | 543 ms: 1.15x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 518 ms: 1.11x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 808 ms: 1.09x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 840 ms: 1.09x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.14x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 150 ms: 1.62x slower                                                     |
| nbody          | 105 ms                                                                | 185 ms: 1.76x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.43x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.07 ms: 1.14x faster                                                    |
| regex_dna      | 254 ms                                                                | 263 ms: 1.04x slower                                                     |
| regex_v8       | 28.3 ms                                                               | 34.9 ms: 1.23x slower                                                    |
| regex_compile  | 137 ms                                                                | 186 ms: 1.36x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.11x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_iterparse  | 150 ms                                                                | 136 ms: 1.11x faster                                                     |
| xml_etree_parse      | 195 ms                                                                | 181 ms: 1.08x faster                                                     |
| pickle_dict          | 37.3 us                                                               | 40.2 us: 1.08x slower                                                    |
| unpickle             | 18.5 us                                                               | 20.9 us: 1.13x slower                                                    |
| pickle_list          | 5.25 us                                                               | 6.02 us: 1.15x slower                                                    |
| json_loads           | 30.7 us                                                               | 36.4 us: 1.19x slower                                                    |
| pickle               | 13.4 us                                                               | 16.0 us: 1.19x slower                                                    |
| unpickle_list        | 6.17 us                                                               | 7.52 us: 1.22x slower                                                    |
| xml_etree_generate   | 112 ms                                                                | 143 ms: 1.27x slower                                                     |
| tomli_loads          | 2.59 sec                                                              | 3.34 sec: 1.29x slower                                                   |
| xml_etree_process    | 79.0 ms                                                               | 111 ms: 1.40x slower                                                     |
| json_dumps           | 12.3 ms                                                               | 18.4 ms: 1.50x slower                                                    |
| unpickle_pure_python | 260 us                                                                | 440 us: 1.69x slower                                                     |
| pickle_pure_python   | 365 us                                                                | 661 us: 1.81x slower                                                     |
| Geometric mean       | (ref)                                                                 | 1.25x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 12.3 ms: 1.47x slower                                                    |
| python_startup         | 11.4 ms                                                               | 20.4 ms: 1.80x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.62x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 81.1 ms: 1.34x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 39.7 ms: 1.45x slower                                                    |
| django_template | 40.7 ms                                                               | 64.2 ms: 1.58x slower                                                    |
| mako            | 12.9 ms                                                               | 25.2 ms: 1.95x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.56x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 1.17 sec: 1.20x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 1.20 sec: 1.18x faster                                                   |
| async_tree_memoization_tg  | 740 ms                                                                | 631 ms: 1.17x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 666 ms: 1.17x faster                                                     |
| async_tree_none            | 624 ms                                                                | 543 ms: 1.15x faster                                                     |
| regex_effbot               | 4.64 ms                                                               | 4.07 ms: 1.14x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 518 ms: 1.11x faster                                                     |
| xml_etree_iterparse        | 150 ms                                                                | 136 ms: 1.11x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 808 ms: 1.09x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 840 ms: 1.09x faster                                                     |
| xml_etree_parse            | 195 ms                                                                | 181 ms: 1.08x faster                                                     |
| pathlib                    | 24.5 ms                                                               | 23.8 ms: 1.03x faster                                                    |
| regex_dna                  | 254 ms                                                                | 263 ms: 1.04x slower                                                     |
| asyncio_websockets         | 658 ms                                                                | 683 ms: 1.04x slower                                                     |
| pickle_dict                | 37.3 us                                                               | 40.2 us: 1.08x slower                                                    |
| coroutines                 | 29.0 ms                                                               | 32.6 ms: 1.12x slower                                                    |
| unpickle                   | 18.5 us                                                               | 20.9 us: 1.13x slower                                                    |
| asyncio_tcp                | 566 ms                                                                | 647 ms: 1.14x slower                                                     |
| gc_traversal               | 4.40 ms                                                               | 5.03 ms: 1.14x slower                                                    |
| pickle_list                | 5.25 us                                                               | 6.02 us: 1.15x slower                                                    |
| spectral_norm              | 131 ms                                                                | 150 ms: 1.15x slower                                                     |
| json                       | 5.54 ms                                                               | 6.38 ms: 1.15x slower                                                    |
| mdp                        | 3.41 sec                                                              | 4.00 sec: 1.17x slower                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 4.81 us: 1.17x slower                                                    |
| scimark_fft                | 418 ms                                                                | 493 ms: 1.18x slower                                                     |
| json_loads                 | 30.7 us                                                               | 36.4 us: 1.19x slower                                                    |
| deepcopy_memo              | 49.6 us                                                               | 59.2 us: 1.19x slower                                                    |
| pickle                     | 13.4 us                                                               | 16.0 us: 1.19x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.61 sec: 1.19x slower                                                   |
| unpickle_list              | 6.17 us                                                               | 7.52 us: 1.22x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 34.9 ms: 1.23x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.68 sec: 1.23x slower                                                   |
| async_generators           | 491 ms                                                                | 606 ms: 1.23x slower                                                     |
| pylint                     | 355 ms                                                                | 443 ms: 1.25x slower                                                     |
| xml_etree_generate         | 112 ms                                                                | 143 ms: 1.27x slower                                                     |
| generators                 | 43.5 ms                                                               | 55.4 ms: 1.27x slower                                                    |
| tomli_loads                | 2.59 sec                                                              | 3.34 sec: 1.29x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 8.22 ms: 1.33x slower                                                    |
| dulwich_log                | 62.0 ms                                                               | 83.0 ms: 1.34x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 81.1 ms: 1.34x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.68 sec: 1.34x slower                                                   |
| nqueens                    | 99.2 ms                                                               | 134 ms: 1.36x slower                                                     |
| regex_compile              | 137 ms                                                                | 186 ms: 1.36x slower                                                     |
| sympy_sum                  | 154 ms                                                                | 210 ms: 1.36x slower                                                     |
| crypto_pyaes               | 86.6 ms                                                               | 119 ms: 1.38x slower                                                     |
| sympy_integrate            | 21.6 ms                                                               | 30.1 ms: 1.39x slower                                                    |
| xml_etree_process          | 79.0 ms                                                               | 111 ms: 1.40x slower                                                     |
| meteor_contest             | 112 ms                                                                | 158 ms: 1.41x slower                                                     |
| logging_simple             | 7.63 us                                                               | 10.8 us: 1.42x slower                                                    |
| logging_format             | 8.34 us                                                               | 11.8 us: 1.42x slower                                                    |
| thrift                     | 937 us                                                                | 1.33 ms: 1.42x slower                                                    |
| sqlglot_optimize           | 61.3 ms                                                               | 87.1 ms: 1.42x slower                                                    |
| sympy_str                  | 280 ms                                                                | 401 ms: 1.43x slower                                                     |
| pprint_safe_repr           | 916 ms                                                                | 1.32 sec: 1.44x slower                                                   |
| sqlglot_normalize          | 126 ms                                                                | 181 ms: 1.44x slower                                                     |
| genshi_text                | 27.4 ms                                                               | 39.7 ms: 1.45x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 2.73 sec: 1.45x slower                                                   |
| sqlalchemy_declarative     | 157 ms                                                                | 231 ms: 1.47x slower                                                     |
| sympy_expand               | 454 ms                                                                | 665 ms: 1.47x slower                                                     |
| python_startup_no_site     | 8.37 ms                                                               | 12.3 ms: 1.47x slower                                                    |
| 2to3                       | 308 ms                                                                | 458 ms: 1.49x slower                                                     |
| comprehensions             | 25.4 us                                                               | 38.0 us: 1.50x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 18.4 ms: 1.50x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 2.89 ms: 1.50x slower                                                    |
| fannkuch                   | 443 ms                                                                | 674 ms: 1.52x slower                                                     |
| typing_runtime_protocols   | 181 us                                                                | 276 us: 1.53x slower                                                     |
| scimark_lu                 | 146 ms                                                                | 223 ms: 1.53x slower                                                     |
| bench_thread_pool          | 1.31 ms                                                               | 2.00 ms: 1.53x slower                                                    |
| pyflate                    | 559 ms                                                                | 866 ms: 1.55x slower                                                     |
| telco                      | 8.51 ms                                                               | 13.3 ms: 1.56x slower                                                    |
| django_template            | 40.7 ms                                                               | 64.2 ms: 1.58x slower                                                    |
| coverage                   | 87.3 ms                                                               | 139 ms: 1.59x slower                                                     |
| sqlalchemy_imperative      | 16.7 ms                                                               | 26.7 ms: 1.60x slower                                                    |
| float                      | 92.1 ms                                                               | 150 ms: 1.62x slower                                                     |
| scimark_monte_carlo        | 85.1 ms                                                               | 143 ms: 1.68x slower                                                     |
| html5lib                   | 65.1 ms                                                               | 110 ms: 1.69x slower                                                     |
| unpickle_pure_python       | 260 us                                                                | 440 us: 1.69x slower                                                     |
| scimark_sor                | 150 ms                                                                | 258 ms: 1.72x slower                                                     |
| hexiom                     | 6.98 ms                                                               | 12.2 ms: 1.75x slower                                                    |
| nbody                      | 105 ms                                                                | 185 ms: 1.76x slower                                                     |
| chaos                      | 71.4 ms                                                               | 126 ms: 1.77x slower                                                     |
| python_startup             | 11.4 ms                                                               | 20.4 ms: 1.80x slower                                                    |
| richards_super             | 58.5 ms                                                               | 106 ms: 1.81x slower                                                     |
| pickle_pure_python         | 365 us                                                                | 661 us: 1.81x slower                                                     |
| richards                   | 50.9 ms                                                               | 93.4 ms: 1.83x slower                                                    |
| raytrace                   | 353 ms                                                                | 655 ms: 1.85x slower                                                     |
| sqlglot_transpile          | 1.83 ms                                                               | 3.49 ms: 1.91x slower                                                    |
| mako                       | 12.9 ms                                                               | 25.2 ms: 1.95x slower                                                    |
| go                         | 157 ms                                                                | 332 ms: 2.11x slower                                                     |
| logging_silent             | 127 ns                                                                | 269 ns: 2.12x slower                                                     |
| sqlglot_parse              | 1.46 ms                                                               | 3.16 ms: 2.16x slower                                                    |
| deltablue                  | 4.12 ms                                                               | 10.8 ms: 2.61x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 61.3 ms: 8.69x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.37x slower                                                             |

Benchmark hidden because not significant (3): deepcopy, sqlite_synth, pidigits
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
Ignored benchmarks (8) of results/bm-20250111-3.14.0a3+-22a4421-NOGIL/bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.242x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.25x
- 95% likely to have a slowdown of 1.24x
- 99% likely to have a slowdown of 1.21x

# Memory
- memory change: 1.25x