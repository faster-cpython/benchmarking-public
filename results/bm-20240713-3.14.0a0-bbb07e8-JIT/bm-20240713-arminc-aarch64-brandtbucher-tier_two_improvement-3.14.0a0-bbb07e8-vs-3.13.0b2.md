# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: tier_two_improvement
- machine: linux-aarch64
- commit hash: bbb07e8
- commit date: 2024-07-13
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-arminc-aarch64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 362 ms: 1.19x slower                                                          |
| docutils       | 3.10 sec                                                     | 3.59 sec: 1.16x slower                                                        |
| html5lib       | 66.1 ms                                                      | 70.8 ms: 1.07x slower                                                         |
| tornado_http   | 128 ms                                                       | 139 ms: 1.08x slower                                                          |
| Geometric mean | (ref)                                                        | 1.12x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-arminc-aarch64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.27 sec                                                     | 1.11 sec: 1.15x faster                                                        |
| async_tree_io              | 1.22 sec                                                     | 1.07 sec: 1.15x faster                                                        |
| async_tree_none_tg         | 476 ms                                                       | 416 ms: 1.15x faster                                                          |
| async_tree_memoization_tg  | 604 ms                                                       | 547 ms: 1.11x faster                                                          |
| async_tree_none            | 492 ms                                                       | 448 ms: 1.10x faster                                                          |
| async_tree_memoization     | 645 ms                                                       | 594 ms: 1.09x faster                                                          |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 734 ms: 1.08x faster                                                          |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 720 ms: 1.06x faster                                                          |
| Geometric mean             | (ref)                                                        | 1.11x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-arminc-aarch64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 91.9 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                  |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-arminc-aarch64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 249 ms: 1.04x faster                                                          |
| regex_v8       | 31.1 ms                                                      | 30.5 ms: 1.02x faster                                                         |
| regex_effbot   | 4.98 ms                                                      | 4.88 ms: 1.02x faster                                                         |
| regex_compile  | 128 ms                                                       | 178 ms: 1.39x slower                                                          |
| Geometric mean | (ref)                                                        | 1.07x slower                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-arminc-aarch64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| xml_etree_generate   | 114 ms                                                       | 112 ms: 1.01x faster                                                          |
| xml_etree_iterparse  | 147 ms                                                       | 149 ms: 1.02x slower                                                          |
| tomli_loads          | 2.57 sec                                                     | 2.62 sec: 1.02x slower                                                        |
| json_dumps           | 13.1 ms                                                      | 13.5 ms: 1.03x slower                                                         |
| json_loads           | 32.1 us                                                      | 33.2 us: 1.03x slower                                                         |
| unpickle_pure_python | 251 us                                                       | 272 us: 1.08x slower                                                          |
| pickle_pure_python   | 359 us                                                       | 400 us: 1.12x slower                                                          |
| Geometric mean       | (ref)                                                        | 1.03x slower                                                                  |

Benchmark hidden because not significant (2): xml_etree_process, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-arminc-aarch64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 12.9 ms: 1.01x faster                                                         |
| python_startup_no_site | 8.60 ms                                                      | 8.72 ms: 1.01x slower                                                         |
| Geometric mean         | (ref)                                                        | 1.00x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-arminc-aarch64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| django_template | 42.3 ms                                                      | 50.6 ms: 1.20x slower                                                         |
| genshi_text     | 27.4 ms                                                      | 34.5 ms: 1.26x slower                                                         |
| genshi_xml      | 60.4 ms                                                      | 78.7 ms: 1.30x slower                                                         |
| Geometric mean  | (ref)                                                        | 1.18x slower                                                                  |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-arminc-aarch64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| deepcopy_memo              | 50.8 us                                                      | 38.8 us: 1.31x faster                                                         |
| deepcopy                   | 448 us                                                       | 383 us: 1.17x faster                                                          |
| async_tree_io_tg           | 1.27 sec                                                     | 1.11 sec: 1.15x faster                                                        |
| async_tree_io              | 1.22 sec                                                     | 1.07 sec: 1.15x faster                                                        |
| async_tree_none_tg         | 476 ms                                                       | 416 ms: 1.15x faster                                                          |
| async_tree_memoization_tg  | 604 ms                                                       | 547 ms: 1.11x faster                                                          |
| async_tree_none            | 492 ms                                                       | 448 ms: 1.10x faster                                                          |
| async_tree_memoization     | 645 ms                                                       | 594 ms: 1.09x faster                                                          |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 734 ms: 1.08x faster                                                          |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 720 ms: 1.06x faster                                                          |
| pathlib                    | 22.8 ms                                                      | 21.8 ms: 1.04x faster                                                         |
| richards                   | 55.9 ms                                                      | 53.6 ms: 1.04x faster                                                         |
| regex_dna                  | 259 ms                                                       | 249 ms: 1.04x faster                                                          |
| gc_traversal               | 5.17 ms                                                      | 5.02 ms: 1.03x faster                                                         |
| richards_super             | 62.3 ms                                                      | 60.5 ms: 1.03x faster                                                         |
| regex_v8                   | 31.1 ms                                                      | 30.5 ms: 1.02x faster                                                         |
| regex_effbot               | 4.98 ms                                                      | 4.88 ms: 1.02x faster                                                         |
| xml_etree_generate         | 114 ms                                                       | 112 ms: 1.01x faster                                                          |
| python_startup             | 13.0 ms                                                      | 12.9 ms: 1.01x faster                                                         |
| float                      | 91.4 ms                                                      | 91.9 ms: 1.01x slower                                                         |
| spectral_norm              | 141 ms                                                       | 143 ms: 1.01x slower                                                          |
| python_startup_no_site     | 8.60 ms                                                      | 8.72 ms: 1.01x slower                                                         |
| xml_etree_iterparse        | 147 ms                                                       | 149 ms: 1.02x slower                                                          |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.25 sec: 1.02x slower                                                        |
| tomli_loads                | 2.57 sec                                                     | 2.62 sec: 1.02x slower                                                        |
| meteor_contest             | 113 ms                                                       | 116 ms: 1.02x slower                                                          |
| coverage                   | 98.4 ms                                                      | 101 ms: 1.02x slower                                                          |
| json_dumps                 | 13.1 ms                                                      | 13.5 ms: 1.03x slower                                                         |
| logging_format             | 7.82 us                                                      | 8.06 us: 1.03x slower                                                         |
| scimark_fft                | 445 ms                                                       | 460 ms: 1.03x slower                                                          |
| json_loads                 | 32.1 us                                                      | 33.2 us: 1.03x slower                                                         |
| async_generators           | 488 ms                                                       | 509 ms: 1.04x slower                                                          |
| mdp                        | 3.33 sec                                                     | 3.47 sec: 1.04x slower                                                        |
| logging_silent             | 133 ns                                                       | 139 ns: 1.04x slower                                                          |
| json                       | 5.64 ms                                                      | 5.90 ms: 1.05x slower                                                         |
| fannkuch                   | 451 ms                                                       | 473 ms: 1.05x slower                                                          |
| deepcopy_reduce            | 4.04 us                                                      | 4.28 us: 1.06x slower                                                         |
| telco                      | 10.0 ms                                                      | 10.6 ms: 1.06x slower                                                         |
| dask                       | 370 ms                                                       | 393 ms: 1.06x slower                                                          |
| asyncio_tcp                | 584 ms                                                       | 621 ms: 1.06x slower                                                          |
| bench_thread_pool          | 1.26 ms                                                      | 1.34 ms: 1.07x slower                                                         |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.99 ms: 1.07x slower                                                         |
| html5lib                   | 66.1 ms                                                      | 70.8 ms: 1.07x slower                                                         |
| unpickle_pure_python       | 251 us                                                       | 272 us: 1.08x slower                                                          |
| scimark_monte_carlo        | 82.3 ms                                                      | 89.0 ms: 1.08x slower                                                         |
| typing_runtime_protocols   | 193 us                                                       | 210 us: 1.08x slower                                                          |
| tornado_http               | 128 ms                                                       | 139 ms: 1.08x slower                                                          |
| crypto_pyaes               | 82.0 ms                                                      | 89.5 ms: 1.09x slower                                                         |
| pyflate                    | 557 ms                                                       | 616 ms: 1.11x slower                                                          |
| raytrace                   | 297 ms                                                       | 329 ms: 1.11x slower                                                          |
| sqlglot_normalize          | 129 ms                                                       | 144 ms: 1.11x slower                                                          |
| go                         | 161 ms                                                       | 179 ms: 1.12x slower                                                          |
| pickle_pure_python         | 359 us                                                       | 400 us: 1.12x slower                                                          |
| sqlglot_optimize           | 62.6 ms                                                      | 70.2 ms: 1.12x slower                                                         |
| bench_mp_pool              | 7.03 ms                                                      | 7.91 ms: 1.13x slower                                                         |
| pycparser                  | 1.22 sec                                                     | 1.38 sec: 1.13x slower                                                        |
| sqlglot_parse              | 1.42 ms                                                      | 1.62 ms: 1.14x slower                                                         |
| scimark_sor                | 159 ms                                                       | 181 ms: 1.14x slower                                                          |
| comprehensions             | 20.5 us                                                      | 23.4 us: 1.14x slower                                                         |
| deltablue                  | 3.88 ms                                                      | 4.44 ms: 1.15x slower                                                         |
| docutils                   | 3.10 sec                                                     | 3.59 sec: 1.16x slower                                                        |
| sqlglot_transpile          | 1.71 ms                                                      | 2.03 ms: 1.19x slower                                                         |
| nqueens                    | 98.9 ms                                                      | 118 ms: 1.19x slower                                                          |
| 2to3                       | 305 ms                                                       | 362 ms: 1.19x slower                                                          |
| django_template            | 42.3 ms                                                      | 50.6 ms: 1.20x slower                                                         |
| pylint                     | 337 ms                                                       | 404 ms: 1.20x slower                                                          |
| sympy_expand               | 457 ms                                                       | 565 ms: 1.23x slower                                                          |
| pprint_pformat             | 1.93 sec                                                     | 2.38 sec: 1.23x slower                                                        |
| pprint_safe_repr           | 933 ms                                                       | 1.16 sec: 1.24x slower                                                        |
| genshi_text                | 27.4 ms                                                      | 34.5 ms: 1.26x slower                                                         |
| dulwich_log                | 58.5 ms                                                      | 74.2 ms: 1.27x slower                                                         |
| sympy_integrate            | 20.9 ms                                                      | 26.6 ms: 1.28x slower                                                         |
| sympy_str                  | 265 ms                                                       | 339 ms: 1.28x slower                                                          |
| hexiom                     | 7.08 ms                                                      | 9.16 ms: 1.29x slower                                                         |
| scimark_lu                 | 141 ms                                                       | 184 ms: 1.30x slower                                                          |
| genshi_xml                 | 60.4 ms                                                      | 78.7 ms: 1.30x slower                                                         |
| chaos                      | 68.3 ms                                                      | 89.9 ms: 1.32x slower                                                         |
| sympy_sum                  | 144 ms                                                       | 195 ms: 1.36x slower                                                          |
| regex_compile              | 128 ms                                                       | 178 ms: 1.39x slower                                                          |
| Geometric mean             | (ref)                                                        | 1.06x slower                                                                  |

Benchmark hidden because not significant (12): xml_etree_process, mako, nbody, xml_etree_parse, coroutines, pidigits, bpe_tokeniser, create_gc_cycles, logging_simple, generators, thrift, asyncio_websockets
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.08x