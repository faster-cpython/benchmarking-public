# Results vs. 3.12.0

- fork: python
- ref: 9d08423b6e0fa89ce9cf
- machine: linux-aarch64
- commit hash: 9d08423
- commit date: 2024-11-09
- overall geometric mean: 1.370x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.41x slower
- Memory change: 1.24x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 538 ms: 1.75x slower                                                     |
| docutils       | 2.98 sec                                                              | 4.28 sec: 1.43x slower                                                   |
| html5lib       | 65.1 ms                                                               | 123 ms: 1.89x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.68x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 1.44 sec: 1.02x slower                                                   |
| async_tree_io              | 1.41 sec                                                              | 1.47 sec: 1.04x slower                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 951 ms: 1.04x slower                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 925 ms: 1.05x slower                                                     |
| async_tree_none_tg         | 577 ms                                                                | 614 ms: 1.06x slower                                                     |
| Geometric mean             | (ref)                                                                 | 1.03x slower                                                             |

Benchmark hidden because not significant (3): async_tree_memoization, async_tree_none, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 213 ms: 2.32x slower                                                     |
| nbody          | 105 ms                                                                | 280 ms: 2.67x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.86x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 271 ms: 1.07x slower                                                     |
| regex_v8       | 28.3 ms                                                               | 35.4 ms: 1.25x slower                                                    |
| regex_compile  | 137 ms                                                                | 256 ms: 1.86x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.26x slower                                                             |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 187 ms: 1.04x faster                                                     |
| xml_etree_iterparse  | 150 ms                                                                | 158 ms: 1.05x slower                                                     |
| json_loads           | 30.7 us                                                               | 39.2 us: 1.28x slower                                                    |
| xml_etree_generate   | 112 ms                                                                | 164 ms: 1.46x slower                                                     |
| tomli_loads          | 2.59 sec                                                              | 4.28 sec: 1.65x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 20.2 ms: 1.65x slower                                                    |
| xml_etree_process    | 79.0 ms                                                               | 133 ms: 1.68x slower                                                     |
| unpickle_pure_python | 260 us                                                                | 567 us: 2.18x slower                                                     |
| pickle_pure_python   | 365 us                                                                | 842 us: 2.31x slower                                                     |
| Geometric mean       | (ref)                                                                 | 1.52x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 12.5 ms: 1.50x slower                                                    |
| python_startup         | 11.4 ms                                                               | 21.1 ms: 1.85x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.67x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 104 ms: 1.71x slower                                                     |
| django_template | 40.7 ms                                                               | 83.8 ms: 2.06x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 56.6 ms: 2.06x slower                                                    |
| mako            | 12.9 ms                                                               | 29.3 ms: 2.27x slower                                                    |
| Geometric mean  | (ref)                                                                 | 2.02x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse            | 195 ms                                                                | 187 ms: 1.04x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 1.44 sec: 1.02x slower                                                   |
| async_tree_io              | 1.41 sec                                                              | 1.47 sec: 1.04x slower                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 951 ms: 1.04x slower                                                     |
| asyncio_websockets         | 658 ms                                                                | 687 ms: 1.05x slower                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 925 ms: 1.05x slower                                                     |
| xml_etree_iterparse        | 150 ms                                                                | 158 ms: 1.05x slower                                                     |
| async_tree_none_tg         | 577 ms                                                                | 614 ms: 1.06x slower                                                     |
| regex_dna                  | 254 ms                                                                | 271 ms: 1.07x slower                                                     |
| sqlite_synth               | 3.77 us                                                               | 4.27 us: 1.13x slower                                                    |
| pathlib                    | 24.5 ms                                                               | 28.4 ms: 1.16x slower                                                    |
| deepcopy                   | 446 us                                                                | 547 us: 1.23x slower                                                     |
| regex_v8                   | 28.3 ms                                                               | 35.4 ms: 1.25x slower                                                    |
| json                       | 5.54 ms                                                               | 7.01 ms: 1.27x slower                                                    |
| json_loads                 | 30.7 us                                                               | 39.2 us: 1.28x slower                                                    |
| scimark_fft                | 418 ms                                                                | 549 ms: 1.31x slower                                                     |
| mdp                        | 3.41 sec                                                              | 4.52 sec: 1.32x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.65 ms: 1.38x slower                                                    |
| coroutines                 | 29.0 ms                                                               | 40.6 ms: 1.40x slower                                                    |
| deepcopy_memo              | 49.6 us                                                               | 70.6 us: 1.42x slower                                                    |
| generators                 | 43.5 ms                                                               | 62.3 ms: 1.43x slower                                                    |
| async_generators           | 491 ms                                                                | 703 ms: 1.43x slower                                                     |
| docutils                   | 2.98 sec                                                              | 4.28 sec: 1.43x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 8.93 ms: 1.44x slower                                                    |
| xml_etree_generate         | 112 ms                                                                | 164 ms: 1.46x slower                                                     |
| pylint                     | 355 ms                                                                | 523 ms: 1.47x slower                                                     |
| deepcopy_reduce            | 4.10 us                                                               | 6.08 us: 1.48x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 12.5 ms: 1.50x slower                                                    |
| telco                      | 8.51 ms                                                               | 13.0 ms: 1.53x slower                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 2.07 ms: 1.58x slower                                                    |
| meteor_contest             | 112 ms                                                                | 177 ms: 1.58x slower                                                     |
| nqueens                    | 99.2 ms                                                               | 159 ms: 1.60x slower                                                     |
| coverage                   | 87.3 ms                                                               | 142 ms: 1.63x slower                                                     |
| dulwich_log                | 62.0 ms                                                               | 102 ms: 1.65x slower                                                     |
| tomli_loads                | 2.59 sec                                                              | 4.28 sec: 1.65x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 20.2 ms: 1.65x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 144 ms: 1.66x slower                                                     |
| spectral_norm              | 131 ms                                                                | 219 ms: 1.67x slower                                                     |
| sympy_integrate            | 21.6 ms                                                               | 36.3 ms: 1.68x slower                                                    |
| xml_etree_process          | 79.0 ms                                                               | 133 ms: 1.68x slower                                                     |
| comprehensions             | 25.4 us                                                               | 42.8 us: 1.69x slower                                                    |
| fannkuch                   | 443 ms                                                                | 751 ms: 1.69x slower                                                     |
| pycparser                  | 1.26 sec                                                              | 2.14 sec: 1.70x slower                                                   |
| genshi_xml                 | 60.6 ms                                                               | 104 ms: 1.71x slower                                                     |
| sqlalchemy_declarative     | 157 ms                                                                | 273 ms: 1.73x slower                                                     |
| 2to3                       | 308 ms                                                                | 538 ms: 1.75x slower                                                     |
| thrift                     | 937 us                                                                | 1.72 ms: 1.84x slower                                                    |
| pyflate                    | 559 ms                                                                | 1.03 sec: 1.85x slower                                                   |
| python_startup             | 11.4 ms                                                               | 21.1 ms: 1.85x slower                                                    |
| regex_compile              | 137 ms                                                                | 256 ms: 1.86x slower                                                     |
| sqlglot_normalize          | 126 ms                                                                | 236 ms: 1.88x slower                                                     |
| sqlglot_optimize           | 61.3 ms                                                               | 115 ms: 1.88x slower                                                     |
| html5lib                   | 65.1 ms                                                               | 123 ms: 1.89x slower                                                     |
| sympy_str                  | 280 ms                                                                | 532 ms: 1.90x slower                                                     |
| pprint_safe_repr           | 916 ms                                                                | 1.76 sec: 1.92x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 3.61 sec: 1.92x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 348 us: 1.93x slower                                                     |
| sqlalchemy_imperative      | 16.7 ms                                                               | 32.2 ms: 1.93x slower                                                    |
| logging_simple             | 7.63 us                                                               | 15.0 us: 1.97x slower                                                    |
| logging_format             | 8.34 us                                                               | 16.5 us: 1.98x slower                                                    |
| django_template            | 40.7 ms                                                               | 83.8 ms: 2.06x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 56.6 ms: 2.06x slower                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 177 ms: 2.08x slower                                                     |
| sympy_sum                  | 154 ms                                                                | 329 ms: 2.13x slower                                                     |
| sympy_expand               | 454 ms                                                                | 988 ms: 2.18x slower                                                     |
| unpickle_pure_python       | 260 us                                                                | 567 us: 2.18x slower                                                     |
| chaos                      | 71.4 ms                                                               | 159 ms: 2.23x slower                                                     |
| mako                       | 12.9 ms                                                               | 29.3 ms: 2.27x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 16.0 ms: 2.30x slower                                                    |
| logging_silent             | 127 ns                                                                | 292 ns: 2.30x slower                                                     |
| pickle_pure_python         | 365 us                                                                | 842 us: 2.31x slower                                                     |
| scimark_sor                | 150 ms                                                                | 346 ms: 2.31x slower                                                     |
| float                      | 92.1 ms                                                               | 213 ms: 2.32x slower                                                     |
| raytrace                   | 353 ms                                                                | 835 ms: 2.36x slower                                                     |
| richards                   | 50.9 ms                                                               | 121 ms: 2.37x slower                                                     |
| scimark_lu                 | 146 ms                                                                | 346 ms: 2.38x slower                                                     |
| sqlglot_transpile          | 1.83 ms                                                               | 4.49 ms: 2.45x slower                                                    |
| richards_super             | 58.5 ms                                                               | 147 ms: 2.51x slower                                                     |
| go                         | 157 ms                                                                | 402 ms: 2.56x slower                                                     |
| sqlglot_parse              | 1.46 ms                                                               | 3.81 ms: 2.61x slower                                                    |
| nbody                      | 105 ms                                                                | 280 ms: 2.67x slower                                                     |
| deltablue                  | 4.12 ms                                                               | 13.4 ms: 3.25x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 63.5 ms: 9.01x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.66x slower                                                             |

Benchmark hidden because not significant (6): async_tree_memoization, async_tree_none, gc_traversal, async_tree_memoization_tg, regex_effbot, pidigits
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20241109-3.14.0a1+-9d08423-NOGIL/bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json: bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.370x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.49x
- 95% likely to have a slowdown of 1.47x
- 99% likely to have a slowdown of 1.41x

# Memory
- memory change: 1.24x