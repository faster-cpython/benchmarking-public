# Results vs. 3.12.0

- fork: nick-arm
- ref: codecache
- machine: linux-aarch64
- commit hash: 0be1ef3
- commit date: 2024-10-21
- overall geometric mean: 1.083x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241021-arminc-aarch64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 375 ms: 1.22x slower                                              |
| docutils       | 2.98 sec                                                              | 3.55 sec: 1.19x slower                                            |
| html5lib       | 65.1 ms                                                               | 72.7 ms: 1.12x slower                                             |
| tornado_http   | 136 ms                                                                | 150 ms: 1.10x slower                                              |
| Geometric mean | (ref)                                                                 | 1.16x slower                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241021-arminc-aarch64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 547 ms: 1.35x faster                                              |
| async_tree_none            | 624 ms                                                                | 473 ms: 1.32x faster                                              |
| async_tree_memoization     | 777 ms                                                                | 607 ms: 1.28x faster                                              |
| async_tree_none_tg         | 577 ms                                                                | 453 ms: 1.27x faster                                              |
| async_tree_io              | 1.41 sec                                                              | 1.17 sec: 1.21x faster                                            |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 760 ms: 1.20x faster                                              |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 744 ms: 1.19x faster                                              |
| async_tree_io_tg           | 1.40 sec                                                              | 1.27 sec: 1.11x faster                                            |
| Geometric mean             | (ref)                                                                 | 1.24x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241021-arminc-aarch64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                              |
| float          | 92.1 ms                                                               | 97.7 ms: 1.06x slower                                             |
| nbody          | 105 ms                                                                | 114 ms: 1.09x slower                                              |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241021-arminc-aarch64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 249 ms: 1.02x faster                                              |
| regex_effbot   | 4.64 ms                                                               | 5.06 ms: 1.09x slower                                             |
| regex_v8       | 28.3 ms                                                               | 31.2 ms: 1.10x slower                                             |
| regex_compile  | 137 ms                                                                | 172 ms: 1.25x slower                                              |
| Geometric mean | (ref)                                                                 | 1.10x slower                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241021-arminc-aarch64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 189 ms: 1.03x faster                                              |
| xml_etree_iterparse  | 150 ms                                                                | 149 ms: 1.01x faster                                              |
| tomli_loads          | 2.59 sec                                                              | 2.62 sec: 1.01x slower                                            |
| unpickle_pure_python | 260 us                                                                | 266 us: 1.02x slower                                              |
| xml_etree_process    | 79.0 ms                                                               | 81.5 ms: 1.03x slower                                             |
| json_loads           | 30.7 us                                                               | 31.8 us: 1.04x slower                                             |
| pickle_pure_python   | 365 us                                                                | 389 us: 1.07x slower                                              |
| json_dumps           | 12.3 ms                                                               | 14.2 ms: 1.16x slower                                             |
| Geometric mean       | (ref)                                                                 | 1.03x slower                                                      |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241021-arminc-aarch64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.78 ms: 1.05x slower                                             |
| python_startup         | 11.4 ms                                                               | 14.6 ms: 1.28x slower                                             |
| Geometric mean         | (ref)                                                                 | 1.16x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241021-arminc-aarch64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.2 ms: 1.02x slower                                             |
| genshi_text     | 27.4 ms                                                               | 34.9 ms: 1.27x slower                                             |
| django_template | 40.7 ms                                                               | 52.3 ms: 1.28x slower                                             |
| genshi_xml      | 60.6 ms                                                               | 82.5 ms: 1.36x slower                                             |
| Geometric mean  | (ref)                                                                 | 1.23x slower                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241021-arminc-aarch64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 547 ms: 1.35x faster                                              |
| async_tree_none            | 624 ms                                                                | 473 ms: 1.32x faster                                              |
| async_tree_memoization     | 777 ms                                                                | 607 ms: 1.28x faster                                              |
| async_tree_none_tg         | 577 ms                                                                | 453 ms: 1.27x faster                                              |
| deepcopy_memo              | 49.6 us                                                               | 39.2 us: 1.26x faster                                             |
| async_tree_io              | 1.41 sec                                                              | 1.17 sec: 1.21x faster                                            |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 760 ms: 1.20x faster                                              |
| deepcopy                   | 446 us                                                                | 374 us: 1.19x faster                                              |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 744 ms: 1.19x faster                                              |
| pathlib                    | 24.5 ms                                                               | 21.8 ms: 1.13x faster                                             |
| async_tree_io_tg           | 1.40 sec                                                              | 1.27 sec: 1.11x faster                                            |
| deepcopy_reduce            | 4.10 us                                                               | 3.87 us: 1.06x faster                                             |
| xml_etree_parse            | 195 ms                                                                | 189 ms: 1.03x faster                                              |
| comprehensions             | 25.4 us                                                               | 24.7 us: 1.03x faster                                             |
| regex_dna                  | 254 ms                                                                | 249 ms: 1.02x faster                                              |
| xml_etree_iterparse        | 150 ms                                                                | 149 ms: 1.01x faster                                              |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                              |
| tomli_loads                | 2.59 sec                                                              | 2.62 sec: 1.01x slower                                            |
| mdp                        | 3.41 sec                                                              | 3.48 sec: 1.02x slower                                            |
| json                       | 5.54 ms                                                               | 5.66 ms: 1.02x slower                                             |
| unpickle_pure_python       | 260 us                                                                | 266 us: 1.02x slower                                              |
| mako                       | 12.9 ms                                                               | 13.2 ms: 1.02x slower                                             |
| crypto_pyaes               | 86.6 ms                                                               | 89.3 ms: 1.03x slower                                             |
| xml_etree_process          | 79.0 ms                                                               | 81.5 ms: 1.03x slower                                             |
| json_loads                 | 30.7 us                                                               | 31.8 us: 1.04x slower                                             |
| scimark_lu                 | 146 ms                                                                | 151 ms: 1.04x slower                                              |
| thrift                     | 937 us                                                                | 974 us: 1.04x slower                                              |
| async_generators           | 491 ms                                                                | 511 ms: 1.04x slower                                              |
| logging_silent             | 127 ns                                                                | 133 ns: 1.05x slower                                              |
| python_startup_no_site     | 8.37 ms                                                               | 8.78 ms: 1.05x slower                                             |
| bench_thread_pool          | 1.31 ms                                                               | 1.38 ms: 1.05x slower                                             |
| float                      | 92.1 ms                                                               | 97.7 ms: 1.06x slower                                             |
| scimark_sor                | 150 ms                                                                | 159 ms: 1.06x slower                                              |
| scimark_monte_carlo        | 85.1 ms                                                               | 90.6 ms: 1.07x slower                                             |
| pickle_pure_python         | 365 us                                                                | 389 us: 1.07x slower                                              |
| scimark_fft                | 418 ms                                                                | 454 ms: 1.09x slower                                              |
| regex_effbot               | 4.64 ms                                                               | 5.06 ms: 1.09x slower                                             |
| nbody                      | 105 ms                                                                | 114 ms: 1.09x slower                                              |
| regex_v8                   | 28.3 ms                                                               | 31.2 ms: 1.10x slower                                             |
| meteor_contest             | 112 ms                                                                | 123 ms: 1.10x slower                                              |
| pyflate                    | 559 ms                                                                | 616 ms: 1.10x slower                                              |
| tornado_http               | 136 ms                                                                | 150 ms: 1.10x slower                                              |
| html5lib                   | 65.1 ms                                                               | 72.7 ms: 1.12x slower                                             |
| telco                      | 8.51 ms                                                               | 9.56 ms: 1.12x slower                                             |
| deltablue                  | 4.12 ms                                                               | 4.66 ms: 1.13x slower                                             |
| coverage                   | 87.3 ms                                                               | 99.0 ms: 1.13x slower                                             |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.13 ms: 1.15x slower                                             |
| richards_super             | 58.5 ms                                                               | 67.5 ms: 1.15x slower                                             |
| fannkuch                   | 443 ms                                                                | 515 ms: 1.16x slower                                              |
| json_dumps                 | 12.3 ms                                                               | 14.2 ms: 1.16x slower                                             |
| typing_runtime_protocols   | 181 us                                                                | 212 us: 1.18x slower                                              |
| spectral_norm              | 131 ms                                                                | 154 ms: 1.18x slower                                              |
| sqlglot_transpile          | 1.83 ms                                                               | 2.16 ms: 1.18x slower                                             |
| sqlglot_parse              | 1.46 ms                                                               | 1.73 ms: 1.18x slower                                             |
| pycparser                  | 1.26 sec                                                              | 1.49 sec: 1.19x slower                                            |
| docutils                   | 2.98 sec                                                              | 3.55 sec: 1.19x slower                                            |
| go                         | 157 ms                                                                | 188 ms: 1.19x slower                                              |
| richards                   | 50.9 ms                                                               | 61.1 ms: 1.20x slower                                             |
| sqlglot_normalize          | 126 ms                                                                | 153 ms: 1.21x slower                                              |
| chaos                      | 71.4 ms                                                               | 86.8 ms: 1.22x slower                                             |
| 2to3                       | 308 ms                                                                | 375 ms: 1.22x slower                                              |
| regex_compile              | 137 ms                                                                | 172 ms: 1.25x slower                                              |
| dulwich_log                | 62.0 ms                                                               | 78.1 ms: 1.26x slower                                             |
| sympy_str                  | 280 ms                                                                | 353 ms: 1.26x slower                                              |
| genshi_text                | 27.4 ms                                                               | 34.9 ms: 1.27x slower                                             |
| python_startup             | 11.4 ms                                                               | 14.6 ms: 1.28x slower                                             |
| django_template            | 40.7 ms                                                               | 52.3 ms: 1.28x slower                                             |
| nqueens                    | 99.2 ms                                                               | 128 ms: 1.29x slower                                              |
| pylint                     | 355 ms                                                                | 458 ms: 1.29x slower                                              |
| sympy_expand               | 454 ms                                                                | 588 ms: 1.30x slower                                              |
| sqlglot_optimize           | 61.3 ms                                                               | 79.9 ms: 1.30x slower                                             |
| pprint_safe_repr           | 916 ms                                                                | 1.20 sec: 1.31x slower                                            |
| pprint_pformat             | 1.88 sec                                                              | 2.55 sec: 1.36x slower                                            |
| genshi_xml                 | 60.6 ms                                                               | 82.5 ms: 1.36x slower                                             |
| sympy_integrate            | 21.6 ms                                                               | 29.7 ms: 1.37x slower                                             |
| generators                 | 43.5 ms                                                               | 60.0 ms: 1.38x slower                                             |
| sympy_sum                  | 154 ms                                                                | 214 ms: 1.38x slower                                              |
| gc_traversal               | 4.40 ms                                                               | 6.37 ms: 1.45x slower                                             |
| hexiom                     | 6.98 ms                                                               | 10.1 ms: 1.45x slower                                             |
| create_gc_cycles           | 1.92 ms                                                               | 3.62 ms: 1.89x slower                                             |
| bench_mp_pool              | 7.05 ms                                                               | 2.50 sec: 353.84x slower                                          |
| Geometric mean             | (ref)                                                                 | 1.17x slower                                                      |

Benchmark hidden because not significant (6): coroutines, logging_format, raytrace, logging_simple, xml_etree_generate, asyncio_websockets
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (2) of results/bm-20241021-3.14.0a1+-0be1ef3-JIT/bm-20241021-arminc-aarch64-nick%2darm-codecache-3.14.0a1+-0be1ef3.json: bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.083x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.13x