# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: experimental_branch_
- machine: windows-amd64
- commit hash: cc98bb5
- commit date: 2024-07-31
- overall geometric mean: 1.07x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 230 ms: 1.11x slower                                                                 |
| docutils       | 1.63 sec                                                        | 1.74 sec: 1.07x slower                                                               |
| html5lib       | 35.0 ms                                                         | 41.5 ms: 1.19x slower                                                                |
| tornado_http   | 81.8 ms                                                         | 92.6 ms: 1.13x slower                                                                |
| Geometric mean | (ref)                                                           | 1.12x slower                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|---------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_io_tg          | 605 ms                                                          | 540 ms: 1.12x faster                                                                 |
| async_tree_memoization_tg | 258 ms                                                          | 247 ms: 1.05x faster                                                                 |
| Geometric mean            | (ref)                                                           | 1.03x faster                                                                         |

Benchmark hidden because not significant (6): async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_io, async_tree_none, async_tree_memoization, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 151 ms: 1.00x slower                                                                 |
| float          | 49.7 ms                                                         | 55.9 ms: 1.12x slower                                                                |
| nbody          | 67.6 ms                                                         | 85.4 ms: 1.26x slower                                                                |
| Geometric mean | (ref)                                                           | 1.13x slower                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_effbot   | 1.58 ms                                                         | 1.59 ms: 1.01x slower                                                                |
| regex_dna      | 119 ms                                                          | 123 ms: 1.03x slower                                                                 |
| regex_compile  | 78.0 ms                                                         | 91.8 ms: 1.18x slower                                                                |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                         |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_loads           | 14.2 us                                                         | 14.3 us: 1.01x slower                                                                |
| xml_etree_parse      | 90.9 ms                                                         | 93.1 ms: 1.02x slower                                                                |
| xml_etree_iterparse  | 62.3 ms                                                         | 65.6 ms: 1.05x slower                                                                |
| xml_etree_generate   | 53.2 ms                                                         | 58.4 ms: 1.10x slower                                                                |
| json_dumps           | 5.61 ms                                                         | 6.22 ms: 1.11x slower                                                                |
| xml_etree_process    | 36.4 ms                                                         | 41.1 ms: 1.13x slower                                                                |
| tomli_loads          | 1.35 sec                                                        | 1.54 sec: 1.14x slower                                                               |
| pickle_pure_python   | 175 us                                                          | 214 us: 1.22x slower                                                                 |
| unpickle_pure_python | 122 us                                                          | 153 us: 1.25x slower                                                                 |
| Geometric mean       | (ref)                                                           | 1.11x slower                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 21.5 ms: 1.06x slower                                                                |
| python_startup_no_site | 16.2 ms                                                         | 17.7 ms: 1.09x slower                                                                |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 7.06 ms: 1.11x slower                                                                |
| django_template | 21.7 ms                                                         | 24.8 ms: 1.14x slower                                                                |
| genshi_xml      | 31.6 ms                                                         | 36.6 ms: 1.16x slower                                                                |
| genshi_text     | 14.4 ms                                                         | 17.4 ms: 1.21x slower                                                                |
| Geometric mean  | (ref)                                                           | 1.15x slower                                                                         |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|---------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| thrift                    | 8.11 ms                                                         | 531 us: 15.26x faster                                                                |
| deepcopy                  | 220 us                                                          | 189 us: 1.16x faster                                                                 |
| async_tree_io_tg          | 605 ms                                                          | 540 ms: 1.12x faster                                                                 |
| deepcopy_memo             | 22.1 us                                                         | 20.9 us: 1.06x faster                                                                |
| async_tree_memoization_tg | 258 ms                                                          | 247 ms: 1.05x faster                                                                 |
| deepcopy_reduce           | 1.99 us                                                         | 1.94 us: 1.03x faster                                                                |
| pidigits                  | 150 ms                                                          | 151 ms: 1.00x slower                                                                 |
| regex_effbot              | 1.58 ms                                                         | 1.59 ms: 1.01x slower                                                                |
| json_loads                | 14.2 us                                                         | 14.3 us: 1.01x slower                                                                |
| create_gc_cycles          | 888 us                                                          | 902 us: 1.02x slower                                                                 |
| xml_etree_parse           | 90.9 ms                                                         | 93.1 ms: 1.02x slower                                                                |
| regex_dna                 | 119 ms                                                          | 123 ms: 1.03x slower                                                                 |
| xml_etree_iterparse       | 62.3 ms                                                         | 65.6 ms: 1.05x slower                                                                |
| bench_thread_pool         | 768 us                                                          | 808 us: 1.05x slower                                                                 |
| python_startup            | 20.3 ms                                                         | 21.5 ms: 1.06x slower                                                                |
| pathlib                   | 75.9 ms                                                         | 80.6 ms: 1.06x slower                                                                |
| bench_mp_pool             | 64.8 ms                                                         | 69.3 ms: 1.07x slower                                                                |
| docutils                  | 1.63 sec                                                        | 1.74 sec: 1.07x slower                                                               |
| telco                     | 4.67 ms                                                         | 5.05 ms: 1.08x slower                                                                |
| sympy_sum                 | 84.4 ms                                                         | 91.4 ms: 1.08x slower                                                                |
| async_generators          | 223 ms                                                          | 243 ms: 1.09x slower                                                                 |
| python_startup_no_site    | 16.2 ms                                                         | 17.7 ms: 1.09x slower                                                                |
| sympy_integrate           | 12.2 ms                                                         | 13.4 ms: 1.09x slower                                                                |
| coroutines                | 12.8 ms                                                         | 14.0 ms: 1.10x slower                                                                |
| xml_etree_generate        | 53.2 ms                                                         | 58.4 ms: 1.10x slower                                                                |
| generators                | 19.6 ms                                                         | 21.5 ms: 1.10x slower                                                                |
| mdp                       | 1.31 sec                                                        | 1.44 sec: 1.10x slower                                                               |
| json_dumps                | 5.61 ms                                                         | 6.22 ms: 1.11x slower                                                                |
| logging_simple            | 5.78 us                                                         | 6.41 us: 1.11x slower                                                                |
| meteor_contest            | 69.9 ms                                                         | 77.5 ms: 1.11x slower                                                                |
| sqlglot_optimize          | 32.7 ms                                                         | 36.3 ms: 1.11x slower                                                                |
| mako                      | 6.36 ms                                                         | 7.06 ms: 1.11x slower                                                                |
| 2to3                      | 207 ms                                                          | 230 ms: 1.11x slower                                                                 |
| asyncio_tcp_ssl           | 1.48 sec                                                        | 1.65 sec: 1.12x slower                                                               |
| pylint                    | 205 ms                                                          | 229 ms: 1.12x slower                                                                 |
| logging_format            | 6.22 us                                                         | 6.98 us: 1.12x slower                                                                |
| float                     | 49.7 ms                                                         | 55.9 ms: 1.12x slower                                                                |
| spectral_norm             | 63.7 ms                                                         | 71.8 ms: 1.13x slower                                                                |
| xml_etree_process         | 36.4 ms                                                         | 41.1 ms: 1.13x slower                                                                |
| sqlglot_normalize         | 173 ms                                                          | 196 ms: 1.13x slower                                                                 |
| typing_runtime_protocols  | 101 us                                                          | 114 us: 1.13x slower                                                                 |
| tornado_http              | 81.8 ms                                                         | 92.6 ms: 1.13x slower                                                                |
| dulwich_log               | 38.0 ms                                                         | 43.1 ms: 1.13x slower                                                                |
| asyncio_tcp               | 471 ms                                                          | 534 ms: 1.13x slower                                                                 |
| sympy_str                 | 159 ms                                                          | 180 ms: 1.13x slower                                                                 |
| tomli_loads               | 1.35 sec                                                        | 1.54 sec: 1.14x slower                                                               |
| sympy_expand              | 271 ms                                                          | 309 ms: 1.14x slower                                                                 |
| django_template           | 21.7 ms                                                         | 24.8 ms: 1.14x slower                                                                |
| scimark_sparse_mat_mult   | 2.50 ms                                                         | 2.87 ms: 1.15x slower                                                                |
| crypto_pyaes              | 45.5 ms                                                         | 52.2 ms: 1.15x slower                                                                |
| coverage                  | 42.1 ms                                                         | 48.7 ms: 1.16x slower                                                                |
| nqueens                   | 56.7 ms                                                         | 65.7 ms: 1.16x slower                                                                |
| genshi_xml                | 31.6 ms                                                         | 36.6 ms: 1.16x slower                                                                |
| scimark_lu                | 56.6 ms                                                         | 65.8 ms: 1.16x slower                                                                |
| sqlglot_transpile         | 955 us                                                          | 1.12 ms: 1.17x slower                                                                |
| chaos                     | 38.4 ms                                                         | 45.0 ms: 1.17x slower                                                                |
| regex_compile             | 78.0 ms                                                         | 91.8 ms: 1.18x slower                                                                |
| pyflate                   | 279 ms                                                          | 328 ms: 1.18x slower                                                                 |
| richards                  | 26.7 ms                                                         | 31.5 ms: 1.18x slower                                                                |
| raytrace                  | 162 ms                                                          | 192 ms: 1.18x slower                                                                 |
| richards_super            | 30.2 ms                                                         | 35.7 ms: 1.18x slower                                                                |
| html5lib                  | 35.0 ms                                                         | 41.5 ms: 1.19x slower                                                                |
| pprint_safe_repr          | 474 ms                                                          | 564 ms: 1.19x slower                                                                 |
| pprint_pformat            | 966 ms                                                          | 1.15 sec: 1.19x slower                                                               |
| comprehensions            | 10.4 us                                                         | 12.4 us: 1.20x slower                                                                |
| sqlglot_parse             | 748 us                                                          | 897 us: 1.20x slower                                                                 |
| deltablue                 | 1.88 ms                                                         | 2.26 ms: 1.20x slower                                                                |
| logging_silent            | 52.9 ns                                                         | 63.6 ns: 1.20x slower                                                                |
| genshi_text               | 14.4 ms                                                         | 17.4 ms: 1.21x slower                                                                |
| scimark_fft               | 171 ms                                                          | 208 ms: 1.22x slower                                                                 |
| go                        | 82.1 ms                                                         | 99.9 ms: 1.22x slower                                                                |
| pickle_pure_python        | 175 us                                                          | 214 us: 1.22x slower                                                                 |
| fannkuch                  | 243 ms                                                          | 302 ms: 1.24x slower                                                                 |
| hexiom                    | 3.72 ms                                                         | 4.62 ms: 1.24x slower                                                                |
| scimark_sor               | 75.3 ms                                                         | 94.3 ms: 1.25x slower                                                                |
| unpickle_pure_python      | 122 us                                                          | 153 us: 1.25x slower                                                                 |
| nbody                     | 67.6 ms                                                         | 85.4 ms: 1.26x slower                                                                |
| scimark_monte_carlo       | 39.1 ms                                                         | 52.7 ms: 1.35x slower                                                                |
| Geometric mean            | (ref)                                                           | 1.07x slower                                                                         |

Benchmark hidden because not significant (10): async_tree_none_tg, regex_v8, async_tree_cpu_io_mixed, json, async_tree_io, async_tree_none, async_tree_memoization, gc_traversal, pycparser, async_tree_cpu_io_mixed_tg
Ignored benchmarks (10) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.09x
- 95% likely to have a slowdown of 1.09x
- 99% likely to have a slowdown of 1.08x

# Memory
- memory change: unknown