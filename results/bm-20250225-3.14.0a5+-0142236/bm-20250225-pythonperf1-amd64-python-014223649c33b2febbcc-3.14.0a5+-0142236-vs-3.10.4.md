# Results vs. 3.10.4

- fork: python
- ref: 014223649c33b2febbcc
- machine: windows-amd64
- commit hash: 0142236
- commit date: 2025-02-25
- overall geometric mean: 1.239x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-pythonperf1-amd64-python-014223649c33b2febbcc-3.14.0a5+-0142236 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 223 ms: 1.10x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.66 sec: 1.16x faster                                                      |
| html5lib       | 51.0 ms                                                     | 40.0 ms: 1.27x faster                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-pythonperf1-amd64-python-014223649c33b2febbcc-3.14.0a5+-0142236 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 417 ms: 2.66x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 219 ms: 2.40x faster                                                        |
| async_tree_none         | 435 ms                                                      | 190 ms: 2.29x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 342 ms: 1.86x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.28x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-pythonperf1-amd64-python-014223649c33b2febbcc-3.14.0a5+-0142236 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 45.3 ms: 1.36x faster                                                       |
| nbody          | 71.3 ms                                                     | 69.2 ms: 1.03x faster                                                       |
| pidigits       | 149 ms                                                      | 150 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-pythonperf1-amd64-python-014223649c33b2febbcc-3.14.0a5+-0142236 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 85.6 ms: 1.24x faster                                                       |
| regex_dna      | 136 ms                                                      | 114 ms: 1.20x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.42 ms: 1.17x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.2 ms: 1.08x faster                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-pythonperf1-amd64-python-014223649c33b2febbcc-3.14.0a5+-0142236 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.66 ms: 1.38x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 145 us: 1.26x faster                                                        |
| pickle_pure_python   | 270 us                                                      | 227 us: 1.19x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.41 sec: 1.18x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 39.9 ms: 1.12x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 89.1 ms: 1.09x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.5 ms: 1.04x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 56.1 ms: 1.01x slower                                                       |
| json_loads           | 14.0 us                                                     | 14.7 us: 1.05x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.13x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-pythonperf1-amd64-python-014223649c33b2febbcc-3.14.0a5+-0142236 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.1 ms: 1.22x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 19.0 ms: 1.23x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.22x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-pythonperf1-amd64-python-014223649c33b2febbcc-3.14.0a5+-0142236 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.75 ms: 1.34x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 16.3 ms: 1.21x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 35.7 ms: 1.15x faster                                                       |
| django_template | 28.9 ms                                                     | 25.2 ms: 1.15x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.21x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-pythonperf1-amd64-python-014223649c33b2febbcc-3.14.0a5+-0142236 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 106 us: 3.18x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 417 ms: 2.66x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 30.2 ms: 2.51x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 219 ms: 2.40x faster                                                        |
| async_tree_none          | 435 ms                                                      | 190 ms: 2.29x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.16 ms: 1.94x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 342 ms: 1.86x faster                                                        |
| pylint                   | 350 ms                                                      | 198 ms: 1.77x faster                                                        |
| generators               | 32.4 ms                                                     | 19.4 ms: 1.67x faster                                                       |
| go                       | 139 ms                                                      | 85.5 ms: 1.63x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 60.7 ns: 1.56x faster                                                       |
| richards_super           | 52.2 ms                                                     | 33.6 ms: 1.56x faster                                                       |
| chaos                    | 61.7 ms                                                     | 41.7 ms: 1.48x faster                                                       |
| richards                 | 42.4 ms                                                     | 29.3 ms: 1.45x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.4 us: 1.45x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 19.9 us: 1.44x faster                                                       |
| raytrace                 | 273 ms                                                      | 191 ms: 1.43x faster                                                        |
| deepcopy                 | 255 us                                                      | 181 us: 1.41x faster                                                        |
| sqlglot_parse            | 1.22 ms                                                     | 865 us: 1.40x faster                                                        |
| sqlglot_transpile        | 1.48 ms                                                     | 1.07 ms: 1.38x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.66 ms: 1.38x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 62.6 ms: 1.37x faster                                                       |
| float                    | 61.7 ms                                                     | 45.3 ms: 1.36x faster                                                       |
| pyflate                  | 409 ms                                                      | 303 ms: 1.35x faster                                                        |
| mako                     | 9.03 ms                                                     | 6.75 ms: 1.34x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 58.4 ms: 1.32x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.37 ms: 1.32x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 43.9 ms: 1.31x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 48.5 ms: 1.29x faster                                                       |
| scimark_sor              | 106 ms                                                      | 82.7 ms: 1.28x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 40.0 ms: 1.27x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 145 us: 1.26x faster                                                        |
| pycparser                | 930 ms                                                      | 746 ms: 1.25x faster                                                        |
| regex_compile            | 106 ms                                                      | 85.6 ms: 1.24x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.0 ms: 1.23x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.57 us: 1.21x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 16.3 ms: 1.21x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 41.9 ms: 1.20x faster                                                       |
| thrift                   | 617 us                                                      | 514 us: 1.20x faster                                                        |
| sympy_sum                | 107 ms                                                      | 89.2 ms: 1.20x faster                                                       |
| regex_dna                | 136 ms                                                      | 114 ms: 1.20x faster                                                        |
| pickle_pure_python       | 270 us                                                      | 227 us: 1.19x faster                                                        |
| tomli_loads              | 1.67 sec                                                    | 1.41 sec: 1.18x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.42 ms: 1.17x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.66 sec: 1.16x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.55 sec: 1.15x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.3 ms: 1.15x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.92 us: 1.15x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 35.7 ms: 1.15x faster                                                       |
| django_template          | 28.9 ms                                                     | 25.2 ms: 1.15x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 34.9 ms: 1.14x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 849 us: 1.13x faster                                                        |
| xml_etree_process        | 44.5 ms                                                     | 39.9 ms: 1.12x faster                                                       |
| sympy_str                | 194 ms                                                      | 175 ms: 1.11x faster                                                        |
| 2to3                     | 246 ms                                                      | 223 ms: 1.10x faster                                                        |
| pprint_pformat           | 1.22 sec                                                    | 1.11 sec: 1.10x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 89.1 ms: 1.09x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 14.2 ms: 1.08x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 191 ms: 1.07x faster                                                        |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.55 ms: 1.07x faster                                                       |
| json                     | 3.14 ms                                                     | 2.94 ms: 1.07x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 557 ms: 1.06x faster                                                        |
| nqueens                  | 66.6 ms                                                     | 63.2 ms: 1.05x faster                                                       |
| sympy_expand             | 314 ms                                                      | 300 ms: 1.05x faster                                                        |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.5 ms: 1.04x faster                                                       |
| nbody                    | 71.3 ms                                                     | 69.2 ms: 1.03x faster                                                       |
| async_generators         | 222 ms                                                      | 219 ms: 1.01x faster                                                        |
| scimark_fft              | 187 ms                                                      | 186 ms: 1.01x faster                                                        |
| pidigits                 | 149 ms                                                      | 150 ms: 1.01x slower                                                        |
| xml_etree_generate       | 55.5 ms                                                     | 56.1 ms: 1.01x slower                                                       |
| logging_format           | 6.76 us                                                     | 6.86 us: 1.02x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.48 us: 1.04x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.7 us: 1.05x slower                                                       |
| fannkuch                 | 256 ms                                                      | 270 ms: 1.06x slower                                                        |
| coverage                 | 39.0 ms                                                     | 46.1 ms: 1.18x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.67 ms: 1.19x slower                                                       |
| python_startup           | 20.6 ms                                                     | 25.1 ms: 1.22x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 19.0 ms: 1.23x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 84.8 ms: 1.37x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.00 ms: 1.42x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.21 ms: 1.51x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.23x faster                                                                |

Benchmark hidden because not significant (1): meteor_contest
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250225-3.14.0a5+-0142236/bm-20250225-pythonperf1-amd64-python-014223649c33b2febbcc-3.14.0a5+-0142236.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.239x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown