# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: experimental_branch_
- machine: windows-amd64
- commit hash: 1a2b0b8
- commit date: 2024-07-31
- overall geometric mean: 1.08x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 234 ms: 1.13x slower                                                                 |
| docutils       | 1.63 sec                                                        | 1.75 sec: 1.08x slower                                                               |
| html5lib       | 35.0 ms                                                         | 42.3 ms: 1.21x slower                                                                |
| tornado_http   | 81.8 ms                                                         | 93.4 ms: 1.14x slower                                                                |
| Geometric mean | (ref)                                                           | 1.14x slower                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|---------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_io_tg          | 605 ms                                                          | 543 ms: 1.12x faster                                                                 |
| async_tree_memoization_tg | 258 ms                                                          | 246 ms: 1.05x faster                                                                 |
| Geometric mean            | (ref)                                                           | 1.02x faster                                                                         |

Benchmark hidden because not significant (6): async_tree_none_tg, async_tree_io, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_none, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 151 ms: 1.01x slower                                                                 |
| float          | 49.7 ms                                                         | 56.6 ms: 1.14x slower                                                                |
| nbody          | 67.6 ms                                                         | 92.0 ms: 1.36x slower                                                                |
| Geometric mean | (ref)                                                           | 1.16x slower                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                          | 120 ms: 1.01x slower                                                                 |
| regex_compile  | 78.0 ms                                                         | 95.0 ms: 1.22x slower                                                                |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                         |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_loads           | 14.2 us                                                         | 14.5 us: 1.02x slower                                                                |
| xml_etree_parse      | 90.9 ms                                                         | 94.8 ms: 1.04x slower                                                                |
| xml_etree_iterparse  | 62.3 ms                                                         | 66.0 ms: 1.06x slower                                                                |
| xml_etree_generate   | 53.2 ms                                                         | 58.1 ms: 1.09x slower                                                                |
| xml_etree_process    | 36.4 ms                                                         | 41.1 ms: 1.13x slower                                                                |
| json_dumps           | 5.61 ms                                                         | 6.43 ms: 1.15x slower                                                                |
| tomli_loads          | 1.35 sec                                                        | 1.61 sec: 1.19x slower                                                               |
| pickle_pure_python   | 175 us                                                          | 217 us: 1.24x slower                                                                 |
| unpickle_pure_python | 122 us                                                          | 157 us: 1.29x slower                                                                 |
| Geometric mean       | (ref)                                                           | 1.13x slower                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 21.7 ms: 1.07x slower                                                                |
| python_startup_no_site | 16.2 ms                                                         | 17.4 ms: 1.08x slower                                                                |
| Geometric mean         | (ref)                                                           | 1.07x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 7.25 ms: 1.14x slower                                                                |
| django_template | 21.7 ms                                                         | 24.7 ms: 1.14x slower                                                                |
| genshi_xml      | 31.6 ms                                                         | 36.8 ms: 1.17x slower                                                                |
| genshi_text     | 14.4 ms                                                         | 17.9 ms: 1.25x slower                                                                |
| Geometric mean  | (ref)                                                           | 1.17x slower                                                                         |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|---------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| thrift                    | 8.11 ms                                                         | 525 us: 15.44x faster                                                                |
| deepcopy                  | 220 us                                                          | 192 us: 1.15x faster                                                                 |
| async_tree_io_tg          | 605 ms                                                          | 543 ms: 1.12x faster                                                                 |
| async_tree_memoization_tg | 258 ms                                                          | 246 ms: 1.05x faster                                                                 |
| deepcopy_memo             | 22.1 us                                                         | 21.1 us: 1.05x faster                                                                |
| deepcopy_reduce           | 1.99 us                                                         | 1.95 us: 1.03x faster                                                                |
| pidigits                  | 150 ms                                                          | 151 ms: 1.01x slower                                                                 |
| regex_dna                 | 119 ms                                                          | 120 ms: 1.01x slower                                                                 |
| json_loads                | 14.2 us                                                         | 14.5 us: 1.02x slower                                                                |
| xml_etree_parse           | 90.9 ms                                                         | 94.8 ms: 1.04x slower                                                                |
| bench_thread_pool         | 768 us                                                          | 808 us: 1.05x slower                                                                 |
| telco                     | 4.67 ms                                                         | 4.93 ms: 1.06x slower                                                                |
| xml_etree_iterparse       | 62.3 ms                                                         | 66.0 ms: 1.06x slower                                                                |
| pathlib                   | 75.9 ms                                                         | 80.5 ms: 1.06x slower                                                                |
| python_startup            | 20.3 ms                                                         | 21.7 ms: 1.07x slower                                                                |
| bench_mp_pool             | 64.8 ms                                                         | 69.1 ms: 1.07x slower                                                                |
| python_startup_no_site    | 16.2 ms                                                         | 17.4 ms: 1.08x slower                                                                |
| docutils                  | 1.63 sec                                                        | 1.75 sec: 1.08x slower                                                               |
| sympy_sum                 | 84.4 ms                                                         | 92.1 ms: 1.09x slower                                                                |
| async_generators          | 223 ms                                                          | 244 ms: 1.09x slower                                                                 |
| xml_etree_generate        | 53.2 ms                                                         | 58.1 ms: 1.09x slower                                                                |
| logging_simple            | 5.78 us                                                         | 6.39 us: 1.10x slower                                                                |
| logging_format            | 6.22 us                                                         | 6.89 us: 1.11x slower                                                                |
| sympy_integrate           | 12.2 ms                                                         | 13.5 ms: 1.11x slower                                                                |
| typing_runtime_protocols  | 101 us                                                          | 112 us: 1.11x slower                                                                 |
| sqlglot_optimize          | 32.7 ms                                                         | 36.3 ms: 1.11x slower                                                                |
| mdp                       | 1.31 sec                                                        | 1.46 sec: 1.11x slower                                                               |
| sqlglot_normalize         | 173 ms                                                          | 193 ms: 1.12x slower                                                                 |
| pylint                    | 205 ms                                                          | 229 ms: 1.12x slower                                                                 |
| coroutines                | 12.8 ms                                                         | 14.3 ms: 1.12x slower                                                                |
| dulwich_log               | 38.0 ms                                                         | 42.7 ms: 1.12x slower                                                                |
| generators                | 19.6 ms                                                         | 22.0 ms: 1.12x slower                                                                |
| coverage                  | 42.1 ms                                                         | 47.4 ms: 1.13x slower                                                                |
| xml_etree_process         | 36.4 ms                                                         | 41.1 ms: 1.13x slower                                                                |
| 2to3                      | 207 ms                                                          | 234 ms: 1.13x slower                                                                 |
| meteor_contest            | 69.9 ms                                                         | 79.0 ms: 1.13x slower                                                                |
| crypto_pyaes              | 45.5 ms                                                         | 51.8 ms: 1.14x slower                                                                |
| float                     | 49.7 ms                                                         | 56.6 ms: 1.14x slower                                                                |
| sympy_str                 | 159 ms                                                          | 181 ms: 1.14x slower                                                                 |
| mako                      | 6.36 ms                                                         | 7.25 ms: 1.14x slower                                                                |
| django_template           | 21.7 ms                                                         | 24.7 ms: 1.14x slower                                                                |
| tornado_http              | 81.8 ms                                                         | 93.4 ms: 1.14x slower                                                                |
| asyncio_tcp               | 471 ms                                                          | 539 ms: 1.14x slower                                                                 |
| json_dumps                | 5.61 ms                                                         | 6.43 ms: 1.15x slower                                                                |
| nqueens                   | 56.7 ms                                                         | 64.9 ms: 1.15x slower                                                                |
| sympy_expand              | 271 ms                                                          | 311 ms: 1.15x slower                                                                 |
| scimark_sparse_mat_mult   | 2.50 ms                                                         | 2.88 ms: 1.15x slower                                                                |
| scimark_lu                | 56.6 ms                                                         | 65.5 ms: 1.16x slower                                                                |
| spectral_norm             | 63.7 ms                                                         | 74.1 ms: 1.16x slower                                                                |
| genshi_xml                | 31.6 ms                                                         | 36.8 ms: 1.17x slower                                                                |
| comprehensions            | 10.4 us                                                         | 12.1 us: 1.17x slower                                                                |
| chaos                     | 38.4 ms                                                         | 44.9 ms: 1.17x slower                                                                |
| sqlglot_transpile         | 955 us                                                          | 1.13 ms: 1.18x slower                                                                |
| pyflate                   | 279 ms                                                          | 330 ms: 1.18x slower                                                                 |
| tomli_loads               | 1.35 sec                                                        | 1.61 sec: 1.19x slower                                                               |
| pprint_safe_repr          | 474 ms                                                          | 569 ms: 1.20x slower                                                                 |
| pprint_pformat            | 966 ms                                                          | 1.16 sec: 1.20x slower                                                               |
| raytrace                  | 162 ms                                                          | 196 ms: 1.21x slower                                                                 |
| html5lib                  | 35.0 ms                                                         | 42.3 ms: 1.21x slower                                                                |
| sqlglot_parse             | 748 us                                                          | 906 us: 1.21x slower                                                                 |
| go                        | 82.1 ms                                                         | 99.7 ms: 1.22x slower                                                                |
| logging_silent            | 52.9 ns                                                         | 64.4 ns: 1.22x slower                                                                |
| regex_compile             | 78.0 ms                                                         | 95.0 ms: 1.22x slower                                                                |
| deltablue                 | 1.88 ms                                                         | 2.31 ms: 1.22x slower                                                                |
| richards_super            | 30.2 ms                                                         | 37.0 ms: 1.23x slower                                                                |
| richards                  | 26.7 ms                                                         | 32.8 ms: 1.23x slower                                                                |
| fannkuch                  | 243 ms                                                          | 301 ms: 1.24x slower                                                                 |
| pickle_pure_python        | 175 us                                                          | 217 us: 1.24x slower                                                                 |
| hexiom                    | 3.72 ms                                                         | 4.61 ms: 1.24x slower                                                                |
| scimark_fft               | 171 ms                                                          | 212 ms: 1.24x slower                                                                 |
| genshi_text               | 14.4 ms                                                         | 17.9 ms: 1.25x slower                                                                |
| asyncio_tcp_ssl           | 1.48 sec                                                        | 1.85 sec: 1.25x slower                                                               |
| scimark_sor               | 75.3 ms                                                         | 96.5 ms: 1.28x slower                                                                |
| unpickle_pure_python      | 122 us                                                          | 157 us: 1.29x slower                                                                 |
| scimark_monte_carlo       | 39.1 ms                                                         | 51.2 ms: 1.31x slower                                                                |
| nbody                     | 67.6 ms                                                         | 92.0 ms: 1.36x slower                                                                |
| Geometric mean            | (ref)                                                           | 1.08x slower                                                                         |

Benchmark hidden because not significant (12): regex_v8, async_tree_none_tg, async_tree_io, json, create_gc_cycles, pycparser, async_tree_cpu_io_mixed, gc_traversal, regex_effbot, async_tree_memoization, async_tree_none, async_tree_cpu_io_mixed_tg
Ignored benchmarks (10) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.11x
- 95% likely to have a slowdown of 1.10x
- 99% likely to have a slowdown of 1.09x

# Memory
- memory change: unknown