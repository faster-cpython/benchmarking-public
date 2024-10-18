# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_likely
- machine: linux-aarch64
- commit hash: bad9944
- commit date: 2024-10-18
- overall geometric mean: 1.16x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 382 ms: 1.24x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.58 sec: 1.20x slower                                                  |
| html5lib       | 65.1 ms                                                               | 71.9 ms: 1.11x slower                                                   |
| tornado_http   | 136 ms                                                                | 147 ms: 1.08x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.16x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 536 ms: 1.38x faster                                                    |
| async_tree_none            | 624 ms                                                                | 457 ms: 1.36x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 600 ms: 1.29x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 446 ms: 1.29x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 755 ms: 1.21x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.18 sec: 1.19x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 742 ms: 1.19x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.25 sec: 1.13x faster                                                  |
| Geometric mean             | (ref)                                                                 | 1.25x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| float          | 92.1 ms                                                               | 97.8 ms: 1.06x slower                                                   |
| nbody          | 105 ms                                                                | 115 ms: 1.10x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.06x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.96 ms: 1.07x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 31.0 ms: 1.10x slower                                                   |
| regex_compile  | 137 ms                                                                | 179 ms: 1.31x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.11x slower                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.59 sec                                                              | 2.66 sec: 1.03x slower                                                  |
| xml_etree_process    | 79.0 ms                                                               | 81.2 ms: 1.03x slower                                                   |
| json_loads           | 30.7 us                                                               | 31.6 us: 1.03x slower                                                   |
| pickle               | 13.4 us                                                               | 13.9 us: 1.04x slower                                                   |
| unpickle_pure_python | 260 us                                                                | 270 us: 1.04x slower                                                    |
| unpickle_list        | 6.17 us                                                               | 6.42 us: 1.04x slower                                                   |
| unpickle             | 18.5 us                                                               | 19.6 us: 1.06x slower                                                   |
| pickle_pure_python   | 365 us                                                                | 392 us: 1.07x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 14.6 ms: 1.19x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.04x slower                                                            |

Benchmark hidden because not significant (5): xml_etree_parse, xml_etree_generate, xml_etree_iterparse, pickle_list, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.73 ms: 1.04x slower                                                   |
| python_startup         | 11.4 ms                                                               | 14.5 ms: 1.28x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.16x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.6 ms: 1.05x slower                                                   |
| genshi_text     | 27.4 ms                                                               | 34.1 ms: 1.24x slower                                                   |
| django_template | 40.7 ms                                                               | 52.6 ms: 1.29x slower                                                   |
| genshi_xml      | 60.6 ms                                                               | 83.9 ms: 1.38x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.24x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 536 ms: 1.38x faster                                                    |
| async_tree_none            | 624 ms                                                                | 457 ms: 1.36x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 600 ms: 1.29x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 446 ms: 1.29x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 39.3 us: 1.26x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 755 ms: 1.21x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.18 sec: 1.19x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 742 ms: 1.19x faster                                                    |
| deepcopy                   | 446 us                                                                | 380 us: 1.17x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 21.8 ms: 1.13x faster                                                   |
| async_tree_io_tg           | 1.40 sec                                                              | 1.25 sec: 1.13x faster                                                  |
| deepcopy_reduce            | 4.10 us                                                               | 3.98 us: 1.03x faster                                                   |
| logging_format             | 8.34 us                                                               | 8.12 us: 1.03x faster                                                   |
| comprehensions             | 25.4 us                                                               | 24.8 us: 1.02x faster                                                   |
| logging_simple             | 7.63 us                                                               | 7.49 us: 1.02x faster                                                   |
| asyncio_websockets         | 658 ms                                                                | 663 ms: 1.01x slower                                                    |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 148 ms: 1.02x slower                                                    |
| json                       | 5.54 ms                                                               | 5.63 ms: 1.02x slower                                                   |
| mdp                        | 3.41 sec                                                              | 3.50 sec: 1.03x slower                                                  |
| tomli_loads                | 2.59 sec                                                              | 2.66 sec: 1.03x slower                                                  |
| xml_etree_process          | 79.0 ms                                                               | 81.2 ms: 1.03x slower                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 89.2 ms: 1.03x slower                                                   |
| json_loads                 | 30.7 us                                                               | 31.6 us: 1.03x slower                                                   |
| scimark_sor                | 150 ms                                                                | 154 ms: 1.03x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.26 sec: 1.03x slower                                                  |
| pickle                     | 13.4 us                                                               | 13.9 us: 1.04x slower                                                   |
| unpickle_pure_python       | 260 us                                                                | 270 us: 1.04x slower                                                    |
| thrift                     | 937 us                                                                | 975 us: 1.04x slower                                                    |
| unpickle_list              | 6.17 us                                                               | 6.42 us: 1.04x slower                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 88.7 ms: 1.04x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.73 ms: 1.04x slower                                                   |
| logging_silent             | 127 ns                                                                | 133 ns: 1.05x slower                                                    |
| async_generators           | 491 ms                                                                | 515 ms: 1.05x slower                                                    |
| mako                       | 12.9 ms                                                               | 13.6 ms: 1.05x slower                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.38 ms: 1.06x slower                                                   |
| sqlite_synth               | 3.77 us                                                               | 4.00 us: 1.06x slower                                                   |
| float                      | 92.1 ms                                                               | 97.8 ms: 1.06x slower                                                   |
| unpickle                   | 18.5 us                                                               | 19.6 us: 1.06x slower                                                   |
| regex_effbot               | 4.64 ms                                                               | 4.96 ms: 1.07x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 392 us: 1.07x slower                                                    |
| tornado_http               | 136 ms                                                                | 147 ms: 1.08x slower                                                    |
| scimark_fft                | 418 ms                                                                | 455 ms: 1.09x slower                                                    |
| deltablue                  | 4.12 ms                                                               | 4.50 ms: 1.09x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 31.0 ms: 1.10x slower                                                   |
| asyncio_tcp                | 566 ms                                                                | 621 ms: 1.10x slower                                                    |
| nbody                      | 105 ms                                                                | 115 ms: 1.10x slower                                                    |
| meteor_contest             | 112 ms                                                                | 124 ms: 1.10x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 71.9 ms: 1.11x slower                                                   |
| coverage                   | 87.3 ms                                                               | 98.6 ms: 1.13x slower                                                   |
| telco                      | 8.51 ms                                                               | 9.64 ms: 1.13x slower                                                   |
| pyflate                    | 559 ms                                                                | 642 ms: 1.15x slower                                                    |
| fannkuch                   | 443 ms                                                                | 512 ms: 1.15x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.23 ms: 1.17x slower                                                   |
| sqlglot_parse              | 1.46 ms                                                               | 1.71 ms: 1.17x slower                                                   |
| spectral_norm              | 131 ms                                                                | 154 ms: 1.18x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 14.6 ms: 1.19x slower                                                   |
| go                         | 157 ms                                                                | 187 ms: 1.19x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.58 sec: 1.20x slower                                                  |
| chaos                      | 71.4 ms                                                               | 85.7 ms: 1.20x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 1.52 sec: 1.21x slower                                                  |
| typing_runtime_protocols   | 181 us                                                                | 219 us: 1.21x slower                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 2.25 ms: 1.23x slower                                                   |
| richards_super             | 58.5 ms                                                               | 72.2 ms: 1.24x slower                                                   |
| 2to3                       | 308 ms                                                                | 382 ms: 1.24x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 34.1 ms: 1.24x slower                                                   |
| nqueens                    | 99.2 ms                                                               | 124 ms: 1.25x slower                                                    |
| sqlglot_normalize          | 126 ms                                                                | 159 ms: 1.26x slower                                                    |
| richards                   | 50.9 ms                                                               | 64.6 ms: 1.27x slower                                                   |
| sympy_str                  | 280 ms                                                                | 356 ms: 1.27x slower                                                    |
| python_startup             | 11.4 ms                                                               | 14.5 ms: 1.28x slower                                                   |
| dulwich_log                | 62.0 ms                                                               | 79.9 ms: 1.29x slower                                                   |
| django_template            | 40.7 ms                                                               | 52.6 ms: 1.29x slower                                                   |
| sympy_expand               | 454 ms                                                                | 589 ms: 1.30x slower                                                    |
| regex_compile              | 137 ms                                                                | 179 ms: 1.31x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 1.23 sec: 1.35x slower                                                  |
| sqlglot_optimize           | 61.3 ms                                                               | 83.1 ms: 1.35x slower                                                   |
| sympy_integrate            | 21.6 ms                                                               | 29.3 ms: 1.36x slower                                                   |
| generators                 | 43.5 ms                                                               | 59.1 ms: 1.36x slower                                                   |
| genshi_xml                 | 60.6 ms                                                               | 83.9 ms: 1.38x slower                                                   |
| sympy_sum                  | 154 ms                                                                | 214 ms: 1.38x slower                                                    |
| pylint                     | 355 ms                                                                | 492 ms: 1.39x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 2.62 sec: 1.39x slower                                                  |
| gc_traversal               | 4.40 ms                                                               | 6.24 ms: 1.42x slower                                                   |
| hexiom                     | 6.98 ms                                                               | 10.3 ms: 1.48x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 3.73 ms: 1.94x slower                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 2.25 sec: 319.12x slower                                                |
| Geometric mean             | (ref)                                                                 | 1.16x slower                                                            |

Benchmark hidden because not significant (8): xml_etree_parse, coroutines, xml_etree_generate, xml_etree_iterparse, raytrace, regex_dna, pickle_list, pickle_dict
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (3) of results/bm-20241018-3.14.0a1+-bad9944-JIT/bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944.json: bpe_tokeniser, sphinx, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.10x