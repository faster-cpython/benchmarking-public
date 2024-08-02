# Results vs. 3.13.0b2

- fork: python
- ref: 6725c78d376eadb01a9d
- machine: windows-amd64
- commit hash: 6725c78
- commit date: 2024-06-04
- overall geometric mean: 1.13x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 236 ms: 1.14x slower                                                        |
| chameleon      | 4.80 ms                                                         | 5.40 ms: 1.12x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.86 sec: 1.15x slower                                                      |
| html5lib       | 35.0 ms                                                         | 41.7 ms: 1.19x slower                                                       |
| tornado_http   | 81.8 ms                                                         | 87.8 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                           | 1.13x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|---------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed   | 389 ms                                                          | 402 ms: 1.03x slower                                                        |
| async_tree_io_tg          | 605 ms                                                          | 632 ms: 1.04x slower                                                        |
| async_tree_none           | 218 ms                                                          | 234 ms: 1.07x slower                                                        |
| async_tree_memoization_tg | 258 ms                                                          | 277 ms: 1.07x slower                                                        |
| async_tree_none_tg        | 202 ms                                                          | 218 ms: 1.08x slower                                                        |
| async_tree_memoization    | 264 ms                                                          | 293 ms: 1.11x slower                                                        |
| Geometric mean            | (ref)                                                           | 1.05x slower                                                                |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 151 ms: 1.00x slower                                                        |
| float          | 49.7 ms                                                         | 56.5 ms: 1.14x slower                                                       |
| nbody          | 67.6 ms                                                         | 80.1 ms: 1.19x slower                                                       |
| Geometric mean | (ref)                                                           | 1.11x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.58 ms                                                         | 1.60 ms: 1.01x slower                                                       |
| regex_dna      | 119 ms                                                          | 121 ms: 1.02x slower                                                        |
| regex_compile  | 78.0 ms                                                         | 110 ms: 1.41x slower                                                        |
| Geometric mean | (ref)                                                           | 1.09x slower                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 90.9 ms                                                         | 89.8 ms: 1.01x faster                                                       |
| pickle_dict          | 18.1 us                                                         | 18.3 us: 1.01x slower                                                       |
| pickle               | 7.11 us                                                         | 7.19 us: 1.01x slower                                                       |
| json_dumps           | 5.61 ms                                                         | 5.90 ms: 1.05x slower                                                       |
| unpickle_list        | 2.62 us                                                         | 2.84 us: 1.08x slower                                                       |
| xml_etree_iterparse  | 62.3 ms                                                         | 67.6 ms: 1.08x slower                                                       |
| xml_etree_generate   | 53.2 ms                                                         | 58.0 ms: 1.09x slower                                                       |
| xml_etree_process    | 36.4 ms                                                         | 40.2 ms: 1.10x slower                                                       |
| tomli_loads          | 1.35 sec                                                        | 1.54 sec: 1.14x slower                                                      |
| pickle_pure_python   | 175 us                                                          | 228 us: 1.30x slower                                                        |
| unpickle_pure_python | 122 us                                                          | 169 us: 1.39x slower                                                        |
| Geometric mean       | (ref)                                                           | 1.08x slower                                                                |

Benchmark hidden because not significant (3): pickle_list, json_loads, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 20.5 ms: 1.01x slower                                                       |
| python_startup_no_site | 16.2 ms                                                         | 16.4 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                           | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 21.7 ms                                                         | 25.6 ms: 1.18x slower                                                       |
| genshi_xml      | 31.6 ms                                                         | 38.5 ms: 1.22x slower                                                       |
| mako            | 6.36 ms                                                         | 7.78 ms: 1.22x slower                                                       |
| genshi_text     | 14.4 ms                                                         | 18.2 ms: 1.27x slower                                                       |
| Geometric mean  | (ref)                                                           | 1.22x slower                                                                |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|---------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json                      | 3.19 ms                                                         | 2.95 ms: 1.08x faster                                                       |
| xml_etree_parse           | 90.9 ms                                                         | 89.8 ms: 1.01x faster                                                       |
| pidigits                  | 150 ms                                                          | 151 ms: 1.00x slower                                                        |
| pickle_dict               | 18.1 us                                                         | 18.3 us: 1.01x slower                                                       |
| generators                | 19.6 ms                                                         | 19.7 ms: 1.01x slower                                                       |
| python_startup            | 20.3 ms                                                         | 20.5 ms: 1.01x slower                                                       |
| pickle                    | 7.11 us                                                         | 7.19 us: 1.01x slower                                                       |
| regex_effbot              | 1.58 ms                                                         | 1.60 ms: 1.01x slower                                                       |
| python_startup_no_site    | 16.2 ms                                                         | 16.4 ms: 1.01x slower                                                       |
| gc_traversal              | 1.55 ms                                                         | 1.58 ms: 1.01x slower                                                       |
| regex_dna                 | 119 ms                                                          | 121 ms: 1.02x slower                                                        |
| sqlite_synth              | 1.60 us                                                         | 1.63 us: 1.02x slower                                                       |
| create_gc_cycles          | 888 us                                                          | 915 us: 1.03x slower                                                        |
| async_tree_cpu_io_mixed   | 389 ms                                                          | 402 ms: 1.03x slower                                                        |
| bench_mp_pool             | 64.8 ms                                                         | 67.0 ms: 1.03x slower                                                       |
| async_tree_io_tg          | 605 ms                                                          | 632 ms: 1.04x slower                                                        |
| json_dumps                | 5.61 ms                                                         | 5.90 ms: 1.05x slower                                                       |
| aiohttp                   | 889 us                                                          | 937 us: 1.05x slower                                                        |
| coverage                  | 42.1 ms                                                         | 44.4 ms: 1.06x slower                                                       |
| logging_format            | 6.22 us                                                         | 6.60 us: 1.06x slower                                                       |
| telco                     | 4.67 ms                                                         | 4.98 ms: 1.07x slower                                                       |
| async_tree_none           | 218 ms                                                          | 234 ms: 1.07x slower                                                        |
| async_tree_memoization_tg | 258 ms                                                          | 277 ms: 1.07x slower                                                        |
| tornado_http              | 81.8 ms                                                         | 87.8 ms: 1.07x slower                                                       |
| logging_simple            | 5.78 us                                                         | 6.24 us: 1.08x slower                                                       |
| async_generators          | 223 ms                                                          | 241 ms: 1.08x slower                                                        |
| async_tree_none_tg        | 202 ms                                                          | 218 ms: 1.08x slower                                                        |
| unpickle_list             | 2.62 us                                                         | 2.84 us: 1.08x slower                                                       |
| xml_etree_iterparse       | 62.3 ms                                                         | 67.6 ms: 1.08x slower                                                       |
| xml_etree_generate        | 53.2 ms                                                         | 58.0 ms: 1.09x slower                                                       |
| bench_thread_pool         | 768 us                                                          | 841 us: 1.10x slower                                                        |
| xml_etree_process         | 36.4 ms                                                         | 40.2 ms: 1.10x slower                                                       |
| async_tree_memoization    | 264 ms                                                          | 293 ms: 1.11x slower                                                        |
| meteor_contest            | 69.9 ms                                                         | 78.4 ms: 1.12x slower                                                       |
| pylint                    | 205 ms                                                          | 230 ms: 1.12x slower                                                        |
| chameleon                 | 4.80 ms                                                         | 5.40 ms: 1.12x slower                                                       |
| mdp                       | 1.31 sec                                                        | 1.48 sec: 1.13x slower                                                      |
| richards_super            | 30.2 ms                                                         | 34.1 ms: 1.13x slower                                                       |
| deepcopy_reduce           | 1.99 us                                                         | 2.26 us: 1.14x slower                                                       |
| float                     | 49.7 ms                                                         | 56.5 ms: 1.14x slower                                                       |
| richards                  | 26.7 ms                                                         | 30.4 ms: 1.14x slower                                                       |
| 2to3                      | 207 ms                                                          | 236 ms: 1.14x slower                                                        |
| tomli_loads               | 1.35 sec                                                        | 1.54 sec: 1.14x slower                                                      |
| docutils                  | 1.63 sec                                                        | 1.86 sec: 1.15x slower                                                      |
| raytrace                  | 162 ms                                                          | 186 ms: 1.15x slower                                                        |
| mypy2                     | 418 ms                                                          | 481 ms: 1.15x slower                                                        |
| typing_runtime_protocols  | 101 us                                                          | 116 us: 1.15x slower                                                        |
| pycparser                 | 754 ms                                                          | 876 ms: 1.16x slower                                                        |
| crypto_pyaes              | 45.5 ms                                                         | 53.0 ms: 1.17x slower                                                       |
| fannkuch                  | 243 ms                                                          | 285 ms: 1.17x slower                                                        |
| dulwich_log               | 38.0 ms                                                         | 44.7 ms: 1.17x slower                                                       |
| django_template           | 21.7 ms                                                         | 25.6 ms: 1.18x slower                                                       |
| sympy_sum                 | 84.4 ms                                                         | 99.8 ms: 1.18x slower                                                       |
| nbody                     | 67.6 ms                                                         | 80.1 ms: 1.19x slower                                                       |
| chaos                     | 38.4 ms                                                         | 45.5 ms: 1.19x slower                                                       |
| sqlglot_optimize          | 32.7 ms                                                         | 38.9 ms: 1.19x slower                                                       |
| html5lib                  | 35.0 ms                                                         | 41.7 ms: 1.19x slower                                                       |
| pprint_safe_repr          | 474 ms                                                          | 567 ms: 1.20x slower                                                        |
| deepcopy                  | 220 us                                                          | 263 us: 1.20x slower                                                        |
| pprint_pformat            | 966 ms                                                          | 1.16 sec: 1.20x slower                                                      |
| scimark_sor               | 75.3 ms                                                         | 90.8 ms: 1.21x slower                                                       |
| sympy_integrate           | 12.2 ms                                                         | 14.8 ms: 1.21x slower                                                       |
| thrift                    | 8.11 ms                                                         | 9.82 ms: 1.21x slower                                                       |
| sqlglot_transpile         | 955 us                                                          | 1.16 ms: 1.22x slower                                                       |
| genshi_xml                | 31.6 ms                                                         | 38.5 ms: 1.22x slower                                                       |
| spectral_norm             | 63.7 ms                                                         | 77.8 ms: 1.22x slower                                                       |
| mako                      | 6.36 ms                                                         | 7.78 ms: 1.22x slower                                                       |
| nqueens                   | 56.7 ms                                                         | 69.7 ms: 1.23x slower                                                       |
| sqlglot_parse             | 748 us                                                          | 926 us: 1.24x slower                                                        |
| pyflate                   | 279 ms                                                          | 345 ms: 1.24x slower                                                        |
| sympy_str                 | 159 ms                                                          | 197 ms: 1.24x slower                                                        |
| scimark_fft               | 171 ms                                                          | 212 ms: 1.24x slower                                                        |
| sympy_expand              | 271 ms                                                          | 336 ms: 1.24x slower                                                        |
| go                        | 82.1 ms                                                         | 104 ms: 1.26x slower                                                        |
| genshi_text               | 14.4 ms                                                         | 18.2 ms: 1.27x slower                                                       |
| scimark_sparse_mat_mult   | 2.50 ms                                                         | 3.20 ms: 1.28x slower                                                       |
| pickle_pure_python        | 175 us                                                          | 228 us: 1.30x slower                                                        |
| scimark_monte_carlo       | 39.1 ms                                                         | 53.5 ms: 1.37x slower                                                       |
| unpickle_pure_python      | 122 us                                                          | 169 us: 1.39x slower                                                        |
| comprehensions            | 10.4 us                                                         | 14.4 us: 1.39x slower                                                       |
| regex_compile             | 78.0 ms                                                         | 110 ms: 1.41x slower                                                        |
| deltablue                 | 1.88 ms                                                         | 2.71 ms: 1.44x slower                                                       |
| logging_silent            | 52.9 ns                                                         | 76.2 ns: 1.44x slower                                                       |
| deepcopy_memo             | 22.1 us                                                         | 31.9 us: 1.44x slower                                                       |
| scimark_lu                | 56.6 ms                                                         | 81.9 ms: 1.45x slower                                                       |
| hexiom                    | 3.72 ms                                                         | 5.66 ms: 1.52x slower                                                       |
| Geometric mean            | (ref)                                                           | 1.13x slower                                                                |

Benchmark hidden because not significant (11): regex_v8, pickle_list, pathlib, json_loads, coroutines, flaskblogging, unpickle, async_tree_cpu_io_mixed_tg, asyncio_tcp_ssl, asyncio_tcp, async_tree_io
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: sqlglot_normalize

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.11x
- 95% likely to have a slowdown of 1.11x
- 99% likely to have a slowdown of 1.09x

# Memory
- memory change: unknown