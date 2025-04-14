# Results vs. 3.10.4

- fork: faster-cpython
- ref: use_stackref_macros
- machine: windows-amd64
- commit hash: 17b97c6
- commit date: 2025-02-27
- overall geometric mean: 1.218x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250227-pythonperf1-amd64-faster%2dcpython-use_stackref_macros-3.14.0a5+-17b97c6 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 227 ms: 1.08x faster                                                                 |
| docutils       | 1.92 sec                                                    | 1.69 sec: 1.14x faster                                                               |
| html5lib       | 51.0 ms                                                     | 41.2 ms: 1.24x faster                                                                |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250227-pythonperf1-amd64-faster%2dcpython-use_stackref_macros-3.14.0a5+-17b97c6 |
|-------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 420 ms: 2.64x faster                                                                 |
| async_tree_memoization  | 526 ms                                                      | 223 ms: 2.36x faster                                                                 |
| async_tree_none         | 435 ms                                                      | 190 ms: 2.29x faster                                                                 |
| async_tree_cpu_io_mixed | 638 ms                                                      | 341 ms: 1.87x faster                                                                 |
| Geometric mean          | (ref)                                                       | 2.27x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250227-pythonperf1-amd64-faster%2dcpython-use_stackref_macros-3.14.0a5+-17b97c6 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 46.8 ms: 1.32x faster                                                                |
| nbody          | 71.3 ms                                                     | 65.5 ms: 1.09x faster                                                                |
| pidigits       | 149 ms                                                      | 150 ms: 1.01x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.13x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250227-pythonperf1-amd64-faster%2dcpython-use_stackref_macros-3.14.0a5+-17b97c6 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 112 ms: 1.22x faster                                                                 |
| regex_compile  | 106 ms                                                      | 87.2 ms: 1.22x faster                                                                |
| regex_effbot   | 1.66 ms                                                     | 1.41 ms: 1.18x faster                                                                |
| regex_v8       | 15.4 ms                                                     | 14.3 ms: 1.08x faster                                                                |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250227-pythonperf1-amd64-faster%2dcpython-use_stackref_macros-3.14.0a5+-17b97c6 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.87 ms: 1.33x faster                                                                |
| unpickle_pure_python | 183 us                                                      | 151 us: 1.22x faster                                                                 |
| pickle_pure_python   | 270 us                                                      | 230 us: 1.17x faster                                                                 |
| tomli_loads          | 1.67 sec                                                    | 1.43 sec: 1.17x faster                                                               |
| xml_etree_process    | 44.5 ms                                                     | 41.1 ms: 1.08x faster                                                                |
| xml_etree_parse      | 96.8 ms                                                     | 89.8 ms: 1.08x faster                                                                |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.3 ms: 1.03x faster                                                                |
| xml_etree_generate   | 55.5 ms                                                     | 57.6 ms: 1.04x slower                                                                |
| json_loads           | 14.0 us                                                     | 15.0 us: 1.07x slower                                                                |
| Geometric mean       | (ref)                                                       | 1.10x faster                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250227-pythonperf1-amd64-faster%2dcpython-use_stackref_macros-3.14.0a5+-17b97c6 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 26.1 ms: 1.27x slower                                                                |
| python_startup_no_site | 15.5 ms                                                     | 19.7 ms: 1.27x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.27x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250227-pythonperf1-amd64-faster%2dcpython-use_stackref_macros-3.14.0a5+-17b97c6 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 7.07 ms: 1.28x faster                                                                |
| genshi_text     | 19.8 ms                                                     | 17.3 ms: 1.14x faster                                                                |
| django_template | 28.9 ms                                                     | 26.2 ms: 1.10x faster                                                                |
| genshi_xml      | 41.0 ms                                                     | 38.1 ms: 1.08x faster                                                                |
| Geometric mean  | (ref)                                                       | 1.15x faster                                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250227-pythonperf1-amd64-faster%2dcpython-use_stackref_macros-3.14.0a5+-17b97c6 |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 109 us: 3.09x faster                                                                 |
| async_tree_io            | 1.11 sec                                                    | 420 ms: 2.64x faster                                                                 |
| async_tree_memoization   | 526 ms                                                      | 223 ms: 2.36x faster                                                                 |
| pathlib                  | 75.7 ms                                                     | 32.1 ms: 2.35x faster                                                                |
| async_tree_none          | 435 ms                                                      | 190 ms: 2.29x faster                                                                 |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 341 ms: 1.87x faster                                                                 |
| deltablue                | 4.19 ms                                                     | 2.31 ms: 1.82x faster                                                                |
| pylint                   | 350 ms                                                      | 203 ms: 1.73x faster                                                                 |
| generators               | 32.4 ms                                                     | 19.4 ms: 1.67x faster                                                                |
| logging_silent           | 94.6 ns                                                     | 59.7 ns: 1.59x faster                                                                |
| go                       | 139 ms                                                      | 89.3 ms: 1.56x faster                                                                |
| richards_super           | 52.2 ms                                                     | 34.1 ms: 1.53x faster                                                                |
| deepcopy_memo            | 28.8 us                                                     | 19.1 us: 1.50x faster                                                                |
| scimark_lu               | 85.8 ms                                                     | 59.9 ms: 1.43x faster                                                                |
| richards                 | 42.4 ms                                                     | 30.2 ms: 1.40x faster                                                                |
| chaos                    | 61.7 ms                                                     | 44.1 ms: 1.40x faster                                                                |
| deepcopy                 | 255 us                                                      | 184 us: 1.39x faster                                                                 |
| comprehensions           | 16.5 us                                                     | 12.1 us: 1.36x faster                                                                |
| spectral_norm            | 77.3 ms                                                     | 56.7 ms: 1.36x faster                                                                |
| raytrace                 | 273 ms                                                      | 204 ms: 1.34x faster                                                                 |
| pyflate                  | 409 ms                                                      | 306 ms: 1.34x faster                                                                 |
| sqlglot_parse            | 1.22 ms                                                     | 910 us: 1.33x faster                                                                 |
| json_dumps               | 9.16 ms                                                     | 6.87 ms: 1.33x faster                                                                |
| float                    | 61.7 ms                                                     | 46.8 ms: 1.32x faster                                                                |
| scimark_sor              | 106 ms                                                      | 80.5 ms: 1.32x faster                                                                |
| sqlglot_transpile        | 1.48 ms                                                     | 1.12 ms: 1.31x faster                                                                |
| hexiom                   | 5.74 ms                                                     | 4.38 ms: 1.31x faster                                                                |
| scimark_monte_carlo      | 57.3 ms                                                     | 44.0 ms: 1.30x faster                                                                |
| mako                     | 9.03 ms                                                     | 7.07 ms: 1.28x faster                                                                |
| pycparser                | 930 ms                                                      | 744 ms: 1.25x faster                                                                 |
| html5lib                 | 51.0 ms                                                     | 41.2 ms: 1.24x faster                                                                |
| crypto_pyaes             | 62.5 ms                                                     | 51.3 ms: 1.22x faster                                                                |
| regex_dna                | 136 ms                                                      | 112 ms: 1.22x faster                                                                 |
| unpickle_pure_python     | 183 us                                                      | 151 us: 1.22x faster                                                                 |
| regex_compile            | 106 ms                                                      | 87.2 ms: 1.22x faster                                                                |
| sqlite_synth             | 1.91 us                                                     | 1.60 us: 1.19x faster                                                                |
| mdp                      | 1.78 sec                                                    | 1.50 sec: 1.19x faster                                                               |
| sympy_sum                | 107 ms                                                      | 90.5 ms: 1.18x faster                                                                |
| regex_effbot             | 1.66 ms                                                     | 1.41 ms: 1.18x faster                                                                |
| pickle_pure_python       | 270 us                                                      | 230 us: 1.17x faster                                                                 |
| thrift                   | 617 us                                                      | 528 us: 1.17x faster                                                                 |
| tomli_loads              | 1.67 sec                                                    | 1.43 sec: 1.17x faster                                                               |
| dulwich_log              | 50.5 ms                                                     | 43.4 ms: 1.16x faster                                                                |
| coroutines               | 16.0 ms                                                     | 13.8 ms: 1.16x faster                                                                |
| sympy_integrate          | 15.3 ms                                                     | 13.3 ms: 1.15x faster                                                                |
| genshi_text              | 19.8 ms                                                     | 17.3 ms: 1.14x faster                                                                |
| docutils                 | 1.92 sec                                                    | 1.69 sec: 1.14x faster                                                               |
| deepcopy_reduce          | 2.20 us                                                     | 1.95 us: 1.13x faster                                                                |
| bench_thread_pool        | 958 us                                                      | 860 us: 1.11x faster                                                                 |
| pprint_pformat           | 1.22 sec                                                    | 1.10 sec: 1.11x faster                                                               |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.46 ms: 1.11x faster                                                                |
| django_template          | 28.9 ms                                                     | 26.2 ms: 1.10x faster                                                                |
| sympy_str                | 194 ms                                                      | 177 ms: 1.10x faster                                                                 |
| sqlglot_optimize         | 39.8 ms                                                     | 36.2 ms: 1.10x faster                                                                |
| nbody                    | 71.3 ms                                                     | 65.5 ms: 1.09x faster                                                                |
| pprint_safe_repr         | 592 ms                                                      | 546 ms: 1.08x faster                                                                 |
| 2to3                     | 246 ms                                                      | 227 ms: 1.08x faster                                                                 |
| xml_etree_process        | 44.5 ms                                                     | 41.1 ms: 1.08x faster                                                                |
| regex_v8                 | 15.4 ms                                                     | 14.3 ms: 1.08x faster                                                                |
| xml_etree_parse          | 96.8 ms                                                     | 89.8 ms: 1.08x faster                                                                |
| genshi_xml               | 41.0 ms                                                     | 38.1 ms: 1.08x faster                                                                |
| sqlglot_normalize        | 205 ms                                                      | 196 ms: 1.05x faster                                                                 |
| json                     | 3.14 ms                                                     | 3.02 ms: 1.04x faster                                                                |
| sympy_expand             | 314 ms                                                      | 305 ms: 1.03x faster                                                                 |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.3 ms: 1.03x faster                                                                |
| nqueens                  | 66.6 ms                                                     | 65.0 ms: 1.02x faster                                                                |
| scimark_fft              | 187 ms                                                      | 184 ms: 1.02x faster                                                                 |
| pidigits                 | 149 ms                                                      | 150 ms: 1.01x slower                                                                 |
| meteor_contest           | 75.9 ms                                                     | 76.9 ms: 1.01x slower                                                                |
| logging_format           | 6.76 us                                                     | 6.95 us: 1.03x slower                                                                |
| async_generators         | 222 ms                                                      | 229 ms: 1.03x slower                                                                 |
| xml_etree_generate       | 55.5 ms                                                     | 57.6 ms: 1.04x slower                                                                |
| logging_simple           | 6.22 us                                                     | 6.50 us: 1.05x slower                                                                |
| fannkuch                 | 256 ms                                                      | 273 ms: 1.07x slower                                                                 |
| json_loads               | 14.0 us                                                     | 15.0 us: 1.07x slower                                                                |
| coverage                 | 39.0 ms                                                     | 47.6 ms: 1.22x slower                                                                |
| telco                    | 3.94 ms                                                     | 4.88 ms: 1.24x slower                                                                |
| python_startup           | 20.6 ms                                                     | 26.1 ms: 1.27x slower                                                                |
| python_startup_no_site   | 15.5 ms                                                     | 19.7 ms: 1.27x slower                                                                |
| bench_mp_pool            | 62.0 ms                                                     | 86.6 ms: 1.40x slower                                                                |
| gc_traversal             | 1.41 ms                                                     | 1.99 ms: 1.41x slower                                                                |
| create_gc_cycles         | 800 us                                                      | 1.23 ms: 1.54x slower                                                                |
| Geometric mean           | (ref)                                                       | 1.21x faster                                                                         |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250227-3.14.0a5+-17b97c6/bm-20250227-pythonperf1-amd64-faster%2dcpython-use_stackref_macros-3.14.0a5+-17b97c6.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.218x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown