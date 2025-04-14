# Results vs. 3.10.4

- fork: python
- ref: v3.13.0rc3
- machine: windows-amd64
- commit hash: fae84c7
- commit date: 2024-10-01
- overall geometric mean: 1.222x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241001-pythonperf1-amd64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 216 ms: 1.14x faster                                              |
| chameleon      | 5.79 ms                                                     | 4.89 ms: 1.18x faster                                             |
| docutils       | 1.92 sec                                                    | 1.56 sec: 1.23x faster                                            |
| html5lib       | 51.0 ms                                                     | 40.2 ms: 1.27x faster                                             |
| tornado_http   | 108 ms                                                      | 92.2 ms: 1.18x faster                                             |
| Geometric mean | (ref)                                                       | 1.20x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241001-pythonperf1-amd64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|-------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 516 ms: 2.15x faster                                              |
| async_tree_none         | 435 ms                                                      | 220 ms: 1.98x faster                                              |
| async_tree_memoization  | 526 ms                                                      | 270 ms: 1.95x faster                                              |
| async_tree_cpu_io_mixed | 638 ms                                                      | 374 ms: 1.71x faster                                              |
| Geometric mean          | (ref)                                                       | 1.94x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241001-pythonperf1-amd64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 50.3 ms: 1.23x faster                                             |
| pidigits       | 149 ms                                                      | 150 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                       | 1.07x faster                                                      |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241001-pythonperf1-amd64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 83.8 ms: 1.26x faster                                             |
| regex_dna      | 136 ms                                                      | 118 ms: 1.15x faster                                              |
| regex_effbot   | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                             |
| Geometric mean | (ref)                                                       | 1.09x faster                                                      |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241001-pythonperf1-amd64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.78 ms: 1.58x faster                                             |
| pickle_pure_python   | 270 us                                                      | 183 us: 1.47x faster                                              |
| unpickle_pure_python | 183 us                                                      | 130 us: 1.41x faster                                              |
| xml_etree_process    | 44.5 ms                                                     | 36.7 ms: 1.21x faster                                             |
| tomli_loads          | 1.67 sec                                                    | 1.39 sec: 1.20x faster                                            |
| unpickle             | 9.09 us                                                     | 8.49 us: 1.07x faster                                             |
| xml_etree_parse      | 96.8 ms                                                     | 90.9 ms: 1.07x faster                                             |
| xml_etree_iterparse  | 65.0 ms                                                     | 61.1 ms: 1.06x faster                                             |
| xml_etree_generate   | 55.5 ms                                                     | 53.0 ms: 1.05x faster                                             |
| unpickle_list        | 2.71 us                                                     | 2.66 us: 1.02x faster                                             |
| pickle               | 6.85 us                                                     | 7.21 us: 1.05x slower                                             |
| pickle_dict          | 17.2 us                                                     | 18.8 us: 1.09x slower                                             |
| pickle_list          | 2.75 us                                                     | 3.11 us: 1.13x slower                                             |
| Geometric mean       | (ref)                                                       | 1.12x faster                                                      |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241001-pythonperf1-amd64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.4 ms: 1.09x slower                                             |
| python_startup_no_site | 15.5 ms                                                     | 17.9 ms: 1.15x slower                                             |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241001-pythonperf1-amd64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.68 ms: 1.35x faster                                             |
| django_template | 28.9 ms                                                     | 22.1 ms: 1.31x faster                                             |
| genshi_text     | 19.8 ms                                                     | 15.5 ms: 1.28x faster                                             |
| genshi_xml      | 41.0 ms                                                     | 34.3 ms: 1.20x faster                                             |
| Geometric mean  | (ref)                                                       | 1.28x faster                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241001-pythonperf1-amd64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|--------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 102 us: 3.30x faster                                              |
| deltablue                | 4.19 ms                                                     | 1.90 ms: 2.20x faster                                             |
| async_tree_io            | 1.11 sec                                                    | 516 ms: 2.15x faster                                              |
| async_tree_none          | 435 ms                                                      | 220 ms: 1.98x faster                                              |
| async_tree_memoization   | 526 ms                                                      | 270 ms: 1.95x faster                                              |
| logging_silent           | 94.6 ns                                                     | 53.2 ns: 1.78x faster                                             |
| richards_super           | 52.2 ms                                                     | 29.8 ms: 1.75x faster                                             |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 374 ms: 1.71x faster                                              |
| pylint                   | 350 ms                                                      | 207 ms: 1.69x faster                                              |
| raytrace                 | 273 ms                                                      | 165 ms: 1.66x faster                                              |
| go                       | 139 ms                                                      | 85.4 ms: 1.63x faster                                             |
| generators               | 32.4 ms                                                     | 20.1 ms: 1.61x faster                                             |
| richards                 | 42.4 ms                                                     | 26.4 ms: 1.61x faster                                             |
| json_dumps               | 9.16 ms                                                     | 5.78 ms: 1.58x faster                                             |
| comprehensions           | 16.5 us                                                     | 10.5 us: 1.58x faster                                             |
| chaos                    | 61.7 ms                                                     | 39.5 ms: 1.56x faster                                             |
| sqlglot_parse            | 1.22 ms                                                     | 789 us: 1.54x faster                                              |
| sqlglot_transpile        | 1.48 ms                                                     | 980 us: 1.51x faster                                              |
| scimark_lu               | 85.8 ms                                                     | 57.2 ms: 1.50x faster                                             |
| hexiom                   | 5.74 ms                                                     | 3.85 ms: 1.49x faster                                             |
| pickle_pure_python       | 270 us                                                      | 183 us: 1.47x faster                                              |
| pyflate                  | 409 ms                                                      | 281 ms: 1.46x faster                                              |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.47 sec: 1.43x faster                                            |
| asyncio_tcp              | 732 ms                                                      | 517 ms: 1.42x faster                                              |
| unpickle_pure_python     | 183 us                                                      | 130 us: 1.41x faster                                              |
| scimark_monte_carlo      | 57.3 ms                                                     | 41.1 ms: 1.39x faster                                             |
| scimark_sor              | 106 ms                                                      | 76.9 ms: 1.38x faster                                             |
| crypto_pyaes             | 62.5 ms                                                     | 45.7 ms: 1.37x faster                                             |
| mako                     | 9.03 ms                                                     | 6.68 ms: 1.35x faster                                             |
| django_template          | 28.9 ms                                                     | 22.1 ms: 1.31x faster                                             |
| mdp                      | 1.78 sec                                                    | 1.36 sec: 1.31x faster                                            |
| mypy2                    | 555 ms                                                      | 431 ms: 1.29x faster                                              |
| genshi_text              | 19.8 ms                                                     | 15.5 ms: 1.28x faster                                             |
| html5lib                 | 51.0 ms                                                     | 40.2 ms: 1.27x faster                                             |
| regex_compile            | 106 ms                                                      | 83.8 ms: 1.26x faster                                             |
| deepcopy_memo            | 28.8 us                                                     | 22.8 us: 1.26x faster                                             |
| spectral_norm            | 77.3 ms                                                     | 61.5 ms: 1.26x faster                                             |
| sympy_sum                | 107 ms                                                      | 86.8 ms: 1.23x faster                                             |
| docutils                 | 1.92 sec                                                    | 1.56 sec: 1.23x faster                                            |
| sympy_integrate          | 15.3 ms                                                     | 12.4 ms: 1.23x faster                                             |
| pycparser                | 930 ms                                                      | 758 ms: 1.23x faster                                              |
| float                    | 61.7 ms                                                     | 50.3 ms: 1.23x faster                                             |
| dulwich_log              | 50.5 ms                                                     | 41.4 ms: 1.22x faster                                             |
| bench_thread_pool        | 958 us                                                      | 786 us: 1.22x faster                                              |
| coroutines               | 16.0 ms                                                     | 13.1 ms: 1.22x faster                                             |
| pprint_pformat           | 1.22 sec                                                    | 1.00 sec: 1.21x faster                                            |
| xml_etree_process        | 44.5 ms                                                     | 36.7 ms: 1.21x faster                                             |
| pprint_safe_repr         | 592 ms                                                      | 492 ms: 1.20x faster                                              |
| tomli_loads              | 1.67 sec                                                    | 1.39 sec: 1.20x faster                                            |
| genshi_xml               | 41.0 ms                                                     | 34.3 ms: 1.20x faster                                             |
| sqlite_synth             | 1.91 us                                                     | 1.60 us: 1.19x faster                                             |
| sqlglot_optimize         | 39.8 ms                                                     | 33.5 ms: 1.19x faster                                             |
| chameleon                | 5.79 ms                                                     | 4.89 ms: 1.18x faster                                             |
| tornado_http             | 108 ms                                                      | 92.2 ms: 1.18x faster                                             |
| sqlglot_normalize        | 205 ms                                                      | 175 ms: 1.17x faster                                              |
| nqueens                  | 66.6 ms                                                     | 56.9 ms: 1.17x faster                                             |
| sympy_str                | 194 ms                                                      | 167 ms: 1.16x faster                                              |
| regex_dna                | 136 ms                                                      | 118 ms: 1.15x faster                                              |
| 2to3                     | 246 ms                                                      | 216 ms: 1.14x faster                                              |
| deepcopy                 | 255 us                                                      | 226 us: 1.13x faster                                              |
| logging_format           | 6.76 us                                                     | 6.11 us: 1.11x faster                                             |
| sympy_expand             | 314 ms                                                      | 285 ms: 1.10x faster                                              |
| logging_simple           | 6.22 us                                                     | 5.70 us: 1.09x faster                                             |
| deepcopy_reduce          | 2.20 us                                                     | 2.02 us: 1.09x faster                                             |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.50 ms: 1.09x faster                                             |
| unpickle                 | 9.09 us                                                     | 8.49 us: 1.07x faster                                             |
| xml_etree_parse          | 96.8 ms                                                     | 90.9 ms: 1.07x faster                                             |
| scimark_fft              | 187 ms                                                      | 176 ms: 1.06x faster                                              |
| xml_etree_iterparse      | 65.0 ms                                                     | 61.1 ms: 1.06x faster                                             |
| regex_effbot             | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                             |
| json                     | 3.14 ms                                                     | 2.99 ms: 1.05x faster                                             |
| unpack_sequence          | 39.6 ns                                                     | 37.8 ns: 1.05x faster                                             |
| aiohttp                  | 995 us                                                      | 950 us: 1.05x faster                                              |
| xml_etree_generate       | 55.5 ms                                                     | 53.0 ms: 1.05x faster                                             |
| fannkuch                 | 256 ms                                                      | 246 ms: 1.04x faster                                              |
| meteor_contest           | 75.9 ms                                                     | 73.9 ms: 1.03x faster                                             |
| unpickle_list            | 2.71 us                                                     | 2.66 us: 1.02x faster                                             |
| async_generators         | 222 ms                                                      | 219 ms: 1.01x faster                                              |
| flaskblogging            | 2.03 sec                                                    | 2.03 sec: 1.00x slower                                            |
| pidigits                 | 149 ms                                                      | 150 ms: 1.01x slower                                              |
| create_gc_cycles         | 800 us                                                      | 807 us: 1.01x slower                                              |
| pathlib                  | 75.7 ms                                                     | 79.3 ms: 1.05x slower                                             |
| pickle                   | 6.85 us                                                     | 7.21 us: 1.05x slower                                             |
| python_startup           | 20.6 ms                                                     | 22.4 ms: 1.09x slower                                             |
| pickle_dict              | 17.2 us                                                     | 18.8 us: 1.09x slower                                             |
| gc_traversal             | 1.41 ms                                                     | 1.55 ms: 1.10x slower                                             |
| bench_mp_pool            | 62.0 ms                                                     | 69.3 ms: 1.12x slower                                             |
| pickle_list              | 2.75 us                                                     | 3.11 us: 1.13x slower                                             |
| python_startup_no_site   | 15.5 ms                                                     | 17.9 ms: 1.15x slower                                             |
| telco                    | 3.94 ms                                                     | 4.61 ms: 1.17x slower                                             |
| coverage                 | 39.0 ms                                                     | 45.9 ms: 1.18x slower                                             |
| thrift                   | 617 us                                                      | 8.70 ms: 14.10x slower                                            |
| Geometric mean           | (ref)                                                       | 1.20x faster                                                      |

Benchmark hidden because not significant (3): nbody, json_loads, regex_v8
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: dask, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20241001-3.13.0rc3-fae84c7/bm-20241001-pythonperf1-amd64-python-v3.13.0rc3-3.13.0rc3-fae84c7.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.222x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: unknown