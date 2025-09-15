# Results vs. 3.10.4

- fork: python
- ref: 7168e98c80d28ab71f39
- machine: windows-amd64
- commit hash: 7168e98
- commit date: 2025-09-13
- overall geometric mean: 1.306x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 215 ms: 1.14x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.63 sec: 1.18x faster                                                     |
| html5lib       | 51.0 ms                                                     | 37.5 ms: 1.36x faster                                                      |
| Geometric mean | (ref)                                                       | 1.23x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 390 ms: 2.84x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 201 ms: 2.62x faster                                                       |
| async_tree_none         | 435 ms                                                      | 176 ms: 2.48x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 329 ms: 1.94x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.44x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 42.5 ms: 1.45x faster                                                      |
| nbody          | 71.3 ms                                                     | 65.5 ms: 1.09x faster                                                      |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 77.3 ms: 1.37x faster                                                      |
| regex_dna      | 136 ms                                                      | 121 ms: 1.13x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.0 ms: 1.11x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.53 ms: 1.08x faster                                                      |
| Geometric mean | (ref)                                                       | 1.17x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.44 ms: 1.68x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 134 us: 1.37x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 209 us: 1.29x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.34 sec: 1.24x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 38.1 ms: 1.17x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 86.3 ms: 1.12x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.48 us: 1.07x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 60.9 ms: 1.07x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 55.1 ms: 1.01x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.3 us: 1.02x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 2.78 us: 1.02x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 19.4 us: 1.13x slower                                                      |
| pickle               | 6.85 us                                                     | 7.80 us: 1.14x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.27 us: 1.19x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.09x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 18.5 ms: 1.19x slower                                                      |
| python_startup         | 20.6 ms                                                     | 24.9 ms: 1.21x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.20x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.67 ms: 1.35x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.3 ms: 1.29x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 34.4 ms: 1.19x faster                                                      |
| django_template | 28.9 ms                                                     | 25.2 ms: 1.15x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.24x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 101 us: 3.33x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 390 ms: 2.84x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 28.8 ms: 2.63x faster                                                      |
| async_tree_memoization   | 526 ms                                                      | 201 ms: 2.62x faster                                                       |
| async_tree_none          | 435 ms                                                      | 176 ms: 2.48x faster                                                       |
| mdp                      | 1.78 sec                                                    | 800 ms: 2.23x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 329 ms: 1.94x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.20 ms: 1.91x faster                                                      |
| go                       | 139 ms                                                      | 75.5 ms: 1.84x faster                                                      |
| pylint                   | 350 ms                                                      | 191 ms: 1.83x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 16.6 us: 1.73x faster                                                      |
| generators               | 32.4 ms                                                     | 18.9 ms: 1.72x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 55.2 ns: 1.71x faster                                                      |
| richards_super           | 52.2 ms                                                     | 30.5 ms: 1.71x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.44 ms: 1.68x faster                                                      |
| richards                 | 42.4 ms                                                     | 26.8 ms: 1.58x faster                                                      |
| raytrace                 | 273 ms                                                      | 177 ms: 1.54x faster                                                       |
| deepcopy                 | 255 us                                                      | 166 us: 1.54x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.39 sec: 1.52x faster                                                     |
| comprehensions           | 16.5 us                                                     | 10.9 us: 1.51x faster                                                      |
| chaos                    | 61.7 ms                                                     | 40.9 ms: 1.51x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 494 ms: 1.48x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 58.3 ms: 1.47x faster                                                      |
| float                    | 61.7 ms                                                     | 42.5 ms: 1.45x faster                                                      |
| pyflate                  | 409 ms                                                      | 282 ms: 1.45x faster                                                       |
| scimark_sor              | 106 ms                                                      | 74.5 ms: 1.42x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.04 ms: 1.42x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.5 ms: 1.42x faster                                                      |
| regex_compile            | 106 ms                                                      | 77.3 ms: 1.37x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 134 us: 1.37x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 37.5 ms: 1.36x faster                                                      |
| mako                     | 9.03 ms                                                     | 6.67 ms: 1.35x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 47.1 ms: 1.33x faster                                                      |
| pycparser                | 930 ms                                                      | 705 ms: 1.32x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 15.3 ms: 1.29x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 209 us: 1.29x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 39.3 ms: 1.29x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 975 ms: 1.25x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 12.3 ms: 1.25x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.34 sec: 1.24x faster                                                     |
| deepcopy_reduce          | 2.20 us                                                     | 1.77 us: 1.24x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 62.5 ms: 1.24x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.55 us: 1.23x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 480 ms: 1.23x faster                                                       |
| thrift                   | 617 us                                                      | 502 us: 1.23x faster                                                       |
| sympy_sum                | 107 ms                                                      | 87.5 ms: 1.22x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 34.4 ms: 1.19x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.63 sec: 1.18x faster                                                     |
| sympy_str                | 194 ms                                                      | 165 ms: 1.18x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 38.1 ms: 1.17x faster                                                      |
| django_template          | 28.9 ms                                                     | 25.2 ms: 1.15x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 836 us: 1.15x faster                                                       |
| 2to3                     | 246 ms                                                      | 215 ms: 1.14x faster                                                       |
| regex_dna                | 136 ms                                                      | 121 ms: 1.13x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 86.3 ms: 1.12x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.4 ms: 1.11x faster                                                      |
| sympy_expand             | 314 ms                                                      | 284 ms: 1.11x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 14.0 ms: 1.11x faster                                                      |
| unpack_sequence          | 39.6 ns                                                     | 36.1 ns: 1.10x faster                                                      |
| nbody                    | 71.3 ms                                                     | 65.5 ms: 1.09x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.51 ms: 1.09x faster                                                      |
| json                     | 3.14 ms                                                     | 2.89 ms: 1.08x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 61.5 ms: 1.08x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.53 ms: 1.08x faster                                                      |
| unpickle                 | 9.09 us                                                     | 8.48 us: 1.07x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 60.9 ms: 1.07x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.46 us: 1.05x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 72.6 ms: 1.05x faster                                                      |
| scimark_fft              | 187 ms                                                      | 180 ms: 1.04x faster                                                       |
| logging_simple           | 6.22 us                                                     | 5.98 us: 1.04x faster                                                      |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 55.1 ms: 1.01x faster                                                      |
| json_loads               | 14.0 us                                                     | 14.3 us: 1.02x slower                                                      |
| fannkuch                 | 256 ms                                                      | 261 ms: 1.02x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 2.78 us: 1.02x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.14 ms: 1.05x slower                                                      |
| async_generators         | 222 ms                                                      | 234 ms: 1.06x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 19.4 us: 1.13x slower                                                      |
| pickle                   | 6.85 us                                                     | 7.80 us: 1.14x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.27 us: 1.19x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 18.5 ms: 1.19x slower                                                      |
| python_startup           | 20.6 ms                                                     | 24.9 ms: 1.21x slower                                                      |
| coverage                 | 39.0 ms                                                     | 48.8 ms: 1.25x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 87.8 ms: 1.41x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.13 ms: 1.51x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.24 ms: 1.55x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.27x faster                                                               |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250913-3.15.0a0-7168e98/bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.306x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: unknown