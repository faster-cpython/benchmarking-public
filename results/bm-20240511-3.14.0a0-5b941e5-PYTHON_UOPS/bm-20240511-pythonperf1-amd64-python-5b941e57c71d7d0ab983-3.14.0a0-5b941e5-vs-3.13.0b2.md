# Results vs. 3.13.0b2

- fork: python
- ref: 5b941e57c71d7d0ab983
- machine: windows-amd64
- commit hash: 5b941e5
- commit date: 2024-05-11
- overall geometric mean: 1.10x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 237 ms: 1.15x slower                                                       |
| chameleon      | 4.80 ms                                                         | 5.39 ms: 1.12x slower                                                      |
| docutils       | 1.63 sec                                                        | 1.85 sec: 1.14x slower                                                     |
| html5lib       | 35.0 ms                                                         | 40.9 ms: 1.17x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 87.9 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                           | 1.13x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed   | 389 ms                                                          | 407 ms: 1.04x slower                                                       |
| async_tree_io_tg          | 605 ms                                                          | 639 ms: 1.05x slower                                                       |
| async_tree_memoization    | 264 ms                                                          | 285 ms: 1.08x slower                                                       |
| async_tree_memoization_tg | 258 ms                                                          | 279 ms: 1.08x slower                                                       |
| async_tree_none           | 218 ms                                                          | 238 ms: 1.09x slower                                                       |
| async_tree_none_tg        | 202 ms                                                          | 221 ms: 1.10x slower                                                       |
| Geometric mean            | (ref)                                                           | 1.06x slower                                                               |

Benchmark hidden because not significant (2): async_tree_io, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 151 ms: 1.01x slower                                                       |
| float          | 49.7 ms                                                         | 54.6 ms: 1.10x slower                                                      |
| nbody          | 67.6 ms                                                         | 75.7 ms: 1.12x slower                                                      |
| Geometric mean | (ref)                                                           | 1.08x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                          | 116 ms: 1.02x faster                                                       |
| regex_effbot   | 1.58 ms                                                         | 1.57 ms: 1.01x faster                                                      |
| regex_compile  | 78.0 ms                                                         | 112 ms: 1.43x slower                                                       |
| Geometric mean | (ref)                                                           | 1.07x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 14.2 us                                                         | 14.0 us: 1.01x faster                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 90.1 ms: 1.01x faster                                                      |
| pickle               | 7.11 us                                                         | 7.13 us: 1.00x slower                                                      |
| pickle_dict          | 18.1 us                                                         | 18.3 us: 1.01x slower                                                      |
| unpickle             | 8.40 us                                                         | 8.55 us: 1.02x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 5.76 ms: 1.03x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 66.4 ms: 1.07x slower                                                      |
| unpickle_list        | 2.62 us                                                         | 2.80 us: 1.07x slower                                                      |
| pickle_list          | 2.90 us                                                         | 3.11 us: 1.07x slower                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 57.4 ms: 1.08x slower                                                      |
| xml_etree_process    | 36.4 ms                                                         | 40.3 ms: 1.11x slower                                                      |
| tomli_loads          | 1.35 sec                                                        | 1.55 sec: 1.15x slower                                                     |
| pickle_pure_python   | 175 us                                                          | 228 us: 1.30x slower                                                       |
| unpickle_pure_python | 122 us                                                          | 167 us: 1.37x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.08x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                         | 16.5 ms: 1.02x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.01x slower                                                               |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 21.7 ms                                                         | 25.2 ms: 1.16x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 37.0 ms: 1.17x slower                                                      |
| mako            | 6.36 ms                                                         | 7.85 ms: 1.23x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 17.8 ms: 1.24x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.20x slower                                                               |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                    | 8.11 ms                                                         | 527 us: 15.40x faster                                                      |
| regex_dna                 | 119 ms                                                          | 116 ms: 1.02x faster                                                       |
| json_loads                | 14.2 us                                                         | 14.0 us: 1.01x faster                                                      |
| xml_etree_parse           | 90.9 ms                                                         | 90.1 ms: 1.01x faster                                                      |
| regex_effbot              | 1.58 ms                                                         | 1.57 ms: 1.01x faster                                                      |
| pickle                    | 7.11 us                                                         | 7.13 us: 1.00x slower                                                      |
| pickle_dict               | 18.1 us                                                         | 18.3 us: 1.01x slower                                                      |
| pidigits                  | 150 ms                                                          | 151 ms: 1.01x slower                                                       |
| gc_traversal              | 1.55 ms                                                         | 1.57 ms: 1.01x slower                                                      |
| coroutines                | 12.8 ms                                                         | 12.9 ms: 1.01x slower                                                      |
| unpickle                  | 8.40 us                                                         | 8.55 us: 1.02x slower                                                      |
| python_startup_no_site    | 16.2 ms                                                         | 16.5 ms: 1.02x slower                                                      |
| sqlite_synth              | 1.60 us                                                         | 1.63 us: 1.02x slower                                                      |
| json_dumps                | 5.61 ms                                                         | 5.76 ms: 1.03x slower                                                      |
| telco                     | 4.67 ms                                                         | 4.84 ms: 1.04x slower                                                      |
| async_tree_cpu_io_mixed   | 389 ms                                                          | 407 ms: 1.04x slower                                                       |
| pathlib                   | 75.9 ms                                                         | 80.0 ms: 1.05x slower                                                      |
| async_tree_io_tg          | 605 ms                                                          | 639 ms: 1.05x slower                                                       |
| generators                | 19.6 ms                                                         | 20.7 ms: 1.06x slower                                                      |
| bench_mp_pool             | 64.8 ms                                                         | 68.5 ms: 1.06x slower                                                      |
| xml_etree_iterparse       | 62.3 ms                                                         | 66.4 ms: 1.07x slower                                                      |
| logging_format            | 6.22 us                                                         | 6.65 us: 1.07x slower                                                      |
| unpickle_list             | 2.62 us                                                         | 2.80 us: 1.07x slower                                                      |
| pickle_list               | 2.90 us                                                         | 3.11 us: 1.07x slower                                                      |
| logging_simple            | 5.78 us                                                         | 6.21 us: 1.07x slower                                                      |
| tornado_http              | 81.8 ms                                                         | 87.9 ms: 1.07x slower                                                      |
| async_tree_memoization    | 264 ms                                                          | 285 ms: 1.08x slower                                                       |
| xml_etree_generate        | 53.2 ms                                                         | 57.4 ms: 1.08x slower                                                      |
| async_tree_memoization_tg | 258 ms                                                          | 279 ms: 1.08x slower                                                       |
| async_tree_none           | 218 ms                                                          | 238 ms: 1.09x slower                                                       |
| coverage                  | 42.1 ms                                                         | 46.0 ms: 1.09x slower                                                      |
| async_tree_none_tg        | 202 ms                                                          | 221 ms: 1.10x slower                                                       |
| float                     | 49.7 ms                                                         | 54.6 ms: 1.10x slower                                                      |
| async_generators          | 223 ms                                                          | 247 ms: 1.11x slower                                                       |
| xml_etree_process         | 36.4 ms                                                         | 40.3 ms: 1.11x slower                                                      |
| mdp                       | 1.31 sec                                                        | 1.47 sec: 1.12x slower                                                     |
| meteor_contest            | 69.9 ms                                                         | 78.1 ms: 1.12x slower                                                      |
| nbody                     | 67.6 ms                                                         | 75.7 ms: 1.12x slower                                                      |
| chameleon                 | 4.80 ms                                                         | 5.39 ms: 1.12x slower                                                      |
| bench_thread_pool         | 768 us                                                          | 861 us: 1.12x slower                                                       |
| docutils                  | 1.63 sec                                                        | 1.85 sec: 1.14x slower                                                     |
| deepcopy_reduce           | 1.99 us                                                         | 2.27 us: 1.14x slower                                                      |
| typing_runtime_protocols  | 101 us                                                          | 116 us: 1.15x slower                                                       |
| 2to3                      | 207 ms                                                          | 237 ms: 1.15x slower                                                       |
| tomli_loads               | 1.35 sec                                                        | 1.55 sec: 1.15x slower                                                     |
| pylint                    | 205 ms                                                          | 235 ms: 1.15x slower                                                       |
| richards_super            | 30.2 ms                                                         | 34.7 ms: 1.15x slower                                                      |
| richards                  | 26.7 ms                                                         | 30.9 ms: 1.16x slower                                                      |
| django_template           | 21.7 ms                                                         | 25.2 ms: 1.16x slower                                                      |
| html5lib                  | 35.0 ms                                                         | 40.9 ms: 1.17x slower                                                      |
| crypto_pyaes              | 45.5 ms                                                         | 53.1 ms: 1.17x slower                                                      |
| genshi_xml                | 31.6 ms                                                         | 37.0 ms: 1.17x slower                                                      |
| raytrace                  | 162 ms                                                          | 190 ms: 1.17x slower                                                       |
| fannkuch                  | 243 ms                                                          | 289 ms: 1.19x slower                                                       |
| chaos                     | 38.4 ms                                                         | 45.6 ms: 1.19x slower                                                      |
| sympy_sum                 | 84.4 ms                                                         | 101 ms: 1.19x slower                                                       |
| sqlglot_optimize          | 32.7 ms                                                         | 39.1 ms: 1.20x slower                                                      |
| pprint_safe_repr          | 474 ms                                                          | 570 ms: 1.20x slower                                                       |
| pprint_pformat            | 966 ms                                                          | 1.17 sec: 1.21x slower                                                     |
| scimark_fft               | 171 ms                                                          | 207 ms: 1.21x slower                                                       |
| sqlglot_transpile         | 955 us                                                          | 1.16 ms: 1.21x slower                                                      |
| deepcopy                  | 220 us                                                          | 266 us: 1.21x slower                                                       |
| asyncio_tcp               | 471 ms                                                          | 572 ms: 1.21x slower                                                       |
| sympy_integrate           | 12.2 ms                                                         | 14.9 ms: 1.22x slower                                                      |
| sqlglot_parse             | 748 us                                                          | 919 us: 1.23x slower                                                       |
| scimark_sor               | 75.3 ms                                                         | 92.5 ms: 1.23x slower                                                      |
| pyflate                   | 279 ms                                                          | 343 ms: 1.23x slower                                                       |
| mako                      | 6.36 ms                                                         | 7.85 ms: 1.23x slower                                                      |
| genshi_text               | 14.4 ms                                                         | 17.8 ms: 1.24x slower                                                      |
| sympy_str                 | 159 ms                                                          | 198 ms: 1.24x slower                                                       |
| sympy_expand              | 271 ms                                                          | 338 ms: 1.25x slower                                                       |
| nqueens                   | 56.7 ms                                                         | 71.2 ms: 1.26x slower                                                      |
| go                        | 82.1 ms                                                         | 104 ms: 1.27x slower                                                       |
| spectral_norm             | 63.7 ms                                                         | 81.6 ms: 1.28x slower                                                      |
| pickle_pure_python        | 175 us                                                          | 228 us: 1.30x slower                                                       |
| scimark_sparse_mat_mult   | 2.50 ms                                                         | 3.29 ms: 1.31x slower                                                      |
| scimark_monte_carlo       | 39.1 ms                                                         | 52.7 ms: 1.35x slower                                                      |
| unpickle_pure_python      | 122 us                                                          | 167 us: 1.37x slower                                                       |
| comprehensions            | 10.4 us                                                         | 14.3 us: 1.38x slower                                                      |
| deepcopy_memo             | 22.1 us                                                         | 31.2 us: 1.41x slower                                                      |
| regex_compile             | 78.0 ms                                                         | 112 ms: 1.43x slower                                                       |
| scimark_lu                | 56.6 ms                                                         | 81.6 ms: 1.44x slower                                                      |
| logging_silent            | 52.9 ns                                                         | 76.5 ns: 1.45x slower                                                      |
| deltablue                 | 1.88 ms                                                         | 2.75 ms: 1.46x slower                                                      |
| hexiom                    | 3.72 ms                                                         | 5.76 ms: 1.55x slower                                                      |
| Geometric mean            | (ref)                                                           | 1.10x slower                                                               |

Benchmark hidden because not significant (9): regex_v8, json, flaskblogging, python_startup, create_gc_cycles, async_tree_io, async_tree_cpu_io_mixed_tg, asyncio_tcp_ssl, pycparser
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, dulwich_log, mypy2, sqlglot_normalize

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.11x
- 95% likely to have a slowdown of 1.10x
- 99% likely to have a slowdown of 1.09x

# Memory
- memory change: unknown