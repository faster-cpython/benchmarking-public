# Results vs. 3.13.0

- fork: brandtbucher
- ref: tier_two_improvement
- machine: linux-aarch64
- commit hash: bbb07e8
- commit date: 2024-07-13
- overall geometric mean: 1.07x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-arminc-aarch64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 362 ms: 1.19x slower                                                          |
| docutils       | 2.91 sec                                                 | 3.59 sec: 1.24x slower                                                        |
| html5lib       | 64.3 ms                                                  | 70.8 ms: 1.10x slower                                                         |
| tornado_http   | 131 ms                                                   | 139 ms: 1.06x slower                                                          |
| Geometric mean | (ref)                                                    | 1.14x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-arminc-aarch64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 547 ms: 1.19x faster                                                          |
| async_tree_none_tg         | 467 ms                                                   | 416 ms: 1.12x faster                                                          |
| async_tree_none            | 493 ms                                                   | 448 ms: 1.10x faster                                                          |
| async_tree_memoization     | 626 ms                                                   | 594 ms: 1.05x faster                                                          |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 734 ms: 1.04x faster                                                          |
| async_tree_io              | 1.11 sec                                                 | 1.07 sec: 1.04x faster                                                        |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 720 ms: 1.02x faster                                                          |
| asyncio_websockets         | 656 ms                                                   | 663 ms: 1.01x slower                                                          |
| async_generators           | 496 ms                                                   | 509 ms: 1.03x slower                                                          |
| coroutines                 | 28.2 ms                                                  | 29.0 ms: 1.03x slower                                                         |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.25 sec: 1.03x slower                                                        |
| asyncio_tcp                | 568 ms                                                   | 621 ms: 1.09x slower                                                          |
| Geometric mean             | (ref)                                                    | 1.03x faster                                                                  |

Benchmark hidden because not significant (1): async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-arminc-aarch64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 94.4 ms                                                  | 91.9 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                    | 1.01x faster                                                                  |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-arminc-aarch64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 30.5 ms: 1.03x faster                                                         |
| regex_dna      | 246 ms                                                   | 249 ms: 1.01x slower                                                          |
| regex_compile  | 128 ms                                                   | 178 ms: 1.39x slower                                                          |
| Geometric mean | (ref)                                                    | 1.08x slower                                                                  |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-arminc-aarch64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 147 ms                                                   | 149 ms: 1.02x slower                                                          |
| tomli_loads          | 2.53 sec                                                 | 2.62 sec: 1.04x slower                                                        |
| json_loads           | 31.4 us                                                  | 33.2 us: 1.06x slower                                                         |
| unpickle_pure_python | 254 us                                                   | 272 us: 1.07x slower                                                          |
| pickle_pure_python   | 359 us                                                   | 400 us: 1.11x slower                                                          |
| Geometric mean       | (ref)                                                    | 1.03x slower                                                                  |

Benchmark hidden because not significant (4): xml_etree_generate, xml_etree_process, json_dumps, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-arminc-aarch64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup | 13.3 ms                                                  | 12.9 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                    | 1.02x faster                                                                  |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-arminc-aarch64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 13.3 ms                                                  | 13.1 ms: 1.02x faster                                                         |
| django_template | 42.3 ms                                                  | 50.6 ms: 1.20x slower                                                         |
| genshi_text     | 27.7 ms                                                  | 34.5 ms: 1.24x slower                                                         |
| genshi_xml      | 60.2 ms                                                  | 78.7 ms: 1.31x slower                                                         |
| Geometric mean  | (ref)                                                    | 1.18x slower                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-arminc-aarch64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| deepcopy_memo              | 51.0 us                                                  | 38.8 us: 1.32x faster                                                         |
| async_tree_memoization_tg  | 649 ms                                                   | 547 ms: 1.19x faster                                                          |
| deepcopy                   | 451 us                                                   | 383 us: 1.18x faster                                                          |
| async_tree_none_tg         | 467 ms                                                   | 416 ms: 1.12x faster                                                          |
| async_tree_none            | 493 ms                                                   | 448 ms: 1.10x faster                                                          |
| async_tree_memoization     | 626 ms                                                   | 594 ms: 1.05x faster                                                          |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 734 ms: 1.04x faster                                                          |
| async_tree_io              | 1.11 sec                                                 | 1.07 sec: 1.04x faster                                                        |
| regex_v8                   | 31.5 ms                                                  | 30.5 ms: 1.03x faster                                                         |
| python_startup             | 13.3 ms                                                  | 12.9 ms: 1.03x faster                                                         |
| float                      | 94.4 ms                                                  | 91.9 ms: 1.03x faster                                                         |
| pathlib                    | 22.4 ms                                                  | 21.8 ms: 1.03x faster                                                         |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 720 ms: 1.02x faster                                                          |
| mako                       | 13.3 ms                                                  | 13.1 ms: 1.02x faster                                                         |
| bpe_tokeniser              | 5.90 sec                                                 | 5.84 sec: 1.01x faster                                                        |
| asyncio_websockets         | 656 ms                                                   | 663 ms: 1.01x slower                                                          |
| regex_dna                  | 246 ms                                                   | 249 ms: 1.01x slower                                                          |
| spectral_norm              | 141 ms                                                   | 143 ms: 1.01x slower                                                          |
| xml_etree_iterparse        | 147 ms                                                   | 149 ms: 1.02x slower                                                          |
| thrift                     | 946 us                                                   | 967 us: 1.02x slower                                                          |
| coverage                   | 98.5 ms                                                  | 101 ms: 1.02x slower                                                          |
| meteor_contest             | 113 ms                                                   | 116 ms: 1.02x slower                                                          |
| async_generators           | 496 ms                                                   | 509 ms: 1.03x slower                                                          |
| logging_simple             | 7.04 us                                                  | 7.22 us: 1.03x slower                                                         |
| coroutines                 | 28.2 ms                                                  | 29.0 ms: 1.03x slower                                                         |
| scimark_fft                | 447 ms                                                   | 460 ms: 1.03x slower                                                          |
| logging_silent             | 135 ns                                                   | 139 ns: 1.03x slower                                                          |
| logging_format             | 7.83 us                                                  | 8.06 us: 1.03x slower                                                         |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.25 sec: 1.03x slower                                                        |
| mdp                        | 3.36 sec                                                 | 3.47 sec: 1.03x slower                                                        |
| tomli_loads                | 2.53 sec                                                 | 2.62 sec: 1.04x slower                                                        |
| fannkuch                   | 452 ms                                                   | 473 ms: 1.05x slower                                                          |
| bench_thread_pool          | 1.28 ms                                                  | 1.34 ms: 1.05x slower                                                         |
| json                       | 5.61 ms                                                  | 5.90 ms: 1.05x slower                                                         |
| deepcopy_reduce            | 4.07 us                                                  | 4.28 us: 1.05x slower                                                         |
| json_loads                 | 31.4 us                                                  | 33.2 us: 1.06x slower                                                         |
| tornado_http               | 131 ms                                                   | 139 ms: 1.06x slower                                                          |
| scimark_monte_carlo        | 83.8 ms                                                  | 89.0 ms: 1.06x slower                                                         |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 6.99 ms: 1.06x slower                                                         |
| unpickle_pure_python       | 254 us                                                   | 272 us: 1.07x slower                                                          |
| crypto_pyaes               | 82.7 ms                                                  | 89.5 ms: 1.08x slower                                                         |
| bench_mp_pool              | 7.30 ms                                                  | 7.91 ms: 1.08x slower                                                         |
| typing_runtime_protocols   | 192 us                                                   | 210 us: 1.09x slower                                                          |
| telco                      | 9.73 ms                                                  | 10.6 ms: 1.09x slower                                                         |
| asyncio_tcp                | 568 ms                                                   | 621 ms: 1.09x slower                                                          |
| pycparser                  | 1.26 sec                                                 | 1.38 sec: 1.10x slower                                                        |
| html5lib                   | 64.3 ms                                                  | 70.8 ms: 1.10x slower                                                         |
| create_gc_cycles           | 2.12 ms                                                  | 2.34 ms: 1.10x slower                                                         |
| go                         | 163 ms                                                   | 179 ms: 1.10x slower                                                          |
| raytrace                   | 298 ms                                                   | 329 ms: 1.10x slower                                                          |
| pyflate                    | 556 ms                                                   | 616 ms: 1.11x slower                                                          |
| gc_traversal               | 4.53 ms                                                  | 5.02 ms: 1.11x slower                                                         |
| pickle_pure_python         | 359 us                                                   | 400 us: 1.11x slower                                                          |
| sqlglot_normalize          | 128 ms                                                   | 144 ms: 1.12x slower                                                          |
| dask                       | 350 ms                                                   | 393 ms: 1.12x slower                                                          |
| sqlglot_optimize           | 62.4 ms                                                  | 70.2 ms: 1.13x slower                                                         |
| scimark_sor                | 159 ms                                                   | 181 ms: 1.14x slower                                                          |
| comprehensions             | 20.4 us                                                  | 23.4 us: 1.15x slower                                                         |
| deltablue                  | 3.85 ms                                                  | 4.44 ms: 1.15x slower                                                         |
| sqlglot_parse              | 1.38 ms                                                  | 1.62 ms: 1.17x slower                                                         |
| sqlglot_transpile          | 1.73 ms                                                  | 2.03 ms: 1.17x slower                                                         |
| pylint                     | 343 ms                                                   | 404 ms: 1.18x slower                                                          |
| 2to3                       | 306 ms                                                   | 362 ms: 1.19x slower                                                          |
| nqueens                    | 98.7 ms                                                  | 118 ms: 1.19x slower                                                          |
| django_template            | 42.3 ms                                                  | 50.6 ms: 1.20x slower                                                         |
| docutils                   | 2.91 sec                                                 | 3.59 sec: 1.24x slower                                                        |
| sympy_expand               | 455 ms                                                   | 565 ms: 1.24x slower                                                          |
| genshi_text                | 27.7 ms                                                  | 34.5 ms: 1.24x slower                                                         |
| pprint_safe_repr           | 926 ms                                                   | 1.16 sec: 1.25x slower                                                        |
| pprint_pformat             | 1.90 sec                                                 | 2.38 sec: 1.26x slower                                                        |
| sympy_integrate            | 21.0 ms                                                  | 26.6 ms: 1.27x slower                                                         |
| hexiom                     | 7.13 ms                                                  | 9.16 ms: 1.28x slower                                                         |
| sympy_str                  | 264 ms                                                   | 339 ms: 1.29x slower                                                          |
| chaos                      | 68.8 ms                                                  | 89.9 ms: 1.31x slower                                                         |
| genshi_xml                 | 60.2 ms                                                  | 78.7 ms: 1.31x slower                                                         |
| scimark_lu                 | 139 ms                                                   | 184 ms: 1.32x slower                                                          |
| sympy_sum                  | 143 ms                                                   | 195 ms: 1.36x slower                                                          |
| regex_compile              | 128 ms                                                   | 178 ms: 1.39x slower                                                          |
| Geometric mean             | (ref)                                                    | 1.07x slower                                                                  |

Benchmark hidden because not significant (12): generators, xml_etree_generate, python_startup_no_site, nbody, xml_etree_process, richards, pidigits, regex_effbot, richards_super, json_dumps, async_tree_io_tg, xml_etree_parse
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240713-3.14.0a0-bbb07e8-JIT/bm-20240713-arminc-aarch64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8.json: dulwich_log

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.09x