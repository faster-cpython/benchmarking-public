# Results vs. 3.10.4

- fork: python
- ref: a852c7bdd48979218a0c
- machine: windows-amd64
- commit hash: a852c7b
- commit date: 2025-07-26
- overall geometric mean: 1.118x faster
- HPT reliability: 99.57%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 232 ms: 1.06x faster                                                       |
| docutils       | 1.92 sec                                                    | 3.10 sec: 1.62x slower                                                     |
| html5lib       | 51.0 ms                                                     | 42.2 ms: 1.21x faster                                                      |
| Geometric mean | (ref)                                                       | 1.08x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 361 ms: 3.07x faster                                                       |
| async_tree_none         | 435 ms                                                      | 172 ms: 2.54x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 217 ms: 2.43x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 333 ms: 1.92x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.45x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 47.1 ms: 1.31x faster                                                      |
| pidigits       | 149 ms                                                      | 138 ms: 1.08x faster                                                       |
| nbody          | 71.3 ms                                                     | 86.0 ms: 1.21x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 118 ms: 1.16x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 13.6 ms: 1.14x faster                                                      |
| regex_compile  | 106 ms                                                      | 95.6 ms: 1.11x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.64 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                       | 1.10x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 7.12 ms: 1.29x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 234 us: 1.15x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 161 us: 1.14x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 59.9 ms: 1.08x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 92.9 ms: 1.04x faster                                                      |
| pickle_list          | 2.75 us                                                     | 3.14 us: 1.14x slower                                                      |
| unpickle             | 9.09 us                                                     | 10.4 us: 1.15x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 63.8 ms: 1.15x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 3.18 us: 1.17x slower                                                      |
| json_loads           | 14.0 us                                                     | 16.6 us: 1.18x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 20.4 us: 1.18x slower                                                      |
| pickle               | 6.85 us                                                     | 8.37 us: 1.22x slower                                                      |
| tomli_loads          | 1.67 sec                                                    | 2.78 sec: 1.67x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 20.2 ms: 1.30x slower                                                      |
| python_startup         | 20.6 ms                                                     | 27.0 ms: 1.31x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.31x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml     | 41.0 ms                                                     | 41.6 ms: 1.01x slower                                                      |
| mako           | 9.03 ms                                                     | 9.55 ms: 1.06x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io            | 1.11 sec                                                    | 361 ms: 3.07x faster                                                       |
| typing_runtime_protocols | 336 us                                                      | 130 us: 2.58x faster                                                       |
| async_tree_none          | 435 ms                                                      | 172 ms: 2.54x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 217 ms: 2.43x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 33.8 ms: 2.24x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 333 ms: 1.92x faster                                                       |
| pylint                   | 350 ms                                                      | 209 ms: 1.68x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.54 ms: 1.65x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 462 ms: 1.58x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 62.8 ns: 1.51x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.21 sec: 1.47x faster                                                     |
| go                       | 139 ms                                                      | 94.9 ms: 1.46x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.35 us: 1.41x faster                                                      |
| generators               | 32.4 ms                                                     | 23.2 ms: 1.40x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 21.0 us: 1.37x faster                                                      |
| comprehensions           | 16.5 us                                                     | 12.3 us: 1.34x faster                                                      |
| chaos                    | 61.7 ms                                                     | 47.0 ms: 1.31x faster                                                      |
| float                    | 61.7 ms                                                     | 47.1 ms: 1.31x faster                                                      |
| richards_super           | 52.2 ms                                                     | 40.2 ms: 1.30x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 66.6 ms: 1.29x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 7.12 ms: 1.29x faster                                                      |
| raytrace                 | 273 ms                                                      | 214 ms: 1.28x faster                                                       |
| pyflate                  | 409 ms                                                      | 326 ms: 1.26x faster                                                       |
| richards                 | 42.4 ms                                                     | 34.2 ms: 1.24x faster                                                      |
| pycparser                | 930 ms                                                      | 754 ms: 1.23x faster                                                       |
| deepcopy                 | 255 us                                                      | 211 us: 1.21x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 42.2 ms: 1.21x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.77 ms: 1.20x faster                                                      |
| scimark_sor              | 106 ms                                                      | 88.8 ms: 1.20x faster                                                      |
| regex_dna                | 136 ms                                                      | 118 ms: 1.16x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 43.7 ms: 1.15x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 234 us: 1.15x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 161 us: 1.14x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 13.6 ms: 1.14x faster                                                      |
| regex_compile            | 106 ms                                                      | 95.6 ms: 1.11x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 51.9 ms: 1.10x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 59.9 ms: 1.08x faster                                                      |
| thrift                   | 617 us                                                      | 570 us: 1.08x faster                                                       |
| pidigits                 | 149 ms                                                      | 138 ms: 1.08x faster                                                       |
| sympy_sum                | 107 ms                                                      | 100 ms: 1.07x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 59.1 ms: 1.06x faster                                                      |
| 2to3                     | 246 ms                                                      | 232 ms: 1.06x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 92.9 ms: 1.04x faster                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.36 ms: 1.03x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 573 ms: 1.03x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 14.9 ms: 1.03x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 75.5 ms: 1.02x faster                                                      |
| coroutines               | 16.0 ms                                                     | 15.7 ms: 1.02x faster                                                      |
| sympy_str                | 194 ms                                                      | 191 ms: 1.02x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.64 ms: 1.01x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 41.6 ms: 1.01x slower                                                      |
| json                     | 3.14 ms                                                     | 3.20 ms: 1.02x slower                                                      |
| sympy_expand             | 314 ms                                                      | 331 ms: 1.05x slower                                                       |
| mako                     | 9.03 ms                                                     | 9.55 ms: 1.06x slower                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 2.33 sec: 1.10x slower                                                     |
| logging_simple           | 6.22 us                                                     | 6.89 us: 1.11x slower                                                      |
| logging_format           | 6.76 us                                                     | 7.51 us: 1.11x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.14 us: 1.14x slower                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 3.12 ms: 1.14x slower                                                      |
| unpickle                 | 9.09 us                                                     | 10.4 us: 1.15x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 63.8 ms: 1.15x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 87.9 ms: 1.16x slower                                                      |
| scimark_fft              | 187 ms                                                      | 217 ms: 1.16x slower                                                       |
| nqueens                  | 66.6 ms                                                     | 77.3 ms: 1.16x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 3.18 us: 1.17x slower                                                      |
| json_loads               | 14.0 us                                                     | 16.6 us: 1.18x slower                                                      |
| async_generators         | 222 ms                                                      | 262 ms: 1.18x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 20.4 us: 1.18x slower                                                      |
| bench_thread_pool        | 958 us                                                      | 1.15 ms: 1.20x slower                                                      |
| nbody                    | 71.3 ms                                                     | 86.0 ms: 1.21x slower                                                      |
| fannkuch                 | 256 ms                                                      | 309 ms: 1.21x slower                                                       |
| pickle                   | 6.85 us                                                     | 8.37 us: 1.22x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 80.4 ms: 1.30x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 20.2 ms: 1.30x slower                                                      |
| python_startup           | 20.6 ms                                                     | 27.0 ms: 1.31x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.06 ms: 1.33x slower                                                      |
| telco                    | 3.94 ms                                                     | 5.29 ms: 1.34x slower                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.83 sec: 1.50x slower                                                     |
| docutils                 | 1.92 sec                                                    | 3.10 sec: 1.62x slower                                                     |
| tomli_loads              | 1.67 sec                                                    | 2.78 sec: 1.67x slower                                                     |
| coverage                 | 39.0 ms                                                     | 68.0 ms: 1.74x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.09x faster                                                               |

Benchmark hidden because not significant (5): unpack_sequence, deepcopy_reduce, django_template, xml_etree_process, genshi_text
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.118x faster

# HPT report

- Reliability score: 99.57% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown