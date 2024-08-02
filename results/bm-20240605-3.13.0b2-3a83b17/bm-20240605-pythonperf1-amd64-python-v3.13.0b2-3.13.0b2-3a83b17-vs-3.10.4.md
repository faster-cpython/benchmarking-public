# Results vs. 3.10.4

- fork: python
- ref: v3.13.0b2
- machine: windows-amd64
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.23x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 207 ms: 1.19x faster                                            |
| chameleon      | 5.79 ms                                                     | 4.80 ms: 1.20x faster                                           |
| docutils       | 1.92 sec                                                    | 1.63 sec: 1.18x faster                                          |
| html5lib       | 51.0 ms                                                     | 35.0 ms: 1.46x faster                                           |
| tornado_http   | 108 ms                                                      | 81.8 ms: 1.32x faster                                           |
| Geometric mean | (ref)                                                       | 1.27x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 218 ms: 2.00x faster                                            |
| async_tree_memoization  | 526 ms                                                      | 264 ms: 1.99x faster                                            |
| async_tree_io           | 1.11 sec                                                    | 588 ms: 1.89x faster                                            |
| async_tree_cpu_io_mixed | 638 ms                                                      | 389 ms: 1.64x faster                                            |
| Geometric mean          | (ref)                                                       | 1.87x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 49.7 ms: 1.24x faster                                           |
| nbody          | 71.3 ms                                                     | 67.6 ms: 1.05x faster                                           |
| pidigits       | 149 ms                                                      | 150 ms: 1.00x slower                                            |
| Geometric mean | (ref)                                                       | 1.09x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 78.0 ms: 1.36x faster                                           |
| regex_dna      | 136 ms                                                      | 119 ms: 1.15x faster                                            |
| regex_effbot   | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                           |
| Geometric mean | (ref)                                                       | 1.12x faster                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.61 ms: 1.63x faster                                           |
| pickle_pure_python   | 270 us                                                      | 175 us: 1.54x faster                                            |
| unpickle_pure_python | 183 us                                                      | 122 us: 1.50x faster                                            |
| tomli_loads          | 1.67 sec                                                    | 1.35 sec: 1.24x faster                                          |
| xml_etree_process    | 44.5 ms                                                     | 36.4 ms: 1.22x faster                                           |
| unpickle             | 9.09 us                                                     | 8.40 us: 1.08x faster                                           |
| xml_etree_parse      | 96.8 ms                                                     | 90.9 ms: 1.06x faster                                           |
| xml_etree_generate   | 55.5 ms                                                     | 53.2 ms: 1.04x faster                                           |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.3 ms: 1.04x faster                                           |
| unpickle_list        | 2.71 us                                                     | 2.62 us: 1.04x faster                                           |
| json_loads           | 14.0 us                                                     | 14.2 us: 1.01x slower                                           |
| pickle               | 6.85 us                                                     | 7.11 us: 1.04x slower                                           |
| pickle_list          | 2.75 us                                                     | 2.90 us: 1.06x slower                                           |
| pickle_dict          | 17.2 us                                                     | 18.1 us: 1.06x slower                                           |
| Geometric mean       | (ref)                                                       | 1.14x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 20.3 ms: 1.02x faster                                           |
| python_startup_no_site | 15.5 ms                                                     | 16.2 ms: 1.05x slower                                           |
| Geometric mean         | (ref)                                                       | 1.01x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.36 ms: 1.42x faster                                           |
| genshi_text     | 19.8 ms                                                     | 14.4 ms: 1.38x faster                                           |
| django_template | 28.9 ms                                                     | 21.7 ms: 1.33x faster                                           |
| genshi_xml      | 41.0 ms                                                     | 31.6 ms: 1.30x faster                                           |
| Geometric mean  | (ref)                                                       | 1.36x faster                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 101 us: 3.33x faster                                            |
| deltablue                | 4.19 ms                                                     | 1.88 ms: 2.22x faster                                           |
| async_tree_none          | 435 ms                                                      | 218 ms: 2.00x faster                                            |
| async_tree_memoization   | 526 ms                                                      | 264 ms: 1.99x faster                                            |
| async_tree_io            | 1.11 sec                                                    | 588 ms: 1.89x faster                                            |
| logging_silent           | 94.6 ns                                                     | 52.9 ns: 1.79x faster                                           |
| richards_super           | 52.2 ms                                                     | 30.2 ms: 1.73x faster                                           |
| pylint                   | 350 ms                                                      | 205 ms: 1.71x faster                                            |
| go                       | 139 ms                                                      | 82.1 ms: 1.69x faster                                           |
| raytrace                 | 273 ms                                                      | 162 ms: 1.68x faster                                            |
| generators               | 32.4 ms                                                     | 19.6 ms: 1.66x faster                                           |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 389 ms: 1.64x faster                                            |
| json_dumps               | 9.16 ms                                                     | 5.61 ms: 1.63x faster                                           |
| sqlglot_parse            | 1.22 ms                                                     | 748 us: 1.62x faster                                            |
| chaos                    | 61.7 ms                                                     | 38.4 ms: 1.61x faster                                           |
| comprehensions           | 16.5 us                                                     | 10.4 us: 1.59x faster                                           |
| richards                 | 42.4 ms                                                     | 26.7 ms: 1.59x faster                                           |
| asyncio_tcp              | 732 ms                                                      | 471 ms: 1.55x faster                                            |
| sqlglot_transpile        | 1.48 ms                                                     | 955 us: 1.54x faster                                            |
| hexiom                   | 5.74 ms                                                     | 3.72 ms: 1.54x faster                                           |
| pickle_pure_python       | 270 us                                                      | 175 us: 1.54x faster                                            |
| scimark_lu               | 85.8 ms                                                     | 56.6 ms: 1.52x faster                                           |
| unpickle_pure_python     | 183 us                                                      | 122 us: 1.50x faster                                            |
| pyflate                  | 409 ms                                                      | 279 ms: 1.47x faster                                            |
| scimark_monte_carlo      | 57.3 ms                                                     | 39.1 ms: 1.46x faster                                           |
| html5lib                 | 51.0 ms                                                     | 35.0 ms: 1.46x faster                                           |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.48 sec: 1.43x faster                                          |
| mako                     | 9.03 ms                                                     | 6.36 ms: 1.42x faster                                           |
| scimark_sor              | 106 ms                                                      | 75.3 ms: 1.41x faster                                           |
| genshi_text              | 19.8 ms                                                     | 14.4 ms: 1.38x faster                                           |
| crypto_pyaes             | 62.5 ms                                                     | 45.5 ms: 1.38x faster                                           |
| regex_compile            | 106 ms                                                      | 78.0 ms: 1.36x faster                                           |
| mdp                      | 1.78 sec                                                    | 1.31 sec: 1.36x faster                                          |
| django_template          | 28.9 ms                                                     | 21.7 ms: 1.33x faster                                           |
| mypy2                    | 555 ms                                                      | 418 ms: 1.33x faster                                            |
| dulwich_log              | 50.5 ms                                                     | 38.0 ms: 1.33x faster                                           |
| tornado_http             | 108 ms                                                      | 81.8 ms: 1.32x faster                                           |
| deepcopy_memo            | 28.8 us                                                     | 22.1 us: 1.30x faster                                           |
| genshi_xml               | 41.0 ms                                                     | 31.6 ms: 1.30x faster                                           |
| sympy_sum                | 107 ms                                                      | 84.4 ms: 1.27x faster                                           |
| pprint_pformat           | 1.22 sec                                                    | 966 ms: 1.26x faster                                            |
| coroutines               | 16.0 ms                                                     | 12.8 ms: 1.25x faster                                           |
| sympy_integrate          | 15.3 ms                                                     | 12.2 ms: 1.25x faster                                           |
| pprint_safe_repr         | 592 ms                                                      | 474 ms: 1.25x faster                                            |
| bench_thread_pool        | 958 us                                                      | 768 us: 1.25x faster                                            |
| float                    | 61.7 ms                                                     | 49.7 ms: 1.24x faster                                           |
| tomli_loads              | 1.67 sec                                                    | 1.35 sec: 1.24x faster                                          |
| pycparser                | 930 ms                                                      | 754 ms: 1.23x faster                                            |
| sympy_str                | 194 ms                                                      | 159 ms: 1.22x faster                                            |
| xml_etree_process        | 44.5 ms                                                     | 36.4 ms: 1.22x faster                                           |
| sqlglot_optimize         | 39.8 ms                                                     | 32.7 ms: 1.22x faster                                           |
| spectral_norm            | 77.3 ms                                                     | 63.7 ms: 1.21x faster                                           |
| chameleon                | 5.79 ms                                                     | 4.80 ms: 1.20x faster                                           |
| sqlite_synth             | 1.91 us                                                     | 1.60 us: 1.20x faster                                           |
| 2to3                     | 246 ms                                                      | 207 ms: 1.19x faster                                            |
| sqlglot_normalize        | 205 ms                                                      | 173 ms: 1.19x faster                                            |
| docutils                 | 1.92 sec                                                    | 1.63 sec: 1.18x faster                                          |
| nqueens                  | 66.6 ms                                                     | 56.7 ms: 1.18x faster                                           |
| deepcopy                 | 255 us                                                      | 220 us: 1.16x faster                                            |
| sympy_expand             | 314 ms                                                      | 271 ms: 1.16x faster                                            |
| regex_dna                | 136 ms                                                      | 119 ms: 1.15x faster                                            |
| aiohttp                  | 995 us                                                      | 889 us: 1.12x faster                                            |
| deepcopy_reduce          | 2.20 us                                                     | 1.99 us: 1.10x faster                                           |
| scimark_fft              | 187 ms                                                      | 171 ms: 1.10x faster                                            |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.50 ms: 1.09x faster                                           |
| meteor_contest           | 75.9 ms                                                     | 69.9 ms: 1.09x faster                                           |
| logging_format           | 6.76 us                                                     | 6.22 us: 1.09x faster                                           |
| unpickle                 | 9.09 us                                                     | 8.40 us: 1.08x faster                                           |
| logging_simple           | 6.22 us                                                     | 5.78 us: 1.08x faster                                           |
| xml_etree_parse          | 96.8 ms                                                     | 90.9 ms: 1.06x faster                                           |
| nbody                    | 71.3 ms                                                     | 67.6 ms: 1.05x faster                                           |
| fannkuch                 | 256 ms                                                      | 243 ms: 1.05x faster                                            |
| regex_effbot             | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                           |
| xml_etree_generate       | 55.5 ms                                                     | 53.2 ms: 1.04x faster                                           |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.3 ms: 1.04x faster                                           |
| unpickle_list            | 2.71 us                                                     | 2.62 us: 1.04x faster                                           |
| python_startup           | 20.6 ms                                                     | 20.3 ms: 1.02x faster                                           |
| flaskblogging            | 2.03 sec                                                    | 2.03 sec: 1.00x slower                                          |
| pidigits                 | 149 ms                                                      | 150 ms: 1.00x slower                                            |
| async_generators         | 222 ms                                                      | 223 ms: 1.01x slower                                            |
| json_loads               | 14.0 us                                                     | 14.2 us: 1.01x slower                                           |
| pickle                   | 6.85 us                                                     | 7.11 us: 1.04x slower                                           |
| bench_mp_pool            | 62.0 ms                                                     | 64.8 ms: 1.04x slower                                           |
| python_startup_no_site   | 15.5 ms                                                     | 16.2 ms: 1.05x slower                                           |
| pickle_list              | 2.75 us                                                     | 2.90 us: 1.06x slower                                           |
| pickle_dict              | 17.2 us                                                     | 18.1 us: 1.06x slower                                           |
| coverage                 | 39.0 ms                                                     | 42.1 ms: 1.08x slower                                           |
| gc_traversal             | 1.41 ms                                                     | 1.55 ms: 1.10x slower                                           |
| create_gc_cycles         | 800 us                                                      | 888 us: 1.11x slower                                            |
| telco                    | 3.94 ms                                                     | 4.67 ms: 1.19x slower                                           |
| thrift                   | 617 us                                                      | 8.11 ms: 13.13x slower                                          |
| Geometric mean           | (ref)                                                       | 1.23x faster                                                    |

Benchmark hidden because not significant (3): pathlib, json, regex_v8
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: unknown