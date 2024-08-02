# Results vs. 3.13.0b2

- fork: python
- ref: a2bec77d25b11f50362a
- machine: windows-amd64
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.01x faster
- HPT reliability: 87.50%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 233 ms: 1.13x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.77 sec: 1.09x slower                                                     |
| html5lib       | 35.0 ms                                                         | 39.9 ms: 1.14x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 84.3 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                           | 1.10x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg          | 605 ms                                                          | 519 ms: 1.17x faster                                                       |
| async_tree_io             | 588 ms                                                          | 525 ms: 1.12x faster                                                       |
| async_tree_none_tg        | 202 ms                                                          | 186 ms: 1.09x faster                                                       |
| async_tree_memoization_tg | 258 ms                                                          | 241 ms: 1.07x faster                                                       |
| async_tree_none           | 218 ms                                                          | 205 ms: 1.06x faster                                                       |
| async_tree_memoization    | 264 ms                                                          | 250 ms: 1.05x faster                                                       |
| Geometric mean            | (ref)                                                           | 1.07x faster                                                               |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 51.0 ms: 1.33x faster                                                      |
| float          | 49.7 ms                                                         | 45.1 ms: 1.10x faster                                                      |
| pidigits       | 150 ms                                                          | 149 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                           | 1.14x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.58 ms                                                         | 1.57 ms: 1.01x faster                                                      |
| regex_dna      | 119 ms                                                          | 121 ms: 1.02x slower                                                       |
| regex_compile  | 78.0 ms                                                         | 90.5 ms: 1.16x slower                                                      |
| regex_v8       | 15.8 ms                                                         | 20.8 ms: 1.32x slower                                                      |
| Geometric mean | (ref)                                                           | 1.12x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.35 sec                                                        | 1.25 sec: 1.08x faster                                                     |
| xml_etree_iterparse  | 62.3 ms                                                         | 60.7 ms: 1.03x faster                                                      |
| pickle_pure_python   | 175 us                                                          | 173 us: 1.01x faster                                                       |
| xml_etree_generate   | 53.2 ms                                                         | 52.8 ms: 1.01x faster                                                      |
| json_loads           | 14.2 us                                                         | 14.3 us: 1.01x slower                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 92.3 ms: 1.02x slower                                                      |
| xml_etree_process    | 36.4 ms                                                         | 37.4 ms: 1.03x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 5.86 ms: 1.04x slower                                                      |
| unpickle_pure_python | 122 us                                                          | 130 us: 1.07x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.00x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 21.0 ms: 1.04x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 17.5 ms: 1.08x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.06x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 5.16 ms: 1.23x faster                                                      |
| django_template | 21.7 ms                                                         | 25.6 ms: 1.18x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 18.1 ms: 1.26x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 45.2 ms: 1.43x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.15x slower                                                               |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                    | 8.11 ms                                                         | 519 us: 15.63x faster                                                      |
| spectral_norm             | 63.7 ms                                                         | 45.5 ms: 1.40x faster                                                      |
| deepcopy_memo             | 22.1 us                                                         | 15.8 us: 1.40x faster                                                      |
| nbody                     | 67.6 ms                                                         | 51.0 ms: 1.33x faster                                                      |
| mako                      | 6.36 ms                                                         | 5.16 ms: 1.23x faster                                                      |
| deepcopy                  | 220 us                                                          | 181 us: 1.21x faster                                                       |
| scimark_sparse_mat_mult   | 2.50 ms                                                         | 2.12 ms: 1.18x faster                                                      |
| async_tree_io_tg          | 605 ms                                                          | 519 ms: 1.17x faster                                                       |
| scimark_fft               | 171 ms                                                          | 151 ms: 1.14x faster                                                       |
| async_tree_io             | 588 ms                                                          | 525 ms: 1.12x faster                                                       |
| crypto_pyaes              | 45.5 ms                                                         | 40.7 ms: 1.12x faster                                                      |
| deepcopy_reduce           | 1.99 us                                                         | 1.79 us: 1.12x faster                                                      |
| float                     | 49.7 ms                                                         | 45.1 ms: 1.10x faster                                                      |
| fannkuch                  | 243 ms                                                          | 221 ms: 1.10x faster                                                       |
| async_tree_none_tg        | 202 ms                                                          | 186 ms: 1.09x faster                                                       |
| pyflate                   | 279 ms                                                          | 258 ms: 1.08x faster                                                       |
| tomli_loads               | 1.35 sec                                                        | 1.25 sec: 1.08x faster                                                     |
| async_tree_memoization_tg | 258 ms                                                          | 241 ms: 1.07x faster                                                       |
| async_tree_none           | 218 ms                                                          | 205 ms: 1.06x faster                                                       |
| async_tree_memoization    | 264 ms                                                          | 250 ms: 1.05x faster                                                       |
| telco                     | 4.67 ms                                                         | 4.48 ms: 1.04x faster                                                      |
| scimark_monte_carlo       | 39.1 ms                                                         | 37.6 ms: 1.04x faster                                                      |
| xml_etree_iterparse       | 62.3 ms                                                         | 60.7 ms: 1.03x faster                                                      |
| pprint_safe_repr          | 474 ms                                                          | 464 ms: 1.02x faster                                                       |
| pathlib                   | 75.9 ms                                                         | 74.6 ms: 1.02x faster                                                      |
| pickle_pure_python        | 175 us                                                          | 173 us: 1.01x faster                                                       |
| pprint_pformat            | 966 ms                                                          | 953 ms: 1.01x faster                                                       |
| logging_simple            | 5.78 us                                                         | 5.74 us: 1.01x faster                                                      |
| xml_etree_generate        | 53.2 ms                                                         | 52.8 ms: 1.01x faster                                                      |
| regex_effbot              | 1.58 ms                                                         | 1.57 ms: 1.01x faster                                                      |
| logging_format            | 6.22 us                                                         | 6.19 us: 1.01x faster                                                      |
| pidigits                  | 150 ms                                                          | 149 ms: 1.00x faster                                                       |
| json_loads                | 14.2 us                                                         | 14.3 us: 1.01x slower                                                      |
| chaos                     | 38.4 ms                                                         | 38.8 ms: 1.01x slower                                                      |
| create_gc_cycles          | 888 us                                                          | 901 us: 1.01x slower                                                       |
| xml_etree_parse           | 90.9 ms                                                         | 92.3 ms: 1.02x slower                                                      |
| regex_dna                 | 119 ms                                                          | 121 ms: 1.02x slower                                                       |
| xml_etree_process         | 36.4 ms                                                         | 37.4 ms: 1.03x slower                                                      |
| tornado_http              | 81.8 ms                                                         | 84.3 ms: 1.03x slower                                                      |
| python_startup            | 20.3 ms                                                         | 21.0 ms: 1.04x slower                                                      |
| json_dumps                | 5.61 ms                                                         | 5.86 ms: 1.04x slower                                                      |
| bench_thread_pool         | 768 us                                                          | 804 us: 1.05x slower                                                       |
| meteor_contest            | 69.9 ms                                                         | 73.6 ms: 1.05x slower                                                      |
| nqueens                   | 56.7 ms                                                         | 59.9 ms: 1.06x slower                                                      |
| unpickle_pure_python      | 122 us                                                          | 130 us: 1.07x slower                                                       |
| logging_silent            | 52.9 ns                                                         | 56.8 ns: 1.07x slower                                                      |
| sqlglot_parse             | 748 us                                                          | 804 us: 1.07x slower                                                       |
| bench_mp_pool             | 64.8 ms                                                         | 69.6 ms: 1.08x slower                                                      |
| sqlglot_transpile         | 955 us                                                          | 1.03 ms: 1.08x slower                                                      |
| python_startup_no_site    | 16.2 ms                                                         | 17.5 ms: 1.08x slower                                                      |
| coroutines                | 12.8 ms                                                         | 13.8 ms: 1.08x slower                                                      |
| mdp                       | 1.31 sec                                                        | 1.42 sec: 1.08x slower                                                     |
| sqlglot_optimize          | 32.7 ms                                                         | 35.6 ms: 1.09x slower                                                      |
| docutils                  | 1.63 sec                                                        | 1.77 sec: 1.09x slower                                                     |
| pycparser                 | 754 ms                                                          | 822 ms: 1.09x slower                                                       |
| coverage                  | 42.1 ms                                                         | 46.1 ms: 1.09x slower                                                      |
| sqlglot_normalize         | 173 ms                                                          | 190 ms: 1.10x slower                                                       |
| raytrace                  | 162 ms                                                          | 179 ms: 1.10x slower                                                       |
| sympy_sum                 | 84.4 ms                                                         | 92.9 ms: 1.10x slower                                                      |
| typing_runtime_protocols  | 101 us                                                          | 113 us: 1.12x slower                                                       |
| richards_super            | 30.2 ms                                                         | 34.0 ms: 1.13x slower                                                      |
| pylint                    | 205 ms                                                          | 231 ms: 1.13x slower                                                       |
| 2to3                      | 207 ms                                                          | 233 ms: 1.13x slower                                                       |
| sympy_str                 | 159 ms                                                          | 181 ms: 1.14x slower                                                       |
| html5lib                  | 35.0 ms                                                         | 39.9 ms: 1.14x slower                                                      |
| sympy_integrate           | 12.2 ms                                                         | 14.0 ms: 1.14x slower                                                      |
| richards                  | 26.7 ms                                                         | 30.6 ms: 1.15x slower                                                      |
| go                        | 82.1 ms                                                         | 94.2 ms: 1.15x slower                                                      |
| async_generators          | 223 ms                                                          | 257 ms: 1.15x slower                                                       |
| sympy_expand              | 271 ms                                                          | 313 ms: 1.16x slower                                                       |
| regex_compile             | 78.0 ms                                                         | 90.5 ms: 1.16x slower                                                      |
| django_template           | 21.7 ms                                                         | 25.6 ms: 1.18x slower                                                      |
| scimark_sor               | 75.3 ms                                                         | 88.9 ms: 1.18x slower                                                      |
| deltablue                 | 1.88 ms                                                         | 2.25 ms: 1.20x slower                                                      |
| generators                | 19.6 ms                                                         | 23.6 ms: 1.21x slower                                                      |
| hexiom                    | 3.72 ms                                                         | 4.62 ms: 1.24x slower                                                      |
| scimark_lu                | 56.6 ms                                                         | 70.3 ms: 1.24x slower                                                      |
| genshi_text               | 14.4 ms                                                         | 18.1 ms: 1.26x slower                                                      |
| regex_v8                  | 15.8 ms                                                         | 20.8 ms: 1.32x slower                                                      |
| genshi_xml                | 31.6 ms                                                         | 45.2 ms: 1.43x slower                                                      |
| Geometric mean            | (ref)                                                           | 1.01x faster                                                               |

Benchmark hidden because not significant (7): json, asyncio_tcp_ssl, async_tree_cpu_io_mixed, asyncio_tcp, gc_traversal, comprehensions, async_tree_cpu_io_mixed_tg
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 87.50% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown