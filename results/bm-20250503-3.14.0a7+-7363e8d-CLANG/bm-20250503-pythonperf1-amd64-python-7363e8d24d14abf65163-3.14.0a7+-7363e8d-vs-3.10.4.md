# Results vs. 3.10.4

- fork: python
- ref: 7363e8d24d14abf65163
- machine: windows-amd64
- commit hash: 7363e8d
- commit date: 2025-05-03
- overall geometric mean: 1.480x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.33x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 205 ms: 1.20x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.59 sec: 1.21x faster                                                      |
| html5lib       | 51.0 ms                                                     | 34.4 ms: 1.48x faster                                                       |
| Geometric mean | (ref)                                                       | 1.29x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 347 ms: 3.20x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 184 ms: 2.86x faster                                                        |
| async_tree_none         | 435 ms                                                      | 157 ms: 2.78x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 317 ms: 2.01x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.67x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 37.9 ms: 1.63x faster                                                       |
| nbody          | 71.3 ms                                                     | 52.2 ms: 1.37x faster                                                       |
| pidigits       | 149 ms                                                      | 146 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                       | 1.31x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 68.6 ms: 1.55x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 13.8 ms: 1.12x faster                                                       |
| regex_dna      | 136 ms                                                      | 127 ms: 1.07x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.76 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 104 us: 1.76x faster                                                        |
| pickle_pure_python   | 270 us                                                      | 169 us: 1.60x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.06 sec: 1.58x faster                                                      |
| json_dumps           | 9.16 ms                                                     | 5.79 ms: 1.58x faster                                                       |
| pickle_dict          | 17.2 us                                                     | 12.2 us: 1.41x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 33.5 ms: 1.33x faster                                                       |
| pickle_list          | 2.75 us                                                     | 2.16 us: 1.28x faster                                                       |
| unpickle_list        | 2.71 us                                                     | 2.30 us: 1.18x faster                                                       |
| unpickle             | 9.09 us                                                     | 7.73 us: 1.18x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 48.3 ms: 1.15x faster                                                       |
| pickle               | 6.85 us                                                     | 6.22 us: 1.10x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 93.8 ms: 1.03x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.2 ms: 1.03x faster                                                       |
| json_loads           | 14.0 us                                                     | 14.4 us: 1.03x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.28x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 20.2 ms: 1.30x slower                                                       |
| python_startup         | 20.6 ms                                                     | 27.0 ms: 1.31x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.31x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 19.8 ms                                                     | 11.3 ms: 1.75x faster                                                       |
| mako            | 9.03 ms                                                     | 5.93 ms: 1.52x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 28.0 ms: 1.47x faster                                                       |
| django_template | 28.9 ms                                                     | 20.0 ms: 1.44x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.54x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 90.7 us: 3.70x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 347 ms: 3.20x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 184 ms: 2.86x faster                                                        |
| async_tree_none          | 435 ms                                                      | 157 ms: 2.78x faster                                                        |
| deltablue                | 4.19 ms                                                     | 1.55 ms: 2.70x faster                                                       |
| mdp                      | 1.78 sec                                                    | 682 ms: 2.61x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 30.7 ms: 2.46x faster                                                       |
| go                       | 139 ms                                                      | 59.7 ms: 2.33x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 43.1 ns: 2.19x faster                                                       |
| generators               | 32.4 ms                                                     | 14.8 ms: 2.19x faster                                                       |
| scimark_sor              | 106 ms                                                      | 49.0 ms: 2.16x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 13.4 us: 2.15x faster                                                       |
| richards_super           | 52.2 ms                                                     | 24.8 ms: 2.11x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 28.0 ms: 2.04x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 317 ms: 2.01x faster                                                        |
| richards                 | 42.4 ms                                                     | 21.4 ms: 1.99x faster                                                       |
| chaos                    | 61.7 ms                                                     | 31.4 ms: 1.97x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 2.94 ms: 1.96x faster                                                       |
| comprehensions           | 16.5 us                                                     | 8.59 us: 1.92x faster                                                       |
| raytrace                 | 273 ms                                                      | 144 ms: 1.89x faster                                                        |
| scimark_lu               | 85.8 ms                                                     | 46.0 ms: 1.87x faster                                                       |
| pylint                   | 350 ms                                                      | 190 ms: 1.85x faster                                                        |
| deepcopy                 | 255 us                                                      | 141 us: 1.81x faster                                                        |
| pyflate                  | 409 ms                                                      | 232 ms: 1.77x faster                                                        |
| unpickle_pure_python     | 183 us                                                      | 104 us: 1.76x faster                                                        |
| genshi_text              | 19.8 ms                                                     | 11.3 ms: 1.75x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 429 ms: 1.71x faster                                                        |
| float                    | 61.7 ms                                                     | 37.9 ms: 1.63x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 48.1 ms: 1.61x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 169 us: 1.60x faster                                                        |
| crypto_pyaes             | 62.5 ms                                                     | 39.1 ms: 1.60x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.33 sec: 1.59x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.06 sec: 1.58x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.79 ms: 1.58x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 786 ms: 1.55x faster                                                        |
| pprint_safe_repr         | 592 ms                                                      | 383 ms: 1.55x faster                                                        |
| regex_compile            | 106 ms                                                      | 68.6 ms: 1.55x faster                                                       |
| mako                     | 9.03 ms                                                     | 5.93 ms: 1.52x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 34.4 ms: 1.48x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.49 us: 1.48x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 28.0 ms: 1.47x faster                                                       |
| coroutines               | 16.0 ms                                                     | 11.1 ms: 1.44x faster                                                       |
| django_template          | 28.9 ms                                                     | 20.0 ms: 1.44x faster                                                       |
| pycparser                | 930 ms                                                      | 649 ms: 1.43x faster                                                        |
| pickle_dict              | 17.2 us                                                     | 12.2 us: 1.41x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 47.5 ms: 1.40x faster                                                       |
| sympy_sum                | 107 ms                                                      | 78.2 ms: 1.37x faster                                                       |
| nbody                    | 71.3 ms                                                     | 52.2 ms: 1.37x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 11.2 ms: 1.36x faster                                                       |
| unpack_sequence          | 39.6 ns                                                     | 29.6 ns: 1.34x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 33.5 ms: 1.33x faster                                                       |
| fannkuch                 | 256 ms                                                      | 197 ms: 1.30x faster                                                        |
| dulwich_log              | 50.5 ms                                                     | 38.9 ms: 1.30x faster                                                       |
| sympy_str                | 194 ms                                                      | 150 ms: 1.30x faster                                                        |
| scimark_fft              | 187 ms                                                      | 146 ms: 1.28x faster                                                        |
| pickle_list              | 2.75 us                                                     | 2.16 us: 1.28x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.51 us: 1.27x faster                                                       |
| sympy_expand             | 314 ms                                                      | 256 ms: 1.23x faster                                                        |
| docutils                 | 1.92 sec                                                    | 1.59 sec: 1.21x faster                                                      |
| 2to3                     | 246 ms                                                      | 205 ms: 1.20x faster                                                        |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.30 ms: 1.18x faster                                                       |
| unpickle_list            | 2.71 us                                                     | 2.30 us: 1.18x faster                                                       |
| unpickle                 | 9.09 us                                                     | 7.73 us: 1.18x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 48.3 ms: 1.15x faster                                                       |
| async_generators         | 222 ms                                                      | 195 ms: 1.14x faster                                                        |
| bench_thread_pool        | 958 us                                                      | 845 us: 1.13x faster                                                        |
| meteor_contest           | 75.9 ms                                                     | 67.2 ms: 1.13x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.00 us: 1.13x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 13.8 ms: 1.12x faster                                                       |
| logging_simple           | 6.22 us                                                     | 5.60 us: 1.11x faster                                                       |
| pickle                   | 6.85 us                                                     | 6.22 us: 1.10x faster                                                       |
| json                     | 3.14 ms                                                     | 2.92 ms: 1.07x faster                                                       |
| regex_dna                | 136 ms                                                      | 127 ms: 1.07x faster                                                        |
| xml_etree_parse          | 96.8 ms                                                     | 93.8 ms: 1.03x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.2 ms: 1.03x faster                                                       |
| pidigits                 | 149 ms                                                      | 146 ms: 1.02x faster                                                        |
| json_loads               | 14.0 us                                                     | 14.4 us: 1.03x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.08 ms: 1.04x slower                                                       |
| coverage                 | 39.0 ms                                                     | 41.1 ms: 1.05x slower                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.76 ms: 1.06x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 20.2 ms: 1.30x slower                                                       |
| python_startup           | 20.6 ms                                                     | 27.0 ms: 1.31x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 90.3 ms: 1.46x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.38 ms: 1.72x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.87 ms: 2.04x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.45x faster                                                                |
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (16) of results/bm-20250503-3.14.0a7+-7363e8d-CLANG/bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.480x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.40x
- 95% likely to have a speedup of 1.38x
- 99% likely to have a speedup of 1.33x

# Memory
- memory change: unknown