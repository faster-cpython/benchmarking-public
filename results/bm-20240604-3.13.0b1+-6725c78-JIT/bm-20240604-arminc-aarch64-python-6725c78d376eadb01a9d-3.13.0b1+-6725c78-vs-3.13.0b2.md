# Results vs. 3.13.0b2

- fork: python
- ref: 6725c78d376eadb01a9d
- machine: linux-aarch64
- commit hash: 6725c78
- commit date: 2024-06-04
- overall geometric mean: 1.09x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 365 ms: 1.20x slower                                                     |
| chameleon      | 8.95 ms                                                      | 9.29 ms: 1.04x slower                                                    |
| docutils       | 3.10 sec                                                     | 3.62 sec: 1.17x slower                                                   |
| html5lib       | 66.1 ms                                                      | 71.7 ms: 1.08x slower                                                    |
| tornado_http   | 128 ms                                                       | 150 ms: 1.17x slower                                                     |
| Geometric mean | (ref)                                                        | 1.13x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.27 sec                                                     | 1.23 sec: 1.04x faster                                                   |
| async_tree_none            | 492 ms                                                       | 504 ms: 1.02x slower                                                     |
| async_tree_none_tg         | 476 ms                                                       | 489 ms: 1.03x slower                                                     |
| async_tree_memoization_tg  | 604 ms                                                       | 623 ms: 1.03x slower                                                     |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 817 ms: 1.03x slower                                                     |
| async_tree_memoization     | 645 ms                                                       | 666 ms: 1.03x slower                                                     |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 801 ms: 1.05x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.02x slower                                                             |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 89.2 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                        | 1.01x faster                                                             |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 31.1 ms                                                      | 30.3 ms: 1.02x faster                                                    |
| regex_compile  | 128 ms                                                       | 176 ms: 1.37x slower                                                     |
| Geometric mean | (ref)                                                        | 1.08x slower                                                             |

Benchmark hidden because not significant (2): regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_loads           | 32.1 us                                                      | 32.0 us: 1.00x faster                                                    |
| json_dumps           | 13.1 ms                                                      | 13.2 ms: 1.00x slower                                                    |
| pickle               | 13.4 us                                                      | 13.6 us: 1.02x slower                                                    |
| unpickle_list        | 6.52 us                                                      | 6.63 us: 1.02x slower                                                    |
| tomli_loads          | 2.57 sec                                                     | 2.62 sec: 1.02x slower                                                   |
| xml_etree_generate   | 114 ms                                                       | 117 ms: 1.03x slower                                                     |
| unpickle_pure_python | 251 us                                                       | 277 us: 1.10x slower                                                     |
| pickle_pure_python   | 359 us                                                       | 396 us: 1.10x slower                                                     |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                             |

Benchmark hidden because not significant (6): xml_etree_parse, pickle_list, pickle_dict, unpickle, xml_etree_iterparse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 15.9 ms: 1.22x slower                                                    |
| python_startup_no_site | 8.60 ms                                                      | 11.2 ms: 1.30x slower                                                    |
| Geometric mean         | (ref)                                                        | 1.26x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 13.2 ms                                                      | 12.9 ms: 1.02x faster                                                    |
| django_template | 42.3 ms                                                      | 49.8 ms: 1.18x slower                                                    |
| genshi_text     | 27.4 ms                                                      | 34.3 ms: 1.25x slower                                                    |
| genshi_xml      | 60.4 ms                                                      | 83.0 ms: 1.38x slower                                                    |
| Geometric mean  | (ref)                                                        | 1.19x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.27 sec                                                     | 1.23 sec: 1.04x faster                                                   |
| deepcopy_memo              | 50.8 us                                                      | 49.4 us: 1.03x faster                                                    |
| float                      | 91.4 ms                                                      | 89.2 ms: 1.02x faster                                                    |
| regex_v8                   | 31.1 ms                                                      | 30.3 ms: 1.02x faster                                                    |
| mako                       | 13.2 ms                                                      | 12.9 ms: 1.02x faster                                                    |
| sqlite_synth               | 3.90 us                                                      | 3.87 us: 1.01x faster                                                    |
| json_loads                 | 32.1 us                                                      | 32.0 us: 1.00x faster                                                    |
| json_dumps                 | 13.1 ms                                                      | 13.2 ms: 1.00x slower                                                    |
| richards_super             | 62.3 ms                                                      | 63.0 ms: 1.01x slower                                                    |
| pickle                     | 13.4 us                                                      | 13.6 us: 1.02x slower                                                    |
| unpickle_list              | 6.52 us                                                      | 6.63 us: 1.02x slower                                                    |
| tomli_loads                | 2.57 sec                                                     | 2.62 sec: 1.02x slower                                                   |
| pathlib                    | 22.8 ms                                                      | 23.3 ms: 1.02x slower                                                    |
| async_tree_none            | 492 ms                                                       | 504 ms: 1.02x slower                                                     |
| logging_format             | 7.82 us                                                      | 8.02 us: 1.02x slower                                                    |
| telco                      | 10.0 ms                                                      | 10.3 ms: 1.03x slower                                                    |
| async_tree_none_tg         | 476 ms                                                       | 489 ms: 1.03x slower                                                     |
| xml_etree_generate         | 114 ms                                                       | 117 ms: 1.03x slower                                                     |
| meteor_contest             | 113 ms                                                       | 117 ms: 1.03x slower                                                     |
| async_tree_memoization_tg  | 604 ms                                                       | 623 ms: 1.03x slower                                                     |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.28 sec: 1.03x slower                                                   |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 817 ms: 1.03x slower                                                     |
| spectral_norm              | 141 ms                                                       | 146 ms: 1.03x slower                                                     |
| async_tree_memoization     | 645 ms                                                       | 666 ms: 1.03x slower                                                     |
| scimark_fft                | 445 ms                                                       | 460 ms: 1.03x slower                                                     |
| mdp                        | 3.33 sec                                                     | 3.44 sec: 1.03x slower                                                   |
| logging_silent             | 133 ns                                                       | 138 ns: 1.04x slower                                                     |
| chameleon                  | 8.95 ms                                                      | 9.29 ms: 1.04x slower                                                    |
| fannkuch                   | 451 ms                                                       | 469 ms: 1.04x slower                                                     |
| create_gc_cycles           | 2.33 ms                                                      | 2.42 ms: 1.04x slower                                                    |
| async_generators           | 488 ms                                                       | 509 ms: 1.04x slower                                                     |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 801 ms: 1.05x slower                                                     |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.95 ms: 1.06x slower                                                    |
| crypto_pyaes               | 82.0 ms                                                      | 87.1 ms: 1.06x slower                                                    |
| generators                 | 37.1 ms                                                      | 39.5 ms: 1.06x slower                                                    |
| scimark_monte_carlo        | 82.3 ms                                                      | 88.1 ms: 1.07x slower                                                    |
| typing_runtime_protocols   | 193 us                                                       | 207 us: 1.07x slower                                                     |
| raytrace                   | 297 ms                                                       | 318 ms: 1.07x slower                                                     |
| bench_thread_pool          | 1.26 ms                                                      | 1.35 ms: 1.08x slower                                                    |
| pyflate                    | 557 ms                                                       | 599 ms: 1.08x slower                                                     |
| html5lib                   | 66.1 ms                                                      | 71.7 ms: 1.08x slower                                                    |
| dask                       | 370 ms                                                       | 403 ms: 1.09x slower                                                     |
| scimark_sor                | 159 ms                                                       | 173 ms: 1.09x slower                                                     |
| sqlglot_normalize          | 129 ms                                                       | 142 ms: 1.10x slower                                                     |
| pycparser                  | 1.22 sec                                                     | 1.34 sec: 1.10x slower                                                   |
| unpickle_pure_python       | 251 us                                                       | 277 us: 1.10x slower                                                     |
| pickle_pure_python         | 359 us                                                       | 396 us: 1.10x slower                                                     |
| asyncio_tcp                | 584 ms                                                       | 645 ms: 1.10x slower                                                     |
| sqlglot_optimize           | 62.6 ms                                                      | 69.3 ms: 1.11x slower                                                    |
| deepcopy                   | 448 us                                                       | 497 us: 1.11x slower                                                     |
| flaskblogging              | 4.70 ms                                                      | 5.25 ms: 1.12x slower                                                    |
| sqlglot_parse              | 1.42 ms                                                      | 1.60 ms: 1.12x slower                                                    |
| go                         | 161 ms                                                       | 180 ms: 1.12x slower                                                     |
| comprehensions             | 20.5 us                                                      | 23.1 us: 1.12x slower                                                    |
| aiohttp                    | 1.18 ms                                                      | 1.35 ms: 1.14x slower                                                    |
| deepcopy_reduce            | 4.04 us                                                      | 4.64 us: 1.15x slower                                                    |
| gunicorn                   | 1.19 ms                                                      | 1.37 ms: 1.16x slower                                                    |
| docutils                   | 3.10 sec                                                     | 3.62 sec: 1.17x slower                                                   |
| nqueens                    | 98.9 ms                                                      | 116 ms: 1.17x slower                                                     |
| tornado_http               | 128 ms                                                       | 150 ms: 1.17x slower                                                     |
| sqlglot_transpile          | 1.71 ms                                                      | 2.00 ms: 1.17x slower                                                    |
| django_template            | 42.3 ms                                                      | 49.8 ms: 1.18x slower                                                    |
| deltablue                  | 3.88 ms                                                      | 4.58 ms: 1.18x slower                                                    |
| pprint_safe_repr           | 933 ms                                                       | 1.10 sec: 1.18x slower                                                   |
| 2to3                       | 305 ms                                                       | 365 ms: 1.20x slower                                                     |
| pprint_pformat             | 1.93 sec                                                     | 2.32 sec: 1.20x slower                                                   |
| bench_mp_pool              | 7.03 ms                                                      | 8.50 ms: 1.21x slower                                                    |
| python_startup             | 13.0 ms                                                      | 15.9 ms: 1.22x slower                                                    |
| mypy2                      | 767 ms                                                       | 938 ms: 1.22x slower                                                     |
| sympy_expand               | 457 ms                                                       | 561 ms: 1.23x slower                                                     |
| pylint                     | 337 ms                                                       | 417 ms: 1.24x slower                                                     |
| genshi_text                | 27.4 ms                                                      | 34.3 ms: 1.25x slower                                                    |
| sympy_str                  | 265 ms                                                       | 332 ms: 1.25x slower                                                     |
| hexiom                     | 7.08 ms                                                      | 8.91 ms: 1.26x slower                                                    |
| chaos                      | 68.3 ms                                                      | 86.1 ms: 1.26x slower                                                    |
| sympy_integrate            | 20.9 ms                                                      | 26.7 ms: 1.28x slower                                                    |
| scimark_lu                 | 141 ms                                                       | 183 ms: 1.29x slower                                                     |
| python_startup_no_site     | 8.60 ms                                                      | 11.2 ms: 1.30x slower                                                    |
| dulwich_log                | 58.5 ms                                                      | 77.4 ms: 1.32x slower                                                    |
| sympy_sum                  | 144 ms                                                       | 191 ms: 1.33x slower                                                     |
| regex_compile              | 128 ms                                                       | 176 ms: 1.37x slower                                                     |
| genshi_xml                 | 60.4 ms                                                      | 83.0 ms: 1.38x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.09x slower                                                             |

Benchmark hidden because not significant (19): xml_etree_parse, regex_effbot, pidigits, nbody, coverage, pickle_list, pickle_dict, gc_traversal, coroutines, regex_dna, asyncio_websockets, logging_simple, thrift, richards, json, unpickle, async_tree_io, xml_etree_iterparse, xml_etree_process
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.09x