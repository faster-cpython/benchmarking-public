# Results vs. 3.12.0

- fork: python
- ref: 7d7d56d8b1147a6b85e1
- machine: linux-aarch64
- commit hash: 7d7d56d
- commit date: 2024-11-02
- overall geometric mean: 1.370x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.40x slower
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 532 ms: 1.73x slower                                                     |
| docutils       | 2.98 sec                                                              | 4.17 sec: 1.40x slower                                                   |
| html5lib       | 65.1 ms                                                               | 120 ms: 1.84x slower                                                     |
| tornado_http   | 136 ms                                                                | 196 ms: 1.45x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.59x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io              | 1.41 sec                                                              | 1.46 sec: 1.04x slower                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 917 ms: 1.04x slower                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 950 ms: 1.04x slower                                                     |
| async_tree_none_tg         | 577 ms                                                                | 609 ms: 1.06x slower                                                     |
| Geometric mean             | (ref)                                                                 | 1.03x slower                                                             |

Benchmark hidden because not significant (4): async_tree_memoization, async_tree_io_tg, async_tree_none, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 242 ms: 1.04x slower                                                     |
| float          | 92.1 ms                                                               | 213 ms: 2.31x slower                                                     |
| nbody          | 105 ms                                                                | 295 ms: 2.82x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.89x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 268 ms: 1.05x slower                                                     |
| regex_v8       | 28.3 ms                                                               | 34.2 ms: 1.21x slower                                                    |
| regex_compile  | 137 ms                                                                | 260 ms: 1.89x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.25x slower                                                             |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_iterparse  | 150 ms                                                                | 157 ms: 1.04x slower                                                     |
| json_loads           | 30.7 us                                                               | 39.1 us: 1.27x slower                                                    |
| xml_etree_generate   | 112 ms                                                                | 170 ms: 1.52x slower                                                     |
| json_dumps           | 12.3 ms                                                               | 20.0 ms: 1.63x slower                                                    |
| tomli_loads          | 2.59 sec                                                              | 4.33 sec: 1.67x slower                                                   |
| xml_etree_process    | 79.0 ms                                                               | 135 ms: 1.71x slower                                                     |
| unpickle_pure_python | 260 us                                                                | 566 us: 2.18x slower                                                     |
| pickle_pure_python   | 365 us                                                                | 828 us: 2.27x slower                                                     |
| Geometric mean       | (ref)                                                                 | 1.53x slower                                                             |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 12.3 ms: 1.47x slower                                                    |
| python_startup         | 11.4 ms                                                               | 20.8 ms: 1.83x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.64x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 109 ms: 1.80x slower                                                     |
| genshi_text     | 27.4 ms                                                               | 54.0 ms: 1.97x slower                                                    |
| django_template | 40.7 ms                                                               | 85.1 ms: 2.09x slower                                                    |
| mako            | 12.9 ms                                                               | 29.7 ms: 2.30x slower                                                    |
| Geometric mean  | (ref)                                                                 | 2.03x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io              | 1.41 sec                                                              | 1.46 sec: 1.04x slower                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 917 ms: 1.04x slower                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 950 ms: 1.04x slower                                                     |
| pidigits                   | 233 ms                                                                | 242 ms: 1.04x slower                                                     |
| xml_etree_iterparse        | 150 ms                                                                | 157 ms: 1.04x slower                                                     |
| gc_traversal               | 4.40 ms                                                               | 4.59 ms: 1.04x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 693 ms: 1.05x slower                                                     |
| regex_dna                  | 254 ms                                                                | 268 ms: 1.05x slower                                                     |
| async_tree_none_tg         | 577 ms                                                                | 609 ms: 1.06x slower                                                     |
| sqlite_synth               | 3.77 us                                                               | 4.34 us: 1.15x slower                                                    |
| pathlib                    | 24.5 ms                                                               | 29.0 ms: 1.18x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 34.2 ms: 1.21x slower                                                    |
| deepcopy                   | 446 us                                                                | 551 us: 1.24x slower                                                     |
| json                       | 5.54 ms                                                               | 6.87 ms: 1.24x slower                                                    |
| json_loads                 | 30.7 us                                                               | 39.1 us: 1.27x slower                                                    |
| mdp                        | 3.41 sec                                                              | 4.48 sec: 1.31x slower                                                   |
| coroutines                 | 29.0 ms                                                               | 40.3 ms: 1.39x slower                                                    |
| async_generators           | 491 ms                                                                | 684 ms: 1.39x slower                                                     |
| docutils                   | 2.98 sec                                                              | 4.17 sec: 1.40x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.71 ms: 1.41x slower                                                    |
| generators                 | 43.5 ms                                                               | 61.5 ms: 1.41x slower                                                    |
| scimark_fft                | 418 ms                                                                | 593 ms: 1.42x slower                                                     |
| tornado_http               | 136 ms                                                                | 196 ms: 1.45x slower                                                     |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 8.97 ms: 1.45x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 12.3 ms: 1.47x slower                                                    |
| pylint                     | 355 ms                                                                | 522 ms: 1.47x slower                                                     |
| deepcopy_reduce            | 4.10 us                                                               | 6.10 us: 1.49x slower                                                    |
| xml_etree_generate         | 112 ms                                                                | 170 ms: 1.52x slower                                                     |
| telco                      | 8.51 ms                                                               | 13.0 ms: 1.53x slower                                                    |
| meteor_contest             | 112 ms                                                                | 172 ms: 1.53x slower                                                     |
| deepcopy_memo              | 49.6 us                                                               | 76.2 us: 1.54x slower                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 2.03 ms: 1.55x slower                                                    |
| dulwich_log                | 62.0 ms                                                               | 97.7 ms: 1.58x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 157 ms: 1.58x slower                                                     |
| coverage                   | 87.3 ms                                                               | 142 ms: 1.63x slower                                                     |
| json_dumps                 | 12.3 ms                                                               | 20.0 ms: 1.63x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 145 ms: 1.67x slower                                                     |
| tomli_loads                | 2.59 sec                                                              | 4.33 sec: 1.67x slower                                                   |
| sympy_integrate            | 21.6 ms                                                               | 36.3 ms: 1.68x slower                                                    |
| comprehensions             | 25.4 us                                                               | 42.9 us: 1.69x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 2.14 sec: 1.70x slower                                                   |
| xml_etree_process          | 79.0 ms                                                               | 135 ms: 1.71x slower                                                     |
| sqlalchemy_declarative     | 157 ms                                                                | 271 ms: 1.72x slower                                                     |
| 2to3                       | 308 ms                                                                | 532 ms: 1.73x slower                                                     |
| spectral_norm              | 131 ms                                                                | 231 ms: 1.77x slower                                                     |
| fannkuch                   | 443 ms                                                                | 797 ms: 1.80x slower                                                     |
| genshi_xml                 | 60.6 ms                                                               | 109 ms: 1.80x slower                                                     |
| sqlalchemy_imperative      | 16.7 ms                                                               | 30.0 ms: 1.80x slower                                                    |
| python_startup             | 11.4 ms                                                               | 20.8 ms: 1.83x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 120 ms: 1.84x slower                                                     |
| sqlglot_normalize          | 126 ms                                                                | 234 ms: 1.86x slower                                                     |
| pyflate                    | 559 ms                                                                | 1.04 sec: 1.86x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 338 us: 1.87x slower                                                     |
| regex_compile              | 137 ms                                                                | 260 ms: 1.89x slower                                                     |
| sympy_str                  | 280 ms                                                                | 530 ms: 1.89x slower                                                     |
| logging_simple             | 7.63 us                                                               | 14.5 us: 1.90x slower                                                    |
| thrift                     | 937 us                                                                | 1.79 ms: 1.92x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 3.61 sec: 1.92x slower                                                   |
| sqlglot_optimize           | 61.3 ms                                                               | 118 ms: 1.93x slower                                                     |
| pprint_safe_repr           | 916 ms                                                                | 1.77 sec: 1.93x slower                                                   |
| logging_format             | 8.34 us                                                               | 16.3 us: 1.96x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 54.0 ms: 1.97x slower                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 177 ms: 2.08x slower                                                     |
| django_template            | 40.7 ms                                                               | 85.1 ms: 2.09x slower                                                    |
| sympy_sum                  | 154 ms                                                                | 329 ms: 2.13x slower                                                     |
| sympy_expand               | 454 ms                                                                | 980 ms: 2.16x slower                                                     |
| unpickle_pure_python       | 260 us                                                                | 566 us: 2.18x slower                                                     |
| chaos                      | 71.4 ms                                                               | 161 ms: 2.26x slower                                                     |
| pickle_pure_python         | 365 us                                                                | 828 us: 2.27x slower                                                     |
| logging_silent             | 127 ns                                                                | 290 ns: 2.29x slower                                                     |
| mako                       | 12.9 ms                                                               | 29.7 ms: 2.30x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 16.1 ms: 2.31x slower                                                    |
| float                      | 92.1 ms                                                               | 213 ms: 2.31x slower                                                     |
| scimark_lu                 | 146 ms                                                                | 347 ms: 2.38x slower                                                     |
| richards_super             | 58.5 ms                                                               | 139 ms: 2.39x slower                                                     |
| scimark_sor                | 150 ms                                                                | 359 ms: 2.40x slower                                                     |
| richards                   | 50.9 ms                                                               | 124 ms: 2.43x slower                                                     |
| sqlglot_transpile          | 1.83 ms                                                               | 4.51 ms: 2.47x slower                                                    |
| raytrace                   | 353 ms                                                                | 891 ms: 2.52x slower                                                     |
| go                         | 157 ms                                                                | 407 ms: 2.59x slower                                                     |
| sqlglot_parse              | 1.46 ms                                                               | 3.80 ms: 2.60x slower                                                    |
| nbody                      | 105 ms                                                                | 295 ms: 2.82x slower                                                     |
| deltablue                  | 4.12 ms                                                               | 12.8 ms: 3.10x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 63.9 ms: 9.05x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.66x slower                                                             |

Benchmark hidden because not significant (6): xml_etree_parse, regex_effbot, async_tree_memoization, async_tree_io_tg, async_tree_none, async_tree_memoization_tg
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20241102-3.14.0a1+-7d7d56d-NOGIL/bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json: bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.370x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.49x
- 95% likely to have a slowdown of 1.45x
- 99% likely to have a slowdown of 1.40x

# Memory
- memory change: 1.21x