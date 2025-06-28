# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_o2
- machine: windows-amd64
- commit hash: f528bf3
- commit date: 2025-06-28
- overall geometric mean: 1.308x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 222 ms: 1.11x faster                                               |
| docutils       | 1.92 sec                                                    | 1.66 sec: 1.16x faster                                             |
| html5lib       | 51.0 ms                                                     | 38.4 ms: 1.33x faster                                              |
| Geometric mean | (ref)                                                       | 1.19x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|-------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 397 ms: 2.79x faster                                               |
| async_tree_none         | 435 ms                                                      | 170 ms: 2.56x faster                                               |
| async_tree_memoization  | 526 ms                                                      | 208 ms: 2.52x faster                                               |
| async_tree_cpu_io_mixed | 638 ms                                                      | 334 ms: 1.91x faster                                               |
| Geometric mean          | (ref)                                                       | 2.42x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 45.0 ms: 1.37x faster                                              |
| nbody          | 71.3 ms                                                     | 55.1 ms: 1.29x faster                                              |
| pidigits       | 149 ms                                                      | 146 ms: 1.02x faster                                               |
| Geometric mean | (ref)                                                       | 1.22x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 78.5 ms: 1.35x faster                                              |
| regex_dna      | 136 ms                                                      | 121 ms: 1.12x faster                                               |
| regex_v8       | 15.4 ms                                                     | 14.3 ms: 1.08x faster                                              |
| regex_effbot   | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                              |
| Geometric mean | (ref)                                                       | 1.15x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 108 us: 1.70x faster                                               |
| json_dumps           | 9.16 ms                                                     | 6.19 ms: 1.48x faster                                              |
| tomli_loads          | 1.67 sec                                                    | 1.16 sec: 1.44x faster                                             |
| pickle_pure_python   | 270 us                                                      | 205 us: 1.31x faster                                               |
| xml_etree_process    | 44.5 ms                                                     | 36.1 ms: 1.23x faster                                              |
| xml_etree_generate   | 55.5 ms                                                     | 50.4 ms: 1.10x faster                                              |
| xml_etree_parse      | 96.8 ms                                                     | 88.2 ms: 1.10x faster                                              |
| json_loads           | 14.0 us                                                     | 14.3 us: 1.02x slower                                              |
| Geometric mean       | (ref)                                                       | 1.24x faster                                                       |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.7 ms: 1.25x slower                                              |
| python_startup_no_site | 15.5 ms                                                     | 19.5 ms: 1.26x slower                                              |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.46 ms: 1.66x faster                                              |
| genshi_text     | 19.8 ms                                                     | 15.6 ms: 1.27x faster                                              |
| django_template | 28.9 ms                                                     | 24.2 ms: 1.19x faster                                              |
| genshi_xml      | 41.0 ms                                                     | 34.7 ms: 1.18x faster                                              |
| Geometric mean  | (ref)                                                       | 1.31x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 104 us: 3.23x faster                                               |
| async_tree_io            | 1.11 sec                                                    | 397 ms: 2.79x faster                                               |
| async_tree_none          | 435 ms                                                      | 170 ms: 2.56x faster                                               |
| async_tree_memoization   | 526 ms                                                      | 208 ms: 2.52x faster                                               |
| pathlib                  | 75.7 ms                                                     | 32.1 ms: 2.36x faster                                              |
| mdp                      | 1.78 sec                                                    | 802 ms: 2.22x faster                                               |
| deltablue                | 4.19 ms                                                     | 2.19 ms: 1.91x faster                                              |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 334 ms: 1.91x faster                                               |
| go                       | 139 ms                                                      | 77.7 ms: 1.79x faster                                              |
| pylint                   | 350 ms                                                      | 200 ms: 1.75x faster                                               |
| logging_silent           | 94.6 ns                                                     | 54.1 ns: 1.75x faster                                              |
| unpickle_pure_python     | 183 us                                                      | 108 us: 1.70x faster                                               |
| mako                     | 9.03 ms                                                     | 5.46 ms: 1.66x faster                                              |
| generators               | 32.4 ms                                                     | 19.6 ms: 1.65x faster                                              |
| richards_super           | 52.2 ms                                                     | 31.7 ms: 1.65x faster                                              |
| deepcopy_memo            | 28.8 us                                                     | 18.1 us: 1.59x faster                                              |
| pyflate                  | 409 ms                                                      | 259 ms: 1.58x faster                                               |
| comprehensions           | 16.5 us                                                     | 10.7 us: 1.55x faster                                              |
| richards                 | 42.4 ms                                                     | 27.6 ms: 1.54x faster                                              |
| raytrace                 | 273 ms                                                      | 181 ms: 1.51x faster                                               |
| chaos                    | 61.7 ms                                                     | 41.0 ms: 1.51x faster                                              |
| deepcopy                 | 255 us                                                      | 172 us: 1.49x faster                                               |
| json_dumps               | 9.16 ms                                                     | 6.19 ms: 1.48x faster                                              |
| tomli_loads              | 1.67 sec                                                    | 1.16 sec: 1.44x faster                                             |
| scimark_lu               | 85.8 ms                                                     | 60.4 ms: 1.42x faster                                              |
| scimark_monte_carlo      | 57.3 ms                                                     | 41.2 ms: 1.39x faster                                              |
| crypto_pyaes             | 62.5 ms                                                     | 45.5 ms: 1.37x faster                                              |
| float                    | 61.7 ms                                                     | 45.0 ms: 1.37x faster                                              |
| hexiom                   | 5.74 ms                                                     | 4.19 ms: 1.37x faster                                              |
| regex_compile            | 106 ms                                                      | 78.5 ms: 1.35x faster                                              |
| pycparser                | 930 ms                                                      | 694 ms: 1.34x faster                                               |
| scimark_sor              | 106 ms                                                      | 79.9 ms: 1.33x faster                                              |
| html5lib                 | 51.0 ms                                                     | 38.4 ms: 1.33x faster                                              |
| pprint_safe_repr         | 592 ms                                                      | 447 ms: 1.33x faster                                               |
| pprint_pformat           | 1.22 sec                                                    | 925 ms: 1.32x faster                                               |
| pickle_pure_python       | 270 us                                                      | 205 us: 1.31x faster                                               |
| nbody                    | 71.3 ms                                                     | 55.1 ms: 1.29x faster                                              |
| genshi_text              | 19.8 ms                                                     | 15.6 ms: 1.27x faster                                              |
| scimark_fft              | 187 ms                                                      | 151 ms: 1.24x faster                                               |
| thrift                   | 617 us                                                      | 499 us: 1.24x faster                                               |
| xml_etree_process        | 44.5 ms                                                     | 36.1 ms: 1.23x faster                                              |
| sqlite_synth             | 1.91 us                                                     | 1.56 us: 1.22x faster                                              |
| sympy_sum                | 107 ms                                                      | 87.9 ms: 1.22x faster                                              |
| dulwich_log              | 50.5 ms                                                     | 41.5 ms: 1.22x faster                                              |
| sympy_integrate          | 15.3 ms                                                     | 12.7 ms: 1.20x faster                                              |
| spectral_norm            | 77.3 ms                                                     | 64.1 ms: 1.20x faster                                              |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.26 ms: 1.20x faster                                              |
| fannkuch                 | 256 ms                                                      | 214 ms: 1.20x faster                                               |
| django_template          | 28.9 ms                                                     | 24.2 ms: 1.19x faster                                              |
| genshi_xml               | 41.0 ms                                                     | 34.7 ms: 1.18x faster                                              |
| deepcopy_reduce          | 2.20 us                                                     | 1.86 us: 1.18x faster                                              |
| docutils                 | 1.92 sec                                                    | 1.66 sec: 1.16x faster                                             |
| sympy_str                | 194 ms                                                      | 170 ms: 1.15x faster                                               |
| coroutines               | 16.0 ms                                                     | 14.1 ms: 1.13x faster                                              |
| regex_dna                | 136 ms                                                      | 121 ms: 1.12x faster                                               |
| nqueens                  | 66.6 ms                                                     | 59.5 ms: 1.12x faster                                              |
| 2to3                     | 246 ms                                                      | 222 ms: 1.11x faster                                               |
| xml_etree_generate       | 55.5 ms                                                     | 50.4 ms: 1.10x faster                                              |
| xml_etree_parse          | 96.8 ms                                                     | 88.2 ms: 1.10x faster                                              |
| regex_v8                 | 15.4 ms                                                     | 14.3 ms: 1.08x faster                                              |
| sympy_expand             | 314 ms                                                      | 292 ms: 1.08x faster                                               |
| meteor_contest           | 75.9 ms                                                     | 71.7 ms: 1.06x faster                                              |
| regex_effbot             | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                              |
| logging_format           | 6.76 us                                                     | 6.57 us: 1.03x faster                                              |
| pidigits                 | 149 ms                                                      | 146 ms: 1.02x faster                                               |
| logging_simple           | 6.22 us                                                     | 6.11 us: 1.02x faster                                              |
| json_loads               | 14.0 us                                                     | 14.3 us: 1.02x slower                                              |
| json                     | 3.14 ms                                                     | 3.25 ms: 1.04x slower                                              |
| telco                    | 3.94 ms                                                     | 4.29 ms: 1.09x slower                                              |
| async_generators         | 222 ms                                                      | 245 ms: 1.11x slower                                               |
| python_startup           | 20.6 ms                                                     | 25.7 ms: 1.25x slower                                              |
| python_startup_no_site   | 15.5 ms                                                     | 19.5 ms: 1.26x slower                                              |
| coverage                 | 39.0 ms                                                     | 50.1 ms: 1.29x slower                                              |
| gc_traversal             | 1.41 ms                                                     | 2.14 ms: 1.52x slower                                              |
| create_gc_cycles         | 800 us                                                      | 1.32 ms: 1.65x slower                                              |
| Geometric mean           | (ref)                                                       | 1.31x faster                                                       |

Benchmark hidden because not significant (1): xml_etree_iterparse
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250628-3.15.0a0-f528bf3-JIT/bm-20250628-pythonperf1-amd64-brandtbucher-jit_o2-3.15.0a0-f528bf3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.308x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: unknown