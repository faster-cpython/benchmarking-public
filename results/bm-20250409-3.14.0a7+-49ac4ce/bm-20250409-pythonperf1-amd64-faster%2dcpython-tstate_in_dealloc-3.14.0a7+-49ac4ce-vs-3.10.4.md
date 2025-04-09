# Results vs. 3.10.4

- fork: faster-cpython
- ref: tstate_in_dealloc
- machine: windows-amd64
- commit hash: 49ac4ce
- commit date: 2025-04-09
- overall geometric mean: 1.275x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-pythonperf1-amd64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 220 ms: 1.12x faster                                                               |
| docutils       | 1.92 sec                                                    | 1.64 sec: 1.17x faster                                                             |
| html5lib       | 51.0 ms                                                     | 38.5 ms: 1.32x faster                                                              |
| Geometric mean | (ref)                                                       | 1.20x faster                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-pythonperf1-amd64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|-------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 411 ms: 2.69x faster                                                               |
| async_tree_memoization  | 526 ms                                                      | 207 ms: 2.55x faster                                                               |
| async_tree_none         | 435 ms                                                      | 183 ms: 2.38x faster                                                               |
| async_tree_cpu_io_mixed | 638 ms                                                      | 331 ms: 1.92x faster                                                               |
| Geometric mean          | (ref)                                                       | 2.37x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-pythonperf1-amd64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 43.5 ms: 1.42x faster                                                              |
| nbody          | 71.3 ms                                                     | 65.5 ms: 1.09x faster                                                              |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                       |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-pythonperf1-amd64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 80.5 ms: 1.32x faster                                                              |
| regex_dna      | 136 ms                                                      | 114 ms: 1.20x faster                                                               |
| regex_effbot   | 1.66 ms                                                     | 1.42 ms: 1.17x faster                                                              |
| regex_v8       | 15.4 ms                                                     | 13.7 ms: 1.13x faster                                                              |
| Geometric mean | (ref)                                                       | 1.20x faster                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-pythonperf1-amd64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.80 ms: 1.35x faster                                                              |
| unpickle_pure_python | 183 us                                                      | 137 us: 1.34x faster                                                               |
| pickle_pure_python   | 270 us                                                      | 215 us: 1.25x faster                                                               |
| tomli_loads          | 1.67 sec                                                    | 1.43 sec: 1.17x faster                                                             |
| xml_etree_process    | 44.5 ms                                                     | 39.5 ms: 1.13x faster                                                              |
| xml_etree_parse      | 96.8 ms                                                     | 88.4 ms: 1.09x faster                                                              |
| xml_etree_iterparse  | 65.0 ms                                                     | 64.0 ms: 1.02x faster                                                              |
| json_loads           | 14.0 us                                                     | 15.2 us: 1.08x slower                                                              |
| Geometric mean       | (ref)                                                       | 1.13x faster                                                                       |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-pythonperf1-amd64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.4 ms: 1.23x slower                                                              |
| python_startup_no_site | 15.5 ms                                                     | 19.7 ms: 1.27x slower                                                              |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-pythonperf1-amd64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.81 ms: 1.33x faster                                                              |
| genshi_text     | 19.8 ms                                                     | 15.8 ms: 1.25x faster                                                              |
| django_template | 28.9 ms                                                     | 24.7 ms: 1.17x faster                                                              |
| genshi_xml      | 41.0 ms                                                     | 35.4 ms: 1.16x faster                                                              |
| Geometric mean  | (ref)                                                       | 1.22x faster                                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250409-pythonperf1-amd64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|--------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 106 us: 3.17x faster                                                               |
| async_tree_io            | 1.11 sec                                                    | 411 ms: 2.69x faster                                                               |
| pathlib                  | 75.7 ms                                                     | 28.7 ms: 2.63x faster                                                              |
| async_tree_memoization   | 526 ms                                                      | 207 ms: 2.55x faster                                                               |
| async_tree_none          | 435 ms                                                      | 183 ms: 2.38x faster                                                               |
| mdp                      | 1.78 sec                                                    | 798 ms: 2.23x faster                                                               |
| deltablue                | 4.19 ms                                                     | 2.16 ms: 1.93x faster                                                              |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 331 ms: 1.92x faster                                                               |
| go                       | 139 ms                                                      | 78.5 ms: 1.77x faster                                                              |
| pylint                   | 350 ms                                                      | 199 ms: 1.76x faster                                                               |
| logging_silent           | 94.6 ns                                                     | 55.9 ns: 1.69x faster                                                              |
| generators               | 32.4 ms                                                     | 19.4 ms: 1.67x faster                                                              |
| richards_super           | 52.2 ms                                                     | 31.6 ms: 1.65x faster                                                              |
| chaos                    | 61.7 ms                                                     | 38.4 ms: 1.61x faster                                                              |
| deepcopy_memo            | 28.8 us                                                     | 18.3 us: 1.58x faster                                                              |
| richards                 | 42.4 ms                                                     | 27.7 ms: 1.53x faster                                                              |
| raytrace                 | 273 ms                                                      | 179 ms: 1.53x faster                                                               |
| deepcopy                 | 255 us                                                      | 174 us: 1.46x faster                                                               |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.2 ms: 1.42x faster                                                              |
| float                    | 61.7 ms                                                     | 43.5 ms: 1.42x faster                                                              |
| comprehensions           | 16.5 us                                                     | 11.7 us: 1.42x faster                                                              |
| scimark_sor              | 106 ms                                                      | 75.8 ms: 1.40x faster                                                              |
| hexiom                   | 5.74 ms                                                     | 4.14 ms: 1.39x faster                                                              |
| pyflate                  | 409 ms                                                      | 296 ms: 1.38x faster                                                               |
| scimark_lu               | 85.8 ms                                                     | 62.7 ms: 1.37x faster                                                              |
| json_dumps               | 9.16 ms                                                     | 6.80 ms: 1.35x faster                                                              |
| unpickle_pure_python     | 183 us                                                      | 137 us: 1.34x faster                                                               |
| mako                     | 9.03 ms                                                     | 6.81 ms: 1.33x faster                                                              |
| html5lib                 | 51.0 ms                                                     | 38.5 ms: 1.32x faster                                                              |
| spectral_norm            | 77.3 ms                                                     | 58.6 ms: 1.32x faster                                                              |
| regex_compile            | 106 ms                                                      | 80.5 ms: 1.32x faster                                                              |
| pycparser                | 930 ms                                                      | 715 ms: 1.30x faster                                                               |
| crypto_pyaes             | 62.5 ms                                                     | 48.8 ms: 1.28x faster                                                              |
| pickle_pure_python       | 270 us                                                      | 215 us: 1.25x faster                                                               |
| genshi_text              | 19.8 ms                                                     | 15.8 ms: 1.25x faster                                                              |
| dulwich_log              | 50.5 ms                                                     | 40.6 ms: 1.24x faster                                                              |
| sympy_integrate          | 15.3 ms                                                     | 12.5 ms: 1.22x faster                                                              |
| sqlite_synth             | 1.91 us                                                     | 1.58 us: 1.21x faster                                                              |
| sympy_sum                | 107 ms                                                      | 89.0 ms: 1.20x faster                                                              |
| regex_dna                | 136 ms                                                      | 114 ms: 1.20x faster                                                               |
| deepcopy_reduce          | 2.20 us                                                     | 1.84 us: 1.20x faster                                                              |
| pprint_pformat           | 1.22 sec                                                    | 1.03 sec: 1.19x faster                                                             |
| django_template          | 28.9 ms                                                     | 24.7 ms: 1.17x faster                                                              |
| docutils                 | 1.92 sec                                                    | 1.64 sec: 1.17x faster                                                             |
| regex_effbot             | 1.66 ms                                                     | 1.42 ms: 1.17x faster                                                              |
| pprint_safe_repr         | 592 ms                                                      | 506 ms: 1.17x faster                                                               |
| tomli_loads              | 1.67 sec                                                    | 1.43 sec: 1.17x faster                                                             |
| genshi_xml               | 41.0 ms                                                     | 35.4 ms: 1.16x faster                                                              |
| coroutines               | 16.0 ms                                                     | 13.9 ms: 1.15x faster                                                              |
| sympy_str                | 194 ms                                                      | 172 ms: 1.13x faster                                                               |
| regex_v8                 | 15.4 ms                                                     | 13.7 ms: 1.13x faster                                                              |
| xml_etree_process        | 44.5 ms                                                     | 39.5 ms: 1.13x faster                                                              |
| bench_thread_pool        | 958 us                                                      | 850 us: 1.13x faster                                                               |
| 2to3                     | 246 ms                                                      | 220 ms: 1.12x faster                                                               |
| xml_etree_parse          | 96.8 ms                                                     | 88.4 ms: 1.09x faster                                                              |
| nbody                    | 71.3 ms                                                     | 65.5 ms: 1.09x faster                                                              |
| nqueens                  | 66.6 ms                                                     | 61.8 ms: 1.08x faster                                                              |
| scimark_fft              | 187 ms                                                      | 175 ms: 1.07x faster                                                               |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.55 ms: 1.07x faster                                                              |
| sympy_expand             | 314 ms                                                      | 295 ms: 1.07x faster                                                               |
| meteor_contest           | 75.9 ms                                                     | 73.2 ms: 1.04x faster                                                              |
| logging_format           | 6.76 us                                                     | 6.64 us: 1.02x faster                                                              |
| xml_etree_iterparse      | 65.0 ms                                                     | 64.0 ms: 1.02x faster                                                              |
| logging_simple           | 6.22 us                                                     | 6.16 us: 1.01x faster                                                              |
| json                     | 3.14 ms                                                     | 3.25 ms: 1.04x slower                                                              |
| async_generators         | 222 ms                                                      | 233 ms: 1.05x slower                                                               |
| json_loads               | 14.0 us                                                     | 15.2 us: 1.08x slower                                                              |
| telco                    | 3.94 ms                                                     | 4.77 ms: 1.21x slower                                                              |
| python_startup           | 20.6 ms                                                     | 25.4 ms: 1.23x slower                                                              |
| python_startup_no_site   | 15.5 ms                                                     | 19.7 ms: 1.27x slower                                                              |
| coverage                 | 39.0 ms                                                     | 52.0 ms: 1.33x slower                                                              |
| bench_mp_pool            | 62.0 ms                                                     | 87.1 ms: 1.40x slower                                                              |
| gc_traversal             | 1.41 ms                                                     | 2.02 ms: 1.43x slower                                                              |
| create_gc_cycles         | 800 us                                                      | 1.22 ms: 1.52x slower                                                              |
| Geometric mean           | (ref)                                                       | 1.27x faster                                                                       |

Benchmark hidden because not significant (3): xml_etree_generate, fannkuch, pidigits
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250409-3.14.0a7+-49ac4ce/bm-20250409-pythonperf1-amd64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.275x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: unknown