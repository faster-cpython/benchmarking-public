# Results vs. 3.13.0b2

- fork: python
- ref: 68e279b37aae3019979a
- machine: windows-amd64
- commit hash: 68e279b
- commit date: 2024-07-07
- overall geometric mean: 1.01x faster
- HPT reliability: 88.12%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 230 ms: 1.11x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.74 sec: 1.07x slower                                                     |
| html5lib       | 35.0 ms                                                         | 38.1 ms: 1.09x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 84.4 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                           | 1.08x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg          | 605 ms                                                          | 516 ms: 1.17x faster                                                       |
| async_tree_io             | 588 ms                                                          | 519 ms: 1.13x faster                                                       |
| async_tree_none_tg        | 202 ms                                                          | 186 ms: 1.08x faster                                                       |
| async_tree_memoization_tg | 258 ms                                                          | 242 ms: 1.07x faster                                                       |
| async_tree_none           | 218 ms                                                          | 206 ms: 1.06x faster                                                       |
| async_tree_memoization    | 264 ms                                                          | 252 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed   | 389 ms                                                          | 382 ms: 1.02x faster                                                       |
| Geometric mean            | (ref)                                                           | 1.07x faster                                                               |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 52.2 ms: 1.30x faster                                                      |
| float          | 49.7 ms                                                         | 45.0 ms: 1.11x faster                                                      |
| pidigits       | 150 ms                                                          | 149 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                           | 1.13x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                          | 116 ms: 1.02x faster                                                       |
| regex_effbot   | 1.58 ms                                                         | 1.57 ms: 1.01x faster                                                      |
| regex_compile  | 78.0 ms                                                         | 87.7 ms: 1.12x slower                                                      |
| regex_v8       | 15.8 ms                                                         | 19.9 ms: 1.26x slower                                                      |
| Geometric mean | (ref)                                                           | 1.08x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.35 sec                                                        | 1.25 sec: 1.08x faster                                                     |
| xml_etree_generate   | 53.2 ms                                                         | 51.8 ms: 1.03x faster                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 60.9 ms: 1.02x faster                                                      |
| pickle_pure_python   | 175 us                                                          | 174 us: 1.01x faster                                                       |
| json_dumps           | 5.61 ms                                                         | 5.68 ms: 1.01x slower                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 92.1 ms: 1.01x slower                                                      |
| xml_etree_process    | 36.4 ms                                                         | 37.1 ms: 1.02x slower                                                      |
| unpickle_pure_python | 122 us                                                          | 127 us: 1.04x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.01x faster                                                               |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 21.1 ms: 1.04x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 17.4 ms: 1.08x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.06x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 5.10 ms: 1.25x faster                                                      |
| genshi_text     | 14.4 ms                                                         | 17.9 ms: 1.25x slower                                                      |
| django_template | 21.7 ms                                                         | 27.1 ms: 1.25x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 44.2 ms: 1.40x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.15x slower                                                               |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                    | 8.11 ms                                                         | 518 us: 15.64x faster                                                      |
| deepcopy_memo             | 22.1 us                                                         | 15.7 us: 1.41x faster                                                      |
| spectral_norm             | 63.7 ms                                                         | 45.7 ms: 1.40x faster                                                      |
| nbody                     | 67.6 ms                                                         | 52.2 ms: 1.30x faster                                                      |
| mako                      | 6.36 ms                                                         | 5.10 ms: 1.25x faster                                                      |
| deepcopy                  | 220 us                                                          | 180 us: 1.22x faster                                                       |
| async_tree_io_tg          | 605 ms                                                          | 516 ms: 1.17x faster                                                       |
| scimark_sparse_mat_mult   | 2.50 ms                                                         | 2.15 ms: 1.16x faster                                                      |
| scimark_fft               | 171 ms                                                          | 149 ms: 1.14x faster                                                       |
| async_tree_io             | 588 ms                                                          | 519 ms: 1.13x faster                                                       |
| crypto_pyaes              | 45.5 ms                                                         | 41.1 ms: 1.11x faster                                                      |
| float                     | 49.7 ms                                                         | 45.0 ms: 1.11x faster                                                      |
| deepcopy_reduce           | 1.99 us                                                         | 1.83 us: 1.09x faster                                                      |
| asyncio_tcp_ssl           | 1.48 sec                                                        | 1.36 sec: 1.09x faster                                                     |
| async_tree_none_tg        | 202 ms                                                          | 186 ms: 1.08x faster                                                       |
| tomli_loads               | 1.35 sec                                                        | 1.25 sec: 1.08x faster                                                     |
| pyflate                   | 279 ms                                                          | 258 ms: 1.08x faster                                                       |
| json                      | 3.19 ms                                                         | 2.96 ms: 1.08x faster                                                      |
| async_tree_memoization_tg | 258 ms                                                          | 242 ms: 1.07x faster                                                       |
| async_tree_none           | 218 ms                                                          | 206 ms: 1.06x faster                                                       |
| fannkuch                  | 243 ms                                                          | 230 ms: 1.06x faster                                                       |
| async_tree_memoization    | 264 ms                                                          | 252 ms: 1.05x faster                                                       |
| telco                     | 4.67 ms                                                         | 4.48 ms: 1.04x faster                                                      |
| scimark_monte_carlo       | 39.1 ms                                                         | 37.9 ms: 1.03x faster                                                      |
| xml_etree_generate        | 53.2 ms                                                         | 51.8 ms: 1.03x faster                                                      |
| xml_etree_iterparse       | 62.3 ms                                                         | 60.9 ms: 1.02x faster                                                      |
| regex_dna                 | 119 ms                                                          | 116 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed   | 389 ms                                                          | 382 ms: 1.02x faster                                                       |
| pprint_safe_repr          | 474 ms                                                          | 466 ms: 1.02x faster                                                       |
| pprint_pformat            | 966 ms                                                          | 952 ms: 1.01x faster                                                       |
| regex_effbot              | 1.58 ms                                                         | 1.57 ms: 1.01x faster                                                      |
| pickle_pure_python        | 175 us                                                          | 174 us: 1.01x faster                                                       |
| comprehensions            | 10.4 us                                                         | 10.3 us: 1.01x faster                                                      |
| pidigits                  | 150 ms                                                          | 149 ms: 1.01x faster                                                       |
| logging_format            | 6.22 us                                                         | 6.28 us: 1.01x slower                                                      |
| logging_simple            | 5.78 us                                                         | 5.84 us: 1.01x slower                                                      |
| json_dumps                | 5.61 ms                                                         | 5.68 ms: 1.01x slower                                                      |
| xml_etree_parse           | 90.9 ms                                                         | 92.1 ms: 1.01x slower                                                      |
| create_gc_cycles          | 888 us                                                          | 902 us: 1.02x slower                                                       |
| xml_etree_process         | 36.4 ms                                                         | 37.1 ms: 1.02x slower                                                      |
| tornado_http              | 81.8 ms                                                         | 84.4 ms: 1.03x slower                                                      |
| python_startup            | 20.3 ms                                                         | 21.1 ms: 1.04x slower                                                      |
| unpickle_pure_python      | 122 us                                                          | 127 us: 1.04x slower                                                       |
| chaos                     | 38.4 ms                                                         | 40.1 ms: 1.05x slower                                                      |
| bench_mp_pool             | 64.8 ms                                                         | 68.7 ms: 1.06x slower                                                      |
| logging_silent            | 52.9 ns                                                         | 56.3 ns: 1.06x slower                                                      |
| coroutines                | 12.8 ms                                                         | 13.6 ms: 1.07x slower                                                      |
| meteor_contest            | 69.9 ms                                                         | 74.7 ms: 1.07x slower                                                      |
| docutils                  | 1.63 sec                                                        | 1.74 sec: 1.07x slower                                                     |
| sqlglot_optimize          | 32.7 ms                                                         | 35.1 ms: 1.07x slower                                                      |
| sqlglot_parse             | 748 us                                                          | 805 us: 1.08x slower                                                       |
| python_startup_no_site    | 16.2 ms                                                         | 17.4 ms: 1.08x slower                                                      |
| sqlglot_normalize         | 173 ms                                                          | 186 ms: 1.08x slower                                                       |
| sqlglot_transpile         | 955 us                                                          | 1.03 ms: 1.08x slower                                                      |
| html5lib                  | 35.0 ms                                                         | 38.1 ms: 1.09x slower                                                      |
| nqueens                   | 56.7 ms                                                         | 61.7 ms: 1.09x slower                                                      |
| sympy_sum                 | 84.4 ms                                                         | 92.2 ms: 1.09x slower                                                      |
| richards                  | 26.7 ms                                                         | 29.3 ms: 1.10x slower                                                      |
| richards_super            | 30.2 ms                                                         | 33.2 ms: 1.10x slower                                                      |
| coverage                  | 42.1 ms                                                         | 46.4 ms: 1.10x slower                                                      |
| typing_runtime_protocols  | 101 us                                                          | 112 us: 1.11x slower                                                       |
| 2to3                      | 207 ms                                                          | 230 ms: 1.11x slower                                                       |
| sympy_str                 | 159 ms                                                          | 177 ms: 1.11x slower                                                       |
| pylint                    | 205 ms                                                          | 228 ms: 1.11x slower                                                       |
| regex_compile             | 78.0 ms                                                         | 87.7 ms: 1.12x slower                                                      |
| sympy_expand              | 271 ms                                                          | 305 ms: 1.13x slower                                                       |
| raytrace                  | 162 ms                                                          | 184 ms: 1.13x slower                                                       |
| sympy_integrate           | 12.2 ms                                                         | 13.9 ms: 1.13x slower                                                      |
| async_generators          | 223 ms                                                          | 253 ms: 1.13x slower                                                       |
| go                        | 82.1 ms                                                         | 93.6 ms: 1.14x slower                                                      |
| mdp                       | 1.31 sec                                                        | 1.50 sec: 1.14x slower                                                     |
| scimark_sor               | 75.3 ms                                                         | 87.9 ms: 1.17x slower                                                      |
| generators                | 19.6 ms                                                         | 22.8 ms: 1.17x slower                                                      |
| deltablue                 | 1.88 ms                                                         | 2.25 ms: 1.20x slower                                                      |
| scimark_lu                | 56.6 ms                                                         | 68.5 ms: 1.21x slower                                                      |
| hexiom                    | 3.72 ms                                                         | 4.64 ms: 1.24x slower                                                      |
| genshi_text               | 14.4 ms                                                         | 17.9 ms: 1.25x slower                                                      |
| django_template           | 21.7 ms                                                         | 27.1 ms: 1.25x slower                                                      |
| regex_v8                  | 15.8 ms                                                         | 19.9 ms: 1.26x slower                                                      |
| genshi_xml                | 31.6 ms                                                         | 44.2 ms: 1.40x slower                                                      |
| Geometric mean            | (ref)                                                           | 1.01x faster                                                               |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed_tg, gc_traversal, bench_thread_pool, pathlib, json_loads, asyncio_tcp, pycparser
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 88.12% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown