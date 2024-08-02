# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_compact
- machine: linux-aarch64
- commit hash: 34e6994
- commit date: 2024-06-20
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240620-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 370 ms: 1.20x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.58 sec: 1.20x slower                                                  |
| html5lib       | 65.1 ms                                                               | 71.2 ms: 1.09x slower                                                   |
| tornado_http   | 136 ms                                                                | 147 ms: 1.09x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.14x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240620-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 500 ms: 1.25x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 605 ms: 1.22x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 476 ms: 1.21x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 664 ms: 1.17x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.21 sec: 1.16x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 799 ms: 1.14x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.24 sec: 1.14x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 795 ms: 1.11x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.17x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240620-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 88.2 ms: 1.04x faster                                                   |
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 115 ms: 1.10x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240620-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 248 ms: 1.02x faster                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.85 ms: 1.05x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 30.4 ms: 1.07x slower                                                   |
| regex_compile  | 137 ms                                                                | 175 ms: 1.28x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.09x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240620-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 190 ms: 1.03x faster                                                    |
| xml_etree_iterparse  | 150 ms                                                                | 148 ms: 1.02x faster                                                    |
| pickle_list          | 5.25 us                                                               | 5.28 us: 1.01x slower                                                   |
| tomli_loads          | 2.59 sec                                                              | 2.63 sec: 1.01x slower                                                  |
| pickle               | 13.4 us                                                               | 13.8 us: 1.03x slower                                                   |
| unpickle             | 18.5 us                                                               | 19.5 us: 1.06x slower                                                   |
| unpickle_pure_python | 260 us                                                                | 279 us: 1.07x slower                                                    |
| unpickle_list        | 6.17 us                                                               | 6.65 us: 1.08x slower                                                   |
| json_loads           | 30.7 us                                                               | 33.2 us: 1.08x slower                                                   |
| pickle_pure_python   | 365 us                                                                | 395 us: 1.08x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 13.4 ms: 1.09x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.03x slower                                                            |

Benchmark hidden because not significant (3): xml_etree_process, xml_etree_generate, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240620-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 11.2 ms: 1.34x slower                                                   |
| python_startup         | 11.4 ms                                                               | 15.8 ms: 1.39x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.36x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240620-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.1 ms: 1.02x slower                                                   |
| django_template | 40.7 ms                                                               | 49.0 ms: 1.20x slower                                                   |
| genshi_text     | 27.4 ms                                                               | 33.5 ms: 1.22x slower                                                   |
| genshi_xml      | 60.6 ms                                                               | 79.0 ms: 1.30x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.18x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240620-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 49.6 us                                                               | 38.5 us: 1.29x faster                                                   |
| async_tree_none            | 624 ms                                                                | 500 ms: 1.25x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 605 ms: 1.22x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 476 ms: 1.21x faster                                                    |
| deepcopy                   | 446 us                                                                | 378 us: 1.18x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 664 ms: 1.17x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.21 sec: 1.16x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 799 ms: 1.14x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.24 sec: 1.14x faster                                                  |
| generators                 | 43.5 ms                                                               | 38.8 ms: 1.12x faster                                                   |
| pathlib                    | 24.5 ms                                                               | 22.1 ms: 1.11x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 795 ms: 1.11x faster                                                    |
| comprehensions             | 25.4 us                                                               | 23.0 us: 1.10x faster                                                   |
| raytrace                   | 353 ms                                                                | 324 ms: 1.09x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.88 us: 1.06x faster                                                   |
| logging_simple             | 7.63 us                                                               | 7.25 us: 1.05x faster                                                   |
| float                      | 92.1 ms                                                               | 88.2 ms: 1.04x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 190 ms: 1.03x faster                                                    |
| regex_dna                  | 254 ms                                                                | 248 ms: 1.02x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 4.03 us: 1.02x faster                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 148 ms: 1.02x faster                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 85.5 ms: 1.01x faster                                                   |
| pickle_list                | 5.25 us                                                               | 5.28 us: 1.01x slower                                                   |
| mdp                        | 3.41 sec                                                              | 3.44 sec: 1.01x slower                                                  |
| sqlite_synth               | 3.77 us                                                               | 3.80 us: 1.01x slower                                                   |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.33 ms: 1.01x slower                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.63 sec: 1.01x slower                                                  |
| mako                       | 12.9 ms                                                               | 13.1 ms: 1.02x slower                                                   |
| thrift                     | 937 us                                                                | 958 us: 1.02x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.25 sec: 1.03x slower                                                  |
| pickle                     | 13.4 us                                                               | 13.8 us: 1.03x slower                                                   |
| async_generators           | 491 ms                                                                | 507 ms: 1.03x slower                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.85 ms: 1.05x slower                                                   |
| richards_super             | 58.5 ms                                                               | 61.5 ms: 1.05x slower                                                   |
| dask                       | 376 ms                                                                | 396 ms: 1.05x slower                                                    |
| fannkuch                   | 443 ms                                                                | 468 ms: 1.06x slower                                                    |
| unpickle                   | 18.5 us                                                               | 19.5 us: 1.06x slower                                                   |
| pyflate                    | 559 ms                                                                | 592 ms: 1.06x slower                                                    |
| meteor_contest             | 112 ms                                                                | 119 ms: 1.06x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 7.50 ms: 1.06x slower                                                   |
| json                       | 5.54 ms                                                               | 5.91 ms: 1.07x slower                                                   |
| deltablue                  | 4.12 ms                                                               | 4.41 ms: 1.07x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 30.4 ms: 1.07x slower                                                   |
| unpickle_pure_python       | 260 us                                                                | 279 us: 1.07x slower                                                    |
| richards                   | 50.9 ms                                                               | 54.8 ms: 1.08x slower                                                   |
| unpickle_list              | 6.17 us                                                               | 6.65 us: 1.08x slower                                                   |
| asyncio_tcp                | 566 ms                                                                | 611 ms: 1.08x slower                                                    |
| json_loads                 | 30.7 us                                                               | 33.2 us: 1.08x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 395 us: 1.08x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.36 sec: 1.08x slower                                                  |
| logging_silent             | 127 ns                                                                | 138 ns: 1.08x slower                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.59 ms: 1.09x slower                                                   |
| tornado_http               | 136 ms                                                                | 147 ms: 1.09x slower                                                    |
| scimark_fft                | 418 ms                                                                | 456 ms: 1.09x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.4 ms: 1.09x slower                                                   |
| html5lib                   | 65.1 ms                                                               | 71.2 ms: 1.09x slower                                                   |
| sqlglot_transpile          | 1.83 ms                                                               | 2.01 ms: 1.10x slower                                                   |
| nbody                      | 105 ms                                                                | 115 ms: 1.10x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.89 ms: 1.11x slower                                                   |
| go                         | 157 ms                                                                | 176 ms: 1.12x slower                                                    |
| spectral_norm              | 131 ms                                                                | 147 ms: 1.12x slower                                                    |
| sqlglot_normalize          | 126 ms                                                                | 143 ms: 1.14x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 5.01 ms: 1.14x slower                                                   |
| sqlglot_optimize           | 61.3 ms                                                               | 70.0 ms: 1.14x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 206 us: 1.14x slower                                                    |
| coverage                   | 87.3 ms                                                               | 102 ms: 1.16x slower                                                    |
| scimark_sor                | 150 ms                                                                | 174 ms: 1.16x slower                                                    |
| telco                      | 8.51 ms                                                               | 9.97 ms: 1.17x slower                                                   |
| pylint                     | 355 ms                                                                | 418 ms: 1.18x slower                                                    |
| sympy_str                  | 280 ms                                                                | 332 ms: 1.19x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.58 sec: 1.20x slower                                                  |
| 2to3                       | 308 ms                                                                | 370 ms: 1.20x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 1.10 sec: 1.20x slower                                                  |
| django_template            | 40.7 ms                                                               | 49.0 ms: 1.20x slower                                                   |
| sympy_expand               | 454 ms                                                                | 550 ms: 1.21x slower                                                    |
| sympy_integrate            | 21.6 ms                                                               | 26.2 ms: 1.21x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.33 ms: 1.21x slower                                                   |
| chaos                      | 71.4 ms                                                               | 86.7 ms: 1.21x slower                                                   |
| sympy_sum                  | 154 ms                                                                | 188 ms: 1.22x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 2.30 sec: 1.22x slower                                                  |
| genshi_text                | 27.4 ms                                                               | 33.5 ms: 1.22x slower                                                   |
| nqueens                    | 99.2 ms                                                               | 122 ms: 1.23x slower                                                    |
| dulwich_log                | 62.0 ms                                                               | 76.2 ms: 1.23x slower                                                   |
| scimark_lu                 | 146 ms                                                                | 181 ms: 1.24x slower                                                    |
| regex_compile              | 137 ms                                                                | 175 ms: 1.28x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 9.00 ms: 1.29x slower                                                   |
| genshi_xml                 | 60.6 ms                                                               | 79.0 ms: 1.30x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 11.2 ms: 1.34x slower                                                   |
| python_startup             | 11.4 ms                                                               | 15.8 ms: 1.39x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.06x slower                                                            |

Benchmark hidden because not significant (6): scimark_monte_carlo, coroutines, xml_etree_process, asyncio_websockets, xml_etree_generate, pickle_dict
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of results/bm-20240620-3.14.0a0-34e6994-JIT/bm-20240620-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-34e6994.json: bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.01x