# Results vs. 3.13.0b2

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: windows-amd64
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.11x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 239 ms: 1.15x slower                                                       |
| chameleon      | 4.80 ms                                                         | 5.39 ms: 1.12x slower                                                      |
| docutils       | 1.63 sec                                                        | 1.85 sec: 1.14x slower                                                     |
| html5lib       | 35.0 ms                                                         | 41.9 ms: 1.20x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 87.2 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                           | 1.13x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg          | 605 ms                                                          | 635 ms: 1.05x slower                                                       |
| async_tree_cpu_io_mixed   | 389 ms                                                          | 410 ms: 1.05x slower                                                       |
| async_tree_io             | 588 ms                                                          | 627 ms: 1.07x slower                                                       |
| async_tree_memoization_tg | 258 ms                                                          | 279 ms: 1.08x slower                                                       |
| async_tree_none_tg        | 202 ms                                                          | 221 ms: 1.09x slower                                                       |
| async_tree_memoization    | 264 ms                                                          | 290 ms: 1.10x slower                                                       |
| async_tree_none           | 218 ms                                                          | 242 ms: 1.11x slower                                                       |
| Geometric mean            | (ref)                                                           | 1.07x slower                                                               |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 151 ms: 1.01x slower                                                       |
| float          | 49.7 ms                                                         | 55.9 ms: 1.12x slower                                                      |
| nbody          | 67.6 ms                                                         | 81.2 ms: 1.20x slower                                                      |
| Geometric mean | (ref)                                                           | 1.11x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                          | 119 ms: 1.00x slower                                                       |
| regex_effbot   | 1.58 ms                                                         | 1.62 ms: 1.03x slower                                                      |
| regex_compile  | 78.0 ms                                                         | 111 ms: 1.42x slower                                                       |
| Geometric mean | (ref)                                                           | 1.12x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 14.2 us                                                         | 14.1 us: 1.01x faster                                                      |
| pickle_dict          | 18.1 us                                                         | 18.4 us: 1.02x slower                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 92.5 ms: 1.02x slower                                                      |
| pickle               | 7.11 us                                                         | 7.26 us: 1.02x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 5.82 ms: 1.04x slower                                                      |
| unpickle             | 8.40 us                                                         | 8.72 us: 1.04x slower                                                      |
| pickle_list          | 2.90 us                                                         | 3.02 us: 1.04x slower                                                      |
| unpickle_list        | 2.62 us                                                         | 2.77 us: 1.06x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 67.4 ms: 1.08x slower                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 57.9 ms: 1.09x slower                                                      |
| xml_etree_process    | 36.4 ms                                                         | 40.4 ms: 1.11x slower                                                      |
| tomli_loads          | 1.35 sec                                                        | 1.53 sec: 1.13x slower                                                     |
| pickle_pure_python   | 175 us                                                          | 227 us: 1.29x slower                                                       |
| unpickle_pure_python | 122 us                                                          | 167 us: 1.37x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.09x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 20.5 ms: 1.01x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 16.7 ms: 1.03x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.02x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 21.7 ms                                                         | 25.3 ms: 1.17x slower                                                      |
| mako            | 6.36 ms                                                         | 7.54 ms: 1.19x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 38.9 ms: 1.23x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 18.2 ms: 1.26x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.21x slower                                                               |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                    | 8.11 ms                                                         | 517 us: 15.68x faster                                                      |
| asyncio_tcp_ssl           | 1.48 sec                                                        | 1.37 sec: 1.08x faster                                                     |
| json                      | 3.19 ms                                                         | 2.95 ms: 1.08x faster                                                      |
| json_loads                | 14.2 us                                                         | 14.1 us: 1.01x faster                                                      |
| regex_dna                 | 119 ms                                                          | 119 ms: 1.00x slower                                                       |
| generators                | 19.6 ms                                                         | 19.7 ms: 1.01x slower                                                      |
| pidigits                  | 150 ms                                                          | 151 ms: 1.01x slower                                                       |
| python_startup            | 20.3 ms                                                         | 20.5 ms: 1.01x slower                                                      |
| sqlite_synth              | 1.60 us                                                         | 1.62 us: 1.01x slower                                                      |
| pickle_dict               | 18.1 us                                                         | 18.4 us: 1.02x slower                                                      |
| xml_etree_parse           | 90.9 ms                                                         | 92.5 ms: 1.02x slower                                                      |
| pickle                    | 7.11 us                                                         | 7.26 us: 1.02x slower                                                      |
| regex_effbot              | 1.58 ms                                                         | 1.62 ms: 1.03x slower                                                      |
| python_startup_no_site    | 16.2 ms                                                         | 16.7 ms: 1.03x slower                                                      |
| asyncio_tcp               | 471 ms                                                          | 488 ms: 1.03x slower                                                       |
| json_dumps                | 5.61 ms                                                         | 5.82 ms: 1.04x slower                                                      |
| unpickle                  | 8.40 us                                                         | 8.72 us: 1.04x slower                                                      |
| pickle_list               | 2.90 us                                                         | 3.02 us: 1.04x slower                                                      |
| pathlib                   | 75.9 ms                                                         | 79.1 ms: 1.04x slower                                                      |
| create_gc_cycles          | 888 us                                                          | 926 us: 1.04x slower                                                       |
| async_tree_io_tg          | 605 ms                                                          | 635 ms: 1.05x slower                                                       |
| bench_mp_pool             | 64.8 ms                                                         | 68.1 ms: 1.05x slower                                                      |
| async_tree_cpu_io_mixed   | 389 ms                                                          | 410 ms: 1.05x slower                                                       |
| unpickle_list             | 2.62 us                                                         | 2.77 us: 1.06x slower                                                      |
| coverage                  | 42.1 ms                                                         | 44.8 ms: 1.06x slower                                                      |
| tornado_http              | 81.8 ms                                                         | 87.2 ms: 1.07x slower                                                      |
| logging_format            | 6.22 us                                                         | 6.64 us: 1.07x slower                                                      |
| async_tree_io             | 588 ms                                                          | 627 ms: 1.07x slower                                                       |
| logging_simple            | 5.78 us                                                         | 6.25 us: 1.08x slower                                                      |
| telco                     | 4.67 ms                                                         | 5.04 ms: 1.08x slower                                                      |
| async_tree_memoization_tg | 258 ms                                                          | 279 ms: 1.08x slower                                                       |
| xml_etree_iterparse       | 62.3 ms                                                         | 67.4 ms: 1.08x slower                                                      |
| xml_etree_generate        | 53.2 ms                                                         | 57.9 ms: 1.09x slower                                                      |
| async_tree_none_tg        | 202 ms                                                          | 221 ms: 1.09x slower                                                       |
| async_tree_memoization    | 264 ms                                                          | 290 ms: 1.10x slower                                                       |
| pycparser                 | 754 ms                                                          | 831 ms: 1.10x slower                                                       |
| bench_thread_pool         | 768 us                                                          | 848 us: 1.10x slower                                                       |
| async_tree_none           | 218 ms                                                          | 242 ms: 1.11x slower                                                       |
| xml_etree_process         | 36.4 ms                                                         | 40.4 ms: 1.11x slower                                                      |
| richards_super            | 30.2 ms                                                         | 33.5 ms: 1.11x slower                                                      |
| chameleon                 | 4.80 ms                                                         | 5.39 ms: 1.12x slower                                                      |
| float                     | 49.7 ms                                                         | 55.9 ms: 1.12x slower                                                      |
| richards                  | 26.7 ms                                                         | 30.0 ms: 1.12x slower                                                      |
| tomli_loads               | 1.35 sec                                                        | 1.53 sec: 1.13x slower                                                     |
| meteor_contest            | 69.9 ms                                                         | 79.0 ms: 1.13x slower                                                      |
| deepcopy_reduce           | 1.99 us                                                         | 2.26 us: 1.13x slower                                                      |
| async_generators          | 223 ms                                                          | 254 ms: 1.14x slower                                                       |
| docutils                  | 1.63 sec                                                        | 1.85 sec: 1.14x slower                                                     |
| crypto_pyaes              | 45.5 ms                                                         | 52.3 ms: 1.15x slower                                                      |
| fannkuch                  | 243 ms                                                          | 280 ms: 1.15x slower                                                       |
| pylint                    | 205 ms                                                          | 236 ms: 1.15x slower                                                       |
| 2to3                      | 207 ms                                                          | 239 ms: 1.15x slower                                                       |
| raytrace                  | 162 ms                                                          | 188 ms: 1.16x slower                                                       |
| django_template           | 21.7 ms                                                         | 25.3 ms: 1.17x slower                                                      |
| typing_runtime_protocols  | 101 us                                                          | 119 us: 1.18x slower                                                       |
| mako                      | 6.36 ms                                                         | 7.54 ms: 1.19x slower                                                      |
| sqlglot_optimize          | 32.7 ms                                                         | 38.9 ms: 1.19x slower                                                      |
| chaos                     | 38.4 ms                                                         | 45.7 ms: 1.19x slower                                                      |
| scimark_fft               | 171 ms                                                          | 204 ms: 1.19x slower                                                       |
| mdp                       | 1.31 sec                                                        | 1.57 sec: 1.19x slower                                                     |
| html5lib                  | 35.0 ms                                                         | 41.9 ms: 1.20x slower                                                      |
| nbody                     | 67.6 ms                                                         | 81.2 ms: 1.20x slower                                                      |
| deepcopy                  | 220 us                                                          | 266 us: 1.21x slower                                                       |
| sympy_sum                 | 84.4 ms                                                         | 102 ms: 1.21x slower                                                       |
| pprint_pformat            | 966 ms                                                          | 1.17 sec: 1.21x slower                                                     |
| pyflate                   | 279 ms                                                          | 339 ms: 1.22x slower                                                       |
| pprint_safe_repr          | 474 ms                                                          | 577 ms: 1.22x slower                                                       |
| sympy_integrate           | 12.2 ms                                                         | 14.9 ms: 1.22x slower                                                      |
| sqlglot_transpile         | 955 us                                                          | 1.17 ms: 1.22x slower                                                      |
| genshi_xml                | 31.6 ms                                                         | 38.9 ms: 1.23x slower                                                      |
| scimark_sor               | 75.3 ms                                                         | 93.2 ms: 1.24x slower                                                      |
| sqlglot_parse             | 748 us                                                          | 927 us: 1.24x slower                                                       |
| sympy_str                 | 159 ms                                                          | 197 ms: 1.24x slower                                                       |
| sympy_expand              | 271 ms                                                          | 337 ms: 1.25x slower                                                       |
| genshi_text               | 14.4 ms                                                         | 18.2 ms: 1.26x slower                                                      |
| nqueens                   | 56.7 ms                                                         | 71.7 ms: 1.27x slower                                                      |
| spectral_norm             | 63.7 ms                                                         | 80.8 ms: 1.27x slower                                                      |
| go                        | 82.1 ms                                                         | 104 ms: 1.27x slower                                                       |
| pickle_pure_python        | 175 us                                                          | 227 us: 1.29x slower                                                       |
| scimark_sparse_mat_mult   | 2.50 ms                                                         | 3.29 ms: 1.32x slower                                                      |
| scimark_monte_carlo       | 39.1 ms                                                         | 51.9 ms: 1.33x slower                                                      |
| unpickle_pure_python      | 122 us                                                          | 167 us: 1.37x slower                                                       |
| comprehensions            | 10.4 us                                                         | 14.5 us: 1.40x slower                                                      |
| deepcopy_memo             | 22.1 us                                                         | 31.2 us: 1.41x slower                                                      |
| regex_compile             | 78.0 ms                                                         | 111 ms: 1.42x slower                                                       |
| deltablue                 | 1.88 ms                                                         | 2.70 ms: 1.43x slower                                                      |
| logging_silent            | 52.9 ns                                                         | 77.4 ns: 1.46x slower                                                      |
| scimark_lu                | 56.6 ms                                                         | 83.1 ms: 1.47x slower                                                      |
| hexiom                    | 3.72 ms                                                         | 5.76 ms: 1.55x slower                                                      |
| Geometric mean            | (ref)                                                           | 1.11x slower                                                               |

Benchmark hidden because not significant (5): coroutines, flaskblogging, gc_traversal, async_tree_cpu_io_mixed_tg, regex_v8
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, dulwich_log, mypy2, sqlglot_normalize

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.11x
- 95% likely to have a slowdown of 1.10x
- 99% likely to have a slowdown of 1.09x

# Memory
- memory change: unknown