# Results vs. 3.13.0b2

- fork: python
- ref: 6343486eb60ac5a9e154
- machine: windows-amd64
- commit hash: 6343486
- commit date: 2024-07-02
- overall geometric mean: 1.04x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-pythonperf1-amd64-python-6343486eb60ac5a9e154-3.14.0a0-6343486 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 223 ms: 1.08x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.68 sec: 1.04x slower                                                     |
| html5lib       | 35.0 ms                                                         | 38.4 ms: 1.10x slower                                                      |
| Geometric mean | (ref)                                                           | 1.05x slower                                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-pythonperf1-amd64-python-6343486eb60ac5a9e154-3.14.0a0-6343486 |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg          | 605 ms                                                          | 525 ms: 1.15x faster                                                       |
| async_tree_io             | 588 ms                                                          | 539 ms: 1.09x faster                                                       |
| async_tree_memoization_tg | 258 ms                                                          | 244 ms: 1.06x faster                                                       |
| async_tree_none_tg        | 202 ms                                                          | 191 ms: 1.06x faster                                                       |
| async_tree_memoization    | 264 ms                                                          | 255 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed   | 389 ms                                                          | 380 ms: 1.02x faster                                                       |
| Geometric mean            | (ref)                                                           | 1.05x faster                                                               |

Benchmark hidden because not significant (2): async_tree_none, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-pythonperf1-amd64-python-6343486eb60ac5a9e154-3.14.0a0-6343486 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 150 ms: 1.00x slower                                                       |
| float          | 49.7 ms                                                         | 56.3 ms: 1.13x slower                                                      |
| nbody          | 67.6 ms                                                         | 79.9 ms: 1.18x slower                                                      |
| Geometric mean | (ref)                                                           | 1.10x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-pythonperf1-amd64-python-6343486eb60ac5a9e154-3.14.0a0-6343486 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.58 ms                                                         | 1.61 ms: 1.02x slower                                                      |
| regex_dna      | 119 ms                                                          | 122 ms: 1.03x slower                                                       |
| regex_compile  | 78.0 ms                                                         | 85.4 ms: 1.09x slower                                                      |
| Geometric mean | (ref)                                                           | 1.06x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-pythonperf1-amd64-python-6343486eb60ac5a9e154-3.14.0a0-6343486 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 14.2 us                                                         | 14.4 us: 1.01x slower                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 93.9 ms: 1.03x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 65.9 ms: 1.06x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 5.99 ms: 1.07x slower                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 57.9 ms: 1.09x slower                                                      |
| xml_etree_process    | 36.4 ms                                                         | 40.6 ms: 1.12x slower                                                      |
| tomli_loads          | 1.35 sec                                                        | 1.55 sec: 1.15x slower                                                     |
| pickle_pure_python   | 175 us                                                          | 205 us: 1.17x slower                                                       |
| unpickle_pure_python | 122 us                                                          | 150 us: 1.23x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.10x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-pythonperf1-amd64-python-6343486eb60ac5a9e154-3.14.0a0-6343486 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 20.8 ms: 1.03x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 17.0 ms: 1.05x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.04x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-pythonperf1-amd64-python-6343486eb60ac5a9e154-3.14.0a0-6343486 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 21.7 ms                                                         | 24.2 ms: 1.12x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 35.9 ms: 1.14x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 16.4 ms: 1.14x slower                                                      |
| mako            | 6.36 ms                                                         | 7.64 ms: 1.20x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.15x slower                                                               |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-pythonperf1-amd64-python-6343486eb60ac5a9e154-3.14.0a0-6343486 |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                    | 8.11 ms                                                         | 527 us: 15.38x faster                                                      |
| deepcopy                  | 220 us                                                          | 183 us: 1.20x faster                                                       |
| async_tree_io_tg          | 605 ms                                                          | 525 ms: 1.15x faster                                                       |
| async_tree_io             | 588 ms                                                          | 539 ms: 1.09x faster                                                       |
| json                      | 3.19 ms                                                         | 2.98 ms: 1.07x faster                                                      |
| deepcopy_memo             | 22.1 us                                                         | 20.8 us: 1.06x faster                                                      |
| async_tree_memoization_tg | 258 ms                                                          | 244 ms: 1.06x faster                                                       |
| async_tree_none_tg        | 202 ms                                                          | 191 ms: 1.06x faster                                                       |
| deepcopy_reduce           | 1.99 us                                                         | 1.89 us: 1.06x faster                                                      |
| async_tree_memoization    | 264 ms                                                          | 255 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed   | 389 ms                                                          | 380 ms: 1.02x faster                                                       |
| gc_traversal              | 1.55 ms                                                         | 1.54 ms: 1.01x faster                                                      |
| pidigits                  | 150 ms                                                          | 150 ms: 1.00x slower                                                       |
| json_loads                | 14.2 us                                                         | 14.4 us: 1.01x slower                                                      |
| regex_effbot              | 1.58 ms                                                         | 1.61 ms: 1.02x slower                                                      |
| bench_mp_pool             | 64.8 ms                                                         | 66.1 ms: 1.02x slower                                                      |
| python_startup            | 20.3 ms                                                         | 20.8 ms: 1.03x slower                                                      |
| regex_dna                 | 119 ms                                                          | 122 ms: 1.03x slower                                                       |
| xml_etree_parse           | 90.9 ms                                                         | 93.9 ms: 1.03x slower                                                      |
| docutils                  | 1.63 sec                                                        | 1.68 sec: 1.04x slower                                                     |
| sympy_sum                 | 84.4 ms                                                         | 88.1 ms: 1.04x slower                                                      |
| mdp                       | 1.31 sec                                                        | 1.37 sec: 1.05x slower                                                     |
| python_startup_no_site    | 16.2 ms                                                         | 17.0 ms: 1.05x slower                                                      |
| xml_etree_iterparse       | 62.3 ms                                                         | 65.9 ms: 1.06x slower                                                      |
| sympy_integrate           | 12.2 ms                                                         | 13.0 ms: 1.06x slower                                                      |
| spectral_norm             | 63.7 ms                                                         | 67.6 ms: 1.06x slower                                                      |
| telco                     | 4.67 ms                                                         | 4.97 ms: 1.06x slower                                                      |
| sqlglot_optimize          | 32.7 ms                                                         | 34.9 ms: 1.07x slower                                                      |
| json_dumps                | 5.61 ms                                                         | 5.99 ms: 1.07x slower                                                      |
| sqlglot_normalize         | 173 ms                                                          | 185 ms: 1.07x slower                                                       |
| coverage                  | 42.1 ms                                                         | 45.2 ms: 1.07x slower                                                      |
| logging_format            | 6.22 us                                                         | 6.70 us: 1.08x slower                                                      |
| sympy_str                 | 159 ms                                                          | 172 ms: 1.08x slower                                                       |
| 2to3                      | 207 ms                                                          | 223 ms: 1.08x slower                                                       |
| logging_simple            | 5.78 us                                                         | 6.26 us: 1.08x slower                                                      |
| sympy_expand              | 271 ms                                                          | 293 ms: 1.08x slower                                                       |
| xml_etree_generate        | 53.2 ms                                                         | 57.9 ms: 1.09x slower                                                      |
| async_generators          | 223 ms                                                          | 243 ms: 1.09x slower                                                       |
| regex_compile             | 78.0 ms                                                         | 85.4 ms: 1.09x slower                                                      |
| html5lib                  | 35.0 ms                                                         | 38.4 ms: 1.10x slower                                                      |
| typing_runtime_protocols  | 101 us                                                          | 112 us: 1.11x slower                                                       |
| nqueens                   | 56.7 ms                                                         | 62.7 ms: 1.11x slower                                                      |
| richards_super            | 30.2 ms                                                         | 33.4 ms: 1.11x slower                                                      |
| richards                  | 26.7 ms                                                         | 29.7 ms: 1.11x slower                                                      |
| scimark_sor               | 75.3 ms                                                         | 83.9 ms: 1.11x slower                                                      |
| xml_etree_process         | 36.4 ms                                                         | 40.6 ms: 1.12x slower                                                      |
| pyflate                   | 279 ms                                                          | 311 ms: 1.12x slower                                                       |
| django_template           | 21.7 ms                                                         | 24.2 ms: 1.12x slower                                                      |
| meteor_contest            | 69.9 ms                                                         | 78.3 ms: 1.12x slower                                                      |
| raytrace                  | 162 ms                                                          | 182 ms: 1.12x slower                                                       |
| pprint_pformat            | 966 ms                                                          | 1.09 sec: 1.13x slower                                                     |
| crypto_pyaes              | 45.5 ms                                                         | 51.2 ms: 1.13x slower                                                      |
| chaos                     | 38.4 ms                                                         | 43.2 ms: 1.13x slower                                                      |
| scimark_lu                | 56.6 ms                                                         | 63.8 ms: 1.13x slower                                                      |
| pprint_safe_repr          | 474 ms                                                          | 535 ms: 1.13x slower                                                       |
| go                        | 82.1 ms                                                         | 92.9 ms: 1.13x slower                                                      |
| float                     | 49.7 ms                                                         | 56.3 ms: 1.13x slower                                                      |
| genshi_xml                | 31.6 ms                                                         | 35.9 ms: 1.14x slower                                                      |
| genshi_text               | 14.4 ms                                                         | 16.4 ms: 1.14x slower                                                      |
| comprehensions            | 10.4 us                                                         | 11.9 us: 1.15x slower                                                      |
| tomli_loads               | 1.35 sec                                                        | 1.55 sec: 1.15x slower                                                     |
| deltablue                 | 1.88 ms                                                         | 2.17 ms: 1.15x slower                                                      |
| hexiom                    | 3.72 ms                                                         | 4.29 ms: 1.15x slower                                                      |
| generators                | 19.6 ms                                                         | 22.6 ms: 1.16x slower                                                      |
| sqlglot_transpile         | 955 us                                                          | 1.10 ms: 1.16x slower                                                      |
| pickle_pure_python        | 175 us                                                          | 205 us: 1.17x slower                                                       |
| coroutines                | 12.8 ms                                                         | 14.9 ms: 1.17x slower                                                      |
| fannkuch                  | 243 ms                                                          | 285 ms: 1.17x slower                                                       |
| nbody                     | 67.6 ms                                                         | 79.9 ms: 1.18x slower                                                      |
| sqlglot_parse             | 748 us                                                          | 889 us: 1.19x slower                                                       |
| scimark_sparse_mat_mult   | 2.50 ms                                                         | 2.99 ms: 1.19x slower                                                      |
| mako                      | 6.36 ms                                                         | 7.64 ms: 1.20x slower                                                      |
| logging_silent            | 52.9 ns                                                         | 64.7 ns: 1.22x slower                                                      |
| unpickle_pure_python      | 122 us                                                          | 150 us: 1.23x slower                                                       |
| scimark_monte_carlo       | 39.1 ms                                                         | 48.1 ms: 1.23x slower                                                      |
| scimark_fft               | 171 ms                                                          | 211 ms: 1.24x slower                                                       |
| Geometric mean            | (ref)                                                           | 1.04x slower                                                               |

Benchmark hidden because not significant (11): async_tree_none, tornado_http, bench_thread_pool, pathlib, create_gc_cycles, async_tree_cpu_io_mixed_tg, pycparser, asyncio_tcp, asyncio_tcp_ssl, pylint, regex_v8
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown