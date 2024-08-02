# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_compact
- machine: linux-aarch64
- commit hash: e04d5ab
- commit date: 2024-06-19
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240619-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 366 ms: 1.19x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.56 sec: 1.19x slower                                                  |
| html5lib       | 65.1 ms                                                               | 71.1 ms: 1.09x slower                                                   |
| tornado_http   | 136 ms                                                                | 138 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.12x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240619-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 505 ms: 1.23x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 473 ms: 1.22x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 614 ms: 1.21x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.20 sec: 1.17x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 664 ms: 1.17x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.24 sec: 1.14x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 813 ms: 1.12x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 793 ms: 1.11x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.17x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240619-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 88.2 ms: 1.04x faster                                                   |
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 114 ms: 1.09x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240619-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.90 ms: 1.06x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 30.2 ms: 1.07x slower                                                   |
| regex_compile  | 137 ms                                                                | 171 ms: 1.25x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.09x slower                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240619-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 187 ms: 1.04x faster                                                    |
| tomli_loads          | 2.59 sec                                                              | 2.61 sec: 1.00x slower                                                  |
| pickle               | 13.4 us                                                               | 13.6 us: 1.02x slower                                                   |
| unpickle             | 18.5 us                                                               | 19.5 us: 1.06x slower                                                   |
| json_loads           | 30.7 us                                                               | 32.6 us: 1.06x slower                                                   |
| unpickle_pure_python | 260 us                                                                | 278 us: 1.07x slower                                                    |
| pickle_pure_python   | 365 us                                                                | 392 us: 1.07x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 13.2 ms: 1.08x slower                                                   |
| unpickle_list        | 6.17 us                                                               | 6.73 us: 1.09x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.03x slower                                                            |

Benchmark hidden because not significant (5): xml_etree_iterparse, pickle_list, pickle_dict, xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240619-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 11.1 ms: 1.32x slower                                                   |
| python_startup         | 11.4 ms                                                               | 15.5 ms: 1.36x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.34x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240619-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.1 ms: 1.02x slower                                                   |
| genshi_text     | 27.4 ms                                                               | 33.8 ms: 1.23x slower                                                   |
| django_template | 40.7 ms                                                               | 50.2 ms: 1.23x slower                                                   |
| genshi_xml      | 60.6 ms                                                               | 78.6 ms: 1.30x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.19x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240619-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 49.6 us                                                               | 38.7 us: 1.28x faster                                                   |
| async_tree_none            | 624 ms                                                                | 505 ms: 1.23x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 473 ms: 1.22x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 614 ms: 1.21x faster                                                    |
| deepcopy                   | 446 us                                                                | 373 us: 1.20x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.20 sec: 1.17x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 664 ms: 1.17x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.24 sec: 1.14x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 813 ms: 1.12x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 793 ms: 1.11x faster                                                    |
| generators                 | 43.5 ms                                                               | 39.2 ms: 1.11x faster                                                   |
| pathlib                    | 24.5 ms                                                               | 22.2 ms: 1.11x faster                                                   |
| comprehensions             | 25.4 us                                                               | 23.0 us: 1.11x faster                                                   |
| raytrace                   | 353 ms                                                                | 321 ms: 1.10x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.76 us: 1.07x faster                                                   |
| logging_simple             | 7.63 us                                                               | 7.16 us: 1.07x faster                                                   |
| float                      | 92.1 ms                                                               | 88.2 ms: 1.04x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 187 ms: 1.04x faster                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 85.9 ms: 1.01x faster                                                   |
| coroutines                 | 29.0 ms                                                               | 28.8 ms: 1.01x faster                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.61 sec: 1.00x slower                                                  |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| mdp                        | 3.41 sec                                                              | 3.45 sec: 1.01x slower                                                  |
| scimark_monte_carlo        | 85.1 ms                                                               | 86.1 ms: 1.01x slower                                                   |
| pickle                     | 13.4 us                                                               | 13.6 us: 1.02x slower                                                   |
| tornado_http               | 136 ms                                                                | 138 ms: 1.02x slower                                                    |
| asyncio_tcp                | 566 ms                                                                | 577 ms: 1.02x slower                                                    |
| mako                       | 12.9 ms                                                               | 13.1 ms: 1.02x slower                                                   |
| sqlite_synth               | 3.77 us                                                               | 3.85 us: 1.02x slower                                                   |
| thrift                     | 937 us                                                                | 960 us: 1.03x slower                                                    |
| meteor_contest             | 112 ms                                                                | 115 ms: 1.03x slower                                                    |
| async_generators           | 491 ms                                                                | 510 ms: 1.04x slower                                                    |
| dask                       | 376 ms                                                                | 392 ms: 1.04x slower                                                    |
| json                       | 5.54 ms                                                               | 5.79 ms: 1.04x slower                                                   |
| fannkuch                   | 443 ms                                                                | 469 ms: 1.06x slower                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.90 ms: 1.06x slower                                                   |
| unpickle                   | 18.5 us                                                               | 19.5 us: 1.06x slower                                                   |
| json_loads                 | 30.7 us                                                               | 32.6 us: 1.06x slower                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 7.50 ms: 1.06x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 1.34 sec: 1.07x slower                                                  |
| regex_v8                   | 28.3 ms                                                               | 30.2 ms: 1.07x slower                                                   |
| richards_super             | 58.5 ms                                                               | 62.5 ms: 1.07x slower                                                   |
| unpickle_pure_python       | 260 us                                                                | 278 us: 1.07x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 392 us: 1.07x slower                                                    |
| deltablue                  | 4.12 ms                                                               | 4.43 ms: 1.07x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 13.2 ms: 1.08x slower                                                   |
| sqlglot_parse              | 1.46 ms                                                               | 1.58 ms: 1.08x slower                                                   |
| richards                   | 50.9 ms                                                               | 55.2 ms: 1.08x slower                                                   |
| logging_silent             | 127 ns                                                                | 138 ns: 1.09x slower                                                    |
| scimark_fft                | 418 ms                                                                | 456 ms: 1.09x slower                                                    |
| unpickle_list              | 6.17 us                                                               | 6.73 us: 1.09x slower                                                   |
| html5lib                   | 65.1 ms                                                               | 71.1 ms: 1.09x slower                                                   |
| nbody                      | 105 ms                                                                | 114 ms: 1.09x slower                                                    |
| pyflate                    | 559 ms                                                                | 614 ms: 1.10x slower                                                    |
| dulwich_log                | 62.0 ms                                                               | 68.8 ms: 1.11x slower                                                   |
| sqlglot_transpile          | 1.83 ms                                                               | 2.03 ms: 1.11x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 4.92 ms: 1.12x slower                                                   |
| go                         | 157 ms                                                                | 176 ms: 1.12x slower                                                    |
| sqlglot_normalize          | 126 ms                                                                | 142 ms: 1.13x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.04 ms: 1.14x slower                                                   |
| sqlglot_optimize           | 61.3 ms                                                               | 69.8 ms: 1.14x slower                                                   |
| spectral_norm              | 131 ms                                                                | 150 ms: 1.14x slower                                                    |
| sympy_str                  | 280 ms                                                                | 323 ms: 1.16x slower                                                    |
| scimark_sor                | 150 ms                                                                | 174 ms: 1.16x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 116 ms: 1.17x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 211 us: 1.17x slower                                                    |
| pylint                     | 355 ms                                                                | 414 ms: 1.17x slower                                                    |
| sympy_sum                  | 154 ms                                                                | 182 ms: 1.18x slower                                                    |
| sympy_expand               | 454 ms                                                                | 538 ms: 1.19x slower                                                    |
| 2to3                       | 308 ms                                                                | 366 ms: 1.19x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.56 sec: 1.19x slower                                                  |
| sympy_integrate            | 21.6 ms                                                               | 25.8 ms: 1.19x slower                                                   |
| coverage                   | 87.3 ms                                                               | 105 ms: 1.20x slower                                                    |
| chaos                      | 71.4 ms                                                               | 85.6 ms: 1.20x slower                                                   |
| pprint_safe_repr           | 916 ms                                                                | 1.11 sec: 1.21x slower                                                  |
| telco                      | 8.51 ms                                                               | 10.4 ms: 1.22x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 2.31 sec: 1.23x slower                                                  |
| genshi_text                | 27.4 ms                                                               | 33.8 ms: 1.23x slower                                                   |
| django_template            | 40.7 ms                                                               | 50.2 ms: 1.23x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.37 ms: 1.24x slower                                                   |
| regex_compile              | 137 ms                                                                | 171 ms: 1.25x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 184 ms: 1.26x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 8.94 ms: 1.28x slower                                                   |
| genshi_xml                 | 60.6 ms                                                               | 78.6 ms: 1.30x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 11.1 ms: 1.32x slower                                                   |
| python_startup             | 11.4 ms                                                               | 15.5 ms: 1.36x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.06x slower                                                            |

Benchmark hidden because not significant (10): xml_etree_iterparse, deepcopy_reduce, pickle_list, bench_thread_pool, asyncio_tcp_ssl, asyncio_websockets, pickle_dict, regex_dna, xml_etree_process, xml_etree_generate
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of results/bm-20240619-3.14.0a0-e04d5ab-JIT/bm-20240619-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-e04d5ab.json: bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.01x