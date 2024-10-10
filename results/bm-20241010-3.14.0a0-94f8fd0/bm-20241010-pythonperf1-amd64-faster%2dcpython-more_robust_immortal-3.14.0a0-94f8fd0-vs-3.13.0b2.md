# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: more_robust_immortal
- machine: windows-amd64
- commit hash: 94f8fd0
- commit date: 2024-10-10
- overall geometric mean: 1.07x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241010-pythonperf1-amd64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 227 ms: 1.10x slower                                                                 |
| docutils       | 1.63 sec                                                        | 1.71 sec: 1.05x slower                                                               |
| html5lib       | 35.0 ms                                                         | 42.2 ms: 1.20x slower                                                                |
| tornado_http   | 81.8 ms                                                         | 94.8 ms: 1.16x slower                                                                |
| Geometric mean | (ref)                                                           | 1.13x slower                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241010-pythonperf1-amd64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 605 ms                                                          | 587 ms: 1.03x faster                                                                 |
| async_tree_none            | 218 ms                                                          | 212 ms: 1.03x faster                                                                 |
| async_tree_cpu_io_mixed    | 389 ms                                                          | 398 ms: 1.02x slower                                                                 |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 393 ms: 1.03x slower                                                                 |
| async_tree_memoization     | 264 ms                                                          | 273 ms: 1.04x slower                                                                 |
| Geometric mean             | (ref)                                                           | 1.01x slower                                                                         |

Benchmark hidden because not significant (3): async_tree_memoization_tg, async_tree_io, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241010-pythonperf1-amd64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 147 ms: 1.02x faster                                                                 |
| float          | 49.7 ms                                                         | 54.8 ms: 1.10x slower                                                                |
| nbody          | 67.6 ms                                                         | 80.7 ms: 1.19x slower                                                                |
| Geometric mean | (ref)                                                           | 1.09x slower                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241010-pythonperf1-amd64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                          | 115 ms: 1.04x faster                                                                 |
| regex_effbot   | 1.58 ms                                                         | 1.56 ms: 1.01x faster                                                                |
| regex_compile  | 78.0 ms                                                         | 90.1 ms: 1.16x slower                                                                |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                         |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241010-pythonperf1-amd64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| xml_etree_parse      | 90.9 ms                                                         | 93.9 ms: 1.03x slower                                                                |
| pickle               | 7.11 us                                                         | 7.45 us: 1.05x slower                                                                |
| json_loads           | 14.2 us                                                         | 14.9 us: 1.05x slower                                                                |
| pickle_dict          | 18.1 us                                                         | 19.2 us: 1.06x slower                                                                |
| xml_etree_iterparse  | 62.3 ms                                                         | 66.9 ms: 1.07x slower                                                                |
| unpickle_list        | 2.62 us                                                         | 2.89 us: 1.10x slower                                                                |
| xml_etree_generate   | 53.2 ms                                                         | 58.7 ms: 1.10x slower                                                                |
| unpickle             | 8.40 us                                                         | 9.35 us: 1.11x slower                                                                |
| xml_etree_process    | 36.4 ms                                                         | 41.1 ms: 1.13x slower                                                                |
| json_dumps           | 5.61 ms                                                         | 6.34 ms: 1.13x slower                                                                |
| tomli_loads          | 1.35 sec                                                        | 1.62 sec: 1.20x slower                                                               |
| unpickle_pure_python | 122 us                                                          | 149 us: 1.22x slower                                                                 |
| pickle_pure_python   | 175 us                                                          | 215 us: 1.23x slower                                                                 |
| Geometric mean       | (ref)                                                           | 1.11x slower                                                                         |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241010-pythonperf1-amd64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 22.1 ms: 1.09x slower                                                                |
| python_startup_no_site | 16.2 ms                                                         | 17.9 ms: 1.10x slower                                                                |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241010-pythonperf1-amd64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 6.85 ms: 1.08x slower                                                                |
| genshi_xml      | 31.6 ms                                                         | 38.2 ms: 1.21x slower                                                                |
| django_template | 21.7 ms                                                         | 26.7 ms: 1.23x slower                                                                |
| genshi_text     | 14.4 ms                                                         | 17.8 ms: 1.24x slower                                                                |
| Geometric mean  | (ref)                                                           | 1.19x slower                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241010-pythonperf1-amd64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| thrift                     | 8.11 ms                                                         | 522 us: 15.54x faster                                                                |
| deepcopy                   | 220 us                                                          | 192 us: 1.14x faster                                                                 |
| deepcopy_memo              | 22.1 us                                                         | 19.9 us: 1.11x faster                                                                |
| regex_dna                  | 119 ms                                                          | 115 ms: 1.04x faster                                                                 |
| async_tree_io_tg           | 605 ms                                                          | 587 ms: 1.03x faster                                                                 |
| async_tree_none            | 218 ms                                                          | 212 ms: 1.03x faster                                                                 |
| pidigits                   | 150 ms                                                          | 147 ms: 1.02x faster                                                                 |
| gc_traversal               | 1.55 ms                                                         | 1.53 ms: 1.02x faster                                                                |
| deepcopy_reduce            | 1.99 us                                                         | 1.97 us: 1.01x faster                                                                |
| regex_effbot               | 1.58 ms                                                         | 1.56 ms: 1.01x faster                                                                |
| scimark_lu                 | 56.6 ms                                                         | 57.4 ms: 1.01x slower                                                                |
| async_tree_cpu_io_mixed    | 389 ms                                                          | 398 ms: 1.02x slower                                                                 |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 393 ms: 1.03x slower                                                                 |
| xml_etree_parse            | 90.9 ms                                                         | 93.9 ms: 1.03x slower                                                                |
| sqlite_synth               | 1.60 us                                                         | 1.65 us: 1.03x slower                                                                |
| async_tree_memoization     | 264 ms                                                          | 273 ms: 1.04x slower                                                                 |
| pickle                     | 7.11 us                                                         | 7.45 us: 1.05x slower                                                                |
| json_loads                 | 14.2 us                                                         | 14.9 us: 1.05x slower                                                                |
| create_gc_cycles           | 888 us                                                          | 934 us: 1.05x slower                                                                 |
| docutils                   | 1.63 sec                                                        | 1.71 sec: 1.05x slower                                                               |
| telco                      | 4.67 ms                                                         | 4.93 ms: 1.06x slower                                                                |
| pickle_dict                | 18.1 us                                                         | 19.2 us: 1.06x slower                                                                |
| pathlib                    | 75.9 ms                                                         | 80.3 ms: 1.06x slower                                                                |
| crypto_pyaes               | 45.5 ms                                                         | 48.3 ms: 1.06x slower                                                                |
| scimark_sparse_mat_mult    | 2.50 ms                                                         | 2.66 ms: 1.06x slower                                                                |
| go                         | 82.1 ms                                                         | 87.4 ms: 1.07x slower                                                                |
| sympy_sum                  | 84.4 ms                                                         | 90.2 ms: 1.07x slower                                                                |
| xml_etree_iterparse        | 62.3 ms                                                         | 66.9 ms: 1.07x slower                                                                |
| bench_mp_pool              | 64.8 ms                                                         | 69.6 ms: 1.07x slower                                                                |
| mako                       | 6.36 ms                                                         | 6.85 ms: 1.08x slower                                                                |
| spectral_norm              | 63.7 ms                                                         | 69.3 ms: 1.09x slower                                                                |
| python_startup             | 20.3 ms                                                         | 22.1 ms: 1.09x slower                                                                |
| coroutines                 | 12.8 ms                                                         | 13.9 ms: 1.09x slower                                                                |
| bench_thread_pool          | 768 us                                                          | 838 us: 1.09x slower                                                                 |
| meteor_contest             | 69.9 ms                                                         | 76.4 ms: 1.09x slower                                                                |
| 2to3                       | 207 ms                                                          | 227 ms: 1.10x slower                                                                 |
| python_startup_no_site     | 16.2 ms                                                         | 17.9 ms: 1.10x slower                                                                |
| float                      | 49.7 ms                                                         | 54.8 ms: 1.10x slower                                                                |
| unpickle_list              | 2.62 us                                                         | 2.89 us: 1.10x slower                                                                |
| xml_etree_generate         | 53.2 ms                                                         | 58.7 ms: 1.10x slower                                                                |
| sympy_integrate            | 12.2 ms                                                         | 13.5 ms: 1.11x slower                                                                |
| generators                 | 19.6 ms                                                         | 21.7 ms: 1.11x slower                                                                |
| logging_format             | 6.22 us                                                         | 6.91 us: 1.11x slower                                                                |
| unpickle                   | 8.40 us                                                         | 9.35 us: 1.11x slower                                                                |
| pylint                     | 205 ms                                                          | 228 ms: 1.11x slower                                                                 |
| logging_simple             | 5.78 us                                                         | 6.45 us: 1.12x slower                                                                |
| typing_runtime_protocols   | 101 us                                                          | 113 us: 1.12x slower                                                                 |
| sympy_str                  | 159 ms                                                          | 179 ms: 1.12x slower                                                                 |
| xml_etree_process          | 36.4 ms                                                         | 41.1 ms: 1.13x slower                                                                |
| json_dumps                 | 5.61 ms                                                         | 6.34 ms: 1.13x slower                                                                |
| async_generators           | 223 ms                                                          | 253 ms: 1.13x slower                                                                 |
| nqueens                    | 56.7 ms                                                         | 64.1 ms: 1.13x slower                                                                |
| logging_silent             | 52.9 ns                                                         | 60.1 ns: 1.14x slower                                                                |
| sympy_expand               | 271 ms                                                          | 308 ms: 1.14x slower                                                                 |
| comprehensions             | 10.4 us                                                         | 11.8 us: 1.14x slower                                                                |
| chaos                      | 38.4 ms                                                         | 43.8 ms: 1.14x slower                                                                |
| pyflate                    | 279 ms                                                          | 319 ms: 1.15x slower                                                                 |
| fannkuch                   | 243 ms                                                          | 279 ms: 1.15x slower                                                                 |
| sqlglot_optimize           | 32.7 ms                                                         | 37.6 ms: 1.15x slower                                                                |
| sqlglot_normalize          | 173 ms                                                          | 200 ms: 1.15x slower                                                                 |
| regex_compile              | 78.0 ms                                                         | 90.1 ms: 1.16x slower                                                                |
| tornado_http               | 81.8 ms                                                         | 94.8 ms: 1.16x slower                                                                |
| hexiom                     | 3.72 ms                                                         | 4.32 ms: 1.16x slower                                                                |
| dulwich_log                | 38.0 ms                                                         | 44.2 ms: 1.16x slower                                                                |
| coverage                   | 42.1 ms                                                         | 48.9 ms: 1.16x slower                                                                |
| pprint_safe_repr           | 474 ms                                                          | 552 ms: 1.16x slower                                                                 |
| scimark_sor                | 75.3 ms                                                         | 88.0 ms: 1.17x slower                                                                |
| pprint_pformat             | 966 ms                                                          | 1.13 sec: 1.17x slower                                                               |
| asyncio_tcp_ssl            | 1.48 sec                                                        | 1.73 sec: 1.17x slower                                                               |
| scimark_fft                | 171 ms                                                          | 202 ms: 1.18x slower                                                                 |
| raytrace                   | 162 ms                                                          | 192 ms: 1.19x slower                                                                 |
| nbody                      | 67.6 ms                                                         | 80.7 ms: 1.19x slower                                                                |
| sqlglot_transpile          | 955 us                                                          | 1.14 ms: 1.19x slower                                                                |
| scimark_monte_carlo        | 39.1 ms                                                         | 46.9 ms: 1.20x slower                                                                |
| mdp                        | 1.31 sec                                                        | 1.58 sec: 1.20x slower                                                               |
| tomli_loads                | 1.35 sec                                                        | 1.62 sec: 1.20x slower                                                               |
| html5lib                   | 35.0 ms                                                         | 42.2 ms: 1.20x slower                                                                |
| genshi_xml                 | 31.6 ms                                                         | 38.2 ms: 1.21x slower                                                                |
| richards_super             | 30.2 ms                                                         | 36.6 ms: 1.21x slower                                                                |
| richards                   | 26.7 ms                                                         | 32.5 ms: 1.22x slower                                                                |
| deltablue                  | 1.88 ms                                                         | 2.29 ms: 1.22x slower                                                                |
| sqlglot_parse              | 748 us                                                          | 912 us: 1.22x slower                                                                 |
| unpickle_pure_python       | 122 us                                                          | 149 us: 1.22x slower                                                                 |
| pickle_pure_python         | 175 us                                                          | 215 us: 1.23x slower                                                                 |
| django_template            | 21.7 ms                                                         | 26.7 ms: 1.23x slower                                                                |
| genshi_text                | 14.4 ms                                                         | 17.8 ms: 1.24x slower                                                                |
| json                       | 3.19 ms                                                         | 4.15 ms: 1.30x slower                                                                |
| asyncio_tcp                | 471 ms                                                          | 695 ms: 1.48x slower                                                                 |
| Geometric mean             | (ref)                                                           | 1.07x slower                                                                         |

Benchmark hidden because not significant (6): regex_v8, async_tree_memoization_tg, pycparser, async_tree_io, pickle_list, async_tree_none_tg
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2
Ignored benchmarks (1) of results/bm-20241010-3.14.0a0-94f8fd0/bm-20241010-pythonperf1-amd64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.09x
- 95% likely to have a slowdown of 1.09x
- 99% likely to have a slowdown of 1.08x

# Memory
- memory change: unknown