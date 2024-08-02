# Results vs. 3.13.0b2

- fork: python
- ref: 6b280a84988ca221b5bd
- machine: windows-amd64
- commit hash: 6b280a8
- commit date: 2024-06-29
- overall geometric mean: 1.02x slower
- HPT reliability: 99.63%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 237 ms: 1.15x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.77 sec: 1.09x slower                                                     |
| html5lib       | 35.0 ms                                                         | 38.9 ms: 1.11x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 84.3 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                           | 1.09x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg          | 605 ms                                                          | 530 ms: 1.14x faster                                                       |
| async_tree_io             | 588 ms                                                          | 544 ms: 1.08x faster                                                       |
| async_tree_none_tg        | 202 ms                                                          | 192 ms: 1.05x faster                                                       |
| async_tree_memoization_tg | 258 ms                                                          | 246 ms: 1.05x faster                                                       |
| async_tree_memoization    | 264 ms                                                          | 256 ms: 1.03x faster                                                       |
| async_tree_none           | 218 ms                                                          | 212 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed   | 389 ms                                                          | 383 ms: 1.02x faster                                                       |
| Geometric mean            | (ref)                                                           | 1.05x faster                                                               |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 51.4 ms: 1.32x faster                                                      |
| float          | 49.7 ms                                                         | 45.6 ms: 1.09x faster                                                      |
| Geometric mean | (ref)                                                           | 1.13x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                          | 121 ms: 1.02x slower                                                       |
| regex_compile  | 78.0 ms                                                         | 90.1 ms: 1.15x slower                                                      |
| regex_v8       | 15.8 ms                                                         | 20.1 ms: 1.28x slower                                                      |
| Geometric mean | (ref)                                                           | 1.10x slower                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.35 sec                                                        | 1.29 sec: 1.05x faster                                                     |
| xml_etree_iterparse  | 62.3 ms                                                         | 62.9 ms: 1.01x slower                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 53.8 ms: 1.01x slower                                                      |
| pickle_pure_python   | 175 us                                                          | 180 us: 1.03x slower                                                       |
| json_dumps           | 5.61 ms                                                         | 5.89 ms: 1.05x slower                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 97.6 ms: 1.07x slower                                                      |
| xml_etree_process    | 36.4 ms                                                         | 39.2 ms: 1.08x slower                                                      |
| unpickle_pure_python | 122 us                                                          | 142 us: 1.16x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.04x slower                                                               |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 22.5 ms: 1.11x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 18.6 ms: 1.15x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.13x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 5.19 ms: 1.23x faster                                                      |
| django_template | 21.7 ms                                                         | 26.9 ms: 1.24x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 18.7 ms: 1.30x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 44.9 ms: 1.42x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.17x slower                                                               |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                    | 8.11 ms                                                         | 518 us: 15.64x faster                                                      |
| spectral_norm             | 63.7 ms                                                         | 45.3 ms: 1.41x faster                                                      |
| deepcopy_memo             | 22.1 us                                                         | 15.8 us: 1.40x faster                                                      |
| nbody                     | 67.6 ms                                                         | 51.4 ms: 1.32x faster                                                      |
| mako                      | 6.36 ms                                                         | 5.19 ms: 1.23x faster                                                      |
| deepcopy                  | 220 us                                                          | 184 us: 1.19x faster                                                       |
| scimark_sparse_mat_mult   | 2.50 ms                                                         | 2.14 ms: 1.17x faster                                                      |
| async_tree_io_tg          | 605 ms                                                          | 530 ms: 1.14x faster                                                       |
| scimark_fft               | 171 ms                                                          | 151 ms: 1.13x faster                                                       |
| crypto_pyaes              | 45.5 ms                                                         | 41.1 ms: 1.11x faster                                                      |
| deepcopy_reduce           | 1.99 us                                                         | 1.81 us: 1.10x faster                                                      |
| fannkuch                  | 243 ms                                                          | 222 ms: 1.09x faster                                                       |
| float                     | 49.7 ms                                                         | 45.6 ms: 1.09x faster                                                      |
| async_tree_io             | 588 ms                                                          | 544 ms: 1.08x faster                                                       |
| json                      | 3.19 ms                                                         | 2.96 ms: 1.08x faster                                                      |
| pyflate                   | 279 ms                                                          | 264 ms: 1.06x faster                                                       |
| async_tree_none_tg        | 202 ms                                                          | 192 ms: 1.05x faster                                                       |
| async_tree_memoization_tg | 258 ms                                                          | 246 ms: 1.05x faster                                                       |
| tomli_loads               | 1.35 sec                                                        | 1.29 sec: 1.05x faster                                                     |
| telco                     | 4.67 ms                                                         | 4.52 ms: 1.03x faster                                                      |
| async_tree_memoization    | 264 ms                                                          | 256 ms: 1.03x faster                                                       |
| async_tree_none           | 218 ms                                                          | 212 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed   | 389 ms                                                          | 383 ms: 1.02x faster                                                       |
| xml_etree_iterparse       | 62.3 ms                                                         | 62.9 ms: 1.01x slower                                                      |
| xml_etree_generate        | 53.2 ms                                                         | 53.8 ms: 1.01x slower                                                      |
| scimark_monte_carlo       | 39.1 ms                                                         | 39.6 ms: 1.01x slower                                                      |
| comprehensions            | 10.4 us                                                         | 10.5 us: 1.01x slower                                                      |
| regex_dna                 | 119 ms                                                          | 121 ms: 1.02x slower                                                       |
| create_gc_cycles          | 888 us                                                          | 907 us: 1.02x slower                                                       |
| pickle_pure_python        | 175 us                                                          | 180 us: 1.03x slower                                                       |
| tornado_http              | 81.8 ms                                                         | 84.3 ms: 1.03x slower                                                      |
| pprint_safe_repr          | 474 ms                                                          | 490 ms: 1.03x slower                                                       |
| logging_format            | 6.22 us                                                         | 6.44 us: 1.03x slower                                                      |
| logging_simple            | 5.78 us                                                         | 5.99 us: 1.04x slower                                                      |
| pprint_pformat            | 966 ms                                                          | 1.00 sec: 1.04x slower                                                     |
| json_dumps                | 5.61 ms                                                         | 5.89 ms: 1.05x slower                                                      |
| meteor_contest            | 69.9 ms                                                         | 74.1 ms: 1.06x slower                                                      |
| chaos                     | 38.4 ms                                                         | 40.9 ms: 1.07x slower                                                      |
| xml_etree_parse           | 90.9 ms                                                         | 97.6 ms: 1.07x slower                                                      |
| xml_etree_process         | 36.4 ms                                                         | 39.2 ms: 1.08x slower                                                      |
| bench_mp_pool             | 64.8 ms                                                         | 70.2 ms: 1.08x slower                                                      |
| pycparser                 | 754 ms                                                          | 820 ms: 1.09x slower                                                       |
| docutils                  | 1.63 sec                                                        | 1.77 sec: 1.09x slower                                                     |
| logging_silent            | 52.9 ns                                                         | 58.1 ns: 1.10x slower                                                      |
| sqlglot_parse             | 748 us                                                          | 823 us: 1.10x slower                                                       |
| mdp                       | 1.31 sec                                                        | 1.44 sec: 1.10x slower                                                     |
| coverage                  | 42.1 ms                                                         | 46.4 ms: 1.10x slower                                                      |
| sqlglot_transpile         | 955 us                                                          | 1.05 ms: 1.10x slower                                                      |
| sympy_sum                 | 84.4 ms                                                         | 93.1 ms: 1.10x slower                                                      |
| nqueens                   | 56.7 ms                                                         | 62.6 ms: 1.10x slower                                                      |
| python_startup            | 20.3 ms                                                         | 22.5 ms: 1.11x slower                                                      |
| html5lib                  | 35.0 ms                                                         | 38.9 ms: 1.11x slower                                                      |
| sqlglot_optimize          | 32.7 ms                                                         | 37.0 ms: 1.13x slower                                                      |
| sympy_str                 | 159 ms                                                          | 182 ms: 1.14x slower                                                       |
| coroutines                | 12.8 ms                                                         | 14.6 ms: 1.14x slower                                                      |
| python_startup_no_site    | 16.2 ms                                                         | 18.6 ms: 1.15x slower                                                      |
| 2to3                      | 207 ms                                                          | 237 ms: 1.15x slower                                                       |
| raytrace                  | 162 ms                                                          | 186 ms: 1.15x slower                                                       |
| sympy_integrate           | 12.2 ms                                                         | 14.1 ms: 1.15x slower                                                      |
| regex_compile             | 78.0 ms                                                         | 90.1 ms: 1.15x slower                                                      |
| pylint                    | 205 ms                                                          | 237 ms: 1.16x slower                                                       |
| sqlglot_normalize         | 173 ms                                                          | 200 ms: 1.16x slower                                                       |
| unpickle_pure_python      | 122 us                                                          | 142 us: 1.16x slower                                                       |
| typing_runtime_protocols  | 101 us                                                          | 118 us: 1.17x slower                                                       |
| sympy_expand              | 271 ms                                                          | 316 ms: 1.17x slower                                                       |
| go                        | 82.1 ms                                                         | 97.8 ms: 1.19x slower                                                      |
| async_generators          | 223 ms                                                          | 271 ms: 1.21x slower                                                       |
| richards_super            | 30.2 ms                                                         | 36.9 ms: 1.22x slower                                                      |
| richards                  | 26.7 ms                                                         | 32.7 ms: 1.23x slower                                                      |
| generators                | 19.6 ms                                                         | 24.0 ms: 1.23x slower                                                      |
| django_template           | 21.7 ms                                                         | 26.9 ms: 1.24x slower                                                      |
| scimark_sor               | 75.3 ms                                                         | 94.3 ms: 1.25x slower                                                      |
| deltablue                 | 1.88 ms                                                         | 2.37 ms: 1.26x slower                                                      |
| regex_v8                  | 15.8 ms                                                         | 20.1 ms: 1.28x slower                                                      |
| hexiom                    | 3.72 ms                                                         | 4.80 ms: 1.29x slower                                                      |
| genshi_text               | 14.4 ms                                                         | 18.7 ms: 1.30x slower                                                      |
| scimark_lu                | 56.6 ms                                                         | 75.0 ms: 1.32x slower                                                      |
| genshi_xml                | 31.6 ms                                                         | 44.9 ms: 1.42x slower                                                      |
| Geometric mean            | (ref)                                                           | 1.02x slower                                                               |

Benchmark hidden because not significant (9): gc_traversal, pathlib, regex_effbot, pidigits, json_loads, async_tree_cpu_io_mixed_tg, bench_thread_pool, asyncio_tcp, asyncio_tcp_ssl
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.63% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown