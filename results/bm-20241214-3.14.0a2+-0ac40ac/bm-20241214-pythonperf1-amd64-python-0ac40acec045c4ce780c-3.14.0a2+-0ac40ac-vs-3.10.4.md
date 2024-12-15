# Results vs. 3.10.4

- fork: python
- ref: 0ac40acec045c4ce780c
- machine: windows-amd64
- commit hash: 0ac40ac
- commit date: 2024-12-14
- overall geometric mean: 1.190x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 223 ms: 1.10x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.66 sec: 1.16x faster                                                      |
| html5lib       | 51.0 ms                                                     | 40.6 ms: 1.26x faster                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 415 ms: 2.67x faster                                                        |
| async_tree_none         | 435 ms                                                      | 184 ms: 2.36x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 227 ms: 2.31x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 356 ms: 1.79x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.26x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 54.4 ms: 1.13x faster                                                       |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                                        |
| nbody          | 71.3 ms                                                     | 79.5 ms: 1.12x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 111 ms: 1.22x faster                                                        |
| regex_compile  | 106 ms                                                      | 89.2 ms: 1.19x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.40 ms: 1.19x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 24.5 ms: 1.59x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.73 ms: 1.36x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 147 us: 1.24x faster                                                        |
| pickle_pure_python   | 270 us                                                      | 222 us: 1.22x faster                                                        |
| xml_etree_parse      | 96.8 ms                                                     | 87.8 ms: 1.10x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.54 sec: 1.09x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 41.3 ms: 1.08x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.0 ms: 1.03x faster                                                       |
| json_loads           | 14.0 us                                                     | 14.4 us: 1.03x slower                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 57.5 ms: 1.03x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.11x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 17.4 ms: 1.12x slower                                                       |
| python_startup         | 20.6 ms                                                     | 23.2 ms: 1.12x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.76 ms: 1.34x faster                                                       |
| django_template | 28.9 ms                                                     | 24.9 ms: 1.16x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 17.2 ms: 1.15x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 37.1 ms: 1.10x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.18x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 114 us: 2.96x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 415 ms: 2.67x faster                                                        |
| async_tree_none          | 435 ms                                                      | 184 ms: 2.36x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 227 ms: 2.31x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.26 ms: 1.86x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 356 ms: 1.79x faster                                                        |
| pylint                   | 350 ms                                                      | 198 ms: 1.77x faster                                                        |
| go                       | 139 ms                                                      | 88.0 ms: 1.58x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 60.8 ns: 1.56x faster                                                       |
| generators               | 32.4 ms                                                     | 22.2 ms: 1.46x faster                                                       |
| richards_super           | 52.2 ms                                                     | 36.2 ms: 1.44x faster                                                       |
| raytrace                 | 273 ms                                                      | 191 ms: 1.43x faster                                                        |
| chaos                    | 61.7 ms                                                     | 43.9 ms: 1.41x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 61.5 ms: 1.40x faster                                                       |
| comprehensions           | 16.5 us                                                     | 12.0 us: 1.38x faster                                                       |
| deepcopy                 | 255 us                                                      | 187 us: 1.37x faster                                                        |
| sqlglot_parse            | 1.22 ms                                                     | 891 us: 1.36x faster                                                        |
| deepcopy_memo            | 28.8 us                                                     | 21.1 us: 1.36x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.73 ms: 1.36x faster                                                       |
| mako                     | 9.03 ms                                                     | 6.76 ms: 1.34x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.11 ms: 1.33x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.31 ms: 1.33x faster                                                       |
| richards                 | 42.4 ms                                                     | 32.0 ms: 1.33x faster                                                       |
| pyflate                  | 409 ms                                                      | 313 ms: 1.31x faster                                                        |
| crypto_pyaes             | 62.5 ms                                                     | 49.4 ms: 1.27x faster                                                       |
| pycparser                | 930 ms                                                      | 737 ms: 1.26x faster                                                        |
| html5lib                 | 51.0 ms                                                     | 40.6 ms: 1.26x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 62.0 ms: 1.25x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 147 us: 1.24x faster                                                        |
| mdp                      | 1.78 sec                                                    | 1.43 sec: 1.24x faster                                                      |
| regex_dna                | 136 ms                                                      | 111 ms: 1.22x faster                                                        |
| scimark_sor              | 106 ms                                                      | 87.1 ms: 1.22x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 222 us: 1.22x faster                                                        |
| scimark_monte_carlo      | 57.3 ms                                                     | 47.2 ms: 1.21x faster                                                       |
| sympy_sum                | 107 ms                                                      | 89.2 ms: 1.20x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.4 ms: 1.19x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.61 us: 1.19x faster                                                       |
| regex_compile            | 106 ms                                                      | 89.2 ms: 1.19x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.40 ms: 1.19x faster                                                       |
| thrift                   | 617 us                                                      | 522 us: 1.18x faster                                                        |
| dulwich_log              | 50.5 ms                                                     | 42.9 ms: 1.18x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 823 us: 1.16x faster                                                        |
| django_template          | 28.9 ms                                                     | 24.9 ms: 1.16x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.66 sec: 1.16x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 17.2 ms: 1.15x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.92 us: 1.15x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.3 ms: 1.15x faster                                                       |
| float                    | 61.7 ms                                                     | 54.4 ms: 1.13x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 35.9 ms: 1.11x faster                                                       |
| sympy_str                | 194 ms                                                      | 176 ms: 1.11x faster                                                        |
| genshi_xml               | 41.0 ms                                                     | 37.1 ms: 1.10x faster                                                       |
| 2to3                     | 246 ms                                                      | 223 ms: 1.10x faster                                                        |
| xml_etree_parse          | 96.8 ms                                                     | 87.8 ms: 1.10x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.11 sec: 1.10x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.54 sec: 1.09x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 41.3 ms: 1.08x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 556 ms: 1.06x faster                                                        |
| nqueens                  | 66.6 ms                                                     | 62.8 ms: 1.06x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.57 ms: 1.06x faster                                                       |
| json                     | 3.14 ms                                                     | 2.96 ms: 1.06x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 195 ms: 1.05x faster                                                        |
| sympy_expand             | 314 ms                                                      | 302 ms: 1.04x faster                                                        |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.0 ms: 1.03x faster                                                       |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                                        |
| scimark_fft              | 187 ms                                                      | 189 ms: 1.01x slower                                                        |
| logging_format           | 6.76 us                                                     | 6.86 us: 1.02x slower                                                       |
| meteor_contest           | 75.9 ms                                                     | 77.5 ms: 1.02x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.4 us: 1.03x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.42 us: 1.03x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 57.5 ms: 1.03x slower                                                       |
| fannkuch                 | 256 ms                                                      | 271 ms: 1.06x slower                                                        |
| async_generators         | 222 ms                                                      | 238 ms: 1.07x slower                                                        |
| nbody                    | 71.3 ms                                                     | 79.5 ms: 1.12x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 17.4 ms: 1.12x slower                                                       |
| python_startup           | 20.6 ms                                                     | 23.2 ms: 1.12x slower                                                       |
| mypy2                    | 555 ms                                                      | 632 ms: 1.14x slower                                                        |
| telco                    | 3.94 ms                                                     | 4.76 ms: 1.21x slower                                                       |
| coverage                 | 39.0 ms                                                     | 48.0 ms: 1.23x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 81.9 ms: 1.32x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.98 ms: 1.40x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.21 ms: 1.51x slower                                                       |
| regex_v8                 | 15.4 ms                                                     | 24.5 ms: 1.59x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.18x faster                                                                |

Benchmark hidden because not significant (1): pathlib
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.190x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown