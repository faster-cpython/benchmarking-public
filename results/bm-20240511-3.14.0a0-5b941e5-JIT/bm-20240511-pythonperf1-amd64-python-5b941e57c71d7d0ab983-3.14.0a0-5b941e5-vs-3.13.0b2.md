# Results vs. 3.13.0b2

- fork: python
- ref: 5b941e57c71d7d0ab983
- machine: windows-amd64
- commit hash: 5b941e5
- commit date: 2024-05-11
- overall geometric mean: 1.00x slower
- HPT reliability: 99.89%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 232 ms: 1.12x slower                                                       |
| chameleon      | 4.80 ms                                                         | 4.99 ms: 1.04x slower                                                      |
| docutils       | 1.63 sec                                                        | 1.76 sec: 1.08x slower                                                     |
| html5lib       | 35.0 ms                                                         | 37.0 ms: 1.06x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 85.4 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                           | 1.07x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg          | 605 ms                                                          | 619 ms: 1.02x slower                                                       |
| async_tree_none           | 218 ms                                                          | 226 ms: 1.04x slower                                                       |
| async_tree_memoization    | 264 ms                                                          | 275 ms: 1.04x slower                                                       |
| async_tree_memoization_tg | 258 ms                                                          | 270 ms: 1.05x slower                                                       |
| async_tree_none_tg        | 202 ms                                                          | 213 ms: 1.06x slower                                                       |
| Geometric mean            | (ref)                                                           | 1.03x slower                                                               |

Benchmark hidden because not significant (3): async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 49.9 ms: 1.36x faster                                                      |
| float          | 49.7 ms                                                         | 43.4 ms: 1.15x faster                                                      |
| Geometric mean | (ref)                                                           | 1.16x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                          | 114 ms: 1.04x faster                                                       |
| regex_effbot   | 1.58 ms                                                         | 1.56 ms: 1.02x faster                                                      |
| regex_compile  | 78.0 ms                                                         | 86.6 ms: 1.11x slower                                                      |
| Geometric mean | (ref)                                                           | 1.00x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.35 sec                                                        | 1.23 sec: 1.10x faster                                                     |
| xml_etree_generate   | 53.2 ms                                                         | 51.1 ms: 1.04x faster                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 59.9 ms: 1.04x faster                                                      |
| pickle_list          | 2.90 us                                                         | 2.80 us: 1.04x faster                                                      |
| pickle_dict          | 18.1 us                                                         | 17.5 us: 1.04x faster                                                      |
| pickle_pure_python   | 175 us                                                          | 172 us: 1.02x faster                                                       |
| xml_etree_process    | 36.4 ms                                                         | 36.1 ms: 1.01x faster                                                      |
| json_dumps           | 5.61 ms                                                         | 5.65 ms: 1.01x slower                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 91.6 ms: 1.01x slower                                                      |
| json_loads           | 14.2 us                                                         | 14.3 us: 1.01x slower                                                      |
| unpickle_pure_python | 122 us                                                          | 124 us: 1.02x slower                                                       |
| pickle               | 7.11 us                                                         | 7.35 us: 1.03x slower                                                      |
| unpickle             | 8.40 us                                                         | 8.69 us: 1.03x slower                                                      |
| unpickle_list        | 2.62 us                                                         | 2.88 us: 1.10x slower                                                      |
| Geometric mean       | (ref)                                                           | 1.00x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 22.0 ms: 1.08x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 18.2 ms: 1.12x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 4.94 ms: 1.29x faster                                                      |
| django_template | 21.7 ms                                                         | 25.4 ms: 1.17x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 17.8 ms: 1.24x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 44.8 ms: 1.42x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.12x slower                                                               |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                    | 8.11 ms                                                         | 533 us: 15.20x faster                                                      |
| spectral_norm             | 63.7 ms                                                         | 44.9 ms: 1.42x faster                                                      |
| nbody                     | 67.6 ms                                                         | 49.9 ms: 1.36x faster                                                      |
| mako                      | 6.36 ms                                                         | 4.94 ms: 1.29x faster                                                      |
| scimark_sparse_mat_mult   | 2.50 ms                                                         | 2.14 ms: 1.17x faster                                                      |
| float                     | 49.7 ms                                                         | 43.4 ms: 1.15x faster                                                      |
| scimark_fft               | 171 ms                                                          | 150 ms: 1.14x faster                                                       |
| crypto_pyaes              | 45.5 ms                                                         | 40.8 ms: 1.12x faster                                                      |
| tomli_loads               | 1.35 sec                                                        | 1.23 sec: 1.10x faster                                                     |
| fannkuch                  | 243 ms                                                          | 223 ms: 1.09x faster                                                       |
| deepcopy_memo             | 22.1 us                                                         | 20.5 us: 1.08x faster                                                      |
| pyflate                   | 279 ms                                                          | 262 ms: 1.06x faster                                                       |
| json                      | 3.19 ms                                                         | 3.01 ms: 1.06x faster                                                      |
| pprint_safe_repr          | 474 ms                                                          | 450 ms: 1.05x faster                                                       |
| pprint_pformat            | 966 ms                                                          | 924 ms: 1.05x faster                                                       |
| xml_etree_generate        | 53.2 ms                                                         | 51.1 ms: 1.04x faster                                                      |
| xml_etree_iterparse       | 62.3 ms                                                         | 59.9 ms: 1.04x faster                                                      |
| regex_dna                 | 119 ms                                                          | 114 ms: 1.04x faster                                                       |
| pickle_list               | 2.90 us                                                         | 2.80 us: 1.04x faster                                                      |
| pickle_dict               | 18.1 us                                                         | 17.5 us: 1.04x faster                                                      |
| scimark_monte_carlo       | 39.1 ms                                                         | 37.9 ms: 1.03x faster                                                      |
| pickle_pure_python        | 175 us                                                          | 172 us: 1.02x faster                                                       |
| regex_effbot              | 1.58 ms                                                         | 1.56 ms: 1.02x faster                                                      |
| comprehensions            | 10.4 us                                                         | 10.3 us: 1.01x faster                                                      |
| xml_etree_process         | 36.4 ms                                                         | 36.1 ms: 1.01x faster                                                      |
| sqlite_synth              | 1.60 us                                                         | 1.58 us: 1.01x faster                                                      |
| json_dumps                | 5.61 ms                                                         | 5.65 ms: 1.01x slower                                                      |
| gc_traversal              | 1.55 ms                                                         | 1.57 ms: 1.01x slower                                                      |
| xml_etree_parse           | 90.9 ms                                                         | 91.6 ms: 1.01x slower                                                      |
| json_loads                | 14.2 us                                                         | 14.3 us: 1.01x slower                                                      |
| logging_format            | 6.22 us                                                         | 6.31 us: 1.01x slower                                                      |
| logging_simple            | 5.78 us                                                         | 5.88 us: 1.02x slower                                                      |
| create_gc_cycles          | 888 us                                                          | 906 us: 1.02x slower                                                       |
| unpickle_pure_python      | 122 us                                                          | 124 us: 1.02x slower                                                       |
| deepcopy_reduce           | 1.99 us                                                         | 2.04 us: 1.02x slower                                                      |
| async_tree_io_tg          | 605 ms                                                          | 619 ms: 1.02x slower                                                       |
| chaos                     | 38.4 ms                                                         | 39.4 ms: 1.03x slower                                                      |
| logging_silent            | 52.9 ns                                                         | 54.5 ns: 1.03x slower                                                      |
| pickle                    | 7.11 us                                                         | 7.35 us: 1.03x slower                                                      |
| unpickle                  | 8.40 us                                                         | 8.69 us: 1.03x slower                                                      |
| async_tree_none           | 218 ms                                                          | 226 ms: 1.04x slower                                                       |
| chameleon                 | 4.80 ms                                                         | 4.99 ms: 1.04x slower                                                      |
| async_tree_memoization    | 264 ms                                                          | 275 ms: 1.04x slower                                                       |
| tornado_http              | 81.8 ms                                                         | 85.4 ms: 1.04x slower                                                      |
| coroutines                | 12.8 ms                                                         | 13.3 ms: 1.04x slower                                                      |
| async_tree_memoization_tg | 258 ms                                                          | 270 ms: 1.05x slower                                                       |
| meteor_contest            | 69.9 ms                                                         | 73.2 ms: 1.05x slower                                                      |
| pathlib                   | 75.9 ms                                                         | 79.6 ms: 1.05x slower                                                      |
| async_tree_none_tg        | 202 ms                                                          | 213 ms: 1.06x slower                                                       |
| html5lib                  | 35.0 ms                                                         | 37.0 ms: 1.06x slower                                                      |
| deepcopy                  | 220 us                                                          | 233 us: 1.06x slower                                                       |
| richards                  | 26.7 ms                                                         | 28.5 ms: 1.07x slower                                                      |
| richards_super            | 30.2 ms                                                         | 32.3 ms: 1.07x slower                                                      |
| coverage                  | 42.1 ms                                                         | 45.1 ms: 1.07x slower                                                      |
| sqlglot_parse             | 748 us                                                          | 803 us: 1.07x slower                                                       |
| nqueens                   | 56.7 ms                                                         | 61.1 ms: 1.08x slower                                                      |
| python_startup            | 20.3 ms                                                         | 22.0 ms: 1.08x slower                                                      |
| bench_thread_pool         | 768 us                                                          | 832 us: 1.08x slower                                                       |
| docutils                  | 1.63 sec                                                        | 1.76 sec: 1.08x slower                                                     |
| sqlglot_transpile         | 955 us                                                          | 1.04 ms: 1.08x slower                                                      |
| bench_mp_pool             | 64.8 ms                                                         | 70.5 ms: 1.09x slower                                                      |
| scimark_sor               | 75.3 ms                                                         | 82.6 ms: 1.10x slower                                                      |
| unpickle_list             | 2.62 us                                                         | 2.88 us: 1.10x slower                                                      |
| raytrace                  | 162 ms                                                          | 179 ms: 1.10x slower                                                       |
| sympy_sum                 | 84.4 ms                                                         | 93.6 ms: 1.11x slower                                                      |
| regex_compile             | 78.0 ms                                                         | 86.6 ms: 1.11x slower                                                      |
| typing_runtime_protocols  | 101 us                                                          | 112 us: 1.11x slower                                                       |
| sympy_str                 | 159 ms                                                          | 178 ms: 1.12x slower                                                       |
| 2to3                      | 207 ms                                                          | 232 ms: 1.12x slower                                                       |
| mdp                       | 1.31 sec                                                        | 1.47 sec: 1.12x slower                                                     |
| generators                | 19.6 ms                                                         | 22.0 ms: 1.12x slower                                                      |
| python_startup_no_site    | 16.2 ms                                                         | 18.2 ms: 1.12x slower                                                      |
| go                        | 82.1 ms                                                         | 92.6 ms: 1.13x slower                                                      |
| sqlglot_optimize          | 32.7 ms                                                         | 37.1 ms: 1.13x slower                                                      |
| sympy_expand              | 271 ms                                                          | 309 ms: 1.14x slower                                                       |
| sympy_integrate           | 12.2 ms                                                         | 14.0 ms: 1.15x slower                                                      |
| asyncio_tcp               | 471 ms                                                          | 545 ms: 1.16x slower                                                       |
| async_generators          | 223 ms                                                          | 259 ms: 1.16x slower                                                       |
| pylint                    | 205 ms                                                          | 238 ms: 1.16x slower                                                       |
| django_template           | 21.7 ms                                                         | 25.4 ms: 1.17x slower                                                      |
| scimark_lu                | 56.6 ms                                                         | 67.5 ms: 1.19x slower                                                      |
| deltablue                 | 1.88 ms                                                         | 2.32 ms: 1.23x slower                                                      |
| genshi_text               | 14.4 ms                                                         | 17.8 ms: 1.24x slower                                                      |
| hexiom                    | 3.72 ms                                                         | 4.65 ms: 1.25x slower                                                      |
| genshi_xml                | 31.6 ms                                                         | 44.8 ms: 1.42x slower                                                      |
| Geometric mean            | (ref)                                                           | 1.00x slower                                                               |

Benchmark hidden because not significant (9): regex_v8, telco, pidigits, flaskblogging, pycparser, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, asyncio_tcp_ssl
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, dulwich_log, mypy2, sqlglot_normalize

# HPT report

- Reliability score: 99.89% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown