# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_os
- machine: windows-amd64
- commit hash: 33054dd
- commit date: 2025-06-28
- overall geometric mean: 1.303x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 219 ms: 1.12x faster                                               |
| docutils       | 1.92 sec                                                    | 1.65 sec: 1.16x faster                                             |
| html5lib       | 51.0 ms                                                     | 38.5 ms: 1.33x faster                                              |
| Geometric mean | (ref)                                                       | 1.20x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_os-3.15.0a0-33054dd |
|-------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 399 ms: 2.78x faster                                               |
| async_tree_none         | 435 ms                                                      | 171 ms: 2.54x faster                                               |
| async_tree_memoization  | 526 ms                                                      | 210 ms: 2.51x faster                                               |
| async_tree_cpu_io_mixed | 638 ms                                                      | 334 ms: 1.91x faster                                               |
| Geometric mean          | (ref)                                                       | 2.41x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 45.0 ms: 1.37x faster                                              |
| nbody          | 71.3 ms                                                     | 59.7 ms: 1.19x faster                                              |
| pidigits       | 149 ms                                                      | 146 ms: 1.02x faster                                               |
| Geometric mean | (ref)                                                       | 1.19x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 80.3 ms: 1.32x faster                                              |
| regex_dna      | 136 ms                                                      | 121 ms: 1.13x faster                                               |
| regex_v8       | 15.4 ms                                                     | 14.2 ms: 1.09x faster                                              |
| regex_effbot   | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                              |
| Geometric mean | (ref)                                                       | 1.14x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 108 us: 1.70x faster                                               |
| tomli_loads          | 1.67 sec                                                    | 1.14 sec: 1.46x faster                                             |
| json_dumps           | 9.16 ms                                                     | 6.29 ms: 1.46x faster                                              |
| pickle_pure_python   | 270 us                                                      | 205 us: 1.32x faster                                               |
| xml_etree_process    | 44.5 ms                                                     | 35.8 ms: 1.24x faster                                              |
| xml_etree_parse      | 96.8 ms                                                     | 89.0 ms: 1.09x faster                                              |
| json_loads           | 14.0 us                                                     | 14.6 us: 1.04x slower                                              |
| Geometric mean       | (ref)                                                       | 1.23x faster                                                       |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_os-3.15.0a0-33054dd |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.3 ms: 1.24x slower                                              |
| python_startup         | 20.6 ms                                                     | 26.0 ms: 1.26x slower                                              |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_os-3.15.0a0-33054dd |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.31 ms: 1.70x faster                                              |
| genshi_text     | 19.8 ms                                                     | 15.5 ms: 1.28x faster                                              |
| django_template | 28.9 ms                                                     | 24.2 ms: 1.20x faster                                              |
| genshi_xml      | 41.0 ms                                                     | 34.5 ms: 1.19x faster                                              |
| Geometric mean  | (ref)                                                       | 1.33x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_os-3.15.0a0-33054dd |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 105 us: 3.20x faster                                               |
| async_tree_io            | 1.11 sec                                                    | 399 ms: 2.78x faster                                               |
| async_tree_none          | 435 ms                                                      | 171 ms: 2.54x faster                                               |
| async_tree_memoization   | 526 ms                                                      | 210 ms: 2.51x faster                                               |
| pathlib                  | 75.7 ms                                                     | 31.7 ms: 2.38x faster                                              |
| mdp                      | 1.78 sec                                                    | 803 ms: 2.22x faster                                               |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 334 ms: 1.91x faster                                               |
| deltablue                | 4.19 ms                                                     | 2.22 ms: 1.89x faster                                              |
| go                       | 139 ms                                                      | 77.9 ms: 1.78x faster                                              |
| pylint                   | 350 ms                                                      | 201 ms: 1.74x faster                                               |
| logging_silent           | 94.6 ns                                                     | 55.3 ns: 1.71x faster                                              |
| unpickle_pure_python     | 183 us                                                      | 108 us: 1.70x faster                                               |
| mako                     | 9.03 ms                                                     | 5.31 ms: 1.70x faster                                              |
| richards_super           | 52.2 ms                                                     | 30.9 ms: 1.69x faster                                              |
| generators               | 32.4 ms                                                     | 19.7 ms: 1.64x faster                                              |
| pyflate                  | 409 ms                                                      | 255 ms: 1.61x faster                                               |
| comprehensions           | 16.5 us                                                     | 10.6 us: 1.56x faster                                              |
| richards                 | 42.4 ms                                                     | 27.2 ms: 1.56x faster                                              |
| deepcopy_memo            | 28.8 us                                                     | 18.5 us: 1.56x faster                                              |
| raytrace                 | 273 ms                                                      | 179 ms: 1.53x faster                                               |
| deepcopy                 | 255 us                                                      | 171 us: 1.50x faster                                               |
| chaos                    | 61.7 ms                                                     | 41.2 ms: 1.50x faster                                              |
| tomli_loads              | 1.67 sec                                                    | 1.14 sec: 1.46x faster                                             |
| json_dumps               | 9.16 ms                                                     | 6.29 ms: 1.46x faster                                              |
| scimark_lu               | 85.8 ms                                                     | 60.2 ms: 1.42x faster                                              |
| hexiom                   | 5.74 ms                                                     | 4.13 ms: 1.39x faster                                              |
| float                    | 61.7 ms                                                     | 45.0 ms: 1.37x faster                                              |
| crypto_pyaes             | 62.5 ms                                                     | 46.0 ms: 1.36x faster                                              |
| scimark_monte_carlo      | 57.3 ms                                                     | 42.6 ms: 1.35x faster                                              |
| scimark_sor              | 106 ms                                                      | 78.9 ms: 1.35x faster                                              |
| pycparser                | 930 ms                                                      | 698 ms: 1.33x faster                                               |
| pprint_pformat           | 1.22 sec                                                    | 918 ms: 1.33x faster                                               |
| html5lib                 | 51.0 ms                                                     | 38.5 ms: 1.33x faster                                              |
| regex_compile            | 106 ms                                                      | 80.3 ms: 1.32x faster                                              |
| pickle_pure_python       | 270 us                                                      | 205 us: 1.32x faster                                               |
| pprint_safe_repr         | 592 ms                                                      | 460 ms: 1.29x faster                                               |
| genshi_text              | 19.8 ms                                                     | 15.5 ms: 1.28x faster                                              |
| xml_etree_process        | 44.5 ms                                                     | 35.8 ms: 1.24x faster                                              |
| scimark_fft              | 187 ms                                                      | 151 ms: 1.24x faster                                               |
| dulwich_log              | 50.5 ms                                                     | 40.9 ms: 1.23x faster                                              |
| thrift                   | 617 us                                                      | 507 us: 1.22x faster                                               |
| sqlite_synth             | 1.91 us                                                     | 1.57 us: 1.22x faster                                              |
| sympy_sum                | 107 ms                                                      | 88.3 ms: 1.21x faster                                              |
| spectral_norm            | 77.3 ms                                                     | 64.3 ms: 1.20x faster                                              |
| sympy_integrate          | 15.3 ms                                                     | 12.8 ms: 1.20x faster                                              |
| django_template          | 28.9 ms                                                     | 24.2 ms: 1.20x faster                                              |
| nbody                    | 71.3 ms                                                     | 59.7 ms: 1.19x faster                                              |
| deepcopy_reduce          | 2.20 us                                                     | 1.85 us: 1.19x faster                                              |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.29 ms: 1.19x faster                                              |
| genshi_xml               | 41.0 ms                                                     | 34.5 ms: 1.19x faster                                              |
| fannkuch                 | 256 ms                                                      | 216 ms: 1.18x faster                                               |
| docutils                 | 1.92 sec                                                    | 1.65 sec: 1.16x faster                                             |
| sympy_str                | 194 ms                                                      | 171 ms: 1.14x faster                                               |
| regex_dna                | 136 ms                                                      | 121 ms: 1.13x faster                                               |
| coroutines               | 16.0 ms                                                     | 14.2 ms: 1.12x faster                                              |
| 2to3                     | 246 ms                                                      | 219 ms: 1.12x faster                                               |
| nqueens                  | 66.6 ms                                                     | 60.8 ms: 1.10x faster                                              |
| regex_v8                 | 15.4 ms                                                     | 14.2 ms: 1.09x faster                                              |
| xml_etree_parse          | 96.8 ms                                                     | 89.0 ms: 1.09x faster                                              |
| meteor_contest           | 75.9 ms                                                     | 70.4 ms: 1.08x faster                                              |
| sympy_expand             | 314 ms                                                      | 296 ms: 1.06x faster                                               |
| regex_effbot             | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                              |
| logging_format           | 6.76 us                                                     | 6.63 us: 1.02x faster                                              |
| pidigits                 | 149 ms                                                      | 146 ms: 1.02x faster                                               |
| json                     | 3.14 ms                                                     | 3.17 ms: 1.01x slower                                              |
| json_loads               | 14.0 us                                                     | 14.6 us: 1.04x slower                                              |
| telco                    | 3.94 ms                                                     | 4.29 ms: 1.09x slower                                              |
| async_generators         | 222 ms                                                      | 250 ms: 1.13x slower                                               |
| python_startup_no_site   | 15.5 ms                                                     | 19.3 ms: 1.24x slower                                              |
| python_startup           | 20.6 ms                                                     | 26.0 ms: 1.26x slower                                              |
| coverage                 | 39.0 ms                                                     | 50.3 ms: 1.29x slower                                              |
| gc_traversal             | 1.41 ms                                                     | 2.14 ms: 1.52x slower                                              |
| create_gc_cycles         | 800 us                                                      | 1.33 ms: 1.66x slower                                              |
| Geometric mean           | (ref)                                                       | 1.31x faster                                                       |

Benchmark hidden because not significant (3): xml_etree_generate, xml_etree_iterparse, logging_simple
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250628-3.15.0a0-33054dd-JIT/bm-20250628-pythonperf1-amd64-brandtbucher-jit_os-3.15.0a0-33054dd.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.303x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: unknown