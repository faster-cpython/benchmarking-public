# Results vs. 3.13.0b2

- fork: python
- ref: 6725c78d376eadb01a9d
- machine: linux-aarch64
- commit hash: 6725c78
- commit date: 2024-06-04
- overall geometric mean: 1.16x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 357 ms: 1.17x slower                                                     |
| chameleon      | 8.95 ms                                                      | 10.3 ms: 1.15x slower                                                    |
| docutils       | 3.10 sec                                                     | 3.60 sec: 1.16x slower                                                   |
| html5lib       | 66.1 ms                                                      | 73.8 ms: 1.12x slower                                                    |
| tornado_http   | 128 ms                                                       | 139 ms: 1.08x slower                                                     |
| Geometric mean | (ref)                                                        | 1.14x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.27 sec                                                     | 1.24 sec: 1.03x faster                                                   |
| async_tree_io              | 1.22 sec                                                     | 1.27 sec: 1.04x slower                                                   |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 827 ms: 1.04x slower                                                     |
| async_tree_memoization_tg  | 604 ms                                                       | 637 ms: 1.05x slower                                                     |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 807 ms: 1.06x slower                                                     |
| async_tree_none            | 492 ms                                                       | 522 ms: 1.06x slower                                                     |
| async_tree_none_tg         | 476 ms                                                       | 505 ms: 1.06x slower                                                     |
| async_tree_memoization     | 645 ms                                                       | 685 ms: 1.06x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.04x slower                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 119 ms: 1.30x slower                                                     |
| nbody          | 114 ms                                                       | 152 ms: 1.34x slower                                                     |
| Geometric mean | (ref)                                                        | 1.20x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.98 ms                                                      | 4.92 ms: 1.01x faster                                                    |
| regex_compile  | 128 ms                                                       | 172 ms: 1.34x slower                                                     |
| Geometric mean | (ref)                                                        | 1.07x slower                                                             |

Benchmark hidden because not significant (2): regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle             | 19.8 us                                                      | 19.9 us: 1.01x slower                                                    |
| unpickle_list        | 6.52 us                                                      | 6.68 us: 1.02x slower                                                    |
| json_dumps           | 13.1 ms                                                      | 14.0 ms: 1.07x slower                                                    |
| xml_etree_iterparse  | 147 ms                                                       | 162 ms: 1.10x slower                                                     |
| xml_etree_process    | 80.8 ms                                                      | 90.9 ms: 1.12x slower                                                    |
| xml_etree_generate   | 114 ms                                                       | 130 ms: 1.15x slower                                                     |
| tomli_loads          | 2.57 sec                                                     | 3.23 sec: 1.26x slower                                                   |
| pickle_pure_python   | 359 us                                                       | 467 us: 1.30x slower                                                     |
| unpickle_pure_python | 251 us                                                       | 364 us: 1.45x slower                                                     |
| Geometric mean       | (ref)                                                        | 1.10x slower                                                             |

Benchmark hidden because not significant (5): json_loads, pickle_list, pickle_dict, pickle, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 13.2 ms: 1.02x slower                                                    |
| python_startup_no_site | 8.60 ms                                                      | 8.77 ms: 1.02x slower                                                    |
| Geometric mean         | (ref)                                                        | 1.02x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 42.3 ms                                                      | 51.1 ms: 1.21x slower                                                    |
| genshi_xml      | 60.4 ms                                                      | 78.6 ms: 1.30x slower                                                    |
| mako            | 13.2 ms                                                      | 17.5 ms: 1.33x slower                                                    |
| genshi_text     | 27.4 ms                                                      | 36.8 ms: 1.34x slower                                                    |
| Geometric mean  | (ref)                                                        | 1.29x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.27 sec                                                     | 1.24 sec: 1.03x faster                                                   |
| regex_effbot               | 4.98 ms                                                      | 4.92 ms: 1.01x faster                                                    |
| unpickle                   | 19.8 us                                                      | 19.9 us: 1.01x slower                                                    |
| gc_traversal               | 5.17 ms                                                      | 5.21 ms: 1.01x slower                                                    |
| coverage                   | 98.4 ms                                                      | 99.3 ms: 1.01x slower                                                    |
| python_startup             | 13.0 ms                                                      | 13.2 ms: 1.02x slower                                                    |
| python_startup_no_site     | 8.60 ms                                                      | 8.77 ms: 1.02x slower                                                    |
| unpickle_list              | 6.52 us                                                      | 6.68 us: 1.02x slower                                                    |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.27 sec: 1.03x slower                                                   |
| pathlib                    | 22.8 ms                                                      | 23.4 ms: 1.03x slower                                                    |
| logging_simple             | 7.21 us                                                      | 7.43 us: 1.03x slower                                                    |
| asyncio_tcp                | 584 ms                                                       | 602 ms: 1.03x slower                                                     |
| create_gc_cycles           | 2.33 ms                                                      | 2.41 ms: 1.03x slower                                                    |
| sqlite_synth               | 3.90 us                                                      | 4.04 us: 1.03x slower                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.27 sec: 1.04x slower                                                   |
| logging_format             | 7.82 us                                                      | 8.16 us: 1.04x slower                                                    |
| json                       | 5.64 ms                                                      | 5.89 ms: 1.04x slower                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 827 ms: 1.04x slower                                                     |
| coroutines                 | 29.0 ms                                                      | 30.3 ms: 1.05x slower                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 637 ms: 1.05x slower                                                     |
| dask                       | 370 ms                                                       | 392 ms: 1.06x slower                                                     |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 807 ms: 1.06x slower                                                     |
| async_generators           | 488 ms                                                       | 517 ms: 1.06x slower                                                     |
| async_tree_none            | 492 ms                                                       | 522 ms: 1.06x slower                                                     |
| async_tree_none_tg         | 476 ms                                                       | 505 ms: 1.06x slower                                                     |
| async_tree_memoization     | 645 ms                                                       | 685 ms: 1.06x slower                                                     |
| json_dumps                 | 13.1 ms                                                      | 14.0 ms: 1.07x slower                                                    |
| tornado_http               | 128 ms                                                       | 139 ms: 1.08x slower                                                     |
| bench_thread_pool          | 1.26 ms                                                      | 1.36 ms: 1.08x slower                                                    |
| mdp                        | 3.33 sec                                                     | 3.61 sec: 1.08x slower                                                   |
| telco                      | 10.0 ms                                                      | 10.9 ms: 1.09x slower                                                    |
| generators                 | 37.1 ms                                                      | 40.7 ms: 1.09x slower                                                    |
| flaskblogging              | 4.70 ms                                                      | 5.17 ms: 1.10x slower                                                    |
| xml_etree_iterparse        | 147 ms                                                       | 162 ms: 1.10x slower                                                     |
| aiohttp                    | 1.18 ms                                                      | 1.31 ms: 1.11x slower                                                    |
| html5lib                   | 66.1 ms                                                      | 73.8 ms: 1.12x slower                                                    |
| xml_etree_process          | 80.8 ms                                                      | 90.9 ms: 1.12x slower                                                    |
| pycparser                  | 1.22 sec                                                     | 1.38 sec: 1.13x slower                                                   |
| mypy2                      | 767 ms                                                       | 866 ms: 1.13x slower                                                     |
| dulwich_log                | 58.5 ms                                                      | 66.7 ms: 1.14x slower                                                    |
| sympy_expand               | 457 ms                                                       | 523 ms: 1.14x slower                                                     |
| xml_etree_generate         | 114 ms                                                       | 130 ms: 1.15x slower                                                     |
| chameleon                  | 8.95 ms                                                      | 10.3 ms: 1.15x slower                                                    |
| gunicorn                   | 1.19 ms                                                      | 1.37 ms: 1.15x slower                                                    |
| docutils                   | 3.10 sec                                                     | 3.60 sec: 1.16x slower                                                   |
| sqlglot_optimize           | 62.6 ms                                                      | 73.0 ms: 1.16x slower                                                    |
| sqlglot_normalize          | 129 ms                                                       | 151 ms: 1.17x slower                                                     |
| raytrace                   | 297 ms                                                       | 347 ms: 1.17x slower                                                     |
| 2to3                       | 305 ms                                                       | 357 ms: 1.17x slower                                                     |
| pylint                     | 337 ms                                                       | 395 ms: 1.17x slower                                                     |
| typing_runtime_protocols   | 193 us                                                       | 227 us: 1.17x slower                                                     |
| meteor_contest             | 113 ms                                                       | 135 ms: 1.19x slower                                                     |
| sympy_str                  | 265 ms                                                       | 318 ms: 1.20x slower                                                     |
| django_template            | 42.3 ms                                                      | 51.1 ms: 1.21x slower                                                    |
| deepcopy_reduce            | 4.04 us                                                      | 4.88 us: 1.21x slower                                                    |
| richards_super             | 62.3 ms                                                      | 75.4 ms: 1.21x slower                                                    |
| bench_mp_pool              | 7.03 ms                                                      | 8.58 ms: 1.22x slower                                                    |
| sympy_sum                  | 144 ms                                                       | 176 ms: 1.22x slower                                                     |
| richards                   | 55.9 ms                                                      | 68.9 ms: 1.23x slower                                                    |
| deepcopy                   | 448 us                                                       | 555 us: 1.24x slower                                                     |
| go                         | 161 ms                                                       | 199 ms: 1.24x slower                                                     |
| scimark_fft                | 445 ms                                                       | 558 ms: 1.25x slower                                                     |
| scimark_sor                | 159 ms                                                       | 200 ms: 1.25x slower                                                     |
| tomli_loads                | 2.57 sec                                                     | 3.23 sec: 1.26x slower                                                   |
| fannkuch                   | 451 ms                                                       | 574 ms: 1.27x slower                                                     |
| sympy_integrate            | 20.9 ms                                                      | 26.6 ms: 1.27x slower                                                    |
| pprint_pformat             | 1.93 sec                                                     | 2.47 sec: 1.28x slower                                                   |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 8.41 ms: 1.28x slower                                                    |
| crypto_pyaes               | 82.0 ms                                                      | 106 ms: 1.29x slower                                                     |
| sqlglot_parse              | 1.42 ms                                                      | 1.83 ms: 1.29x slower                                                    |
| pprint_safe_repr           | 933 ms                                                       | 1.21 sec: 1.30x slower                                                   |
| float                      | 91.4 ms                                                      | 119 ms: 1.30x slower                                                     |
| genshi_xml                 | 60.4 ms                                                      | 78.6 ms: 1.30x slower                                                    |
| pickle_pure_python         | 359 us                                                       | 467 us: 1.30x slower                                                     |
| chaos                      | 68.3 ms                                                      | 89.3 ms: 1.31x slower                                                    |
| sqlglot_transpile          | 1.71 ms                                                      | 2.25 ms: 1.32x slower                                                    |
| pyflate                    | 557 ms                                                       | 738 ms: 1.33x slower                                                     |
| mako                       | 13.2 ms                                                      | 17.5 ms: 1.33x slower                                                    |
| nbody                      | 114 ms                                                       | 152 ms: 1.34x slower                                                     |
| regex_compile              | 128 ms                                                       | 172 ms: 1.34x slower                                                     |
| genshi_text                | 27.4 ms                                                      | 36.8 ms: 1.34x slower                                                    |
| spectral_norm              | 141 ms                                                       | 191 ms: 1.35x slower                                                     |
| nqueens                    | 98.9 ms                                                      | 134 ms: 1.36x slower                                                     |
| deltablue                  | 3.88 ms                                                      | 5.31 ms: 1.37x slower                                                    |
| unpickle_pure_python       | 251 us                                                       | 364 us: 1.45x slower                                                     |
| scimark_monte_carlo        | 82.3 ms                                                      | 120 ms: 1.46x slower                                                     |
| logging_silent             | 133 ns                                                       | 199 ns: 1.49x slower                                                     |
| deepcopy_memo              | 50.8 us                                                      | 75.8 us: 1.49x slower                                                    |
| scimark_lu                 | 141 ms                                                       | 215 ms: 1.52x slower                                                     |
| comprehensions             | 20.5 us                                                      | 31.5 us: 1.54x slower                                                    |
| hexiom                     | 7.08 ms                                                      | 11.3 ms: 1.59x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.16x slower                                                             |

Benchmark hidden because not significant (10): regex_v8, regex_dna, json_loads, asyncio_websockets, pickle_list, pidigits, pickle_dict, thrift, pickle, xml_etree_parse
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.12x
- 95% likely to have a slowdown of 1.11x
- 99% likely to have a slowdown of 1.10x

# Memory
- memory change: 1.01x