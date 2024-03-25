# Results vs. 3.10.4

- fork: python
- ref: d610d821fd210dce63a1
- machine: windows-amd64
- commit hash: d610d82
- commit date: 2024-03-23
- overall geometric mean: 1.22x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 210 ms: 1.17x faster                                                        |
| chameleon      | 5.79 ms                                                     | 4.74 ms: 1.22x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.62 sec: 1.19x faster                                                      |
| html5lib       | 51.0 ms                                                     | 36.3 ms: 1.41x faster                                                       |
| tornado_http   | 108 ms                                                      | 83.2 ms: 1.30x faster                                                       |
| Geometric mean | (ref)                                                       | 1.26x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 221 ms: 1.97x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 276 ms: 1.91x faster                                                        |
| async_tree_io           | 1.11 sec                                                    | 583 ms: 1.90x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 381 ms: 1.68x faster                                                        |
| Geometric mean          | (ref)                                                       | 1.86x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 52.7 ms: 1.17x faster                                                       |
| nbody          | 71.3 ms                                                     | 68.6 ms: 1.04x faster                                                       |
| pidigits       | 149 ms                                                      | 147 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 76.8 ms: 1.38x faster                                                       |
| regex_dna      | 136 ms                                                      | 116 ms: 1.17x faster                                                        |
| regex_v8       | 15.4 ms                                                     | 14.3 ms: 1.08x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.61 ms: 1.63x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 179 us: 1.51x faster                                                        |
| unpickle_pure_python | 183 us                                                      | 127 us: 1.44x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 36.8 ms: 1.21x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.42 sec: 1.17x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.39 us: 1.08x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 91.9 ms: 1.05x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 53.3 ms: 1.04x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.3 ms: 1.03x faster                                                       |
| json_loads           | 14.0 us                                                     | 13.8 us: 1.01x faster                                                       |
| pickle_list          | 2.75 us                                                     | 2.84 us: 1.03x slower                                                       |
| pickle               | 6.85 us                                                     | 7.44 us: 1.09x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 19.0 us: 1.11x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.12x faster                                                                |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 20.2 ms: 1.02x faster                                                       |
| python_startup_no_site | 15.5 ms                                                     | 18.7 ms: 1.20x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.09x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.23 ms: 1.45x faster                                                       |
| django_template | 28.9 ms                                                     | 21.7 ms: 1.33x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 15.8 ms: 1.26x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 35.0 ms: 1.17x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.30x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 70.7 us: 4.75x faster                                                       |
| deltablue                | 4.19 ms                                                     | 1.98 ms: 2.11x faster                                                       |
| async_tree_none          | 435 ms                                                      | 221 ms: 1.97x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 276 ms: 1.91x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 583 ms: 1.90x faster                                                        |
| logging_silent           | 94.6 ns                                                     | 55.4 ns: 1.71x faster                                                       |
| richards_super           | 52.2 ms                                                     | 30.7 ms: 1.70x faster                                                       |
| pylint                   | 350 ms                                                      | 209 ms: 1.68x faster                                                        |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 381 ms: 1.68x faster                                                        |
| raytrace                 | 273 ms                                                      | 163 ms: 1.67x faster                                                        |
| go                       | 139 ms                                                      | 84.5 ms: 1.64x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 5.61 ms: 1.63x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 761 us: 1.60x faster                                                        |
| chaos                    | 61.7 ms                                                     | 39.1 ms: 1.58x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 54.4 ms: 1.58x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 465 ms: 1.57x faster                                                        |
| richards                 | 42.4 ms                                                     | 27.3 ms: 1.55x faster                                                       |
| comprehensions           | 16.5 us                                                     | 10.7 us: 1.54x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 3.78 ms: 1.52x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 972 us: 1.52x faster                                                        |
| pickle_pure_python       | 270 us                                                      | 179 us: 1.51x faster                                                        |
| scimark_monte_carlo      | 57.3 ms                                                     | 38.9 ms: 1.47x faster                                                       |
| mako                     | 9.03 ms                                                     | 6.23 ms: 1.45x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 43.2 ms: 1.45x faster                                                       |
| generators               | 32.4 ms                                                     | 22.4 ms: 1.45x faster                                                       |
| pyflate                  | 409 ms                                                      | 284 ms: 1.44x faster                                                        |
| unpickle_pure_python     | 183 us                                                      | 127 us: 1.44x faster                                                        |
| html5lib                 | 51.0 ms                                                     | 36.3 ms: 1.41x faster                                                       |
| pycparser                | 930 ms                                                      | 663 ms: 1.40x faster                                                        |
| regex_compile            | 106 ms                                                      | 76.8 ms: 1.38x faster                                                       |
| scimark_sor              | 106 ms                                                      | 77.7 ms: 1.37x faster                                                       |
| django_template          | 28.9 ms                                                     | 21.7 ms: 1.33x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 21.9 us: 1.31x faster                                                       |
| tornado_http             | 108 ms                                                      | 83.2 ms: 1.30x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.38 sec: 1.29x faster                                                      |
| sympy_sum                | 107 ms                                                      | 83.5 ms: 1.28x faster                                                       |
| mypy2                    | 555 ms                                                      | 436 ms: 1.27x faster                                                        |
| spectral_norm            | 77.3 ms                                                     | 61.2 ms: 1.26x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 15.8 ms: 1.26x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 40.5 ms: 1.25x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 12.3 ms: 1.25x faster                                                       |
| sympy_str                | 194 ms                                                      | 159 ms: 1.23x faster                                                        |
| chameleon                | 5.79 ms                                                     | 4.74 ms: 1.22x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.00 sec: 1.22x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 489 ms: 1.21x faster                                                        |
| xml_etree_process        | 44.5 ms                                                     | 36.8 ms: 1.21x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.3 ms: 1.20x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.62 sec: 1.19x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 807 us: 1.19x faster                                                        |
| sqlite_synth             | 1.91 us                                                     | 1.61 us: 1.19x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 33.8 ms: 1.18x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.42 sec: 1.17x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 35.0 ms: 1.17x faster                                                       |
| regex_dna                | 136 ms                                                      | 116 ms: 1.17x faster                                                        |
| 2to3                     | 246 ms                                                      | 210 ms: 1.17x faster                                                        |
| float                    | 61.7 ms                                                     | 52.7 ms: 1.17x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.81 sec: 1.17x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 57.6 ms: 1.16x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 179 ms: 1.15x faster                                                        |
| sympy_expand             | 314 ms                                                      | 274 ms: 1.15x faster                                                        |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.40 ms: 1.13x faster                                                       |
| aiohttp                  | 995 us                                                      | 881 us: 1.13x faster                                                        |
| deepcopy                 | 255 us                                                      | 227 us: 1.12x faster                                                        |
| create_gc_cycles         | 800 us                                                      | 717 us: 1.12x faster                                                        |
| scimark_fft              | 187 ms                                                      | 171 ms: 1.09x faster                                                        |
| unpickle                 | 9.09 us                                                     | 8.39 us: 1.08x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 14.3 ms: 1.08x faster                                                       |
| json                     | 3.14 ms                                                     | 2.92 ms: 1.07x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 2.06 us: 1.07x faster                                                       |
| unpack_sequence          | 39.6 ns                                                     | 37.3 ns: 1.06x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 91.9 ms: 1.05x faster                                                       |
| fannkuch                 | 256 ms                                                      | 244 ms: 1.05x faster                                                        |
| xml_etree_generate       | 55.5 ms                                                     | 53.3 ms: 1.04x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 72.9 ms: 1.04x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.49 us: 1.04x faster                                                       |
| nbody                    | 71.3 ms                                                     | 68.6 ms: 1.04x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.3 ms: 1.03x faster                                                       |
| python_startup           | 20.6 ms                                                     | 20.2 ms: 1.02x faster                                                       |
| pidigits                 | 149 ms                                                      | 147 ms: 1.02x faster                                                        |
| logging_simple           | 6.22 us                                                     | 6.14 us: 1.01x faster                                                       |
| json_loads               | 14.0 us                                                     | 13.8 us: 1.01x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 77.2 ms: 1.02x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 63.6 ms: 1.02x slower                                                       |
| async_generators         | 222 ms                                                      | 227 ms: 1.03x slower                                                        |
| pickle_list              | 2.75 us                                                     | 2.84 us: 1.03x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.46 ms: 1.04x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.44 us: 1.09x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 19.0 us: 1.11x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 18.7 ms: 1.20x slower                                                       |
| coverage                 | 39.0 ms                                                     | 46.9 ms: 1.20x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.75 ms: 1.21x slower                                                       |
| thrift                   | 617 us                                                      | 8.04 ms: 13.02x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.22x faster                                                                |

Benchmark hidden because not significant (1): unpickle_list
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: dask, flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240323-3.13.0a5+-d610d82/bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.17x


# Memory

- memory change: unknown