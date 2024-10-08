# Results vs. 3.13.0b2

- fork: python
- ref: v3.10.4
- machine: windows-amd64
- commit hash: 9d38120
- commit date: 2022-03-23
- overall geometric mean: 1.23x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 246 ms: 1.19x slower                                        |
| chameleon      | 4.80 ms                                                         | 5.79 ms: 1.20x slower                                       |
| docutils       | 1.63 sec                                                        | 1.92 sec: 1.18x slower                                      |
| html5lib       | 35.0 ms                                                         | 51.0 ms: 1.46x slower                                       |
| tornado_http   | 81.8 ms                                                         | 108 ms: 1.32x slower                                        |
| Geometric mean | (ref)                                                           | 1.27x slower                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 |
|-------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_cpu_io_mixed | 389 ms                                                          | 638 ms: 1.64x slower                                        |
| async_tree_io           | 588 ms                                                          | 1.11 sec: 1.89x slower                                      |
| async_tree_memoization  | 264 ms                                                          | 526 ms: 1.99x slower                                        |
| async_tree_none         | 218 ms                                                          | 435 ms: 2.00x slower                                        |
| Geometric mean          | (ref)                                                           | 1.87x slower                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 149 ms: 1.00x faster                                        |
| nbody          | 67.6 ms                                                         | 71.3 ms: 1.05x slower                                       |
| float          | 49.7 ms                                                         | 61.7 ms: 1.24x slower                                       |
| Geometric mean | (ref)                                                           | 1.09x slower                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_effbot   | 1.58 ms                                                         | 1.66 ms: 1.05x slower                                       |
| regex_dna      | 119 ms                                                          | 136 ms: 1.15x slower                                        |
| regex_compile  | 78.0 ms                                                         | 106 ms: 1.36x slower                                        |
| Geometric mean | (ref)                                                           | 1.12x slower                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 |
|----------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------:|
| pickle_dict          | 18.1 us                                                         | 17.2 us: 1.06x faster                                       |
| pickle_list          | 2.90 us                                                         | 2.75 us: 1.06x faster                                       |
| pickle               | 7.11 us                                                         | 6.85 us: 1.04x faster                                       |
| json_loads           | 14.2 us                                                         | 14.0 us: 1.01x faster                                       |
| unpickle_list        | 2.62 us                                                         | 2.71 us: 1.04x slower                                       |
| xml_etree_iterparse  | 62.3 ms                                                         | 65.0 ms: 1.04x slower                                       |
| xml_etree_generate   | 53.2 ms                                                         | 55.5 ms: 1.04x slower                                       |
| xml_etree_parse      | 90.9 ms                                                         | 96.8 ms: 1.06x slower                                       |
| unpickle             | 8.40 us                                                         | 9.09 us: 1.08x slower                                       |
| xml_etree_process    | 36.4 ms                                                         | 44.5 ms: 1.22x slower                                       |
| tomli_loads          | 1.35 sec                                                        | 1.67 sec: 1.24x slower                                      |
| unpickle_pure_python | 122 us                                                          | 183 us: 1.50x slower                                        |
| pickle_pure_python   | 175 us                                                          | 270 us: 1.54x slower                                        |
| json_dumps           | 5.61 ms                                                         | 9.16 ms: 1.63x slower                                       |
| Geometric mean       | (ref)                                                           | 1.14x slower                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 |
|------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                         | 15.5 ms: 1.05x faster                                       |
| python_startup         | 20.3 ms                                                         | 20.6 ms: 1.02x slower                                       |
| Geometric mean         | (ref)                                                           | 1.01x faster                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 |
|-----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------:|
| genshi_xml      | 31.6 ms                                                         | 41.0 ms: 1.30x slower                                       |
| django_template | 21.7 ms                                                         | 28.9 ms: 1.33x slower                                       |
| genshi_text     | 14.4 ms                                                         | 19.8 ms: 1.38x slower                                       |
| mako            | 6.36 ms                                                         | 9.03 ms: 1.42x slower                                       |
| Geometric mean  | (ref)                                                           | 1.36x slower                                                |

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 |
|--------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------:|
| thrift                   | 8.11 ms                                                         | 617 us: 13.13x faster                                       |
| telco                    | 4.67 ms                                                         | 3.94 ms: 1.19x faster                                       |
| create_gc_cycles         | 888 us                                                          | 800 us: 1.11x faster                                        |
| gc_traversal             | 1.55 ms                                                         | 1.41 ms: 1.10x faster                                       |
| coverage                 | 42.1 ms                                                         | 39.0 ms: 1.08x faster                                       |
| pickle_dict              | 18.1 us                                                         | 17.2 us: 1.06x faster                                       |
| pickle_list              | 2.90 us                                                         | 2.75 us: 1.06x faster                                       |
| python_startup_no_site   | 16.2 ms                                                         | 15.5 ms: 1.05x faster                                       |
| bench_mp_pool            | 64.8 ms                                                         | 62.0 ms: 1.04x faster                                       |
| pickle                   | 7.11 us                                                         | 6.85 us: 1.04x faster                                       |
| json_loads               | 14.2 us                                                         | 14.0 us: 1.01x faster                                       |
| async_generators         | 223 ms                                                          | 222 ms: 1.01x faster                                        |
| pidigits                 | 150 ms                                                          | 149 ms: 1.00x faster                                        |
| flaskblogging            | 2.03 sec                                                        | 2.03 sec: 1.00x faster                                      |
| python_startup           | 20.3 ms                                                         | 20.6 ms: 1.02x slower                                       |
| unpickle_list            | 2.62 us                                                         | 2.71 us: 1.04x slower                                       |
| xml_etree_iterparse      | 62.3 ms                                                         | 65.0 ms: 1.04x slower                                       |
| xml_etree_generate       | 53.2 ms                                                         | 55.5 ms: 1.04x slower                                       |
| regex_effbot             | 1.58 ms                                                         | 1.66 ms: 1.05x slower                                       |
| fannkuch                 | 243 ms                                                          | 256 ms: 1.05x slower                                        |
| nbody                    | 67.6 ms                                                         | 71.3 ms: 1.05x slower                                       |
| xml_etree_parse          | 90.9 ms                                                         | 96.8 ms: 1.06x slower                                       |
| logging_simple           | 5.78 us                                                         | 6.22 us: 1.08x slower                                       |
| unpickle                 | 8.40 us                                                         | 9.09 us: 1.08x slower                                       |
| logging_format           | 6.22 us                                                         | 6.76 us: 1.09x slower                                       |
| meteor_contest           | 69.9 ms                                                         | 75.9 ms: 1.09x slower                                       |
| scimark_sparse_mat_mult  | 2.50 ms                                                         | 2.72 ms: 1.09x slower                                       |
| scimark_fft              | 171 ms                                                          | 187 ms: 1.10x slower                                        |
| deepcopy_reduce          | 1.99 us                                                         | 2.20 us: 1.10x slower                                       |
| aiohttp                  | 889 us                                                          | 995 us: 1.12x slower                                        |
| regex_dna                | 119 ms                                                          | 136 ms: 1.15x slower                                        |
| sympy_expand             | 271 ms                                                          | 314 ms: 1.16x slower                                        |
| deepcopy                 | 220 us                                                          | 255 us: 1.16x slower                                        |
| nqueens                  | 56.7 ms                                                         | 66.6 ms: 1.18x slower                                       |
| docutils                 | 1.63 sec                                                        | 1.92 sec: 1.18x slower                                      |
| sqlglot_normalize        | 173 ms                                                          | 205 ms: 1.19x slower                                        |
| 2to3                     | 207 ms                                                          | 246 ms: 1.19x slower                                        |
| sqlite_synth             | 1.60 us                                                         | 1.91 us: 1.20x slower                                       |
| chameleon                | 4.80 ms                                                         | 5.79 ms: 1.20x slower                                       |
| spectral_norm            | 63.7 ms                                                         | 77.3 ms: 1.21x slower                                       |
| sqlglot_optimize         | 32.7 ms                                                         | 39.8 ms: 1.22x slower                                       |
| xml_etree_process        | 36.4 ms                                                         | 44.5 ms: 1.22x slower                                       |
| sympy_str                | 159 ms                                                          | 194 ms: 1.22x slower                                        |
| pycparser                | 754 ms                                                          | 930 ms: 1.23x slower                                        |
| tomli_loads              | 1.35 sec                                                        | 1.67 sec: 1.24x slower                                      |
| float                    | 49.7 ms                                                         | 61.7 ms: 1.24x slower                                       |
| bench_thread_pool        | 768 us                                                          | 958 us: 1.25x slower                                        |
| pprint_safe_repr         | 474 ms                                                          | 592 ms: 1.25x slower                                        |
| sympy_integrate          | 12.2 ms                                                         | 15.3 ms: 1.25x slower                                       |
| coroutines               | 12.8 ms                                                         | 16.0 ms: 1.25x slower                                       |
| pprint_pformat           | 966 ms                                                          | 1.22 sec: 1.26x slower                                      |
| sympy_sum                | 84.4 ms                                                         | 107 ms: 1.27x slower                                        |
| genshi_xml               | 31.6 ms                                                         | 41.0 ms: 1.30x slower                                       |
| deepcopy_memo            | 22.1 us                                                         | 28.8 us: 1.30x slower                                       |
| tornado_http             | 81.8 ms                                                         | 108 ms: 1.32x slower                                        |
| dulwich_log              | 38.0 ms                                                         | 50.5 ms: 1.33x slower                                       |
| mypy2                    | 418 ms                                                          | 555 ms: 1.33x slower                                        |
| django_template          | 21.7 ms                                                         | 28.9 ms: 1.33x slower                                       |
| mdp                      | 1.31 sec                                                        | 1.78 sec: 1.36x slower                                      |
| regex_compile            | 78.0 ms                                                         | 106 ms: 1.36x slower                                        |
| crypto_pyaes             | 45.5 ms                                                         | 62.5 ms: 1.38x slower                                       |
| genshi_text              | 14.4 ms                                                         | 19.8 ms: 1.38x slower                                       |
| scimark_sor              | 75.3 ms                                                         | 106 ms: 1.41x slower                                        |
| mako                     | 6.36 ms                                                         | 9.03 ms: 1.42x slower                                       |
| asyncio_tcp_ssl          | 1.48 sec                                                        | 2.11 sec: 1.43x slower                                      |
| html5lib                 | 35.0 ms                                                         | 51.0 ms: 1.46x slower                                       |
| scimark_monte_carlo      | 39.1 ms                                                         | 57.3 ms: 1.46x slower                                       |
| pyflate                  | 279 ms                                                          | 409 ms: 1.47x slower                                        |
| unpickle_pure_python     | 122 us                                                          | 183 us: 1.50x slower                                        |
| scimark_lu               | 56.6 ms                                                         | 85.8 ms: 1.52x slower                                       |
| pickle_pure_python       | 175 us                                                          | 270 us: 1.54x slower                                        |
| hexiom                   | 3.72 ms                                                         | 5.74 ms: 1.54x slower                                       |
| sqlglot_transpile        | 955 us                                                          | 1.48 ms: 1.54x slower                                       |
| asyncio_tcp              | 471 ms                                                          | 732 ms: 1.55x slower                                        |
| richards                 | 26.7 ms                                                         | 42.4 ms: 1.59x slower                                       |
| comprehensions           | 10.4 us                                                         | 16.5 us: 1.59x slower                                       |
| chaos                    | 38.4 ms                                                         | 61.7 ms: 1.61x slower                                       |
| sqlglot_parse            | 748 us                                                          | 1.22 ms: 1.62x slower                                       |
| json_dumps               | 5.61 ms                                                         | 9.16 ms: 1.63x slower                                       |
| async_tree_cpu_io_mixed  | 389 ms                                                          | 638 ms: 1.64x slower                                        |
| generators               | 19.6 ms                                                         | 32.4 ms: 1.66x slower                                       |
| raytrace                 | 162 ms                                                          | 273 ms: 1.68x slower                                        |
| go                       | 82.1 ms                                                         | 139 ms: 1.69x slower                                        |
| pylint                   | 205 ms                                                          | 350 ms: 1.71x slower                                        |
| richards_super           | 30.2 ms                                                         | 52.2 ms: 1.73x slower                                       |
| logging_silent           | 52.9 ns                                                         | 94.6 ns: 1.79x slower                                       |
| async_tree_io            | 588 ms                                                          | 1.11 sec: 1.89x slower                                      |
| async_tree_memoization   | 264 ms                                                          | 526 ms: 1.99x slower                                        |
| async_tree_none          | 218 ms                                                          | 435 ms: 2.00x slower                                        |
| deltablue                | 1.88 ms                                                         | 4.19 ms: 2.22x slower                                       |
| typing_runtime_protocols | 101 us                                                          | 336 us: 3.33x slower                                        |
| Geometric mean           | (ref)                                                           | 1.23x slower                                                |

Benchmark hidden because not significant (3): regex_v8, json, pathlib
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.22x
- 95% likely to have a slowdown of 1.21x
- 99% likely to have a slowdown of 1.19x

# Memory
- memory change: unknown