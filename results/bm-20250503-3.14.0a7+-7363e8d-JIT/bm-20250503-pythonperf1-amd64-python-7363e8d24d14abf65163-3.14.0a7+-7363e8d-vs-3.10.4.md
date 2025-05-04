# Results vs. 3.10.4

- fork: python
- ref: 7363e8d24d14abf65163
- machine: windows-amd64
- commit hash: 7363e8d
- commit date: 2025-05-03
- overall geometric mean: 1.273x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 223 ms: 1.10x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.72 sec: 1.12x faster                                                      |
| html5lib       | 51.0 ms                                                     | 39.4 ms: 1.30x faster                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 415 ms: 2.67x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 207 ms: 2.54x faster                                                        |
| async_tree_none         | 435 ms                                                      | 181 ms: 2.41x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 335 ms: 1.90x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.36x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 45.3 ms: 1.36x faster                                                       |
| nbody          | 71.3 ms                                                     | 56.9 ms: 1.25x faster                                                       |
| Geometric mean | (ref)                                                       | 1.20x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 81.5 ms: 1.30x faster                                                       |
| regex_dna      | 136 ms                                                      | 123 ms: 1.10x faster                                                        |
| regex_v8       | 15.4 ms                                                     | 14.4 ms: 1.08x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                       | 1.13x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 119 us: 1.53x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.22 sec: 1.37x faster                                                      |
| json_dumps           | 9.16 ms                                                     | 6.74 ms: 1.36x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 215 us: 1.26x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 36.5 ms: 1.22x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 90.0 ms: 1.08x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 51.7 ms: 1.07x faster                                                       |
| unpickle             | 9.09 us                                                     | 8.61 us: 1.06x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 64.1 ms: 1.01x faster                                                       |
| unpickle_list        | 2.71 us                                                     | 2.86 us: 1.06x slower                                                       |
| json_loads           | 14.0 us                                                     | 14.9 us: 1.06x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 19.7 us: 1.15x slower                                                       |
| pickle               | 6.85 us                                                     | 7.97 us: 1.16x slower                                                       |
| pickle_list          | 2.75 us                                                     | 3.38 us: 1.23x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.08x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.2 ms: 1.24x slower                                                       |
| python_startup         | 20.6 ms                                                     | 25.7 ms: 1.25x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.24x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.60 ms: 1.61x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 16.0 ms: 1.24x faster                                                       |
| django_template | 28.9 ms                                                     | 24.7 ms: 1.17x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 35.4 ms: 1.16x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.28x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 114 us: 2.95x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 415 ms: 2.67x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 207 ms: 2.54x faster                                                        |
| async_tree_none          | 435 ms                                                      | 181 ms: 2.41x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 32.1 ms: 2.35x faster                                                       |
| mdp                      | 1.78 sec                                                    | 817 ms: 2.18x faster                                                        |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 335 ms: 1.90x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.21 ms: 1.89x faster                                                       |
| go                       | 139 ms                                                      | 80.7 ms: 1.72x faster                                                       |
| pylint                   | 350 ms                                                      | 204 ms: 1.71x faster                                                        |
| logging_silent           | 94.6 ns                                                     | 57.7 ns: 1.64x faster                                                       |
| generators               | 32.4 ms                                                     | 19.9 ms: 1.63x faster                                                       |
| richards_super           | 52.2 ms                                                     | 32.2 ms: 1.62x faster                                                       |
| mako                     | 9.03 ms                                                     | 5.60 ms: 1.61x faster                                                       |
| pyflate                  | 409 ms                                                      | 263 ms: 1.56x faster                                                        |
| chaos                    | 61.7 ms                                                     | 39.8 ms: 1.55x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 119 us: 1.53x faster                                                        |
| raytrace                 | 273 ms                                                      | 179 ms: 1.52x faster                                                        |
| richards                 | 42.4 ms                                                     | 28.4 ms: 1.49x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.47 sec: 1.43x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 59.9 ms: 1.43x faster                                                       |
| deepcopy                 | 255 us                                                      | 181 us: 1.41x faster                                                        |
| comprehensions           | 16.5 us                                                     | 11.9 us: 1.39x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.22 sec: 1.37x faster                                                      |
| float                    | 61.7 ms                                                     | 45.3 ms: 1.36x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.74 ms: 1.36x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 540 ms: 1.35x faster                                                        |
| scimark_sor              | 106 ms                                                      | 79.0 ms: 1.34x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 42.7 ms: 1.34x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 46.6 ms: 1.34x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 21.6 us: 1.33x faster                                                       |
| regex_compile            | 106 ms                                                      | 81.5 ms: 1.30x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 39.4 ms: 1.30x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.44 ms: 1.29x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 957 ms: 1.27x faster                                                        |
| pycparser                | 930 ms                                                      | 739 ms: 1.26x faster                                                        |
| pickle_pure_python       | 270 us                                                      | 215 us: 1.26x faster                                                        |
| nbody                    | 71.3 ms                                                     | 56.9 ms: 1.25x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 16.0 ms: 1.24x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.56 us: 1.23x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 486 ms: 1.22x faster                                                        |
| xml_etree_process        | 44.5 ms                                                     | 36.5 ms: 1.22x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 63.6 ms: 1.21x faster                                                       |
| sympy_sum                | 107 ms                                                      | 89.2 ms: 1.20x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 12.9 ms: 1.19x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.30 ms: 1.18x faster                                                       |
| django_template          | 28.9 ms                                                     | 24.7 ms: 1.17x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 43.2 ms: 1.17x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 35.4 ms: 1.16x faster                                                       |
| scimark_fft              | 187 ms                                                      | 162 ms: 1.15x faster                                                        |
| deepcopy_reduce          | 2.20 us                                                     | 1.92 us: 1.15x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.72 sec: 1.12x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.3 ms: 1.12x faster                                                       |
| sympy_str                | 194 ms                                                      | 175 ms: 1.11x faster                                                        |
| regex_dna                | 136 ms                                                      | 123 ms: 1.10x faster                                                        |
| 2to3                     | 246 ms                                                      | 223 ms: 1.10x faster                                                        |
| bench_thread_pool        | 958 us                                                      | 878 us: 1.09x faster                                                        |
| nqueens                  | 66.6 ms                                                     | 61.6 ms: 1.08x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 90.0 ms: 1.08x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 14.4 ms: 1.08x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 51.7 ms: 1.07x faster                                                       |
| unpickle                 | 9.09 us                                                     | 8.61 us: 1.06x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                       |
| sympy_expand             | 314 ms                                                      | 304 ms: 1.04x faster                                                        |
| fannkuch                 | 256 ms                                                      | 249 ms: 1.03x faster                                                        |
| xml_etree_iterparse      | 65.0 ms                                                     | 64.1 ms: 1.01x faster                                                       |
| json                     | 3.14 ms                                                     | 3.10 ms: 1.01x faster                                                       |
| logging_simple           | 6.22 us                                                     | 6.29 us: 1.01x slower                                                       |
| meteor_contest           | 75.9 ms                                                     | 77.3 ms: 1.02x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 2.86 us: 1.06x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.9 us: 1.06x slower                                                       |
| async_generators         | 222 ms                                                      | 247 ms: 1.12x slower                                                        |
| telco                    | 3.94 ms                                                     | 4.42 ms: 1.12x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 19.7 us: 1.15x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.97 us: 1.16x slower                                                       |
| pickle_list              | 2.75 us                                                     | 3.38 us: 1.23x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 19.2 ms: 1.24x slower                                                       |
| python_startup           | 20.6 ms                                                     | 25.7 ms: 1.25x slower                                                       |
| coverage                 | 39.0 ms                                                     | 51.4 ms: 1.32x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 89.7 ms: 1.45x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.08 ms: 1.48x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.26 ms: 1.57x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.24x faster                                                                |

Benchmark hidden because not significant (3): pidigits, logging_format, unpack_sequence
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (16) of results/bm-20250503-3.14.0a7+-7363e8d-JIT/bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.273x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: unknown