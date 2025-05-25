# Results vs. 3.10.4

- fork: python
- ref: 2fd09b011031f3c00c34
- machine: windows-amd64
- commit hash: 2fd09b0
- commit date: 2025-05-24
- overall geometric mean: 1.171x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 219 ms: 1.12x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.63 sec: 1.18x faster                                                     |
| html5lib       | 51.0 ms                                                     | 38.3 ms: 1.33x faster                                                      |
| Geometric mean | (ref)                                                       | 1.21x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 397 ms: 2.79x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 204 ms: 2.58x faster                                                       |
| async_tree_none         | 435 ms                                                      | 171 ms: 2.55x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 328 ms: 1.95x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.44x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 44.6 ms: 1.38x faster                                                      |
| nbody          | 71.3 ms                                                     | 62.7 ms: 1.14x faster                                                      |
| pidigits       | 149 ms                                                      | 147 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 79.5 ms: 1.33x faster                                                      |
| regex_dna      | 136 ms                                                      | 120 ms: 1.13x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.48 ms: 1.12x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 14.4 ms: 1.07x faster                                                      |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.32 ms: 1.45x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 134 us: 1.37x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 211 us: 1.28x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.38 sec: 1.21x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 37.9 ms: 1.17x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 88.4 ms: 1.09x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.53 us: 1.07x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 54.1 ms: 1.03x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.5 ms: 1.02x faster                                                      |
| unpickle_list        | 2.71 us                                                     | 2.81 us: 1.04x slower                                                      |
| json_loads           | 14.0 us                                                     | 14.8 us: 1.06x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 19.6 us: 1.14x slower                                                      |
| pickle               | 6.85 us                                                     | 8.02 us: 1.17x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.40 us: 1.23x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.07x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 24.4 ms: 1.18x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 18.4 ms: 1.19x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.19x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.46 ms: 1.40x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.7 ms: 1.26x faster                                                      |
| django_template | 28.9 ms                                                     | 24.4 ms: 1.19x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 34.8 ms: 1.18x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.25x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 106 us: 3.18x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 397 ms: 2.79x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 204 ms: 2.58x faster                                                       |
| async_tree_none          | 435 ms                                                      | 171 ms: 2.55x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 29.8 ms: 2.54x faster                                                      |
| mdp                      | 1.78 sec                                                    | 811 ms: 2.19x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 328 ms: 1.95x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.16 ms: 1.93x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 404 ms: 1.81x faster                                                       |
| pylint                   | 350 ms                                                      | 196 ms: 1.78x faster                                                       |
| go                       | 139 ms                                                      | 80.2 ms: 1.73x faster                                                      |
| richards_super           | 52.2 ms                                                     | 31.0 ms: 1.68x faster                                                      |
| generators               | 32.4 ms                                                     | 19.4 ms: 1.67x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.29 sec: 1.63x faster                                                     |
| deepcopy_memo            | 28.8 us                                                     | 17.9 us: 1.60x faster                                                      |
| richards                 | 42.4 ms                                                     | 27.3 ms: 1.55x faster                                                      |
| chaos                    | 61.7 ms                                                     | 39.9 ms: 1.55x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 56.7 ms: 1.51x faster                                                      |
| deepcopy                 | 255 us                                                      | 173 us: 1.47x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.32 ms: 1.45x faster                                                      |
| pyflate                  | 409 ms                                                      | 283 ms: 1.44x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.4 us: 1.44x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.2 ms: 1.43x faster                                                      |
| scimark_sor              | 106 ms                                                      | 75.4 ms: 1.41x faster                                                      |
| raytrace                 | 273 ms                                                      | 195 ms: 1.41x faster                                                       |
| mako                     | 9.03 ms                                                     | 6.46 ms: 1.40x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.11 ms: 1.40x faster                                                      |
| float                    | 61.7 ms                                                     | 44.6 ms: 1.38x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 134 us: 1.37x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 57.3 ms: 1.35x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 46.7 ms: 1.34x faster                                                      |
| regex_compile            | 106 ms                                                      | 79.5 ms: 1.33x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 38.3 ms: 1.33x faster                                                      |
| pycparser                | 930 ms                                                      | 705 ms: 1.32x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 211 us: 1.28x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 15.7 ms: 1.26x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 40.3 ms: 1.25x faster                                                      |
| sympy_sum                | 107 ms                                                      | 87.0 ms: 1.23x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 12.4 ms: 1.23x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.82 us: 1.21x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.58 us: 1.21x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.38 sec: 1.21x faster                                                     |
| django_template          | 28.9 ms                                                     | 24.4 ms: 1.19x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 34.8 ms: 1.18x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.63 sec: 1.18x faster                                                     |
| xml_etree_process        | 44.5 ms                                                     | 37.9 ms: 1.17x faster                                                      |
| coroutines               | 16.0 ms                                                     | 13.8 ms: 1.16x faster                                                      |
| sympy_str                | 194 ms                                                      | 169 ms: 1.15x faster                                                       |
| nbody                    | 71.3 ms                                                     | 62.7 ms: 1.14x faster                                                      |
| regex_dna                | 136 ms                                                      | 120 ms: 1.13x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 852 us: 1.12x faster                                                       |
| 2to3                     | 246 ms                                                      | 219 ms: 1.12x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.48 ms: 1.12x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.44 ms: 1.12x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.10 sec: 1.11x faster                                                     |
| nqueens                  | 66.6 ms                                                     | 60.3 ms: 1.10x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 88.4 ms: 1.09x faster                                                      |
| scimark_fft              | 187 ms                                                      | 171 ms: 1.09x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 543 ms: 1.09x faster                                                       |
| sympy_expand             | 314 ms                                                      | 290 ms: 1.08x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 14.4 ms: 1.07x faster                                                      |
| unpickle                 | 9.09 us                                                     | 8.53 us: 1.07x faster                                                      |
| json                     | 3.14 ms                                                     | 2.96 ms: 1.06x faster                                                      |
| unpack_sequence          | 39.6 ns                                                     | 37.8 ns: 1.05x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 72.9 ms: 1.04x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 54.1 ms: 1.03x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.5 ms: 1.02x faster                                                      |
| fannkuch                 | 256 ms                                                      | 251 ms: 1.02x faster                                                       |
| pidigits                 | 149 ms                                                      | 147 ms: 1.02x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.93 us: 1.03x slower                                                      |
| logging_simple           | 6.22 us                                                     | 6.38 us: 1.03x slower                                                      |
| async_generators         | 222 ms                                                      | 228 ms: 1.03x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 2.81 us: 1.04x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.8 us: 1.06x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 19.6 us: 1.14x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.56 ms: 1.16x slower                                                      |
| pickle                   | 6.85 us                                                     | 8.02 us: 1.17x slower                                                      |
| python_startup           | 20.6 ms                                                     | 24.4 ms: 1.18x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 18.4 ms: 1.19x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.40 us: 1.23x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 91.2 ms: 1.47x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.09 ms: 1.49x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.28 ms: 1.61x slower                                                      |
| logging_silent           | 94.6 ns                                                     | 317 ns: 3.35x slower                                                       |
| coverage                 | 39.0 ms                                                     | 296 ms: 7.59x slower                                                       |
| thrift                   | 617 us                                                      | 92.7 ms: 150.12x slower                                                    |
| Geometric mean           | (ref)                                                       | 1.14x faster                                                               |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250524-3.15.0a0-2fd09b0/bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.171x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: unknown