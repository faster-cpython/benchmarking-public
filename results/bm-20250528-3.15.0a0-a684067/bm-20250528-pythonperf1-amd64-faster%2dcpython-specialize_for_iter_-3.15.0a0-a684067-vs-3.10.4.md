# Results vs. 3.10.4

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: windows-amd64
- commit hash: a684067
- commit date: 2025-05-28
- overall geometric mean: 1.159x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250528-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 219 ms: 1.12x faster                                                                 |
| docutils       | 1.92 sec                                                    | 1.62 sec: 1.19x faster                                                               |
| html5lib       | 51.0 ms                                                     | 38.5 ms: 1.33x faster                                                                |
| Geometric mean | (ref)                                                       | 1.21x faster                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250528-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|-------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 402 ms: 2.76x faster                                                                 |
| async_tree_memoization  | 526 ms                                                      | 207 ms: 2.54x faster                                                                 |
| async_tree_none         | 435 ms                                                      | 172 ms: 2.54x faster                                                                 |
| async_tree_cpu_io_mixed | 638 ms                                                      | 328 ms: 1.94x faster                                                                 |
| Geometric mean          | (ref)                                                       | 2.42x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250528-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 45.8 ms: 1.35x faster                                                                |
| nbody          | 71.3 ms                                                     | 64.1 ms: 1.11x faster                                                                |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                                                 |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250528-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 81.6 ms: 1.30x faster                                                                |
| regex_dna      | 136 ms                                                      | 121 ms: 1.12x faster                                                                 |
| regex_v8       | 15.4 ms                                                     | 14.1 ms: 1.10x faster                                                                |
| regex_effbot   | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                                |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250528-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.28 ms: 1.46x faster                                                                |
| unpickle_pure_python | 183 us                                                      | 139 us: 1.32x faster                                                                 |
| pickle_pure_python   | 270 us                                                      | 214 us: 1.26x faster                                                                 |
| tomli_loads          | 1.67 sec                                                    | 1.39 sec: 1.21x faster                                                               |
| xml_etree_process    | 44.5 ms                                                     | 38.7 ms: 1.15x faster                                                                |
| xml_etree_parse      | 96.8 ms                                                     | 87.6 ms: 1.10x faster                                                                |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.3 ms: 1.03x faster                                                                |
| xml_etree_generate   | 55.5 ms                                                     | 55.2 ms: 1.01x faster                                                                |
| json_loads           | 14.0 us                                                     | 14.9 us: 1.06x slower                                                                |
| Geometric mean       | (ref)                                                       | 1.15x faster                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250528-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.0 ms: 1.22x slower                                                                |
| python_startup         | 20.6 ms                                                     | 25.2 ms: 1.22x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.22x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250528-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.64 ms: 1.36x faster                                                                |
| genshi_text     | 19.8 ms                                                     | 15.3 ms: 1.30x faster                                                                |
| django_template | 28.9 ms                                                     | 23.9 ms: 1.21x faster                                                                |
| genshi_xml      | 41.0 ms                                                     | 34.3 ms: 1.20x faster                                                                |
| Geometric mean  | (ref)                                                       | 1.26x faster                                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250528-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 101 us: 3.31x faster                                                                 |
| async_tree_io            | 1.11 sec                                                    | 402 ms: 2.76x faster                                                                 |
| pathlib                  | 75.7 ms                                                     | 29.6 ms: 2.55x faster                                                                |
| async_tree_memoization   | 526 ms                                                      | 207 ms: 2.54x faster                                                                 |
| async_tree_none          | 435 ms                                                      | 172 ms: 2.54x faster                                                                 |
| mdp                      | 1.78 sec                                                    | 817 ms: 2.18x faster                                                                 |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 328 ms: 1.94x faster                                                                 |
| deltablue                | 4.19 ms                                                     | 2.20 ms: 1.91x faster                                                                |
| go                       | 139 ms                                                      | 77.2 ms: 1.80x faster                                                                |
| pylint                   | 350 ms                                                      | 197 ms: 1.78x faster                                                                 |
| richards_super           | 52.2 ms                                                     | 31.6 ms: 1.65x faster                                                                |
| generators               | 32.4 ms                                                     | 20.0 ms: 1.62x faster                                                                |
| chaos                    | 61.7 ms                                                     | 38.5 ms: 1.60x faster                                                                |
| deepcopy_memo            | 28.8 us                                                     | 18.5 us: 1.55x faster                                                                |
| richards                 | 42.4 ms                                                     | 27.6 ms: 1.54x faster                                                                |
| raytrace                 | 273 ms                                                      | 182 ms: 1.50x faster                                                                 |
| comprehensions           | 16.5 us                                                     | 11.0 us: 1.50x faster                                                                |
| deepcopy                 | 255 us                                                      | 172 us: 1.48x faster                                                                 |
| pyflate                  | 409 ms                                                      | 279 ms: 1.47x faster                                                                 |
| json_dumps               | 9.16 ms                                                     | 6.28 ms: 1.46x faster                                                                |
| scimark_lu               | 85.8 ms                                                     | 58.8 ms: 1.46x faster                                                                |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.9 ms: 1.40x faster                                                                |
| hexiom                   | 5.74 ms                                                     | 4.15 ms: 1.38x faster                                                                |
| scimark_sor              | 106 ms                                                      | 76.8 ms: 1.38x faster                                                                |
| mako                     | 9.03 ms                                                     | 6.64 ms: 1.36x faster                                                                |
| float                    | 61.7 ms                                                     | 45.8 ms: 1.35x faster                                                                |
| html5lib                 | 51.0 ms                                                     | 38.5 ms: 1.33x faster                                                                |
| crypto_pyaes             | 62.5 ms                                                     | 47.3 ms: 1.32x faster                                                                |
| spectral_norm            | 77.3 ms                                                     | 58.5 ms: 1.32x faster                                                                |
| unpickle_pure_python     | 183 us                                                      | 139 us: 1.32x faster                                                                 |
| pycparser                | 930 ms                                                      | 716 ms: 1.30x faster                                                                 |
| regex_compile            | 106 ms                                                      | 81.6 ms: 1.30x faster                                                                |
| genshi_text              | 19.8 ms                                                     | 15.3 ms: 1.30x faster                                                                |
| pickle_pure_python       | 270 us                                                      | 214 us: 1.26x faster                                                                 |
| dulwich_log              | 50.5 ms                                                     | 40.9 ms: 1.23x faster                                                                |
| sympy_integrate          | 15.3 ms                                                     | 12.5 ms: 1.22x faster                                                                |
| sympy_sum                | 107 ms                                                      | 88.0 ms: 1.22x faster                                                                |
| django_template          | 28.9 ms                                                     | 23.9 ms: 1.21x faster                                                                |
| tomli_loads              | 1.67 sec                                                    | 1.39 sec: 1.21x faster                                                               |
| sqlite_synth             | 1.91 us                                                     | 1.59 us: 1.20x faster                                                                |
| genshi_xml               | 41.0 ms                                                     | 34.3 ms: 1.20x faster                                                                |
| docutils                 | 1.92 sec                                                    | 1.62 sec: 1.19x faster                                                               |
| deepcopy_reduce          | 2.20 us                                                     | 1.88 us: 1.17x faster                                                                |
| sympy_str                | 194 ms                                                      | 169 ms: 1.15x faster                                                                 |
| xml_etree_process        | 44.5 ms                                                     | 38.7 ms: 1.15x faster                                                                |
| bench_thread_pool        | 958 us                                                      | 843 us: 1.14x faster                                                                 |
| coroutines               | 16.0 ms                                                     | 14.1 ms: 1.14x faster                                                                |
| regex_dna                | 136 ms                                                      | 121 ms: 1.12x faster                                                                 |
| 2to3                     | 246 ms                                                      | 219 ms: 1.12x faster                                                                 |
| nbody                    | 71.3 ms                                                     | 64.1 ms: 1.11x faster                                                                |
| xml_etree_parse          | 96.8 ms                                                     | 87.6 ms: 1.10x faster                                                                |
| regex_v8                 | 15.4 ms                                                     | 14.1 ms: 1.10x faster                                                                |
| sympy_expand             | 314 ms                                                      | 290 ms: 1.08x faster                                                                 |
| pprint_pformat           | 1.22 sec                                                    | 1.14 sec: 1.07x faster                                                               |
| pprint_safe_repr         | 592 ms                                                      | 558 ms: 1.06x faster                                                                 |
| nqueens                  | 66.6 ms                                                     | 62.9 ms: 1.06x faster                                                                |
| regex_effbot             | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                                |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.61 ms: 1.04x faster                                                                |
| meteor_contest           | 75.9 ms                                                     | 72.9 ms: 1.04x faster                                                                |
| scimark_fft              | 187 ms                                                      | 181 ms: 1.03x faster                                                                 |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.3 ms: 1.03x faster                                                                |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                                                 |
| xml_etree_generate       | 55.5 ms                                                     | 55.2 ms: 1.01x faster                                                                |
| logging_simple           | 6.22 us                                                     | 6.33 us: 1.02x slower                                                                |
| async_generators         | 222 ms                                                      | 233 ms: 1.05x slower                                                                 |
| json_loads               | 14.0 us                                                     | 14.9 us: 1.06x slower                                                                |
| telco                    | 3.94 ms                                                     | 4.67 ms: 1.19x slower                                                                |
| python_startup_no_site   | 15.5 ms                                                     | 19.0 ms: 1.22x slower                                                                |
| python_startup           | 20.6 ms                                                     | 25.2 ms: 1.22x slower                                                                |
| bench_mp_pool            | 62.0 ms                                                     | 92.7 ms: 1.49x slower                                                                |
| gc_traversal             | 1.41 ms                                                     | 2.19 ms: 1.55x slower                                                                |
| create_gc_cycles         | 800 us                                                      | 1.31 ms: 1.64x slower                                                                |
| logging_silent           | 94.6 ns                                                     | 318 ns: 3.37x slower                                                                 |
| coverage                 | 39.0 ms                                                     | 291 ms: 7.47x slower                                                                 |
| thrift                   | 617 us                                                      | 93.3 ms: 151.19x slower                                                              |
| Geometric mean           | (ref)                                                       | 1.13x faster                                                                         |

Benchmark hidden because not significant (3): fannkuch, logging_format, json
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250528-3.15.0a0-a684067/bm-20250528-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.159x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown