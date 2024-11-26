# Results vs. 3.10.4

- fork: mdboom
- ref: pysequence_tuple
- machine: windows-amd64
- commit hash: 3b5fdc8
- commit date: 2024-09-11
- overall geometric mean: 1.185x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 222 ms: 1.11x faster                                                   |
| docutils       | 1.92 sec                                                    | 1.70 sec: 1.13x faster                                                 |
| html5lib       | 51.0 ms                                                     | 40.3 ms: 1.27x faster                                                  |
| tornado_http   | 108 ms                                                      | 84.1 ms: 1.29x faster                                                  |
| Geometric mean | (ref)                                                       | 1.20x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|-------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 205 ms: 2.12x faster                                                   |
| async_tree_memoization  | 526 ms                                                      | 259 ms: 2.03x faster                                                   |
| async_tree_io           | 1.11 sec                                                    | 566 ms: 1.96x faster                                                   |
| async_tree_cpu_io_mixed | 638 ms                                                      | 390 ms: 1.64x faster                                                   |
| Geometric mean          | (ref)                                                       | 1.93x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 56.6 ms: 1.09x faster                                                  |
| pidigits       | 149 ms                                                      | 151 ms: 1.01x slower                                                   |
| nbody          | 71.3 ms                                                     | 81.8 ms: 1.15x slower                                                  |
| Geometric mean | (ref)                                                       | 1.02x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 91.5 ms: 1.16x faster                                                  |
| regex_dna      | 136 ms                                                      | 121 ms: 1.12x faster                                                   |
| regex_effbot   | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                                  |
| regex_v8       | 15.4 ms                                                     | 15.1 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                       | 1.09x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.23 ms: 1.47x faster                                                  |
| pickle_pure_python   | 270 us                                                      | 212 us: 1.27x faster                                                   |
| unpickle_pure_python | 183 us                                                      | 153 us: 1.20x faster                                                   |
| xml_etree_process    | 44.5 ms                                                     | 40.8 ms: 1.09x faster                                                  |
| tomli_loads          | 1.67 sec                                                    | 1.59 sec: 1.05x faster                                                 |
| xml_etree_parse      | 96.8 ms                                                     | 93.8 ms: 1.03x faster                                                  |
| unpickle             | 9.09 us                                                     | 9.28 us: 1.02x slower                                                  |
| json_loads           | 14.0 us                                                     | 14.6 us: 1.04x slower                                                  |
| pickle               | 6.85 us                                                     | 7.17 us: 1.05x slower                                                  |
| xml_etree_generate   | 55.5 ms                                                     | 58.6 ms: 1.06x slower                                                  |
| pickle_list          | 2.75 us                                                     | 2.99 us: 1.09x slower                                                  |
| pickle_dict          | 17.2 us                                                     | 18.7 us: 1.09x slower                                                  |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                           |

Benchmark hidden because not significant (2): xml_etree_iterparse, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 21.4 ms: 1.04x slower                                                  |
| python_startup_no_site | 15.5 ms                                                     | 17.5 ms: 1.13x slower                                                  |
| Geometric mean         | (ref)                                                       | 1.08x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.89 ms: 1.31x faster                                                  |
| django_template | 28.9 ms                                                     | 24.9 ms: 1.16x faster                                                  |
| genshi_text     | 19.8 ms                                                     | 17.3 ms: 1.15x faster                                                  |
| genshi_xml      | 41.0 ms                                                     | 37.4 ms: 1.10x faster                                                  |
| Geometric mean  | (ref)                                                       | 1.18x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|--------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 111 us: 3.04x faster                                                   |
| async_tree_none          | 435 ms                                                      | 205 ms: 2.12x faster                                                   |
| async_tree_memoization   | 526 ms                                                      | 259 ms: 2.03x faster                                                   |
| async_tree_io            | 1.11 sec                                                    | 566 ms: 1.96x faster                                                   |
| deltablue                | 4.19 ms                                                     | 2.26 ms: 1.85x faster                                                  |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 390 ms: 1.64x faster                                                   |
| go                       | 139 ms                                                      | 87.3 ms: 1.59x faster                                                  |
| pylint                   | 350 ms                                                      | 226 ms: 1.55x faster                                                   |
| asyncio_tcp              | 732 ms                                                      | 472 ms: 1.55x faster                                                   |
| generators               | 32.4 ms                                                     | 21.0 ms: 1.54x faster                                                  |
| logging_silent           | 94.6 ns                                                     | 62.6 ns: 1.51x faster                                                  |
| json_dumps               | 9.16 ms                                                     | 6.23 ms: 1.47x faster                                                  |
| raytrace                 | 273 ms                                                      | 188 ms: 1.46x faster                                                   |
| richards_super           | 52.2 ms                                                     | 36.4 ms: 1.44x faster                                                  |
| comprehensions           | 16.5 us                                                     | 11.7 us: 1.41x faster                                                  |
| chaos                    | 61.7 ms                                                     | 43.7 ms: 1.41x faster                                                  |
| deepcopy_memo            | 28.8 us                                                     | 20.6 us: 1.40x faster                                                  |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.52 sec: 1.39x faster                                                 |
| deepcopy                 | 255 us                                                      | 188 us: 1.36x faster                                                   |
| sqlglot_parse            | 1.22 ms                                                     | 900 us: 1.35x faster                                                   |
| scimark_lu               | 85.8 ms                                                     | 63.6 ms: 1.35x faster                                                  |
| sqlglot_transpile        | 1.48 ms                                                     | 1.12 ms: 1.32x faster                                                  |
| mako                     | 9.03 ms                                                     | 6.89 ms: 1.31x faster                                                  |
| richards                 | 42.4 ms                                                     | 32.4 ms: 1.31x faster                                                  |
| hexiom                   | 5.74 ms                                                     | 4.39 ms: 1.31x faster                                                  |
| crypto_pyaes             | 62.5 ms                                                     | 48.1 ms: 1.30x faster                                                  |
| tornado_http             | 108 ms                                                      | 84.1 ms: 1.29x faster                                                  |
| pyflate                  | 409 ms                                                      | 319 ms: 1.28x faster                                                   |
| pickle_pure_python       | 270 us                                                      | 212 us: 1.27x faster                                                   |
| html5lib                 | 51.0 ms                                                     | 40.3 ms: 1.27x faster                                                  |
| unpickle_pure_python     | 183 us                                                      | 153 us: 1.20x faster                                                   |
| scimark_sor              | 106 ms                                                      | 88.8 ms: 1.20x faster                                                  |
| bench_thread_pool        | 958 us                                                      | 805 us: 1.19x faster                                                   |
| mdp                      | 1.78 sec                                                    | 1.50 sec: 1.19x faster                                                 |
| dulwich_log              | 50.5 ms                                                     | 42.6 ms: 1.19x faster                                                  |
| sqlite_synth             | 1.91 us                                                     | 1.62 us: 1.18x faster                                                  |
| sympy_sum                | 107 ms                                                      | 91.2 ms: 1.17x faster                                                  |
| pycparser                | 930 ms                                                      | 802 ms: 1.16x faster                                                   |
| django_template          | 28.9 ms                                                     | 24.9 ms: 1.16x faster                                                  |
| regex_compile            | 106 ms                                                      | 91.5 ms: 1.16x faster                                                  |
| sympy_integrate          | 15.3 ms                                                     | 13.2 ms: 1.15x faster                                                  |
| deepcopy_reduce          | 2.20 us                                                     | 1.92 us: 1.15x faster                                                  |
| scimark_monte_carlo      | 57.3 ms                                                     | 49.9 ms: 1.15x faster                                                  |
| genshi_text              | 19.8 ms                                                     | 17.3 ms: 1.15x faster                                                  |
| coroutines               | 16.0 ms                                                     | 14.0 ms: 1.14x faster                                                  |
| thrift                   | 617 us                                                      | 544 us: 1.13x faster                                                   |
| docutils                 | 1.92 sec                                                    | 1.70 sec: 1.13x faster                                                 |
| regex_dna                | 136 ms                                                      | 121 ms: 1.12x faster                                                   |
| spectral_norm            | 77.3 ms                                                     | 69.0 ms: 1.12x faster                                                  |
| 2to3                     | 246 ms                                                      | 222 ms: 1.11x faster                                                   |
| pprint_pformat           | 1.22 sec                                                    | 1.11 sec: 1.10x faster                                                 |
| genshi_xml               | 41.0 ms                                                     | 37.4 ms: 1.10x faster                                                  |
| sqlglot_optimize         | 39.8 ms                                                     | 36.5 ms: 1.09x faster                                                  |
| sympy_str                | 194 ms                                                      | 178 ms: 1.09x faster                                                   |
| float                    | 61.7 ms                                                     | 56.6 ms: 1.09x faster                                                  |
| xml_etree_process        | 44.5 ms                                                     | 40.8 ms: 1.09x faster                                                  |
| pprint_safe_repr         | 592 ms                                                      | 546 ms: 1.08x faster                                                   |
| sqlglot_normalize        | 205 ms                                                      | 193 ms: 1.07x faster                                                   |
| tomli_loads              | 1.67 sec                                                    | 1.59 sec: 1.05x faster                                                 |
| nqueens                  | 66.6 ms                                                     | 63.7 ms: 1.05x faster                                                  |
| regex_effbot             | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                                  |
| xml_etree_parse          | 96.8 ms                                                     | 93.8 ms: 1.03x faster                                                  |
| pathlib                  | 75.7 ms                                                     | 73.5 ms: 1.03x faster                                                  |
| regex_v8                 | 15.4 ms                                                     | 15.1 ms: 1.03x faster                                                  |
| sympy_expand             | 314 ms                                                      | 307 ms: 1.02x faster                                                   |
| pidigits                 | 149 ms                                                      | 151 ms: 1.01x slower                                                   |
| logging_format           | 6.76 us                                                     | 6.88 us: 1.02x slower                                                  |
| unpickle                 | 9.09 us                                                     | 9.28 us: 1.02x slower                                                  |
| meteor_contest           | 75.9 ms                                                     | 77.9 ms: 1.03x slower                                                  |
| logging_simple           | 6.22 us                                                     | 6.39 us: 1.03x slower                                                  |
| python_startup           | 20.6 ms                                                     | 21.4 ms: 1.04x slower                                                  |
| json_loads               | 14.0 us                                                     | 14.6 us: 1.04x slower                                                  |
| unpack_sequence          | 39.6 ns                                                     | 41.3 ns: 1.04x slower                                                  |
| pickle                   | 6.85 us                                                     | 7.17 us: 1.05x slower                                                  |
| xml_etree_generate       | 55.5 ms                                                     | 58.6 ms: 1.06x slower                                                  |
| bench_mp_pool            | 62.0 ms                                                     | 66.6 ms: 1.07x slower                                                  |
| async_generators         | 222 ms                                                      | 239 ms: 1.08x slower                                                   |
| gc_traversal             | 1.41 ms                                                     | 1.52 ms: 1.08x slower                                                  |
| scimark_fft              | 187 ms                                                      | 203 ms: 1.08x slower                                                   |
| pickle_list              | 2.75 us                                                     | 2.99 us: 1.09x slower                                                  |
| pickle_dict              | 17.2 us                                                     | 18.7 us: 1.09x slower                                                  |
| create_gc_cycles         | 800 us                                                      | 878 us: 1.10x slower                                                   |
| python_startup_no_site   | 15.5 ms                                                     | 17.5 ms: 1.13x slower                                                  |
| fannkuch                 | 256 ms                                                      | 292 ms: 1.14x slower                                                   |
| nbody                    | 71.3 ms                                                     | 81.8 ms: 1.15x slower                                                  |
| coverage                 | 39.0 ms                                                     | 46.9 ms: 1.20x slower                                                  |
| telco                    | 3.94 ms                                                     | 5.16 ms: 1.31x slower                                                  |
| Geometric mean           | (ref)                                                       | 1.17x faster                                                           |

Benchmark hidden because not significant (4): scimark_sparse_mat_mult, xml_etree_iterparse, unpickle_list, json
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240911-3.14.0a0-3b5fdc8/bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.185x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown