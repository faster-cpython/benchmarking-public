# Results vs. 3.12.0

- fork: python
- ref: 61b35f74aa4a6ac60663
- machine: linux-aarch64
- commit hash: 61b35f7
- commit date: 2025-01-18
- overall geometric mean: 1.132x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x slower
- Memory change: 1.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 387 ms: 1.26x slower                                                     |
| docutils       | 2.98 sec                                                              | 3.41 sec: 1.14x slower                                                   |
| html5lib       | 65.1 ms                                                               | 76.2 ms: 1.17x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.19x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 920 ms: 1.53x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 492 ms: 1.51x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 966 ms: 1.46x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 399 ms: 1.44x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 538 ms: 1.44x faster                                                     |
| async_tree_none            | 624 ms                                                                | 442 ms: 1.41x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 678 ms: 1.30x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 733 ms: 1.24x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.41x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 103 ms: 1.12x slower                                                     |
| nbody          | 105 ms                                                                | 182 ms: 1.74x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.25x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.02 ms: 1.16x faster                                                    |
| regex_v8       | 28.3 ms                                                               | 31.9 ms: 1.13x slower                                                    |
| regex_compile  | 137 ms                                                                | 159 ms: 1.16x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_iterparse  | 150 ms                                                                | 133 ms: 1.13x faster                                                     |
| xml_etree_parse      | 195 ms                                                                | 177 ms: 1.10x faster                                                     |
| pickle_dict          | 37.3 us                                                               | 40.6 us: 1.09x slower                                                    |
| unpickle             | 18.5 us                                                               | 21.1 us: 1.14x slower                                                    |
| unpickle_list        | 6.17 us                                                               | 7.27 us: 1.18x slower                                                    |
| pickle               | 13.4 us                                                               | 15.8 us: 1.18x slower                                                    |
| pickle_list          | 5.25 us                                                               | 6.32 us: 1.20x slower                                                    |
| json_loads           | 30.7 us                                                               | 37.2 us: 1.21x slower                                                    |
| xml_etree_generate   | 112 ms                                                                | 140 ms: 1.25x slower                                                     |
| tomli_loads          | 2.59 sec                                                              | 3.25 sec: 1.25x slower                                                   |
| unpickle_pure_python | 260 us                                                                | 331 us: 1.27x slower                                                     |
| pickle_pure_python   | 365 us                                                                | 483 us: 1.32x slower                                                     |
| xml_etree_process    | 79.0 ms                                                               | 104 ms: 1.32x slower                                                     |
| json_dumps           | 12.3 ms                                                               | 16.7 ms: 1.36x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.17x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 12.2 ms: 1.46x slower                                                    |
| python_startup         | 11.4 ms                                                               | 20.0 ms: 1.76x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.60x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 80.2 ms: 1.32x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 37.2 ms: 1.36x slower                                                    |
| django_template | 40.7 ms                                                               | 56.5 ms: 1.39x slower                                                    |
| mako            | 12.9 ms                                                               | 23.6 ms: 1.83x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.46x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 920 ms: 1.53x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 492 ms: 1.51x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 966 ms: 1.46x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 399 ms: 1.44x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 538 ms: 1.44x faster                                                     |
| async_tree_none            | 624 ms                                                                | 442 ms: 1.41x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 678 ms: 1.30x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 733 ms: 1.24x faster                                                     |
| regex_effbot               | 4.64 ms                                                               | 4.02 ms: 1.16x faster                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 133 ms: 1.13x faster                                                     |
| xml_etree_parse            | 195 ms                                                                | 177 ms: 1.10x faster                                                     |
| pathlib                    | 24.5 ms                                                               | 23.5 ms: 1.04x faster                                                    |
| deepcopy                   | 446 us                                                                | 429 us: 1.04x faster                                                     |
| asyncio_websockets         | 658 ms                                                                | 680 ms: 1.03x slower                                                     |
| deepcopy_memo              | 49.6 us                                                               | 52.9 us: 1.06x slower                                                    |
| pickle_dict                | 37.3 us                                                               | 40.6 us: 1.09x slower                                                    |
| asyncio_tcp                | 566 ms                                                                | 618 ms: 1.09x slower                                                     |
| coroutines                 | 29.0 ms                                                               | 31.8 ms: 1.10x slower                                                    |
| pylint                     | 355 ms                                                                | 392 ms: 1.10x slower                                                     |
| async_generators           | 491 ms                                                                | 542 ms: 1.10x slower                                                     |
| dulwich_log                | 62.0 ms                                                               | 69.0 ms: 1.11x slower                                                    |
| spectral_norm              | 131 ms                                                                | 145 ms: 1.11x slower                                                     |
| float                      | 92.1 ms                                                               | 103 ms: 1.12x slower                                                     |
| mdp                        | 3.41 sec                                                              | 3.84 sec: 1.13x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 31.9 ms: 1.13x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 2.17 ms: 1.13x slower                                                    |
| unpickle                   | 18.5 us                                                               | 21.1 us: 1.14x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.41 sec: 1.14x slower                                                   |
| json                       | 5.54 ms                                                               | 6.34 ms: 1.14x slower                                                    |
| go                         | 157 ms                                                                | 181 ms: 1.15x slower                                                     |
| pycparser                  | 1.26 sec                                                              | 1.46 sec: 1.16x slower                                                   |
| regex_compile              | 137 ms                                                                | 159 ms: 1.16x slower                                                     |
| deepcopy_reduce            | 4.10 us                                                               | 4.76 us: 1.16x slower                                                    |
| comprehensions             | 25.4 us                                                               | 29.6 us: 1.16x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 76.2 ms: 1.17x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.57 sec: 1.18x slower                                                   |
| unpickle_list              | 6.17 us                                                               | 7.27 us: 1.18x slower                                                    |
| scimark_fft                | 418 ms                                                                | 494 ms: 1.18x slower                                                     |
| pickle                     | 13.4 us                                                               | 15.8 us: 1.18x slower                                                    |
| pyflate                    | 559 ms                                                                | 661 ms: 1.18x slower                                                     |
| logging_simple             | 7.63 us                                                               | 9.16 us: 1.20x slower                                                    |
| pickle_list                | 5.25 us                                                               | 6.32 us: 1.20x slower                                                    |
| raytrace                   | 353 ms                                                                | 426 ms: 1.21x slower                                                     |
| logging_format             | 8.34 us                                                               | 10.1 us: 1.21x slower                                                    |
| json_loads                 | 30.7 us                                                               | 37.2 us: 1.21x slower                                                    |
| scimark_sor                | 150 ms                                                                | 183 ms: 1.22x slower                                                     |
| gc_traversal               | 4.40 ms                                                               | 5.42 ms: 1.23x slower                                                    |
| chaos                      | 71.4 ms                                                               | 88.7 ms: 1.24x slower                                                    |
| xml_etree_generate         | 112 ms                                                                | 140 ms: 1.25x slower                                                     |
| tomli_loads                | 2.59 sec                                                              | 3.25 sec: 1.25x slower                                                   |
| logging_silent             | 127 ns                                                                | 159 ns: 1.25x slower                                                     |
| 2to3                       | 308 ms                                                                | 387 ms: 1.26x slower                                                     |
| sqlglot_normalize          | 126 ms                                                                | 159 ms: 1.27x slower                                                     |
| pprint_safe_repr           | 916 ms                                                                | 1.16 sec: 1.27x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 2.39 sec: 1.27x slower                                                   |
| unpickle_pure_python       | 260 us                                                                | 331 us: 1.27x slower                                                     |
| sympy_sum                  | 154 ms                                                                | 199 ms: 1.29x slower                                                     |
| sqlglot_optimize           | 61.3 ms                                                               | 79.4 ms: 1.30x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 112 ms: 1.30x slower                                                     |
| scimark_lu                 | 146 ms                                                                | 189 ms: 1.30x slower                                                     |
| sqlalchemy_declarative     | 157 ms                                                                | 205 ms: 1.30x slower                                                     |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 8.06 ms: 1.30x slower                                                    |
| sympy_str                  | 280 ms                                                                | 364 ms: 1.30x slower                                                     |
| sqlalchemy_imperative      | 16.7 ms                                                               | 21.8 ms: 1.31x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 483 us: 1.32x slower                                                     |
| xml_etree_process          | 79.0 ms                                                               | 104 ms: 1.32x slower                                                     |
| genshi_xml                 | 60.6 ms                                                               | 80.2 ms: 1.32x slower                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 113 ms: 1.33x slower                                                     |
| genshi_text                | 27.4 ms                                                               | 37.2 ms: 1.36x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 135 ms: 1.36x slower                                                     |
| json_dumps                 | 12.3 ms                                                               | 16.7 ms: 1.36x slower                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 2.49 ms: 1.36x slower                                                    |
| sympy_expand               | 454 ms                                                                | 621 ms: 1.37x slower                                                     |
| hexiom                     | 6.98 ms                                                               | 9.63 ms: 1.38x slower                                                    |
| thrift                     | 937 us                                                                | 1.29 ms: 1.38x slower                                                    |
| django_template            | 40.7 ms                                                               | 56.5 ms: 1.39x slower                                                    |
| telco                      | 8.51 ms                                                               | 11.8 ms: 1.39x slower                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.83 ms: 1.40x slower                                                    |
| meteor_contest             | 112 ms                                                                | 158 ms: 1.41x slower                                                     |
| sympy_integrate            | 21.6 ms                                                               | 31.0 ms: 1.43x slower                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 2.12 ms: 1.45x slower                                                    |
| richards                   | 50.9 ms                                                               | 73.8 ms: 1.45x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 12.2 ms: 1.46x slower                                                    |
| coverage                   | 87.3 ms                                                               | 132 ms: 1.51x slower                                                     |
| richards_super             | 58.5 ms                                                               | 88.6 ms: 1.52x slower                                                    |
| fannkuch                   | 443 ms                                                                | 678 ms: 1.53x slower                                                     |
| deltablue                  | 4.12 ms                                                               | 6.30 ms: 1.53x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 288 us: 1.59x slower                                                     |
| nbody                      | 105 ms                                                                | 182 ms: 1.74x slower                                                     |
| python_startup             | 11.4 ms                                                               | 20.0 ms: 1.76x slower                                                    |
| mako                       | 12.9 ms                                                               | 23.6 ms: 1.83x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 56.3 ms: 7.99x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.20x slower                                                             |

Benchmark hidden because not significant (4): sqlite_synth, pidigits, generators, regex_dna
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
Ignored benchmarks (8) of results/bm-20250118-3.14.0a4+-61b35f7-NOGIL/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.132x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.14x
- 95% likely to have a slowdown of 1.13x
- 99% likely to have a slowdown of 1.11x

# Memory
- memory change: 1.25x