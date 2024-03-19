# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_mprotect_cost
- machine: windows-amd64
- commit hash: c8d6017
- commit date: 2024-03-18
- overall geometric mean: 1.20x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240318-pythonperf1-amd64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 221 ms: 1.11x faster                                                              |
| chameleon      | 5.79 ms                                                     | 4.70 ms: 1.23x faster                                                             |
| docutils       | 1.92 sec                                                    | 1.58 sec: 1.21x faster                                                            |
| html5lib       | 51.0 ms                                                     | 35.8 ms: 1.43x faster                                                             |
| tornado_http   | 108 ms                                                      | 83.7 ms: 1.29x faster                                                             |
| Geometric mean | (ref)                                                       | 1.25x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240318-pythonperf1-amd64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 265 ms: 1.64x faster                                                              |
| async_tree_memoization  | 526 ms                                                      | 340 ms: 1.55x faster                                                              |
| async_tree_io           | 1.11 sec                                                    | 717 ms: 1.55x faster                                                              |
| async_tree_cpu_io_mixed | 638 ms                                                      | 454 ms: 1.40x faster                                                              |
| Geometric mean          | (ref)                                                       | 1.53x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240318-pythonperf1-amd64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 48.1 ms: 1.28x faster                                                             |
| nbody          | 71.3 ms                                                     | 58.4 ms: 1.22x faster                                                             |
| pidigits       | 149 ms                                                      | 150 ms: 1.01x slower                                                              |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240318-pythonperf1-amd64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 83.0 ms: 1.28x faster                                                             |
| regex_dna      | 136 ms                                                      | 114 ms: 1.19x faster                                                              |
| regex_effbot   | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                                             |
| Geometric mean | (ref)                                                       | 1.13x faster                                                                      |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240318-pythonperf1-amd64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.51 ms: 1.66x faster                                                             |
| pickle_pure_python   | 270 us                                                      | 177 us: 1.52x faster                                                              |
| unpickle_pure_python | 183 us                                                      | 128 us: 1.43x faster                                                              |
| tomli_loads          | 1.67 sec                                                    | 1.19 sec: 1.40x faster                                                            |
| xml_etree_process    | 44.5 ms                                                     | 36.8 ms: 1.21x faster                                                             |
| xml_etree_parse      | 96.8 ms                                                     | 91.7 ms: 1.06x faster                                                             |
| xml_etree_iterparse  | 65.0 ms                                                     | 61.9 ms: 1.05x faster                                                             |
| unpickle             | 9.09 us                                                     | 8.70 us: 1.05x faster                                                             |
| xml_etree_generate   | 55.5 ms                                                     | 54.1 ms: 1.03x faster                                                             |
| json_loads           | 14.0 us                                                     | 13.7 us: 1.02x faster                                                             |
| pickle_list          | 2.75 us                                                     | 2.73 us: 1.01x faster                                                             |
| pickle_dict          | 17.2 us                                                     | 17.6 us: 1.02x slower                                                             |
| pickle               | 6.85 us                                                     | 7.28 us: 1.06x slower                                                             |
| Geometric mean       | (ref)                                                       | 1.15x faster                                                                      |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240318-pythonperf1-amd64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 23.4 ms: 1.14x slower                                                             |
| python_startup_no_site | 15.5 ms                                                     | 21.4 ms: 1.38x slower                                                             |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240318-pythonperf1-amd64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.48 ms: 1.65x faster                                                             |
| django_template | 28.9 ms                                                     | 21.9 ms: 1.32x faster                                                             |
| genshi_text     | 19.8 ms                                                     | 16.1 ms: 1.23x faster                                                             |
| genshi_xml      | 41.0 ms                                                     | 37.1 ms: 1.11x faster                                                             |
| Geometric mean  | (ref)                                                       | 1.31x faster                                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240318-pythonperf1-amd64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 70.3 us: 4.78x faster                                                             |
| deltablue                | 4.19 ms                                                     | 2.04 ms: 2.06x faster                                                             |
| logging_silent           | 94.6 ns                                                     | 55.5 ns: 1.70x faster                                                             |
| richards_super           | 52.2 ms                                                     | 31.2 ms: 1.67x faster                                                             |
| json_dumps               | 9.16 ms                                                     | 5.51 ms: 1.66x faster                                                             |
| pylint                   | 350 ms                                                      | 211 ms: 1.66x faster                                                              |
| mako                     | 9.03 ms                                                     | 5.48 ms: 1.65x faster                                                             |
| async_tree_none          | 435 ms                                                      | 265 ms: 1.64x faster                                                              |
| generators               | 32.4 ms                                                     | 20.2 ms: 1.60x faster                                                             |
| chaos                    | 61.7 ms                                                     | 39.4 ms: 1.57x faster                                                             |
| sqlglot_parse            | 1.22 ms                                                     | 777 us: 1.56x faster                                                              |
| comprehensions           | 16.5 us                                                     | 10.6 us: 1.56x faster                                                             |
| async_tree_memoization   | 526 ms                                                      | 340 ms: 1.55x faster                                                              |
| async_tree_io            | 1.11 sec                                                    | 717 ms: 1.55x faster                                                              |
| raytrace                 | 273 ms                                                      | 178 ms: 1.53x faster                                                              |
| spectral_norm            | 77.3 ms                                                     | 50.7 ms: 1.53x faster                                                             |
| pickle_pure_python       | 270 us                                                      | 177 us: 1.52x faster                                                              |
| richards                 | 42.4 ms                                                     | 27.9 ms: 1.52x faster                                                             |
| asyncio_tcp              | 732 ms                                                      | 484 ms: 1.51x faster                                                              |
| sqlglot_transpile        | 1.48 ms                                                     | 999 us: 1.48x faster                                                              |
| pyflate                  | 409 ms                                                      | 282 ms: 1.45x faster                                                              |
| go                       | 139 ms                                                      | 96.8 ms: 1.43x faster                                                             |
| unpickle_pure_python     | 183 us                                                      | 128 us: 1.43x faster                                                              |
| html5lib                 | 51.0 ms                                                     | 35.8 ms: 1.43x faster                                                             |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 454 ms: 1.40x faster                                                              |
| tomli_loads              | 1.67 sec                                                    | 1.19 sec: 1.40x faster                                                            |
| scimark_monte_carlo      | 57.3 ms                                                     | 41.5 ms: 1.38x faster                                                             |
| crypto_pyaes             | 62.5 ms                                                     | 45.3 ms: 1.38x faster                                                             |
| deepcopy_memo            | 28.8 us                                                     | 21.8 us: 1.32x faster                                                             |
| hexiom                   | 5.74 ms                                                     | 4.36 ms: 1.32x faster                                                             |
| django_template          | 28.9 ms                                                     | 21.9 ms: 1.32x faster                                                             |
| pycparser                | 930 ms                                                      | 707 ms: 1.32x faster                                                              |
| tornado_http             | 108 ms                                                      | 83.7 ms: 1.29x faster                                                             |
| scimark_sor              | 106 ms                                                      | 82.7 ms: 1.28x faster                                                             |
| float                    | 61.7 ms                                                     | 48.1 ms: 1.28x faster                                                             |
| regex_compile            | 106 ms                                                      | 83.0 ms: 1.28x faster                                                             |
| mypy2                    | 555 ms                                                      | 435 ms: 1.28x faster                                                              |
| pprint_pformat           | 1.22 sec                                                    | 969 ms: 1.26x faster                                                              |
| pprint_safe_repr         | 592 ms                                                      | 475 ms: 1.24x faster                                                              |
| sympy_sum                | 107 ms                                                      | 86.3 ms: 1.24x faster                                                             |
| chameleon                | 5.79 ms                                                     | 4.70 ms: 1.23x faster                                                             |
| dulwich_log              | 50.5 ms                                                     | 41.0 ms: 1.23x faster                                                             |
| genshi_text              | 19.8 ms                                                     | 16.1 ms: 1.23x faster                                                             |
| nbody                    | 71.3 ms                                                     | 58.4 ms: 1.22x faster                                                             |
| sqlite_synth             | 1.91 us                                                     | 1.57 us: 1.22x faster                                                             |
| mdp                      | 1.78 sec                                                    | 1.46 sec: 1.22x faster                                                            |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.24 ms: 1.22x faster                                                             |
| coroutines               | 16.0 ms                                                     | 13.1 ms: 1.22x faster                                                             |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.74 sec: 1.22x faster                                                            |
| docutils                 | 1.92 sec                                                    | 1.58 sec: 1.21x faster                                                            |
| xml_etree_process        | 44.5 ms                                                     | 36.8 ms: 1.21x faster                                                             |
| fannkuch                 | 256 ms                                                      | 213 ms: 1.20x faster                                                              |
| regex_dna                | 136 ms                                                      | 114 ms: 1.19x faster                                                              |
| sympy_str                | 194 ms                                                      | 165 ms: 1.18x faster                                                              |
| sympy_integrate          | 15.3 ms                                                     | 13.0 ms: 1.17x faster                                                             |
| bench_thread_pool        | 958 us                                                      | 819 us: 1.17x faster                                                              |
| sqlglot_normalize        | 205 ms                                                      | 176 ms: 1.17x faster                                                              |
| sqlglot_optimize         | 39.8 ms                                                     | 34.5 ms: 1.15x faster                                                             |
| deepcopy                 | 255 us                                                      | 222 us: 1.15x faster                                                              |
| deepcopy_reduce          | 2.20 us                                                     | 1.93 us: 1.14x faster                                                             |
| 2to3                     | 246 ms                                                      | 221 ms: 1.11x faster                                                              |
| aiohttp                  | 995 us                                                      | 898 us: 1.11x faster                                                              |
| genshi_xml               | 41.0 ms                                                     | 37.1 ms: 1.11x faster                                                             |
| sympy_expand             | 314 ms                                                      | 285 ms: 1.10x faster                                                              |
| scimark_fft              | 187 ms                                                      | 170 ms: 1.10x faster                                                              |
| nqueens                  | 66.6 ms                                                     | 60.6 ms: 1.10x faster                                                             |
| scimark_lu               | 85.8 ms                                                     | 78.2 ms: 1.10x faster                                                             |
| logging_format           | 6.76 us                                                     | 6.28 us: 1.08x faster                                                             |
| create_gc_cycles         | 800 us                                                      | 744 us: 1.07x faster                                                              |
| logging_simple           | 6.22 us                                                     | 5.79 us: 1.07x faster                                                             |
| regex_effbot             | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                                             |
| xml_etree_parse          | 96.8 ms                                                     | 91.7 ms: 1.06x faster                                                             |
| xml_etree_iterparse      | 65.0 ms                                                     | 61.9 ms: 1.05x faster                                                             |
| meteor_contest           | 75.9 ms                                                     | 72.6 ms: 1.05x faster                                                             |
| unpickle                 | 9.09 us                                                     | 8.70 us: 1.05x faster                                                             |
| xml_etree_generate       | 55.5 ms                                                     | 54.1 ms: 1.03x faster                                                             |
| json_loads               | 14.0 us                                                     | 13.7 us: 1.02x faster                                                             |
| pickle_list              | 2.75 us                                                     | 2.73 us: 1.01x faster                                                             |
| pidigits                 | 149 ms                                                      | 150 ms: 1.01x slower                                                              |
| pathlib                  | 75.7 ms                                                     | 77.1 ms: 1.02x slower                                                             |
| pickle_dict              | 17.2 us                                                     | 17.6 us: 1.02x slower                                                             |
| pickle                   | 6.85 us                                                     | 7.28 us: 1.06x slower                                                             |
| gc_traversal             | 1.41 ms                                                     | 1.50 ms: 1.07x slower                                                             |
| async_generators         | 222 ms                                                      | 240 ms: 1.08x slower                                                              |
| bench_mp_pool            | 62.0 ms                                                     | 69.3 ms: 1.12x slower                                                             |
| python_startup           | 20.6 ms                                                     | 23.4 ms: 1.14x slower                                                             |
| unpack_sequence          | 39.6 ns                                                     | 46.6 ns: 1.17x slower                                                             |
| telco                    | 3.94 ms                                                     | 4.63 ms: 1.18x slower                                                             |
| coverage                 | 39.0 ms                                                     | 46.1 ms: 1.18x slower                                                             |
| python_startup_no_site   | 15.5 ms                                                     | 21.4 ms: 1.38x slower                                                             |
| thrift                   | 617 us                                                      | 8.94 ms: 14.48x slower                                                            |
| Geometric mean           | (ref)                                                       | 1.20x faster                                                                      |

Benchmark hidden because not significant (3): json, regex_v8, unpickle_list
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: dask, flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240318-3.13.0a5+-c8d6017-JIT/bm-20240318-pythonperf1-amd64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.18x


# Memory

- memory change: unknown