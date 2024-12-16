# Results vs. 3.10.4

- fork: python
- ref: 2de048ce79e621f5ae05
- machine: windows-amd64
- commit hash: 2de048c
- commit date: 2024-12-13
- overall geometric mean: 1.248x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241213-pythonperf1-amd64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 219 ms: 1.12x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.71 sec: 1.12x faster                                                      |
| html5lib       | 51.0 ms                                                     | 39.2 ms: 1.30x faster                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241213-pythonperf1-amd64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 395 ms: 2.80x faster                                                        |
| async_tree_none         | 435 ms                                                      | 181 ms: 2.41x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 220 ms: 2.39x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 354 ms: 1.80x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.32x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241213-pythonperf1-amd64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 45.3 ms: 1.36x faster                                                       |
| nbody          | 71.3 ms                                                     | 52.8 ms: 1.35x faster                                                       |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                       | 1.23x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241213-pythonperf1-amd64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 81.3 ms: 1.30x faster                                                       |
| regex_dna      | 136 ms                                                      | 113 ms: 1.21x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.40 ms: 1.18x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 20.9 ms: 1.35x slower                                                       |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241213-pythonperf1-amd64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 110 us: 1.66x faster                                                        |
| json_dumps           | 9.16 ms                                                     | 6.22 ms: 1.47x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.23 sec: 1.36x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 208 us: 1.29x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 36.4 ms: 1.22x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 85.0 ms: 1.14x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 58.3 ms: 1.11x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 50.8 ms: 1.09x faster                                                       |
| json_loads           | 14.0 us                                                     | 14.2 us: 1.01x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.25x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241213-pythonperf1-amd64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 17.4 ms: 1.12x slower                                                       |
| python_startup         | 20.6 ms                                                     | 23.3 ms: 1.13x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241213-pythonperf1-amd64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.11 ms: 1.77x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 18.8 ms: 1.05x faster                                                       |
| django_template | 28.9 ms                                                     | 27.5 ms: 1.05x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 48.5 ms: 1.18x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.13x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241213-pythonperf1-amd64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 114 us: 2.95x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 395 ms: 2.80x faster                                                        |
| async_tree_none          | 435 ms                                                      | 181 ms: 2.41x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 220 ms: 2.39x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.29 ms: 1.83x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 354 ms: 1.80x faster                                                        |
| mako                     | 9.03 ms                                                     | 5.11 ms: 1.77x faster                                                       |
| scimark_sor              | 106 ms                                                      | 61.2 ms: 1.74x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 16.6 us: 1.73x faster                                                       |
| pylint                   | 350 ms                                                      | 207 ms: 1.69x faster                                                        |
| unpickle_pure_python     | 183 us                                                      | 110 us: 1.66x faster                                                        |
| spectral_norm            | 77.3 ms                                                     | 49.1 ms: 1.57x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 36.4 ms: 1.57x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 55.5 ms: 1.55x faster                                                       |
| go                       | 139 ms                                                      | 90.0 ms: 1.54x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 40.7 ms: 1.54x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 61.7 ns: 1.53x faster                                                       |
| pyflate                  | 409 ms                                                      | 276 ms: 1.48x faster                                                        |
| json_dumps               | 9.16 ms                                                     | 6.22 ms: 1.47x faster                                                       |
| chaos                    | 61.7 ms                                                     | 42.4 ms: 1.45x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 838 us: 1.45x faster                                                        |
| comprehensions           | 16.5 us                                                     | 11.9 us: 1.39x faster                                                       |
| float                    | 61.7 ms                                                     | 45.3 ms: 1.36x faster                                                       |
| generators               | 32.4 ms                                                     | 23.8 ms: 1.36x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.09 ms: 1.36x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.23 sec: 1.36x faster                                                      |
| deepcopy                 | 255 us                                                      | 188 us: 1.36x faster                                                        |
| nbody                    | 71.3 ms                                                     | 52.8 ms: 1.35x faster                                                       |
| richards_super           | 52.2 ms                                                     | 39.1 ms: 1.34x faster                                                       |
| pycparser                | 930 ms                                                      | 707 ms: 1.32x faster                                                        |
| raytrace                 | 273 ms                                                      | 208 ms: 1.31x faster                                                        |
| regex_compile            | 106 ms                                                      | 81.3 ms: 1.30x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 39.2 ms: 1.30x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 208 us: 1.29x faster                                                        |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.11 ms: 1.29x faster                                                       |
| scimark_fft              | 187 ms                                                      | 146 ms: 1.29x faster                                                        |
| pprint_pformat           | 1.22 sec                                                    | 988 ms: 1.23x faster                                                        |
| dulwich_log              | 50.5 ms                                                     | 40.9 ms: 1.23x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.55 us: 1.23x faster                                                       |
| richards                 | 42.4 ms                                                     | 34.7 ms: 1.22x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 36.4 ms: 1.22x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.81 us: 1.22x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 489 ms: 1.21x faster                                                        |
| regex_dna                | 136 ms                                                      | 113 ms: 1.21x faster                                                        |
| mdp                      | 1.78 sec                                                    | 1.49 sec: 1.20x faster                                                      |
| coroutines               | 16.0 ms                                                     | 13.5 ms: 1.18x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.40 ms: 1.18x faster                                                       |
| sympy_sum                | 107 ms                                                      | 90.9 ms: 1.18x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 828 us: 1.16x faster                                                        |
| hexiom                   | 5.74 ms                                                     | 4.97 ms: 1.16x faster                                                       |
| thrift                   | 617 us                                                      | 537 us: 1.15x faster                                                        |
| xml_etree_parse          | 96.8 ms                                                     | 85.0 ms: 1.14x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.6 ms: 1.13x faster                                                       |
| 2to3                     | 246 ms                                                      | 219 ms: 1.12x faster                                                        |
| docutils                 | 1.92 sec                                                    | 1.71 sec: 1.12x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 58.3 ms: 1.11x faster                                                       |
| sympy_str                | 194 ms                                                      | 176 ms: 1.10x faster                                                        |
| xml_etree_generate       | 55.5 ms                                                     | 50.8 ms: 1.09x faster                                                       |
| json                     | 3.14 ms                                                     | 2.97 ms: 1.06x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 18.8 ms: 1.05x faster                                                       |
| django_template          | 28.9 ms                                                     | 27.5 ms: 1.05x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 38.0 ms: 1.05x faster                                                       |
| fannkuch                 | 256 ms                                                      | 244 ms: 1.05x faster                                                        |
| nqueens                  | 66.6 ms                                                     | 64.5 ms: 1.03x faster                                                       |
| sympy_expand             | 314 ms                                                      | 304 ms: 1.03x faster                                                        |
| meteor_contest           | 75.9 ms                                                     | 74.5 ms: 1.02x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.66 us: 1.02x faster                                                       |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                                        |
| sqlglot_normalize        | 205 ms                                                      | 207 ms: 1.01x slower                                                        |
| pathlib                  | 75.7 ms                                                     | 76.2 ms: 1.01x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.2 us: 1.01x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.22 ms: 1.07x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 17.4 ms: 1.12x slower                                                       |
| python_startup           | 20.6 ms                                                     | 23.3 ms: 1.13x slower                                                       |
| mypy2                    | 555 ms                                                      | 634 ms: 1.14x slower                                                        |
| async_generators         | 222 ms                                                      | 255 ms: 1.15x slower                                                        |
| genshi_xml               | 41.0 ms                                                     | 48.5 ms: 1.18x slower                                                       |
| coverage                 | 39.0 ms                                                     | 47.1 ms: 1.21x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 82.3 ms: 1.33x slower                                                       |
| regex_v8                 | 15.4 ms                                                     | 20.9 ms: 1.35x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.98 ms: 1.40x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.21 ms: 1.52x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.24x faster                                                                |

Benchmark hidden because not significant (1): logging_simple
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241213-3.14.0a2+-2de048c-JIT/bm-20241213-pythonperf1-amd64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.248x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown