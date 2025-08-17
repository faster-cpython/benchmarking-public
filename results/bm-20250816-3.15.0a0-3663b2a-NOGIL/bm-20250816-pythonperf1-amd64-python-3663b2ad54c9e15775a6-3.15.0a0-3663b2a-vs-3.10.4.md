# Results vs. 3.10.4

- fork: python
- ref: 3663b2ad54c9e15775a6
- machine: windows-amd64
- commit hash: 3663b2a
- commit date: 2025-08-16
- overall geometric mean: 1.167x faster
- HPT reliability: 99.95%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 224 ms: 1.10x faster                                                       |
| docutils       | 1.92 sec                                                    | 2.79 sec: 1.45x slower                                                     |
| html5lib       | 51.0 ms                                                     | 39.2 ms: 1.30x faster                                                      |
| Geometric mean | (ref)                                                       | 1.00x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 344 ms: 3.22x faster                                                       |
| async_tree_none         | 435 ms                                                      | 168 ms: 2.60x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 207 ms: 2.55x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 326 ms: 1.96x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.54x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 45.6 ms: 1.35x faster                                                      |
| pidigits       | 149 ms                                                      | 134 ms: 1.11x faster                                                       |
| nbody          | 71.3 ms                                                     | 83.1 ms: 1.17x slower                                                      |
| Geometric mean | (ref)                                                       | 1.09x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 113 ms: 1.21x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 13.4 ms: 1.15x faster                                                      |
| regex_compile  | 106 ms                                                      | 92.6 ms: 1.15x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                                      |
| Geometric mean | (ref)                                                       | 1.14x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.86 ms: 1.56x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 159 us: 1.16x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 235 us: 1.15x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 57.7 ms: 1.13x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 90.4 ms: 1.07x faster                                                      |
| unpickle             | 9.09 us                                                     | 9.80 us: 1.08x slower                                                      |
| json_loads           | 14.0 us                                                     | 15.5 us: 1.10x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.06 us: 1.11x slower                                                      |
| pickle               | 6.85 us                                                     | 7.73 us: 1.13x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 63.1 ms: 1.14x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 19.7 us: 1.15x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 3.14 us: 1.16x slower                                                      |
| tomli_loads          | 1.67 sec                                                    | 2.42 sec: 1.45x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.1 ms: 1.23x slower                                                      |
| python_startup         | 20.6 ms                                                     | 25.4 ms: 1.23x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.23x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 28.9 ms                                                     | 27.2 ms: 1.06x faster                                                      |
| mako            | 9.03 ms                                                     | 9.92 ms: 1.10x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.00x slower                                                               |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io            | 1.11 sec                                                    | 344 ms: 3.22x faster                                                       |
| typing_runtime_protocols | 336 us                                                      | 127 us: 2.64x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 28.7 ms: 2.64x faster                                                      |
| async_tree_none          | 435 ms                                                      | 168 ms: 2.60x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 207 ms: 2.55x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 326 ms: 1.96x faster                                                       |
| pylint                   | 350 ms                                                      | 198 ms: 1.77x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.44 ms: 1.71x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.05 sec: 1.69x faster                                                     |
| asyncio_tcp              | 732 ms                                                      | 459 ms: 1.60x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 5.86 ms: 1.56x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 62.0 ns: 1.53x faster                                                      |
| go                       | 139 ms                                                      | 91.5 ms: 1.52x faster                                                      |
| generators               | 32.4 ms                                                     | 22.5 ms: 1.44x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.34 us: 1.43x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 21.0 us: 1.37x faster                                                      |
| chaos                    | 61.7 ms                                                     | 45.2 ms: 1.37x faster                                                      |
| comprehensions           | 16.5 us                                                     | 12.1 us: 1.36x faster                                                      |
| float                    | 61.7 ms                                                     | 45.6 ms: 1.35x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 64.0 ms: 1.34x faster                                                      |
| pyflate                  | 409 ms                                                      | 309 ms: 1.33x faster                                                       |
| raytrace                 | 273 ms                                                      | 207 ms: 1.32x faster                                                       |
| richards_super           | 52.2 ms                                                     | 39.9 ms: 1.31x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 39.2 ms: 1.30x faster                                                      |
| pycparser                | 930 ms                                                      | 715 ms: 1.30x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.59 ms: 1.25x faster                                                      |
| richards                 | 42.4 ms                                                     | 34.1 ms: 1.25x faster                                                      |
| deepcopy                 | 255 us                                                      | 205 us: 1.25x faster                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.14 ms: 1.24x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 40.8 ms: 1.24x faster                                                      |
| scimark_sor              | 106 ms                                                      | 86.4 ms: 1.23x faster                                                      |
| regex_dna                | 136 ms                                                      | 113 ms: 1.21x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 159 us: 1.16x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 13.4 ms: 1.15x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 235 us: 1.15x faster                                                       |
| regex_compile            | 106 ms                                                      | 92.6 ms: 1.15x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 57.7 ms: 1.13x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 50.9 ms: 1.13x faster                                                      |
| sympy_sum                | 107 ms                                                      | 95.5 ms: 1.12x faster                                                      |
| pidigits                 | 149 ms                                                      | 134 ms: 1.11x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 56.2 ms: 1.11x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.9 ms: 1.10x faster                                                      |
| 2to3                     | 246 ms                                                      | 224 ms: 1.10x faster                                                       |
| thrift                   | 617 us                                                      | 571 us: 1.08x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 90.4 ms: 1.07x faster                                                      |
| django_template          | 28.9 ms                                                     | 27.2 ms: 1.06x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 560 ms: 1.06x faster                                                       |
| json                     | 3.14 ms                                                     | 3.00 ms: 1.04x faster                                                      |
| coroutines               | 16.0 ms                                                     | 15.4 ms: 1.04x faster                                                      |
| sympy_str                | 194 ms                                                      | 187 ms: 1.04x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 76.9 ms: 1.00x faster                                                      |
| sympy_expand             | 314 ms                                                      | 316 ms: 1.01x slower                                                       |
| unpack_sequence          | 39.6 ns                                                     | 40.1 ns: 1.01x slower                                                      |
| logging_format           | 6.76 us                                                     | 7.00 us: 1.04x slower                                                      |
| logging_simple           | 6.22 us                                                     | 6.58 us: 1.06x slower                                                      |
| unpickle                 | 9.09 us                                                     | 9.80 us: 1.08x slower                                                      |
| nqueens                  | 66.6 ms                                                     | 72.1 ms: 1.08x slower                                                      |
| mako                     | 9.03 ms                                                     | 9.92 ms: 1.10x slower                                                      |
| json_loads               | 14.0 us                                                     | 15.5 us: 1.10x slower                                                      |
| bench_thread_pool        | 958 us                                                      | 1.06 ms: 1.11x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.06 us: 1.11x slower                                                      |
| scimark_fft              | 187 ms                                                      | 211 ms: 1.13x slower                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 3.07 ms: 1.13x slower                                                      |
| pickle                   | 6.85 us                                                     | 7.73 us: 1.13x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 85.9 ms: 1.13x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 63.1 ms: 1.14x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 19.7 us: 1.15x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 3.14 us: 1.16x slower                                                      |
| async_generators         | 222 ms                                                      | 258 ms: 1.16x slower                                                       |
| nbody                    | 71.3 ms                                                     | 83.1 ms: 1.17x slower                                                      |
| fannkuch                 | 256 ms                                                      | 299 ms: 1.17x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 982 us: 1.23x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 19.1 ms: 1.23x slower                                                      |
| python_startup           | 20.6 ms                                                     | 25.4 ms: 1.23x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 77.5 ms: 1.25x slower                                                      |
| telco                    | 3.94 ms                                                     | 5.03 ms: 1.28x slower                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.63 sec: 1.33x slower                                                     |
| tomli_loads              | 1.67 sec                                                    | 2.42 sec: 1.45x slower                                                     |
| docutils                 | 1.92 sec                                                    | 2.79 sec: 1.45x slower                                                     |
| coverage                 | 39.0 ms                                                     | 67.7 ms: 1.74x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.14x faster                                                               |

Benchmark hidden because not significant (5): asyncio_tcp_ssl, genshi_text, genshi_xml, deepcopy_reduce, xml_etree_process
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250816-3.15.0a0-3663b2a-NOGIL/bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.167x faster

# HPT report

- Reliability score: 99.95% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown