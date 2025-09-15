# Results vs. 3.10.4

- fork: python
- ref: 7168e98c80d28ab71f39
- machine: windows-amd64
- commit hash: 7168e98
- commit date: 2025-09-13
- overall geometric mean: 1.145x faster
- HPT reliability: 99.85%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 228 ms: 1.08x faster                                                       |
| docutils       | 1.92 sec                                                    | 2.87 sec: 1.49x slower                                                     |
| html5lib       | 51.0 ms                                                     | 40.8 ms: 1.25x faster                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 358 ms: 3.10x faster                                                       |
| async_tree_none         | 435 ms                                                      | 174 ms: 2.50x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 214 ms: 2.46x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 334 ms: 1.91x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.45x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 46.5 ms: 1.33x faster                                                      |
| pidigits       | 149 ms                                                      | 136 ms: 1.09x faster                                                       |
| nbody          | 71.3 ms                                                     | 82.5 ms: 1.16x slower                                                      |
| Geometric mean | (ref)                                                       | 1.08x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 117 ms: 1.16x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 13.5 ms: 1.14x faster                                                      |
| regex_compile  | 106 ms                                                      | 95.2 ms: 1.11x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.60 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                       | 1.11x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.15 ms: 1.49x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 160 us: 1.14x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 238 us: 1.13x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 58.4 ms: 1.11x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 91.0 ms: 1.06x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 44.9 ms: 1.01x slower                                                      |
| unpickle             | 9.09 us                                                     | 9.94 us: 1.09x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.05 us: 1.11x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 62.9 ms: 1.13x slower                                                      |
| json_loads           | 14.0 us                                                     | 16.1 us: 1.15x slower                                                      |
| pickle               | 6.85 us                                                     | 7.92 us: 1.16x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 20.2 us: 1.18x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 3.30 us: 1.22x slower                                                      |
| tomli_loads          | 1.67 sec                                                    | 2.40 sec: 1.43x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.0 ms: 1.22x slower                                                      |
| python_startup         | 20.6 ms                                                     | 25.2 ms: 1.22x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.22x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 28.9 ms                                                     | 27.5 ms: 1.05x faster                                                      |
| mako            | 9.03 ms                                                     | 10.1 ms: 1.12x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io            | 1.11 sec                                                    | 358 ms: 3.10x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 28.9 ms: 2.61x faster                                                      |
| typing_runtime_protocols | 336 us                                                      | 134 us: 2.50x faster                                                       |
| async_tree_none          | 435 ms                                                      | 174 ms: 2.50x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 214 ms: 2.46x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 334 ms: 1.91x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 413 ms: 1.77x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.45 ms: 1.71x faster                                                      |
| pylint                   | 350 ms                                                      | 209 ms: 1.68x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 62.3 ns: 1.52x faster                                                      |
| go                       | 139 ms                                                      | 91.8 ms: 1.51x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.18 sec: 1.51x faster                                                     |
| json_dumps               | 9.16 ms                                                     | 6.15 ms: 1.49x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 19.9 us: 1.44x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.34 us: 1.42x faster                                                      |
| generators               | 32.4 ms                                                     | 23.2 ms: 1.39x faster                                                      |
| comprehensions           | 16.5 us                                                     | 12.2 us: 1.35x faster                                                      |
| float                    | 61.7 ms                                                     | 46.5 ms: 1.33x faster                                                      |
| deepcopy                 | 255 us                                                      | 195 us: 1.31x faster                                                       |
| richards_super           | 52.2 ms                                                     | 39.9 ms: 1.31x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 65.6 ms: 1.31x faster                                                      |
| chaos                    | 61.7 ms                                                     | 47.6 ms: 1.30x faster                                                      |
| pyflate                  | 409 ms                                                      | 319 ms: 1.28x faster                                                       |
| raytrace                 | 273 ms                                                      | 217 ms: 1.26x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 40.8 ms: 1.25x faster                                                      |
| richards                 | 42.4 ms                                                     | 34.1 ms: 1.24x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.71 ms: 1.22x faster                                                      |
| scimark_sor              | 106 ms                                                      | 88.4 ms: 1.20x faster                                                      |
| pycparser                | 930 ms                                                      | 775 ms: 1.20x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 42.3 ms: 1.19x faster                                                      |
| regex_dna                | 136 ms                                                      | 117 ms: 1.16x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 160 us: 1.14x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 13.5 ms: 1.14x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 238 us: 1.13x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 51.3 ms: 1.12x faster                                                      |
| regex_compile            | 106 ms                                                      | 95.2 ms: 1.11x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 58.4 ms: 1.11x faster                                                      |
| sympy_sum                | 107 ms                                                      | 97.5 ms: 1.10x faster                                                      |
| pidigits                 | 149 ms                                                      | 136 ms: 1.09x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 70.7 ms: 1.09x faster                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.30 ms: 1.08x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 14.1 ms: 1.08x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.8 ms: 1.08x faster                                                      |
| thrift                   | 617 us                                                      | 573 us: 1.08x faster                                                       |
| 2to3                     | 246 ms                                                      | 228 ms: 1.08x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 58.5 ms: 1.07x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 91.0 ms: 1.06x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 2.08 us: 1.06x faster                                                      |
| django_template          | 28.9 ms                                                     | 27.5 ms: 1.05x faster                                                      |
| unpack_sequence          | 39.6 ns                                                     | 37.9 ns: 1.05x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.60 ms: 1.04x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 577 ms: 1.03x faster                                                       |
| sympy_str                | 194 ms                                                      | 190 ms: 1.02x faster                                                       |
| json                     | 3.14 ms                                                     | 3.08 ms: 1.02x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 44.9 ms: 1.01x slower                                                      |
| sympy_expand             | 314 ms                                                      | 321 ms: 1.02x slower                                                       |
| logging_format           | 6.76 us                                                     | 7.19 us: 1.06x slower                                                      |
| logging_simple           | 6.22 us                                                     | 6.69 us: 1.08x slower                                                      |
| unpickle                 | 9.09 us                                                     | 9.94 us: 1.09x slower                                                      |
| nqueens                  | 66.6 ms                                                     | 72.9 ms: 1.09x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.05 us: 1.11x slower                                                      |
| bench_thread_pool        | 958 us                                                      | 1.07 ms: 1.12x slower                                                      |
| mako                     | 9.03 ms                                                     | 10.1 ms: 1.12x slower                                                      |
| scimark_fft              | 187 ms                                                      | 212 ms: 1.13x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 62.9 ms: 1.13x slower                                                      |
| json_loads               | 14.0 us                                                     | 16.1 us: 1.15x slower                                                      |
| pickle                   | 6.85 us                                                     | 7.92 us: 1.16x slower                                                      |
| nbody                    | 71.3 ms                                                     | 82.5 ms: 1.16x slower                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 3.19 ms: 1.17x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 89.0 ms: 1.17x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 20.2 us: 1.18x slower                                                      |
| fannkuch                 | 256 ms                                                      | 305 ms: 1.19x slower                                                       |
| async_generators         | 222 ms                                                      | 265 ms: 1.20x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.77 ms: 1.21x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 75.3 ms: 1.21x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 3.30 us: 1.22x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.0 ms: 1.22x slower                                                      |
| python_startup           | 20.6 ms                                                     | 25.2 ms: 1.22x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 998 us: 1.25x slower                                                       |
| tomli_loads              | 1.67 sec                                                    | 2.40 sec: 1.43x slower                                                     |
| pprint_pformat           | 1.22 sec                                                    | 1.76 sec: 1.44x slower                                                     |
| docutils                 | 1.92 sec                                                    | 2.87 sec: 1.49x slower                                                     |
| coverage                 | 39.0 ms                                                     | 67.7 ms: 1.74x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.12x faster                                                               |

Benchmark hidden because not significant (3): genshi_xml, genshi_text, asyncio_tcp_ssl
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250913-3.15.0a0-7168e98-NOGIL/bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.145x faster

# HPT report

- Reliability score: 99.85% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown