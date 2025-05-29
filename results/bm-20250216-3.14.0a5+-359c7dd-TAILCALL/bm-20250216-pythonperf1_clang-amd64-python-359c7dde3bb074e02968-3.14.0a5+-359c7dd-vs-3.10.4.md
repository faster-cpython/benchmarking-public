# Results vs. 3.10.4

- fork: python
- ref: 359c7dde3bb074e02968
- machine: windows-amd64
- commit hash: 359c7dd
- commit date: 2025-02-16
- overall geometric mean: 1.235x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 224 ms: 1.10x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.71 sec: 1.12x faster                                                      |
| html5lib       | 51.0 ms                                                     | 38.7 ms: 1.32x faster                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 392 ms: 2.82x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 210 ms: 2.51x faster                                                        |
| async_tree_none         | 435 ms                                                      | 177 ms: 2.46x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 359 ms: 1.77x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.36x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 44.1 ms: 1.40x faster                                                       |
| nbody          | 71.3 ms                                                     | 68.3 ms: 1.04x faster                                                       |
| pidigits       | 149 ms                                                      | 154 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 84.4 ms: 1.26x faster                                                       |
| regex_dna      | 136 ms                                                      | 130 ms: 1.05x faster                                                        |
| regex_v8       | 15.4 ms                                                     | 16.5 ms: 1.07x slower                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.93 ms: 1.16x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 141 us: 1.30x faster                                                        |
| pickle_pure_python   | 270 us                                                      | 209 us: 1.29x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.31 sec: 1.28x faster                                                      |
| json_dumps           | 9.16 ms                                                     | 7.81 ms: 1.17x faster                                                       |
| unpickle_list        | 2.71 us                                                     | 2.48 us: 1.10x faster                                                       |
| pickle_dict          | 17.2 us                                                     | 16.5 us: 1.04x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 43.7 ms: 1.02x faster                                                       |
| pickle_list          | 2.75 us                                                     | 2.80 us: 1.02x slower                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 68.1 ms: 1.05x slower                                                       |
| unpickle             | 9.09 us                                                     | 9.53 us: 1.05x slower                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 102 ms: 1.05x slower                                                        |
| xml_etree_generate   | 55.5 ms                                                     | 63.6 ms: 1.15x slower                                                       |
| pickle               | 6.85 us                                                     | 7.85 us: 1.15x slower                                                       |
| json_loads           | 14.0 us                                                     | 19.3 us: 1.38x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.7 ms: 1.25x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 19.8 ms: 1.28x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 19.8 ms                                                     | 14.6 ms: 1.35x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 31.4 ms: 1.31x faster                                                       |
| django_template | 28.9 ms                                                     | 24.2 ms: 1.20x faster                                                       |
| mako            | 9.03 ms                                                     | 7.57 ms: 1.19x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.26x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 110 us: 3.07x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 392 ms: 2.82x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 29.2 ms: 2.59x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 210 ms: 2.51x faster                                                        |
| async_tree_none          | 435 ms                                                      | 177 ms: 2.46x faster                                                        |
| deltablue                | 4.19 ms                                                     | 1.82 ms: 2.30x faster                                                       |
| go                       | 139 ms                                                      | 70.8 ms: 1.96x faster                                                       |
| generators               | 32.4 ms                                                     | 17.4 ms: 1.86x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 396 ms: 1.85x faster                                                        |
| unpack_sequence          | 39.6 ns                                                     | 21.7 ns: 1.82x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 359 ms: 1.77x faster                                                        |
| pylint                   | 350 ms                                                      | 201 ms: 1.75x faster                                                        |
| richards_super           | 52.2 ms                                                     | 31.4 ms: 1.66x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 57.3 ns: 1.65x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.30 sec: 1.63x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 17.8 us: 1.62x faster                                                       |
| raytrace                 | 273 ms                                                      | 172 ms: 1.59x faster                                                        |
| chaos                    | 61.7 ms                                                     | 39.2 ms: 1.57x faster                                                       |
| richards                 | 42.4 ms                                                     | 27.5 ms: 1.54x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 806 us: 1.51x faster                                                        |
| scimark_sor              | 106 ms                                                      | 71.6 ms: 1.48x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 3.90 ms: 1.47x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 38.9 ms: 1.47x faster                                                       |
| deepcopy                 | 255 us                                                      | 175 us: 1.46x faster                                                        |
| sqlglot_transpile        | 1.48 ms                                                     | 1.01 ms: 1.46x faster                                                       |
| pyflate                  | 409 ms                                                      | 281 ms: 1.46x faster                                                        |
| comprehensions           | 16.5 us                                                     | 11.4 us: 1.45x faster                                                       |
| float                    | 61.7 ms                                                     | 44.1 ms: 1.40x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 55.8 ms: 1.38x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 62.6 ms: 1.37x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 14.6 ms: 1.35x faster                                                       |
| pycparser                | 930 ms                                                      | 699 ms: 1.33x faster                                                        |
| html5lib                 | 51.0 ms                                                     | 38.7 ms: 1.32x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 31.4 ms: 1.31x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 141 us: 1.30x faster                                                        |
| pickle_pure_python       | 270 us                                                      | 209 us: 1.29x faster                                                        |
| tomli_loads              | 1.67 sec                                                    | 1.31 sec: 1.28x faster                                                      |
| regex_compile            | 106 ms                                                      | 84.4 ms: 1.26x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 51.5 ms: 1.21x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 41.7 ms: 1.21x faster                                                       |
| django_template          | 28.9 ms                                                     | 24.2 ms: 1.20x faster                                                       |
| mako                     | 9.03 ms                                                     | 7.57 ms: 1.19x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.63 us: 1.18x faster                                                       |
| sympy_sum                | 107 ms                                                      | 91.1 ms: 1.17x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 7.81 ms: 1.17x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.8 ms: 1.16x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.90 us: 1.16x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 512 ms: 1.16x faster                                                        |
| pprint_pformat           | 1.22 sec                                                    | 1.06 sec: 1.15x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.3 ms: 1.15x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 35.3 ms: 1.13x faster                                                       |
| thrift                   | 617 us                                                      | 550 us: 1.12x faster                                                        |
| docutils                 | 1.92 sec                                                    | 1.71 sec: 1.12x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.61 sec: 1.10x faster                                                      |
| sympy_str                | 194 ms                                                      | 176 ms: 1.10x faster                                                        |
| bench_thread_pool        | 958 us                                                      | 873 us: 1.10x faster                                                        |
| 2to3                     | 246 ms                                                      | 224 ms: 1.10x faster                                                        |
| unpickle_list            | 2.71 us                                                     | 2.48 us: 1.10x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 188 ms: 1.09x faster                                                        |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.52 ms: 1.08x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 62.4 ms: 1.07x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 71.2 ms: 1.07x faster                                                       |
| regex_dna                | 136 ms                                                      | 130 ms: 1.05x faster                                                        |
| sympy_expand             | 314 ms                                                      | 300 ms: 1.05x faster                                                        |
| nbody                    | 71.3 ms                                                     | 68.3 ms: 1.04x faster                                                       |
| pickle_dict              | 17.2 us                                                     | 16.5 us: 1.04x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.58 us: 1.03x faster                                                       |
| scimark_fft              | 187 ms                                                      | 184 ms: 1.02x faster                                                        |
| xml_etree_process        | 44.5 ms                                                     | 43.7 ms: 1.02x faster                                                       |
| logging_simple           | 6.22 us                                                     | 6.14 us: 1.01x faster                                                       |
| async_generators         | 222 ms                                                      | 220 ms: 1.01x faster                                                        |
| pickle_list              | 2.75 us                                                     | 2.80 us: 1.02x slower                                                       |
| pidigits                 | 149 ms                                                      | 154 ms: 1.03x slower                                                        |
| fannkuch                 | 256 ms                                                      | 267 ms: 1.04x slower                                                        |
| xml_etree_iterparse      | 65.0 ms                                                     | 68.1 ms: 1.05x slower                                                       |
| unpickle                 | 9.09 us                                                     | 9.53 us: 1.05x slower                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 102 ms: 1.05x slower                                                        |
| regex_v8                 | 15.4 ms                                                     | 16.5 ms: 1.07x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 63.6 ms: 1.15x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.85 us: 1.15x slower                                                       |
| json                     | 3.14 ms                                                     | 3.60 ms: 1.15x slower                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.93 ms: 1.16x slower                                                       |
| python_startup           | 20.6 ms                                                     | 25.7 ms: 1.25x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 19.8 ms: 1.28x slower                                                       |
| telco                    | 3.94 ms                                                     | 5.12 ms: 1.30x slower                                                       |
| coverage                 | 39.0 ms                                                     | 51.9 ms: 1.33x slower                                                       |
| json_loads               | 14.0 us                                                     | 19.3 us: 1.38x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 88.8 ms: 1.43x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.33 ms: 1.67x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.89 ms: 2.05x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.23x faster                                                                |
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (12) of results/bm-20250216-3.14.0a5+-359c7dd-CLANG/bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.235x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: unknown