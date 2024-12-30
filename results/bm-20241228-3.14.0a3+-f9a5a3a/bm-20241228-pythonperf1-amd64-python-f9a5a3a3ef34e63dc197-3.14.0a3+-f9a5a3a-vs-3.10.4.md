# Results vs. 3.10.4

- fork: python
- ref: f9a5a3a3ef34e63dc197
- machine: windows-amd64
- commit hash: f9a5a3a
- commit date: 2024-12-28
- overall geometric mean: 1.181x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 227 ms: 1.08x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.68 sec: 1.14x faster                                                      |
| html5lib       | 51.0 ms                                                     | 40.1 ms: 1.27x faster                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 410 ms: 2.70x faster                                                        |
| async_tree_none         | 435 ms                                                      | 183 ms: 2.38x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 225 ms: 2.34x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 348 ms: 1.84x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.29x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 55.4 ms: 1.11x faster                                                       |
| pidigits       | 149 ms                                                      | 147 ms: 1.02x faster                                                        |
| nbody          | 71.3 ms                                                     | 83.2 ms: 1.17x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 88.2 ms: 1.20x faster                                                       |
| regex_dna      | 136 ms                                                      | 119 ms: 1.14x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.53 ms: 1.08x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 21.5 ms: 1.40x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.66 ms: 1.37x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 151 us: 1.21x faster                                                        |
| pickle_pure_python   | 270 us                                                      | 227 us: 1.19x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.43 sec: 1.17x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 87.5 ms: 1.11x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 40.8 ms: 1.09x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.1 ms: 1.03x faster                                                       |
| json_loads           | 14.0 us                                                     | 14.5 us: 1.03x slower                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 57.7 ms: 1.04x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 18.1 ms: 1.16x slower                                                       |
| python_startup         | 20.6 ms                                                     | 24.2 ms: 1.17x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.17x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 7.03 ms: 1.29x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 16.8 ms: 1.18x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 35.1 ms: 1.17x faster                                                       |
| django_template | 28.9 ms                                                     | 25.1 ms: 1.15x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.20x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 112 us: 2.99x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 410 ms: 2.70x faster                                                        |
| async_tree_none          | 435 ms                                                      | 183 ms: 2.38x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 225 ms: 2.34x faster                                                        |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 348 ms: 1.84x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.30 ms: 1.82x faster                                                       |
| pylint                   | 350 ms                                                      | 199 ms: 1.76x faster                                                        |
| go                       | 139 ms                                                      | 90.9 ms: 1.53x faster                                                       |
| generators               | 32.4 ms                                                     | 21.2 ms: 1.53x faster                                                       |
| richards_super           | 52.2 ms                                                     | 36.2 ms: 1.44x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 65.8 ns: 1.44x faster                                                       |
| chaos                    | 61.7 ms                                                     | 43.5 ms: 1.42x faster                                                       |
| raytrace                 | 273 ms                                                      | 198 ms: 1.38x faster                                                        |
| json_dumps               | 9.16 ms                                                     | 6.66 ms: 1.37x faster                                                       |
| deepcopy                 | 255 us                                                      | 186 us: 1.37x faster                                                        |
| scimark_lu               | 85.8 ms                                                     | 63.3 ms: 1.35x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 21.3 us: 1.35x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 909 us: 1.34x faster                                                        |
| richards                 | 42.4 ms                                                     | 32.1 ms: 1.32x faster                                                       |
| comprehensions           | 16.5 us                                                     | 12.5 us: 1.32x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.13 ms: 1.31x faster                                                       |
| pyflate                  | 409 ms                                                      | 316 ms: 1.29x faster                                                        |
| mako                     | 9.03 ms                                                     | 7.03 ms: 1.29x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 40.1 ms: 1.27x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 49.5 ms: 1.26x faster                                                       |
| pycparser                | 930 ms                                                      | 738 ms: 1.26x faster                                                        |
| hexiom                   | 5.74 ms                                                     | 4.59 ms: 1.25x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 62.8 ms: 1.23x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 151 us: 1.21x faster                                                        |
| regex_compile            | 106 ms                                                      | 88.2 ms: 1.20x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.48 sec: 1.20x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 47.7 ms: 1.20x faster                                                       |
| scimark_sor              | 106 ms                                                      | 88.8 ms: 1.19x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 227 us: 1.19x faster                                                        |
| sqlite_synth             | 1.91 us                                                     | 1.61 us: 1.19x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 42.7 ms: 1.18x faster                                                       |
| sympy_sum                | 107 ms                                                      | 90.4 ms: 1.18x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 16.8 ms: 1.18x faster                                                       |
| thrift                   | 617 us                                                      | 525 us: 1.18x faster                                                        |
| bench_thread_pool        | 958 us                                                      | 816 us: 1.17x faster                                                        |
| genshi_xml               | 41.0 ms                                                     | 35.1 ms: 1.17x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.7 ms: 1.17x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.43 sec: 1.17x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.90 us: 1.16x faster                                                       |
| django_template          | 28.9 ms                                                     | 25.1 ms: 1.15x faster                                                       |
| regex_dna                | 136 ms                                                      | 119 ms: 1.14x faster                                                        |
| docutils                 | 1.92 sec                                                    | 1.68 sec: 1.14x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.5 ms: 1.13x faster                                                       |
| float                    | 61.7 ms                                                     | 55.4 ms: 1.11x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 35.8 ms: 1.11x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 87.5 ms: 1.11x faster                                                       |
| sympy_str                | 194 ms                                                      | 178 ms: 1.09x faster                                                        |
| xml_etree_process        | 44.5 ms                                                     | 40.8 ms: 1.09x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.12 sec: 1.09x faster                                                      |
| 2to3                     | 246 ms                                                      | 227 ms: 1.08x faster                                                        |
| regex_effbot             | 1.66 ms                                                     | 1.53 ms: 1.08x faster                                                       |
| json                     | 3.14 ms                                                     | 2.93 ms: 1.07x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 553 ms: 1.07x faster                                                        |
| sqlglot_normalize        | 205 ms                                                      | 196 ms: 1.05x faster                                                        |
| sympy_expand             | 314 ms                                                      | 305 ms: 1.03x faster                                                        |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.1 ms: 1.03x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.66 ms: 1.02x faster                                                       |
| pidigits                 | 149 ms                                                      | 147 ms: 1.02x faster                                                        |
| nqueens                  | 66.6 ms                                                     | 66.3 ms: 1.00x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.83 us: 1.01x slower                                                       |
| meteor_contest           | 75.9 ms                                                     | 77.8 ms: 1.02x slower                                                       |
| scimark_fft              | 187 ms                                                      | 193 ms: 1.03x slower                                                        |
| json_loads               | 14.0 us                                                     | 14.5 us: 1.03x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.44 us: 1.03x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 57.7 ms: 1.04x slower                                                       |
| async_generators         | 222 ms                                                      | 238 ms: 1.07x slower                                                        |
| fannkuch                 | 256 ms                                                      | 287 ms: 1.12x slower                                                        |
| mypy2                    | 555 ms                                                      | 633 ms: 1.14x slower                                                        |
| python_startup_no_site   | 15.5 ms                                                     | 18.1 ms: 1.16x slower                                                       |
| nbody                    | 71.3 ms                                                     | 83.2 ms: 1.17x slower                                                       |
| python_startup           | 20.6 ms                                                     | 24.2 ms: 1.17x slower                                                       |
| coverage                 | 39.0 ms                                                     | 46.9 ms: 1.20x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.89 ms: 1.24x slower                                                       |
| regex_v8                 | 15.4 ms                                                     | 21.5 ms: 1.40x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.97 ms: 1.40x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 88.0 ms: 1.42x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.20 ms: 1.50x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.17x faster                                                                |

Benchmark hidden because not significant (1): pathlib
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241228-3.14.0a3+-f9a5a3a/bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.181x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown