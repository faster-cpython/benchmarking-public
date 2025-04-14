# Results vs. 3.10.4

- fork: python
- ref: 2498c22fa0a2b560491b
- machine: windows-amd64
- commit hash: 2498c22
- commit date: 2025-02-19
- overall geometric mean: 1.233x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250219-pythonperf1-amd64-python-2498c22fa0a2b560491b-3.14.0a5+-2498c22 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 223 ms: 1.10x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.65 sec: 1.16x faster                                                      |
| html5lib       | 51.0 ms                                                     | 39.7 ms: 1.29x faster                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250219-pythonperf1-amd64-python-2498c22fa0a2b560491b-3.14.0a5+-2498c22 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 416 ms: 2.66x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 218 ms: 2.42x faster                                                        |
| async_tree_none         | 435 ms                                                      | 187 ms: 2.33x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 337 ms: 1.89x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.31x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250219-pythonperf1-amd64-python-2498c22fa0a2b560491b-3.14.0a5+-2498c22 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 45.4 ms: 1.36x faster                                                       |
| pidigits       | 149 ms                                                      | 153 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                       | 1.10x faster                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250219-pythonperf1-amd64-python-2498c22fa0a2b560491b-3.14.0a5+-2498c22 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 85.2 ms: 1.24x faster                                                       |
| regex_dna      | 136 ms                                                      | 114 ms: 1.20x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.46 ms: 1.14x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.4 ms: 1.07x faster                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250219-pythonperf1-amd64-python-2498c22fa0a2b560491b-3.14.0a5+-2498c22 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.75 ms: 1.36x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 147 us: 1.25x faster                                                        |
| pickle_pure_python   | 270 us                                                      | 224 us: 1.20x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.41 sec: 1.18x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 39.8 ms: 1.12x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 92.7 ms: 1.04x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.6 ms: 1.04x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 56.6 ms: 1.02x slower                                                       |
| json_loads           | 14.0 us                                                     | 15.0 us: 1.07x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250219-pythonperf1-amd64-python-2498c22fa0a2b560491b-3.14.0a5+-2498c22 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 24.8 ms: 1.20x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 19.0 ms: 1.23x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.22x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250219-pythonperf1-amd64-python-2498c22fa0a2b560491b-3.14.0a5+-2498c22 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.81 ms: 1.33x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 16.2 ms: 1.22x faster                                                       |
| django_template | 28.9 ms                                                     | 24.8 ms: 1.17x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 35.5 ms: 1.16x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.22x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250219-pythonperf1-amd64-python-2498c22fa0a2b560491b-3.14.0a5+-2498c22 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 105 us: 3.20x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 416 ms: 2.66x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 29.5 ms: 2.57x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 218 ms: 2.42x faster                                                        |
| async_tree_none          | 435 ms                                                      | 187 ms: 2.33x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.19 ms: 1.91x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 337 ms: 1.89x faster                                                        |
| pylint                   | 350 ms                                                      | 197 ms: 1.78x faster                                                        |
| generators               | 32.4 ms                                                     | 19.4 ms: 1.67x faster                                                       |
| go                       | 139 ms                                                      | 84.5 ms: 1.64x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 58.2 ns: 1.62x faster                                                       |
| richards_super           | 52.2 ms                                                     | 33.8 ms: 1.55x faster                                                       |
| chaos                    | 61.7 ms                                                     | 41.8 ms: 1.48x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.3 us: 1.46x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 20.0 us: 1.44x faster                                                       |
| richards                 | 42.4 ms                                                     | 29.7 ms: 1.43x faster                                                       |
| deepcopy                 | 255 us                                                      | 183 us: 1.40x faster                                                        |
| raytrace                 | 273 ms                                                      | 196 ms: 1.39x faster                                                        |
| sqlglot_parse            | 1.22 ms                                                     | 885 us: 1.37x faster                                                        |
| hexiom                   | 5.74 ms                                                     | 4.19 ms: 1.37x faster                                                       |
| float                    | 61.7 ms                                                     | 45.4 ms: 1.36x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.75 ms: 1.36x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.10 ms: 1.34x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 64.2 ms: 1.34x faster                                                       |
| mako                     | 9.03 ms                                                     | 6.81 ms: 1.33x faster                                                       |
| pyflate                  | 409 ms                                                      | 310 ms: 1.32x faster                                                        |
| html5lib                 | 51.0 ms                                                     | 39.7 ms: 1.29x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 61.0 ms: 1.27x faster                                                       |
| pycparser                | 930 ms                                                      | 739 ms: 1.26x faster                                                        |
| crypto_pyaes             | 62.5 ms                                                     | 49.9 ms: 1.25x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 147 us: 1.25x faster                                                        |
| regex_compile            | 106 ms                                                      | 85.2 ms: 1.24x faster                                                       |
| thrift                   | 617 us                                                      | 498 us: 1.24x faster                                                        |
| scimark_sor              | 106 ms                                                      | 85.8 ms: 1.24x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 46.3 ms: 1.24x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.56 us: 1.22x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 16.2 ms: 1.22x faster                                                       |
| sympy_sum                | 107 ms                                                      | 88.2 ms: 1.21x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.2 ms: 1.21x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 41.7 ms: 1.21x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 224 us: 1.20x faster                                                        |
| regex_dna                | 136 ms                                                      | 114 ms: 1.20x faster                                                        |
| tomli_loads              | 1.67 sec                                                    | 1.41 sec: 1.18x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.8 ms: 1.17x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.65 sec: 1.16x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.90 us: 1.16x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 35.5 ms: 1.16x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.54 sec: 1.16x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.2 ms: 1.15x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 831 us: 1.15x faster                                                        |
| sqlglot_optimize         | 39.8 ms                                                     | 34.7 ms: 1.15x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.46 ms: 1.14x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.08 sec: 1.13x faster                                                      |
| sympy_str                | 194 ms                                                      | 173 ms: 1.12x faster                                                        |
| xml_etree_process        | 44.5 ms                                                     | 39.8 ms: 1.12x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 534 ms: 1.11x faster                                                        |
| 2to3                     | 246 ms                                                      | 223 ms: 1.10x faster                                                        |
| sqlglot_normalize        | 205 ms                                                      | 190 ms: 1.08x faster                                                        |
| regex_v8                 | 15.4 ms                                                     | 14.4 ms: 1.07x faster                                                       |
| sympy_expand             | 314 ms                                                      | 297 ms: 1.06x faster                                                        |
| nqueens                  | 66.6 ms                                                     | 63.4 ms: 1.05x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 92.7 ms: 1.04x faster                                                       |
| json                     | 3.14 ms                                                     | 3.00 ms: 1.04x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.6 ms: 1.04x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 74.9 ms: 1.01x faster                                                       |
| async_generators         | 222 ms                                                      | 223 ms: 1.00x slower                                                        |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.76 ms: 1.01x slower                                                       |
| logging_format           | 6.76 us                                                     | 6.88 us: 1.02x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 56.6 ms: 1.02x slower                                                       |
| pidigits                 | 149 ms                                                      | 153 ms: 1.02x slower                                                        |
| logging_simple           | 6.22 us                                                     | 6.42 us: 1.03x slower                                                       |
| scimark_fft              | 187 ms                                                      | 194 ms: 1.03x slower                                                        |
| fannkuch                 | 256 ms                                                      | 273 ms: 1.07x slower                                                        |
| json_loads               | 14.0 us                                                     | 15.0 us: 1.07x slower                                                       |
| python_startup           | 20.6 ms                                                     | 24.8 ms: 1.20x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.74 ms: 1.20x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 19.0 ms: 1.23x slower                                                       |
| coverage                 | 39.0 ms                                                     | 48.1 ms: 1.23x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 84.9 ms: 1.37x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.97 ms: 1.40x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.22 ms: 1.52x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.23x faster                                                                |

Benchmark hidden because not significant (1): nbody
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250219-3.14.0a5+-2498c22/bm-20250219-pythonperf1-amd64-python-2498c22fa0a2b560491b-3.14.0a5+-2498c22.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.233x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown