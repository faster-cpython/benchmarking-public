# Results vs. 3.10.4

- fork: python
- ref: 359c7dde3bb074e02968
- machine: windows-amd64
- commit hash: 359c7dd
- commit date: 2025-02-16
- overall geometric mean: 1.225x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 223 ms: 1.10x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.65 sec: 1.17x faster                                                      |
| html5lib       | 51.0 ms                                                     | 39.5 ms: 1.29x faster                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 416 ms: 2.66x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 224 ms: 2.35x faster                                                        |
| async_tree_none         | 435 ms                                                      | 190 ms: 2.29x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 343 ms: 1.86x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.27x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 46.8 ms: 1.32x faster                                                       |
| nbody          | 71.3 ms                                                     | 68.9 ms: 1.03x faster                                                       |
| pidigits       | 149 ms                                                      | 150 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 86.0 ms: 1.23x faster                                                       |
| regex_dna      | 136 ms                                                      | 114 ms: 1.20x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.42 ms: 1.16x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.3 ms: 1.08x faster                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.68 ms: 1.37x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 149 us: 1.23x faster                                                        |
| pickle_pure_python   | 270 us                                                      | 224 us: 1.20x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.45 sec: 1.15x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 40.0 ms: 1.11x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 89.6 ms: 1.08x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.1 ms: 1.03x faster                                                       |
| unpickle_list        | 2.71 us                                                     | 2.76 us: 1.02x slower                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 56.8 ms: 1.02x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 17.8 us: 1.04x slower                                                       |
| pickle_list          | 2.75 us                                                     | 2.95 us: 1.07x slower                                                       |
| json_loads           | 14.0 us                                                     | 15.7 us: 1.12x slower                                                       |
| pickle               | 6.85 us                                                     | 7.84 us: 1.14x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                                |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 24.6 ms: 1.19x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 18.7 ms: 1.20x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.20x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.89 ms: 1.31x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 16.3 ms: 1.21x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 35.3 ms: 1.16x faster                                                       |
| django_template | 28.9 ms                                                     | 24.9 ms: 1.16x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.21x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 110 us: 3.05x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 416 ms: 2.66x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 29.1 ms: 2.60x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 224 ms: 2.35x faster                                                        |
| async_tree_none          | 435 ms                                                      | 190 ms: 2.29x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.24 ms: 1.87x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 343 ms: 1.86x faster                                                        |
| pylint                   | 350 ms                                                      | 197 ms: 1.78x faster                                                        |
| generators               | 32.4 ms                                                     | 19.6 ms: 1.65x faster                                                       |
| go                       | 139 ms                                                      | 90.3 ms: 1.54x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 62.5 ns: 1.51x faster                                                       |
| richards_super           | 52.2 ms                                                     | 34.7 ms: 1.50x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.44 sec: 1.47x faster                                                      |
| comprehensions           | 16.5 us                                                     | 11.3 us: 1.46x faster                                                       |
| chaos                    | 61.7 ms                                                     | 42.5 ms: 1.45x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 521 ms: 1.41x faster                                                        |
| richards                 | 42.4 ms                                                     | 30.3 ms: 1.40x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 20.6 us: 1.39x faster                                                       |
| raytrace                 | 273 ms                                                      | 197 ms: 1.38x faster                                                        |
| json_dumps               | 9.16 ms                                                     | 6.68 ms: 1.37x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 888 us: 1.37x faster                                                        |
| deepcopy                 | 255 us                                                      | 187 us: 1.37x faster                                                        |
| sqlglot_transpile        | 1.48 ms                                                     | 1.10 ms: 1.34x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 64.0 ms: 1.34x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.30 ms: 1.33x faster                                                       |
| pyflate                  | 409 ms                                                      | 309 ms: 1.32x faster                                                        |
| float                    | 61.7 ms                                                     | 46.8 ms: 1.32x faster                                                       |
| mako                     | 9.03 ms                                                     | 6.89 ms: 1.31x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 39.5 ms: 1.29x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 48.5 ms: 1.29x faster                                                       |
| pycparser                | 930 ms                                                      | 728 ms: 1.28x faster                                                        |
| spectral_norm            | 77.3 ms                                                     | 60.7 ms: 1.27x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 46.4 ms: 1.23x faster                                                       |
| regex_compile            | 106 ms                                                      | 86.0 ms: 1.23x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 149 us: 1.23x faster                                                        |
| sqlite_synth             | 1.91 us                                                     | 1.56 us: 1.22x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 16.3 ms: 1.21x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 41.6 ms: 1.21x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 224 us: 1.20x faster                                                        |
| thrift                   | 617 us                                                      | 516 us: 1.20x faster                                                        |
| regex_dna                | 136 ms                                                      | 114 ms: 1.20x faster                                                        |
| sympy_sum                | 107 ms                                                      | 89.9 ms: 1.19x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.6 ms: 1.18x faster                                                       |
| scimark_sor              | 106 ms                                                      | 90.7 ms: 1.17x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.65 sec: 1.17x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 35.3 ms: 1.16x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.42 ms: 1.16x faster                                                       |
| django_template          | 28.9 ms                                                     | 24.9 ms: 1.16x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.45 sec: 1.15x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 832 us: 1.15x faster                                                        |
| mdp                      | 1.78 sec                                                    | 1.55 sec: 1.15x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.92 us: 1.15x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.3 ms: 1.15x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 35.5 ms: 1.12x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 40.0 ms: 1.11x faster                                                       |
| sympy_str                | 194 ms                                                      | 176 ms: 1.11x faster                                                        |
| 2to3                     | 246 ms                                                      | 223 ms: 1.10x faster                                                        |
| pprint_pformat           | 1.22 sec                                                    | 1.12 sec: 1.09x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 61.2 ms: 1.09x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 89.6 ms: 1.08x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 14.3 ms: 1.08x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 549 ms: 1.08x faster                                                        |
| sqlglot_normalize        | 205 ms                                                      | 191 ms: 1.07x faster                                                        |
| sympy_expand             | 314 ms                                                      | 302 ms: 1.04x faster                                                        |
| nbody                    | 71.3 ms                                                     | 68.9 ms: 1.03x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.1 ms: 1.03x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.68 ms: 1.02x faster                                                       |
| json                     | 3.14 ms                                                     | 3.09 ms: 1.02x faster                                                       |
| pidigits                 | 149 ms                                                      | 150 ms: 1.01x slower                                                        |
| logging_format           | 6.76 us                                                     | 6.84 us: 1.01x slower                                                       |
| scimark_fft              | 187 ms                                                      | 190 ms: 1.02x slower                                                        |
| logging_simple           | 6.22 us                                                     | 6.33 us: 1.02x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 2.76 us: 1.02x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 56.8 ms: 1.02x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 17.8 us: 1.04x slower                                                       |
| pickle_list              | 2.75 us                                                     | 2.95 us: 1.07x slower                                                       |
| fannkuch                 | 256 ms                                                      | 276 ms: 1.08x slower                                                        |
| unpack_sequence          | 39.6 ns                                                     | 43.9 ns: 1.11x slower                                                       |
| json_loads               | 14.0 us                                                     | 15.7 us: 1.12x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.84 us: 1.14x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.69 ms: 1.19x slower                                                       |
| python_startup           | 20.6 ms                                                     | 24.6 ms: 1.19x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 18.7 ms: 1.20x slower                                                       |
| coverage                 | 39.0 ms                                                     | 48.1 ms: 1.23x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 83.5 ms: 1.35x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.00 ms: 1.42x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.22 ms: 1.52x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.20x faster                                                                |

Benchmark hidden because not significant (3): unpickle, meteor_contest, async_generators
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (12) of results/bm-20250216-3.14.0a5+-359c7dd/bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.225x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: unknown