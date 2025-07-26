# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_shim
- machine: windows-amd64
- commit hash: a6ef3b7
- commit date: 2025-07-25
- overall geometric mean: 1.300x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 223 ms: 1.10x faster                                                 |
| docutils       | 1.92 sec                                                    | 1.66 sec: 1.16x faster                                               |
| html5lib       | 51.0 ms                                                     | 39.2 ms: 1.30x faster                                                |
| Geometric mean | (ref)                                                       | 1.18x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 389 ms: 2.85x faster                                                 |
| async_tree_none         | 435 ms                                                      | 176 ms: 2.47x faster                                                 |
| async_tree_memoization  | 526 ms                                                      | 216 ms: 2.43x faster                                                 |
| async_tree_cpu_io_mixed | 638 ms                                                      | 344 ms: 1.85x faster                                                 |
| Geometric mean          | (ref)                                                       | 2.37x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 43.9 ms: 1.40x faster                                                |
| nbody          | 71.3 ms                                                     | 57.0 ms: 1.25x faster                                                |
| Geometric mean | (ref)                                                       | 1.21x faster                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 82.5 ms: 1.29x faster                                                |
| regex_dna      | 136 ms                                                      | 120 ms: 1.13x faster                                                 |
| regex_v8       | 15.4 ms                                                     | 14.4 ms: 1.07x faster                                                |
| Geometric mean | (ref)                                                       | 1.12x faster                                                         |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 109 us: 1.67x faster                                                 |
| tomli_loads          | 1.67 sec                                                    | 1.12 sec: 1.49x faster                                               |
| json_dumps           | 9.16 ms                                                     | 6.30 ms: 1.46x faster                                                |
| pickle_pure_python   | 270 us                                                      | 211 us: 1.28x faster                                                 |
| xml_etree_process    | 44.5 ms                                                     | 36.0 ms: 1.24x faster                                                |
| xml_etree_generate   | 55.5 ms                                                     | 51.4 ms: 1.08x faster                                                |
| xml_etree_parse      | 96.8 ms                                                     | 89.8 ms: 1.08x faster                                                |
| json_loads           | 14.0 us                                                     | 14.4 us: 1.03x slower                                                |
| Geometric mean       | (ref)                                                       | 1.23x faster                                                         |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 20.1 ms: 1.30x slower                                                |
| python_startup         | 20.6 ms                                                     | 27.1 ms: 1.32x slower                                                |
| Geometric mean         | (ref)                                                       | 1.31x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.33 ms: 1.69x faster                                                |
| genshi_text     | 19.8 ms                                                     | 15.8 ms: 1.26x faster                                                |
| django_template | 28.9 ms                                                     | 24.8 ms: 1.16x faster                                                |
| genshi_xml      | 41.0 ms                                                     | 35.6 ms: 1.15x faster                                                |
| Geometric mean  | (ref)                                                       | 1.30x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 108 us: 3.12x faster                                                 |
| async_tree_io            | 1.11 sec                                                    | 389 ms: 2.85x faster                                                 |
| async_tree_none          | 435 ms                                                      | 176 ms: 2.47x faster                                                 |
| async_tree_memoization   | 526 ms                                                      | 216 ms: 2.43x faster                                                 |
| pathlib                  | 75.7 ms                                                     | 33.1 ms: 2.29x faster                                                |
| mdp                      | 1.78 sec                                                    | 802 ms: 2.22x faster                                                 |
| deltablue                | 4.19 ms                                                     | 2.19 ms: 1.91x faster                                                |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 344 ms: 1.85x faster                                                 |
| go                       | 139 ms                                                      | 78.8 ms: 1.76x faster                                                |
| pylint                   | 350 ms                                                      | 199 ms: 1.76x faster                                                 |
| mako                     | 9.03 ms                                                     | 5.33 ms: 1.69x faster                                                |
| logging_silent           | 94.6 ns                                                     | 56.1 ns: 1.69x faster                                                |
| richards_super           | 52.2 ms                                                     | 31.0 ms: 1.69x faster                                                |
| unpickle_pure_python     | 183 us                                                      | 109 us: 1.67x faster                                                 |
| pyflate                  | 409 ms                                                      | 252 ms: 1.63x faster                                                 |
| deepcopy_memo            | 28.8 us                                                     | 17.8 us: 1.62x faster                                                |
| generators               | 32.4 ms                                                     | 20.0 ms: 1.62x faster                                                |
| comprehensions           | 16.5 us                                                     | 10.4 us: 1.58x faster                                                |
| chaos                    | 61.7 ms                                                     | 40.1 ms: 1.54x faster                                                |
| richards                 | 42.4 ms                                                     | 27.7 ms: 1.53x faster                                                |
| deepcopy                 | 255 us                                                      | 168 us: 1.52x faster                                                 |
| raytrace                 | 273 ms                                                      | 181 ms: 1.51x faster                                                 |
| tomli_loads              | 1.67 sec                                                    | 1.12 sec: 1.49x faster                                               |
| json_dumps               | 9.16 ms                                                     | 6.30 ms: 1.46x faster                                                |
| scimark_lu               | 85.8 ms                                                     | 59.9 ms: 1.43x faster                                                |
| float                    | 61.7 ms                                                     | 43.9 ms: 1.40x faster                                                |
| hexiom                   | 5.74 ms                                                     | 4.11 ms: 1.40x faster                                                |
| crypto_pyaes             | 62.5 ms                                                     | 45.7 ms: 1.37x faster                                                |
| scimark_sor              | 106 ms                                                      | 77.7 ms: 1.37x faster                                                |
| scimark_monte_carlo      | 57.3 ms                                                     | 42.2 ms: 1.36x faster                                                |
| pprint_pformat           | 1.22 sec                                                    | 911 ms: 1.34x faster                                                 |
| pycparser                | 930 ms                                                      | 702 ms: 1.33x faster                                                 |
| pprint_safe_repr         | 592 ms                                                      | 451 ms: 1.31x faster                                                 |
| html5lib                 | 51.0 ms                                                     | 39.2 ms: 1.30x faster                                                |
| regex_compile            | 106 ms                                                      | 82.5 ms: 1.29x faster                                                |
| pickle_pure_python       | 270 us                                                      | 211 us: 1.28x faster                                                 |
| genshi_text              | 19.8 ms                                                     | 15.8 ms: 1.26x faster                                                |
| nbody                    | 71.3 ms                                                     | 57.0 ms: 1.25x faster                                                |
| sqlite_synth             | 1.91 us                                                     | 1.55 us: 1.24x faster                                                |
| xml_etree_process        | 44.5 ms                                                     | 36.0 ms: 1.24x faster                                                |
| thrift                   | 617 us                                                      | 505 us: 1.22x faster                                                 |
| dulwich_log              | 50.5 ms                                                     | 41.4 ms: 1.22x faster                                                |
| deepcopy_reduce          | 2.20 us                                                     | 1.81 us: 1.22x faster                                                |
| scimark_fft              | 187 ms                                                      | 154 ms: 1.21x faster                                                 |
| spectral_norm            | 77.3 ms                                                     | 65.5 ms: 1.18x faster                                                |
| fannkuch                 | 256 ms                                                      | 217 ms: 1.18x faster                                                 |
| sympy_sum                | 107 ms                                                      | 91.4 ms: 1.17x faster                                                |
| django_template          | 28.9 ms                                                     | 24.8 ms: 1.16x faster                                                |
| docutils                 | 1.92 sec                                                    | 1.66 sec: 1.16x faster                                               |
| genshi_xml               | 41.0 ms                                                     | 35.6 ms: 1.15x faster                                                |
| sympy_integrate          | 15.3 ms                                                     | 13.4 ms: 1.14x faster                                                |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.40 ms: 1.14x faster                                                |
| regex_dna                | 136 ms                                                      | 120 ms: 1.13x faster                                                 |
| sympy_str                | 194 ms                                                      | 173 ms: 1.12x faster                                                 |
| nqueens                  | 66.6 ms                                                     | 60.2 ms: 1.11x faster                                                |
| 2to3                     | 246 ms                                                      | 223 ms: 1.10x faster                                                 |
| xml_etree_generate       | 55.5 ms                                                     | 51.4 ms: 1.08x faster                                                |
| xml_etree_parse          | 96.8 ms                                                     | 89.8 ms: 1.08x faster                                                |
| coroutines               | 16.0 ms                                                     | 14.9 ms: 1.08x faster                                                |
| regex_v8                 | 15.4 ms                                                     | 14.4 ms: 1.07x faster                                                |
| json                     | 3.14 ms                                                     | 2.93 ms: 1.07x faster                                                |
| sympy_expand             | 314 ms                                                      | 300 ms: 1.05x faster                                                 |
| meteor_contest           | 75.9 ms                                                     | 73.8 ms: 1.03x faster                                                |
| logging_simple           | 6.22 us                                                     | 6.06 us: 1.03x faster                                                |
| json_loads               | 14.0 us                                                     | 14.4 us: 1.03x slower                                                |
| telco                    | 3.94 ms                                                     | 4.33 ms: 1.10x slower                                                |
| async_generators         | 222 ms                                                      | 248 ms: 1.12x slower                                                 |
| python_startup_no_site   | 15.5 ms                                                     | 20.1 ms: 1.30x slower                                                |
| coverage                 | 39.0 ms                                                     | 51.2 ms: 1.31x slower                                                |
| python_startup           | 20.6 ms                                                     | 27.1 ms: 1.32x slower                                                |
| gc_traversal             | 1.41 ms                                                     | 2.24 ms: 1.59x slower                                                |
| create_gc_cycles         | 800 us                                                      | 1.39 ms: 1.74x slower                                                |
| Geometric mean           | (ref)                                                       | 1.30x faster                                                         |

Benchmark hidden because not significant (4): logging_format, xml_etree_iterparse, pidigits, regex_effbot
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250725-3.15.0a0-a6ef3b7-JIT/bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.300x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: unknown