# Results vs. 3.10.4

- fork: python
- ref: v3.13.0rc1
- machine: windows-amd64
- commit hash: e4a3e78
- commit date: 2024-07-31
- overall geometric mean: 1.184x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf1-amd64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 226 ms: 1.09x faster                                              |
| chameleon      | 5.79 ms                                                     | 5.10 ms: 1.13x faster                                             |
| docutils       | 1.92 sec                                                    | 1.68 sec: 1.14x faster                                            |
| html5lib       | 51.0 ms                                                     | 39.1 ms: 1.31x faster                                             |
| tornado_http   | 108 ms                                                      | 92.0 ms: 1.18x faster                                             |
| Geometric mean | (ref)                                                       | 1.17x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf1-amd64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|-------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 228 ms: 1.91x faster                                              |
| async_tree_memoization  | 526 ms                                                      | 278 ms: 1.89x faster                                              |
| async_tree_io           | 1.11 sec                                                    | 603 ms: 1.84x faster                                              |
| async_tree_cpu_io_mixed | 638 ms                                                      | 396 ms: 1.61x faster                                              |
| Geometric mean          | (ref)                                                       | 1.81x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf1-amd64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 50.1 ms: 1.23x faster                                             |
| pidigits       | 149 ms                                                      | 151 ms: 1.01x slower                                              |
| nbody          | 71.3 ms                                                     | 76.8 ms: 1.08x slower                                             |
| Geometric mean | (ref)                                                       | 1.04x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf1-amd64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 83.9 ms: 1.26x faster                                             |
| regex_dna      | 136 ms                                                      | 123 ms: 1.11x faster                                              |
| regex_effbot   | 1.66 ms                                                     | 1.62 ms: 1.03x faster                                             |
| Geometric mean | (ref)                                                       | 1.08x faster                                                      |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf1-amd64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.90 ms: 1.55x faster                                             |
| pickle_pure_python   | 270 us                                                      | 194 us: 1.39x faster                                              |
| unpickle_pure_python | 183 us                                                      | 138 us: 1.33x faster                                              |
| tomli_loads          | 1.67 sec                                                    | 1.42 sec: 1.18x faster                                            |
| xml_etree_process    | 44.5 ms                                                     | 38.4 ms: 1.16x faster                                             |
| xml_etree_parse      | 96.8 ms                                                     | 91.5 ms: 1.06x faster                                             |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.0 ms: 1.03x faster                                             |
| json_loads           | 14.0 us                                                     | 14.2 us: 1.01x slower                                             |
| Geometric mean       | (ref)                                                       | 1.17x faster                                                      |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf1-amd64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.5 ms: 1.09x slower                                             |
| python_startup_no_site | 15.5 ms                                                     | 18.4 ms: 1.19x slower                                             |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf1-amd64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.66 ms: 1.36x faster                                             |
| genshi_text     | 19.8 ms                                                     | 15.3 ms: 1.29x faster                                             |
| django_template | 28.9 ms                                                     | 22.7 ms: 1.27x faster                                             |
| genshi_xml      | 41.0 ms                                                     | 33.2 ms: 1.24x faster                                             |
| Geometric mean  | (ref)                                                       | 1.29x faster                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf1-amd64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|--------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 106 us: 3.17x faster                                              |
| deltablue                | 4.19 ms                                                     | 2.01 ms: 2.08x faster                                             |
| async_tree_none          | 435 ms                                                      | 228 ms: 1.91x faster                                              |
| async_tree_memoization   | 526 ms                                                      | 278 ms: 1.89x faster                                              |
| async_tree_io            | 1.11 sec                                                    | 603 ms: 1.84x faster                                              |
| logging_silent           | 94.6 ns                                                     | 56.1 ns: 1.69x faster                                             |
| raytrace                 | 273 ms                                                      | 164 ms: 1.67x faster                                              |
| richards_super           | 52.2 ms                                                     | 32.1 ms: 1.63x faster                                             |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 396 ms: 1.61x faster                                              |
| pylint                   | 350 ms                                                      | 220 ms: 1.59x faster                                              |
| generators               | 32.4 ms                                                     | 20.6 ms: 1.57x faster                                             |
| go                       | 139 ms                                                      | 88.6 ms: 1.57x faster                                             |
| json_dumps               | 9.16 ms                                                     | 5.90 ms: 1.55x faster                                             |
| chaos                    | 61.7 ms                                                     | 40.4 ms: 1.53x faster                                             |
| sqlglot_parse            | 1.22 ms                                                     | 803 us: 1.51x faster                                              |
| comprehensions           | 16.5 us                                                     | 10.9 us: 1.51x faster                                             |
| richards                 | 42.4 ms                                                     | 28.3 ms: 1.50x faster                                             |
| sqlglot_transpile        | 1.48 ms                                                     | 1.01 ms: 1.46x faster                                             |
| hexiom                   | 5.74 ms                                                     | 4.08 ms: 1.41x faster                                             |
| scimark_lu               | 85.8 ms                                                     | 61.4 ms: 1.40x faster                                             |
| pickle_pure_python       | 270 us                                                      | 194 us: 1.39x faster                                              |
| pyflate                  | 409 ms                                                      | 298 ms: 1.37x faster                                              |
| mako                     | 9.03 ms                                                     | 6.66 ms: 1.36x faster                                             |
| unpickle_pure_python     | 183 us                                                      | 138 us: 1.33x faster                                              |
| crypto_pyaes             | 62.5 ms                                                     | 47.4 ms: 1.32x faster                                             |
| html5lib                 | 51.0 ms                                                     | 39.1 ms: 1.31x faster                                             |
| scimark_sor              | 106 ms                                                      | 81.9 ms: 1.30x faster                                             |
| genshi_text              | 19.8 ms                                                     | 15.3 ms: 1.29x faster                                             |
| scimark_monte_carlo      | 57.3 ms                                                     | 44.4 ms: 1.29x faster                                             |
| django_template          | 28.9 ms                                                     | 22.7 ms: 1.27x faster                                             |
| mypy2                    | 555 ms                                                      | 439 ms: 1.26x faster                                              |
| regex_compile            | 106 ms                                                      | 83.9 ms: 1.26x faster                                             |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.68 sec: 1.26x faster                                            |
| genshi_xml               | 41.0 ms                                                     | 33.2 ms: 1.24x faster                                             |
| pycparser                | 930 ms                                                      | 754 ms: 1.23x faster                                              |
| mdp                      | 1.78 sec                                                    | 1.44 sec: 1.23x faster                                            |
| float                    | 61.7 ms                                                     | 50.1 ms: 1.23x faster                                             |
| dulwich_log              | 50.5 ms                                                     | 41.0 ms: 1.23x faster                                             |
| coroutines               | 16.0 ms                                                     | 13.0 ms: 1.23x faster                                             |
| sympy_sum                | 107 ms                                                      | 87.6 ms: 1.22x faster                                             |
| sympy_integrate          | 15.3 ms                                                     | 12.7 ms: 1.20x faster                                             |
| spectral_norm            | 77.3 ms                                                     | 64.3 ms: 1.20x faster                                             |
| tomli_loads              | 1.67 sec                                                    | 1.42 sec: 1.18x faster                                            |
| bench_thread_pool        | 958 us                                                      | 813 us: 1.18x faster                                              |
| tornado_http             | 108 ms                                                      | 92.0 ms: 1.18x faster                                             |
| sqlglot_optimize         | 39.8 ms                                                     | 33.9 ms: 1.17x faster                                             |
| pprint_pformat           | 1.22 sec                                                    | 1.05 sec: 1.16x faster                                            |
| asyncio_tcp              | 732 ms                                                      | 631 ms: 1.16x faster                                              |
| xml_etree_process        | 44.5 ms                                                     | 38.4 ms: 1.16x faster                                             |
| pprint_safe_repr         | 592 ms                                                      | 512 ms: 1.16x faster                                              |
| deepcopy_memo            | 28.8 us                                                     | 24.9 us: 1.16x faster                                             |
| sympy_str                | 194 ms                                                      | 169 ms: 1.15x faster                                              |
| docutils                 | 1.92 sec                                                    | 1.68 sec: 1.14x faster                                            |
| sqlglot_normalize        | 205 ms                                                      | 180 ms: 1.14x faster                                              |
| chameleon                | 5.79 ms                                                     | 5.10 ms: 1.13x faster                                             |
| nqueens                  | 66.6 ms                                                     | 59.8 ms: 1.11x faster                                             |
| regex_dna                | 136 ms                                                      | 123 ms: 1.11x faster                                              |
| sympy_expand             | 314 ms                                                      | 289 ms: 1.09x faster                                              |
| 2to3                     | 246 ms                                                      | 226 ms: 1.09x faster                                              |
| deepcopy                 | 255 us                                                      | 237 us: 1.08x faster                                              |
| logging_format           | 6.76 us                                                     | 6.29 us: 1.07x faster                                             |
| logging_simple           | 6.22 us                                                     | 5.85 us: 1.06x faster                                             |
| xml_etree_parse          | 96.8 ms                                                     | 91.5 ms: 1.06x faster                                             |
| deepcopy_reduce          | 2.20 us                                                     | 2.11 us: 1.04x faster                                             |
| meteor_contest           | 75.9 ms                                                     | 73.3 ms: 1.04x faster                                             |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.0 ms: 1.03x faster                                             |
| regex_effbot             | 1.66 ms                                                     | 1.62 ms: 1.03x faster                                             |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.68 ms: 1.02x faster                                             |
| json                     | 3.14 ms                                                     | 3.10 ms: 1.01x faster                                             |
| json_loads               | 14.0 us                                                     | 14.2 us: 1.01x slower                                             |
| pidigits                 | 149 ms                                                      | 151 ms: 1.01x slower                                              |
| scimark_fft              | 187 ms                                                      | 192 ms: 1.02x slower                                              |
| async_generators         | 222 ms                                                      | 231 ms: 1.04x slower                                              |
| fannkuch                 | 256 ms                                                      | 271 ms: 1.06x slower                                              |
| nbody                    | 71.3 ms                                                     | 76.8 ms: 1.08x slower                                             |
| pathlib                  | 75.7 ms                                                     | 82.3 ms: 1.09x slower                                             |
| python_startup           | 20.6 ms                                                     | 22.5 ms: 1.09x slower                                             |
| gc_traversal             | 1.41 ms                                                     | 1.58 ms: 1.12x slower                                             |
| bench_mp_pool            | 62.0 ms                                                     | 71.1 ms: 1.15x slower                                             |
| create_gc_cycles         | 800 us                                                      | 917 us: 1.15x slower                                              |
| coverage                 | 39.0 ms                                                     | 45.7 ms: 1.17x slower                                             |
| python_startup_no_site   | 15.5 ms                                                     | 18.4 ms: 1.19x slower                                             |
| telco                    | 3.94 ms                                                     | 4.79 ms: 1.22x slower                                             |
| thrift                   | 617 us                                                      | 8.84 ms: 14.32x slower                                            |
| Geometric mean           | (ref)                                                       | 1.18x faster                                                      |

Benchmark hidden because not significant (2): xml_etree_generate, regex_v8
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240731-3.13.0rc1-e4a3e78/bm-20240731-pythonperf1-amd64-python-v3.13.0rc1-3.13.0rc1-e4a3e78.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.184x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: unknown