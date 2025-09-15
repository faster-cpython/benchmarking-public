# Results vs. 3.10.4

- fork: python
- ref: 7168e98c80d28ab71f39
- machine: windows-amd64
- commit hash: 7168e98
- commit date: 2025-09-13
- overall geometric mean: 1.355x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 214 ms: 1.15x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.60 sec: 1.20x faster                                                     |
| html5lib       | 51.0 ms                                                     | 36.7 ms: 1.39x faster                                                      |
| Geometric mean | (ref)                                                       | 1.24x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 382 ms: 2.90x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 202 ms: 2.60x faster                                                       |
| async_tree_none         | 435 ms                                                      | 168 ms: 2.58x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 330 ms: 1.93x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.48x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 43.7 ms: 1.41x faster                                                      |
| nbody          | 71.3 ms                                                     | 55.5 ms: 1.28x faster                                                      |
| pidigits       | 149 ms                                                      | 147 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.22x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 76.8 ms: 1.38x faster                                                      |
| regex_dna      | 136 ms                                                      | 118 ms: 1.16x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.2 ms: 1.09x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                                      |
| Geometric mean | (ref)                                                       | 1.17x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 105 us: 1.75x faster                                                       |
| json_dumps           | 9.16 ms                                                     | 5.51 ms: 1.66x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.08 sec: 1.54x faster                                                     |
| pickle_pure_python   | 270 us                                                      | 198 us: 1.36x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 35.8 ms: 1.24x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 84.7 ms: 1.14x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 50.2 ms: 1.11x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.41 us: 1.08x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 60.9 ms: 1.07x faster                                                      |
| json_loads           | 14.0 us                                                     | 13.8 us: 1.02x faster                                                      |
| pickle               | 6.85 us                                                     | 7.44 us: 1.09x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 19.0 us: 1.10x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.16 us: 1.15x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.16x faster                                                               |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 18.6 ms: 1.20x slower                                                      |
| python_startup         | 20.6 ms                                                     | 25.0 ms: 1.21x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.21x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.25 ms: 1.72x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.3 ms: 1.29x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 34.0 ms: 1.21x faster                                                      |
| django_template | 28.9 ms                                                     | 24.0 ms: 1.20x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.34x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 100 us: 3.36x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 382 ms: 2.90x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 28.9 ms: 2.62x faster                                                      |
| async_tree_memoization   | 526 ms                                                      | 202 ms: 2.60x faster                                                       |
| async_tree_none          | 435 ms                                                      | 168 ms: 2.58x faster                                                       |
| mdp                      | 1.78 sec                                                    | 791 ms: 2.25x faster                                                       |
| richards_super           | 52.2 ms                                                     | 26.5 ms: 1.97x faster                                                      |
| deltablue                | 4.19 ms                                                     | 2.15 ms: 1.95x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 330 ms: 1.93x faster                                                       |
| richards                 | 42.4 ms                                                     | 22.3 ms: 1.90x faster                                                      |
| go                       | 139 ms                                                      | 74.3 ms: 1.87x faster                                                      |
| pylint                   | 350 ms                                                      | 194 ms: 1.81x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 53.2 ns: 1.78x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 105 us: 1.75x faster                                                       |
| mako                     | 9.03 ms                                                     | 5.25 ms: 1.72x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 16.9 us: 1.70x faster                                                      |
| generators               | 32.4 ms                                                     | 19.2 ms: 1.69x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.51 ms: 1.66x faster                                                      |
| pyflate                  | 409 ms                                                      | 252 ms: 1.62x faster                                                       |
| comprehensions           | 16.5 us                                                     | 10.5 us: 1.57x faster                                                      |
| raytrace                 | 273 ms                                                      | 174 ms: 1.57x faster                                                       |
| deepcopy                 | 255 us                                                      | 164 us: 1.56x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.08 sec: 1.54x faster                                                     |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.39 sec: 1.52x faster                                                     |
| chaos                    | 61.7 ms                                                     | 40.7 ms: 1.52x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 56.8 ms: 1.51x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 38.1 ms: 1.50x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 497 ms: 1.47x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.02 ms: 1.43x faster                                                      |
| scimark_sor              | 106 ms                                                      | 74.4 ms: 1.43x faster                                                      |
| float                    | 61.7 ms                                                     | 43.7 ms: 1.41x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 867 ms: 1.41x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 422 ms: 1.40x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 44.7 ms: 1.40x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 36.7 ms: 1.39x faster                                                      |
| regex_compile            | 106 ms                                                      | 76.8 ms: 1.38x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 198 us: 1.36x faster                                                       |
| pycparser                | 930 ms                                                      | 685 ms: 1.36x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 15.3 ms: 1.29x faster                                                      |
| nbody                    | 71.3 ms                                                     | 55.5 ms: 1.28x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 39.5 ms: 1.28x faster                                                      |
| scimark_fft              | 187 ms                                                      | 147 ms: 1.27x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.51 us: 1.26x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 61.2 ms: 1.26x faster                                                      |
| sympy_sum                | 107 ms                                                      | 85.4 ms: 1.25x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.77 us: 1.25x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 35.8 ms: 1.24x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 12.4 ms: 1.23x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.23 ms: 1.22x faster                                                      |
| thrift                   | 617 us                                                      | 510 us: 1.21x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 34.0 ms: 1.21x faster                                                      |
| fannkuch                 | 256 ms                                                      | 212 ms: 1.20x faster                                                       |
| django_template          | 28.9 ms                                                     | 24.0 ms: 1.20x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.60 sec: 1.20x faster                                                     |
| sympy_str                | 194 ms                                                      | 166 ms: 1.17x faster                                                       |
| regex_dna                | 136 ms                                                      | 118 ms: 1.16x faster                                                       |
| 2to3                     | 246 ms                                                      | 214 ms: 1.15x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 84.7 ms: 1.14x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 58.8 ms: 1.13x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 860 us: 1.11x faster                                                       |
| json                     | 3.14 ms                                                     | 2.83 ms: 1.11x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 50.2 ms: 1.11x faster                                                      |
| unpack_sequence          | 39.6 ns                                                     | 36.0 ns: 1.10x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.6 ms: 1.10x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 14.2 ms: 1.09x faster                                                      |
| unpickle                 | 9.09 us                                                     | 8.41 us: 1.08x faster                                                      |
| sympy_expand             | 314 ms                                                      | 292 ms: 1.08x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 60.9 ms: 1.07x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 71.4 ms: 1.06x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.41 us: 1.05x faster                                                      |
| logging_simple           | 6.22 us                                                     | 5.97 us: 1.04x faster                                                      |
| telco                    | 3.94 ms                                                     | 3.80 ms: 1.04x faster                                                      |
| json_loads               | 14.0 us                                                     | 13.8 us: 1.02x faster                                                      |
| pidigits                 | 149 ms                                                      | 147 ms: 1.01x faster                                                       |
| pickle                   | 6.85 us                                                     | 7.44 us: 1.09x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 19.0 us: 1.10x slower                                                      |
| async_generators         | 222 ms                                                      | 251 ms: 1.13x slower                                                       |
| pickle_list              | 2.75 us                                                     | 3.16 us: 1.15x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 18.6 ms: 1.20x slower                                                      |
| python_startup           | 20.6 ms                                                     | 25.0 ms: 1.21x slower                                                      |
| coverage                 | 39.0 ms                                                     | 49.3 ms: 1.26x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 88.0 ms: 1.42x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.06 ms: 1.46x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.25 ms: 1.57x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.32x faster                                                               |

Benchmark hidden because not significant (1): unpickle_list
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250913-3.15.0a0-7168e98-JIT/bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.355x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: unknown