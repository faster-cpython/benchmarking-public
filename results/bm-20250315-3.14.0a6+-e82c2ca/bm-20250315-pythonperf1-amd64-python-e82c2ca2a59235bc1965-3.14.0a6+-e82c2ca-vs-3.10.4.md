# Results vs. 3.10.4

- fork: python
- ref: e82c2ca2a59235bc1965
- machine: windows-amd64
- commit hash: e82c2ca
- commit date: 2025-03-15
- overall geometric mean: 1.212x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 226 ms: 1.09x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.69 sec: 1.13x faster                                                      |
| html5lib       | 51.0 ms                                                     | 40.6 ms: 1.26x faster                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 427 ms: 2.59x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 222 ms: 2.37x faster                                                        |
| async_tree_none         | 435 ms                                                      | 190 ms: 2.29x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 342 ms: 1.87x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.26x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 46.1 ms: 1.34x faster                                                       |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                       | 1.10x faster                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 86.8 ms: 1.22x faster                                                       |
| regex_dna      | 136 ms                                                      | 114 ms: 1.20x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.40 ms: 1.18x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 13.8 ms: 1.12x faster                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.99 ms: 1.31x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 151 us: 1.21x faster                                                        |
| pickle_pure_python   | 270 us                                                      | 227 us: 1.19x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.46 sec: 1.15x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 88.3 ms: 1.10x faster                                                       |
| unpickle             | 9.09 us                                                     | 8.49 us: 1.07x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 41.6 ms: 1.07x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 64.2 ms: 1.01x faster                                                       |
| unpickle_list        | 2.71 us                                                     | 2.79 us: 1.03x slower                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 58.8 ms: 1.06x slower                                                       |
| json_loads           | 14.0 us                                                     | 15.1 us: 1.08x slower                                                       |
| pickle               | 6.85 us                                                     | 8.03 us: 1.17x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 20.6 us: 1.20x slower                                                       |
| pickle_list          | 2.75 us                                                     | 3.51 us: 1.28x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 26.1 ms: 1.27x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 20.4 ms: 1.32x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.29x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.84 ms: 1.32x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 17.5 ms: 1.13x faster                                                       |
| django_template | 28.9 ms                                                     | 26.6 ms: 1.09x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 38.0 ms: 1.08x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.15x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 114 us: 2.95x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 427 ms: 2.59x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 222 ms: 2.37x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 32.6 ms: 2.32x faster                                                       |
| async_tree_none          | 435 ms                                                      | 190 ms: 2.29x faster                                                        |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 342 ms: 1.87x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.25 ms: 1.86x faster                                                       |
| pylint                   | 350 ms                                                      | 204 ms: 1.72x faster                                                        |
| generators               | 32.4 ms                                                     | 19.5 ms: 1.66x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 59.5 ns: 1.59x faster                                                       |
| richards_super           | 52.2 ms                                                     | 33.4 ms: 1.56x faster                                                       |
| go                       | 139 ms                                                      | 91.5 ms: 1.52x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 19.2 us: 1.50x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.43 sec: 1.47x faster                                                      |
| richards                 | 42.4 ms                                                     | 29.3 ms: 1.45x faster                                                       |
| chaos                    | 61.7 ms                                                     | 43.7 ms: 1.41x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 61.0 ms: 1.41x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 524 ms: 1.40x faster                                                        |
| spectral_norm            | 77.3 ms                                                     | 55.3 ms: 1.40x faster                                                       |
| raytrace                 | 273 ms                                                      | 197 ms: 1.38x faster                                                        |
| comprehensions           | 16.5 us                                                     | 12.1 us: 1.37x faster                                                       |
| deepcopy                 | 255 us                                                      | 188 us: 1.36x faster                                                        |
| float                    | 61.7 ms                                                     | 46.1 ms: 1.34x faster                                                       |
| mako                     | 9.03 ms                                                     | 6.84 ms: 1.32x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.99 ms: 1.31x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.39 ms: 1.31x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 43.8 ms: 1.31x faster                                                       |
| pyflate                  | 409 ms                                                      | 314 ms: 1.30x faster                                                        |
| scimark_sor              | 106 ms                                                      | 83.4 ms: 1.27x faster                                                       |
| pycparser                | 930 ms                                                      | 738 ms: 1.26x faster                                                        |
| html5lib                 | 51.0 ms                                                     | 40.6 ms: 1.26x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 50.1 ms: 1.25x faster                                                       |
| regex_compile            | 106 ms                                                      | 86.8 ms: 1.22x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.57 us: 1.22x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 151 us: 1.21x faster                                                        |
| regex_dna                | 136 ms                                                      | 114 ms: 1.20x faster                                                        |
| dulwich_log              | 50.5 ms                                                     | 42.2 ms: 1.20x faster                                                       |
| sympy_sum                | 107 ms                                                      | 90.1 ms: 1.19x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.5 ms: 1.19x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 227 us: 1.19x faster                                                        |
| regex_effbot             | 1.66 ms                                                     | 1.40 ms: 1.18x faster                                                       |
| thrift                   | 617 us                                                      | 530 us: 1.17x faster                                                        |
| tomli_loads              | 1.67 sec                                                    | 1.46 sec: 1.15x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.3 ms: 1.15x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.69 sec: 1.13x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 17.5 ms: 1.13x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 13.8 ms: 1.12x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 863 us: 1.11x faster                                                        |
| pprint_pformat           | 1.22 sec                                                    | 1.11 sec: 1.10x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 88.3 ms: 1.10x faster                                                       |
| sympy_str                | 194 ms                                                      | 178 ms: 1.09x faster                                                        |
| deepcopy_reduce          | 2.20 us                                                     | 2.02 us: 1.09x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.64 sec: 1.09x faster                                                      |
| django_template          | 28.9 ms                                                     | 26.6 ms: 1.09x faster                                                       |
| 2to3                     | 246 ms                                                      | 226 ms: 1.09x faster                                                        |
| pprint_safe_repr         | 592 ms                                                      | 547 ms: 1.08x faster                                                        |
| genshi_xml               | 41.0 ms                                                     | 38.0 ms: 1.08x faster                                                       |
| unpickle                 | 9.09 us                                                     | 8.49 us: 1.07x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 41.6 ms: 1.07x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.56 ms: 1.06x faster                                                       |
| sympy_expand             | 314 ms                                                      | 306 ms: 1.03x faster                                                        |
| nqueens                  | 66.6 ms                                                     | 65.5 ms: 1.02x faster                                                       |
| scimark_fft              | 187 ms                                                      | 184 ms: 1.02x faster                                                        |
| json                     | 3.14 ms                                                     | 3.09 ms: 1.01x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 64.2 ms: 1.01x faster                                                       |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                                        |
| meteor_contest           | 75.9 ms                                                     | 77.2 ms: 1.02x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 2.79 us: 1.03x slower                                                       |
| unpack_sequence          | 39.6 ns                                                     | 41.4 ns: 1.04x slower                                                       |
| async_generators         | 222 ms                                                      | 234 ms: 1.06x slower                                                        |
| xml_etree_generate       | 55.5 ms                                                     | 58.8 ms: 1.06x slower                                                       |
| logging_format           | 6.76 us                                                     | 7.26 us: 1.07x slower                                                       |
| json_loads               | 14.0 us                                                     | 15.1 us: 1.08x slower                                                       |
| fannkuch                 | 256 ms                                                      | 276 ms: 1.08x slower                                                        |
| logging_simple           | 6.22 us                                                     | 6.73 us: 1.08x slower                                                       |
| pickle                   | 6.85 us                                                     | 8.03 us: 1.17x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 20.6 us: 1.20x slower                                                       |
| coverage                 | 39.0 ms                                                     | 48.0 ms: 1.23x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.92 ms: 1.25x slower                                                       |
| python_startup           | 20.6 ms                                                     | 26.1 ms: 1.27x slower                                                       |
| pickle_list              | 2.75 us                                                     | 3.51 us: 1.28x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 20.4 ms: 1.32x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 89.1 ms: 1.44x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.04 ms: 1.45x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.25 ms: 1.56x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.18x faster                                                                |

Benchmark hidden because not significant (1): nbody
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250315-3.14.0a6+-e82c2ca/bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.212x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown