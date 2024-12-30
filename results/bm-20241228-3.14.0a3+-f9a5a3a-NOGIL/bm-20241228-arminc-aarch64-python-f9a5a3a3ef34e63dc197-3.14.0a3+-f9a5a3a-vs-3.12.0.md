# Results vs. 3.12.0

- fork: python
- ref: f9a5a3a3ef34e63dc197
- machine: linux-aarch64
- commit hash: f9a5a3a
- commit date: 2024-12-28
- overall geometric mean: 1.260x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x slower
- Memory change: 1.23x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 471 ms: 1.53x slower                                                     |
| docutils       | 2.98 sec                                                              | 3.71 sec: 1.24x slower                                                   |
| html5lib       | 65.1 ms                                                               | 110 ms: 1.69x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.48x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 1.18 sec: 1.19x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 1.21 sec: 1.17x faster                                                   |
| async_tree_memoization_tg  | 740 ms                                                                | 635 ms: 1.17x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 667 ms: 1.16x faster                                                     |
| async_tree_none            | 624 ms                                                                | 543 ms: 1.15x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 519 ms: 1.11x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 850 ms: 1.07x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 825 ms: 1.07x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.14x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 162 ms: 1.76x slower                                                     |
| nbody          | 105 ms                                                                | 191 ms: 1.83x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.49x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.13 ms: 1.12x faster                                                    |
| regex_dna      | 254 ms                                                                | 267 ms: 1.05x slower                                                     |
| regex_v8       | 28.3 ms                                                               | 33.4 ms: 1.18x slower                                                    |
| regex_compile  | 137 ms                                                                | 195 ms: 1.42x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.12x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 180 ms: 1.08x faster                                                     |
| xml_etree_iterparse  | 150 ms                                                                | 142 ms: 1.06x faster                                                     |
| json_loads           | 30.7 us                                                               | 37.3 us: 1.22x slower                                                    |
| xml_etree_generate   | 112 ms                                                                | 143 ms: 1.28x slower                                                     |
| tomli_loads          | 2.59 sec                                                              | 3.58 sec: 1.38x slower                                                   |
| xml_etree_process    | 79.0 ms                                                               | 111 ms: 1.41x slower                                                     |
| json_dumps           | 12.3 ms                                                               | 18.6 ms: 1.51x slower                                                    |
| unpickle_pure_python | 260 us                                                                | 467 us: 1.80x slower                                                     |
| pickle_pure_python   | 365 us                                                                | 701 us: 1.92x slower                                                     |
| Geometric mean       | (ref)                                                                 | 1.34x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 12.4 ms: 1.48x slower                                                    |
| python_startup         | 11.4 ms                                                               | 20.6 ms: 1.81x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.64x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 85.3 ms: 1.41x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 40.4 ms: 1.47x slower                                                    |
| django_template | 40.7 ms                                                               | 65.9 ms: 1.62x slower                                                    |
| mako            | 12.9 ms                                                               | 25.2 ms: 1.95x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.60x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 1.18 sec: 1.19x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 1.21 sec: 1.17x faster                                                   |
| async_tree_memoization_tg  | 740 ms                                                                | 635 ms: 1.17x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 667 ms: 1.16x faster                                                     |
| async_tree_none            | 624 ms                                                                | 543 ms: 1.15x faster                                                     |
| regex_effbot               | 4.64 ms                                                               | 4.13 ms: 1.12x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 519 ms: 1.11x faster                                                     |
| xml_etree_parse            | 195 ms                                                                | 180 ms: 1.08x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 850 ms: 1.07x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 825 ms: 1.07x faster                                                     |
| xml_etree_iterparse        | 150 ms                                                                | 142 ms: 1.06x faster                                                     |
| deepcopy                   | 446 us                                                                | 437 us: 1.02x faster                                                     |
| asyncio_websockets         | 658 ms                                                                | 681 ms: 1.04x slower                                                     |
| regex_dna                  | 254 ms                                                                | 267 ms: 1.05x slower                                                     |
| gc_traversal               | 4.40 ms                                                               | 5.02 ms: 1.14x slower                                                    |
| json                       | 5.54 ms                                                               | 6.37 ms: 1.15x slower                                                    |
| deepcopy_memo              | 49.6 us                                                               | 57.4 us: 1.16x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 33.4 ms: 1.18x slower                                                    |
| coroutines                 | 29.0 ms                                                               | 34.4 ms: 1.19x slower                                                    |
| mdp                        | 3.41 sec                                                              | 4.05 sec: 1.19x slower                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 4.87 us: 1.19x slower                                                    |
| json_loads                 | 30.7 us                                                               | 37.3 us: 1.22x slower                                                    |
| scimark_fft                | 418 ms                                                                | 509 ms: 1.22x slower                                                     |
| docutils                   | 2.98 sec                                                              | 3.71 sec: 1.24x slower                                                   |
| pylint                     | 355 ms                                                                | 446 ms: 1.26x slower                                                     |
| spectral_norm              | 131 ms                                                                | 165 ms: 1.26x slower                                                     |
| async_generators           | 491 ms                                                                | 621 ms: 1.27x slower                                                     |
| xml_etree_generate         | 112 ms                                                                | 143 ms: 1.28x slower                                                     |
| generators                 | 43.5 ms                                                               | 57.3 ms: 1.32x slower                                                    |
| sympy_sum                  | 154 ms                                                                | 206 ms: 1.33x slower                                                     |
| dulwich_log                | 62.0 ms                                                               | 82.8 ms: 1.34x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 8.32 ms: 1.34x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.71 sec: 1.37x slower                                                   |
| tomli_loads                | 2.59 sec                                                              | 3.58 sec: 1.38x slower                                                   |
| nqueens                    | 99.2 ms                                                               | 138 ms: 1.39x slower                                                     |
| sqlglot_normalize          | 126 ms                                                                | 176 ms: 1.40x slower                                                     |
| sqlglot_optimize           | 61.3 ms                                                               | 86.3 ms: 1.41x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 85.3 ms: 1.41x slower                                                    |
| xml_etree_process          | 79.0 ms                                                               | 111 ms: 1.41x slower                                                     |
| sympy_integrate            | 21.6 ms                                                               | 30.5 ms: 1.41x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 122 ms: 1.41x slower                                                     |
| regex_compile              | 137 ms                                                                | 195 ms: 1.42x slower                                                     |
| sympy_str                  | 280 ms                                                                | 400 ms: 1.43x slower                                                     |
| telco                      | 8.51 ms                                                               | 12.4 ms: 1.45x slower                                                    |
| meteor_contest             | 112 ms                                                                | 163 ms: 1.46x slower                                                     |
| genshi_text                | 27.4 ms                                                               | 40.4 ms: 1.47x slower                                                    |
| logging_simple             | 7.63 us                                                               | 11.3 us: 1.48x slower                                                    |
| logging_format             | 8.34 us                                                               | 12.3 us: 1.48x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 12.4 ms: 1.48x slower                                                    |
| sqlalchemy_declarative     | 157 ms                                                                | 235 ms: 1.49x slower                                                     |
| thrift                     | 937 us                                                                | 1.41 ms: 1.50x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 18.6 ms: 1.51x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 220 ms: 1.51x slower                                                     |
| sympy_expand               | 454 ms                                                                | 687 ms: 1.52x slower                                                     |
| create_gc_cycles           | 1.92 ms                                                               | 2.92 ms: 1.52x slower                                                    |
| 2to3                       | 308 ms                                                                | 471 ms: 1.53x slower                                                     |
| pprint_safe_repr           | 916 ms                                                                | 1.40 sec: 1.53x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 2.89 sec: 1.53x slower                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 2.02 ms: 1.54x slower                                                    |
| fannkuch                   | 443 ms                                                                | 703 ms: 1.58x slower                                                     |
| comprehensions             | 25.4 us                                                               | 40.3 us: 1.59x slower                                                    |
| sqlalchemy_imperative      | 16.7 ms                                                               | 26.7 ms: 1.60x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 290 us: 1.60x slower                                                     |
| django_template            | 40.7 ms                                                               | 65.9 ms: 1.62x slower                                                    |
| coverage                   | 87.3 ms                                                               | 143 ms: 1.64x slower                                                     |
| pyflate                    | 559 ms                                                                | 921 ms: 1.65x slower                                                     |
| html5lib                   | 65.1 ms                                                               | 110 ms: 1.69x slower                                                     |
| mypy2                      | 873 ms                                                                | 1.53 sec: 1.75x slower                                                   |
| float                      | 92.1 ms                                                               | 162 ms: 1.76x slower                                                     |
| unpickle_pure_python       | 260 us                                                                | 467 us: 1.80x slower                                                     |
| chaos                      | 71.4 ms                                                               | 129 ms: 1.81x slower                                                     |
| python_startup             | 11.4 ms                                                               | 20.6 ms: 1.81x slower                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 155 ms: 1.82x slower                                                     |
| nbody                      | 105 ms                                                                | 191 ms: 1.83x slower                                                     |
| richards_super             | 58.5 ms                                                               | 109 ms: 1.86x slower                                                     |
| raytrace                   | 353 ms                                                                | 664 ms: 1.88x slower                                                     |
| sqlglot_transpile          | 1.83 ms                                                               | 3.49 ms: 1.91x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 13.4 ms: 1.92x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 701 us: 1.92x slower                                                     |
| scimark_sor                | 150 ms                                                                | 288 ms: 1.92x slower                                                     |
| richards                   | 50.9 ms                                                               | 98.2 ms: 1.93x slower                                                    |
| mako                       | 12.9 ms                                                               | 25.2 ms: 1.95x slower                                                    |
| logging_silent             | 127 ns                                                                | 265 ns: 2.09x slower                                                     |
| sqlglot_parse              | 1.46 ms                                                               | 3.11 ms: 2.12x slower                                                    |
| go                         | 157 ms                                                                | 341 ms: 2.17x slower                                                     |
| deltablue                  | 4.12 ms                                                               | 11.1 ms: 2.70x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 63.2 ms: 8.96x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.42x slower                                                             |

Benchmark hidden because not significant (3): sqlite_synth, pidigits, pathlib
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20241228-3.14.0a3+-f9a5a3a-NOGIL/bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.260x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.29x
- 95% likely to have a slowdown of 1.27x
- 99% likely to have a slowdown of 1.24x

# Memory
- memory change: 1.23x