# Results vs. 3.10.4

- fork: python
- ref: v3.14.0a1
- machine: windows-amd64
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.153x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 231 ms: 1.06x faster                                            |
| docutils       | 1.92 sec                                                    | 1.72 sec: 1.12x faster                                          |
| html5lib       | 51.0 ms                                                     | 40.8 ms: 1.25x faster                                           |
| tornado_http   | 108 ms                                                      | 93.8 ms: 1.15x faster                                           |
| Geometric mean | (ref)                                                       | 1.14x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 574 ms: 1.93x faster                                            |
| async_tree_none         | 435 ms                                                      | 226 ms: 1.93x faster                                            |
| async_tree_memoization  | 526 ms                                                      | 281 ms: 1.87x faster                                            |
| async_tree_cpu_io_mixed | 638 ms                                                      | 386 ms: 1.65x faster                                            |
| Geometric mean          | (ref)                                                       | 1.84x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 55.6 ms: 1.11x faster                                           |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                            |
| nbody          | 71.3 ms                                                     | 79.3 ms: 1.11x slower                                           |
| Geometric mean | (ref)                                                       | 1.00x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 116 ms: 1.17x faster                                            |
| regex_compile  | 106 ms                                                      | 91.1 ms: 1.16x faster                                           |
| regex_effbot   | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                           |
| Geometric mean | (ref)                                                       | 1.07x faster                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.93 ms: 1.32x faster                                           |
| pickle_pure_python   | 270 us                                                      | 217 us: 1.24x faster                                            |
| unpickle_pure_python | 183 us                                                      | 151 us: 1.21x faster                                            |
| xml_etree_process    | 44.5 ms                                                     | 41.7 ms: 1.07x faster                                           |
| tomli_loads          | 1.67 sec                                                    | 1.61 sec: 1.04x faster                                          |
| xml_etree_parse      | 96.8 ms                                                     | 95.4 ms: 1.02x faster                                           |
| unpickle             | 9.09 us                                                     | 9.00 us: 1.01x faster                                           |
| xml_etree_iterparse  | 65.0 ms                                                     | 66.3 ms: 1.02x slower                                           |
| unpickle_list        | 2.71 us                                                     | 2.83 us: 1.04x slower                                           |
| xml_etree_generate   | 55.5 ms                                                     | 59.3 ms: 1.07x slower                                           |
| pickle               | 6.85 us                                                     | 7.37 us: 1.08x slower                                           |
| pickle_list          | 2.75 us                                                     | 3.00 us: 1.09x slower                                           |
| json_loads           | 14.0 us                                                     | 15.5 us: 1.11x slower                                           |
| pickle_dict          | 17.2 us                                                     | 19.3 us: 1.12x slower                                           |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 18.3 ms: 1.18x slower                                           |
| python_startup         | 20.6 ms                                                     | 24.6 ms: 1.19x slower                                           |
| Geometric mean         | (ref)                                                       | 1.19x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.73 ms: 1.34x faster                                           |
| genshi_text     | 19.8 ms                                                     | 17.5 ms: 1.13x faster                                           |
| django_template | 28.9 ms                                                     | 25.9 ms: 1.11x faster                                           |
| genshi_xml      | 41.0 ms                                                     | 39.6 ms: 1.04x faster                                           |
| Geometric mean  | (ref)                                                       | 1.15x faster                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 112 us: 2.99x faster                                            |
| async_tree_io            | 1.11 sec                                                    | 574 ms: 1.93x faster                                            |
| async_tree_none          | 435 ms                                                      | 226 ms: 1.93x faster                                            |
| async_tree_memoization   | 526 ms                                                      | 281 ms: 1.87x faster                                            |
| deltablue                | 4.19 ms                                                     | 2.29 ms: 1.83x faster                                           |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 386 ms: 1.65x faster                                            |
| go                       | 139 ms                                                      | 88.5 ms: 1.57x faster                                           |
| pylint                   | 350 ms                                                      | 229 ms: 1.53x faster                                            |
| logging_silent           | 94.6 ns                                                     | 62.9 ns: 1.51x faster                                           |
| generators               | 32.4 ms                                                     | 22.1 ms: 1.47x faster                                           |
| richards_super           | 52.2 ms                                                     | 36.8 ms: 1.42x faster                                           |
| deepcopy_memo            | 28.8 us                                                     | 20.4 us: 1.41x faster                                           |
| comprehensions           | 16.5 us                                                     | 11.9 us: 1.39x faster                                           |
| chaos                    | 61.7 ms                                                     | 44.6 ms: 1.38x faster                                           |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.53 sec: 1.38x faster                                          |
| raytrace                 | 273 ms                                                      | 198 ms: 1.38x faster                                            |
| scimark_lu               | 85.8 ms                                                     | 63.2 ms: 1.36x faster                                           |
| mako                     | 9.03 ms                                                     | 6.73 ms: 1.34x faster                                           |
| json_dumps               | 9.16 ms                                                     | 6.93 ms: 1.32x faster                                           |
| deepcopy                 | 255 us                                                      | 194 us: 1.32x faster                                            |
| sqlglot_parse            | 1.22 ms                                                     | 921 us: 1.32x faster                                            |
| richards                 | 42.4 ms                                                     | 32.3 ms: 1.32x faster                                           |
| sqlglot_transpile        | 1.48 ms                                                     | 1.14 ms: 1.29x faster                                           |
| hexiom                   | 5.74 ms                                                     | 4.46 ms: 1.29x faster                                           |
| pyflate                  | 409 ms                                                      | 327 ms: 1.25x faster                                            |
| html5lib                 | 51.0 ms                                                     | 40.8 ms: 1.25x faster                                           |
| crypto_pyaes             | 62.5 ms                                                     | 50.3 ms: 1.24x faster                                           |
| pickle_pure_python       | 270 us                                                      | 217 us: 1.24x faster                                            |
| pycparser                | 930 ms                                                      | 756 ms: 1.23x faster                                            |
| unpickle_pure_python     | 183 us                                                      | 151 us: 1.21x faster                                            |
| mdp                      | 1.78 sec                                                    | 1.50 sec: 1.19x faster                                          |
| scimark_monte_carlo      | 57.3 ms                                                     | 48.2 ms: 1.19x faster                                           |
| sympy_sum                | 107 ms                                                      | 90.9 ms: 1.18x faster                                           |
| regex_dna                | 136 ms                                                      | 116 ms: 1.17x faster                                            |
| sqlite_synth             | 1.91 us                                                     | 1.63 us: 1.17x faster                                           |
| regex_compile            | 106 ms                                                      | 91.1 ms: 1.16x faster                                           |
| dulwich_log              | 50.5 ms                                                     | 43.6 ms: 1.16x faster                                           |
| tornado_http             | 108 ms                                                      | 93.8 ms: 1.15x faster                                           |
| coroutines               | 16.0 ms                                                     | 13.9 ms: 1.15x faster                                           |
| bench_thread_pool        | 958 us                                                      | 831 us: 1.15x faster                                            |
| thrift                   | 617 us                                                      | 539 us: 1.15x faster                                            |
| scimark_sor              | 106 ms                                                      | 93.2 ms: 1.14x faster                                           |
| genshi_text              | 19.8 ms                                                     | 17.5 ms: 1.13x faster                                           |
| sympy_integrate          | 15.3 ms                                                     | 13.5 ms: 1.13x faster                                           |
| docutils                 | 1.92 sec                                                    | 1.72 sec: 1.12x faster                                          |
| django_template          | 28.9 ms                                                     | 25.9 ms: 1.11x faster                                           |
| float                    | 61.7 ms                                                     | 55.6 ms: 1.11x faster                                           |
| asyncio_tcp              | 732 ms                                                      | 661 ms: 1.11x faster                                            |
| deepcopy_reduce          | 2.20 us                                                     | 2.02 us: 1.09x faster                                           |
| sympy_str                | 194 ms                                                      | 181 ms: 1.08x faster                                            |
| sqlglot_optimize         | 39.8 ms                                                     | 37.2 ms: 1.07x faster                                           |
| pprint_pformat           | 1.22 sec                                                    | 1.14 sec: 1.07x faster                                          |
| xml_etree_process        | 44.5 ms                                                     | 41.7 ms: 1.07x faster                                           |
| 2to3                     | 246 ms                                                      | 231 ms: 1.06x faster                                            |
| spectral_norm            | 77.3 ms                                                     | 72.9 ms: 1.06x faster                                           |
| pprint_safe_repr         | 592 ms                                                      | 565 ms: 1.05x faster                                            |
| nqueens                  | 66.6 ms                                                     | 63.9 ms: 1.04x faster                                           |
| regex_effbot             | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                           |
| genshi_xml               | 41.0 ms                                                     | 39.6 ms: 1.04x faster                                           |
| tomli_loads              | 1.67 sec                                                    | 1.61 sec: 1.04x faster                                          |
| sqlglot_normalize        | 205 ms                                                      | 199 ms: 1.03x faster                                            |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.68 ms: 1.02x faster                                           |
| xml_etree_parse          | 96.8 ms                                                     | 95.4 ms: 1.02x faster                                           |
| unpickle                 | 9.09 us                                                     | 9.00 us: 1.01x faster                                           |
| sympy_expand             | 314 ms                                                      | 312 ms: 1.01x faster                                            |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                            |
| logging_format           | 6.76 us                                                     | 6.85 us: 1.01x slower                                           |
| meteor_contest           | 75.9 ms                                                     | 77.0 ms: 1.01x slower                                           |
| xml_etree_iterparse      | 65.0 ms                                                     | 66.3 ms: 1.02x slower                                           |
| logging_simple           | 6.22 us                                                     | 6.42 us: 1.03x slower                                           |
| unpickle_list            | 2.71 us                                                     | 2.83 us: 1.04x slower                                           |
| pathlib                  | 75.7 ms                                                     | 80.8 ms: 1.07x slower                                           |
| xml_etree_generate       | 55.5 ms                                                     | 59.3 ms: 1.07x slower                                           |
| pickle                   | 6.85 us                                                     | 7.37 us: 1.08x slower                                           |
| scimark_fft              | 187 ms                                                      | 202 ms: 1.08x slower                                            |
| unpack_sequence          | 39.6 ns                                                     | 42.7 ns: 1.08x slower                                           |
| pickle_list              | 2.75 us                                                     | 3.00 us: 1.09x slower                                           |
| json_loads               | 14.0 us                                                     | 15.5 us: 1.11x slower                                           |
| nbody                    | 71.3 ms                                                     | 79.3 ms: 1.11x slower                                           |
| fannkuch                 | 256 ms                                                      | 286 ms: 1.12x slower                                            |
| async_generators         | 222 ms                                                      | 249 ms: 1.12x slower                                            |
| pickle_dict              | 17.2 us                                                     | 19.3 us: 1.12x slower                                           |
| python_startup_no_site   | 15.5 ms                                                     | 18.3 ms: 1.18x slower                                           |
| python_startup           | 20.6 ms                                                     | 24.6 ms: 1.19x slower                                           |
| telco                    | 3.94 ms                                                     | 4.89 ms: 1.24x slower                                           |
| coverage                 | 39.0 ms                                                     | 49.0 ms: 1.26x slower                                           |
| bench_mp_pool            | 62.0 ms                                                     | 84.0 ms: 1.35x slower                                           |
| gc_traversal             | 1.41 ms                                                     | 1.97 ms: 1.40x slower                                           |
| create_gc_cycles         | 800 us                                                      | 1.41 ms: 1.77x slower                                           |
| Geometric mean           | (ref)                                                       | 1.13x faster                                                    |

Benchmark hidden because not significant (2): json, regex_v8
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx

- Geometric mean (including insignificant results): 1.153x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: unknown