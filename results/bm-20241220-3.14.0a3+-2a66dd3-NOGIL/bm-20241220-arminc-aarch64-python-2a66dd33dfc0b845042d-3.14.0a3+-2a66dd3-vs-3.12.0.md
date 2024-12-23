# Results vs. 3.12.0

- fork: python
- ref: 2a66dd33dfc0b845042d
- machine: linux-aarch64
- commit hash: 2a66dd3
- commit date: 2024-12-20
- overall geometric mean: 1.267x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x slower
- Memory change: 1.24x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 477 ms: 1.55x slower                                                     |
| docutils       | 2.98 sec                                                              | 3.78 sec: 1.27x slower                                                   |
| html5lib       | 65.1 ms                                                               | 109 ms: 1.68x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.49x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 1.19 sec: 1.18x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 1.21 sec: 1.16x faster                                                   |
| async_tree_memoization_tg  | 740 ms                                                                | 638 ms: 1.16x faster                                                     |
| async_tree_none            | 624 ms                                                                | 542 ms: 1.15x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 678 ms: 1.15x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 523 ms: 1.10x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 824 ms: 1.07x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 852 ms: 1.07x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.13x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 247 ms: 1.06x slower                                                     |
| float          | 92.1 ms                                                               | 159 ms: 1.73x slower                                                     |
| nbody          | 105 ms                                                                | 188 ms: 1.80x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.49x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.12 ms: 1.13x faster                                                    |
| regex_dna      | 254 ms                                                                | 267 ms: 1.05x slower                                                     |
| regex_v8       | 28.3 ms                                                               | 33.9 ms: 1.20x slower                                                    |
| regex_compile  | 137 ms                                                                | 191 ms: 1.39x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.12x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_iterparse  | 150 ms                                                                | 135 ms: 1.11x faster                                                     |
| xml_etree_parse      | 195 ms                                                                | 178 ms: 1.09x faster                                                     |
| json_loads           | 30.7 us                                                               | 37.4 us: 1.22x slower                                                    |
| xml_etree_generate   | 112 ms                                                                | 143 ms: 1.28x slower                                                     |
| tomli_loads          | 2.59 sec                                                              | 3.57 sec: 1.38x slower                                                   |
| xml_etree_process    | 79.0 ms                                                               | 111 ms: 1.41x slower                                                     |
| json_dumps           | 12.3 ms                                                               | 18.2 ms: 1.48x slower                                                    |
| unpickle_pure_python | 260 us                                                                | 472 us: 1.81x slower                                                     |
| pickle_pure_python   | 365 us                                                                | 692 us: 1.90x slower                                                     |
| Geometric mean       | (ref)                                                                 | 1.33x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 12.5 ms: 1.50x slower                                                    |
| python_startup         | 11.4 ms                                                               | 21.4 ms: 1.88x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.68x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 83.9 ms: 1.38x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 42.2 ms: 1.54x slower                                                    |
| django_template | 40.7 ms                                                               | 67.4 ms: 1.66x slower                                                    |
| mako            | 12.9 ms                                                               | 25.6 ms: 1.98x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.63x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 1.19 sec: 1.18x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 1.21 sec: 1.16x faster                                                   |
| async_tree_memoization_tg  | 740 ms                                                                | 638 ms: 1.16x faster                                                     |
| async_tree_none            | 624 ms                                                                | 542 ms: 1.15x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 678 ms: 1.15x faster                                                     |
| regex_effbot               | 4.64 ms                                                               | 4.12 ms: 1.13x faster                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 135 ms: 1.11x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 523 ms: 1.10x faster                                                     |
| xml_etree_parse            | 195 ms                                                                | 178 ms: 1.09x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 824 ms: 1.07x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 852 ms: 1.07x faster                                                     |
| asyncio_websockets         | 658 ms                                                                | 687 ms: 1.04x slower                                                     |
| regex_dna                  | 254 ms                                                                | 267 ms: 1.05x slower                                                     |
| pidigits                   | 233 ms                                                                | 247 ms: 1.06x slower                                                     |
| gc_traversal               | 4.40 ms                                                               | 5.03 ms: 1.15x slower                                                    |
| deepcopy_memo              | 49.6 us                                                               | 57.8 us: 1.17x slower                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 4.81 us: 1.17x slower                                                    |
| mdp                        | 3.41 sec                                                              | 4.05 sec: 1.19x slower                                                   |
| coroutines                 | 29.0 ms                                                               | 34.6 ms: 1.19x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 33.9 ms: 1.20x slower                                                    |
| spectral_norm              | 131 ms                                                                | 157 ms: 1.20x slower                                                     |
| json_loads                 | 30.7 us                                                               | 37.4 us: 1.22x slower                                                    |
| scimark_fft                | 418 ms                                                                | 517 ms: 1.24x slower                                                     |
| async_generators           | 491 ms                                                                | 606 ms: 1.24x slower                                                     |
| json                       | 5.54 ms                                                               | 6.85 ms: 1.24x slower                                                    |
| pylint                     | 355 ms                                                                | 446 ms: 1.26x slower                                                     |
| docutils                   | 2.98 sec                                                              | 3.78 sec: 1.27x slower                                                   |
| xml_etree_generate         | 112 ms                                                                | 143 ms: 1.28x slower                                                     |
| generators                 | 43.5 ms                                                               | 58.1 ms: 1.33x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 8.38 ms: 1.35x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 135 ms: 1.36x slower                                                     |
| dulwich_log                | 62.0 ms                                                               | 84.9 ms: 1.37x slower                                                    |
| tomli_loads                | 2.59 sec                                                              | 3.57 sec: 1.38x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 1.74 sec: 1.38x slower                                                   |
| genshi_xml                 | 60.6 ms                                                               | 83.9 ms: 1.38x slower                                                    |
| regex_compile              | 137 ms                                                                | 191 ms: 1.39x slower                                                     |
| crypto_pyaes               | 86.6 ms                                                               | 122 ms: 1.41x slower                                                     |
| xml_etree_process          | 79.0 ms                                                               | 111 ms: 1.41x slower                                                     |
| meteor_contest             | 112 ms                                                                | 159 ms: 1.42x slower                                                     |
| sqlglot_normalize          | 126 ms                                                                | 179 ms: 1.42x slower                                                     |
| telco                      | 8.51 ms                                                               | 12.1 ms: 1.42x slower                                                    |
| sqlglot_optimize           | 61.3 ms                                                               | 87.9 ms: 1.43x slower                                                    |
| thrift                     | 937 us                                                                | 1.35 ms: 1.44x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 18.2 ms: 1.48x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 218 ms: 1.50x slower                                                     |
| logging_format             | 8.34 us                                                               | 12.5 us: 1.50x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 12.5 ms: 1.50x slower                                                    |
| logging_simple             | 7.63 us                                                               | 11.5 us: 1.50x slower                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.97 ms: 1.51x slower                                                    |
| sympy_integrate            | 21.6 ms                                                               | 32.7 ms: 1.51x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 2.90 ms: 1.51x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 1.39 sec: 1.52x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 2.87 sec: 1.53x slower                                                   |
| comprehensions             | 25.4 us                                                               | 38.8 us: 1.53x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 42.2 ms: 1.54x slower                                                    |
| 2to3                       | 308 ms                                                                | 477 ms: 1.55x slower                                                     |
| fannkuch                   | 443 ms                                                                | 698 ms: 1.57x slower                                                     |
| typing_runtime_protocols   | 181 us                                                                | 284 us: 1.57x slower                                                     |
| sqlalchemy_declarative     | 157 ms                                                                | 248 ms: 1.58x slower                                                     |
| sqlalchemy_imperative      | 16.7 ms                                                               | 26.5 ms: 1.59x slower                                                    |
| pyflate                    | 559 ms                                                                | 894 ms: 1.60x slower                                                     |
| coverage                   | 87.3 ms                                                               | 144 ms: 1.65x slower                                                     |
| django_template            | 40.7 ms                                                               | 67.4 ms: 1.66x slower                                                    |
| sympy_str                  | 280 ms                                                                | 468 ms: 1.67x slower                                                     |
| html5lib                   | 65.1 ms                                                               | 109 ms: 1.68x slower                                                     |
| float                      | 92.1 ms                                                               | 159 ms: 1.73x slower                                                     |
| mypy2                      | 873 ms                                                                | 1.53 sec: 1.75x slower                                                   |
| nbody                      | 105 ms                                                                | 188 ms: 1.80x slower                                                     |
| scimark_monte_carlo        | 85.1 ms                                                               | 154 ms: 1.81x slower                                                     |
| chaos                      | 71.4 ms                                                               | 129 ms: 1.81x slower                                                     |
| unpickle_pure_python       | 260 us                                                                | 472 us: 1.81x slower                                                     |
| richards_super             | 58.5 ms                                                               | 109 ms: 1.86x slower                                                     |
| hexiom                     | 6.98 ms                                                               | 13.0 ms: 1.86x slower                                                    |
| raytrace                   | 353 ms                                                                | 663 ms: 1.88x slower                                                     |
| sympy_sum                  | 154 ms                                                                | 290 ms: 1.88x slower                                                     |
| python_startup             | 11.4 ms                                                               | 21.4 ms: 1.88x slower                                                    |
| richards                   | 50.9 ms                                                               | 96.0 ms: 1.88x slower                                                    |
| scimark_sor                | 150 ms                                                                | 283 ms: 1.89x slower                                                     |
| pickle_pure_python         | 365 us                                                                | 692 us: 1.90x slower                                                     |
| sympy_expand               | 454 ms                                                                | 870 ms: 1.92x slower                                                     |
| sqlglot_transpile          | 1.83 ms                                                               | 3.52 ms: 1.92x slower                                                    |
| mako                       | 12.9 ms                                                               | 25.6 ms: 1.98x slower                                                    |
| logging_silent             | 127 ns                                                                | 258 ns: 2.03x slower                                                     |
| sqlglot_parse              | 1.46 ms                                                               | 3.12 ms: 2.13x slower                                                    |
| go                         | 157 ms                                                                | 336 ms: 2.14x slower                                                     |
| deltablue                  | 4.12 ms                                                               | 11.0 ms: 2.67x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 64.1 ms: 9.09x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.43x slower                                                             |

Benchmark hidden because not significant (3): deepcopy, pathlib, sqlite_synth
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20241220-3.14.0a3+-2a66dd3-NOGIL/bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.267x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.31x
- 95% likely to have a slowdown of 1.28x
- 99% likely to have a slowdown of 1.25x

# Memory
- memory change: 1.24x