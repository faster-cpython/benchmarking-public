# Results vs. 3.12.0

- fork: python
- ref: ded105a62b9d78717f8d
- machine: linux-aarch64
- commit hash: ded105a
- commit date: 2024-10-21
- overall geometric mean: 1.089x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 385 ms: 1.25x slower                                                     |
| docutils       | 2.98 sec                                                              | 3.64 sec: 1.22x slower                                                   |
| html5lib       | 65.1 ms                                                               | 72.4 ms: 1.11x slower                                                    |
| tornado_http   | 136 ms                                                                | 148 ms: 1.09x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.17x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 543 ms: 1.36x faster                                                     |
| async_tree_none            | 624 ms                                                                | 475 ms: 1.31x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 449 ms: 1.28x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 607 ms: 1.28x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 765 ms: 1.19x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 1.18 sec: 1.19x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 748 ms: 1.18x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 1.25 sec: 1.12x faster                                                   |
| Geometric mean             | (ref)                                                                 | 1.24x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                     |
| float          | 92.1 ms                                                               | 96.8 ms: 1.05x slower                                                    |
| nbody          | 105 ms                                                                | 114 ms: 1.09x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.94 ms: 1.06x slower                                                    |
| regex_v8       | 28.3 ms                                                               | 31.0 ms: 1.09x slower                                                    |
| regex_compile  | 137 ms                                                                | 177 ms: 1.29x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.11x slower                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 187 ms: 1.05x faster                                                     |
| tomli_loads          | 2.59 sec                                                              | 2.62 sec: 1.01x slower                                                   |
| xml_etree_process    | 79.0 ms                                                               | 80.9 ms: 1.02x slower                                                    |
| json_loads           | 30.7 us                                                               | 31.8 us: 1.04x slower                                                    |
| unpickle_pure_python | 260 us                                                                | 272 us: 1.05x slower                                                     |
| pickle_pure_python   | 365 us                                                                | 390 us: 1.07x slower                                                     |
| json_dumps           | 12.3 ms                                                               | 14.4 ms: 1.17x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.04x slower                                                             |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.70 ms: 1.04x slower                                                    |
| python_startup         | 11.4 ms                                                               | 14.5 ms: 1.28x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.15x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.2 ms: 1.02x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 34.9 ms: 1.27x slower                                                    |
| django_template | 40.7 ms                                                               | 53.3 ms: 1.31x slower                                                    |
| genshi_xml      | 60.6 ms                                                               | 85.7 ms: 1.41x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.25x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 543 ms: 1.36x faster                                                     |
| async_tree_none            | 624 ms                                                                | 475 ms: 1.31x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 449 ms: 1.28x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 607 ms: 1.28x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 39.0 us: 1.27x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 765 ms: 1.19x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 1.18 sec: 1.19x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 748 ms: 1.18x faster                                                     |
| deepcopy                   | 446 us                                                                | 382 us: 1.17x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 1.25 sec: 1.12x faster                                                   |
| pathlib                    | 24.5 ms                                                               | 21.9 ms: 1.12x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 187 ms: 1.05x faster                                                     |
| logging_format             | 8.34 us                                                               | 8.22 us: 1.02x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.62 sec: 1.01x slower                                                   |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                     |
| mako                       | 12.9 ms                                                               | 13.2 ms: 1.02x slower                                                    |
| mdp                        | 3.41 sec                                                              | 3.49 sec: 1.02x slower                                                   |
| xml_etree_process          | 79.0 ms                                                               | 80.9 ms: 1.02x slower                                                    |
| thrift                     | 937 us                                                                | 964 us: 1.03x slower                                                     |
| scimark_lu                 | 146 ms                                                                | 151 ms: 1.03x slower                                                     |
| json_loads                 | 30.7 us                                                               | 31.8 us: 1.04x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 90.0 ms: 1.04x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 8.70 ms: 1.04x slower                                                    |
| async_generators           | 491 ms                                                                | 511 ms: 1.04x slower                                                     |
| scimark_sor                | 150 ms                                                                | 156 ms: 1.04x slower                                                     |
| bench_thread_pool          | 1.31 ms                                                               | 1.36 ms: 1.04x slower                                                    |
| json                       | 5.54 ms                                                               | 5.78 ms: 1.04x slower                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 89.1 ms: 1.05x slower                                                    |
| unpickle_pure_python       | 260 us                                                                | 272 us: 1.05x slower                                                     |
| float                      | 92.1 ms                                                               | 96.8 ms: 1.05x slower                                                    |
| logging_silent             | 127 ns                                                                | 134 ns: 1.05x slower                                                     |
| regex_effbot               | 4.64 ms                                                               | 4.94 ms: 1.06x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 390 us: 1.07x slower                                                     |
| scimark_fft                | 418 ms                                                                | 453 ms: 1.08x slower                                                     |
| tornado_http               | 136 ms                                                                | 148 ms: 1.09x slower                                                     |
| nbody                      | 105 ms                                                                | 114 ms: 1.09x slower                                                     |
| regex_v8                   | 28.3 ms                                                               | 31.0 ms: 1.09x slower                                                    |
| deltablue                  | 4.12 ms                                                               | 4.53 ms: 1.10x slower                                                    |
| meteor_contest             | 112 ms                                                                | 123 ms: 1.10x slower                                                     |
| html5lib                   | 65.1 ms                                                               | 72.4 ms: 1.11x slower                                                    |
| telco                      | 8.51 ms                                                               | 9.63 ms: 1.13x slower                                                    |
| pyflate                    | 559 ms                                                                | 638 ms: 1.14x slower                                                     |
| coverage                   | 87.3 ms                                                               | 101 ms: 1.16x slower                                                     |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.18 ms: 1.16x slower                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.70 ms: 1.16x slower                                                    |
| fannkuch                   | 443 ms                                                                | 519 ms: 1.17x slower                                                     |
| richards_super             | 58.5 ms                                                               | 68.5 ms: 1.17x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 14.4 ms: 1.17x slower                                                    |
| go                         | 157 ms                                                                | 185 ms: 1.18x slower                                                     |
| typing_runtime_protocols   | 181 us                                                                | 214 us: 1.19x slower                                                     |
| spectral_norm              | 131 ms                                                                | 155 ms: 1.19x slower                                                     |
| chaos                      | 71.4 ms                                                               | 85.0 ms: 1.19x slower                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 2.19 ms: 1.20x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.64 sec: 1.22x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 1.53 sec: 1.22x slower                                                   |
| richards                   | 50.9 ms                                                               | 63.2 ms: 1.24x slower                                                    |
| sqlglot_normalize          | 126 ms                                                                | 157 ms: 1.25x slower                                                     |
| 2to3                       | 308 ms                                                                | 385 ms: 1.25x slower                                                     |
| genshi_text                | 27.4 ms                                                               | 34.9 ms: 1.27x slower                                                    |
| python_startup             | 11.4 ms                                                               | 14.5 ms: 1.28x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 127 ms: 1.28x slower                                                     |
| regex_compile              | 137 ms                                                                | 177 ms: 1.29x slower                                                     |
| sympy_str                  | 280 ms                                                                | 361 ms: 1.29x slower                                                     |
| django_template            | 40.7 ms                                                               | 53.3 ms: 1.31x slower                                                    |
| sympy_expand               | 454 ms                                                                | 595 ms: 1.31x slower                                                     |
| pprint_safe_repr           | 916 ms                                                                | 1.20 sec: 1.31x slower                                                   |
| dulwich_log                | 62.0 ms                                                               | 81.5 ms: 1.32x slower                                                    |
| pylint                     | 355 ms                                                                | 472 ms: 1.33x slower                                                     |
| pprint_pformat             | 1.88 sec                                                              | 2.51 sec: 1.33x slower                                                   |
| generators                 | 43.5 ms                                                               | 58.8 ms: 1.35x slower                                                    |
| sqlglot_optimize           | 61.3 ms                                                               | 83.1 ms: 1.36x slower                                                    |
| sympy_integrate            | 21.6 ms                                                               | 30.2 ms: 1.40x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 85.7 ms: 1.41x slower                                                    |
| sympy_sum                  | 154 ms                                                                | 219 ms: 1.42x slower                                                     |
| gc_traversal               | 4.40 ms                                                               | 6.34 ms: 1.44x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 10.4 ms: 1.49x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.61 ms: 1.88x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 2.71 sec: 384.69x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.18x slower                                                             |

Benchmark hidden because not significant (9): comprehensions, deepcopy_reduce, coroutines, raytrace, regex_dna, logging_simple, asyncio_websockets, xml_etree_generate, xml_etree_iterparse
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (2) of results/bm-20241021-3.14.0a1+-ded105a-JIT/bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a.json: bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.089x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.10x