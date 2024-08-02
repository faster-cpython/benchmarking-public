# Results vs. 3.13.0b2

- fork: python
- ref: 44995aab499b09a550de
- machine: linux-aarch64
- commit hash: 44995aa
- commit date: 2024-05-13
- overall geometric mean: 1.19x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 360 ms: 1.18x slower                                                     |
| chameleon      | 8.95 ms                                                      | 10.3 ms: 1.15x slower                                                    |
| docutils       | 3.10 sec                                                     | 3.54 sec: 1.14x slower                                                   |
| html5lib       | 66.1 ms                                                      | 75.0 ms: 1.14x slower                                                    |
| tornado_http   | 128 ms                                                       | 136 ms: 1.06x slower                                                     |
| Geometric mean | (ref)                                                        | 1.13x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 791 ms                                                       | 813 ms: 1.03x slower                                                     |
| async_tree_none            | 492 ms                                                       | 507 ms: 1.03x slower                                                     |
| async_tree_memoization_tg  | 604 ms                                                       | 625 ms: 1.03x slower                                                     |
| async_tree_memoization     | 645 ms                                                       | 673 ms: 1.04x slower                                                     |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 820 ms: 1.07x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.03x slower                                                             |

Benchmark hidden because not significant (3): async_tree_io_tg, async_tree_none_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 234 ms                                                       | 237 ms: 1.01x slower                                                     |
| float          | 91.4 ms                                                      | 116 ms: 1.27x slower                                                     |
| nbody          | 114 ms                                                       | 150 ms: 1.32x slower                                                     |
| Geometric mean | (ref)                                                        | 1.19x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 128 ms                                                       | 173 ms: 1.35x slower                                                     |
| Geometric mean | (ref)                                                        | 1.07x slower                                                             |

Benchmark hidden because not significant (3): regex_dna, regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle             | 19.8 us                                                      | 19.7 us: 1.00x faster                                                    |
| unpickle_list        | 6.52 us                                                      | 6.73 us: 1.03x slower                                                    |
| pickle               | 13.4 us                                                      | 13.8 us: 1.03x slower                                                    |
| json_dumps           | 13.1 ms                                                      | 13.7 ms: 1.04x slower                                                    |
| xml_etree_iterparse  | 147 ms                                                       | 161 ms: 1.10x slower                                                     |
| xml_etree_process    | 80.8 ms                                                      | 89.8 ms: 1.11x slower                                                    |
| xml_etree_generate   | 114 ms                                                       | 128 ms: 1.13x slower                                                     |
| tomli_loads          | 2.57 sec                                                     | 3.25 sec: 1.27x slower                                                   |
| pickle_pure_python   | 359 us                                                       | 470 us: 1.31x slower                                                     |
| unpickle_pure_python | 251 us                                                       | 367 us: 1.46x slower                                                     |
| Geometric mean       | (ref)                                                        | 1.10x slower                                                             |

Benchmark hidden because not significant (4): pickle_list, pickle_dict, json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup | 13.0 ms                                                      | 12.5 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                        | 1.02x faster                                                             |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 42.3 ms                                                      | 51.0 ms: 1.21x slower                                                    |
| genshi_xml      | 60.4 ms                                                      | 77.7 ms: 1.29x slower                                                    |
| mako            | 13.2 ms                                                      | 17.5 ms: 1.33x slower                                                    |
| genshi_text     | 27.4 ms                                                      | 37.0 ms: 1.35x slower                                                    |
| Geometric mean  | (ref)                                                        | 1.29x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup             | 13.0 ms                                                      | 12.5 ms: 1.03x faster                                                    |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.17 sec: 1.02x faster                                                   |
| unpickle                   | 19.8 us                                                      | 19.7 us: 1.00x faster                                                    |
| asyncio_websockets         | 657 ms                                                       | 662 ms: 1.01x slower                                                     |
| pidigits                   | 234 ms                                                       | 237 ms: 1.01x slower                                                     |
| thrift                     | 962 us                                                       | 986 us: 1.03x slower                                                     |
| create_gc_cycles           | 2.33 ms                                                      | 2.39 ms: 1.03x slower                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 813 ms: 1.03x slower                                                     |
| gc_traversal               | 5.17 ms                                                      | 5.32 ms: 1.03x slower                                                    |
| async_tree_none            | 492 ms                                                       | 507 ms: 1.03x slower                                                     |
| unpickle_list              | 6.52 us                                                      | 6.73 us: 1.03x slower                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 625 ms: 1.03x slower                                                     |
| pickle                     | 13.4 us                                                      | 13.8 us: 1.03x slower                                                    |
| coverage                   | 98.4 ms                                                      | 102 ms: 1.04x slower                                                     |
| dask                       | 370 ms                                                       | 385 ms: 1.04x slower                                                     |
| logging_simple             | 7.21 us                                                      | 7.49 us: 1.04x slower                                                    |
| sqlite_synth               | 3.90 us                                                      | 4.06 us: 1.04x slower                                                    |
| json                       | 5.64 ms                                                      | 5.88 ms: 1.04x slower                                                    |
| async_tree_memoization     | 645 ms                                                       | 673 ms: 1.04x slower                                                     |
| json_dumps                 | 13.1 ms                                                      | 13.7 ms: 1.04x slower                                                    |
| pathlib                    | 22.8 ms                                                      | 23.9 ms: 1.05x slower                                                    |
| logging_format             | 7.82 us                                                      | 8.28 us: 1.06x slower                                                    |
| coroutines                 | 29.0 ms                                                      | 30.7 ms: 1.06x slower                                                    |
| tornado_http               | 128 ms                                                       | 136 ms: 1.06x slower                                                     |
| generators                 | 37.1 ms                                                      | 39.5 ms: 1.06x slower                                                    |
| async_generators           | 488 ms                                                       | 524 ms: 1.07x slower                                                     |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 820 ms: 1.07x slower                                                     |
| bench_thread_pool          | 1.26 ms                                                      | 1.36 ms: 1.08x slower                                                    |
| flaskblogging              | 4.70 ms                                                      | 5.07 ms: 1.08x slower                                                    |
| mdp                        | 3.33 sec                                                     | 3.61 sec: 1.08x slower                                                   |
| xml_etree_iterparse        | 147 ms                                                       | 161 ms: 1.10x slower                                                     |
| bench_mp_pool              | 7.03 ms                                                      | 7.77 ms: 1.10x slower                                                    |
| aiohttp                    | 1.18 ms                                                      | 1.31 ms: 1.11x slower                                                    |
| xml_etree_process          | 80.8 ms                                                      | 89.8 ms: 1.11x slower                                                    |
| gunicorn                   | 1.19 ms                                                      | 1.33 ms: 1.12x slower                                                    |
| xml_etree_generate         | 114 ms                                                       | 128 ms: 1.13x slower                                                     |
| pycparser                  | 1.22 sec                                                     | 1.38 sec: 1.13x slower                                                   |
| dulwich_log                | 58.5 ms                                                      | 66.4 ms: 1.13x slower                                                    |
| html5lib                   | 66.1 ms                                                      | 75.0 ms: 1.14x slower                                                    |
| mypy2                      | 767 ms                                                       | 873 ms: 1.14x slower                                                     |
| docutils                   | 3.10 sec                                                     | 3.54 sec: 1.14x slower                                                   |
| sympy_expand               | 457 ms                                                       | 525 ms: 1.15x slower                                                     |
| chameleon                  | 8.95 ms                                                      | 10.3 ms: 1.15x slower                                                    |
| pylint                     | 337 ms                                                       | 393 ms: 1.17x slower                                                     |
| typing_runtime_protocols   | 193 us                                                       | 227 us: 1.17x slower                                                     |
| raytrace                   | 297 ms                                                       | 348 ms: 1.17x slower                                                     |
| sqlglot_normalize          | 129 ms                                                       | 152 ms: 1.17x slower                                                     |
| sqlglot_optimize           | 62.6 ms                                                      | 73.7 ms: 1.18x slower                                                    |
| 2to3                       | 305 ms                                                       | 360 ms: 1.18x slower                                                     |
| meteor_contest             | 113 ms                                                       | 136 ms: 1.20x slower                                                     |
| deepcopy_reduce            | 4.04 us                                                      | 4.83 us: 1.20x slower                                                    |
| sympy_str                  | 265 ms                                                       | 320 ms: 1.20x slower                                                     |
| sympy_sum                  | 144 ms                                                       | 173 ms: 1.21x slower                                                     |
| django_template            | 42.3 ms                                                      | 51.0 ms: 1.21x slower                                                    |
| richards_super             | 62.3 ms                                                      | 76.9 ms: 1.23x slower                                                    |
| deepcopy                   | 448 us                                                       | 558 us: 1.25x slower                                                     |
| richards                   | 55.9 ms                                                      | 69.6 ms: 1.25x slower                                                    |
| go                         | 161 ms                                                       | 201 ms: 1.25x slower                                                     |
| scimark_fft                | 445 ms                                                       | 561 ms: 1.26x slower                                                     |
| sqlglot_parse              | 1.42 ms                                                      | 1.80 ms: 1.26x slower                                                    |
| tomli_loads                | 2.57 sec                                                     | 3.25 sec: 1.27x slower                                                   |
| sympy_integrate            | 20.9 ms                                                      | 26.4 ms: 1.27x slower                                                    |
| pprint_pformat             | 1.93 sec                                                     | 2.45 sec: 1.27x slower                                                   |
| scimark_sor                | 159 ms                                                       | 202 ms: 1.27x slower                                                     |
| float                      | 91.4 ms                                                      | 116 ms: 1.27x slower                                                     |
| pprint_safe_repr           | 933 ms                                                       | 1.20 sec: 1.28x slower                                                   |
| genshi_xml                 | 60.4 ms                                                      | 77.7 ms: 1.29x slower                                                    |
| crypto_pyaes               | 82.0 ms                                                      | 106 ms: 1.29x slower                                                     |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 8.47 ms: 1.29x slower                                                    |
| chaos                      | 68.3 ms                                                      | 89.5 ms: 1.31x slower                                                    |
| pickle_pure_python         | 359 us                                                       | 470 us: 1.31x slower                                                     |
| sqlglot_transpile          | 1.71 ms                                                      | 2.25 ms: 1.31x slower                                                    |
| nbody                      | 114 ms                                                       | 150 ms: 1.32x slower                                                     |
| fannkuch                   | 451 ms                                                       | 599 ms: 1.33x slower                                                     |
| mako                       | 13.2 ms                                                      | 17.5 ms: 1.33x slower                                                    |
| genshi_text                | 27.4 ms                                                      | 37.0 ms: 1.35x slower                                                    |
| regex_compile              | 128 ms                                                       | 173 ms: 1.35x slower                                                     |
| nqueens                    | 98.9 ms                                                      | 134 ms: 1.36x slower                                                     |
| pyflate                    | 557 ms                                                       | 759 ms: 1.36x slower                                                     |
| deltablue                  | 3.88 ms                                                      | 5.32 ms: 1.37x slower                                                    |
| spectral_norm              | 141 ms                                                       | 194 ms: 1.37x slower                                                     |
| scimark_monte_carlo        | 82.3 ms                                                      | 119 ms: 1.45x slower                                                     |
| unpickle_pure_python       | 251 us                                                       | 367 us: 1.46x slower                                                     |
| logging_silent             | 133 ns                                                       | 199 ns: 1.49x slower                                                     |
| deepcopy_memo              | 50.8 us                                                      | 75.9 us: 1.50x slower                                                    |
| scimark_lu                 | 141 ms                                                       | 213 ms: 1.50x slower                                                     |
| comprehensions             | 20.5 us                                                      | 32.0 us: 1.56x slower                                                    |
| hexiom                     | 7.08 ms                                                      | 11.4 ms: 1.61x slower                                                    |
| telco                      | 10.0 ms                                                      | 165 ms: 16.50x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.19x slower                                                             |

Benchmark hidden because not significant (12): async_tree_io_tg, regex_dna, python_startup_no_site, regex_effbot, asyncio_tcp, pickle_list, pickle_dict, regex_v8, json_loads, xml_etree_parse, async_tree_none_tg, async_tree_io
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.12x
- 95% likely to have a slowdown of 1.11x
- 99% likely to have a slowdown of 1.09x

# Memory
- memory change: 1.01x