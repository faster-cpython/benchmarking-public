# Results vs. 3.12.0

- fork: savannahostrowski
- ref: remove_ghccc
- machine: linux-aarch64
- commit hash: 9827ade
- commit date: 2024-10-16
- overall geometric mean: 1.060x slower
- HPT reliability: 99.92%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 373 ms: 1.21x slower                                                        |
| docutils       | 2.98 sec                                                              | 3.66 sec: 1.23x slower                                                      |
| html5lib       | 65.1 ms                                                               | 71.4 ms: 1.10x slower                                                       |
| tornado_http   | 136 ms                                                                | 150 ms: 1.10x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.16x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 458 ms: 1.36x faster                                                        |
| async_tree_memoization_tg  | 740 ms                                                                | 549 ms: 1.35x faster                                                        |
| async_tree_none_tg         | 577 ms                                                                | 448 ms: 1.29x faster                                                        |
| async_tree_memoization     | 777 ms                                                                | 605 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 760 ms: 1.20x faster                                                        |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 744 ms: 1.19x faster                                                        |
| async_tree_io              | 1.41 sec                                                              | 1.19 sec: 1.19x faster                                                      |
| async_tree_io_tg           | 1.40 sec                                                              | 1.25 sec: 1.12x faster                                                      |
| Geometric mean             | (ref)                                                                 | 1.24x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                        |
| nbody          | 105 ms                                                                | 108 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 245 ms: 1.04x faster                                                        |
| regex_effbot   | 4.64 ms                                                               | 4.89 ms: 1.05x slower                                                       |
| regex_v8       | 28.3 ms                                                               | 31.8 ms: 1.12x slower                                                       |
| regex_compile  | 137 ms                                                                | 165 ms: 1.20x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.08x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.59 sec                                                              | 2.49 sec: 1.04x faster                                                      |
| xml_etree_generate   | 112 ms                                                                | 109 ms: 1.03x faster                                                        |
| xml_etree_process    | 79.0 ms                                                               | 78.0 ms: 1.01x faster                                                       |
| pickle_list          | 5.25 us                                                               | 5.19 us: 1.01x faster                                                       |
| pickle_dict          | 37.3 us                                                               | 37.7 us: 1.01x slower                                                       |
| unpickle_pure_python | 260 us                                                                | 264 us: 1.02x slower                                                        |
| json_loads           | 30.7 us                                                               | 31.5 us: 1.03x slower                                                       |
| pickle               | 13.4 us                                                               | 13.8 us: 1.03x slower                                                       |
| pickle_pure_python   | 365 us                                                                | 377 us: 1.03x slower                                                        |
| unpickle             | 18.5 us                                                               | 19.2 us: 1.04x slower                                                       |
| unpickle_list        | 6.17 us                                                               | 6.66 us: 1.08x slower                                                       |
| json_dumps           | 12.3 ms                                                               | 14.3 ms: 1.17x slower                                                       |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                                                |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.83 ms: 1.05x slower                                                       |
| python_startup         | 11.4 ms                                                               | 14.8 ms: 1.31x slower                                                       |
| Geometric mean         | (ref)                                                                 | 1.17x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 12.8 ms: 1.01x faster                                                       |
| genshi_text     | 27.4 ms                                                               | 32.2 ms: 1.18x slower                                                       |
| django_template | 40.7 ms                                                               | 49.0 ms: 1.21x slower                                                       |
| genshi_xml      | 60.6 ms                                                               | 78.6 ms: 1.30x slower                                                       |
| Geometric mean  | (ref)                                                                 | 1.16x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 458 ms: 1.36x faster                                                        |
| async_tree_memoization_tg  | 740 ms                                                                | 549 ms: 1.35x faster                                                        |
| deepcopy_memo              | 49.6 us                                                               | 38.1 us: 1.30x faster                                                       |
| async_tree_none_tg         | 577 ms                                                                | 448 ms: 1.29x faster                                                        |
| async_tree_memoization     | 777 ms                                                                | 605 ms: 1.28x faster                                                        |
| deepcopy                   | 446 us                                                                | 366 us: 1.22x faster                                                        |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 760 ms: 1.20x faster                                                        |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 744 ms: 1.19x faster                                                        |
| async_tree_io              | 1.41 sec                                                              | 1.19 sec: 1.19x faster                                                      |
| async_tree_io_tg           | 1.40 sec                                                              | 1.25 sec: 1.12x faster                                                      |
| comprehensions             | 25.4 us                                                               | 23.3 us: 1.09x faster                                                       |
| pathlib                    | 24.5 ms                                                               | 22.6 ms: 1.09x faster                                                       |
| deepcopy_reduce            | 4.10 us                                                               | 3.78 us: 1.08x faster                                                       |
| crypto_pyaes               | 86.6 ms                                                               | 83.0 ms: 1.04x faster                                                       |
| tomli_loads                | 2.59 sec                                                              | 2.49 sec: 1.04x faster                                                      |
| logging_simple             | 7.63 us                                                               | 7.35 us: 1.04x faster                                                       |
| logging_format             | 8.34 us                                                               | 8.04 us: 1.04x faster                                                       |
| regex_dna                  | 254 ms                                                                | 245 ms: 1.04x faster                                                        |
| xml_etree_generate         | 112 ms                                                                | 109 ms: 1.03x faster                                                        |
| xml_etree_process          | 79.0 ms                                                               | 78.0 ms: 1.01x faster                                                       |
| pickle_list                | 5.25 us                                                               | 5.19 us: 1.01x faster                                                       |
| mako                       | 12.9 ms                                                               | 12.8 ms: 1.01x faster                                                       |
| json                       | 5.54 ms                                                               | 5.48 ms: 1.01x faster                                                       |
| raytrace                   | 353 ms                                                                | 350 ms: 1.01x faster                                                        |
| deltablue                  | 4.12 ms                                                               | 4.15 ms: 1.01x slower                                                       |
| pickle_dict                | 37.3 us                                                               | 37.7 us: 1.01x slower                                                       |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                        |
| scimark_fft                | 418 ms                                                                | 424 ms: 1.01x slower                                                        |
| mdp                        | 3.41 sec                                                              | 3.46 sec: 1.01x slower                                                      |
| scimark_monte_carlo        | 85.1 ms                                                               | 86.4 ms: 1.02x slower                                                       |
| unpickle_pure_python       | 260 us                                                                | 264 us: 1.02x slower                                                        |
| scimark_lu                 | 146 ms                                                                | 148 ms: 1.02x slower                                                        |
| json_loads                 | 30.7 us                                                               | 31.5 us: 1.03x slower                                                       |
| pickle                     | 13.4 us                                                               | 13.8 us: 1.03x slower                                                       |
| logging_silent             | 127 ns                                                                | 131 ns: 1.03x slower                                                        |
| nbody                      | 105 ms                                                                | 108 ms: 1.03x slower                                                        |
| pickle_pure_python         | 365 us                                                                | 377 us: 1.03x slower                                                        |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.26 sec: 1.03x slower                                                      |
| async_generators           | 491 ms                                                                | 508 ms: 1.04x slower                                                        |
| pyflate                    | 559 ms                                                                | 581 ms: 1.04x slower                                                        |
| unpickle                   | 18.5 us                                                               | 19.2 us: 1.04x slower                                                       |
| thrift                     | 937 us                                                                | 977 us: 1.04x slower                                                        |
| fannkuch                   | 443 ms                                                                | 463 ms: 1.04x slower                                                        |
| bench_thread_pool          | 1.31 ms                                                               | 1.37 ms: 1.05x slower                                                       |
| regex_effbot               | 4.64 ms                                                               | 4.89 ms: 1.05x slower                                                       |
| python_startup_no_site     | 8.37 ms                                                               | 8.83 ms: 1.05x slower                                                       |
| scimark_sor                | 150 ms                                                                | 159 ms: 1.07x slower                                                        |
| meteor_contest             | 112 ms                                                                | 120 ms: 1.07x slower                                                        |
| unpickle_list              | 6.17 us                                                               | 6.66 us: 1.08x slower                                                       |
| sqlglot_parse              | 1.46 ms                                                               | 1.59 ms: 1.09x slower                                                       |
| asyncio_tcp                | 566 ms                                                                | 618 ms: 1.09x slower                                                        |
| html5lib                   | 65.1 ms                                                               | 71.4 ms: 1.10x slower                                                       |
| chaos                      | 71.4 ms                                                               | 78.8 ms: 1.10x slower                                                       |
| tornado_http               | 136 ms                                                                | 150 ms: 1.10x slower                                                        |
| generators                 | 43.5 ms                                                               | 48.3 ms: 1.11x slower                                                       |
| spectral_norm              | 131 ms                                                                | 146 ms: 1.12x slower                                                        |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.94 ms: 1.12x slower                                                       |
| regex_v8                   | 28.3 ms                                                               | 31.8 ms: 1.12x slower                                                       |
| telco                      | 8.51 ms                                                               | 9.57 ms: 1.13x slower                                                       |
| coverage                   | 87.3 ms                                                               | 98.5 ms: 1.13x slower                                                       |
| go                         | 157 ms                                                                | 179 ms: 1.14x slower                                                        |
| sqlglot_transpile          | 1.83 ms                                                               | 2.10 ms: 1.15x slower                                                       |
| pycparser                  | 1.26 sec                                                              | 1.45 sec: 1.15x slower                                                      |
| richards_super             | 58.5 ms                                                               | 67.9 ms: 1.16x slower                                                       |
| typing_runtime_protocols   | 181 us                                                                | 210 us: 1.16x slower                                                        |
| json_dumps                 | 12.3 ms                                                               | 14.3 ms: 1.17x slower                                                       |
| genshi_text                | 27.4 ms                                                               | 32.2 ms: 1.18x slower                                                       |
| nqueens                    | 99.2 ms                                                               | 117 ms: 1.18x slower                                                        |
| richards                   | 50.9 ms                                                               | 60.9 ms: 1.19x slower                                                       |
| sqlglot_normalize          | 126 ms                                                                | 151 ms: 1.20x slower                                                        |
| regex_compile              | 137 ms                                                                | 165 ms: 1.20x slower                                                        |
| django_template            | 40.7 ms                                                               | 49.0 ms: 1.21x slower                                                       |
| 2to3                       | 308 ms                                                                | 373 ms: 1.21x slower                                                        |
| docutils                   | 2.98 sec                                                              | 3.66 sec: 1.23x slower                                                      |
| sympy_str                  | 280 ms                                                                | 347 ms: 1.24x slower                                                        |
| pprint_safe_repr           | 916 ms                                                                | 1.17 sec: 1.27x slower                                                      |
| sympy_expand               | 454 ms                                                                | 580 ms: 1.28x slower                                                        |
| pprint_pformat             | 1.88 sec                                                              | 2.42 sec: 1.29x slower                                                      |
| sqlglot_optimize           | 61.3 ms                                                               | 79.3 ms: 1.29x slower                                                       |
| genshi_xml                 | 60.6 ms                                                               | 78.6 ms: 1.30x slower                                                       |
| dulwich_log                | 62.0 ms                                                               | 80.8 ms: 1.30x slower                                                       |
| python_startup             | 11.4 ms                                                               | 14.8 ms: 1.31x slower                                                       |
| sympy_integrate            | 21.6 ms                                                               | 29.1 ms: 1.34x slower                                                       |
| hexiom                     | 6.98 ms                                                               | 9.54 ms: 1.37x slower                                                       |
| sympy_sum                  | 154 ms                                                                | 211 ms: 1.37x slower                                                        |
| pylint                     | 355 ms                                                                | 486 ms: 1.37x slower                                                        |
| gc_traversal               | 4.40 ms                                                               | 6.34 ms: 1.44x slower                                                       |
| create_gc_cycles           | 1.92 ms                                                               | 3.73 ms: 1.94x slower                                                       |
| bench_mp_pool              | 7.05 ms                                                               | 2.16 sec: 306.40x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.13x slower                                                                |

Benchmark hidden because not significant (6): xml_etree_parse, coroutines, xml_etree_iterparse, float, asyncio_websockets, sqlite_synth
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (3) of results/bm-20241016-3.14.0a1+-9827ade-JIT/bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade.json: bpe_tokeniser, sphinx, unpack_sequence

- Geometric mean (including insignificant results): 1.060x slower
# HPT report

- Reliability score: 99.92% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.09x