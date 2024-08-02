# Results vs. 3.10.4

- fork: gvanrossum
- ref: backoff_counter_woes
- machine: windows-amd64
- commit hash: 4c1049b
- commit date: 2024-05-04
- overall geometric mean: 1.23x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-pythonperf1-amd64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 207 ms: 1.19x faster                                                            |
| chameleon      | 5.79 ms                                                     | 4.74 ms: 1.22x faster                                                           |
| docutils       | 1.92 sec                                                    | 1.63 sec: 1.17x faster                                                          |
| html5lib       | 51.0 ms                                                     | 36.4 ms: 1.40x faster                                                           |
| tornado_http   | 108 ms                                                      | 79.8 ms: 1.36x faster                                                           |
| Geometric mean | (ref)                                                       | 1.26x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-pythonperf1-amd64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|-------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 218 ms: 2.00x faster                                                            |
| async_tree_memoization  | 526 ms                                                      | 267 ms: 1.97x faster                                                            |
| async_tree_io           | 1.11 sec                                                    | 588 ms: 1.89x faster                                                            |
| async_tree_cpu_io_mixed | 638 ms                                                      | 384 ms: 1.66x faster                                                            |
| Geometric mean          | (ref)                                                       | 1.87x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-pythonperf1-amd64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 48.7 ms: 1.27x faster                                                           |
| nbody          | 71.3 ms                                                     | 67.0 ms: 1.06x faster                                                           |
| pidigits       | 149 ms                                                      | 147 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-pythonperf1-amd64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 78.1 ms: 1.36x faster                                                           |
| regex_dna      | 136 ms                                                      | 118 ms: 1.15x faster                                                            |
| regex_effbot   | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                                           |
| Geometric mean | (ref)                                                       | 1.13x faster                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-pythonperf1-amd64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.57 ms: 1.64x faster                                                           |
| pickle_pure_python   | 270 us                                                      | 174 us: 1.55x faster                                                            |
| unpickle_pure_python | 183 us                                                      | 124 us: 1.47x faster                                                            |
| xml_etree_process    | 44.5 ms                                                     | 36.2 ms: 1.23x faster                                                           |
| tomli_loads          | 1.67 sec                                                    | 1.37 sec: 1.22x faster                                                          |
| unpickle             | 9.09 us                                                     | 8.17 us: 1.11x faster                                                           |
| xml_etree_parse      | 96.8 ms                                                     | 88.2 ms: 1.10x faster                                                           |
| xml_etree_iterparse  | 65.0 ms                                                     | 60.8 ms: 1.07x faster                                                           |
| xml_etree_generate   | 55.5 ms                                                     | 52.9 ms: 1.05x faster                                                           |
| unpickle_list        | 2.71 us                                                     | 2.74 us: 1.01x slower                                                           |
| pickle               | 6.85 us                                                     | 7.47 us: 1.09x slower                                                           |
| pickle_dict          | 17.2 us                                                     | 18.9 us: 1.10x slower                                                           |
| pickle_list          | 2.75 us                                                     | 3.28 us: 1.19x slower                                                           |
| Geometric mean       | (ref)                                                       | 1.13x faster                                                                    |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-pythonperf1-amd64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 20.0 ms: 1.03x faster                                                           |
| python_startup_no_site | 15.5 ms                                                     | 16.4 ms: 1.06x slower                                                           |
| Geometric mean         | (ref)                                                       | 1.01x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-pythonperf1-amd64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.48 ms: 1.39x faster                                                           |
| django_template | 28.9 ms                                                     | 21.7 ms: 1.33x faster                                                           |
| genshi_text     | 19.8 ms                                                     | 15.0 ms: 1.32x faster                                                           |
| genshi_xml      | 41.0 ms                                                     | 34.0 ms: 1.21x faster                                                           |
| Geometric mean  | (ref)                                                       | 1.31x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-pythonperf1-amd64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|--------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 99.5 us: 3.38x faster                                                           |
| deltablue                | 4.19 ms                                                     | 1.89 ms: 2.22x faster                                                           |
| async_tree_none          | 435 ms                                                      | 218 ms: 2.00x faster                                                            |
| async_tree_memoization   | 526 ms                                                      | 267 ms: 1.97x faster                                                            |
| async_tree_io            | 1.11 sec                                                    | 588 ms: 1.89x faster                                                            |
| logging_silent           | 94.6 ns                                                     | 50.7 ns: 1.87x faster                                                           |
| richards_super           | 52.2 ms                                                     | 29.7 ms: 1.76x faster                                                           |
| raytrace                 | 273 ms                                                      | 156 ms: 1.75x faster                                                            |
| generators               | 32.4 ms                                                     | 19.0 ms: 1.71x faster                                                           |
| pylint                   | 350 ms                                                      | 206 ms: 1.70x faster                                                            |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 384 ms: 1.66x faster                                                            |
| json_dumps               | 9.16 ms                                                     | 5.57 ms: 1.64x faster                                                           |
| go                       | 139 ms                                                      | 84.5 ms: 1.64x faster                                                           |
| chaos                    | 61.7 ms                                                     | 37.9 ms: 1.63x faster                                                           |
| comprehensions           | 16.5 us                                                     | 10.2 us: 1.62x faster                                                           |
| richards                 | 42.4 ms                                                     | 26.4 ms: 1.61x faster                                                           |
| sqlglot_parse            | 1.22 ms                                                     | 757 us: 1.60x faster                                                            |
| scimark_lu               | 85.8 ms                                                     | 54.4 ms: 1.58x faster                                                           |
| asyncio_tcp              | 732 ms                                                      | 471 ms: 1.56x faster                                                            |
| pickle_pure_python       | 270 us                                                      | 174 us: 1.55x faster                                                            |
| sqlglot_transpile        | 1.48 ms                                                     | 963 us: 1.53x faster                                                            |
| hexiom                   | 5.74 ms                                                     | 3.81 ms: 1.51x faster                                                           |
| unpickle_pure_python     | 183 us                                                      | 124 us: 1.47x faster                                                            |
| pyflate                  | 409 ms                                                      | 281 ms: 1.45x faster                                                            |
| scimark_monte_carlo      | 57.3 ms                                                     | 39.7 ms: 1.44x faster                                                           |
| html5lib                 | 51.0 ms                                                     | 36.4 ms: 1.40x faster                                                           |
| scimark_sor              | 106 ms                                                      | 76.0 ms: 1.40x faster                                                           |
| mako                     | 9.03 ms                                                     | 6.48 ms: 1.39x faster                                                           |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.54 sec: 1.37x faster                                                          |
| regex_compile            | 106 ms                                                      | 78.1 ms: 1.36x faster                                                           |
| mdp                      | 1.78 sec                                                    | 1.31 sec: 1.36x faster                                                          |
| tornado_http             | 108 ms                                                      | 79.8 ms: 1.36x faster                                                           |
| crypto_pyaes             | 62.5 ms                                                     | 46.9 ms: 1.33x faster                                                           |
| django_template          | 28.9 ms                                                     | 21.7 ms: 1.33x faster                                                           |
| mypy2                    | 555 ms                                                      | 420 ms: 1.32x faster                                                            |
| genshi_text              | 19.8 ms                                                     | 15.0 ms: 1.32x faster                                                           |
| deepcopy_memo            | 28.8 us                                                     | 21.9 us: 1.31x faster                                                           |
| spectral_norm            | 77.3 ms                                                     | 59.3 ms: 1.30x faster                                                           |
| coroutines               | 16.0 ms                                                     | 12.6 ms: 1.27x faster                                                           |
| float                    | 61.7 ms                                                     | 48.7 ms: 1.27x faster                                                           |
| sympy_sum                | 107 ms                                                      | 84.9 ms: 1.26x faster                                                           |
| dulwich_log              | 50.5 ms                                                     | 40.2 ms: 1.25x faster                                                           |
| pprint_pformat           | 1.22 sec                                                    | 975 ms: 1.25x faster                                                            |
| pycparser                | 930 ms                                                      | 749 ms: 1.24x faster                                                            |
| sympy_integrate          | 15.3 ms                                                     | 12.3 ms: 1.24x faster                                                           |
| pprint_safe_repr         | 592 ms                                                      | 478 ms: 1.24x faster                                                            |
| xml_etree_process        | 44.5 ms                                                     | 36.2 ms: 1.23x faster                                                           |
| tomli_loads              | 1.67 sec                                                    | 1.37 sec: 1.22x faster                                                          |
| sqlglot_optimize         | 39.8 ms                                                     | 32.6 ms: 1.22x faster                                                           |
| chameleon                | 5.79 ms                                                     | 4.74 ms: 1.22x faster                                                           |
| sympy_str                | 194 ms                                                      | 161 ms: 1.21x faster                                                            |
| genshi_xml               | 41.0 ms                                                     | 34.0 ms: 1.21x faster                                                           |
| bench_thread_pool        | 958 us                                                      | 801 us: 1.20x faster                                                            |
| sqlglot_normalize        | 205 ms                                                      | 172 ms: 1.19x faster                                                            |
| 2to3                     | 246 ms                                                      | 207 ms: 1.19x faster                                                            |
| deepcopy                 | 255 us                                                      | 217 us: 1.18x faster                                                            |
| sqlite_synth             | 1.91 us                                                     | 1.63 us: 1.18x faster                                                           |
| docutils                 | 1.92 sec                                                    | 1.63 sec: 1.17x faster                                                          |
| nqueens                  | 66.6 ms                                                     | 56.8 ms: 1.17x faster                                                           |
| sympy_expand             | 314 ms                                                      | 273 ms: 1.15x faster                                                            |
| regex_dna                | 136 ms                                                      | 118 ms: 1.15x faster                                                            |
| deepcopy_reduce          | 2.20 us                                                     | 1.97 us: 1.12x faster                                                           |
| unpickle                 | 9.09 us                                                     | 8.17 us: 1.11x faster                                                           |
| aiohttp                  | 995 us                                                      | 896 us: 1.11x faster                                                            |
| xml_etree_parse          | 96.8 ms                                                     | 88.2 ms: 1.10x faster                                                           |
| logging_format           | 6.76 us                                                     | 6.17 us: 1.10x faster                                                           |
| logging_simple           | 6.22 us                                                     | 5.76 us: 1.08x faster                                                           |
| meteor_contest           | 75.9 ms                                                     | 70.9 ms: 1.07x faster                                                           |
| scimark_fft              | 187 ms                                                      | 175 ms: 1.07x faster                                                            |
| xml_etree_iterparse      | 65.0 ms                                                     | 60.8 ms: 1.07x faster                                                           |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.55 ms: 1.07x faster                                                           |
| nbody                    | 71.3 ms                                                     | 67.0 ms: 1.06x faster                                                           |
| xml_etree_generate       | 55.5 ms                                                     | 52.9 ms: 1.05x faster                                                           |
| regex_effbot             | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                                           |
| fannkuch                 | 256 ms                                                      | 245 ms: 1.04x faster                                                            |
| python_startup           | 20.6 ms                                                     | 20.0 ms: 1.03x faster                                                           |
| pidigits                 | 149 ms                                                      | 147 ms: 1.01x faster                                                            |
| unpickle_list            | 2.71 us                                                     | 2.74 us: 1.01x slower                                                           |
| async_generators         | 222 ms                                                      | 228 ms: 1.03x slower                                                            |
| bench_mp_pool            | 62.0 ms                                                     | 64.5 ms: 1.04x slower                                                           |
| pathlib                  | 75.7 ms                                                     | 78.7 ms: 1.04x slower                                                           |
| python_startup_no_site   | 15.5 ms                                                     | 16.4 ms: 1.06x slower                                                           |
| pickle                   | 6.85 us                                                     | 7.47 us: 1.09x slower                                                           |
| gc_traversal             | 1.41 ms                                                     | 1.55 ms: 1.10x slower                                                           |
| pickle_dict              | 17.2 us                                                     | 18.9 us: 1.10x slower                                                           |
| create_gc_cycles         | 800 us                                                      | 898 us: 1.12x slower                                                            |
| coverage                 | 39.0 ms                                                     | 44.6 ms: 1.14x slower                                                           |
| pickle_list              | 2.75 us                                                     | 3.28 us: 1.19x slower                                                           |
| telco                    | 3.94 ms                                                     | 4.82 ms: 1.22x slower                                                           |
| thrift                   | 617 us                                                      | 8.10 ms: 13.13x slower                                                          |
| Geometric mean           | (ref)                                                       | 1.23x faster                                                                    |

Benchmark hidden because not significant (5): regex_v8, dask, json_loads, flaskblogging, json
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240504-3.13.0a6+-4c1049b/bm-20240504-pythonperf1-amd64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: unknown