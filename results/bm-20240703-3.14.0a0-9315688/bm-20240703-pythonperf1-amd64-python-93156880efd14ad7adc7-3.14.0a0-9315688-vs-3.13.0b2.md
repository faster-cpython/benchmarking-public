# Results vs. 3.13.0b2

- fork: python
- ref: 93156880efd14ad7adc7
- machine: windows-amd64
- commit hash: 9315688
- commit date: 2024-07-03
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-pythonperf1-amd64-python-93156880efd14ad7adc7-3.14.0a0-9315688 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 227 ms: 1.10x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.67 sec: 1.03x slower                                                     |
| html5lib       | 35.0 ms                                                         | 38.8 ms: 1.11x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 91.1 ms: 1.11x slower                                                      |
| Geometric mean | (ref)                                                           | 1.09x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-pythonperf1-amd64-python-93156880efd14ad7adc7-3.14.0a0-9315688 |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg          | 605 ms                                                          | 532 ms: 1.14x faster                                                       |
| async_tree_io             | 588 ms                                                          | 545 ms: 1.08x faster                                                       |
| async_tree_memoization_tg | 258 ms                                                          | 245 ms: 1.05x faster                                                       |
| Geometric mean            | (ref)                                                           | 1.04x faster                                                               |

Benchmark hidden because not significant (5): async_tree_none_tg, async_tree_memoization, async_tree_none, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-pythonperf1-amd64-python-93156880efd14ad7adc7-3.14.0a0-9315688 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 151 ms: 1.01x slower                                                       |
| float          | 49.7 ms                                                         | 56.9 ms: 1.14x slower                                                      |
| nbody          | 67.6 ms                                                         | 80.3 ms: 1.19x slower                                                      |
| Geometric mean | (ref)                                                           | 1.11x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-pythonperf1-amd64-python-93156880efd14ad7adc7-3.14.0a0-9315688 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.58 ms                                                         | 1.62 ms: 1.02x slower                                                      |
| regex_dna      | 119 ms                                                          | 124 ms: 1.04x slower                                                       |
| regex_compile  | 78.0 ms                                                         | 85.8 ms: 1.10x slower                                                      |
| Geometric mean | (ref)                                                           | 1.07x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-pythonperf1-amd64-python-93156880efd14ad7adc7-3.14.0a0-9315688 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 14.2 us                                                         | 14.4 us: 1.01x slower                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 92.5 ms: 1.02x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 65.9 ms: 1.06x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 6.09 ms: 1.08x slower                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 59.1 ms: 1.11x slower                                                      |
| xml_etree_process    | 36.4 ms                                                         | 41.1 ms: 1.13x slower                                                      |
| tomli_loads          | 1.35 sec                                                        | 1.57 sec: 1.16x slower                                                     |
| pickle_pure_python   | 175 us                                                          | 209 us: 1.19x slower                                                       |
| unpickle_pure_python | 122 us                                                          | 150 us: 1.23x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.11x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-pythonperf1-amd64-python-93156880efd14ad7adc7-3.14.0a0-9315688 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 21.2 ms: 1.05x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 17.5 ms: 1.08x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.06x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-pythonperf1-amd64-python-93156880efd14ad7adc7-3.14.0a0-9315688 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 21.7 ms                                                         | 24.4 ms: 1.13x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 37.0 ms: 1.17x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 16.8 ms: 1.17x slower                                                      |
| mako            | 6.36 ms                                                         | 7.52 ms: 1.18x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.16x slower                                                               |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-pythonperf1-amd64-python-93156880efd14ad7adc7-3.14.0a0-9315688 |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                    | 8.11 ms                                                         | 540 us: 15.03x faster                                                      |
| deepcopy                  | 220 us                                                          | 182 us: 1.21x faster                                                       |
| async_tree_io_tg          | 605 ms                                                          | 532 ms: 1.14x faster                                                       |
| async_tree_io             | 588 ms                                                          | 545 ms: 1.08x faster                                                       |
| deepcopy_reduce           | 1.99 us                                                         | 1.86 us: 1.08x faster                                                      |
| deepcopy_memo             | 22.1 us                                                         | 21.0 us: 1.05x faster                                                      |
| async_tree_memoization_tg | 258 ms                                                          | 245 ms: 1.05x faster                                                       |
| pidigits                  | 150 ms                                                          | 151 ms: 1.01x slower                                                       |
| gc_traversal              | 1.55 ms                                                         | 1.57 ms: 1.01x slower                                                      |
| json_loads                | 14.2 us                                                         | 14.4 us: 1.01x slower                                                      |
| xml_etree_parse           | 90.9 ms                                                         | 92.5 ms: 1.02x slower                                                      |
| regex_effbot              | 1.58 ms                                                         | 1.62 ms: 1.02x slower                                                      |
| create_gc_cycles          | 888 us                                                          | 911 us: 1.03x slower                                                       |
| docutils                  | 1.63 sec                                                        | 1.67 sec: 1.03x slower                                                     |
| regex_dna                 | 119 ms                                                          | 124 ms: 1.04x slower                                                       |
| python_startup            | 20.3 ms                                                         | 21.2 ms: 1.05x slower                                                      |
| bench_mp_pool             | 64.8 ms                                                         | 67.8 ms: 1.05x slower                                                      |
| sympy_sum                 | 84.4 ms                                                         | 88.7 ms: 1.05x slower                                                      |
| xml_etree_iterparse       | 62.3 ms                                                         | 65.9 ms: 1.06x slower                                                      |
| telco                     | 4.67 ms                                                         | 4.97 ms: 1.06x slower                                                      |
| sympy_integrate           | 12.2 ms                                                         | 13.0 ms: 1.07x slower                                                      |
| spectral_norm             | 63.7 ms                                                         | 68.2 ms: 1.07x slower                                                      |
| pathlib                   | 75.9 ms                                                         | 81.2 ms: 1.07x slower                                                      |
| typing_runtime_protocols  | 101 us                                                          | 109 us: 1.08x slower                                                       |
| bench_thread_pool         | 768 us                                                          | 827 us: 1.08x slower                                                       |
| sqlglot_optimize          | 32.7 ms                                                         | 35.2 ms: 1.08x slower                                                      |
| sympy_str                 | 159 ms                                                          | 171 ms: 1.08x slower                                                       |
| python_startup_no_site    | 16.2 ms                                                         | 17.5 ms: 1.08x slower                                                      |
| sympy_expand              | 271 ms                                                          | 293 ms: 1.08x slower                                                       |
| logging_format            | 6.22 us                                                         | 6.75 us: 1.08x slower                                                      |
| json_dumps                | 5.61 ms                                                         | 6.09 ms: 1.08x slower                                                      |
| mdp                       | 1.31 sec                                                        | 1.43 sec: 1.09x slower                                                     |
| sqlglot_normalize         | 173 ms                                                          | 188 ms: 1.09x slower                                                       |
| logging_simple            | 5.78 us                                                         | 6.31 us: 1.09x slower                                                      |
| nqueens                   | 56.7 ms                                                         | 61.8 ms: 1.09x slower                                                      |
| asyncio_tcp_ssl           | 1.48 sec                                                        | 1.62 sec: 1.09x slower                                                     |
| raytrace                  | 162 ms                                                          | 177 ms: 1.09x slower                                                       |
| async_generators          | 223 ms                                                          | 245 ms: 1.10x slower                                                       |
| 2to3                      | 207 ms                                                          | 227 ms: 1.10x slower                                                       |
| coroutines                | 12.8 ms                                                         | 14.0 ms: 1.10x slower                                                      |
| regex_compile             | 78.0 ms                                                         | 85.8 ms: 1.10x slower                                                      |
| meteor_contest            | 69.9 ms                                                         | 77.0 ms: 1.10x slower                                                      |
| html5lib                  | 35.0 ms                                                         | 38.8 ms: 1.11x slower                                                      |
| richards_super            | 30.2 ms                                                         | 33.4 ms: 1.11x slower                                                      |
| richards                  | 26.7 ms                                                         | 29.6 ms: 1.11x slower                                                      |
| xml_etree_generate        | 53.2 ms                                                         | 59.1 ms: 1.11x slower                                                      |
| tornado_http              | 81.8 ms                                                         | 91.1 ms: 1.11x slower                                                      |
| scimark_sor               | 75.3 ms                                                         | 84.4 ms: 1.12x slower                                                      |
| pycparser                 | 754 ms                                                          | 848 ms: 1.13x slower                                                       |
| django_template           | 21.7 ms                                                         | 24.4 ms: 1.13x slower                                                      |
| xml_etree_process         | 36.4 ms                                                         | 41.1 ms: 1.13x slower                                                      |
| pyflate                   | 279 ms                                                          | 315 ms: 1.13x slower                                                       |
| asyncio_tcp               | 471 ms                                                          | 533 ms: 1.13x slower                                                       |
| crypto_pyaes              | 45.5 ms                                                         | 51.5 ms: 1.13x slower                                                      |
| comprehensions            | 10.4 us                                                         | 11.8 us: 1.14x slower                                                      |
| chaos                     | 38.4 ms                                                         | 43.6 ms: 1.14x slower                                                      |
| go                        | 82.1 ms                                                         | 93.5 ms: 1.14x slower                                                      |
| generators                | 19.6 ms                                                         | 22.3 ms: 1.14x slower                                                      |
| float                     | 49.7 ms                                                         | 56.9 ms: 1.14x slower                                                      |
| coverage                  | 42.1 ms                                                         | 48.2 ms: 1.14x slower                                                      |
| pprint_safe_repr          | 474 ms                                                          | 543 ms: 1.15x slower                                                       |
| pprint_pformat            | 966 ms                                                          | 1.11 sec: 1.15x slower                                                     |
| deltablue                 | 1.88 ms                                                         | 2.17 ms: 1.15x slower                                                      |
| hexiom                    | 3.72 ms                                                         | 4.30 ms: 1.16x slower                                                      |
| sqlglot_transpile         | 955 us                                                          | 1.11 ms: 1.16x slower                                                      |
| scimark_lu                | 56.6 ms                                                         | 65.6 ms: 1.16x slower                                                      |
| tomli_loads               | 1.35 sec                                                        | 1.57 sec: 1.16x slower                                                     |
| logging_silent            | 52.9 ns                                                         | 61.8 ns: 1.17x slower                                                      |
| genshi_xml                | 31.6 ms                                                         | 37.0 ms: 1.17x slower                                                      |
| genshi_text               | 14.4 ms                                                         | 16.8 ms: 1.17x slower                                                      |
| mako                      | 6.36 ms                                                         | 7.52 ms: 1.18x slower                                                      |
| nbody                     | 67.6 ms                                                         | 80.3 ms: 1.19x slower                                                      |
| pickle_pure_python        | 175 us                                                          | 209 us: 1.19x slower                                                       |
| scimark_sparse_mat_mult   | 2.50 ms                                                         | 2.98 ms: 1.19x slower                                                      |
| sqlglot_parse             | 748 us                                                          | 891 us: 1.19x slower                                                       |
| fannkuch                  | 243 ms                                                          | 291 ms: 1.19x slower                                                       |
| unpickle_pure_python      | 122 us                                                          | 150 us: 1.23x slower                                                       |
| scimark_monte_carlo       | 39.1 ms                                                         | 48.4 ms: 1.24x slower                                                      |
| scimark_fft               | 171 ms                                                          | 213 ms: 1.25x slower                                                       |
| Geometric mean            | (ref)                                                           | 1.05x slower                                                               |

Benchmark hidden because not significant (8): json, async_tree_none_tg, async_tree_memoization, async_tree_none, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, pylint, regex_v8
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: unknown