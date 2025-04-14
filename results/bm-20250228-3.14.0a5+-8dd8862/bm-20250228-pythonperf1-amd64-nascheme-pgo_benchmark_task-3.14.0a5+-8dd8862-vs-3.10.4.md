# Results vs. 3.10.4

- fork: nascheme
- ref: pgo_benchmark_task
- machine: windows-amd64
- commit hash: 8dd8862
- commit date: 2025-02-28
- overall geometric mean: 1.229x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf1-amd64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 224 ms: 1.10x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.65 sec: 1.16x faster                                                      |
| html5lib       | 51.0 ms                                                     | 40.5 ms: 1.26x faster                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf1-amd64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 414 ms: 2.68x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 217 ms: 2.43x faster                                                        |
| async_tree_none         | 435 ms                                                      | 186 ms: 2.34x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 340 ms: 1.88x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.31x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf1-amd64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 46.1 ms: 1.34x faster                                                       |
| pidigits       | 149 ms                                                      | 151 ms: 1.01x slower                                                        |
| nbody          | 71.3 ms                                                     | 72.8 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf1-amd64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 86.4 ms: 1.23x faster                                                       |
| regex_dna      | 136 ms                                                      | 117 ms: 1.16x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.48 ms: 1.12x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.9 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf1-amd64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.83 ms: 1.34x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 148 us: 1.24x faster                                                        |
| pickle_pure_python   | 270 us                                                      | 226 us: 1.19x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.41 sec: 1.18x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 40.4 ms: 1.10x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 90.9 ms: 1.06x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.7 ms: 1.04x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 56.9 ms: 1.02x slower                                                       |
| json_loads           | 14.0 us                                                     | 14.8 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.11x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf1-amd64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.7 ms: 1.25x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 19.6 ms: 1.26x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf1-amd64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.77 ms: 1.33x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 16.4 ms: 1.21x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 35.8 ms: 1.15x faster                                                       |
| django_template | 28.9 ms                                                     | 25.4 ms: 1.14x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.20x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf1-amd64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 109 us: 3.08x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 414 ms: 2.68x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 217 ms: 2.43x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 32.0 ms: 2.36x faster                                                       |
| async_tree_none          | 435 ms                                                      | 186 ms: 2.34x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.19 ms: 1.91x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 340 ms: 1.88x faster                                                        |
| pylint                   | 350 ms                                                      | 198 ms: 1.77x faster                                                        |
| generators               | 32.4 ms                                                     | 19.6 ms: 1.65x faster                                                       |
| go                       | 139 ms                                                      | 86.6 ms: 1.60x faster                                                       |
| richards_super           | 52.2 ms                                                     | 33.5 ms: 1.56x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 61.7 ns: 1.53x faster                                                       |
| chaos                    | 61.7 ms                                                     | 42.2 ms: 1.46x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.4 us: 1.45x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 19.9 us: 1.44x faster                                                       |
| richards                 | 42.4 ms                                                     | 29.5 ms: 1.44x faster                                                       |
| raytrace                 | 273 ms                                                      | 192 ms: 1.42x faster                                                        |
| deepcopy                 | 255 us                                                      | 184 us: 1.39x faster                                                        |
| sqlglot_parse            | 1.22 ms                                                     | 882 us: 1.38x faster                                                        |
| scimark_lu               | 85.8 ms                                                     | 62.9 ms: 1.36x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.09 ms: 1.35x faster                                                       |
| pyflate                  | 409 ms                                                      | 304 ms: 1.34x faster                                                        |
| json_dumps               | 9.16 ms                                                     | 6.83 ms: 1.34x faster                                                       |
| float                    | 61.7 ms                                                     | 46.1 ms: 1.34x faster                                                       |
| mako                     | 9.03 ms                                                     | 6.77 ms: 1.33x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.35 ms: 1.32x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 58.5 ms: 1.32x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 44.5 ms: 1.29x faster                                                       |
| pycparser                | 930 ms                                                      | 735 ms: 1.26x faster                                                        |
| scimark_sor              | 106 ms                                                      | 84.2 ms: 1.26x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 40.5 ms: 1.26x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 50.1 ms: 1.25x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 148 us: 1.24x faster                                                        |
| regex_compile            | 106 ms                                                      | 86.4 ms: 1.23x faster                                                       |
| thrift                   | 617 us                                                      | 506 us: 1.22x faster                                                        |
| sqlite_synth             | 1.91 us                                                     | 1.58 us: 1.21x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 16.4 ms: 1.21x faster                                                       |
| sympy_sum                | 107 ms                                                      | 89.4 ms: 1.20x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 226 us: 1.19x faster                                                        |
| dulwich_log              | 50.5 ms                                                     | 42.5 ms: 1.19x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.41 sec: 1.18x faster                                                      |
| coroutines               | 16.0 ms                                                     | 13.6 ms: 1.18x faster                                                       |
| regex_dna                | 136 ms                                                      | 117 ms: 1.16x faster                                                        |
| docutils                 | 1.92 sec                                                    | 1.65 sec: 1.16x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.91 us: 1.15x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 35.8 ms: 1.15x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.3 ms: 1.14x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 34.9 ms: 1.14x faster                                                       |
| django_template          | 28.9 ms                                                     | 25.4 ms: 1.14x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.48 ms: 1.12x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 855 us: 1.12x faster                                                        |
| sympy_str                | 194 ms                                                      | 174 ms: 1.12x faster                                                        |
| pprint_pformat           | 1.22 sec                                                    | 1.09 sec: 1.12x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.61 sec: 1.10x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 40.4 ms: 1.10x faster                                                       |
| 2to3                     | 246 ms                                                      | 224 ms: 1.10x faster                                                        |
| pprint_safe_repr         | 592 ms                                                      | 542 ms: 1.09x faster                                                        |
| sqlglot_normalize        | 205 ms                                                      | 192 ms: 1.07x faster                                                        |
| xml_etree_parse          | 96.8 ms                                                     | 90.9 ms: 1.06x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 62.8 ms: 1.06x faster                                                       |
| sympy_expand             | 314 ms                                                      | 297 ms: 1.06x faster                                                        |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.58 ms: 1.05x faster                                                       |
| json                     | 3.14 ms                                                     | 3.01 ms: 1.04x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.7 ms: 1.04x faster                                                       |
| scimark_fft              | 187 ms                                                      | 181 ms: 1.04x faster                                                        |
| regex_v8                 | 15.4 ms                                                     | 14.9 ms: 1.04x faster                                                       |
| async_generators         | 222 ms                                                      | 218 ms: 1.02x faster                                                        |
| meteor_contest           | 75.9 ms                                                     | 75.0 ms: 1.01x faster                                                       |
| pidigits                 | 149 ms                                                      | 151 ms: 1.01x slower                                                        |
| logging_format           | 6.76 us                                                     | 6.86 us: 1.02x slower                                                       |
| nbody                    | 71.3 ms                                                     | 72.8 ms: 1.02x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 56.9 ms: 1.02x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.40 us: 1.03x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.8 us: 1.06x slower                                                       |
| fannkuch                 | 256 ms                                                      | 274 ms: 1.07x slower                                                        |
| telco                    | 3.94 ms                                                     | 4.81 ms: 1.22x slower                                                       |
| coverage                 | 39.0 ms                                                     | 47.8 ms: 1.23x slower                                                       |
| python_startup           | 20.6 ms                                                     | 25.7 ms: 1.25x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 19.6 ms: 1.26x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 86.2 ms: 1.39x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.00 ms: 1.42x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.20 ms: 1.50x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.22x faster                                                                |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250228-3.14.0a5+-8dd8862/bm-20250228-pythonperf1-amd64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.229x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: unknown