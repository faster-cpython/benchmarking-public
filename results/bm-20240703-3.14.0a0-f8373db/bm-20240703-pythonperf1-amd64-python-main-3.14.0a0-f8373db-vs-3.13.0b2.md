# Results vs. 3.13.0b2

- fork: python
- ref: main
- machine: windows-amd64
- commit hash: f8373db
- commit date: 2024-07-03
- overall geometric mean: 1.01x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-pythonperf1-amd64-python-main-3.14.0a0-f8373db |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 216 ms: 1.04x slower                                       |
| html5lib       | 35.0 ms                                                         | 36.8 ms: 1.05x slower                                      |
| tornado_http   | 81.8 ms                                                         | 80.2 ms: 1.02x faster                                      |
| Geometric mean | (ref)                                                           | 1.02x slower                                               |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-pythonperf1-amd64-python-main-3.14.0a0-f8373db |
|---------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_io_tg          | 605 ms                                                          | 512 ms: 1.18x faster                                       |
| async_tree_io             | 588 ms                                                          | 523 ms: 1.12x faster                                       |
| async_tree_none_tg        | 202 ms                                                          | 185 ms: 1.09x faster                                       |
| async_tree_memoization_tg | 258 ms                                                          | 240 ms: 1.07x faster                                       |
| async_tree_none           | 218 ms                                                          | 204 ms: 1.07x faster                                       |
| async_tree_memoization    | 264 ms                                                          | 249 ms: 1.06x faster                                       |
| async_tree_cpu_io_mixed   | 389 ms                                                          | 381 ms: 1.02x faster                                       |
| Geometric mean            | (ref)                                                           | 1.08x faster                                               |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-pythonperf1-amd64-python-main-3.14.0a0-f8373db |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 49.7 ms                                                         | 54.0 ms: 1.09x slower                                      |
| nbody          | 67.6 ms                                                         | 73.6 ms: 1.09x slower                                      |
| Geometric mean | (ref)                                                           | 1.06x slower                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-pythonperf1-amd64-python-main-3.14.0a0-f8373db |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 78.0 ms                                                         | 80.2 ms: 1.03x slower                                      |
| regex_effbot   | 1.58 ms                                                         | 1.64 ms: 1.04x slower                                      |
| regex_dna      | 119 ms                                                          | 125 ms: 1.05x slower                                       |
| Geometric mean | (ref)                                                           | 1.02x slower                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-pythonperf1-amd64-python-main-3.14.0a0-f8373db |
|----------------------|:---------------------------------------------------------------:|:----------------------------------------------------------:|
| json_loads           | 14.2 us                                                         | 14.3 us: 1.01x slower                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 63.7 ms: 1.02x slower                                      |
| xml_etree_parse      | 90.9 ms                                                         | 93.1 ms: 1.02x slower                                      |
| json_dumps           | 5.61 ms                                                         | 5.80 ms: 1.03x slower                                      |
| xml_etree_generate   | 53.2 ms                                                         | 55.7 ms: 1.05x slower                                      |
| xml_etree_process    | 36.4 ms                                                         | 38.4 ms: 1.05x slower                                      |
| pickle_pure_python   | 175 us                                                          | 189 us: 1.08x slower                                       |
| tomli_loads          | 1.35 sec                                                        | 1.48 sec: 1.10x slower                                     |
| unpickle_pure_python | 122 us                                                          | 135 us: 1.10x slower                                       |
| Geometric mean       | (ref)                                                           | 1.05x slower                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-pythonperf1-amd64-python-main-3.14.0a0-f8373db |
|------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 20.9 ms: 1.03x slower                                      |
| python_startup_no_site | 16.2 ms                                                         | 17.1 ms: 1.05x slower                                      |
| Geometric mean         | (ref)                                                           | 1.04x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-pythonperf1-amd64-python-main-3.14.0a0-f8373db |
|-----------------|:---------------------------------------------------------------:|:----------------------------------------------------------:|
| django_template | 21.7 ms                                                         | 22.7 ms: 1.05x slower                                      |
| genshi_text     | 14.4 ms                                                         | 15.3 ms: 1.07x slower                                      |
| mako            | 6.36 ms                                                         | 6.82 ms: 1.07x slower                                      |
| genshi_xml      | 31.6 ms                                                         | 33.9 ms: 1.07x slower                                      |
| Geometric mean  | (ref)                                                           | 1.06x slower                                               |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-pythonperf1-amd64-python-main-3.14.0a0-f8373db |
|---------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------:|
| thrift                    | 8.11 ms                                                         | 509 us: 15.93x faster                                      |
| deepcopy                  | 220 us                                                          | 172 us: 1.28x faster                                       |
| deepcopy_memo             | 22.1 us                                                         | 18.5 us: 1.20x faster                                      |
| async_tree_io_tg          | 605 ms                                                          | 512 ms: 1.18x faster                                       |
| deepcopy_reduce           | 1.99 us                                                         | 1.77 us: 1.13x faster                                      |
| async_tree_io             | 588 ms                                                          | 523 ms: 1.12x faster                                       |
| async_tree_none_tg        | 202 ms                                                          | 185 ms: 1.09x faster                                       |
| async_tree_memoization_tg | 258 ms                                                          | 240 ms: 1.07x faster                                       |
| async_tree_none           | 218 ms                                                          | 204 ms: 1.07x faster                                       |
| async_tree_memoization    | 264 ms                                                          | 249 ms: 1.06x faster                                       |
| json                      | 3.19 ms                                                         | 3.01 ms: 1.06x faster                                      |
| async_tree_cpu_io_mixed   | 389 ms                                                          | 381 ms: 1.02x faster                                       |
| tornado_http              | 81.8 ms                                                         | 80.2 ms: 1.02x faster                                      |
| scimark_lu                | 56.6 ms                                                         | 56.8 ms: 1.00x slower                                      |
| json_loads                | 14.2 us                                                         | 14.3 us: 1.01x slower                                      |
| bench_mp_pool             | 64.8 ms                                                         | 65.2 ms: 1.01x slower                                      |
| sympy_sum                 | 84.4 ms                                                         | 85.1 ms: 1.01x slower                                      |
| create_gc_cycles          | 888 us                                                          | 903 us: 1.02x slower                                       |
| telco                     | 4.67 ms                                                         | 4.75 ms: 1.02x slower                                      |
| logging_simple            | 5.78 us                                                         | 5.89 us: 1.02x slower                                      |
| spectral_norm             | 63.7 ms                                                         | 64.9 ms: 1.02x slower                                      |
| logging_format            | 6.22 us                                                         | 6.35 us: 1.02x slower                                      |
| sqlglot_optimize          | 32.7 ms                                                         | 33.4 ms: 1.02x slower                                      |
| xml_etree_iterparse       | 62.3 ms                                                         | 63.7 ms: 1.02x slower                                      |
| sympy_str                 | 159 ms                                                          | 163 ms: 1.02x slower                                       |
| richards                  | 26.7 ms                                                         | 27.3 ms: 1.02x slower                                      |
| xml_etree_parse           | 90.9 ms                                                         | 93.1 ms: 1.02x slower                                      |
| sqlglot_normalize         | 173 ms                                                          | 177 ms: 1.02x slower                                       |
| richards_super            | 30.2 ms                                                         | 30.9 ms: 1.02x slower                                      |
| sympy_integrate           | 12.2 ms                                                         | 12.6 ms: 1.03x slower                                      |
| regex_compile             | 78.0 ms                                                         | 80.2 ms: 1.03x slower                                      |
| sympy_expand              | 271 ms                                                          | 278 ms: 1.03x slower                                       |
| python_startup            | 20.3 ms                                                         | 20.9 ms: 1.03x slower                                      |
| nqueens                   | 56.7 ms                                                         | 58.4 ms: 1.03x slower                                      |
| typing_runtime_protocols  | 101 us                                                          | 104 us: 1.03x slower                                       |
| comprehensions            | 10.4 us                                                         | 10.7 us: 1.03x slower                                      |
| json_dumps                | 5.61 ms                                                         | 5.80 ms: 1.03x slower                                      |
| regex_effbot              | 1.58 ms                                                         | 1.64 ms: 1.04x slower                                      |
| crypto_pyaes              | 45.5 ms                                                         | 47.2 ms: 1.04x slower                                      |
| async_generators          | 223 ms                                                          | 232 ms: 1.04x slower                                       |
| 2to3                      | 207 ms                                                          | 216 ms: 1.04x slower                                       |
| django_template           | 21.7 ms                                                         | 22.7 ms: 1.05x slower                                      |
| raytrace                  | 162 ms                                                          | 170 ms: 1.05x slower                                       |
| xml_etree_generate        | 53.2 ms                                                         | 55.7 ms: 1.05x slower                                      |
| coroutines                | 12.8 ms                                                         | 13.4 ms: 1.05x slower                                      |
| meteor_contest            | 69.9 ms                                                         | 73.3 ms: 1.05x slower                                      |
| regex_dna                 | 119 ms                                                          | 125 ms: 1.05x slower                                       |
| scimark_sparse_mat_mult   | 2.50 ms                                                         | 2.63 ms: 1.05x slower                                      |
| html5lib                  | 35.0 ms                                                         | 36.8 ms: 1.05x slower                                      |
| xml_etree_process         | 36.4 ms                                                         | 38.4 ms: 1.05x slower                                      |
| python_startup_no_site    | 16.2 ms                                                         | 17.1 ms: 1.05x slower                                      |
| go                        | 82.1 ms                                                         | 86.4 ms: 1.05x slower                                      |
| hexiom                    | 3.72 ms                                                         | 3.92 ms: 1.05x slower                                      |
| generators                | 19.6 ms                                                         | 20.8 ms: 1.06x slower                                      |
| scimark_sor               | 75.3 ms                                                         | 80.4 ms: 1.07x slower                                      |
| genshi_text               | 14.4 ms                                                         | 15.3 ms: 1.07x slower                                      |
| pyflate                   | 279 ms                                                          | 298 ms: 1.07x slower                                       |
| mako                      | 6.36 ms                                                         | 6.82 ms: 1.07x slower                                      |
| genshi_xml                | 31.6 ms                                                         | 33.9 ms: 1.07x slower                                      |
| coverage                  | 42.1 ms                                                         | 45.2 ms: 1.07x slower                                      |
| pprint_safe_repr          | 474 ms                                                          | 509 ms: 1.07x slower                                       |
| pprint_pformat            | 966 ms                                                          | 1.04 sec: 1.08x slower                                     |
| pickle_pure_python        | 175 us                                                          | 189 us: 1.08x slower                                       |
| chaos                     | 38.4 ms                                                         | 41.3 ms: 1.08x slower                                      |
| sqlglot_transpile         | 955 us                                                          | 1.03 ms: 1.08x slower                                      |
| deltablue                 | 1.88 ms                                                         | 2.03 ms: 1.08x slower                                      |
| float                     | 49.7 ms                                                         | 54.0 ms: 1.09x slower                                      |
| nbody                     | 67.6 ms                                                         | 73.6 ms: 1.09x slower                                      |
| sqlglot_parse             | 748 us                                                          | 820 us: 1.10x slower                                       |
| tomli_loads               | 1.35 sec                                                        | 1.48 sec: 1.10x slower                                     |
| unpickle_pure_python      | 122 us                                                          | 135 us: 1.10x slower                                       |
| scimark_fft               | 171 ms                                                          | 189 ms: 1.11x slower                                       |
| scimark_monte_carlo       | 39.1 ms                                                         | 43.4 ms: 1.11x slower                                      |
| mdp                       | 1.31 sec                                                        | 1.49 sec: 1.13x slower                                     |
| fannkuch                  | 243 ms                                                          | 276 ms: 1.13x slower                                       |
| logging_silent            | 52.9 ns                                                         | 60.9 ns: 1.15x slower                                      |
| Geometric mean            | (ref)                                                           | 1.01x faster                                               |

Benchmark hidden because not significant (11): pycparser, regex_v8, pathlib, asyncio_tcp, pidigits, gc_traversal, docutils, async_tree_cpu_io_mixed_tg, bench_thread_pool, pylint, asyncio_tcp_ssl
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: unknown