# Results vs. 3.13.0b2

- fork: mdboom
- ref: remove_pragma
- machine: windows-amd64
- commit hash: a03affd
- commit date: 2024-07-02
- overall geometric mean: 1.01x slower
- HPT reliability: 99.42%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 236 ms: 1.14x slower                                                |
| docutils       | 1.63 sec                                                        | 1.79 sec: 1.10x slower                                              |
| html5lib       | 35.0 ms                                                         | 39.6 ms: 1.13x slower                                               |
| tornado_http   | 81.8 ms                                                         | 85.0 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                           | 1.10x slower                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|---------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io_tg          | 605 ms                                                          | 529 ms: 1.14x faster                                                |
| async_tree_io             | 588 ms                                                          | 541 ms: 1.09x faster                                                |
| async_tree_none_tg        | 202 ms                                                          | 192 ms: 1.05x faster                                                |
| async_tree_memoization_tg | 258 ms                                                          | 247 ms: 1.04x faster                                                |
| async_tree_none           | 218 ms                                                          | 212 ms: 1.03x faster                                                |
| Geometric mean            | (ref)                                                           | 1.05x faster                                                        |

Benchmark hidden because not significant (3): async_tree_memoization, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 49.7 ms: 1.36x faster                                               |
| float          | 49.7 ms                                                         | 46.1 ms: 1.08x faster                                               |
| pidigits       | 150 ms                                                          | 149 ms: 1.00x faster                                                |
| Geometric mean | (ref)                                                           | 1.14x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 1.58 ms                                                         | 1.59 ms: 1.01x slower                                               |
| regex_dna      | 119 ms                                                          | 122 ms: 1.02x slower                                                |
| regex_compile  | 78.0 ms                                                         | 90.2 ms: 1.16x slower                                               |
| regex_v8       | 15.8 ms                                                         | 19.9 ms: 1.26x slower                                               |
| Geometric mean | (ref)                                                           | 1.11x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 1.35 sec                                                        | 1.29 sec: 1.05x faster                                              |
| xml_etree_iterparse  | 62.3 ms                                                         | 60.6 ms: 1.03x faster                                               |
| json_loads           | 14.2 us                                                         | 14.3 us: 1.01x slower                                               |
| xml_etree_parse      | 90.9 ms                                                         | 92.0 ms: 1.01x slower                                               |
| pickle_pure_python   | 175 us                                                          | 182 us: 1.04x slower                                                |
| json_dumps           | 5.61 ms                                                         | 5.86 ms: 1.04x slower                                               |
| xml_etree_process    | 36.4 ms                                                         | 38.5 ms: 1.06x slower                                               |
| unpickle_pure_python | 122 us                                                          | 136 us: 1.11x slower                                                |
| Geometric mean       | (ref)                                                           | 1.02x slower                                                        |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 21.1 ms: 1.04x slower                                               |
| python_startup_no_site | 16.2 ms                                                         | 17.3 ms: 1.07x slower                                               |
| Geometric mean         | (ref)                                                           | 1.05x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 5.30 ms: 1.20x faster                                               |
| django_template | 21.7 ms                                                         | 26.3 ms: 1.21x slower                                               |
| genshi_text     | 14.4 ms                                                         | 18.3 ms: 1.27x slower                                               |
| genshi_xml      | 31.6 ms                                                         | 45.9 ms: 1.45x slower                                               |
| Geometric mean  | (ref)                                                           | 1.17x slower                                                        |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|---------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| thrift                    | 8.11 ms                                                         | 524 us: 15.48x faster                                               |
| spectral_norm             | 63.7 ms                                                         | 45.6 ms: 1.40x faster                                               |
| deepcopy_memo             | 22.1 us                                                         | 15.9 us: 1.39x faster                                               |
| nbody                     | 67.6 ms                                                         | 49.7 ms: 1.36x faster                                               |
| deepcopy                  | 220 us                                                          | 181 us: 1.21x faster                                                |
| scimark_sparse_mat_mult   | 2.50 ms                                                         | 2.08 ms: 1.20x faster                                               |
| mako                      | 6.36 ms                                                         | 5.30 ms: 1.20x faster                                               |
| scimark_fft               | 171 ms                                                          | 147 ms: 1.16x faster                                                |
| async_tree_io_tg          | 605 ms                                                          | 529 ms: 1.14x faster                                                |
| fannkuch                  | 243 ms                                                          | 220 ms: 1.11x faster                                                |
| crypto_pyaes              | 45.5 ms                                                         | 41.1 ms: 1.11x faster                                               |
| async_tree_io             | 588 ms                                                          | 541 ms: 1.09x faster                                                |
| float                     | 49.7 ms                                                         | 46.1 ms: 1.08x faster                                               |
| json                      | 3.19 ms                                                         | 2.96 ms: 1.08x faster                                               |
| asyncio_tcp_ssl           | 1.48 sec                                                        | 1.39 sec: 1.07x faster                                              |
| pyflate                   | 279 ms                                                          | 261 ms: 1.07x faster                                                |
| deepcopy_reduce           | 1.99 us                                                         | 1.87 us: 1.07x faster                                               |
| async_tree_none_tg        | 202 ms                                                          | 192 ms: 1.05x faster                                                |
| tomli_loads               | 1.35 sec                                                        | 1.29 sec: 1.05x faster                                              |
| async_tree_memoization_tg | 258 ms                                                          | 247 ms: 1.04x faster                                                |
| xml_etree_iterparse       | 62.3 ms                                                         | 60.6 ms: 1.03x faster                                               |
| async_tree_none           | 218 ms                                                          | 212 ms: 1.03x faster                                                |
| telco                     | 4.67 ms                                                         | 4.56 ms: 1.02x faster                                               |
| scimark_monte_carlo       | 39.1 ms                                                         | 38.6 ms: 1.01x faster                                               |
| pidigits                  | 150 ms                                                          | 149 ms: 1.00x faster                                                |
| regex_effbot              | 1.58 ms                                                         | 1.59 ms: 1.01x slower                                               |
| gc_traversal              | 1.55 ms                                                         | 1.56 ms: 1.01x slower                                               |
| json_loads                | 14.2 us                                                         | 14.3 us: 1.01x slower                                               |
| comprehensions            | 10.4 us                                                         | 10.5 us: 1.01x slower                                               |
| xml_etree_parse           | 90.9 ms                                                         | 92.0 ms: 1.01x slower                                               |
| logging_format            | 6.22 us                                                         | 6.31 us: 1.01x slower                                               |
| pprint_safe_repr          | 474 ms                                                          | 482 ms: 1.02x slower                                                |
| create_gc_cycles          | 888 us                                                          | 904 us: 1.02x slower                                                |
| logging_simple            | 5.78 us                                                         | 5.91 us: 1.02x slower                                               |
| regex_dna                 | 119 ms                                                          | 122 ms: 1.02x slower                                                |
| asyncio_tcp               | 471 ms                                                          | 483 ms: 1.03x slower                                                |
| bench_thread_pool         | 768 us                                                          | 792 us: 1.03x slower                                                |
| pprint_pformat            | 966 ms                                                          | 1.00 sec: 1.04x slower                                              |
| tornado_http              | 81.8 ms                                                         | 85.0 ms: 1.04x slower                                               |
| pickle_pure_python        | 175 us                                                          | 182 us: 1.04x slower                                                |
| python_startup            | 20.3 ms                                                         | 21.1 ms: 1.04x slower                                               |
| json_dumps                | 5.61 ms                                                         | 5.86 ms: 1.04x slower                                               |
| chaos                     | 38.4 ms                                                         | 40.5 ms: 1.06x slower                                               |
| xml_etree_process         | 36.4 ms                                                         | 38.5 ms: 1.06x slower                                               |
| mdp                       | 1.31 sec                                                        | 1.40 sec: 1.07x slower                                              |
| python_startup_no_site    | 16.2 ms                                                         | 17.3 ms: 1.07x slower                                               |
| logging_silent            | 52.9 ns                                                         | 56.7 ns: 1.07x slower                                               |
| meteor_contest            | 69.9 ms                                                         | 75.0 ms: 1.07x slower                                               |
| bench_mp_pool             | 64.8 ms                                                         | 69.6 ms: 1.08x slower                                               |
| nqueens                   | 56.7 ms                                                         | 61.7 ms: 1.09x slower                                               |
| coverage                  | 42.1 ms                                                         | 46.2 ms: 1.10x slower                                               |
| docutils                  | 1.63 sec                                                        | 1.79 sec: 1.10x slower                                              |
| sqlglot_parse             | 748 us                                                          | 827 us: 1.11x slower                                                |
| sqlglot_transpile         | 955 us                                                          | 1.06 ms: 1.11x slower                                               |
| unpickle_pure_python      | 122 us                                                          | 136 us: 1.11x slower                                                |
| sqlglot_optimize          | 32.7 ms                                                         | 36.6 ms: 1.12x slower                                               |
| sympy_sum                 | 84.4 ms                                                         | 94.4 ms: 1.12x slower                                               |
| coroutines                | 12.8 ms                                                         | 14.3 ms: 1.12x slower                                               |
| sqlglot_normalize         | 173 ms                                                          | 196 ms: 1.13x slower                                                |
| typing_runtime_protocols  | 101 us                                                          | 114 us: 1.13x slower                                                |
| html5lib                  | 35.0 ms                                                         | 39.6 ms: 1.13x slower                                               |
| 2to3                      | 207 ms                                                          | 236 ms: 1.14x slower                                                |
| pycparser                 | 754 ms                                                          | 862 ms: 1.14x slower                                                |
| richards                  | 26.7 ms                                                         | 30.6 ms: 1.15x slower                                               |
| raytrace                  | 162 ms                                                          | 186 ms: 1.15x slower                                                |
| sympy_integrate           | 12.2 ms                                                         | 14.1 ms: 1.15x slower                                               |
| sympy_str                 | 159 ms                                                          | 183 ms: 1.15x slower                                                |
| pylint                    | 205 ms                                                          | 236 ms: 1.15x slower                                                |
| regex_compile             | 78.0 ms                                                         | 90.2 ms: 1.16x slower                                               |
| richards_super            | 30.2 ms                                                         | 35.0 ms: 1.16x slower                                               |
| sympy_expand              | 271 ms                                                          | 316 ms: 1.17x slower                                                |
| go                        | 82.1 ms                                                         | 96.8 ms: 1.18x slower                                               |
| async_generators          | 223 ms                                                          | 270 ms: 1.21x slower                                                |
| django_template           | 21.7 ms                                                         | 26.3 ms: 1.21x slower                                               |
| scimark_sor               | 75.3 ms                                                         | 92.0 ms: 1.22x slower                                               |
| deltablue                 | 1.88 ms                                                         | 2.32 ms: 1.23x slower                                               |
| generators                | 19.6 ms                                                         | 24.1 ms: 1.23x slower                                               |
| hexiom                    | 3.72 ms                                                         | 4.69 ms: 1.26x slower                                               |
| regex_v8                  | 15.8 ms                                                         | 19.9 ms: 1.26x slower                                               |
| genshi_text               | 14.4 ms                                                         | 18.3 ms: 1.27x slower                                               |
| scimark_lu                | 56.6 ms                                                         | 76.4 ms: 1.35x slower                                               |
| genshi_xml                | 31.6 ms                                                         | 45.9 ms: 1.45x slower                                               |
| Geometric mean            | (ref)                                                           | 1.01x slower                                                        |

Benchmark hidden because not significant (5): async_tree_memoization, async_tree_cpu_io_mixed, pathlib, xml_etree_generate, async_tree_cpu_io_mixed_tg
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.42% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown