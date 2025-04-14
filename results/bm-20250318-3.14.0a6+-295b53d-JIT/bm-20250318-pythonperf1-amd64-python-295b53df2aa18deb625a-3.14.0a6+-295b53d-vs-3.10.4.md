# Results vs. 3.10.4

- fork: python
- ref: 295b53df2aa18deb625a
- machine: windows-amd64
- commit hash: 295b53d
- commit date: 2025-03-18
- overall geometric mean: 1.235x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-pythonperf1-amd64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 227 ms: 1.08x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.75 sec: 1.09x faster                                                      |
| html5lib       | 51.0 ms                                                     | 41.3 ms: 1.24x faster                                                       |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-pythonperf1-amd64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 418 ms: 2.65x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 221 ms: 2.38x faster                                                        |
| async_tree_none         | 435 ms                                                      | 186 ms: 2.34x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 341 ms: 1.87x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.29x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-pythonperf1-amd64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 47.3 ms: 1.30x faster                                                       |
| nbody          | 71.3 ms                                                     | 58.6 ms: 1.22x faster                                                       |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-pythonperf1-amd64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 86.2 ms: 1.23x faster                                                       |
| regex_dna      | 136 ms                                                      | 117 ms: 1.17x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.45 ms: 1.14x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.2 ms: 1.08x faster                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-pythonperf1-amd64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 126 us: 1.46x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.22 sec: 1.37x faster                                                      |
| json_dumps           | 9.16 ms                                                     | 6.98 ms: 1.31x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 222 us: 1.22x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 38.9 ms: 1.14x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 87.6 ms: 1.10x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 53.0 ms: 1.05x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.1 ms: 1.03x faster                                                       |
| json_loads           | 14.0 us                                                     | 15.3 us: 1.09x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.17x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-pythonperf1-amd64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.8 ms: 1.25x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 20.6 ms: 1.33x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.29x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-pythonperf1-amd64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.81 ms: 1.55x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 16.9 ms: 1.17x faster                                                       |
| django_template | 28.9 ms                                                     | 26.2 ms: 1.10x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 38.3 ms: 1.07x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.21x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-pythonperf1-amd64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 112 us: 3.00x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 418 ms: 2.65x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 221 ms: 2.38x faster                                                        |
| async_tree_none          | 435 ms                                                      | 186 ms: 2.34x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 32.7 ms: 2.31x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 341 ms: 1.87x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.40 ms: 1.75x faster                                                       |
| pylint                   | 350 ms                                                      | 205 ms: 1.71x faster                                                        |
| deepcopy_memo            | 28.8 us                                                     | 18.0 us: 1.60x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 59.5 ns: 1.59x faster                                                       |
| richards_super           | 52.2 ms                                                     | 33.0 ms: 1.58x faster                                                       |
| generators               | 32.4 ms                                                     | 20.6 ms: 1.57x faster                                                       |
| go                       | 139 ms                                                      | 88.7 ms: 1.57x faster                                                       |
| mako                     | 9.03 ms                                                     | 5.81 ms: 1.55x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 126 us: 1.46x faster                                                        |
| pyflate                  | 409 ms                                                      | 283 ms: 1.45x faster                                                        |
| richards                 | 42.4 ms                                                     | 29.4 ms: 1.44x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.7 us: 1.41x faster                                                       |
| raytrace                 | 273 ms                                                      | 194 ms: 1.41x faster                                                        |
| chaos                    | 61.7 ms                                                     | 44.1 ms: 1.40x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 62.3 ms: 1.38x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.22 sec: 1.37x faster                                                      |
| deepcopy                 | 255 us                                                      | 193 us: 1.33x faster                                                        |
| spectral_norm            | 77.3 ms                                                     | 58.8 ms: 1.31x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.98 ms: 1.31x faster                                                       |
| float                    | 61.7 ms                                                     | 47.3 ms: 1.30x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 44.1 ms: 1.30x faster                                                       |
| scimark_sor              | 106 ms                                                      | 81.8 ms: 1.30x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.53 ms: 1.27x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.53 us: 1.25x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 50.1 ms: 1.25x faster                                                       |
| pycparser                | 930 ms                                                      | 750 ms: 1.24x faster                                                        |
| html5lib                 | 51.0 ms                                                     | 41.3 ms: 1.24x faster                                                       |
| regex_compile            | 106 ms                                                      | 86.2 ms: 1.23x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 222 us: 1.22x faster                                                        |
| nbody                    | 71.3 ms                                                     | 58.6 ms: 1.22x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.27 ms: 1.20x faster                                                       |
| scimark_fft              | 187 ms                                                      | 158 ms: 1.19x faster                                                        |
| genshi_text              | 19.8 ms                                                     | 16.9 ms: 1.17x faster                                                       |
| sympy_sum                | 107 ms                                                      | 91.7 ms: 1.17x faster                                                       |
| regex_dna                | 136 ms                                                      | 117 ms: 1.17x faster                                                        |
| dulwich_log              | 50.5 ms                                                     | 43.5 ms: 1.16x faster                                                       |
| thrift                   | 617 us                                                      | 537 us: 1.15x faster                                                        |
| xml_etree_process        | 44.5 ms                                                     | 38.9 ms: 1.14x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.45 ms: 1.14x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 519 ms: 1.14x faster                                                        |
| coroutines               | 16.0 ms                                                     | 14.1 ms: 1.14x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.5 ms: 1.13x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.58 sec: 1.12x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.10 sec: 1.11x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 87.6 ms: 1.10x faster                                                       |
| django_template          | 28.9 ms                                                     | 26.2 ms: 1.10x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 874 us: 1.10x faster                                                        |
| docutils                 | 1.92 sec                                                    | 1.75 sec: 1.09x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 2.03 us: 1.08x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 14.2 ms: 1.08x faster                                                       |
| 2to3                     | 246 ms                                                      | 227 ms: 1.08x faster                                                        |
| nqueens                  | 66.6 ms                                                     | 61.6 ms: 1.08x faster                                                       |
| sympy_str                | 194 ms                                                      | 180 ms: 1.08x faster                                                        |
| genshi_xml               | 41.0 ms                                                     | 38.3 ms: 1.07x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 53.0 ms: 1.05x faster                                                       |
| fannkuch                 | 256 ms                                                      | 246 ms: 1.04x faster                                                        |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.1 ms: 1.03x faster                                                       |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                                        |
| json                     | 3.14 ms                                                     | 3.16 ms: 1.01x slower                                                       |
| logging_format           | 6.76 us                                                     | 7.17 us: 1.06x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.63 us: 1.06x slower                                                       |
| json_loads               | 14.0 us                                                     | 15.3 us: 1.09x slower                                                       |
| async_generators         | 222 ms                                                      | 246 ms: 1.11x slower                                                        |
| telco                    | 3.94 ms                                                     | 4.58 ms: 1.16x slower                                                       |
| coverage                 | 39.0 ms                                                     | 47.4 ms: 1.21x slower                                                       |
| python_startup           | 20.6 ms                                                     | 25.8 ms: 1.25x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 20.6 ms: 1.33x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 89.1 ms: 1.44x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.04 ms: 1.45x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.25 ms: 1.57x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.22x faster                                                                |

Benchmark hidden because not significant (2): meteor_contest, sympy_expand
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250318-3.14.0a6+-295b53d-JIT/bm-20250318-pythonperf1-amd64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.235x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown