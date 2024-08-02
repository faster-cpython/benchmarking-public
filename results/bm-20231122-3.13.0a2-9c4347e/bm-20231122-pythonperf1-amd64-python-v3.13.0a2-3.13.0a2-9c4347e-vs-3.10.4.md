# Results vs. 3.10.4

- fork: python
- ref: v3.13.0a2
- machine: windows-amd64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.21x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 210 ms: 1.17x faster                                            |
| chameleon      | 5.79 ms                                                     | 4.81 ms: 1.20x faster                                           |
| docutils       | 1.92 sec                                                    | 1.55 sec: 1.24x faster                                          |
| html5lib       | 51.0 ms                                                     | 36.6 ms: 1.39x faster                                           |
| tornado_http   | 108 ms                                                      | 86.1 ms: 1.26x faster                                           |
| Geometric mean | (ref)                                                       | 1.25x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 264 ms: 1.65x faster                                            |
| async_tree_memoization  | 526 ms                                                      | 341 ms: 1.55x faster                                            |
| async_tree_io           | 1.11 sec                                                    | 731 ms: 1.52x faster                                            |
| async_tree_cpu_io_mixed | 638 ms                                                      | 453 ms: 1.41x faster                                            |
| Geometric mean          | (ref)                                                       | 1.53x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 52.3 ms: 1.18x faster                                           |
| pidigits       | 149 ms                                                      | 147 ms: 1.01x faster                                            |
| nbody          | 71.3 ms                                                     | 72.0 ms: 1.01x slower                                           |
| Geometric mean | (ref)                                                       | 1.06x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 78.9 ms: 1.34x faster                                           |
| regex_dna      | 136 ms                                                      | 122 ms: 1.11x faster                                            |
| regex_effbot   | 1.66 ms                                                     | 1.62 ms: 1.02x faster                                           |
| regex_v8       | 15.4 ms                                                     | 15.3 ms: 1.01x faster                                           |
| Geometric mean | (ref)                                                       | 1.11x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.50 ms: 1.66x faster                                           |
| pickle_pure_python   | 270 us                                                      | 179 us: 1.51x faster                                            |
| unpickle_pure_python | 183 us                                                      | 128 us: 1.43x faster                                            |
| tomli_loads          | 1.67 sec                                                    | 1.37 sec: 1.22x faster                                          |
| xml_etree_process    | 44.5 ms                                                     | 36.4 ms: 1.22x faster                                           |
| unpickle             | 9.09 us                                                     | 8.09 us: 1.12x faster                                           |
| xml_etree_parse      | 96.8 ms                                                     | 92.3 ms: 1.05x faster                                           |
| json_loads           | 14.0 us                                                     | 13.4 us: 1.05x faster                                           |
| xml_etree_generate   | 55.5 ms                                                     | 53.2 ms: 1.04x faster                                           |
| pickle               | 6.85 us                                                     | 6.94 us: 1.01x slower                                           |
| pickle_list          | 2.75 us                                                     | 2.83 us: 1.03x slower                                           |
| pickle_dict          | 17.2 us                                                     | 19.1 us: 1.11x slower                                           |
| Geometric mean       | (ref)                                                       | 1.14x faster                                                    |

Benchmark hidden because not significant (2): xml_etree_iterparse, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 19.9 ms: 1.03x faster                                           |
| python_startup_no_site | 15.5 ms                                                     | 17.6 ms: 1.14x slower                                           |
| Geometric mean         | (ref)                                                       | 1.05x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.48 ms: 1.39x faster                                           |
| genshi_text     | 19.8 ms                                                     | 15.0 ms: 1.32x faster                                           |
| django_template | 28.9 ms                                                     | 21.9 ms: 1.32x faster                                           |
| genshi_xml      | 41.0 ms                                                     | 33.1 ms: 1.24x faster                                           |
| Geometric mean  | (ref)                                                       | 1.32x faster                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 73.9 us: 4.55x faster                                           |
| deltablue                | 4.19 ms                                                     | 2.01 ms: 2.08x faster                                           |
| logging_silent           | 94.6 ns                                                     | 54.1 ns: 1.75x faster                                           |
| pylint                   | 350 ms                                                      | 202 ms: 1.73x faster                                            |
| richards_super           | 52.2 ms                                                     | 30.8 ms: 1.70x faster                                           |
| raytrace                 | 273 ms                                                      | 163 ms: 1.68x faster                                            |
| json_dumps               | 9.16 ms                                                     | 5.50 ms: 1.66x faster                                           |
| async_tree_none          | 435 ms                                                      | 264 ms: 1.65x faster                                            |
| go                       | 139 ms                                                      | 84.3 ms: 1.65x faster                                           |
| generators               | 32.4 ms                                                     | 20.0 ms: 1.62x faster                                           |
| sqlglot_parse            | 1.22 ms                                                     | 752 us: 1.62x faster                                            |
| comprehensions           | 16.5 us                                                     | 10.3 us: 1.60x faster                                           |
| chaos                    | 61.7 ms                                                     | 39.2 ms: 1.57x faster                                           |
| asyncio_tcp              | 732 ms                                                      | 465 ms: 1.57x faster                                            |
| richards                 | 42.4 ms                                                     | 27.3 ms: 1.55x faster                                           |
| async_tree_memoization   | 526 ms                                                      | 341 ms: 1.55x faster                                            |
| sqlglot_transpile        | 1.48 ms                                                     | 965 us: 1.53x faster                                            |
| scimark_lu               | 85.8 ms                                                     | 56.4 ms: 1.52x faster                                           |
| async_tree_io            | 1.11 sec                                                    | 731 ms: 1.52x faster                                            |
| pickle_pure_python       | 270 us                                                      | 179 us: 1.51x faster                                            |
| hexiom                   | 5.74 ms                                                     | 3.81 ms: 1.51x faster                                           |
| crypto_pyaes             | 62.5 ms                                                     | 43.3 ms: 1.44x faster                                           |
| unpickle_pure_python     | 183 us                                                      | 128 us: 1.43x faster                                            |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 453 ms: 1.41x faster                                            |
| pyflate                  | 409 ms                                                      | 291 ms: 1.41x faster                                            |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.9 ms: 1.40x faster                                           |
| html5lib                 | 51.0 ms                                                     | 36.6 ms: 1.39x faster                                           |
| mako                     | 9.03 ms                                                     | 6.48 ms: 1.39x faster                                           |
| regex_compile            | 106 ms                                                      | 78.9 ms: 1.34x faster                                           |
| genshi_text              | 19.8 ms                                                     | 15.0 ms: 1.32x faster                                           |
| django_template          | 28.9 ms                                                     | 21.9 ms: 1.32x faster                                           |
| mdp                      | 1.78 sec                                                    | 1.36 sec: 1.31x faster                                          |
| sympy_sum                | 107 ms                                                      | 82.3 ms: 1.30x faster                                           |
| pycparser                | 930 ms                                                      | 723 ms: 1.29x faster                                            |
| tornado_http             | 108 ms                                                      | 86.1 ms: 1.26x faster                                           |
| sympy_integrate          | 15.3 ms                                                     | 12.2 ms: 1.26x faster                                           |
| pprint_pformat           | 1.22 sec                                                    | 979 ms: 1.25x faster                                            |
| scimark_sor              | 106 ms                                                      | 85.4 ms: 1.24x faster                                           |
| sympy_str                | 194 ms                                                      | 156 ms: 1.24x faster                                            |
| docutils                 | 1.92 sec                                                    | 1.55 sec: 1.24x faster                                          |
| genshi_xml               | 41.0 ms                                                     | 33.1 ms: 1.24x faster                                           |
| pprint_safe_repr         | 592 ms                                                      | 479 ms: 1.24x faster                                            |
| sqlglot_optimize         | 39.8 ms                                                     | 32.5 ms: 1.23x faster                                           |
| sqlite_synth             | 1.91 us                                                     | 1.56 us: 1.23x faster                                           |
| deepcopy_memo            | 28.8 us                                                     | 23.5 us: 1.22x faster                                           |
| tomli_loads              | 1.67 sec                                                    | 1.37 sec: 1.22x faster                                          |
| xml_etree_process        | 44.5 ms                                                     | 36.4 ms: 1.22x faster                                           |
| dulwich_log              | 50.5 ms                                                     | 41.4 ms: 1.22x faster                                           |
| spectral_norm            | 77.3 ms                                                     | 63.6 ms: 1.21x faster                                           |
| coroutines               | 16.0 ms                                                     | 13.2 ms: 1.21x faster                                           |
| chameleon                | 5.79 ms                                                     | 4.81 ms: 1.20x faster                                           |
| sqlglot_normalize        | 205 ms                                                      | 171 ms: 1.20x faster                                            |
| float                    | 61.7 ms                                                     | 52.3 ms: 1.18x faster                                           |
| 2to3                     | 246 ms                                                      | 210 ms: 1.17x faster                                            |
| deepcopy                 | 255 us                                                      | 218 us: 1.17x faster                                            |
| sympy_expand             | 314 ms                                                      | 269 ms: 1.17x faster                                            |
| nqueens                  | 66.6 ms                                                     | 58.2 ms: 1.14x faster                                           |
| deepcopy_reduce          | 2.20 us                                                     | 1.95 us: 1.13x faster                                           |
| bench_thread_pool        | 958 us                                                      | 848 us: 1.13x faster                                            |
| unpickle                 | 9.09 us                                                     | 8.09 us: 1.12x faster                                           |
| aiohttp                  | 995 us                                                      | 889 us: 1.12x faster                                            |
| regex_dna                | 136 ms                                                      | 122 ms: 1.11x faster                                            |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.46 ms: 1.11x faster                                           |
| json                     | 3.14 ms                                                     | 2.85 ms: 1.10x faster                                           |
| create_gc_cycles         | 800 us                                                      | 746 us: 1.07x faster                                            |
| fannkuch                 | 256 ms                                                      | 241 ms: 1.06x faster                                            |
| xml_etree_parse          | 96.8 ms                                                     | 92.3 ms: 1.05x faster                                           |
| json_loads               | 14.0 us                                                     | 13.4 us: 1.05x faster                                           |
| meteor_contest           | 75.9 ms                                                     | 72.6 ms: 1.05x faster                                           |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 2.02 sec: 1.05x faster                                          |
| xml_etree_generate       | 55.5 ms                                                     | 53.2 ms: 1.04x faster                                           |
| logging_format           | 6.76 us                                                     | 6.51 us: 1.04x faster                                           |
| python_startup           | 20.6 ms                                                     | 19.9 ms: 1.03x faster                                           |
| logging_simple           | 6.22 us                                                     | 6.07 us: 1.03x faster                                           |
| regex_effbot             | 1.66 ms                                                     | 1.62 ms: 1.02x faster                                           |
| scimark_fft              | 187 ms                                                      | 184 ms: 1.02x faster                                            |
| pidigits                 | 149 ms                                                      | 147 ms: 1.01x faster                                            |
| regex_v8                 | 15.4 ms                                                     | 15.3 ms: 1.01x faster                                           |
| nbody                    | 71.3 ms                                                     | 72.0 ms: 1.01x slower                                           |
| pickle                   | 6.85 us                                                     | 6.94 us: 1.01x slower                                           |
| async_generators         | 222 ms                                                      | 227 ms: 1.03x slower                                            |
| pickle_list              | 2.75 us                                                     | 2.83 us: 1.03x slower                                           |
| bench_mp_pool            | 62.0 ms                                                     | 64.0 ms: 1.03x slower                                           |
| pathlib                  | 75.7 ms                                                     | 79.9 ms: 1.06x slower                                           |
| gc_traversal             | 1.41 ms                                                     | 1.52 ms: 1.08x slower                                           |
| pickle_dict              | 17.2 us                                                     | 19.1 us: 1.11x slower                                           |
| python_startup_no_site   | 15.5 ms                                                     | 17.6 ms: 1.14x slower                                           |
| telco                    | 3.94 ms                                                     | 4.57 ms: 1.16x slower                                           |
| coverage                 | 39.0 ms                                                     | 45.8 ms: 1.17x slower                                           |
| thrift                   | 617 us                                                      | 8.35 ms: 13.52x slower                                          |
| Geometric mean           | (ref)                                                       | 1.21x faster                                                    |

Benchmark hidden because not significant (4): xml_etree_iterparse, unpickle_list, flaskblogging, mypy2
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: unknown