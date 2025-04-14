# Results vs. 3.10.4

- fork: python
- ref: 155c44b9015089eacc6e
- machine: windows-amd64
- commit hash: 155c44b
- commit date: 2025-03-12
- overall geometric mean: 1.214x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-pythonperf1-amd64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 226 ms: 1.09x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.68 sec: 1.14x faster                                                      |
| html5lib       | 51.0 ms                                                     | 40.6 ms: 1.26x faster                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-pythonperf1-amd64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 424 ms: 2.62x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 222 ms: 2.37x faster                                                        |
| async_tree_none         | 435 ms                                                      | 189 ms: 2.30x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 339 ms: 1.88x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.28x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-pythonperf1-amd64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 46.1 ms: 1.34x faster                                                       |
| nbody          | 71.3 ms                                                     | 67.8 ms: 1.05x faster                                                       |
| pidigits       | 149 ms                                                      | 151 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-pythonperf1-amd64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 86.4 ms: 1.23x faster                                                       |
| regex_dna      | 136 ms                                                      | 119 ms: 1.14x faster                                                        |
| regex_v8       | 15.4 ms                                                     | 14.2 ms: 1.08x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.54 ms: 1.08x faster                                                       |
| Geometric mean | (ref)                                                       | 1.13x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-pythonperf1-amd64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.92 ms: 1.32x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 150 us: 1.23x faster                                                        |
| pickle_pure_python   | 270 us                                                      | 227 us: 1.19x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.44 sec: 1.16x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 90.8 ms: 1.07x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 42.6 ms: 1.04x faster                                                       |
| json_loads           | 14.0 us                                                     | 14.8 us: 1.05x slower                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 60.0 ms: 1.08x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.09x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-pythonperf1-amd64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 26.5 ms: 1.29x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 20.6 ms: 1.33x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.31x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-pythonperf1-amd64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.87 ms: 1.31x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 17.0 ms: 1.16x faster                                                       |
| django_template | 28.9 ms                                                     | 25.7 ms: 1.13x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 37.3 ms: 1.10x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.17x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-pythonperf1-amd64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 111 us: 3.03x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 424 ms: 2.62x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 222 ms: 2.37x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 32.1 ms: 2.36x faster                                                       |
| async_tree_none          | 435 ms                                                      | 189 ms: 2.30x faster                                                        |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 339 ms: 1.88x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.25 ms: 1.86x faster                                                       |
| pylint                   | 350 ms                                                      | 202 ms: 1.73x faster                                                        |
| generators               | 32.4 ms                                                     | 19.2 ms: 1.69x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 59.1 ns: 1.60x faster                                                       |
| go                       | 139 ms                                                      | 88.2 ms: 1.58x faster                                                       |
| richards_super           | 52.2 ms                                                     | 33.8 ms: 1.55x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 19.4 us: 1.48x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 60.0 ms: 1.43x faster                                                       |
| richards                 | 42.4 ms                                                     | 29.8 ms: 1.42x faster                                                       |
| deepcopy                 | 255 us                                                      | 181 us: 1.41x faster                                                        |
| chaos                    | 61.7 ms                                                     | 43.9 ms: 1.40x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.8 us: 1.39x faster                                                       |
| raytrace                 | 273 ms                                                      | 199 ms: 1.37x faster                                                        |
| float                    | 61.7 ms                                                     | 46.1 ms: 1.34x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.34 ms: 1.32x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.92 ms: 1.32x faster                                                       |
| mako                     | 9.03 ms                                                     | 6.87 ms: 1.31x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 59.3 ms: 1.30x faster                                                       |
| pyflate                  | 409 ms                                                      | 314 ms: 1.30x faster                                                        |
| scimark_monte_carlo      | 57.3 ms                                                     | 44.1 ms: 1.30x faster                                                       |
| scimark_sor              | 106 ms                                                      | 83.3 ms: 1.27x faster                                                       |
| pycparser                | 930 ms                                                      | 740 ms: 1.26x faster                                                        |
| html5lib                 | 51.0 ms                                                     | 40.6 ms: 1.26x faster                                                       |
| regex_compile            | 106 ms                                                      | 86.4 ms: 1.23x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 150 us: 1.23x faster                                                        |
| crypto_pyaes             | 62.5 ms                                                     | 51.3 ms: 1.22x faster                                                       |
| sympy_sum                | 107 ms                                                      | 89.4 ms: 1.20x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 42.4 ms: 1.19x faster                                                       |
| thrift                   | 617 us                                                      | 520 us: 1.19x faster                                                        |
| pickle_pure_python       | 270 us                                                      | 227 us: 1.19x faster                                                        |
| sqlite_synth             | 1.91 us                                                     | 1.62 us: 1.18x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.6 ms: 1.18x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 17.0 ms: 1.16x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.44 sec: 1.16x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.92 us: 1.15x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.3 ms: 1.15x faster                                                       |
| regex_dna                | 136 ms                                                      | 119 ms: 1.14x faster                                                        |
| docutils                 | 1.92 sec                                                    | 1.68 sec: 1.14x faster                                                      |
| django_template          | 28.9 ms                                                     | 25.7 ms: 1.13x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.59 sec: 1.12x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.09 sec: 1.12x faster                                                      |
| sympy_str                | 194 ms                                                      | 175 ms: 1.11x faster                                                        |
| bench_thread_pool        | 958 us                                                      | 865 us: 1.11x faster                                                        |
| genshi_xml               | 41.0 ms                                                     | 37.3 ms: 1.10x faster                                                       |
| 2to3                     | 246 ms                                                      | 226 ms: 1.09x faster                                                        |
| regex_v8                 | 15.4 ms                                                     | 14.2 ms: 1.08x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.54 ms: 1.08x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.54 ms: 1.07x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 90.8 ms: 1.07x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 558 ms: 1.06x faster                                                        |
| nbody                    | 71.3 ms                                                     | 67.8 ms: 1.05x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 42.6 ms: 1.04x faster                                                       |
| json                     | 3.14 ms                                                     | 3.01 ms: 1.04x faster                                                       |
| sympy_expand             | 314 ms                                                      | 303 ms: 1.04x faster                                                        |
| scimark_fft              | 187 ms                                                      | 181 ms: 1.03x faster                                                        |
| nqueens                  | 66.6 ms                                                     | 64.8 ms: 1.03x faster                                                       |
| pidigits                 | 149 ms                                                      | 151 ms: 1.01x slower                                                        |
| async_generators         | 222 ms                                                      | 228 ms: 1.03x slower                                                        |
| meteor_contest           | 75.9 ms                                                     | 78.3 ms: 1.03x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.8 us: 1.05x slower                                                       |
| logging_format           | 6.76 us                                                     | 7.16 us: 1.06x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.62 us: 1.06x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 60.0 ms: 1.08x slower                                                       |
| fannkuch                 | 256 ms                                                      | 283 ms: 1.11x slower                                                        |
| telco                    | 3.94 ms                                                     | 4.91 ms: 1.25x slower                                                       |
| coverage                 | 39.0 ms                                                     | 48.7 ms: 1.25x slower                                                       |
| python_startup           | 20.6 ms                                                     | 26.5 ms: 1.29x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 20.6 ms: 1.33x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 88.5 ms: 1.43x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.03 ms: 1.44x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.26 ms: 1.57x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.21x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250312-3.14.0a5+-155c44b/bm-20250312-pythonperf1-amd64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.214x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: unknown