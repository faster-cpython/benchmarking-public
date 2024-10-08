# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: bound_method_instrum
- machine: windows-amd64
- commit hash: 5787d3e
- commit date: 2024-07-23
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-pythonperf1-amd64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 227 ms: 1.10x slower                                                                 |
| docutils       | 1.63 sec                                                        | 1.69 sec: 1.04x slower                                                               |
| html5lib       | 35.0 ms                                                         | 41.4 ms: 1.18x slower                                                                |
| tornado_http   | 81.8 ms                                                         | 91.6 ms: 1.12x slower                                                                |
| Geometric mean | (ref)                                                           | 1.11x slower                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-pythonperf1-amd64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|---------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_io_tg          | 605 ms                                                          | 533 ms: 1.14x faster                                                                 |
| async_tree_io             | 588 ms                                                          | 547 ms: 1.07x faster                                                                 |
| async_tree_memoization_tg | 258 ms                                                          | 245 ms: 1.05x faster                                                                 |
| async_tree_none_tg        | 202 ms                                                          | 193 ms: 1.05x faster                                                                 |
| async_tree_cpu_io_mixed   | 389 ms                                                          | 382 ms: 1.02x faster                                                                 |
| Geometric mean            | (ref)                                                           | 1.04x faster                                                                         |

Benchmark hidden because not significant (3): async_tree_memoization, async_tree_none, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-pythonperf1-amd64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 151 ms: 1.00x slower                                                                 |
| float          | 49.7 ms                                                         | 56.3 ms: 1.13x slower                                                                |
| nbody          | 67.6 ms                                                         | 83.8 ms: 1.24x slower                                                                |
| Geometric mean | (ref)                                                           | 1.12x slower                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-pythonperf1-amd64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_v8       | 15.8 ms                                                         | 14.6 ms: 1.08x faster                                                                |
| regex_dna      | 119 ms                                                          | 120 ms: 1.01x slower                                                                 |
| regex_effbot   | 1.58 ms                                                         | 1.60 ms: 1.01x slower                                                                |
| regex_compile  | 78.0 ms                                                         | 90.4 ms: 1.16x slower                                                                |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-pythonperf1-amd64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_loads           | 14.2 us                                                         | 14.0 us: 1.02x faster                                                                |
| xml_etree_parse      | 90.9 ms                                                         | 91.9 ms: 1.01x slower                                                                |
| xml_etree_iterparse  | 62.3 ms                                                         | 66.3 ms: 1.06x slower                                                                |
| json_dumps           | 5.61 ms                                                         | 6.00 ms: 1.07x slower                                                                |
| xml_etree_generate   | 53.2 ms                                                         | 58.1 ms: 1.09x slower                                                                |
| xml_etree_process    | 36.4 ms                                                         | 40.6 ms: 1.11x slower                                                                |
| tomli_loads          | 1.35 sec                                                        | 1.57 sec: 1.16x slower                                                               |
| pickle_pure_python   | 175 us                                                          | 209 us: 1.19x slower                                                                 |
| unpickle_pure_python | 122 us                                                          | 150 us: 1.23x slower                                                                 |
| Geometric mean       | (ref)                                                           | 1.10x slower                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-pythonperf1-amd64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 21.7 ms: 1.07x slower                                                                |
| python_startup_no_site | 16.2 ms                                                         | 17.6 ms: 1.09x slower                                                                |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-pythonperf1-amd64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| django_template | 21.7 ms                                                         | 23.7 ms: 1.10x slower                                                                |
| genshi_xml      | 31.6 ms                                                         | 36.3 ms: 1.15x slower                                                                |
| genshi_text     | 14.4 ms                                                         | 16.7 ms: 1.16x slower                                                                |
| mako            | 6.36 ms                                                         | 7.48 ms: 1.18x slower                                                                |
| Geometric mean  | (ref)                                                           | 1.15x slower                                                                         |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-pythonperf1-amd64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|---------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| thrift                    | 8.11 ms                                                         | 530 us: 15.31x faster                                                                |
| deepcopy                  | 220 us                                                          | 184 us: 1.19x faster                                                                 |
| async_tree_io_tg          | 605 ms                                                          | 533 ms: 1.14x faster                                                                 |
| json                      | 3.19 ms                                                         | 2.93 ms: 1.09x faster                                                                |
| regex_v8                  | 15.8 ms                                                         | 14.6 ms: 1.08x faster                                                                |
| async_tree_io             | 588 ms                                                          | 547 ms: 1.07x faster                                                                 |
| deepcopy_reduce           | 1.99 us                                                         | 1.89 us: 1.05x faster                                                                |
| async_tree_memoization_tg | 258 ms                                                          | 245 ms: 1.05x faster                                                                 |
| async_tree_none_tg        | 202 ms                                                          | 193 ms: 1.05x faster                                                                 |
| async_tree_cpu_io_mixed   | 389 ms                                                          | 382 ms: 1.02x faster                                                                 |
| deepcopy_memo             | 22.1 us                                                         | 21.7 us: 1.02x faster                                                                |
| json_loads                | 14.2 us                                                         | 14.0 us: 1.02x faster                                                                |
| pidigits                  | 150 ms                                                          | 151 ms: 1.00x slower                                                                 |
| regex_dna                 | 119 ms                                                          | 120 ms: 1.01x slower                                                                 |
| regex_effbot              | 1.58 ms                                                         | 1.60 ms: 1.01x slower                                                                |
| xml_etree_parse           | 90.9 ms                                                         | 91.9 ms: 1.01x slower                                                                |
| create_gc_cycles          | 888 us                                                          | 903 us: 1.02x slower                                                                 |
| bench_mp_pool             | 64.8 ms                                                         | 67.3 ms: 1.04x slower                                                                |
| docutils                  | 1.63 sec                                                        | 1.69 sec: 1.04x slower                                                               |
| telco                     | 4.67 ms                                                         | 4.87 ms: 1.04x slower                                                                |
| bench_thread_pool         | 768 us                                                          | 806 us: 1.05x slower                                                                 |
| coroutines                | 12.8 ms                                                         | 13.5 ms: 1.06x slower                                                                |
| sqlglot_optimize          | 32.7 ms                                                         | 34.6 ms: 1.06x slower                                                                |
| sympy_sum                 | 84.4 ms                                                         | 89.3 ms: 1.06x slower                                                                |
| sqlglot_normalize         | 173 ms                                                          | 184 ms: 1.06x slower                                                                 |
| pathlib                   | 75.9 ms                                                         | 80.5 ms: 1.06x slower                                                                |
| sympy_integrate           | 12.2 ms                                                         | 13.0 ms: 1.06x slower                                                                |
| xml_etree_iterparse       | 62.3 ms                                                         | 66.3 ms: 1.06x slower                                                                |
| python_startup            | 20.3 ms                                                         | 21.7 ms: 1.07x slower                                                                |
| json_dumps                | 5.61 ms                                                         | 6.00 ms: 1.07x slower                                                                |
| typing_runtime_protocols  | 101 us                                                          | 108 us: 1.07x slower                                                                 |
| mdp                       | 1.31 sec                                                        | 1.40 sec: 1.07x slower                                                               |
| logging_simple            | 5.78 us                                                         | 6.20 us: 1.07x slower                                                                |
| logging_format            | 6.22 us                                                         | 6.68 us: 1.07x slower                                                                |
| pylint                    | 205 ms                                                          | 221 ms: 1.08x slower                                                                 |
| generators                | 19.6 ms                                                         | 21.2 ms: 1.08x slower                                                                |
| meteor_contest            | 69.9 ms                                                         | 75.6 ms: 1.08x slower                                                                |
| python_startup_no_site    | 16.2 ms                                                         | 17.6 ms: 1.09x slower                                                                |
| xml_etree_generate        | 53.2 ms                                                         | 58.1 ms: 1.09x slower                                                                |
| django_template           | 21.7 ms                                                         | 23.7 ms: 1.10x slower                                                                |
| sympy_str                 | 159 ms                                                          | 174 ms: 1.10x slower                                                                 |
| async_generators          | 223 ms                                                          | 245 ms: 1.10x slower                                                                 |
| 2to3                      | 207 ms                                                          | 227 ms: 1.10x slower                                                                 |
| sympy_expand              | 271 ms                                                          | 298 ms: 1.10x slower                                                                 |
| crypto_pyaes              | 45.5 ms                                                         | 50.2 ms: 1.10x slower                                                                |
| raytrace                  | 162 ms                                                          | 179 ms: 1.10x slower                                                                 |
| xml_etree_process         | 36.4 ms                                                         | 40.6 ms: 1.11x slower                                                                |
| nqueens                   | 56.7 ms                                                         | 63.2 ms: 1.11x slower                                                                |
| tornado_http              | 81.8 ms                                                         | 91.6 ms: 1.12x slower                                                                |
| comprehensions            | 10.4 us                                                         | 11.6 us: 1.12x slower                                                                |
| coverage                  | 42.1 ms                                                         | 47.4 ms: 1.13x slower                                                                |
| pyflate                   | 279 ms                                                          | 316 ms: 1.13x slower                                                                 |
| asyncio_tcp               | 471 ms                                                          | 533 ms: 1.13x slower                                                                 |
| float                     | 49.7 ms                                                         | 56.3 ms: 1.13x slower                                                                |
| genshi_xml                | 31.6 ms                                                         | 36.3 ms: 1.15x slower                                                                |
| sqlglot_transpile         | 955 us                                                          | 1.10 ms: 1.15x slower                                                                |
| spectral_norm             | 63.7 ms                                                         | 73.5 ms: 1.15x slower                                                                |
| chaos                     | 38.4 ms                                                         | 44.5 ms: 1.16x slower                                                                |
| scimark_sparse_mat_mult   | 2.50 ms                                                         | 2.90 ms: 1.16x slower                                                                |
| regex_compile             | 78.0 ms                                                         | 90.4 ms: 1.16x slower                                                                |
| genshi_text               | 14.4 ms                                                         | 16.7 ms: 1.16x slower                                                                |
| tomli_loads               | 1.35 sec                                                        | 1.57 sec: 1.16x slower                                                               |
| scimark_lu                | 56.6 ms                                                         | 65.9 ms: 1.16x slower                                                                |
| go                        | 82.1 ms                                                         | 95.5 ms: 1.16x slower                                                                |
| richards_super            | 30.2 ms                                                         | 35.1 ms: 1.16x slower                                                                |
| deltablue                 | 1.88 ms                                                         | 2.21 ms: 1.17x slower                                                                |
| richards                  | 26.7 ms                                                         | 31.4 ms: 1.18x slower                                                                |
| mako                      | 6.36 ms                                                         | 7.48 ms: 1.18x slower                                                                |
| html5lib                  | 35.0 ms                                                         | 41.4 ms: 1.18x slower                                                                |
| logging_silent            | 52.9 ns                                                         | 62.6 ns: 1.18x slower                                                                |
| pprint_pformat            | 966 ms                                                          | 1.15 sec: 1.19x slower                                                               |
| pprint_safe_repr          | 474 ms                                                          | 563 ms: 1.19x slower                                                                 |
| pickle_pure_python        | 175 us                                                          | 209 us: 1.19x slower                                                                 |
| sqlglot_parse             | 748 us                                                          | 893 us: 1.19x slower                                                                 |
| hexiom                    | 3.72 ms                                                         | 4.46 ms: 1.20x slower                                                                |
| scimark_sor               | 75.3 ms                                                         | 90.9 ms: 1.21x slower                                                                |
| asyncio_tcp_ssl           | 1.48 sec                                                        | 1.79 sec: 1.21x slower                                                               |
| fannkuch                  | 243 ms                                                          | 300 ms: 1.23x slower                                                                 |
| unpickle_pure_python      | 122 us                                                          | 150 us: 1.23x slower                                                                 |
| nbody                     | 67.6 ms                                                         | 83.8 ms: 1.24x slower                                                                |
| scimark_monte_carlo       | 39.1 ms                                                         | 50.1 ms: 1.28x slower                                                                |
| scimark_fft               | 171 ms                                                          | 219 ms: 1.28x slower                                                                 |
| Geometric mean            | (ref)                                                           | 1.05x slower                                                                         |

Benchmark hidden because not significant (5): async_tree_memoization, async_tree_none, gc_traversal, async_tree_cpu_io_mixed_tg, pycparser
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: unknown