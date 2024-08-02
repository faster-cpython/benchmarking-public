# Results vs. 3.13.0b2

- fork: python
- ref: 6725c78d376eadb01a9d
- machine: windows-amd64
- commit hash: 6725c78
- commit date: 2024-06-04
- overall geometric mean: 1.03x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.02x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 229 ms: 1.11x slower                                                        |
| chameleon      | 4.80 ms                                                         | 4.94 ms: 1.03x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.78 sec: 1.09x slower                                                      |
| html5lib       | 35.0 ms                                                         | 37.5 ms: 1.07x slower                                                       |
| tornado_http   | 81.8 ms                                                         | 86.1 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                           | 1.07x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|---------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed   | 389 ms                                                          | 402 ms: 1.03x slower                                                        |
| async_tree_io_tg          | 605 ms                                                          | 625 ms: 1.03x slower                                                        |
| async_tree_none           | 218 ms                                                          | 230 ms: 1.05x slower                                                        |
| async_tree_memoization    | 264 ms                                                          | 278 ms: 1.05x slower                                                        |
| async_tree_memoization_tg | 258 ms                                                          | 273 ms: 1.06x slower                                                        |
| async_tree_none_tg        | 202 ms                                                          | 216 ms: 1.07x slower                                                        |
| Geometric mean            | (ref)                                                           | 1.04x slower                                                                |

Benchmark hidden because not significant (2): async_tree_io, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 51.1 ms: 1.32x faster                                                       |
| float          | 49.7 ms                                                         | 43.7 ms: 1.14x faster                                                       |
| Geometric mean | (ref)                                                           | 1.15x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.58 ms                                                         | 1.62 ms: 1.02x slower                                                       |
| regex_dna      | 119 ms                                                          | 124 ms: 1.04x slower                                                        |
| regex_compile  | 78.0 ms                                                         | 87.7 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.35 sec                                                        | 1.22 sec: 1.11x faster                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 51.1 ms: 1.04x faster                                                       |
| pickle_list          | 2.90 us                                                         | 2.81 us: 1.03x faster                                                       |
| xml_etree_iterparse  | 62.3 ms                                                         | 60.5 ms: 1.03x faster                                                       |
| pickle_pure_python   | 175 us                                                          | 172 us: 1.02x faster                                                        |
| pickle_dict          | 18.1 us                                                         | 17.9 us: 1.01x faster                                                       |
| xml_etree_parse      | 90.9 ms                                                         | 90.2 ms: 1.01x faster                                                       |
| json_loads           | 14.2 us                                                         | 14.1 us: 1.01x faster                                                       |
| xml_etree_process    | 36.4 ms                                                         | 36.3 ms: 1.00x faster                                                       |
| unpickle             | 8.40 us                                                         | 8.54 us: 1.02x slower                                                       |
| json_dumps           | 5.61 ms                                                         | 5.74 ms: 1.02x slower                                                       |
| unpickle_pure_python | 122 us                                                          | 126 us: 1.04x slower                                                        |
| pickle               | 7.11 us                                                         | 7.42 us: 1.04x slower                                                       |
| unpickle_list        | 2.62 us                                                         | 2.85 us: 1.09x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.00x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 21.9 ms: 1.08x slower                                                       |
| python_startup_no_site | 16.2 ms                                                         | 17.9 ms: 1.11x slower                                                       |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 5.02 ms: 1.27x faster                                                       |
| django_template | 21.7 ms                                                         | 25.8 ms: 1.19x slower                                                       |
| genshi_text     | 14.4 ms                                                         | 17.8 ms: 1.24x slower                                                       |
| genshi_xml      | 31.6 ms                                                         | 44.6 ms: 1.41x slower                                                       |
| Geometric mean  | (ref)                                                           | 1.13x slower                                                                |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|---------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| spectral_norm             | 63.7 ms                                                         | 44.8 ms: 1.42x faster                                                       |
| nbody                     | 67.6 ms                                                         | 51.1 ms: 1.32x faster                                                       |
| mako                      | 6.36 ms                                                         | 5.02 ms: 1.27x faster                                                       |
| scimark_sparse_mat_mult   | 2.50 ms                                                         | 2.04 ms: 1.23x faster                                                       |
| scimark_fft               | 171 ms                                                          | 147 ms: 1.16x faster                                                        |
| float                     | 49.7 ms                                                         | 43.7 ms: 1.14x faster                                                       |
| fannkuch                  | 243 ms                                                          | 215 ms: 1.13x faster                                                        |
| crypto_pyaes              | 45.5 ms                                                         | 40.8 ms: 1.11x faster                                                       |
| tomli_loads               | 1.35 sec                                                        | 1.22 sec: 1.11x faster                                                      |
| json                      | 3.19 ms                                                         | 2.90 ms: 1.10x faster                                                       |
| deepcopy_memo             | 22.1 us                                                         | 20.3 us: 1.09x faster                                                       |
| pyflate                   | 279 ms                                                          | 259 ms: 1.08x faster                                                        |
| pprint_safe_repr          | 474 ms                                                          | 452 ms: 1.05x faster                                                        |
| xml_etree_generate        | 53.2 ms                                                         | 51.1 ms: 1.04x faster                                                       |
| pprint_pformat            | 966 ms                                                          | 930 ms: 1.04x faster                                                        |
| pickle_list               | 2.90 us                                                         | 2.81 us: 1.03x faster                                                       |
| scimark_monte_carlo       | 39.1 ms                                                         | 37.9 ms: 1.03x faster                                                       |
| telco                     | 4.67 ms                                                         | 4.52 ms: 1.03x faster                                                       |
| xml_etree_iterparse       | 62.3 ms                                                         | 60.5 ms: 1.03x faster                                                       |
| comprehensions            | 10.4 us                                                         | 10.2 us: 1.02x faster                                                       |
| pickle_pure_python        | 175 us                                                          | 172 us: 1.02x faster                                                        |
| sqlite_synth              | 1.60 us                                                         | 1.57 us: 1.02x faster                                                       |
| pickle_dict               | 18.1 us                                                         | 17.9 us: 1.01x faster                                                       |
| xml_etree_parse           | 90.9 ms                                                         | 90.2 ms: 1.01x faster                                                       |
| json_loads                | 14.2 us                                                         | 14.1 us: 1.01x faster                                                       |
| xml_etree_process         | 36.4 ms                                                         | 36.3 ms: 1.00x faster                                                       |
| logging_simple            | 5.78 us                                                         | 5.82 us: 1.01x slower                                                       |
| logging_format            | 6.22 us                                                         | 6.29 us: 1.01x slower                                                       |
| unpickle                  | 8.40 us                                                         | 8.54 us: 1.02x slower                                                       |
| chaos                     | 38.4 ms                                                         | 39.1 ms: 1.02x slower                                                       |
| regex_effbot              | 1.58 ms                                                         | 1.62 ms: 1.02x slower                                                       |
| json_dumps                | 5.61 ms                                                         | 5.74 ms: 1.02x slower                                                       |
| chameleon                 | 4.80 ms                                                         | 4.94 ms: 1.03x slower                                                       |
| coroutines                | 12.8 ms                                                         | 13.2 ms: 1.03x slower                                                       |
| meteor_contest            | 69.9 ms                                                         | 72.1 ms: 1.03x slower                                                       |
| async_tree_cpu_io_mixed   | 389 ms                                                          | 402 ms: 1.03x slower                                                        |
| async_tree_io_tg          | 605 ms                                                          | 625 ms: 1.03x slower                                                        |
| unpickle_pure_python      | 122 us                                                          | 126 us: 1.04x slower                                                        |
| create_gc_cycles          | 888 us                                                          | 923 us: 1.04x slower                                                        |
| pickle                    | 7.11 us                                                         | 7.42 us: 1.04x slower                                                       |
| regex_dna                 | 119 ms                                                          | 124 ms: 1.04x slower                                                        |
| logging_silent            | 52.9 ns                                                         | 55.3 ns: 1.04x slower                                                       |
| aiohttp                   | 889 us                                                          | 930 us: 1.05x slower                                                        |
| tornado_http              | 81.8 ms                                                         | 86.1 ms: 1.05x slower                                                       |
| async_tree_none           | 218 ms                                                          | 230 ms: 1.05x slower                                                        |
| async_tree_memoization    | 264 ms                                                          | 278 ms: 1.05x slower                                                        |
| async_tree_memoization_tg | 258 ms                                                          | 273 ms: 1.06x slower                                                        |
| dulwich_log               | 38.0 ms                                                         | 40.5 ms: 1.07x slower                                                       |
| bench_thread_pool         | 768 us                                                          | 820 us: 1.07x slower                                                        |
| scimark_sor               | 75.3 ms                                                         | 80.7 ms: 1.07x slower                                                       |
| html5lib                  | 35.0 ms                                                         | 37.5 ms: 1.07x slower                                                       |
| nqueens                   | 56.7 ms                                                         | 60.7 ms: 1.07x slower                                                       |
| async_tree_none_tg        | 202 ms                                                          | 216 ms: 1.07x slower                                                        |
| deepcopy_reduce           | 1.99 us                                                         | 2.14 us: 1.07x slower                                                       |
| bench_mp_pool             | 64.8 ms                                                         | 69.6 ms: 1.08x slower                                                       |
| sqlglot_parse             | 748 us                                                          | 807 us: 1.08x slower                                                        |
| python_startup            | 20.3 ms                                                         | 21.9 ms: 1.08x slower                                                       |
| coverage                  | 42.1 ms                                                         | 45.7 ms: 1.08x slower                                                       |
| sqlglot_transpile         | 955 us                                                          | 1.04 ms: 1.09x slower                                                       |
| unpickle_list             | 2.62 us                                                         | 2.85 us: 1.09x slower                                                       |
| docutils                  | 1.63 sec                                                        | 1.78 sec: 1.09x slower                                                      |
| deepcopy                  | 220 us                                                          | 241 us: 1.10x slower                                                        |
| richards_super            | 30.2 ms                                                         | 33.1 ms: 1.10x slower                                                       |
| generators                | 19.6 ms                                                         | 21.5 ms: 1.10x slower                                                       |
| richards                  | 26.7 ms                                                         | 29.4 ms: 1.10x slower                                                       |
| python_startup_no_site    | 16.2 ms                                                         | 17.9 ms: 1.11x slower                                                       |
| 2to3                      | 207 ms                                                          | 229 ms: 1.11x slower                                                        |
| sympy_sum                 | 84.4 ms                                                         | 94.0 ms: 1.11x slower                                                       |
| raytrace                  | 162 ms                                                          | 181 ms: 1.12x slower                                                        |
| typing_runtime_protocols  | 101 us                                                          | 113 us: 1.12x slower                                                        |
| regex_compile             | 78.0 ms                                                         | 87.7 ms: 1.13x slower                                                       |
| mdp                       | 1.31 sec                                                        | 1.48 sec: 1.13x slower                                                      |
| async_generators          | 223 ms                                                          | 252 ms: 1.13x slower                                                        |
| sqlglot_optimize          | 32.7 ms                                                         | 37.0 ms: 1.13x slower                                                       |
| sympy_str                 | 159 ms                                                          | 180 ms: 1.13x slower                                                        |
| go                        | 82.1 ms                                                         | 93.2 ms: 1.14x slower                                                       |
| thrift                    | 8.11 ms                                                         | 9.25 ms: 1.14x slower                                                       |
| pylint                    | 205 ms                                                          | 235 ms: 1.15x slower                                                        |
| sympy_integrate           | 12.2 ms                                                         | 14.1 ms: 1.15x slower                                                       |
| mypy2                     | 418 ms                                                          | 485 ms: 1.16x slower                                                        |
| sympy_expand              | 271 ms                                                          | 319 ms: 1.18x slower                                                        |
| django_template           | 21.7 ms                                                         | 25.8 ms: 1.19x slower                                                       |
| scimark_lu                | 56.6 ms                                                         | 70.2 ms: 1.24x slower                                                       |
| genshi_text               | 14.4 ms                                                         | 17.8 ms: 1.24x slower                                                       |
| deltablue                 | 1.88 ms                                                         | 2.35 ms: 1.25x slower                                                       |
| hexiom                    | 3.72 ms                                                         | 4.68 ms: 1.26x slower                                                       |
| genshi_xml                | 31.6 ms                                                         | 44.6 ms: 1.41x slower                                                       |
| Geometric mean            | (ref)                                                           | 1.03x slower                                                                |

Benchmark hidden because not significant (10): pycparser, regex_v8, pathlib, pidigits, flaskblogging, async_tree_io, asyncio_tcp_ssl, gc_traversal, async_tree_cpu_io_mixed_tg, asyncio_tcp
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: sqlglot_normalize

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: unknown