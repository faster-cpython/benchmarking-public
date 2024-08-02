# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: no_cold_exits
- machine: windows-amd64
- commit hash: f837cc6
- commit date: 2024-06-10
- overall geometric mean: 1.00x faster
- HPT reliability: 99.94%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240610-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 230 ms: 1.11x slower                                                      |
| docutils       | 1.63 sec                                                        | 1.77 sec: 1.09x slower                                                    |
| html5lib       | 35.0 ms                                                         | 37.2 ms: 1.06x slower                                                     |
| tornado_http   | 81.8 ms                                                         | 85.5 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                           | 1.08x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240610-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|---------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io_tg          | 605 ms                                                          | 619 ms: 1.02x slower                                                      |
| async_tree_cpu_io_mixed   | 389 ms                                                          | 402 ms: 1.03x slower                                                      |
| async_tree_io             | 588 ms                                                          | 610 ms: 1.04x slower                                                      |
| async_tree_memoization_tg | 258 ms                                                          | 271 ms: 1.05x slower                                                      |
| async_tree_none_tg        | 202 ms                                                          | 213 ms: 1.06x slower                                                      |
| async_tree_memoization    | 264 ms                                                          | 280 ms: 1.06x slower                                                      |
| async_tree_none           | 218 ms                                                          | 232 ms: 1.06x slower                                                      |
| Geometric mean            | (ref)                                                           | 1.04x slower                                                              |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240610-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 56.2 ms: 1.20x faster                                                     |
| float          | 49.7 ms                                                         | 44.0 ms: 1.13x faster                                                     |
| pidigits       | 150 ms                                                          | 150 ms: 1.00x slower                                                      |
| Geometric mean | (ref)                                                           | 1.11x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240610-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 15.8 ms                                                         | 14.4 ms: 1.10x faster                                                     |
| regex_dna      | 119 ms                                                          | 116 ms: 1.02x faster                                                      |
| regex_effbot   | 1.58 ms                                                         | 1.56 ms: 1.02x faster                                                     |
| regex_compile  | 78.0 ms                                                         | 88.3 ms: 1.13x slower                                                     |
| Geometric mean | (ref)                                                           | 1.00x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240610-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 1.35 sec                                                        | 1.22 sec: 1.11x faster                                                    |
| pickle_dict          | 18.1 us                                                         | 17.6 us: 1.03x faster                                                     |
| pickle_list          | 2.90 us                                                         | 2.82 us: 1.03x faster                                                     |
| xml_etree_generate   | 53.2 ms                                                         | 51.7 ms: 1.03x faster                                                     |
| pickle_pure_python   | 175 us                                                          | 172 us: 1.02x faster                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 92.5 ms: 1.02x slower                                                     |
| pickle               | 7.11 us                                                         | 7.25 us: 1.02x slower                                                     |
| xml_etree_iterparse  | 62.3 ms                                                         | 64.2 ms: 1.03x slower                                                     |
| unpickle_pure_python | 122 us                                                          | 128 us: 1.05x slower                                                      |
| unpickle             | 8.40 us                                                         | 8.81 us: 1.05x slower                                                     |
| unpickle_list        | 2.62 us                                                         | 2.87 us: 1.10x slower                                                     |
| Geometric mean       | (ref)                                                           | 1.00x slower                                                              |

Benchmark hidden because not significant (3): xml_etree_process, json_dumps, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240610-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 20.5 ms: 1.01x slower                                                     |
| python_startup_no_site | 16.2 ms                                                         | 17.0 ms: 1.05x slower                                                     |
| Geometric mean         | (ref)                                                           | 1.03x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240610-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 5.25 ms: 1.21x faster                                                     |
| django_template | 21.7 ms                                                         | 26.1 ms: 1.20x slower                                                     |
| genshi_text     | 14.4 ms                                                         | 18.0 ms: 1.25x slower                                                     |
| genshi_xml      | 31.6 ms                                                         | 45.7 ms: 1.45x slower                                                     |
| Geometric mean  | (ref)                                                           | 1.16x slower                                                              |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240610-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|---------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| thrift                    | 8.11 ms                                                         | 511 us: 15.85x faster                                                     |
| spectral_norm             | 63.7 ms                                                         | 45.4 ms: 1.40x faster                                                     |
| mako                      | 6.36 ms                                                         | 5.25 ms: 1.21x faster                                                     |
| nbody                     | 67.6 ms                                                         | 56.2 ms: 1.20x faster                                                     |
| scimark_sparse_mat_mult   | 2.50 ms                                                         | 2.14 ms: 1.17x faster                                                     |
| scimark_fft               | 171 ms                                                          | 148 ms: 1.15x faster                                                      |
| float                     | 49.7 ms                                                         | 44.0 ms: 1.13x faster                                                     |
| crypto_pyaes              | 45.5 ms                                                         | 41.0 ms: 1.11x faster                                                     |
| tomli_loads               | 1.35 sec                                                        | 1.22 sec: 1.11x faster                                                    |
| regex_v8                  | 15.8 ms                                                         | 14.4 ms: 1.10x faster                                                     |
| fannkuch                  | 243 ms                                                          | 223 ms: 1.09x faster                                                      |
| pyflate                   | 279 ms                                                          | 259 ms: 1.08x faster                                                      |
| deepcopy_memo             | 22.1 us                                                         | 20.7 us: 1.07x faster                                                     |
| json                      | 3.19 ms                                                         | 3.03 ms: 1.05x faster                                                     |
| asyncio_tcp_ssl           | 1.48 sec                                                        | 1.42 sec: 1.05x faster                                                    |
| pickle_dict               | 18.1 us                                                         | 17.6 us: 1.03x faster                                                     |
| pickle_list               | 2.90 us                                                         | 2.82 us: 1.03x faster                                                     |
| xml_etree_generate        | 53.2 ms                                                         | 51.7 ms: 1.03x faster                                                     |
| scimark_monte_carlo       | 39.1 ms                                                         | 38.2 ms: 1.02x faster                                                     |
| regex_dna                 | 119 ms                                                          | 116 ms: 1.02x faster                                                      |
| comprehensions            | 10.4 us                                                         | 10.2 us: 1.02x faster                                                     |
| regex_effbot              | 1.58 ms                                                         | 1.56 ms: 1.02x faster                                                     |
| pickle_pure_python        | 175 us                                                          | 172 us: 1.02x faster                                                      |
| pprint_safe_repr          | 474 ms                                                          | 467 ms: 1.02x faster                                                      |
| pprint_pformat            | 966 ms                                                          | 954 ms: 1.01x faster                                                      |
| pathlib                   | 75.9 ms                                                         | 75.3 ms: 1.01x faster                                                     |
| sqlite_synth              | 1.60 us                                                         | 1.59 us: 1.01x faster                                                     |
| pidigits                  | 150 ms                                                          | 150 ms: 1.00x slower                                                      |
| gc_traversal              | 1.55 ms                                                         | 1.57 ms: 1.01x slower                                                     |
| python_startup            | 20.3 ms                                                         | 20.5 ms: 1.01x slower                                                     |
| xml_etree_parse           | 90.9 ms                                                         | 92.5 ms: 1.02x slower                                                     |
| pickle                    | 7.11 us                                                         | 7.25 us: 1.02x slower                                                     |
| logging_format            | 6.22 us                                                         | 6.36 us: 1.02x slower                                                     |
| create_gc_cycles          | 888 us                                                          | 907 us: 1.02x slower                                                      |
| async_tree_io_tg          | 605 ms                                                          | 619 ms: 1.02x slower                                                      |
| logging_simple            | 5.78 us                                                         | 5.92 us: 1.02x slower                                                     |
| xml_etree_iterparse       | 62.3 ms                                                         | 64.2 ms: 1.03x slower                                                     |
| async_tree_cpu_io_mixed   | 389 ms                                                          | 402 ms: 1.03x slower                                                      |
| coroutines                | 12.8 ms                                                         | 13.2 ms: 1.03x slower                                                     |
| chaos                     | 38.4 ms                                                         | 39.7 ms: 1.03x slower                                                     |
| logging_silent            | 52.9 ns                                                         | 54.8 ns: 1.03x slower                                                     |
| async_tree_io             | 588 ms                                                          | 610 ms: 1.04x slower                                                      |
| richards                  | 26.7 ms                                                         | 27.8 ms: 1.04x slower                                                     |
| meteor_contest            | 69.9 ms                                                         | 72.7 ms: 1.04x slower                                                     |
| richards_super            | 30.2 ms                                                         | 31.4 ms: 1.04x slower                                                     |
| tornado_http              | 81.8 ms                                                         | 85.5 ms: 1.04x slower                                                     |
| python_startup_no_site    | 16.2 ms                                                         | 17.0 ms: 1.05x slower                                                     |
| unpickle_pure_python      | 122 us                                                          | 128 us: 1.05x slower                                                      |
| unpickle                  | 8.40 us                                                         | 8.81 us: 1.05x slower                                                     |
| coverage                  | 42.1 ms                                                         | 44.1 ms: 1.05x slower                                                     |
| async_tree_memoization_tg | 258 ms                                                          | 271 ms: 1.05x slower                                                      |
| bench_mp_pool             | 64.8 ms                                                         | 68.4 ms: 1.06x slower                                                     |
| async_tree_none_tg        | 202 ms                                                          | 213 ms: 1.06x slower                                                      |
| deepcopy_reduce           | 1.99 us                                                         | 2.11 us: 1.06x slower                                                     |
| async_tree_memoization    | 264 ms                                                          | 280 ms: 1.06x slower                                                      |
| html5lib                  | 35.0 ms                                                         | 37.2 ms: 1.06x slower                                                     |
| bench_thread_pool         | 768 us                                                          | 817 us: 1.06x slower                                                      |
| async_tree_none           | 218 ms                                                          | 232 ms: 1.06x slower                                                      |
| sqlglot_parse             | 748 us                                                          | 799 us: 1.07x slower                                                      |
| mdp                       | 1.31 sec                                                        | 1.40 sec: 1.07x slower                                                    |
| nqueens                   | 56.7 ms                                                         | 60.8 ms: 1.07x slower                                                     |
| raytrace                  | 162 ms                                                          | 175 ms: 1.08x slower                                                      |
| deepcopy                  | 220 us                                                          | 237 us: 1.08x slower                                                      |
| generators                | 19.6 ms                                                         | 21.1 ms: 1.08x slower                                                     |
| sqlglot_transpile         | 955 us                                                          | 1.03 ms: 1.08x slower                                                     |
| docutils                  | 1.63 sec                                                        | 1.77 sec: 1.09x slower                                                    |
| unpickle_list             | 2.62 us                                                         | 2.87 us: 1.10x slower                                                     |
| sympy_sum                 | 84.4 ms                                                         | 93.3 ms: 1.11x slower                                                     |
| scimark_sor               | 75.3 ms                                                         | 83.8 ms: 1.11x slower                                                     |
| 2to3                      | 207 ms                                                          | 230 ms: 1.11x slower                                                      |
| sqlglot_optimize          | 32.7 ms                                                         | 36.6 ms: 1.12x slower                                                     |
| sympy_str                 | 159 ms                                                          | 178 ms: 1.12x slower                                                      |
| go                        | 82.1 ms                                                         | 92.4 ms: 1.13x slower                                                     |
| regex_compile             | 78.0 ms                                                         | 88.3 ms: 1.13x slower                                                     |
| typing_runtime_protocols  | 101 us                                                          | 115 us: 1.14x slower                                                      |
| sympy_expand              | 271 ms                                                          | 309 ms: 1.14x slower                                                      |
| sympy_integrate           | 12.2 ms                                                         | 14.0 ms: 1.14x slower                                                     |
| async_generators          | 223 ms                                                          | 257 ms: 1.15x slower                                                      |
| pylint                    | 205 ms                                                          | 236 ms: 1.15x slower                                                      |
| django_template           | 21.7 ms                                                         | 26.1 ms: 1.20x slower                                                     |
| hexiom                    | 3.72 ms                                                         | 4.60 ms: 1.24x slower                                                     |
| deltablue                 | 1.88 ms                                                         | 2.34 ms: 1.24x slower                                                     |
| scimark_lu                | 56.6 ms                                                         | 70.4 ms: 1.24x slower                                                     |
| genshi_text               | 14.4 ms                                                         | 18.0 ms: 1.25x slower                                                     |
| genshi_xml                | 31.6 ms                                                         | 45.7 ms: 1.45x slower                                                     |
| Geometric mean            | (ref)                                                           | 1.00x faster                                                              |

Benchmark hidden because not significant (7): xml_etree_process, asyncio_tcp, pycparser, json_dumps, telco, json_loads, async_tree_cpu_io_mixed_tg
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, sqlglot_normalize

# HPT report

- Reliability score: 99.94% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown