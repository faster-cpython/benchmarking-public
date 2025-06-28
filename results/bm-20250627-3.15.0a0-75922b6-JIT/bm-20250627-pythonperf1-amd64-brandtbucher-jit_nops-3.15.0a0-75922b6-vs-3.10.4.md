# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_nops
- machine: windows-amd64
- commit hash: 75922b6
- commit date: 2025-06-27
- overall geometric mean: 1.305x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250627-pythonperf1-amd64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 220 ms: 1.12x faster                                                 |
| docutils       | 1.92 sec                                                    | 1.67 sec: 1.15x faster                                               |
| html5lib       | 51.0 ms                                                     | 38.5 ms: 1.33x faster                                                |
| Geometric mean | (ref)                                                       | 1.19x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250627-pythonperf1-amd64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 393 ms: 2.82x faster                                                 |
| async_tree_none         | 435 ms                                                      | 171 ms: 2.55x faster                                                 |
| async_tree_memoization  | 526 ms                                                      | 207 ms: 2.54x faster                                                 |
| async_tree_cpu_io_mixed | 638 ms                                                      | 331 ms: 1.93x faster                                                 |
| Geometric mean          | (ref)                                                       | 2.43x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250627-pythonperf1-amd64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 45.5 ms: 1.36x faster                                                |
| nbody          | 71.3 ms                                                     | 54.3 ms: 1.31x faster                                                |
| pidigits       | 149 ms                                                      | 145 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                       | 1.22x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250627-pythonperf1-amd64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 78.8 ms: 1.35x faster                                                |
| regex_dna      | 136 ms                                                      | 115 ms: 1.18x faster                                                 |
| regex_v8       | 15.4 ms                                                     | 13.9 ms: 1.11x faster                                                |
| regex_effbot   | 1.66 ms                                                     | 1.54 ms: 1.07x faster                                                |
| Geometric mean | (ref)                                                       | 1.17x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250627-pythonperf1-amd64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 107 us: 1.70x faster                                                 |
| tomli_loads          | 1.67 sec                                                    | 1.14 sec: 1.46x faster                                               |
| json_dumps           | 9.16 ms                                                     | 6.55 ms: 1.40x faster                                                |
| pickle_pure_python   | 270 us                                                      | 209 us: 1.29x faster                                                 |
| xml_etree_process    | 44.5 ms                                                     | 35.9 ms: 1.24x faster                                                |
| xml_etree_generate   | 55.5 ms                                                     | 50.4 ms: 1.10x faster                                                |
| xml_etree_parse      | 96.8 ms                                                     | 88.4 ms: 1.09x faster                                                |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.2 ms: 1.03x faster                                                |
| json_loads           | 14.0 us                                                     | 14.4 us: 1.03x slower                                                |
| Geometric mean       | (ref)                                                       | 1.24x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250627-pythonperf1-amd64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.4 ms: 1.25x slower                                                |
| python_startup         | 20.6 ms                                                     | 25.9 ms: 1.26x slower                                                |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250627-pythonperf1-amd64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.38 ms: 1.68x faster                                                |
| genshi_text     | 19.8 ms                                                     | 15.6 ms: 1.27x faster                                                |
| genshi_xml      | 41.0 ms                                                     | 34.3 ms: 1.20x faster                                                |
| django_template | 28.9 ms                                                     | 24.3 ms: 1.19x faster                                                |
| Geometric mean  | (ref)                                                       | 1.32x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250627-pythonperf1-amd64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 104 us: 3.23x faster                                                 |
| async_tree_io            | 1.11 sec                                                    | 393 ms: 2.82x faster                                                 |
| async_tree_none          | 435 ms                                                      | 171 ms: 2.55x faster                                                 |
| async_tree_memoization   | 526 ms                                                      | 207 ms: 2.54x faster                                                 |
| pathlib                  | 75.7 ms                                                     | 32.0 ms: 2.37x faster                                                |
| mdp                      | 1.78 sec                                                    | 804 ms: 2.21x faster                                                 |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 331 ms: 1.93x faster                                                 |
| deltablue                | 4.19 ms                                                     | 2.23 ms: 1.88x faster                                                |
| go                       | 139 ms                                                      | 78.6 ms: 1.77x faster                                                |
| pylint                   | 350 ms                                                      | 199 ms: 1.76x faster                                                 |
| logging_silent           | 94.6 ns                                                     | 55.0 ns: 1.72x faster                                                |
| unpickle_pure_python     | 183 us                                                      | 107 us: 1.70x faster                                                 |
| richards_super           | 52.2 ms                                                     | 30.9 ms: 1.69x faster                                                |
| mako                     | 9.03 ms                                                     | 5.38 ms: 1.68x faster                                                |
| generators               | 32.4 ms                                                     | 19.6 ms: 1.65x faster                                                |
| pyflate                  | 409 ms                                                      | 258 ms: 1.58x faster                                                 |
| deepcopy_memo            | 28.8 us                                                     | 18.2 us: 1.58x faster                                                |
| richards                 | 42.4 ms                                                     | 27.1 ms: 1.56x faster                                                |
| comprehensions           | 16.5 us                                                     | 10.6 us: 1.56x faster                                                |
| raytrace                 | 273 ms                                                      | 180 ms: 1.52x faster                                                 |
| deepcopy                 | 255 us                                                      | 169 us: 1.51x faster                                                 |
| chaos                    | 61.7 ms                                                     | 41.6 ms: 1.48x faster                                                |
| tomli_loads              | 1.67 sec                                                    | 1.14 sec: 1.46x faster                                               |
| scimark_lu               | 85.8 ms                                                     | 60.9 ms: 1.41x faster                                                |
| json_dumps               | 9.16 ms                                                     | 6.55 ms: 1.40x faster                                                |
| scimark_monte_carlo      | 57.3 ms                                                     | 41.5 ms: 1.38x faster                                                |
| float                    | 61.7 ms                                                     | 45.5 ms: 1.36x faster                                                |
| hexiom                   | 5.74 ms                                                     | 4.24 ms: 1.35x faster                                                |
| crypto_pyaes             | 62.5 ms                                                     | 46.4 ms: 1.35x faster                                                |
| regex_compile            | 106 ms                                                      | 78.8 ms: 1.35x faster                                                |
| pycparser                | 930 ms                                                      | 700 ms: 1.33x faster                                                 |
| html5lib                 | 51.0 ms                                                     | 38.5 ms: 1.33x faster                                                |
| nbody                    | 71.3 ms                                                     | 54.3 ms: 1.31x faster                                                |
| scimark_sor              | 106 ms                                                      | 81.1 ms: 1.31x faster                                                |
| pprint_pformat           | 1.22 sec                                                    | 936 ms: 1.30x faster                                                 |
| pickle_pure_python       | 270 us                                                      | 209 us: 1.29x faster                                                 |
| pprint_safe_repr         | 592 ms                                                      | 459 ms: 1.29x faster                                                 |
| genshi_text              | 19.8 ms                                                     | 15.6 ms: 1.27x faster                                                |
| thrift                   | 617 us                                                      | 490 us: 1.26x faster                                                 |
| xml_etree_process        | 44.5 ms                                                     | 35.9 ms: 1.24x faster                                                |
| scimark_fft              | 187 ms                                                      | 152 ms: 1.23x faster                                                 |
| dulwich_log              | 50.5 ms                                                     | 41.1 ms: 1.23x faster                                                |
| sympy_sum                | 107 ms                                                      | 87.9 ms: 1.22x faster                                                |
| sqlite_synth             | 1.91 us                                                     | 1.58 us: 1.21x faster                                                |
| deepcopy_reduce          | 2.20 us                                                     | 1.83 us: 1.21x faster                                                |
| genshi_xml               | 41.0 ms                                                     | 34.3 ms: 1.20x faster                                                |
| sympy_integrate          | 15.3 ms                                                     | 12.8 ms: 1.19x faster                                                |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.29 ms: 1.19x faster                                                |
| django_template          | 28.9 ms                                                     | 24.3 ms: 1.19x faster                                                |
| regex_dna                | 136 ms                                                      | 115 ms: 1.18x faster                                                 |
| spectral_norm            | 77.3 ms                                                     | 65.9 ms: 1.17x faster                                                |
| docutils                 | 1.92 sec                                                    | 1.67 sec: 1.15x faster                                               |
| sympy_str                | 194 ms                                                      | 171 ms: 1.14x faster                                                 |
| fannkuch                 | 256 ms                                                      | 227 ms: 1.13x faster                                                 |
| 2to3                     | 246 ms                                                      | 220 ms: 1.12x faster                                                 |
| regex_v8                 | 15.4 ms                                                     | 13.9 ms: 1.11x faster                                                |
| nqueens                  | 66.6 ms                                                     | 60.0 ms: 1.11x faster                                                |
| xml_etree_generate       | 55.5 ms                                                     | 50.4 ms: 1.10x faster                                                |
| xml_etree_parse          | 96.8 ms                                                     | 88.4 ms: 1.09x faster                                                |
| regex_effbot             | 1.66 ms                                                     | 1.54 ms: 1.07x faster                                                |
| sympy_expand             | 314 ms                                                      | 295 ms: 1.07x faster                                                 |
| coroutines               | 16.0 ms                                                     | 15.2 ms: 1.05x faster                                                |
| meteor_contest           | 75.9 ms                                                     | 72.6 ms: 1.05x faster                                                |
| json                     | 3.14 ms                                                     | 3.05 ms: 1.03x faster                                                |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.2 ms: 1.03x faster                                                |
| pidigits                 | 149 ms                                                      | 145 ms: 1.03x faster                                                 |
| logging_format           | 6.76 us                                                     | 6.66 us: 1.01x faster                                                |
| json_loads               | 14.0 us                                                     | 14.4 us: 1.03x slower                                                |
| telco                    | 3.94 ms                                                     | 4.29 ms: 1.09x slower                                                |
| async_generators         | 222 ms                                                      | 250 ms: 1.13x slower                                                 |
| python_startup_no_site   | 15.5 ms                                                     | 19.4 ms: 1.25x slower                                                |
| python_startup           | 20.6 ms                                                     | 25.9 ms: 1.26x slower                                                |
| coverage                 | 39.0 ms                                                     | 50.6 ms: 1.30x slower                                                |
| gc_traversal             | 1.41 ms                                                     | 2.16 ms: 1.53x slower                                                |
| create_gc_cycles         | 800 us                                                      | 1.34 ms: 1.67x slower                                                |
| Geometric mean           | (ref)                                                       | 1.31x faster                                                         |

Benchmark hidden because not significant (1): logging_simple
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250627-3.15.0a0-75922b6-JIT/bm-20250627-pythonperf1-amd64-brandtbucher-jit_nops-3.15.0a0-75922b6.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.305x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: unknown