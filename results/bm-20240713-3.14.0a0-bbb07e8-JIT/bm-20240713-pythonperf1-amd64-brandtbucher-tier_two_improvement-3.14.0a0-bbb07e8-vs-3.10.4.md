# Results vs. 3.10.4

- fork: brandtbucher
- ref: tier_two_improvement
- machine: windows-amd64
- commit hash: bbb07e8
- commit date: 2024-07-13
- overall geometric mean: 1.27x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf1-amd64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 233 ms: 1.06x faster                                                             |
| docutils       | 1.92 sec                                                    | 1.78 sec: 1.08x faster                                                           |
| html5lib       | 51.0 ms                                                     | 39.6 ms: 1.29x faster                                                            |
| tornado_http   | 108 ms                                                      | 85.2 ms: 1.27x faster                                                            |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf1-amd64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 523 ms: 2.12x faster                                                             |
| async_tree_none         | 435 ms                                                      | 206 ms: 2.11x faster                                                             |
| async_tree_memoization  | 526 ms                                                      | 249 ms: 2.11x faster                                                             |
| async_tree_cpu_io_mixed | 638 ms                                                      | 384 ms: 1.66x faster                                                             |
| Geometric mean          | (ref)                                                       | 1.99x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf1-amd64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 44.5 ms: 1.39x faster                                                            |
| nbody          | 71.3 ms                                                     | 53.0 ms: 1.35x faster                                                            |
| Geometric mean | (ref)                                                       | 1.23x faster                                                                     |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf1-amd64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 88.9 ms: 1.19x faster                                                            |
| regex_dna      | 136 ms                                                      | 120 ms: 1.14x faster                                                             |
| regex_effbot   | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                                            |
| Geometric mean | (ref)                                                       | 1.10x faster                                                                     |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf1-amd64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.80 ms: 1.58x faster                                                            |
| pickle_pure_python   | 270 us                                                      | 178 us: 1.52x faster                                                             |
| unpickle_pure_python | 183 us                                                      | 128 us: 1.43x faster                                                             |
| tomli_loads          | 1.67 sec                                                    | 1.26 sec: 1.32x faster                                                           |
| xml_etree_process    | 44.5 ms                                                     | 36.2 ms: 1.23x faster                                                            |
| xml_etree_generate   | 55.5 ms                                                     | 51.3 ms: 1.08x faster                                                            |
| xml_etree_iterparse  | 65.0 ms                                                     | 60.2 ms: 1.08x faster                                                            |
| xml_etree_parse      | 96.8 ms                                                     | 91.1 ms: 1.06x faster                                                            |
| json_loads           | 14.0 us                                                     | 14.3 us: 1.02x slower                                                            |
| Geometric mean       | (ref)                                                       | 1.24x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf1-amd64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 21.3 ms: 1.03x slower                                                            |
| python_startup_no_site | 15.5 ms                                                     | 17.5 ms: 1.13x slower                                                            |
| Geometric mean         | (ref)                                                       | 1.08x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf1-amd64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.10 ms: 1.77x faster                                                            |
| django_template | 28.9 ms                                                     | 25.9 ms: 1.11x faster                                                            |
| genshi_text     | 19.8 ms                                                     | 17.8 ms: 1.11x faster                                                            |
| genshi_xml      | 41.0 ms                                                     | 45.2 ms: 1.10x slower                                                            |
| Geometric mean  | (ref)                                                       | 1.19x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf1-amd64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 113 us: 2.99x faster                                                             |
| async_tree_io            | 1.11 sec                                                    | 523 ms: 2.12x faster                                                             |
| async_tree_none          | 435 ms                                                      | 206 ms: 2.11x faster                                                             |
| async_tree_memoization   | 526 ms                                                      | 249 ms: 2.11x faster                                                             |
| deltablue                | 4.19 ms                                                     | 2.22 ms: 1.89x faster                                                            |
| deepcopy_memo            | 28.8 us                                                     | 16.1 us: 1.78x faster                                                            |
| mako                     | 9.03 ms                                                     | 5.10 ms: 1.77x faster                                                            |
| spectral_norm            | 77.3 ms                                                     | 45.1 ms: 1.71x faster                                                            |
| logging_silent           | 94.6 ns                                                     | 55.5 ns: 1.70x faster                                                            |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 384 ms: 1.66x faster                                                             |
| pyflate                  | 409 ms                                                      | 250 ms: 1.63x faster                                                             |
| comprehensions           | 16.5 us                                                     | 10.4 us: 1.59x faster                                                            |
| json_dumps               | 9.16 ms                                                     | 5.80 ms: 1.58x faster                                                            |
| crypto_pyaes             | 62.5 ms                                                     | 39.7 ms: 1.57x faster                                                            |
| richards_super           | 52.2 ms                                                     | 33.2 ms: 1.57x faster                                                            |
| chaos                    | 61.7 ms                                                     | 39.4 ms: 1.57x faster                                                            |
| asyncio_tcp              | 732 ms                                                      | 469 ms: 1.56x faster                                                             |
| scimark_monte_carlo      | 57.3 ms                                                     | 37.5 ms: 1.53x faster                                                            |
| pylint                   | 350 ms                                                      | 230 ms: 1.52x faster                                                             |
| raytrace                 | 273 ms                                                      | 180 ms: 1.52x faster                                                             |
| pickle_pure_python       | 270 us                                                      | 178 us: 1.52x faster                                                             |
| go                       | 139 ms                                                      | 92.8 ms: 1.50x faster                                                            |
| sqlglot_parse            | 1.22 ms                                                     | 815 us: 1.49x faster                                                             |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.42 sec: 1.49x faster                                                           |
| richards                 | 42.4 ms                                                     | 29.4 ms: 1.44x faster                                                            |
| unpickle_pure_python     | 183 us                                                      | 128 us: 1.43x faster                                                             |
| sqlglot_transpile        | 1.48 ms                                                     | 1.04 ms: 1.42x faster                                                            |
| generators               | 32.4 ms                                                     | 22.9 ms: 1.42x faster                                                            |
| deepcopy                 | 255 us                                                      | 182 us: 1.40x faster                                                             |
| float                    | 61.7 ms                                                     | 44.5 ms: 1.39x faster                                                            |
| nbody                    | 71.3 ms                                                     | 53.0 ms: 1.35x faster                                                            |
| tomli_loads              | 1.67 sec                                                    | 1.26 sec: 1.32x faster                                                           |
| html5lib                 | 51.0 ms                                                     | 39.6 ms: 1.29x faster                                                            |
| tornado_http             | 108 ms                                                      | 85.2 ms: 1.27x faster                                                            |
| pycparser                | 930 ms                                                      | 740 ms: 1.26x faster                                                             |
| hexiom                   | 5.74 ms                                                     | 4.59 ms: 1.25x faster                                                            |
| scimark_sor              | 106 ms                                                      | 85.0 ms: 1.25x faster                                                            |
| scimark_fft              | 187 ms                                                      | 150 ms: 1.25x faster                                                             |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.19 ms: 1.24x faster                                                            |
| mdp                      | 1.78 sec                                                    | 1.44 sec: 1.23x faster                                                           |
| pprint_pformat           | 1.22 sec                                                    | 989 ms: 1.23x faster                                                             |
| xml_etree_process        | 44.5 ms                                                     | 36.2 ms: 1.23x faster                                                            |
| pprint_safe_repr         | 592 ms                                                      | 483 ms: 1.23x faster                                                             |
| deepcopy_reduce          | 2.20 us                                                     | 1.80 us: 1.22x faster                                                            |
| scimark_lu               | 85.8 ms                                                     | 70.3 ms: 1.22x faster                                                            |
| bench_thread_pool        | 958 us                                                      | 801 us: 1.20x faster                                                             |
| regex_compile            | 106 ms                                                      | 88.9 ms: 1.19x faster                                                            |
| thrift                   | 617 us                                                      | 518 us: 1.19x faster                                                             |
| coroutines               | 16.0 ms                                                     | 13.5 ms: 1.18x faster                                                            |
| fannkuch                 | 256 ms                                                      | 219 ms: 1.17x faster                                                             |
| regex_dna                | 136 ms                                                      | 120 ms: 1.14x faster                                                             |
| sympy_sum                | 107 ms                                                      | 94.2 ms: 1.14x faster                                                            |
| django_template          | 28.9 ms                                                     | 25.9 ms: 1.11x faster                                                            |
| genshi_text              | 19.8 ms                                                     | 17.8 ms: 1.11x faster                                                            |
| logging_format           | 6.76 us                                                     | 6.09 us: 1.11x faster                                                            |
| logging_simple           | 6.22 us                                                     | 5.64 us: 1.10x faster                                                            |
| sqlglot_optimize         | 39.8 ms                                                     | 36.1 ms: 1.10x faster                                                            |
| nqueens                  | 66.6 ms                                                     | 60.6 ms: 1.10x faster                                                            |
| sympy_integrate          | 15.3 ms                                                     | 14.0 ms: 1.09x faster                                                            |
| xml_etree_generate       | 55.5 ms                                                     | 51.3 ms: 1.08x faster                                                            |
| xml_etree_iterparse      | 65.0 ms                                                     | 60.2 ms: 1.08x faster                                                            |
| docutils                 | 1.92 sec                                                    | 1.78 sec: 1.08x faster                                                           |
| sympy_str                | 194 ms                                                      | 181 ms: 1.07x faster                                                             |
| regex_effbot             | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                                            |
| sqlglot_normalize        | 205 ms                                                      | 192 ms: 1.07x faster                                                             |
| xml_etree_parse          | 96.8 ms                                                     | 91.1 ms: 1.06x faster                                                            |
| meteor_contest           | 75.9 ms                                                     | 71.7 ms: 1.06x faster                                                            |
| 2to3                     | 246 ms                                                      | 233 ms: 1.06x faster                                                             |
| json                     | 3.14 ms                                                     | 2.98 ms: 1.05x faster                                                            |
| pathlib                  | 75.7 ms                                                     | 75.1 ms: 1.01x faster                                                            |
| sympy_expand             | 314 ms                                                      | 313 ms: 1.00x faster                                                             |
| json_loads               | 14.0 us                                                     | 14.3 us: 1.02x slower                                                            |
| python_startup           | 20.6 ms                                                     | 21.3 ms: 1.03x slower                                                            |
| gc_traversal             | 1.41 ms                                                     | 1.55 ms: 1.10x slower                                                            |
| genshi_xml               | 41.0 ms                                                     | 45.2 ms: 1.10x slower                                                            |
| bench_mp_pool            | 62.0 ms                                                     | 69.3 ms: 1.12x slower                                                            |
| create_gc_cycles         | 800 us                                                      | 899 us: 1.12x slower                                                             |
| python_startup_no_site   | 15.5 ms                                                     | 17.5 ms: 1.13x slower                                                            |
| telco                    | 3.94 ms                                                     | 4.50 ms: 1.14x slower                                                            |
| async_generators         | 222 ms                                                      | 255 ms: 1.15x slower                                                             |
| coverage                 | 39.0 ms                                                     | 46.5 ms: 1.19x slower                                                            |
| Geometric mean           | (ref)                                                       | 1.27x faster                                                                     |

Benchmark hidden because not significant (2): regex_v8, pidigits
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240713-3.14.0a0-bbb07e8-JIT/bm-20240713-pythonperf1-amd64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: unknown