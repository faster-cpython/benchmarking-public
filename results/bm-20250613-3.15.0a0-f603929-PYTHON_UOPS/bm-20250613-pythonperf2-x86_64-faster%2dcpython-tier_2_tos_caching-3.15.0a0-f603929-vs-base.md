# Results vs. base

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-x86_64
- commit hash: f603929
- commit date: 2025-06-13
- overall geometric mean: 1.034x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250612-pythonperf2-x86_64-python-e6c3039cb39e68ae9af9-3.15.0a0-e6c3039 | bm-20250613-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| 2to3           | 321 ms                                                                      | 331 ms: 1.03x slower                                                                |
| docutils       | 3.13 sec                                                                    | 3.19 sec: 1.02x slower                                                              |
| html5lib       | 70.2 ms                                                                     | 70.9 ms: 1.01x slower                                                               |
| sphinx         | 1.14 sec                                                                    | 1.15 sec: 1.01x slower                                                              |
| Geometric mean | (ref)                                                                       | 1.02x slower                                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250612-pythonperf2-x86_64-python-e6c3039cb39e68ae9af9-3.15.0a0-e6c3039 | bm-20250613-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_generators           | 460 ms                                                                      | 462 ms: 1.01x slower                                                                |
| async_tree_io_tg           | 676 ms                                                                      | 683 ms: 1.01x slower                                                                |
| async_tree_cpu_io_mixed_tg | 530 ms                                                                      | 535 ms: 1.01x slower                                                                |
| async_tree_memoization_tg  | 357 ms                                                                      | 361 ms: 1.01x slower                                                                |
| coroutines                 | 22.3 ms                                                                     | 22.6 ms: 1.01x slower                                                               |
| async_tree_none_tg         | 291 ms                                                                      | 296 ms: 1.02x slower                                                                |
| async_tree_cpu_io_mixed    | 531 ms                                                                      | 540 ms: 1.02x slower                                                                |
| async_tree_io              | 666 ms                                                                      | 679 ms: 1.02x slower                                                                |
| async_tree_memoization     | 356 ms                                                                      | 364 ms: 1.02x slower                                                                |
| async_tree_none            | 307 ms                                                                      | 315 ms: 1.02x slower                                                                |
| Geometric mean             | (ref)                                                                       | 1.01x slower                                                                        |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250612-pythonperf2-x86_64-python-e6c3039cb39e68ae9af9-3.15.0a0-e6c3039 | bm-20250613-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| pidigits       | 260 ms                                                                      | 260 ms: 1.00x slower                                                                |
| float          | 105 ms                                                                      | 112 ms: 1.06x slower                                                                |
| nbody          | 187 ms                                                                      | 216 ms: 1.16x slower                                                                |
| Geometric mean | (ref)                                                                       | 1.07x slower                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250612-pythonperf2-x86_64-python-e6c3039cb39e68ae9af9-3.15.0a0-e6c3039 | bm-20250613-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                                     | 3.75 ms: 1.00x faster                                                               |
| regex_dna      | 221 ms                                                                      | 222 ms: 1.00x slower                                                                |
| regex_compile  | 160 ms                                                                      | 164 ms: 1.03x slower                                                                |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                        |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250612-pythonperf2-x86_64-python-e6c3039cb39e68ae9af9-3.15.0a0-e6c3039 | bm-20250613-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| json_dumps           | 11.1 ms                                                                     | 11.2 ms: 1.01x slower                                                               |
| xml_etree_parse      | 143 ms                                                                      | 145 ms: 1.01x slower                                                                |
| xml_etree_iterparse  | 107 ms                                                                      | 110 ms: 1.03x slower                                                                |
| tomli_loads          | 3.17 sec                                                                    | 3.34 sec: 1.05x slower                                                              |
| pickle_pure_python   | 410 us                                                                      | 432 us: 1.05x slower                                                                |
| xml_etree_generate   | 107 ms                                                                      | 115 ms: 1.08x slower                                                                |
| xml_etree_process    | 75.0 ms                                                                     | 80.7 ms: 1.08x slower                                                               |
| unpickle_pure_python | 382 us                                                                      | 425 us: 1.11x slower                                                                |
| Geometric mean       | (ref)                                                                       | 1.05x slower                                                                        |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250612-pythonperf2-x86_64-python-e6c3039cb39e68ae9af9-3.15.0a0-e6c3039 | bm-20250613-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|------------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup_no_site | 8.80 ms                                                                     | 8.82 ms: 1.00x slower                                                               |
| python_startup         | 15.2 ms                                                                     | 15.3 ms: 1.00x slower                                                               |
| Geometric mean         | (ref)                                                                       | 1.00x slower                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250612-pythonperf2-x86_64-python-e6c3039cb39e68ae9af9-3.15.0a0-e6c3039 | bm-20250613-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|-----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                                     | 35.6 ms: 1.01x faster                                                               |
| genshi_text     | 23.5 ms                                                                     | 23.3 ms: 1.01x faster                                                               |
| genshi_xml      | 56.0 ms                                                                     | 56.4 ms: 1.01x slower                                                               |
| mako            | 16.8 ms                                                                     | 19.9 ms: 1.19x slower                                                               |
| Geometric mean  | (ref)                                                                       | 1.04x slower                                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20250612-pythonperf2-x86_64-python-e6c3039cb39e68ae9af9-3.15.0a0-e6c3039 | bm-20250613-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| generators                 | 29.9 ms                                                                     | 27.9 ms: 1.07x faster                                                               |
| gc_traversal               | 6.70 ms                                                                     | 6.38 ms: 1.05x faster                                                               |
| coverage                   | 80.5 ms                                                                     | 77.5 ms: 1.04x faster                                                               |
| logging_format             | 7.26 us                                                                     | 7.04 us: 1.03x faster                                                               |
| create_gc_cycles           | 2.88 ms                                                                     | 2.80 ms: 1.03x faster                                                               |
| logging_simple             | 6.61 us                                                                     | 6.42 us: 1.03x faster                                                               |
| deepcopy_reduce            | 2.97 us                                                                     | 2.94 us: 1.01x faster                                                               |
| django_template            | 36.0 ms                                                                     | 35.6 ms: 1.01x faster                                                               |
| genshi_text                | 23.5 ms                                                                     | 23.3 ms: 1.01x faster                                                               |
| deepcopy                   | 280 us                                                                      | 278 us: 1.01x faster                                                                |
| logging_silent             | 504 ns                                                                      | 501 ns: 1.01x faster                                                                |
| scimark_sor                | 104 ms                                                                      | 104 ms: 1.00x faster                                                                |
| regex_effbot               | 3.77 ms                                                                     | 3.75 ms: 1.00x faster                                                               |
| scimark_lu                 | 93.5 ms                                                                     | 93.3 ms: 1.00x faster                                                               |
| regex_dna                  | 221 ms                                                                      | 222 ms: 1.00x slower                                                                |
| python_startup_no_site     | 8.80 ms                                                                     | 8.82 ms: 1.00x slower                                                               |
| python_startup             | 15.2 ms                                                                     | 15.3 ms: 1.00x slower                                                               |
| pidigits                   | 260 ms                                                                      | 260 ms: 1.00x slower                                                                |
| async_generators           | 460 ms                                                                      | 462 ms: 1.01x slower                                                                |
| pathlib                    | 17.4 ms                                                                     | 17.5 ms: 1.01x slower                                                               |
| genshi_xml                 | 56.0 ms                                                                     | 56.4 ms: 1.01x slower                                                               |
| json_dumps                 | 11.1 ms                                                                     | 11.2 ms: 1.01x slower                                                               |
| subparsers                 | 25.6 ms                                                                     | 25.8 ms: 1.01x slower                                                               |
| html5lib                   | 70.2 ms                                                                     | 70.9 ms: 1.01x slower                                                               |
| async_tree_io_tg           | 676 ms                                                                      | 683 ms: 1.01x slower                                                                |
| sqlite_synth               | 3.04 us                                                                     | 3.07 us: 1.01x slower                                                               |
| async_tree_cpu_io_mixed_tg | 530 ms                                                                      | 535 ms: 1.01x slower                                                                |
| sphinx                     | 1.14 sec                                                                    | 1.15 sec: 1.01x slower                                                              |
| xml_etree_parse            | 143 ms                                                                      | 145 ms: 1.01x slower                                                                |
| sympy_integrate            | 23.6 ms                                                                     | 23.9 ms: 1.01x slower                                                               |
| async_tree_memoization_tg  | 357 ms                                                                      | 361 ms: 1.01x slower                                                                |
| coroutines                 | 22.3 ms                                                                     | 22.6 ms: 1.01x slower                                                               |
| raytrace                   | 334 ms                                                                      | 339 ms: 1.01x slower                                                                |
| sympy_sum                  | 162 ms                                                                      | 164 ms: 1.02x slower                                                                |
| async_tree_none_tg         | 291 ms                                                                      | 296 ms: 1.02x slower                                                                |
| json                       | 5.29 ms                                                                     | 5.38 ms: 1.02x slower                                                               |
| async_tree_cpu_io_mixed    | 531 ms                                                                      | 540 ms: 1.02x slower                                                                |
| async_tree_io              | 666 ms                                                                      | 679 ms: 1.02x slower                                                                |
| k_core                     | 2.32 sec                                                                    | 2.36 sec: 1.02x slower                                                              |
| docutils                   | 3.13 sec                                                                    | 3.19 sec: 1.02x slower                                                              |
| async_tree_memoization     | 356 ms                                                                      | 364 ms: 1.02x slower                                                                |
| chaos                      | 63.9 ms                                                                     | 65.3 ms: 1.02x slower                                                               |
| async_tree_none            | 307 ms                                                                      | 315 ms: 1.02x slower                                                                |
| sympy_str                  | 314 ms                                                                      | 321 ms: 1.02x slower                                                                |
| sqlglot_v2_normalize       | 122 ms                                                                      | 126 ms: 1.03x slower                                                                |
| regex_compile              | 160 ms                                                                      | 164 ms: 1.03x slower                                                                |
| xml_etree_iterparse        | 107 ms                                                                      | 110 ms: 1.03x slower                                                                |
| dulwich_log                | 61.8 ms                                                                     | 63.6 ms: 1.03x slower                                                               |
| 2to3                       | 321 ms                                                                      | 331 ms: 1.03x slower                                                                |
| sympy_expand               | 543 ms                                                                      | 562 ms: 1.03x slower                                                                |
| mdp                        | 1.46 sec                                                                    | 1.51 sec: 1.04x slower                                                              |
| sqlglot_v2_optimize        | 64.1 ms                                                                     | 66.7 ms: 1.04x slower                                                               |
| sqlglot_v2_transpile       | 2.15 ms                                                                     | 2.26 ms: 1.05x slower                                                               |
| tomli_loads                | 3.17 sec                                                                    | 3.34 sec: 1.05x slower                                                              |
| pickle_pure_python         | 410 us                                                                      | 432 us: 1.05x slower                                                                |
| telco                      | 9.18 ms                                                                     | 9.67 ms: 1.05x slower                                                               |
| richards_super             | 61.1 ms                                                                     | 64.5 ms: 1.06x slower                                                               |
| pycparser                  | 1.47 sec                                                                    | 1.55 sec: 1.06x slower                                                              |
| nqueens                    | 104 ms                                                                      | 110 ms: 1.06x slower                                                                |
| sqlglot_v2_parse           | 1.77 ms                                                                     | 1.87 ms: 1.06x slower                                                               |
| float                      | 105 ms                                                                      | 112 ms: 1.06x slower                                                                |
| meteor_contest             | 164 ms                                                                      | 174 ms: 1.06x slower                                                                |
| typing_runtime_protocols   | 202 us                                                                      | 215 us: 1.06x slower                                                                |
| pyflate                    | 650 ms                                                                      | 691 ms: 1.06x slower                                                                |
| richards                   | 54.2 ms                                                                     | 57.9 ms: 1.07x slower                                                               |
| shortest_path              | 498 ms                                                                      | 532 ms: 1.07x slower                                                                |
| xml_etree_generate         | 107 ms                                                                      | 115 ms: 1.08x slower                                                                |
| xml_etree_process          | 75.0 ms                                                                     | 80.7 ms: 1.08x slower                                                               |
| crypto_pyaes               | 108 ms                                                                      | 117 ms: 1.08x slower                                                                |
| connected_components       | 487 ms                                                                      | 528 ms: 1.08x slower                                                                |
| bpe_tokeniser              | 6.64 sec                                                                    | 7.23 sec: 1.09x slower                                                              |
| scimark_fft                | 493 ms                                                                      | 538 ms: 1.09x slower                                                                |
| comprehensions             | 30.3 us                                                                     | 33.2 us: 1.10x slower                                                               |
| deltablue                  | 5.92 ms                                                                     | 6.51 ms: 1.10x slower                                                               |
| pprint_safe_repr           | 1.18 sec                                                                    | 1.31 sec: 1.11x slower                                                              |
| pprint_pformat             | 2.40 sec                                                                    | 2.67 sec: 1.11x slower                                                              |
| unpickle_pure_python       | 382 us                                                                      | 425 us: 1.11x slower                                                                |
| scimark_monte_carlo        | 87.7 ms                                                                     | 97.8 ms: 1.11x slower                                                               |
| hexiom                     | 10.4 ms                                                                     | 11.7 ms: 1.12x slower                                                               |
| spectral_norm              | 191 ms                                                                      | 214 ms: 1.12x slower                                                                |
| fannkuch                   | 644 ms                                                                      | 725 ms: 1.13x slower                                                                |
| go                         | 220 ms                                                                      | 249 ms: 1.13x slower                                                                |
| nbody                      | 187 ms                                                                      | 216 ms: 1.16x slower                                                                |
| scimark_sparse_mat_mult    | 8.32 ms                                                                     | 9.65 ms: 1.16x slower                                                               |
| mako                       | 16.8 ms                                                                     | 19.9 ms: 1.19x slower                                                               |
| Geometric mean             | (ref)                                                                       | 1.03x slower                                                                        |

Benchmark hidden because not significant (8): thrift, asyncio_websockets, json_loads, deepcopy_memo, djangocms, many_optionals, pylint, regex_v8

- Geometric mean (including insignificant results): 1.034x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.00x