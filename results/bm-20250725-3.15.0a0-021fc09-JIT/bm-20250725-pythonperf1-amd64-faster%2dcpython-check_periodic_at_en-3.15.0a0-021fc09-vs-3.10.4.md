# Results vs. 3.10.4

- fork: faster-cpython
- ref: check_periodic_at_en
- machine: windows-amd64
- commit hash: 021fc09
- commit date: 2025-07-25
- overall geometric mean: 1.302x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 222 ms: 1.11x faster                                                                 |
| docutils       | 1.92 sec                                                    | 1.65 sec: 1.16x faster                                                               |
| html5lib       | 51.0 ms                                                     | 38.8 ms: 1.32x faster                                                                |
| Geometric mean | (ref)                                                       | 1.19x faster                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|-------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 393 ms: 2.82x faster                                                                 |
| async_tree_memoization  | 526 ms                                                      | 214 ms: 2.46x faster                                                                 |
| async_tree_none         | 435 ms                                                      | 180 ms: 2.42x faster                                                                 |
| async_tree_cpu_io_mixed | 638 ms                                                      | 337 ms: 1.90x faster                                                                 |
| Geometric mean          | (ref)                                                       | 2.37x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 44.5 ms: 1.39x faster                                                                |
| nbody          | 71.3 ms                                                     | 55.8 ms: 1.28x faster                                                                |
| Geometric mean | (ref)                                                       | 1.21x faster                                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 78.7 ms: 1.35x faster                                                                |
| regex_dna      | 136 ms                                                      | 119 ms: 1.14x faster                                                                 |
| regex_v8       | 15.4 ms                                                     | 14.1 ms: 1.10x faster                                                                |
| regex_effbot   | 1.66 ms                                                     | 1.61 ms: 1.03x faster                                                                |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 113 us: 1.62x faster                                                                 |
| tomli_loads          | 1.67 sec                                                    | 1.11 sec: 1.50x faster                                                               |
| json_dumps           | 9.16 ms                                                     | 6.30 ms: 1.45x faster                                                                |
| pickle_pure_python   | 270 us                                                      | 207 us: 1.30x faster                                                                 |
| xml_etree_process    | 44.5 ms                                                     | 36.2 ms: 1.23x faster                                                                |
| xml_etree_generate   | 55.5 ms                                                     | 51.4 ms: 1.08x faster                                                                |
| xml_etree_parse      | 96.8 ms                                                     | 91.1 ms: 1.06x faster                                                                |
| xml_etree_iterparse  | 65.0 ms                                                     | 66.7 ms: 1.03x slower                                                                |
| json_loads           | 14.0 us                                                     | 14.8 us: 1.06x slower                                                                |
| Geometric mean       | (ref)                                                       | 1.22x faster                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.9 ms: 1.28x slower                                                                |
| python_startup         | 20.6 ms                                                     | 26.7 ms: 1.29x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.29x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.51 ms: 1.64x faster                                                                |
| genshi_text     | 19.8 ms                                                     | 15.7 ms: 1.26x faster                                                                |
| django_template | 28.9 ms                                                     | 24.1 ms: 1.20x faster                                                                |
| genshi_xml      | 41.0 ms                                                     | 35.1 ms: 1.17x faster                                                                |
| Geometric mean  | (ref)                                                       | 1.31x faster                                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 105 us: 3.21x faster                                                                 |
| async_tree_io            | 1.11 sec                                                    | 393 ms: 2.82x faster                                                                 |
| async_tree_memoization   | 526 ms                                                      | 214 ms: 2.46x faster                                                                 |
| async_tree_none          | 435 ms                                                      | 180 ms: 2.42x faster                                                                 |
| pathlib                  | 75.7 ms                                                     | 33.2 ms: 2.28x faster                                                                |
| mdp                      | 1.78 sec                                                    | 823 ms: 2.16x faster                                                                 |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 337 ms: 1.90x faster                                                                 |
| deltablue                | 4.19 ms                                                     | 2.28 ms: 1.83x faster                                                                |
| go                       | 139 ms                                                      | 78.8 ms: 1.76x faster                                                                |
| pylint                   | 350 ms                                                      | 203 ms: 1.73x faster                                                                 |
| logging_silent           | 94.6 ns                                                     | 55.6 ns: 1.70x faster                                                                |
| richards_super           | 52.2 ms                                                     | 30.8 ms: 1.70x faster                                                                |
| mako                     | 9.03 ms                                                     | 5.51 ms: 1.64x faster                                                                |
| generators               | 32.4 ms                                                     | 19.8 ms: 1.64x faster                                                                |
| unpickle_pure_python     | 183 us                                                      | 113 us: 1.62x faster                                                                 |
| deepcopy_memo            | 28.8 us                                                     | 18.0 us: 1.60x faster                                                                |
| pyflate                  | 409 ms                                                      | 257 ms: 1.59x faster                                                                 |
| comprehensions           | 16.5 us                                                     | 10.5 us: 1.57x faster                                                                |
| raytrace                 | 273 ms                                                      | 177 ms: 1.55x faster                                                                 |
| richards                 | 42.4 ms                                                     | 27.5 ms: 1.55x faster                                                                |
| tomli_loads              | 1.67 sec                                                    | 1.11 sec: 1.50x faster                                                               |
| deepcopy                 | 255 us                                                      | 170 us: 1.50x faster                                                                 |
| chaos                    | 61.7 ms                                                     | 41.6 ms: 1.48x faster                                                                |
| json_dumps               | 9.16 ms                                                     | 6.30 ms: 1.45x faster                                                                |
| scimark_lu               | 85.8 ms                                                     | 60.6 ms: 1.41x faster                                                                |
| float                    | 61.7 ms                                                     | 44.5 ms: 1.39x faster                                                                |
| hexiom                   | 5.74 ms                                                     | 4.16 ms: 1.38x faster                                                                |
| scimark_monte_carlo      | 57.3 ms                                                     | 41.8 ms: 1.37x faster                                                                |
| pprint_pformat           | 1.22 sec                                                    | 896 ms: 1.36x faster                                                                 |
| scimark_sor              | 106 ms                                                      | 78.5 ms: 1.35x faster                                                                |
| regex_compile            | 106 ms                                                      | 78.7 ms: 1.35x faster                                                                |
| crypto_pyaes             | 62.5 ms                                                     | 46.6 ms: 1.34x faster                                                                |
| pycparser                | 930 ms                                                      | 701 ms: 1.33x faster                                                                 |
| html5lib                 | 51.0 ms                                                     | 38.8 ms: 1.32x faster                                                                |
| pickle_pure_python       | 270 us                                                      | 207 us: 1.30x faster                                                                 |
| pprint_safe_repr         | 592 ms                                                      | 454 ms: 1.30x faster                                                                 |
| nbody                    | 71.3 ms                                                     | 55.8 ms: 1.28x faster                                                                |
| genshi_text              | 19.8 ms                                                     | 15.7 ms: 1.26x faster                                                                |
| thrift                   | 617 us                                                      | 490 us: 1.26x faster                                                                 |
| scimark_fft              | 187 ms                                                      | 151 ms: 1.24x faster                                                                 |
| xml_etree_process        | 44.5 ms                                                     | 36.2 ms: 1.23x faster                                                                |
| sympy_sum                | 107 ms                                                      | 87.7 ms: 1.22x faster                                                                |
| sqlite_synth             | 1.91 us                                                     | 1.58 us: 1.21x faster                                                                |
| dulwich_log              | 50.5 ms                                                     | 42.0 ms: 1.20x faster                                                                |
| django_template          | 28.9 ms                                                     | 24.1 ms: 1.20x faster                                                                |
| sympy_integrate          | 15.3 ms                                                     | 12.8 ms: 1.19x faster                                                                |
| deepcopy_reduce          | 2.20 us                                                     | 1.85 us: 1.19x faster                                                                |
| fannkuch                 | 256 ms                                                      | 217 ms: 1.18x faster                                                                 |
| genshi_xml               | 41.0 ms                                                     | 35.1 ms: 1.17x faster                                                                |
| docutils                 | 1.92 sec                                                    | 1.65 sec: 1.16x faster                                                               |
| regex_dna                | 136 ms                                                      | 119 ms: 1.14x faster                                                                 |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.39 ms: 1.14x faster                                                                |
| sympy_str                | 194 ms                                                      | 172 ms: 1.13x faster                                                                 |
| spectral_norm            | 77.3 ms                                                     | 68.8 ms: 1.12x faster                                                                |
| 2to3                     | 246 ms                                                      | 222 ms: 1.11x faster                                                                 |
| coroutines               | 16.0 ms                                                     | 14.5 ms: 1.11x faster                                                                |
| nqueens                  | 66.6 ms                                                     | 60.4 ms: 1.10x faster                                                                |
| regex_v8                 | 15.4 ms                                                     | 14.1 ms: 1.10x faster                                                                |
| xml_etree_generate       | 55.5 ms                                                     | 51.4 ms: 1.08x faster                                                                |
| sympy_expand             | 314 ms                                                      | 294 ms: 1.07x faster                                                                 |
| xml_etree_parse          | 96.8 ms                                                     | 91.1 ms: 1.06x faster                                                                |
| json                     | 3.14 ms                                                     | 3.02 ms: 1.04x faster                                                                |
| regex_effbot             | 1.66 ms                                                     | 1.61 ms: 1.03x faster                                                                |
| meteor_contest           | 75.9 ms                                                     | 74.0 ms: 1.03x faster                                                                |
| xml_etree_iterparse      | 65.0 ms                                                     | 66.7 ms: 1.03x slower                                                                |
| json_loads               | 14.0 us                                                     | 14.8 us: 1.06x slower                                                                |
| telco                    | 3.94 ms                                                     | 4.30 ms: 1.09x slower                                                                |
| async_generators         | 222 ms                                                      | 252 ms: 1.14x slower                                                                 |
| python_startup_no_site   | 15.5 ms                                                     | 19.9 ms: 1.28x slower                                                                |
| python_startup           | 20.6 ms                                                     | 26.7 ms: 1.29x slower                                                                |
| coverage                 | 39.0 ms                                                     | 50.9 ms: 1.31x slower                                                                |
| gc_traversal             | 1.41 ms                                                     | 2.17 ms: 1.54x slower                                                                |
| create_gc_cycles         | 800 us                                                      | 1.34 ms: 1.68x slower                                                                |
| Geometric mean           | (ref)                                                       | 1.30x faster                                                                         |

Benchmark hidden because not significant (3): logging_simple, logging_format, pidigits
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250725-3.15.0a0-021fc09-JIT/bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.302x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: unknown