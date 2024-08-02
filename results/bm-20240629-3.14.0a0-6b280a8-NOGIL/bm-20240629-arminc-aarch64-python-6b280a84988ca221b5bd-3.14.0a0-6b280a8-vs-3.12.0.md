# Results vs. 3.12.0

- fork: python
- ref: 6b280a84988ca221b5bd
- machine: linux-aarch64
- commit hash: 6b280a8
- commit date: 2024-06-29
- overall geometric mean: 1.56x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.36x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 523 ms: 1.70x slower                                                    |
| docutils       | 2.98 sec                                                              | 4.12 sec: 1.38x slower                                                  |
| html5lib       | 65.1 ms                                                               | 120 ms: 1.85x slower                                                    |
| tornado_http   | 136 ms                                                                | 202 ms: 1.49x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.59x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 698 ms: 1.06x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.36 sec: 1.03x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 762 ms: 1.02x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 871 ms: 1.01x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 925 ms: 1.01x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.01x faster                                                            |

Benchmark hidden because not significant (3): async_tree_none, async_tree_none_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| float          | 92.1 ms                                                               | 211 ms: 2.29x slower                                                    |
| nbody          | 105 ms                                                                | 293 ms: 2.80x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.86x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.27 ms: 1.09x faster                                                   |
| regex_dna      | 254 ms                                                                | 241 ms: 1.05x faster                                                    |
| regex_v8       | 28.3 ms                                                               | 32.2 ms: 1.14x slower                                                   |
| regex_compile  | 137 ms                                                                | 258 ms: 1.88x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.17x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 182 ms: 1.07x faster                                                    |
| xml_etree_iterparse  | 150 ms                                                                | 155 ms: 1.03x slower                                                    |
| json_loads           | 30.7 us                                                               | 38.4 us: 1.25x slower                                                   |
| xml_etree_generate   | 112 ms                                                                | 164 ms: 1.46x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 18.1 ms: 1.47x slower                                                   |
| tomli_loads          | 2.59 sec                                                              | 4.29 sec: 1.65x slower                                                  |
| xml_etree_process    | 79.0 ms                                                               | 131 ms: 1.66x slower                                                    |
| unpickle_pure_python | 260 us                                                                | 546 us: 2.10x slower                                                    |
| pickle_pure_python   | 365 us                                                                | 778 us: 2.13x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.47x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 11.9 ms: 1.42x slower                                                   |
| python_startup         | 11.4 ms                                                               | 17.7 ms: 1.55x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.48x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 105 ms: 1.73x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 52.5 ms: 1.92x slower                                                   |
| django_template | 40.7 ms                                                               | 82.4 ms: 2.03x slower                                                   |
| mako            | 12.9 ms                                                               | 28.7 ms: 2.22x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.96x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| gc_traversal               | 4.40 ms                                                               | 3.43 ms: 1.28x faster                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 1.59 ms: 1.21x faster                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 6.25 ms: 1.13x faster                                                   |
| regex_effbot               | 4.64 ms                                                               | 4.27 ms: 1.09x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 182 ms: 1.07x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 698 ms: 1.06x faster                                                    |
| regex_dna                  | 254 ms                                                                | 241 ms: 1.05x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.36 sec: 1.03x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 762 ms: 1.02x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 871 ms: 1.01x faster                                                    |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 925 ms: 1.01x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 668 ms: 1.02x slower                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 155 ms: 1.03x slower                                                    |
| pathlib                    | 24.5 ms                                                               | 26.9 ms: 1.10x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 32.2 ms: 1.14x slower                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.48 sec: 1.14x slower                                                  |
| asyncio_tcp                | 566 ms                                                                | 681 ms: 1.20x slower                                                    |
| json                       | 5.54 ms                                                               | 6.89 ms: 1.24x slower                                                   |
| json_loads                 | 30.7 us                                                               | 38.4 us: 1.25x slower                                                   |
| deepcopy                   | 446 us                                                                | 562 us: 1.26x slower                                                    |
| mdp                        | 3.41 sec                                                              | 4.42 sec: 1.29x slower                                                  |
| generators                 | 43.5 ms                                                               | 57.2 ms: 1.31x slower                                                   |
| async_generators           | 491 ms                                                                | 667 ms: 1.36x slower                                                    |
| coroutines                 | 29.0 ms                                                               | 39.9 ms: 1.38x slower                                                   |
| docutils                   | 2.98 sec                                                              | 4.12 sec: 1.38x slower                                                  |
| scimark_fft                | 418 ms                                                                | 589 ms: 1.41x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 11.9 ms: 1.42x slower                                                   |
| pylint                     | 355 ms                                                                | 507 ms: 1.43x slower                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.87 ms: 1.43x slower                                                   |
| deepcopy_memo              | 49.6 us                                                               | 72.6 us: 1.46x slower                                                   |
| xml_etree_generate         | 112 ms                                                                | 164 ms: 1.46x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 18.1 ms: 1.47x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 9.16 ms: 1.48x slower                                                   |
| telco                      | 8.51 ms                                                               | 12.6 ms: 1.48x slower                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 6.11 us: 1.49x slower                                                   |
| tornado_http               | 136 ms                                                                | 202 ms: 1.49x slower                                                    |
| dulwich_log                | 62.0 ms                                                               | 95.9 ms: 1.55x slower                                                   |
| python_startup             | 11.4 ms                                                               | 17.7 ms: 1.55x slower                                                   |
| meteor_contest             | 112 ms                                                                | 176 ms: 1.57x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 156 ms: 1.57x slower                                                    |
| comprehensions             | 25.4 us                                                               | 40.8 us: 1.61x slower                                                   |
| coverage                   | 87.3 ms                                                               | 142 ms: 1.63x slower                                                    |
| sympy_integrate            | 21.6 ms                                                               | 35.3 ms: 1.63x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 2.06 sec: 1.64x slower                                                  |
| crypto_pyaes               | 86.6 ms                                                               | 142 ms: 1.64x slower                                                    |
| tomli_loads                | 2.59 sec                                                              | 4.29 sec: 1.65x slower                                                  |
| xml_etree_process          | 79.0 ms                                                               | 131 ms: 1.66x slower                                                    |
| 2to3                       | 308 ms                                                                | 523 ms: 1.70x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 105 ms: 1.73x slower                                                    |
| fannkuch                   | 443 ms                                                                | 769 ms: 1.74x slower                                                    |
| spectral_norm              | 131 ms                                                                | 235 ms: 1.80x slower                                                    |
| pyflate                    | 559 ms                                                                | 1.01 sec: 1.81x slower                                                  |
| thrift                     | 937 us                                                                | 1.72 ms: 1.83x slower                                                   |
| sqlglot_normalize          | 126 ms                                                                | 232 ms: 1.85x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 120 ms: 1.85x slower                                                    |
| sympy_str                  | 280 ms                                                                | 519 ms: 1.86x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 338 us: 1.87x slower                                                    |
| regex_compile              | 137 ms                                                                | 258 ms: 1.88x slower                                                    |
| sqlglot_optimize           | 61.3 ms                                                               | 116 ms: 1.89x slower                                                    |
| logging_format             | 8.34 us                                                               | 16.0 us: 1.91x slower                                                   |
| genshi_text                | 27.4 ms                                                               | 52.5 ms: 1.92x slower                                                   |
| logging_simple             | 7.63 us                                                               | 14.6 us: 1.92x slower                                                   |
| pprint_safe_repr           | 916 ms                                                                | 1.81 sec: 1.97x slower                                                  |
| pprint_pformat             | 1.88 sec                                                              | 3.73 sec: 1.98x slower                                                  |
| scimark_monte_carlo        | 85.1 ms                                                               | 172 ms: 2.02x slower                                                    |
| django_template            | 40.7 ms                                                               | 82.4 ms: 2.03x slower                                                   |
| sympy_sum                  | 154 ms                                                                | 314 ms: 2.04x slower                                                    |
| unpickle_pure_python       | 260 us                                                                | 546 us: 2.10x slower                                                    |
| sympy_expand               | 454 ms                                                                | 956 ms: 2.11x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 778 us: 2.13x slower                                                    |
| logging_silent             | 127 ns                                                                | 276 ns: 2.17x slower                                                    |
| mako                       | 12.9 ms                                                               | 28.7 ms: 2.22x slower                                                   |
| scimark_sor                | 150 ms                                                                | 340 ms: 2.27x slower                                                    |
| chaos                      | 71.4 ms                                                               | 163 ms: 2.28x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 15.9 ms: 2.28x slower                                                   |
| float                      | 92.1 ms                                                               | 211 ms: 2.29x slower                                                    |
| raytrace                   | 353 ms                                                                | 824 ms: 2.33x slower                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 4.28 ms: 2.34x slower                                                   |
| richards                   | 50.9 ms                                                               | 119 ms: 2.34x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 345 ms: 2.37x slower                                                    |
| richards_super             | 58.5 ms                                                               | 142 ms: 2.42x slower                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 3.69 ms: 2.52x slower                                                   |
| nbody                      | 105 ms                                                                | 293 ms: 2.80x slower                                                    |
| go                         | 157 ms                                                                | 449 ms: 2.85x slower                                                    |
| deltablue                  | 4.12 ms                                                               | 12.3 ms: 2.99x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.56x slower                                                            |

Benchmark hidden because not significant (3): async_tree_none, async_tree_none_tg, async_tree_io
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240629-3.14.0a0-6b280a8-NOGIL/bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json: bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.44x
- 95% likely to have a slowdown of 1.41x
- 99% likely to have a slowdown of 1.36x

# Memory
- memory change: 1.07x