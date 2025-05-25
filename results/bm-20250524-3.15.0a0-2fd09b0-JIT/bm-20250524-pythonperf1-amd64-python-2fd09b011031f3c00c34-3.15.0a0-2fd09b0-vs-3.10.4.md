# Results vs. 3.10.4

- fork: python
- ref: 2fd09b011031f3c00c34
- machine: windows-amd64
- commit hash: 2fd09b0
- commit date: 2025-05-24
- overall geometric mean: 1.196x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 219 ms: 1.12x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.67 sec: 1.15x faster                                                     |
| html5lib       | 51.0 ms                                                     | 38.4 ms: 1.33x faster                                                      |
| Geometric mean | (ref)                                                       | 1.20x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 390 ms: 2.84x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 199 ms: 2.64x faster                                                       |
| async_tree_none         | 435 ms                                                      | 165 ms: 2.63x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 329 ms: 1.94x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.49x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 42.9 ms: 1.44x faster                                                      |
| nbody          | 71.3 ms                                                     | 60.1 ms: 1.19x faster                                                      |
| pidigits       | 149 ms                                                      | 147 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.20x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 78.4 ms: 1.35x faster                                                      |
| regex_dna      | 136 ms                                                      | 117 ms: 1.17x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 13.7 ms: 1.13x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                                      |
| Geometric mean | (ref)                                                       | 1.18x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 111 us: 1.65x faster                                                       |
| json_dumps           | 9.16 ms                                                     | 6.20 ms: 1.48x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.14 sec: 1.47x faster                                                     |
| pickle_pure_python   | 270 us                                                      | 205 us: 1.31x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 36.2 ms: 1.23x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 88.7 ms: 1.09x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 51.2 ms: 1.08x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.47 us: 1.07x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.6 ms: 1.02x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.9 us: 1.06x slower                                                      |
| pickle               | 6.85 us                                                     | 7.52 us: 1.10x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 19.5 us: 1.13x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.31 us: 1.20x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.12x faster                                                               |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 18.5 ms: 1.19x slower                                                      |
| python_startup         | 20.6 ms                                                     | 24.6 ms: 1.19x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.19x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.54 ms: 1.63x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.4 ms: 1.29x faster                                                      |
| django_template | 28.9 ms                                                     | 23.6 ms: 1.22x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 34.3 ms: 1.20x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.32x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 108 us: 3.10x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 390 ms: 2.84x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 199 ms: 2.64x faster                                                       |
| async_tree_none          | 435 ms                                                      | 165 ms: 2.63x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 29.5 ms: 2.57x faster                                                      |
| mdp                      | 1.78 sec                                                    | 816 ms: 2.18x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.15 ms: 1.95x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 329 ms: 1.94x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 388 ms: 1.89x faster                                                       |
| go                       | 139 ms                                                      | 77.4 ms: 1.79x faster                                                      |
| pylint                   | 350 ms                                                      | 200 ms: 1.75x faster                                                       |
| richards_super           | 52.2 ms                                                     | 30.7 ms: 1.70x faster                                                      |
| generators               | 32.4 ms                                                     | 19.3 ms: 1.68x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 111 us: 1.65x faster                                                       |
| mako                     | 9.03 ms                                                     | 5.54 ms: 1.63x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.29 sec: 1.63x faster                                                     |
| deepcopy_memo            | 28.8 us                                                     | 17.8 us: 1.62x faster                                                      |
| chaos                    | 61.7 ms                                                     | 38.3 ms: 1.61x faster                                                      |
| pyflate                  | 409 ms                                                      | 257 ms: 1.59x faster                                                       |
| richards                 | 42.4 ms                                                     | 26.9 ms: 1.58x faster                                                      |
| raytrace                 | 273 ms                                                      | 178 ms: 1.54x faster                                                       |
| deepcopy                 | 255 us                                                      | 168 us: 1.52x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 56.7 ms: 1.51x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.20 ms: 1.48x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.14 sec: 1.47x faster                                                     |
| scimark_sor              | 106 ms                                                      | 72.8 ms: 1.46x faster                                                      |
| comprehensions           | 16.5 us                                                     | 11.4 us: 1.45x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 39.6 ms: 1.45x faster                                                      |
| float                    | 61.7 ms                                                     | 42.9 ms: 1.44x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.13 ms: 1.39x faster                                                      |
| regex_compile            | 106 ms                                                      | 78.4 ms: 1.35x faster                                                      |
| pycparser                | 930 ms                                                      | 693 ms: 1.34x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 46.7 ms: 1.34x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 38.4 ms: 1.33x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 205 us: 1.31x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 15.4 ms: 1.29x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 60.7 ms: 1.27x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.52 us: 1.26x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 40.5 ms: 1.25x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.78 us: 1.24x faster                                                      |
| sympy_sum                | 107 ms                                                      | 86.7 ms: 1.23x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 36.2 ms: 1.23x faster                                                      |
| django_template          | 28.9 ms                                                     | 23.6 ms: 1.22x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 12.6 ms: 1.21x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.26 ms: 1.21x faster                                                      |
| scimark_fft              | 187 ms                                                      | 156 ms: 1.20x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 34.3 ms: 1.20x faster                                                      |
| nbody                    | 71.3 ms                                                     | 60.1 ms: 1.19x faster                                                      |
| regex_dna                | 136 ms                                                      | 117 ms: 1.17x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.05 sec: 1.16x faster                                                     |
| pprint_safe_repr         | 592 ms                                                      | 511 ms: 1.16x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.67 sec: 1.15x faster                                                     |
| coroutines               | 16.0 ms                                                     | 13.9 ms: 1.15x faster                                                      |
| sympy_str                | 194 ms                                                      | 170 ms: 1.15x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 13.7 ms: 1.13x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 59.1 ms: 1.13x faster                                                      |
| 2to3                     | 246 ms                                                      | 219 ms: 1.12x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 855 us: 1.12x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 88.7 ms: 1.09x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 51.2 ms: 1.08x faster                                                      |
| fannkuch                 | 256 ms                                                      | 236 ms: 1.08x faster                                                       |
| unpickle                 | 9.09 us                                                     | 8.47 us: 1.07x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                                      |
| sympy_expand             | 314 ms                                                      | 294 ms: 1.07x faster                                                       |
| json                     | 3.14 ms                                                     | 2.99 ms: 1.05x faster                                                      |
| unpack_sequence          | 39.6 ns                                                     | 37.8 ns: 1.05x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.6 ms: 1.02x faster                                                      |
| pidigits                 | 149 ms                                                      | 147 ms: 1.01x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.70 us: 1.01x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 76.3 ms: 1.00x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.9 us: 1.06x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.29 ms: 1.09x slower                                                      |
| pickle                   | 6.85 us                                                     | 7.52 us: 1.10x slower                                                      |
| async_generators         | 222 ms                                                      | 249 ms: 1.12x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 19.5 us: 1.13x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 18.5 ms: 1.19x slower                                                      |
| python_startup           | 20.6 ms                                                     | 24.6 ms: 1.19x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.31 us: 1.20x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 91.4 ms: 1.47x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.15 ms: 1.52x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.30 ms: 1.62x slower                                                      |
| logging_silent           | 94.6 ns                                                     | 307 ns: 3.24x slower                                                       |
| coverage                 | 39.0 ms                                                     | 288 ms: 7.39x slower                                                       |
| thrift                   | 617 us                                                      | 93.4 ms: 151.27x slower                                                    |
| Geometric mean           | (ref)                                                       | 1.16x faster                                                               |

Benchmark hidden because not significant (2): logging_simple, unpickle_list
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250524-3.15.0a0-2fd09b0-JIT/bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.196x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: unknown