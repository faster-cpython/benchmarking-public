# Results vs. 3.12.0

- fork: python
- ref: f6cc7c8bd01d8468af70
- machine: linux-aarch64
- commit hash: f6cc7c8
- commit date: 2024-10-26
- overall geometric mean: 1.093x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 389 ms: 1.26x slower                                                     |
| docutils       | 2.98 sec                                                              | 3.70 sec: 1.24x slower                                                   |
| html5lib       | 65.1 ms                                                               | 72.7 ms: 1.12x slower                                                    |
| tornado_http   | 136 ms                                                                | 148 ms: 1.09x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.18x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 468 ms: 1.33x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 565 ms: 1.31x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 597 ms: 1.30x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 471 ms: 1.22x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 1.18 sec: 1.20x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 769 ms: 1.19x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 755 ms: 1.17x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 1.24 sec: 1.14x faster                                                   |
| Geometric mean             | (ref)                                                                 | 1.23x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                     |
| float          | 92.1 ms                                                               | 96.8 ms: 1.05x slower                                                    |
| nbody          | 105 ms                                                                | 114 ms: 1.09x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 250 ms: 1.01x faster                                                     |
| regex_v8       | 28.3 ms                                                               | 30.9 ms: 1.09x slower                                                    |
| regex_effbot   | 4.64 ms                                                               | 5.27 ms: 1.14x slower                                                    |
| regex_compile  | 137 ms                                                                | 175 ms: 1.27x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.12x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 186 ms: 1.05x faster                                                     |
| json_loads           | 30.7 us                                                               | 31.5 us: 1.03x slower                                                    |
| unpickle_pure_python | 260 us                                                                | 268 us: 1.03x slower                                                     |
| tomli_loads          | 2.59 sec                                                              | 2.68 sec: 1.03x slower                                                   |
| xml_etree_process    | 79.0 ms                                                               | 81.5 ms: 1.03x slower                                                    |
| pickle_pure_python   | 365 us                                                                | 391 us: 1.07x slower                                                     |
| json_dumps           | 12.3 ms                                                               | 14.2 ms: 1.16x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.03x slower                                                             |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.79 ms: 1.05x slower                                                    |
| python_startup         | 11.4 ms                                                               | 15.6 ms: 1.37x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.20x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.2 ms: 1.03x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 34.1 ms: 1.24x slower                                                    |
| django_template | 40.7 ms                                                               | 53.0 ms: 1.30x slower                                                    |
| genshi_xml      | 60.6 ms                                                               | 82.8 ms: 1.37x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.23x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 468 ms: 1.33x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 565 ms: 1.31x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 597 ms: 1.30x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 39.3 us: 1.26x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 471 ms: 1.22x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 1.18 sec: 1.20x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 769 ms: 1.19x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 755 ms: 1.17x faster                                                     |
| deepcopy                   | 446 us                                                                | 383 us: 1.16x faster                                                     |
| pathlib                    | 24.5 ms                                                               | 21.5 ms: 1.14x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.24 sec: 1.14x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 186 ms: 1.05x faster                                                     |
| deepcopy_reduce            | 4.10 us                                                               | 3.95 us: 1.04x faster                                                    |
| raytrace                   | 353 ms                                                                | 347 ms: 1.02x faster                                                     |
| regex_dna                  | 254 ms                                                                | 250 ms: 1.01x faster                                                     |
| asyncio_websockets         | 658 ms                                                                | 662 ms: 1.01x slower                                                     |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                     |
| mako                       | 12.9 ms                                                               | 13.2 ms: 1.03x slower                                                    |
| json_loads                 | 30.7 us                                                               | 31.5 us: 1.03x slower                                                    |
| mdp                        | 3.41 sec                                                              | 3.51 sec: 1.03x slower                                                   |
| unpickle_pure_python       | 260 us                                                                | 268 us: 1.03x slower                                                     |
| tomli_loads                | 2.59 sec                                                              | 2.68 sec: 1.03x slower                                                   |
| xml_etree_process          | 79.0 ms                                                               | 81.5 ms: 1.03x slower                                                    |
| scimark_sor                | 150 ms                                                                | 155 ms: 1.03x slower                                                     |
| json                       | 5.54 ms                                                               | 5.74 ms: 1.04x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 89.9 ms: 1.04x slower                                                    |
| thrift                     | 937 us                                                                | 976 us: 1.04x slower                                                     |
| scimark_monte_carlo        | 85.1 ms                                                               | 88.7 ms: 1.04x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 152 ms: 1.05x slower                                                     |
| bench_thread_pool          | 1.31 ms                                                               | 1.37 ms: 1.05x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 8.79 ms: 1.05x slower                                                    |
| float                      | 92.1 ms                                                               | 96.8 ms: 1.05x slower                                                    |
| async_generators           | 491 ms                                                                | 519 ms: 1.06x slower                                                     |
| logging_silent             | 127 ns                                                                | 135 ns: 1.06x slower                                                     |
| pickle_pure_python         | 365 us                                                                | 391 us: 1.07x slower                                                     |
| regex_v8                   | 28.3 ms                                                               | 30.9 ms: 1.09x slower                                                    |
| tornado_http               | 136 ms                                                                | 148 ms: 1.09x slower                                                     |
| nbody                      | 105 ms                                                                | 114 ms: 1.09x slower                                                     |
| scimark_fft                | 418 ms                                                                | 461 ms: 1.10x slower                                                     |
| deltablue                  | 4.12 ms                                                               | 4.54 ms: 1.10x slower                                                    |
| meteor_contest             | 112 ms                                                                | 124 ms: 1.10x slower                                                     |
| telco                      | 8.51 ms                                                               | 9.50 ms: 1.12x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 72.7 ms: 1.12x slower                                                    |
| sqlalchemy_imperative      | 16.7 ms                                                               | 18.8 ms: 1.13x slower                                                    |
| coverage                   | 87.3 ms                                                               | 98.9 ms: 1.13x slower                                                    |
| regex_effbot               | 4.64 ms                                                               | 5.27 ms: 1.14x slower                                                    |
| fannkuch                   | 443 ms                                                                | 505 ms: 1.14x slower                                                     |
| pyflate                    | 559 ms                                                                | 643 ms: 1.15x slower                                                     |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.14 ms: 1.15x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 14.2 ms: 1.16x slower                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.72 ms: 1.17x slower                                                    |
| go                         | 157 ms                                                                | 185 ms: 1.18x slower                                                     |
| spectral_norm              | 131 ms                                                                | 155 ms: 1.19x slower                                                     |
| sqlglot_transpile          | 1.83 ms                                                               | 2.19 ms: 1.20x slower                                                    |
| richards_super             | 58.5 ms                                                               | 70.5 ms: 1.21x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.51 sec: 1.21x slower                                                   |
| sqlalchemy_declarative     | 157 ms                                                                | 190 ms: 1.21x slower                                                     |
| chaos                      | 71.4 ms                                                               | 86.1 ms: 1.21x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 219 us: 1.21x slower                                                     |
| docutils                   | 2.98 sec                                                              | 3.70 sec: 1.24x slower                                                   |
| genshi_text                | 27.4 ms                                                               | 34.1 ms: 1.24x slower                                                    |
| sqlglot_normalize          | 126 ms                                                                | 157 ms: 1.25x slower                                                     |
| 2to3                       | 308 ms                                                                | 389 ms: 1.26x slower                                                     |
| nqueens                    | 99.2 ms                                                               | 126 ms: 1.27x slower                                                     |
| richards                   | 50.9 ms                                                               | 64.9 ms: 1.27x slower                                                    |
| regex_compile              | 137 ms                                                                | 175 ms: 1.27x slower                                                     |
| sympy_str                  | 280 ms                                                                | 362 ms: 1.30x slower                                                     |
| django_template            | 40.7 ms                                                               | 53.0 ms: 1.30x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 1.19 sec: 1.30x slower                                                   |
| dulwich_log                | 62.0 ms                                                               | 81.8 ms: 1.32x slower                                                    |
| sympy_expand               | 454 ms                                                                | 600 ms: 1.32x slower                                                     |
| pprint_pformat             | 1.88 sec                                                              | 2.51 sec: 1.33x slower                                                   |
| generators                 | 43.5 ms                                                               | 58.8 ms: 1.35x slower                                                    |
| sqlglot_optimize           | 61.3 ms                                                               | 83.4 ms: 1.36x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 82.8 ms: 1.37x slower                                                    |
| python_startup             | 11.4 ms                                                               | 15.6 ms: 1.37x slower                                                    |
| pylint                     | 355 ms                                                                | 489 ms: 1.38x slower                                                     |
| sympy_integrate            | 21.6 ms                                                               | 29.9 ms: 1.38x slower                                                    |
| sympy_sum                  | 154 ms                                                                | 222 ms: 1.44x slower                                                     |
| gc_traversal               | 4.40 ms                                                               | 6.35 ms: 1.44x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 10.5 ms: 1.50x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.65 ms: 1.90x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 1.47 sec: 208.45x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.17x slower                                                             |

Benchmark hidden because not significant (6): logging_format, xml_etree_generate, coroutines, xml_etree_iterparse, logging_simple, comprehensions
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (2) of results/bm-20241026-3.14.0a1+-f6cc7c8-JIT/bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json: bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.093x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: 1.11x