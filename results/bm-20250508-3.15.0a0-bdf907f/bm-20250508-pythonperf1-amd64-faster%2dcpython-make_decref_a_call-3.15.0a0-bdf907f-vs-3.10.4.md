# Results vs. 3.10.4

- fork: faster-cpython
- ref: make_decref_a_call
- machine: windows-amd64
- commit hash: bdf907f
- commit date: 2025-05-08
- overall geometric mean: 1.235x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 238 ms: 1.03x faster                                                               |
| docutils       | 1.92 sec                                                    | 1.72 sec: 1.11x faster                                                             |
| html5lib       | 51.0 ms                                                     | 38.3 ms: 1.33x faster                                                              |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|-------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 418 ms: 2.65x faster                                                               |
| async_tree_memoization  | 526 ms                                                      | 217 ms: 2.43x faster                                                               |
| async_tree_none         | 435 ms                                                      | 180 ms: 2.42x faster                                                               |
| async_tree_cpu_io_mixed | 638 ms                                                      | 338 ms: 1.88x faster                                                               |
| Geometric mean          | (ref)                                                       | 2.33x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 44.9 ms: 1.37x faster                                                              |
| nbody          | 71.3 ms                                                     | 62.7 ms: 1.14x faster                                                              |
| pidigits       | 149 ms                                                      | 150 ms: 1.01x slower                                                               |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 82.7 ms: 1.28x faster                                                              |
| regex_dna      | 136 ms                                                      | 120 ms: 1.14x faster                                                               |
| regex_v8       | 15.4 ms                                                     | 14.3 ms: 1.08x faster                                                              |
| regex_effbot   | 1.66 ms                                                     | 1.63 ms: 1.02x faster                                                              |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 136 us: 1.35x faster                                                               |
| json_dumps           | 9.16 ms                                                     | 7.19 ms: 1.27x faster                                                              |
| pickle_pure_python   | 270 us                                                      | 216 us: 1.25x faster                                                               |
| tomli_loads          | 1.67 sec                                                    | 1.42 sec: 1.18x faster                                                             |
| xml_etree_process    | 44.5 ms                                                     | 42.2 ms: 1.05x faster                                                              |
| xml_etree_iterparse  | 65.0 ms                                                     | 68.0 ms: 1.05x slower                                                              |
| xml_etree_generate   | 55.5 ms                                                     | 60.5 ms: 1.09x slower                                                              |
| json_loads           | 14.0 us                                                     | 15.4 us: 1.10x slower                                                              |
| Geometric mean       | (ref)                                                       | 1.09x faster                                                                       |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 20.0 ms: 1.29x slower                                                              |
| python_startup         | 20.6 ms                                                     | 26.7 ms: 1.30x slower                                                              |
| Geometric mean         | (ref)                                                       | 1.30x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.57 ms: 1.38x faster                                                              |
| genshi_text     | 19.8 ms                                                     | 15.7 ms: 1.26x faster                                                              |
| genshi_xml      | 41.0 ms                                                     | 34.8 ms: 1.18x faster                                                              |
| django_template | 28.9 ms                                                     | 24.6 ms: 1.17x faster                                                              |
| Geometric mean  | (ref)                                                       | 1.24x faster                                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|--------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 114 us: 2.95x faster                                                               |
| async_tree_io            | 1.11 sec                                                    | 418 ms: 2.65x faster                                                               |
| async_tree_memoization   | 526 ms                                                      | 217 ms: 2.43x faster                                                               |
| async_tree_none          | 435 ms                                                      | 180 ms: 2.42x faster                                                               |
| pathlib                  | 75.7 ms                                                     | 32.4 ms: 2.33x faster                                                              |
| mdp                      | 1.78 sec                                                    | 855 ms: 2.08x faster                                                               |
| deltablue                | 4.19 ms                                                     | 2.20 ms: 1.90x faster                                                              |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 338 ms: 1.88x faster                                                               |
| go                       | 139 ms                                                      | 78.2 ms: 1.78x faster                                                              |
| pylint                   | 350 ms                                                      | 206 ms: 1.70x faster                                                               |
| generators               | 32.4 ms                                                     | 19.9 ms: 1.63x faster                                                              |
| richards_super           | 52.2 ms                                                     | 32.1 ms: 1.63x faster                                                              |
| logging_silent           | 94.6 ns                                                     | 58.6 ns: 1.61x faster                                                              |
| chaos                    | 61.7 ms                                                     | 39.3 ms: 1.57x faster                                                              |
| deepcopy_memo            | 28.8 us                                                     | 19.0 us: 1.52x faster                                                              |
| raytrace                 | 273 ms                                                      | 181 ms: 1.51x faster                                                               |
| richards                 | 42.4 ms                                                     | 28.2 ms: 1.51x faster                                                              |
| scimark_lu               | 85.8 ms                                                     | 58.9 ms: 1.46x faster                                                              |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.2 ms: 1.42x faster                                                              |
| hexiom                   | 5.74 ms                                                     | 4.10 ms: 1.40x faster                                                              |
| deepcopy                 | 255 us                                                      | 183 us: 1.39x faster                                                               |
| comprehensions           | 16.5 us                                                     | 12.0 us: 1.38x faster                                                              |
| mako                     | 9.03 ms                                                     | 6.57 ms: 1.38x faster                                                              |
| float                    | 61.7 ms                                                     | 44.9 ms: 1.37x faster                                                              |
| scimark_sor              | 106 ms                                                      | 77.6 ms: 1.37x faster                                                              |
| unpickle_pure_python     | 183 us                                                      | 136 us: 1.35x faster                                                               |
| html5lib                 | 51.0 ms                                                     | 38.3 ms: 1.33x faster                                                              |
| pyflate                  | 409 ms                                                      | 308 ms: 1.33x faster                                                               |
| spectral_norm            | 77.3 ms                                                     | 59.4 ms: 1.30x faster                                                              |
| crypto_pyaes             | 62.5 ms                                                     | 48.6 ms: 1.29x faster                                                              |
| regex_compile            | 106 ms                                                      | 82.7 ms: 1.28x faster                                                              |
| json_dumps               | 9.16 ms                                                     | 7.19 ms: 1.27x faster                                                              |
| pycparser                | 930 ms                                                      | 733 ms: 1.27x faster                                                               |
| genshi_text              | 19.8 ms                                                     | 15.7 ms: 1.26x faster                                                              |
| pickle_pure_python       | 270 us                                                      | 216 us: 1.25x faster                                                               |
| sympy_integrate          | 15.3 ms                                                     | 12.8 ms: 1.19x faster                                                              |
| tomli_loads              | 1.67 sec                                                    | 1.42 sec: 1.18x faster                                                             |
| genshi_xml               | 41.0 ms                                                     | 34.8 ms: 1.18x faster                                                              |
| dulwich_log              | 50.5 ms                                                     | 42.9 ms: 1.18x faster                                                              |
| django_template          | 28.9 ms                                                     | 24.6 ms: 1.17x faster                                                              |
| sympy_sum                | 107 ms                                                      | 91.3 ms: 1.17x faster                                                              |
| thrift                   | 617 us                                                      | 528 us: 1.17x faster                                                               |
| pprint_pformat           | 1.22 sec                                                    | 1.04 sec: 1.17x faster                                                             |
| pprint_safe_repr         | 592 ms                                                      | 513 ms: 1.15x faster                                                               |
| sqlite_synth             | 1.91 us                                                     | 1.67 us: 1.14x faster                                                              |
| deepcopy_reduce          | 2.20 us                                                     | 1.93 us: 1.14x faster                                                              |
| nbody                    | 71.3 ms                                                     | 62.7 ms: 1.14x faster                                                              |
| regex_dna                | 136 ms                                                      | 120 ms: 1.14x faster                                                               |
| docutils                 | 1.92 sec                                                    | 1.72 sec: 1.11x faster                                                             |
| coroutines               | 16.0 ms                                                     | 14.5 ms: 1.11x faster                                                              |
| bench_thread_pool        | 958 us                                                      | 876 us: 1.09x faster                                                               |
| sympy_str                | 194 ms                                                      | 179 ms: 1.08x faster                                                               |
| regex_v8                 | 15.4 ms                                                     | 14.3 ms: 1.08x faster                                                              |
| xml_etree_process        | 44.5 ms                                                     | 42.2 ms: 1.05x faster                                                              |
| nqueens                  | 66.6 ms                                                     | 64.2 ms: 1.04x faster                                                              |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.63 ms: 1.04x faster                                                              |
| 2to3                     | 246 ms                                                      | 238 ms: 1.03x faster                                                               |
| json                     | 3.14 ms                                                     | 3.07 ms: 1.02x faster                                                              |
| regex_effbot             | 1.66 ms                                                     | 1.63 ms: 1.02x faster                                                              |
| scimark_fft              | 187 ms                                                      | 184 ms: 1.02x faster                                                               |
| sympy_expand             | 314 ms                                                      | 310 ms: 1.01x faster                                                               |
| pidigits                 | 149 ms                                                      | 150 ms: 1.01x slower                                                               |
| logging_format           | 6.76 us                                                     | 6.82 us: 1.01x slower                                                              |
| logging_simple           | 6.22 us                                                     | 6.29 us: 1.01x slower                                                              |
| meteor_contest           | 75.9 ms                                                     | 78.0 ms: 1.03x slower                                                              |
| xml_etree_iterparse      | 65.0 ms                                                     | 68.0 ms: 1.05x slower                                                              |
| xml_etree_generate       | 55.5 ms                                                     | 60.5 ms: 1.09x slower                                                              |
| fannkuch                 | 256 ms                                                      | 279 ms: 1.09x slower                                                               |
| json_loads               | 14.0 us                                                     | 15.4 us: 1.10x slower                                                              |
| async_generators         | 222 ms                                                      | 256 ms: 1.16x slower                                                               |
| python_startup_no_site   | 15.5 ms                                                     | 20.0 ms: 1.29x slower                                                              |
| telco                    | 3.94 ms                                                     | 5.11 ms: 1.30x slower                                                              |
| python_startup           | 20.6 ms                                                     | 26.7 ms: 1.30x slower                                                              |
| coverage                 | 39.0 ms                                                     | 55.9 ms: 1.43x slower                                                              |
| gc_traversal             | 1.41 ms                                                     | 2.15 ms: 1.52x slower                                                              |
| bench_mp_pool            | 62.0 ms                                                     | 98.1 ms: 1.58x slower                                                              |
| create_gc_cycles         | 800 us                                                      | 1.33 ms: 1.66x slower                                                              |
| Geometric mean           | (ref)                                                       | 1.22x faster                                                                       |

Benchmark hidden because not significant (1): xml_etree_parse
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250508-3.15.0a0-bdf907f/bm-20250508-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.235x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown