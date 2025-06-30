# Results vs. base

- fork: python
- ref: 75f40595e555e7d016cf
- machine: windows-amd64
- commit hash: 75f4059
- commit date: 2025-06-30
- overall geometric mean: 1.009x faster
- HPT reliability: 63.62%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250630-3.15.0a0-75f4059/bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json | results/bm-20250630-3.15.0a0-75f4059-JIT/bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| docutils       | 1.60 sec                                                                                                                   | 1.67 sec: 1.05x slower                                                                                                         |
| html5lib       | 38.0 ms                                                                                                                    | 38.7 ms: 1.02x slower                                                                                                          |
| sphinx         | 633 ms                                                                                                                     | 646 ms: 1.02x slower                                                                                                           |
| Geometric mean | (ref)                                                                                                                      | 1.02x slower                                                                                                                   |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250630-3.15.0a0-75f4059/bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json | results/bm-20250630-3.15.0a0-75f4059-JIT/bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 393 ms                                                                                                                     | 388 ms: 1.01x faster                                                                                                           |
| async_tree_none_tg         | 170 ms                                                                                                                     | 168 ms: 1.01x faster                                                                                                           |
| async_tree_cpu_io_mixed    | 328 ms                                                                                                                     | 333 ms: 1.01x slower                                                                                                           |
| asyncio_websockets         | 158 ms                                                                                                                     | 160 ms: 1.02x slower                                                                                                           |
| async_tree_cpu_io_mixed_tg | 340 ms                                                                                                                     | 346 ms: 1.02x slower                                                                                                           |
| coroutines                 | 14.4 ms                                                                                                                    | 14.8 ms: 1.03x slower                                                                                                          |
| asyncio_tcp_ssl            | 1.33 sec                                                                                                                   | 1.44 sec: 1.09x slower                                                                                                         |
| async_generators           | 230 ms                                                                                                                     | 253 ms: 1.10x slower                                                                                                           |
| asyncio_tcp                | 433 ms                                                                                                                     | 531 ms: 1.23x slower                                                                                                           |
| Geometric mean             | (ref)                                                                                                                      | 1.03x slower                                                                                                                   |

Benchmark hidden because not significant (4): async_tree_memoization_tg, async_tree_io, async_tree_memoization, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250630-3.15.0a0-75f4059/bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json | results/bm-20250630-3.15.0a0-75f4059-JIT/bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 63.0 ms                                                                                                                    | 56.8 ms: 1.11x faster                                                                                                          |
| float          | 43.1 ms                                                                                                                    | 44.5 ms: 1.03x slower                                                                                                          |
| Geometric mean | (ref)                                                                                                                      | 1.02x faster                                                                                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250630-3.15.0a0-75f4059/bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json | results/bm-20250630-3.15.0a0-75f4059-JIT/bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 79.4 ms                                                                                                                    | 78.1 ms: 1.02x faster                                                                                                          |
| regex_effbot   | 1.50 ms                                                                                                                    | 1.57 ms: 1.05x slower                                                                                                          |
| regex_dna      | 115 ms                                                                                                                     | 122 ms: 1.05x slower                                                                                                           |
| regex_v8       | 13.3 ms                                                                                                                    | 14.2 ms: 1.06x slower                                                                                                          |
| Geometric mean | (ref)                                                                                                                      | 1.04x slower                                                                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250630-3.15.0a0-75f4059/bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json | results/bm-20250630-3.15.0a0-75f4059-JIT/bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 135 us                                                                                                                     | 109 us: 1.24x faster                                                                                                           |
| tomli_loads          | 1.38 sec                                                                                                                   | 1.14 sec: 1.21x faster                                                                                                         |
| xml_etree_process    | 39.1 ms                                                                                                                    | 35.5 ms: 1.10x faster                                                                                                          |
| xml_etree_generate   | 56.1 ms                                                                                                                    | 51.8 ms: 1.08x faster                                                                                                          |
| xml_etree_iterparse  | 66.3 ms                                                                                                                    | 64.0 ms: 1.04x faster                                                                                                          |
| pickle               | 7.96 us                                                                                                                    | 7.71 us: 1.03x faster                                                                                                          |
| pickle_pure_python   | 208 us                                                                                                                     | 204 us: 1.02x faster                                                                                                           |
| xml_etree_parse      | 89.2 ms                                                                                                                    | 87.6 ms: 1.02x faster                                                                                                          |
| pickle_list          | 3.40 us                                                                                                                    | 3.36 us: 1.01x faster                                                                                                          |
| json_dumps           | 6.19 ms                                                                                                                    | 6.25 ms: 1.01x slower                                                                                                          |
| json_loads           | 14.3 us                                                                                                                    | 14.6 us: 1.02x slower                                                                                                          |
| unpickle_list        | 2.78 us                                                                                                                    | 2.85 us: 1.03x slower                                                                                                          |
| unpickle             | 8.57 us                                                                                                                    | 8.84 us: 1.03x slower                                                                                                          |
| Geometric mean       | (ref)                                                                                                                      | 1.04x faster                                                                                                                   |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250630-3.15.0a0-75f4059/bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json | results/bm-20250630-3.15.0a0-75f4059-JIT/bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json |
|-----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.55 ms                                                                                                                    | 5.47 ms: 1.20x faster                                                                                                          |
| django_template | 24.3 ms                                                                                                                    | 23.9 ms: 1.02x faster                                                                                                          |
| genshi_xml      | 34.3 ms                                                                                                                    | 34.7 ms: 1.01x slower                                                                                                          |
| Geometric mean  | (ref)                                                                                                                      | 1.05x faster                                                                                                                   |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | results/bm-20250630-3.15.0a0-75f4059/bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json | results/bm-20250630-3.15.0a0-75f4059-JIT/bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python       | 135 us                                                                                                                     | 109 us: 1.24x faster                                                                                                           |
| tomli_loads                | 1.38 sec                                                                                                                   | 1.14 sec: 1.21x faster                                                                                                         |
| mako                       | 6.55 ms                                                                                                                    | 5.47 ms: 1.20x faster                                                                                                          |
| scimark_fft                | 176 ms                                                                                                                     | 153 ms: 1.15x faster                                                                                                           |
| fannkuch                   | 255 ms                                                                                                                     | 225 ms: 1.13x faster                                                                                                           |
| bpe_tokeniser              | 2.92 sec                                                                                                                   | 2.59 sec: 1.12x faster                                                                                                         |
| nbody                      | 63.0 ms                                                                                                                    | 56.8 ms: 1.11x faster                                                                                                          |
| xml_etree_process          | 39.1 ms                                                                                                                    | 35.5 ms: 1.10x faster                                                                                                          |
| pyflate                    | 285 ms                                                                                                                     | 259 ms: 1.10x faster                                                                                                           |
| scimark_sparse_mat_mult    | 2.49 ms                                                                                                                    | 2.29 ms: 1.09x faster                                                                                                          |
| xml_etree_generate         | 56.1 ms                                                                                                                    | 51.8 ms: 1.08x faster                                                                                                          |
| telco                      | 4.60 ms                                                                                                                    | 4.25 ms: 1.08x faster                                                                                                          |
| k_core                     | 1.73 sec                                                                                                                   | 1.64 sec: 1.06x faster                                                                                                         |
| pprint_safe_repr           | 490 ms                                                                                                                     | 465 ms: 1.05x faster                                                                                                           |
| pprint_pformat             | 1.01 sec                                                                                                                   | 959 ms: 1.05x faster                                                                                                           |
| sqlglot_v2_parse           | 815 us                                                                                                                     | 786 us: 1.04x faster                                                                                                           |
| xml_etree_iterparse        | 66.3 ms                                                                                                                    | 64.0 ms: 1.04x faster                                                                                                          |
| crypto_pyaes               | 47.8 ms                                                                                                                    | 46.2 ms: 1.03x faster                                                                                                          |
| pickle                     | 7.96 us                                                                                                                    | 7.71 us: 1.03x faster                                                                                                          |
| connected_components       | 337 ms                                                                                                                     | 327 ms: 1.03x faster                                                                                                           |
| sqlglot_v2_transpile       | 1.02 ms                                                                                                                    | 993 us: 1.02x faster                                                                                                           |
| sqlite_synth               | 1.59 us                                                                                                                    | 1.56 us: 1.02x faster                                                                                                          |
| pickle_pure_python         | 208 us                                                                                                                     | 204 us: 1.02x faster                                                                                                           |
| django_template            | 24.3 ms                                                                                                                    | 23.9 ms: 1.02x faster                                                                                                          |
| xml_etree_parse            | 89.2 ms                                                                                                                    | 87.6 ms: 1.02x faster                                                                                                          |
| regex_compile              | 79.4 ms                                                                                                                    | 78.1 ms: 1.02x faster                                                                                                          |
| raytrace                   | 180 ms                                                                                                                     | 177 ms: 1.02x faster                                                                                                           |
| meteor_contest             | 71.8 ms                                                                                                                    | 70.7 ms: 1.01x faster                                                                                                          |
| async_tree_io_tg           | 393 ms                                                                                                                     | 388 ms: 1.01x faster                                                                                                           |
| thrift                     | 494 us                                                                                                                     | 488 us: 1.01x faster                                                                                                           |
| dulwich_log                | 40.9 ms                                                                                                                    | 40.4 ms: 1.01x faster                                                                                                          |
| pickle_list                | 3.40 us                                                                                                                    | 3.36 us: 1.01x faster                                                                                                          |
| comprehensions             | 10.9 us                                                                                                                    | 10.7 us: 1.01x faster                                                                                                          |
| shortest_path              | 364 ms                                                                                                                     | 360 ms: 1.01x faster                                                                                                           |
| async_tree_none_tg         | 170 ms                                                                                                                     | 168 ms: 1.01x faster                                                                                                           |
| logging_silent             | 55.2 ns                                                                                                                    | 54.9 ns: 1.01x faster                                                                                                          |
| bench_mp_pool              | 95.7 ms                                                                                                                    | 95.3 ms: 1.00x faster                                                                                                          |
| sqlglot_v2_normalize       | 70.6 ms                                                                                                                    | 71.2 ms: 1.01x slower                                                                                                          |
| json_dumps                 | 6.19 ms                                                                                                                    | 6.25 ms: 1.01x slower                                                                                                          |
| deepcopy_reduce            | 1.84 us                                                                                                                    | 1.87 us: 1.01x slower                                                                                                          |
| sympy_sum                  | 87.3 ms                                                                                                                    | 88.3 ms: 1.01x slower                                                                                                          |
| genshi_xml                 | 34.3 ms                                                                                                                    | 34.7 ms: 1.01x slower                                                                                                          |
| async_tree_cpu_io_mixed    | 328 ms                                                                                                                     | 333 ms: 1.01x slower                                                                                                           |
| sympy_str                  | 170 ms                                                                                                                     | 172 ms: 1.01x slower                                                                                                           |
| asyncio_websockets         | 158 ms                                                                                                                     | 160 ms: 1.02x slower                                                                                                           |
| async_tree_cpu_io_mixed_tg | 340 ms                                                                                                                     | 346 ms: 1.02x slower                                                                                                           |
| nqueens                    | 60.5 ms                                                                                                                    | 61.7 ms: 1.02x slower                                                                                                          |
| html5lib                   | 38.0 ms                                                                                                                    | 38.7 ms: 1.02x slower                                                                                                          |
| go                         | 75.5 ms                                                                                                                    | 77.0 ms: 1.02x slower                                                                                                          |
| typing_runtime_protocols   | 101 us                                                                                                                     | 103 us: 1.02x slower                                                                                                           |
| json_loads                 | 14.3 us                                                                                                                    | 14.6 us: 1.02x slower                                                                                                          |
| deepcopy                   | 168 us                                                                                                                     | 172 us: 1.02x slower                                                                                                           |
| sphinx                     | 633 ms                                                                                                                     | 646 ms: 1.02x slower                                                                                                           |
| logging_simple             | 5.99 us                                                                                                                    | 6.13 us: 1.02x slower                                                                                                          |
| generators                 | 19.4 ms                                                                                                                    | 19.9 ms: 1.02x slower                                                                                                          |
| coroutines                 | 14.4 ms                                                                                                                    | 14.8 ms: 1.03x slower                                                                                                          |
| many_optionals             | 436 us                                                                                                                     | 447 us: 1.03x slower                                                                                                           |
| unpickle_list              | 2.78 us                                                                                                                    | 2.85 us: 1.03x slower                                                                                                          |
| scimark_monte_carlo        | 40.1 ms                                                                                                                    | 41.1 ms: 1.03x slower                                                                                                          |
| chaos                      | 40.6 ms                                                                                                                    | 41.7 ms: 1.03x slower                                                                                                          |
| deepcopy_memo              | 17.6 us                                                                                                                    | 18.1 us: 1.03x slower                                                                                                          |
| mdp                        | 801 ms                                                                                                                     | 824 ms: 1.03x slower                                                                                                           |
| sqlglot_v2_optimize        | 33.7 ms                                                                                                                    | 34.7 ms: 1.03x slower                                                                                                          |
| unpack_sequence            | 36.2 ns                                                                                                                    | 37.3 ns: 1.03x slower                                                                                                          |
| hexiom                     | 4.03 ms                                                                                                                    | 4.16 ms: 1.03x slower                                                                                                          |
| unpickle                   | 8.57 us                                                                                                                    | 8.84 us: 1.03x slower                                                                                                          |
| sympy_integrate            | 12.4 ms                                                                                                                    | 12.8 ms: 1.03x slower                                                                                                          |
| float                      | 43.1 ms                                                                                                                    | 44.5 ms: 1.03x slower                                                                                                          |
| deltablue                  | 2.15 ms                                                                                                                    | 2.23 ms: 1.04x slower                                                                                                          |
| sympy_expand               | 287 ms                                                                                                                     | 298 ms: 1.04x slower                                                                                                           |
| docutils                   | 1.60 sec                                                                                                                   | 1.67 sec: 1.05x slower                                                                                                         |
| regex_effbot               | 1.50 ms                                                                                                                    | 1.57 ms: 1.05x slower                                                                                                          |
| regex_dna                  | 115 ms                                                                                                                     | 122 ms: 1.05x slower                                                                                                           |
| coverage                   | 47.6 ms                                                                                                                    | 50.4 ms: 1.06x slower                                                                                                          |
| spectral_norm              | 64.7 ms                                                                                                                    | 68.7 ms: 1.06x slower                                                                                                          |
| regex_v8                   | 13.3 ms                                                                                                                    | 14.2 ms: 1.06x slower                                                                                                          |
| scimark_sor                | 74.0 ms                                                                                                                    | 80.2 ms: 1.08x slower                                                                                                          |
| asyncio_tcp_ssl            | 1.33 sec                                                                                                                   | 1.44 sec: 1.09x slower                                                                                                         |
| async_generators           | 230 ms                                                                                                                     | 253 ms: 1.10x slower                                                                                                           |
| scimark_lu                 | 56.6 ms                                                                                                                    | 62.8 ms: 1.11x slower                                                                                                          |
| asyncio_tcp                | 433 ms                                                                                                                     | 531 ms: 1.23x slower                                                                                                           |
| Geometric mean             | (ref)                                                                                                                      | 1.00x faster                                                                                                                   |

Benchmark hidden because not significant (21): python_startup_no_site, async_tree_memoization_tg, pickle_dict, async_tree_io, async_tree_memoization, gc_traversal, python_startup, subparsers, pidigits, genshi_text, create_gc_cycles, richards, async_tree_none, richards_super, 2to3, pathlib, pycparser, bench_thread_pool, json, logging_format, pylint

- Geometric mean (including insignificant results): 1.009x faster

# HPT report

- Reliability score: 63.62% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown