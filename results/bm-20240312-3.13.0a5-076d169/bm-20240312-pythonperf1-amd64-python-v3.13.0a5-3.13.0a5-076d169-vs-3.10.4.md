# Results vs. 3.10.4

- fork: python
- ref: v3.13.0a5
- machine: windows-amd64
- commit hash: 076d169
- commit date: 2024-03-12
- overall geometric mean: 1.21x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 216 ms: 1.14x faster                                            |
| chameleon      | 5.79 ms                                                     | 4.84 ms: 1.20x faster                                           |
| docutils       | 1.92 sec                                                    | 1.54 sec: 1.25x faster                                          |
| html5lib       | 51.0 ms                                                     | 36.5 ms: 1.40x faster                                           |
| tornado_http   | 108 ms                                                      | 84.8 ms: 1.28x faster                                           |
| Geometric mean | (ref)                                                       | 1.25x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 270 ms: 1.61x faster                                            |
| async_tree_memoization  | 526 ms                                                      | 340 ms: 1.55x faster                                            |
| async_tree_io           | 1.11 sec                                                    | 738 ms: 1.50x faster                                            |
| async_tree_cpu_io_mixed | 638 ms                                                      | 454 ms: 1.40x faster                                            |
| Geometric mean          | (ref)                                                       | 1.51x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 50.8 ms: 1.22x faster                                           |
| nbody          | 71.3 ms                                                     | 68.2 ms: 1.04x faster                                           |
| pidigits       | 149 ms                                                      | 147 ms: 1.01x faster                                            |
| Geometric mean | (ref)                                                       | 1.09x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 78.2 ms: 1.36x faster                                           |
| regex_dna      | 136 ms                                                      | 118 ms: 1.15x faster                                            |
| regex_effbot   | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                           |
| Geometric mean | (ref)                                                       | 1.13x faster                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.63 ms: 1.63x faster                                           |
| pickle_pure_python   | 270 us                                                      | 180 us: 1.50x faster                                            |
| unpickle_pure_python | 183 us                                                      | 125 us: 1.47x faster                                            |
| xml_etree_process    | 44.5 ms                                                     | 36.7 ms: 1.21x faster                                           |
| tomli_loads          | 1.67 sec                                                    | 1.43 sec: 1.17x faster                                          |
| unpickle             | 9.09 us                                                     | 8.29 us: 1.10x faster                                           |
| xml_etree_parse      | 96.8 ms                                                     | 93.6 ms: 1.03x faster                                           |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.9 ms: 1.03x faster                                           |
| xml_etree_generate   | 55.5 ms                                                     | 53.8 ms: 1.03x faster                                           |
| unpickle_list        | 2.71 us                                                     | 2.68 us: 1.01x faster                                           |
| json_loads           | 14.0 us                                                     | 13.9 us: 1.01x faster                                           |
| pickle               | 6.85 us                                                     | 7.17 us: 1.05x slower                                           |
| pickle_list          | 2.75 us                                                     | 2.90 us: 1.05x slower                                           |
| pickle_dict          | 17.2 us                                                     | 18.5 us: 1.08x slower                                           |
| Geometric mean       | (ref)                                                       | 1.13x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 20.3 ms: 1.02x faster                                           |
| python_startup_no_site | 15.5 ms                                                     | 18.1 ms: 1.17x slower                                           |
| Geometric mean         | (ref)                                                       | 1.07x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.21 ms: 1.46x faster                                           |
| django_template | 28.9 ms                                                     | 22.1 ms: 1.31x faster                                           |
| genshi_text     | 19.8 ms                                                     | 15.8 ms: 1.25x faster                                           |
| genshi_xml      | 41.0 ms                                                     | 34.6 ms: 1.18x faster                                           |
| Geometric mean  | (ref)                                                       | 1.30x faster                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 75.1 us: 4.47x faster                                           |
| deltablue                | 4.19 ms                                                     | 1.98 ms: 2.12x faster                                           |
| logging_silent           | 94.6 ns                                                     | 53.5 ns: 1.77x faster                                           |
| richards_super           | 52.2 ms                                                     | 30.6 ms: 1.70x faster                                           |
| raytrace                 | 273 ms                                                      | 160 ms: 1.70x faster                                            |
| pylint                   | 350 ms                                                      | 206 ms: 1.70x faster                                            |
| json_dumps               | 9.16 ms                                                     | 5.63 ms: 1.63x faster                                           |
| go                       | 139 ms                                                      | 86.1 ms: 1.61x faster                                           |
| async_tree_none          | 435 ms                                                      | 270 ms: 1.61x faster                                            |
| chaos                    | 61.7 ms                                                     | 38.4 ms: 1.61x faster                                           |
| sqlglot_parse            | 1.22 ms                                                     | 762 us: 1.60x faster                                            |
| generators               | 32.4 ms                                                     | 20.6 ms: 1.58x faster                                           |
| async_tree_memoization   | 526 ms                                                      | 340 ms: 1.55x faster                                            |
| scimark_lu               | 85.8 ms                                                     | 55.5 ms: 1.55x faster                                           |
| richards                 | 42.4 ms                                                     | 27.5 ms: 1.55x faster                                           |
| asyncio_tcp              | 732 ms                                                      | 478 ms: 1.53x faster                                            |
| sqlglot_transpile        | 1.48 ms                                                     | 980 us: 1.51x faster                                            |
| async_tree_io            | 1.11 sec                                                    | 738 ms: 1.50x faster                                            |
| pickle_pure_python       | 270 us                                                      | 180 us: 1.50x faster                                            |
| comprehensions           | 16.5 us                                                     | 11.0 us: 1.49x faster                                           |
| unpickle_pure_python     | 183 us                                                      | 125 us: 1.47x faster                                            |
| hexiom                   | 5.74 ms                                                     | 3.91 ms: 1.47x faster                                           |
| crypto_pyaes             | 62.5 ms                                                     | 42.6 ms: 1.47x faster                                           |
| scimark_monte_carlo      | 57.3 ms                                                     | 39.2 ms: 1.46x faster                                           |
| mako                     | 9.03 ms                                                     | 6.21 ms: 1.46x faster                                           |
| pyflate                  | 409 ms                                                      | 281 ms: 1.45x faster                                            |
| scimark_sor              | 106 ms                                                      | 75.4 ms: 1.41x faster                                           |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 454 ms: 1.40x faster                                            |
| html5lib                 | 51.0 ms                                                     | 36.5 ms: 1.40x faster                                           |
| regex_compile            | 106 ms                                                      | 78.2 ms: 1.36x faster                                           |
| mypy2                    | 555 ms                                                      | 413 ms: 1.34x faster                                            |
| pycparser                | 930 ms                                                      | 693 ms: 1.34x faster                                            |
| django_template          | 28.9 ms                                                     | 22.1 ms: 1.31x faster                                           |
| mdp                      | 1.78 sec                                                    | 1.37 sec: 1.30x faster                                          |
| spectral_norm            | 77.3 ms                                                     | 59.7 ms: 1.29x faster                                           |
| deepcopy_memo            | 28.8 us                                                     | 22.3 us: 1.29x faster                                           |
| sympy_sum                | 107 ms                                                      | 82.9 ms: 1.29x faster                                           |
| tornado_http             | 108 ms                                                      | 84.8 ms: 1.28x faster                                           |
| genshi_text              | 19.8 ms                                                     | 15.8 ms: 1.25x faster                                           |
| dulwich_log              | 50.5 ms                                                     | 40.4 ms: 1.25x faster                                           |
| docutils                 | 1.92 sec                                                    | 1.54 sec: 1.25x faster                                          |
| sympy_integrate          | 15.3 ms                                                     | 12.3 ms: 1.24x faster                                           |
| sympy_str                | 194 ms                                                      | 158 ms: 1.23x faster                                            |
| pprint_pformat           | 1.22 sec                                                    | 992 ms: 1.23x faster                                            |
| sqlglot_optimize         | 39.8 ms                                                     | 32.6 ms: 1.22x faster                                           |
| coroutines               | 16.0 ms                                                     | 13.2 ms: 1.22x faster                                           |
| float                    | 61.7 ms                                                     | 50.8 ms: 1.22x faster                                           |
| pprint_safe_repr         | 592 ms                                                      | 487 ms: 1.21x faster                                            |
| xml_etree_process        | 44.5 ms                                                     | 36.7 ms: 1.21x faster                                           |
| sqlite_synth             | 1.91 us                                                     | 1.59 us: 1.20x faster                                           |
| chameleon                | 5.79 ms                                                     | 4.84 ms: 1.20x faster                                           |
| sqlglot_normalize        | 205 ms                                                      | 172 ms: 1.19x faster                                            |
| genshi_xml               | 41.0 ms                                                     | 34.6 ms: 1.18x faster                                           |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.80 sec: 1.17x faster                                          |
| tomli_loads              | 1.67 sec                                                    | 1.43 sec: 1.17x faster                                          |
| sympy_expand             | 314 ms                                                      | 270 ms: 1.17x faster                                            |
| deepcopy                 | 255 us                                                      | 220 us: 1.16x faster                                            |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.35 ms: 1.16x faster                                           |
| bench_thread_pool        | 958 us                                                      | 831 us: 1.15x faster                                            |
| regex_dna                | 136 ms                                                      | 118 ms: 1.15x faster                                            |
| 2to3                     | 246 ms                                                      | 216 ms: 1.14x faster                                            |
| deepcopy_reduce          | 2.20 us                                                     | 1.95 us: 1.13x faster                                           |
| nqueens                  | 66.6 ms                                                     | 59.9 ms: 1.11x faster                                           |
| aiohttp                  | 995 us                                                      | 896 us: 1.11x faster                                            |
| unpickle                 | 9.09 us                                                     | 8.29 us: 1.10x faster                                           |
| scimark_fft              | 187 ms                                                      | 172 ms: 1.09x faster                                            |
| create_gc_cycles         | 800 us                                                      | 745 us: 1.07x faster                                            |
| regex_effbot             | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                           |
| logging_format           | 6.76 us                                                     | 6.41 us: 1.05x faster                                           |
| fannkuch                 | 256 ms                                                      | 243 ms: 1.05x faster                                            |
| nbody                    | 71.3 ms                                                     | 68.2 ms: 1.04x faster                                           |
| meteor_contest           | 75.9 ms                                                     | 72.8 ms: 1.04x faster                                           |
| logging_simple           | 6.22 us                                                     | 5.97 us: 1.04x faster                                           |
| xml_etree_parse          | 96.8 ms                                                     | 93.6 ms: 1.03x faster                                           |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.9 ms: 1.03x faster                                           |
| xml_etree_generate       | 55.5 ms                                                     | 53.8 ms: 1.03x faster                                           |
| python_startup           | 20.6 ms                                                     | 20.3 ms: 1.02x faster                                           |
| unpickle_list            | 2.71 us                                                     | 2.68 us: 1.01x faster                                           |
| pidigits                 | 149 ms                                                      | 147 ms: 1.01x faster                                            |
| json_loads               | 14.0 us                                                     | 13.9 us: 1.01x faster                                           |
| async_generators         | 222 ms                                                      | 224 ms: 1.01x slower                                            |
| pickle                   | 6.85 us                                                     | 7.17 us: 1.05x slower                                           |
| pickle_list              | 2.75 us                                                     | 2.90 us: 1.05x slower                                           |
| pathlib                  | 75.7 ms                                                     | 80.3 ms: 1.06x slower                                           |
| gc_traversal             | 1.41 ms                                                     | 1.50 ms: 1.06x slower                                           |
| bench_mp_pool            | 62.0 ms                                                     | 66.6 ms: 1.07x slower                                           |
| pickle_dict              | 17.2 us                                                     | 18.5 us: 1.08x slower                                           |
| python_startup_no_site   | 15.5 ms                                                     | 18.1 ms: 1.17x slower                                           |
| telco                    | 3.94 ms                                                     | 4.75 ms: 1.21x slower                                           |
| coverage                 | 39.0 ms                                                     | 47.1 ms: 1.21x slower                                           |
| thrift                   | 617 us                                                      | 8.19 ms: 13.27x slower                                          |
| Geometric mean           | (ref)                                                       | 1.21x faster                                                    |

Benchmark hidden because not significant (3): flaskblogging, regex_v8, json
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240312-3.13.0a5-076d169/bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: unknown