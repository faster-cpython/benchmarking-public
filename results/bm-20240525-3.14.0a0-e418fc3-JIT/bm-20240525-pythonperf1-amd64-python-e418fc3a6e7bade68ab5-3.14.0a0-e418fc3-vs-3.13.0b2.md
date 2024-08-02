# Results vs. 3.13.0b2

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: windows-amd64
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.00x slower
- HPT reliability: 99.86%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 244 ms: 1.18x slower                                                       |
| chameleon      | 4.80 ms                                                         | 5.14 ms: 1.07x slower                                                      |
| docutils       | 1.63 sec                                                        | 1.77 sec: 1.09x slower                                                     |
| html5lib       | 35.0 ms                                                         | 37.5 ms: 1.07x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 85.3 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                           | 1.09x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg          | 605 ms                                                          | 622 ms: 1.03x slower                                                       |
| async_tree_cpu_io_mixed   | 389 ms                                                          | 401 ms: 1.03x slower                                                       |
| async_tree_none           | 218 ms                                                          | 228 ms: 1.04x slower                                                       |
| async_tree_memoization_tg | 258 ms                                                          | 270 ms: 1.05x slower                                                       |
| async_tree_none_tg        | 202 ms                                                          | 211 ms: 1.05x slower                                                       |
| async_tree_memoization    | 264 ms                                                          | 281 ms: 1.06x slower                                                       |
| Geometric mean            | (ref)                                                           | 1.04x slower                                                               |

Benchmark hidden because not significant (2): async_tree_io, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 51.2 ms: 1.32x faster                                                      |
| float          | 49.7 ms                                                         | 43.4 ms: 1.14x faster                                                      |
| Geometric mean | (ref)                                                           | 1.15x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                          | 117 ms: 1.02x faster                                                       |
| regex_effbot   | 1.58 ms                                                         | 1.57 ms: 1.01x faster                                                      |
| regex_compile  | 78.0 ms                                                         | 87.5 ms: 1.12x slower                                                      |
| Geometric mean | (ref)                                                           | 1.01x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.35 sec                                                        | 1.23 sec: 1.10x faster                                                     |
| xml_etree_generate   | 53.2 ms                                                         | 50.9 ms: 1.04x faster                                                      |
| pickle_dict          | 18.1 us                                                         | 17.5 us: 1.04x faster                                                      |
| pickle_pure_python   | 175 us                                                          | 170 us: 1.03x faster                                                       |
| xml_etree_iterparse  | 62.3 ms                                                         | 61.1 ms: 1.02x faster                                                      |
| xml_etree_process    | 36.4 ms                                                         | 36.0 ms: 1.01x faster                                                      |
| pickle               | 7.11 us                                                         | 7.08 us: 1.01x faster                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 92.3 ms: 1.01x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 5.75 ms: 1.02x slower                                                      |
| unpickle_pure_python | 122 us                                                          | 125 us: 1.03x slower                                                       |
| unpickle             | 8.40 us                                                         | 8.96 us: 1.07x slower                                                      |
| unpickle_list        | 2.62 us                                                         | 2.92 us: 1.11x slower                                                      |
| Geometric mean       | (ref)                                                           | 1.00x faster                                                               |

Benchmark hidden because not significant (2): pickle_list, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 22.8 ms: 1.12x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 18.8 ms: 1.16x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.14x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 4.90 ms: 1.30x faster                                                      |
| django_template | 21.7 ms                                                         | 25.6 ms: 1.18x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 18.2 ms: 1.26x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 44.8 ms: 1.42x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.13x slower                                                               |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                    | 8.11 ms                                                         | 513 us: 15.81x faster                                                      |
| spectral_norm             | 63.7 ms                                                         | 46.1 ms: 1.38x faster                                                      |
| nbody                     | 67.6 ms                                                         | 51.2 ms: 1.32x faster                                                      |
| mako                      | 6.36 ms                                                         | 4.90 ms: 1.30x faster                                                      |
| scimark_sparse_mat_mult   | 2.50 ms                                                         | 2.14 ms: 1.17x faster                                                      |
| float                     | 49.7 ms                                                         | 43.4 ms: 1.14x faster                                                      |
| scimark_fft               | 171 ms                                                          | 149 ms: 1.14x faster                                                       |
| tomli_loads               | 1.35 sec                                                        | 1.23 sec: 1.10x faster                                                     |
| fannkuch                  | 243 ms                                                          | 221 ms: 1.10x faster                                                       |
| crypto_pyaes              | 45.5 ms                                                         | 41.4 ms: 1.10x faster                                                      |
| pyflate                   | 279 ms                                                          | 256 ms: 1.09x faster                                                       |
| asyncio_tcp_ssl           | 1.48 sec                                                        | 1.37 sec: 1.08x faster                                                     |
| json                      | 3.19 ms                                                         | 2.94 ms: 1.08x faster                                                      |
| deepcopy_memo             | 22.1 us                                                         | 20.7 us: 1.07x faster                                                      |
| xml_etree_generate        | 53.2 ms                                                         | 50.9 ms: 1.04x faster                                                      |
| pickle_dict               | 18.1 us                                                         | 17.5 us: 1.04x faster                                                      |
| pprint_pformat            | 966 ms                                                          | 935 ms: 1.03x faster                                                       |
| pickle_pure_python        | 175 us                                                          | 170 us: 1.03x faster                                                       |
| pprint_safe_repr          | 474 ms                                                          | 461 ms: 1.03x faster                                                       |
| scimark_monte_carlo       | 39.1 ms                                                         | 38.3 ms: 1.02x faster                                                      |
| xml_etree_iterparse       | 62.3 ms                                                         | 61.1 ms: 1.02x faster                                                      |
| sqlite_synth              | 1.60 us                                                         | 1.57 us: 1.02x faster                                                      |
| regex_dna                 | 119 ms                                                          | 117 ms: 1.02x faster                                                       |
| xml_etree_process         | 36.4 ms                                                         | 36.0 ms: 1.01x faster                                                      |
| logging_format            | 6.22 us                                                         | 6.15 us: 1.01x faster                                                      |
| comprehensions            | 10.4 us                                                         | 10.3 us: 1.01x faster                                                      |
| telco                     | 4.67 ms                                                         | 4.62 ms: 1.01x faster                                                      |
| regex_effbot              | 1.58 ms                                                         | 1.57 ms: 1.01x faster                                                      |
| pickle                    | 7.11 us                                                         | 7.08 us: 1.01x faster                                                      |
| flaskblogging             | 2.03 sec                                                        | 2.03 sec: 1.00x faster                                                     |
| xml_etree_parse           | 90.9 ms                                                         | 92.3 ms: 1.01x slower                                                      |
| json_dumps                | 5.61 ms                                                         | 5.75 ms: 1.02x slower                                                      |
| coroutines                | 12.8 ms                                                         | 13.1 ms: 1.03x slower                                                      |
| create_gc_cycles          | 888 us                                                          | 911 us: 1.03x slower                                                       |
| async_tree_io_tg          | 605 ms                                                          | 622 ms: 1.03x slower                                                       |
| logging_silent            | 52.9 ns                                                         | 54.5 ns: 1.03x slower                                                      |
| unpickle_pure_python      | 122 us                                                          | 125 us: 1.03x slower                                                       |
| async_tree_cpu_io_mixed   | 389 ms                                                          | 401 ms: 1.03x slower                                                       |
| asyncio_tcp               | 471 ms                                                          | 487 ms: 1.03x slower                                                       |
| pathlib                   | 75.9 ms                                                         | 78.8 ms: 1.04x slower                                                      |
| tornado_http              | 81.8 ms                                                         | 85.3 ms: 1.04x slower                                                      |
| async_tree_none           | 218 ms                                                          | 228 ms: 1.04x slower                                                       |
| async_tree_memoization_tg | 258 ms                                                          | 270 ms: 1.05x slower                                                       |
| async_tree_none_tg        | 202 ms                                                          | 211 ms: 1.05x slower                                                       |
| meteor_contest            | 69.9 ms                                                         | 73.2 ms: 1.05x slower                                                      |
| chaos                     | 38.4 ms                                                         | 40.3 ms: 1.05x slower                                                      |
| async_tree_memoization    | 264 ms                                                          | 281 ms: 1.06x slower                                                       |
| unpickle                  | 8.40 us                                                         | 8.96 us: 1.07x slower                                                      |
| html5lib                  | 35.0 ms                                                         | 37.5 ms: 1.07x slower                                                      |
| chameleon                 | 4.80 ms                                                         | 5.14 ms: 1.07x slower                                                      |
| richards_super            | 30.2 ms                                                         | 32.3 ms: 1.07x slower                                                      |
| richards                  | 26.7 ms                                                         | 28.7 ms: 1.07x slower                                                      |
| sqlglot_parse             | 748 us                                                          | 805 us: 1.08x slower                                                       |
| bench_thread_pool         | 768 us                                                          | 826 us: 1.08x slower                                                       |
| coverage                  | 42.1 ms                                                         | 45.3 ms: 1.08x slower                                                      |
| deepcopy_reduce           | 1.99 us                                                         | 2.15 us: 1.08x slower                                                      |
| raytrace                  | 162 ms                                                          | 175 ms: 1.08x slower                                                       |
| scimark_sor               | 75.3 ms                                                         | 81.5 ms: 1.08x slower                                                      |
| generators                | 19.6 ms                                                         | 21.2 ms: 1.09x slower                                                      |
| sqlglot_transpile         | 955 us                                                          | 1.04 ms: 1.09x slower                                                      |
| docutils                  | 1.63 sec                                                        | 1.77 sec: 1.09x slower                                                     |
| deepcopy                  | 220 us                                                          | 240 us: 1.09x slower                                                       |
| nqueens                   | 56.7 ms                                                         | 62.0 ms: 1.09x slower                                                      |
| sympy_sum                 | 84.4 ms                                                         | 92.4 ms: 1.09x slower                                                      |
| mdp                       | 1.31 sec                                                        | 1.45 sec: 1.10x slower                                                     |
| unpickle_list             | 2.62 us                                                         | 2.92 us: 1.11x slower                                                      |
| sympy_str                 | 159 ms                                                          | 177 ms: 1.12x slower                                                       |
| regex_compile             | 78.0 ms                                                         | 87.5 ms: 1.12x slower                                                      |
| python_startup            | 20.3 ms                                                         | 22.8 ms: 1.12x slower                                                      |
| sqlglot_optimize          | 32.7 ms                                                         | 36.8 ms: 1.13x slower                                                      |
| async_generators          | 223 ms                                                          | 253 ms: 1.13x slower                                                       |
| sympy_integrate           | 12.2 ms                                                         | 13.9 ms: 1.14x slower                                                      |
| bench_mp_pool             | 64.8 ms                                                         | 73.8 ms: 1.14x slower                                                      |
| sympy_expand              | 271 ms                                                          | 309 ms: 1.14x slower                                                       |
| go                        | 82.1 ms                                                         | 93.7 ms: 1.14x slower                                                      |
| typing_runtime_protocols  | 101 us                                                          | 115 us: 1.14x slower                                                       |
| pylint                    | 205 ms                                                          | 236 ms: 1.15x slower                                                       |
| python_startup_no_site    | 16.2 ms                                                         | 18.8 ms: 1.16x slower                                                      |
| 2to3                      | 207 ms                                                          | 244 ms: 1.18x slower                                                       |
| django_template           | 21.7 ms                                                         | 25.6 ms: 1.18x slower                                                      |
| scimark_lu                | 56.6 ms                                                         | 67.7 ms: 1.20x slower                                                      |
| deltablue                 | 1.88 ms                                                         | 2.35 ms: 1.25x slower                                                      |
| hexiom                    | 3.72 ms                                                         | 4.67 ms: 1.26x slower                                                      |
| genshi_text               | 14.4 ms                                                         | 18.2 ms: 1.26x slower                                                      |
| genshi_xml                | 31.6 ms                                                         | 44.8 ms: 1.42x slower                                                      |
| Geometric mean            | (ref)                                                           | 1.00x slower                                                               |

Benchmark hidden because not significant (9): regex_v8, pycparser, pickle_list, logging_simple, json_loads, pidigits, gc_traversal, async_tree_io, async_tree_cpu_io_mixed_tg
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, dulwich_log, mypy2, sqlglot_normalize

# HPT report

- Reliability score: 99.86% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown