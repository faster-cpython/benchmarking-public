# Results vs. 3.13.0b2

- fork: python
- ref: 68e279b37aae3019979a
- machine: windows-amd64
- commit hash: 68e279b
- commit date: 2024-07-07
- overall geometric mean: 1.02x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 214 ms: 1.03x slower                                                       |
| html5lib       | 35.0 ms                                                         | 36.4 ms: 1.04x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 80.9 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                           | 1.02x slower                                                               |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg          | 605 ms                                                          | 516 ms: 1.17x faster                                                       |
| async_tree_io             | 588 ms                                                          | 522 ms: 1.12x faster                                                       |
| async_tree_none_tg        | 202 ms                                                          | 186 ms: 1.09x faster                                                       |
| async_tree_memoization_tg | 258 ms                                                          | 241 ms: 1.07x faster                                                       |
| async_tree_none           | 218 ms                                                          | 205 ms: 1.06x faster                                                       |
| async_tree_memoization    | 264 ms                                                          | 250 ms: 1.06x faster                                                       |
| async_tree_cpu_io_mixed   | 389 ms                                                          | 380 ms: 1.02x faster                                                       |
| Geometric mean            | (ref)                                                           | 1.07x faster                                                               |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 150 ms: 1.00x slower                                                       |
| float          | 49.7 ms                                                         | 52.6 ms: 1.06x slower                                                      |
| nbody          | 67.6 ms                                                         | 73.2 ms: 1.08x slower                                                      |
| Geometric mean | (ref)                                                           | 1.05x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 78.0 ms                                                         | 78.5 ms: 1.01x slower                                                      |
| regex_dna      | 119 ms                                                          | 122 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                           | 1.03x slower                                                               |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 14.2 us                                                         | 14.0 us: 1.01x faster                                                      |
| json_dumps           | 5.61 ms                                                         | 5.66 ms: 1.01x slower                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 92.4 ms: 1.02x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 63.8 ms: 1.02x slower                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 55.0 ms: 1.03x slower                                                      |
| xml_etree_process    | 36.4 ms                                                         | 37.8 ms: 1.04x slower                                                      |
| pickle_pure_python   | 175 us                                                          | 186 us: 1.06x slower                                                       |
| tomli_loads          | 1.35 sec                                                        | 1.47 sec: 1.09x slower                                                     |
| unpickle_pure_python | 122 us                                                          | 133 us: 1.09x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.04x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 20.9 ms: 1.03x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 16.7 ms: 1.03x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.03x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 6.59 ms: 1.04x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 33.1 ms: 1.05x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 15.1 ms: 1.05x slower                                                      |
| django_template | 21.7 ms                                                         | 23.2 ms: 1.07x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.05x slower                                                               |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                    | 8.11 ms                                                         | 509 us: 15.92x faster                                                      |
| deepcopy                  | 220 us                                                          | 170 us: 1.29x faster                                                       |
| deepcopy_memo             | 22.1 us                                                         | 18.6 us: 1.19x faster                                                      |
| async_tree_io_tg          | 605 ms                                                          | 516 ms: 1.17x faster                                                       |
| deepcopy_reduce           | 1.99 us                                                         | 1.76 us: 1.13x faster                                                      |
| async_tree_io             | 588 ms                                                          | 522 ms: 1.12x faster                                                       |
| async_tree_none_tg        | 202 ms                                                          | 186 ms: 1.09x faster                                                       |
| json                      | 3.19 ms                                                         | 2.94 ms: 1.08x faster                                                      |
| async_tree_memoization_tg | 258 ms                                                          | 241 ms: 1.07x faster                                                       |
| async_tree_none           | 218 ms                                                          | 205 ms: 1.06x faster                                                       |
| async_tree_memoization    | 264 ms                                                          | 250 ms: 1.06x faster                                                       |
| bench_thread_pool         | 768 us                                                          | 750 us: 1.02x faster                                                       |
| async_tree_cpu_io_mixed   | 389 ms                                                          | 380 ms: 1.02x faster                                                       |
| spectral_norm             | 63.7 ms                                                         | 62.3 ms: 1.02x faster                                                      |
| json_loads                | 14.2 us                                                         | 14.0 us: 1.01x faster                                                      |
| tornado_http              | 81.8 ms                                                         | 80.9 ms: 1.01x faster                                                      |
| telco                     | 4.67 ms                                                         | 4.69 ms: 1.00x slower                                                      |
| pidigits                  | 150 ms                                                          | 150 ms: 1.00x slower                                                       |
| sympy_sum                 | 84.4 ms                                                         | 84.9 ms: 1.01x slower                                                      |
| regex_compile             | 78.0 ms                                                         | 78.5 ms: 1.01x slower                                                      |
| json_dumps                | 5.61 ms                                                         | 5.66 ms: 1.01x slower                                                      |
| richards                  | 26.7 ms                                                         | 26.9 ms: 1.01x slower                                                      |
| sqlglot_normalize         | 173 ms                                                          | 175 ms: 1.01x slower                                                       |
| sqlglot_optimize          | 32.7 ms                                                         | 33.1 ms: 1.01x slower                                                      |
| richards_super            | 30.2 ms                                                         | 30.6 ms: 1.02x slower                                                      |
| xml_etree_parse           | 90.9 ms                                                         | 92.4 ms: 1.02x slower                                                      |
| logging_format            | 6.22 us                                                         | 6.33 us: 1.02x slower                                                      |
| comprehensions            | 10.4 us                                                         | 10.6 us: 1.02x slower                                                      |
| logging_simple            | 5.78 us                                                         | 5.89 us: 1.02x slower                                                      |
| sympy_integrate           | 12.2 ms                                                         | 12.5 ms: 1.02x slower                                                      |
| chaos                     | 38.4 ms                                                         | 39.2 ms: 1.02x slower                                                      |
| xml_etree_iterparse       | 62.3 ms                                                         | 63.8 ms: 1.02x slower                                                      |
| regex_dna                 | 119 ms                                                          | 122 ms: 1.02x slower                                                       |
| nqueens                   | 56.7 ms                                                         | 58.2 ms: 1.03x slower                                                      |
| raytrace                  | 162 ms                                                          | 167 ms: 1.03x slower                                                       |
| crypto_pyaes              | 45.5 ms                                                         | 46.8 ms: 1.03x slower                                                      |
| sympy_str                 | 159 ms                                                          | 164 ms: 1.03x slower                                                       |
| python_startup            | 20.3 ms                                                         | 20.9 ms: 1.03x slower                                                      |
| sympy_expand              | 271 ms                                                          | 278 ms: 1.03x slower                                                       |
| python_startup_no_site    | 16.2 ms                                                         | 16.7 ms: 1.03x slower                                                      |
| xml_etree_generate        | 53.2 ms                                                         | 55.0 ms: 1.03x slower                                                      |
| 2to3                      | 207 ms                                                          | 214 ms: 1.03x slower                                                       |
| mako                      | 6.36 ms                                                         | 6.59 ms: 1.04x slower                                                      |
| xml_etree_process         | 36.4 ms                                                         | 37.8 ms: 1.04x slower                                                      |
| coroutines                | 12.8 ms                                                         | 13.3 ms: 1.04x slower                                                      |
| html5lib                  | 35.0 ms                                                         | 36.4 ms: 1.04x slower                                                      |
| scimark_sor               | 75.3 ms                                                         | 78.4 ms: 1.04x slower                                                      |
| go                        | 82.1 ms                                                         | 85.7 ms: 1.04x slower                                                      |
| async_generators          | 223 ms                                                          | 233 ms: 1.05x slower                                                       |
| pprint_pformat            | 966 ms                                                          | 1.01 sec: 1.05x slower                                                     |
| hexiom                    | 3.72 ms                                                         | 3.90 ms: 1.05x slower                                                      |
| pprint_safe_repr          | 474 ms                                                          | 496 ms: 1.05x slower                                                       |
| genshi_xml                | 31.6 ms                                                         | 33.1 ms: 1.05x slower                                                      |
| pyflate                   | 279 ms                                                          | 293 ms: 1.05x slower                                                       |
| genshi_text               | 14.4 ms                                                         | 15.1 ms: 1.05x slower                                                      |
| scimark_sparse_mat_mult   | 2.50 ms                                                         | 2.64 ms: 1.05x slower                                                      |
| deltablue                 | 1.88 ms                                                         | 1.99 ms: 1.05x slower                                                      |
| scimark_lu                | 56.6 ms                                                         | 59.8 ms: 1.06x slower                                                      |
| float                     | 49.7 ms                                                         | 52.6 ms: 1.06x slower                                                      |
| pickle_pure_python        | 175 us                                                          | 186 us: 1.06x slower                                                       |
| django_template           | 21.7 ms                                                         | 23.2 ms: 1.07x slower                                                      |
| meteor_contest            | 69.9 ms                                                         | 74.9 ms: 1.07x slower                                                      |
| generators                | 19.6 ms                                                         | 21.0 ms: 1.07x slower                                                      |
| sqlglot_transpile         | 955 us                                                          | 1.03 ms: 1.08x slower                                                      |
| asyncio_tcp_ssl           | 1.48 sec                                                        | 1.60 sec: 1.08x slower                                                     |
| scimark_fft               | 171 ms                                                          | 185 ms: 1.08x slower                                                       |
| nbody                     | 67.6 ms                                                         | 73.2 ms: 1.08x slower                                                      |
| tomli_loads               | 1.35 sec                                                        | 1.47 sec: 1.09x slower                                                     |
| sqlglot_parse             | 748 us                                                          | 813 us: 1.09x slower                                                       |
| coverage                  | 42.1 ms                                                         | 45.8 ms: 1.09x slower                                                      |
| unpickle_pure_python      | 122 us                                                          | 133 us: 1.09x slower                                                       |
| logging_silent            | 52.9 ns                                                         | 57.9 ns: 1.09x slower                                                      |
| scimark_monte_carlo       | 39.1 ms                                                         | 43.6 ms: 1.11x slower                                                      |
| fannkuch                  | 243 ms                                                          | 273 ms: 1.12x slower                                                       |
| mdp                       | 1.31 sec                                                        | 1.50 sec: 1.14x slower                                                     |
| Geometric mean            | (ref)                                                           | 1.02x faster                                                               |

Benchmark hidden because not significant (12): pycparser, create_gc_cycles, gc_traversal, pathlib, async_tree_cpu_io_mixed_tg, pylint, docutils, bench_mp_pool, typing_runtime_protocols, regex_effbot, asyncio_tcp, regex_v8
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown