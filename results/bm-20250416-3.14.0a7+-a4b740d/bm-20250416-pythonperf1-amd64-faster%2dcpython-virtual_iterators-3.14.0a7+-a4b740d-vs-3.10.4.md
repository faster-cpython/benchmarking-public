# Results vs. 3.10.4

- fork: faster-cpython
- ref: virtual_iterators
- machine: windows-amd64
- commit hash: a4b740d
- commit date: 2025-04-16
- overall geometric mean: 1.284x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250416-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 217 ms: 1.13x faster                                                               |
| docutils       | 1.92 sec                                                    | 1.64 sec: 1.17x faster                                                             |
| html5lib       | 51.0 ms                                                     | 39.4 ms: 1.30x faster                                                              |
| Geometric mean | (ref)                                                       | 1.20x faster                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250416-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|-------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 413 ms: 2.68x faster                                                               |
| async_tree_memoization  | 526 ms                                                      | 208 ms: 2.52x faster                                                               |
| async_tree_none         | 435 ms                                                      | 182 ms: 2.40x faster                                                               |
| async_tree_cpu_io_mixed | 638 ms                                                      | 331 ms: 1.93x faster                                                               |
| Geometric mean          | (ref)                                                       | 2.36x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250416-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 43.3 ms: 1.43x faster                                                              |
| nbody          | 71.3 ms                                                     | 63.0 ms: 1.13x faster                                                              |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                       |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250416-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 81.0 ms: 1.31x faster                                                              |
| regex_dna      | 136 ms                                                      | 116 ms: 1.17x faster                                                               |
| regex_effbot   | 1.66 ms                                                     | 1.43 ms: 1.16x faster                                                              |
| regex_v8       | 15.4 ms                                                     | 14.2 ms: 1.09x faster                                                              |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250416-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.58 ms: 1.39x faster                                                              |
| unpickle_pure_python | 183 us                                                      | 139 us: 1.32x faster                                                               |
| pickle_pure_python   | 270 us                                                      | 212 us: 1.27x faster                                                               |
| tomli_loads          | 1.67 sec                                                    | 1.39 sec: 1.21x faster                                                             |
| xml_etree_process    | 44.5 ms                                                     | 38.9 ms: 1.14x faster                                                              |
| xml_etree_parse      | 96.8 ms                                                     | 90.8 ms: 1.07x faster                                                              |
| json_loads           | 14.0 us                                                     | 14.9 us: 1.06x slower                                                              |
| Geometric mean       | (ref)                                                       | 1.14x faster                                                                       |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250416-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 26.4 ms: 1.28x slower                                                              |
| python_startup_no_site | 15.5 ms                                                     | 20.5 ms: 1.32x slower                                                              |
| Geometric mean         | (ref)                                                       | 1.30x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250416-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.66 ms: 1.36x faster                                                              |
| genshi_text     | 19.8 ms                                                     | 15.5 ms: 1.28x faster                                                              |
| genshi_xml      | 41.0 ms                                                     | 34.1 ms: 1.20x faster                                                              |
| django_template | 28.9 ms                                                     | 24.4 ms: 1.18x faster                                                              |
| Geometric mean  | (ref)                                                       | 1.25x faster                                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250416-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|--------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 101 us: 3.32x faster                                                               |
| async_tree_io            | 1.11 sec                                                    | 413 ms: 2.68x faster                                                               |
| async_tree_memoization   | 526 ms                                                      | 208 ms: 2.52x faster                                                               |
| async_tree_none          | 435 ms                                                      | 182 ms: 2.40x faster                                                               |
| pathlib                  | 75.7 ms                                                     | 32.2 ms: 2.35x faster                                                              |
| mdp                      | 1.78 sec                                                    | 769 ms: 2.32x faster                                                               |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 331 ms: 1.93x faster                                                               |
| deltablue                | 4.19 ms                                                     | 2.19 ms: 1.91x faster                                                              |
| go                       | 139 ms                                                      | 78.4 ms: 1.77x faster                                                              |
| logging_silent           | 94.6 ns                                                     | 54.7 ns: 1.73x faster                                                              |
| richards_super           | 52.2 ms                                                     | 31.6 ms: 1.65x faster                                                              |
| generators               | 32.4 ms                                                     | 20.1 ms: 1.61x faster                                                              |
| chaos                    | 61.7 ms                                                     | 38.6 ms: 1.60x faster                                                              |
| deepcopy_memo            | 28.8 us                                                     | 18.5 us: 1.56x faster                                                              |
| raytrace                 | 273 ms                                                      | 176 ms: 1.55x faster                                                               |
| comprehensions           | 16.5 us                                                     | 10.7 us: 1.54x faster                                                              |
| richards                 | 42.4 ms                                                     | 28.1 ms: 1.51x faster                                                              |
| deepcopy                 | 255 us                                                      | 171 us: 1.49x faster                                                               |
| pyflate                  | 409 ms                                                      | 283 ms: 1.45x faster                                                               |
| scimark_lu               | 85.8 ms                                                     | 59.5 ms: 1.44x faster                                                              |
| scimark_monte_carlo      | 57.3 ms                                                     | 39.9 ms: 1.44x faster                                                              |
| hexiom                   | 5.74 ms                                                     | 4.02 ms: 1.43x faster                                                              |
| float                    | 61.7 ms                                                     | 43.3 ms: 1.43x faster                                                              |
| json_dumps               | 9.16 ms                                                     | 6.58 ms: 1.39x faster                                                              |
| scimark_sor              | 106 ms                                                      | 76.8 ms: 1.38x faster                                                              |
| mako                     | 9.03 ms                                                     | 6.66 ms: 1.36x faster                                                              |
| spectral_norm            | 77.3 ms                                                     | 57.9 ms: 1.33x faster                                                              |
| crypto_pyaes             | 62.5 ms                                                     | 47.5 ms: 1.32x faster                                                              |
| unpickle_pure_python     | 183 us                                                      | 139 us: 1.32x faster                                                               |
| regex_compile            | 106 ms                                                      | 81.0 ms: 1.31x faster                                                              |
| pycparser                | 930 ms                                                      | 717 ms: 1.30x faster                                                               |
| html5lib                 | 51.0 ms                                                     | 39.4 ms: 1.30x faster                                                              |
| genshi_text              | 19.8 ms                                                     | 15.5 ms: 1.28x faster                                                              |
| pickle_pure_python       | 270 us                                                      | 212 us: 1.27x faster                                                               |
| sqlite_synth             | 1.91 us                                                     | 1.54 us: 1.24x faster                                                              |
| pprint_pformat           | 1.22 sec                                                    | 997 ms: 1.22x faster                                                               |
| deepcopy_reduce          | 2.20 us                                                     | 1.82 us: 1.21x faster                                                              |
| tomli_loads              | 1.67 sec                                                    | 1.39 sec: 1.21x faster                                                             |
| pprint_safe_repr         | 592 ms                                                      | 492 ms: 1.20x faster                                                               |
| genshi_xml               | 41.0 ms                                                     | 34.1 ms: 1.20x faster                                                              |
| django_template          | 28.9 ms                                                     | 24.4 ms: 1.18x faster                                                              |
| dulwich_log              | 50.5 ms                                                     | 42.6 ms: 1.18x faster                                                              |
| regex_dna                | 136 ms                                                      | 116 ms: 1.17x faster                                                               |
| docutils                 | 1.92 sec                                                    | 1.64 sec: 1.17x faster                                                             |
| coroutines               | 16.0 ms                                                     | 13.7 ms: 1.17x faster                                                              |
| regex_effbot             | 1.66 ms                                                     | 1.43 ms: 1.16x faster                                                              |
| xml_etree_process        | 44.5 ms                                                     | 38.9 ms: 1.14x faster                                                              |
| 2to3                     | 246 ms                                                      | 217 ms: 1.13x faster                                                               |
| nbody                    | 71.3 ms                                                     | 63.0 ms: 1.13x faster                                                              |
| nqueens                  | 66.6 ms                                                     | 59.6 ms: 1.12x faster                                                              |
| bench_thread_pool        | 958 us                                                      | 869 us: 1.10x faster                                                               |
| regex_v8                 | 15.4 ms                                                     | 14.2 ms: 1.09x faster                                                              |
| scimark_fft              | 187 ms                                                      | 175 ms: 1.07x faster                                                               |
| meteor_contest           | 75.9 ms                                                     | 71.2 ms: 1.07x faster                                                              |
| xml_etree_parse          | 96.8 ms                                                     | 90.8 ms: 1.07x faster                                                              |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.59 ms: 1.05x faster                                                              |
| json                     | 3.14 ms                                                     | 3.05 ms: 1.03x faster                                                              |
| json_loads               | 14.0 us                                                     | 14.9 us: 1.06x slower                                                              |
| telco                    | 3.94 ms                                                     | 4.59 ms: 1.16x slower                                                              |
| coverage                 | 39.0 ms                                                     | 48.8 ms: 1.25x slower                                                              |
| python_startup           | 20.6 ms                                                     | 26.4 ms: 1.28x slower                                                              |
| python_startup_no_site   | 15.5 ms                                                     | 20.5 ms: 1.32x slower                                                              |
| bench_mp_pool            | 62.0 ms                                                     | 88.8 ms: 1.43x slower                                                              |
| gc_traversal             | 1.41 ms                                                     | 2.08 ms: 1.48x slower                                                              |
| create_gc_cycles         | 800 us                                                      | 1.25 ms: 1.56x slower                                                              |
| Geometric mean           | (ref)                                                       | 1.27x faster                                                                       |

Benchmark hidden because not significant (7): async_generators, pidigits, xml_etree_generate, fannkuch, logging_simple, logging_format, xml_etree_iterparse
Ignored benchmarks (26) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250416-3.14.0a7+-a4b740d/bm-20250416-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.284x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: unknown