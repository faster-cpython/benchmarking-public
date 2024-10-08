# Results vs. 3.13.0b2

- fork: python
- ref: 2c1b1e7a07eba0138b98
- machine: windows-amd64
- commit hash: 2c1b1e7
- commit date: 2024-07-23
- overall geometric mean: 1.01x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-pythonperf1-amd64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 220 ms: 1.06x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.67 sec: 1.03x slower                                                     |
| html5lib       | 35.0 ms                                                         | 39.4 ms: 1.12x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 91.1 ms: 1.11x slower                                                      |
| Geometric mean | (ref)                                                           | 1.08x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-pythonperf1-amd64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg          | 605 ms                                                          | 522 ms: 1.16x faster                                                       |
| async_tree_io             | 588 ms                                                          | 530 ms: 1.11x faster                                                       |
| async_tree_none_tg        | 202 ms                                                          | 186 ms: 1.08x faster                                                       |
| async_tree_memoization_tg | 258 ms                                                          | 241 ms: 1.07x faster                                                       |
| async_tree_memoization    | 264 ms                                                          | 250 ms: 1.05x faster                                                       |
| async_tree_none           | 218 ms                                                          | 207 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed   | 389 ms                                                          | 381 ms: 1.02x faster                                                       |
| Geometric mean            | (ref)                                                           | 1.07x faster                                                               |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-pythonperf1-amd64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 49.7 ms                                                         | 54.3 ms: 1.09x slower                                                      |
| nbody          | 67.6 ms                                                         | 75.2 ms: 1.11x slower                                                      |
| Geometric mean | (ref)                                                           | 1.07x slower                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-pythonperf1-amd64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 78.0 ms                                                         | 85.0 ms: 1.09x slower                                                      |
| Geometric mean | (ref)                                                           | 1.02x slower                                                               |

Benchmark hidden because not significant (3): regex_dna, regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-pythonperf1-amd64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 14.2 us                                                         | 14.5 us: 1.02x slower                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 93.2 ms: 1.03x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 5.80 ms: 1.03x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 64.8 ms: 1.04x slower                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 56.0 ms: 1.05x slower                                                      |
| xml_etree_process    | 36.4 ms                                                         | 38.5 ms: 1.06x slower                                                      |
| pickle_pure_python   | 175 us                                                          | 193 us: 1.10x slower                                                       |
| tomli_loads          | 1.35 sec                                                        | 1.49 sec: 1.10x slower                                                     |
| unpickle_pure_python | 122 us                                                          | 136 us: 1.11x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.06x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-pythonperf1-amd64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 21.7 ms: 1.07x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 17.8 ms: 1.10x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-pythonperf1-amd64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 21.7 ms                                                         | 22.9 ms: 1.05x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 33.8 ms: 1.07x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 15.5 ms: 1.08x slower                                                      |
| mako            | 6.36 ms                                                         | 6.88 ms: 1.08x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.07x slower                                                               |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-pythonperf1-amd64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                    | 8.11 ms                                                         | 514 us: 15.77x faster                                                      |
| deepcopy                  | 220 us                                                          | 177 us: 1.24x faster                                                       |
| deepcopy_memo             | 22.1 us                                                         | 18.9 us: 1.17x faster                                                      |
| async_tree_io_tg          | 605 ms                                                          | 522 ms: 1.16x faster                                                       |
| async_tree_io             | 588 ms                                                          | 530 ms: 1.11x faster                                                       |
| deepcopy_reduce           | 1.99 us                                                         | 1.80 us: 1.11x faster                                                      |
| async_tree_none_tg        | 202 ms                                                          | 186 ms: 1.08x faster                                                       |
| json                      | 3.19 ms                                                         | 2.96 ms: 1.08x faster                                                      |
| async_tree_memoization_tg | 258 ms                                                          | 241 ms: 1.07x faster                                                       |
| async_tree_memoization    | 264 ms                                                          | 250 ms: 1.05x faster                                                       |
| async_tree_none           | 218 ms                                                          | 207 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed   | 389 ms                                                          | 381 ms: 1.02x faster                                                       |
| create_gc_cycles          | 888 us                                                          | 899 us: 1.01x slower                                                       |
| logging_simple            | 5.78 us                                                         | 5.88 us: 1.02x slower                                                      |
| logging_format            | 6.22 us                                                         | 6.33 us: 1.02x slower                                                      |
| json_loads                | 14.2 us                                                         | 14.5 us: 1.02x slower                                                      |
| xml_etree_parse           | 90.9 ms                                                         | 93.2 ms: 1.03x slower                                                      |
| docutils                  | 1.63 sec                                                        | 1.67 sec: 1.03x slower                                                     |
| sqlglot_optimize          | 32.7 ms                                                         | 33.6 ms: 1.03x slower                                                      |
| sqlglot_normalize         | 173 ms                                                          | 178 ms: 1.03x slower                                                       |
| telco                     | 4.67 ms                                                         | 4.81 ms: 1.03x slower                                                      |
| coroutines                | 12.8 ms                                                         | 13.2 ms: 1.03x slower                                                      |
| typing_runtime_protocols  | 101 us                                                          | 104 us: 1.03x slower                                                       |
| bench_thread_pool         | 768 us                                                          | 793 us: 1.03x slower                                                       |
| json_dumps                | 5.61 ms                                                         | 5.80 ms: 1.03x slower                                                      |
| xml_etree_iterparse       | 62.3 ms                                                         | 64.8 ms: 1.04x slower                                                      |
| bench_mp_pool             | 64.8 ms                                                         | 67.4 ms: 1.04x slower                                                      |
| sympy_integrate           | 12.2 ms                                                         | 12.7 ms: 1.04x slower                                                      |
| richards                  | 26.7 ms                                                         | 27.8 ms: 1.04x slower                                                      |
| sympy_sum                 | 84.4 ms                                                         | 88.0 ms: 1.04x slower                                                      |
| raytrace                  | 162 ms                                                          | 169 ms: 1.04x slower                                                       |
| richards_super            | 30.2 ms                                                         | 31.6 ms: 1.05x slower                                                      |
| scimark_lu                | 56.6 ms                                                         | 59.4 ms: 1.05x slower                                                      |
| crypto_pyaes              | 45.5 ms                                                         | 47.7 ms: 1.05x slower                                                      |
| xml_etree_generate        | 53.2 ms                                                         | 56.0 ms: 1.05x slower                                                      |
| django_template           | 21.7 ms                                                         | 22.9 ms: 1.05x slower                                                      |
| xml_etree_process         | 36.4 ms                                                         | 38.5 ms: 1.06x slower                                                      |
| deltablue                 | 1.88 ms                                                         | 1.99 ms: 1.06x slower                                                      |
| pathlib                   | 75.9 ms                                                         | 80.3 ms: 1.06x slower                                                      |
| generators                | 19.6 ms                                                         | 20.7 ms: 1.06x slower                                                      |
| comprehensions            | 10.4 us                                                         | 11.0 us: 1.06x slower                                                      |
| spectral_norm             | 63.7 ms                                                         | 67.8 ms: 1.06x slower                                                      |
| 2to3                      | 207 ms                                                          | 220 ms: 1.06x slower                                                       |
| python_startup            | 20.3 ms                                                         | 21.7 ms: 1.07x slower                                                      |
| genshi_xml                | 31.6 ms                                                         | 33.8 ms: 1.07x slower                                                      |
| hexiom                    | 3.72 ms                                                         | 3.98 ms: 1.07x slower                                                      |
| sympy_str                 | 159 ms                                                          | 170 ms: 1.07x slower                                                       |
| meteor_contest            | 69.9 ms                                                         | 74.9 ms: 1.07x slower                                                      |
| nqueens                   | 56.7 ms                                                         | 60.8 ms: 1.07x slower                                                      |
| pyflate                   | 279 ms                                                          | 299 ms: 1.07x slower                                                       |
| go                        | 82.1 ms                                                         | 88.1 ms: 1.07x slower                                                      |
| sympy_expand              | 271 ms                                                          | 292 ms: 1.08x slower                                                       |
| genshi_text               | 14.4 ms                                                         | 15.5 ms: 1.08x slower                                                      |
| logging_silent            | 52.9 ns                                                         | 57.1 ns: 1.08x slower                                                      |
| chaos                     | 38.4 ms                                                         | 41.4 ms: 1.08x slower                                                      |
| async_generators          | 223 ms                                                          | 241 ms: 1.08x slower                                                       |
| mako                      | 6.36 ms                                                         | 6.88 ms: 1.08x slower                                                      |
| regex_compile             | 78.0 ms                                                         | 85.0 ms: 1.09x slower                                                      |
| float                     | 49.7 ms                                                         | 54.3 ms: 1.09x slower                                                      |
| sqlglot_transpile         | 955 us                                                          | 1.04 ms: 1.09x slower                                                      |
| pprint_pformat            | 966 ms                                                          | 1.06 sec: 1.10x slower                                                     |
| python_startup_no_site    | 16.2 ms                                                         | 17.8 ms: 1.10x slower                                                      |
| scimark_sor               | 75.3 ms                                                         | 83.0 ms: 1.10x slower                                                      |
| pickle_pure_python        | 175 us                                                          | 193 us: 1.10x slower                                                       |
| tomli_loads               | 1.35 sec                                                        | 1.49 sec: 1.10x slower                                                     |
| asyncio_tcp_ssl           | 1.48 sec                                                        | 1.63 sec: 1.10x slower                                                     |
| coverage                  | 42.1 ms                                                         | 46.5 ms: 1.11x slower                                                      |
| nbody                     | 67.6 ms                                                         | 75.2 ms: 1.11x slower                                                      |
| unpickle_pure_python      | 122 us                                                          | 136 us: 1.11x slower                                                       |
| tornado_http              | 81.8 ms                                                         | 91.1 ms: 1.11x slower                                                      |
| pprint_safe_repr          | 474 ms                                                          | 528 ms: 1.11x slower                                                       |
| asyncio_tcp               | 471 ms                                                          | 528 ms: 1.12x slower                                                       |
| mdp                       | 1.31 sec                                                        | 1.47 sec: 1.12x slower                                                     |
| html5lib                  | 35.0 ms                                                         | 39.4 ms: 1.12x slower                                                      |
| sqlglot_parse             | 748 us                                                          | 843 us: 1.13x slower                                                       |
| pycparser                 | 754 ms                                                          | 852 ms: 1.13x slower                                                       |
| scimark_sparse_mat_mult   | 2.50 ms                                                         | 2.91 ms: 1.16x slower                                                      |
| fannkuch                  | 243 ms                                                          | 290 ms: 1.19x slower                                                       |
| scimark_fft               | 171 ms                                                          | 207 ms: 1.21x slower                                                       |
| scimark_monte_carlo       | 39.1 ms                                                         | 48.6 ms: 1.24x slower                                                      |
| Geometric mean            | (ref)                                                           | 1.01x slower                                                               |

Benchmark hidden because not significant (7): regex_dna, gc_traversal, async_tree_cpu_io_mixed_tg, pidigits, regex_v8, regex_effbot, pylint
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown