# Results vs. 3.10.4

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: windows-amd64
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.260x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 221 ms: 1.11x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.71 sec: 1.12x faster                                                      |
| html5lib       | 51.0 ms                                                     | 39.9 ms: 1.28x faster                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 414 ms: 2.68x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 215 ms: 2.45x faster                                                        |
| async_tree_none         | 435 ms                                                      | 183 ms: 2.38x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 341 ms: 1.87x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.32x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 48.0 ms: 1.28x faster                                                       |
| nbody          | 71.3 ms                                                     | 60.0 ms: 1.19x faster                                                       |
| pidigits       | 149 ms                                                      | 154 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 83.4 ms: 1.27x faster                                                       |
| regex_dna      | 136 ms                                                      | 113 ms: 1.21x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.41 ms: 1.17x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.1 ms: 1.09x faster                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 116 us: 1.58x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.20 sec: 1.39x faster                                                      |
| json_dumps           | 9.16 ms                                                     | 6.70 ms: 1.37x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 213 us: 1.26x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 36.7 ms: 1.21x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 50.7 ms: 1.09x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 89.9 ms: 1.08x faster                                                       |
| unpickle             | 9.09 us                                                     | 8.65 us: 1.05x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.6 ms: 1.02x faster                                                       |
| json_loads           | 14.0 us                                                     | 14.8 us: 1.06x slower                                                       |
| unpickle_list        | 2.71 us                                                     | 2.89 us: 1.06x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 19.6 us: 1.14x slower                                                       |
| pickle_list          | 2.75 us                                                     | 3.17 us: 1.15x slower                                                       |
| pickle               | 6.85 us                                                     | 7.91 us: 1.15x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.09x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 24.6 ms: 1.20x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 19.0 ms: 1.23x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.21x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.25 ms: 1.72x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 16.4 ms: 1.21x faster                                                       |
| django_template | 28.9 ms                                                     | 25.5 ms: 1.13x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 36.9 ms: 1.11x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.27x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 109 us: 3.09x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 414 ms: 2.68x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 29.7 ms: 2.55x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 215 ms: 2.45x faster                                                        |
| async_tree_none          | 435 ms                                                      | 183 ms: 2.38x faster                                                        |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 341 ms: 1.87x faster                                                        |
| asyncio_tcp              | 732 ms                                                      | 393 ms: 1.86x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.25 ms: 1.86x faster                                                       |
| pylint                   | 350 ms                                                      | 200 ms: 1.75x faster                                                        |
| mako                     | 9.03 ms                                                     | 5.25 ms: 1.72x faster                                                       |
| generators               | 32.4 ms                                                     | 19.8 ms: 1.64x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.29 sec: 1.63x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 116 us: 1.58x faster                                                        |
| go                       | 139 ms                                                      | 89.5 ms: 1.55x faster                                                       |
| richards_super           | 52.2 ms                                                     | 34.1 ms: 1.53x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.0 us: 1.51x faster                                                       |
| pyflate                  | 409 ms                                                      | 278 ms: 1.47x faster                                                        |
| logging_silent           | 94.6 ns                                                     | 64.7 ns: 1.46x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 831 us: 1.46x faster                                                        |
| chaos                    | 61.7 ms                                                     | 42.4 ms: 1.46x faster                                                       |
| raytrace                 | 273 ms                                                      | 192 ms: 1.43x faster                                                        |
| sqlglot_transpile        | 1.48 ms                                                     | 1.06 ms: 1.40x faster                                                       |
| richards                 | 42.4 ms                                                     | 30.5 ms: 1.39x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 20.7 us: 1.39x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.20 sec: 1.39x faster                                                      |
| deepcopy                 | 255 us                                                      | 185 us: 1.38x faster                                                        |
| json_dumps               | 9.16 ms                                                     | 6.70 ms: 1.37x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 47.4 ms: 1.32x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 65.1 ms: 1.32x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.11 ms: 1.29x faster                                                       |
| float                    | 61.7 ms                                                     | 48.0 ms: 1.28x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.48 ms: 1.28x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 39.9 ms: 1.28x faster                                                       |
| regex_compile            | 106 ms                                                      | 83.4 ms: 1.27x faster                                                       |
| pycparser                | 930 ms                                                      | 735 ms: 1.27x faster                                                        |
| pickle_pure_python       | 270 us                                                      | 213 us: 1.26x faster                                                        |
| sqlite_synth             | 1.91 us                                                     | 1.53 us: 1.25x faster                                                       |
| scimark_fft              | 187 ms                                                      | 152 ms: 1.23x faster                                                        |
| pprint_pformat           | 1.22 sec                                                    | 999 ms: 1.22x faster                                                        |
| scimark_monte_carlo      | 57.3 ms                                                     | 47.1 ms: 1.22x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 36.7 ms: 1.21x faster                                                       |
| thrift                   | 617 us                                                      | 509 us: 1.21x faster                                                        |
| regex_dna                | 136 ms                                                      | 113 ms: 1.21x faster                                                        |
| genshi_text              | 19.8 ms                                                     | 16.4 ms: 1.21x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.3 ms: 1.20x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 493 ms: 1.20x faster                                                        |
| dulwich_log              | 50.5 ms                                                     | 42.1 ms: 1.20x faster                                                       |
| sympy_sum                | 107 ms                                                      | 89.7 ms: 1.19x faster                                                       |
| nbody                    | 71.3 ms                                                     | 60.0 ms: 1.19x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 65.3 ms: 1.18x faster                                                       |
| scimark_sor              | 106 ms                                                      | 90.1 ms: 1.18x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.41 ms: 1.17x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.93 us: 1.14x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.4 ms: 1.14x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.56 sec: 1.14x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 843 us: 1.14x faster                                                        |
| django_template          | 28.9 ms                                                     | 25.5 ms: 1.13x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.71 sec: 1.12x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 36.9 ms: 1.11x faster                                                       |
| 2to3                     | 246 ms                                                      | 221 ms: 1.11x faster                                                        |
| sympy_str                | 194 ms                                                      | 177 ms: 1.10x faster                                                        |
| sqlglot_optimize         | 39.8 ms                                                     | 36.3 ms: 1.10x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 50.7 ms: 1.09x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 14.1 ms: 1.09x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 61.1 ms: 1.09x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 89.9 ms: 1.08x faster                                                       |
| fannkuch                 | 256 ms                                                      | 238 ms: 1.07x faster                                                        |
| unpickle                 | 9.09 us                                                     | 8.65 us: 1.05x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 195 ms: 1.05x faster                                                        |
| json                     | 3.14 ms                                                     | 3.00 ms: 1.04x faster                                                       |
| sympy_expand             | 314 ms                                                      | 306 ms: 1.03x faster                                                        |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.6 ms: 1.02x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 74.6 ms: 1.02x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.92 us: 1.02x slower                                                       |
| pidigits                 | 149 ms                                                      | 154 ms: 1.03x slower                                                        |
| logging_simple           | 6.22 us                                                     | 6.41 us: 1.03x slower                                                       |
| async_generators         | 222 ms                                                      | 234 ms: 1.06x slower                                                        |
| json_loads               | 14.0 us                                                     | 14.8 us: 1.06x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 2.89 us: 1.06x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.39 ms: 1.11x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 19.6 us: 1.14x slower                                                       |
| pickle_list              | 2.75 us                                                     | 3.17 us: 1.15x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.91 us: 1.15x slower                                                       |
| unpack_sequence          | 39.6 ns                                                     | 45.8 ns: 1.16x slower                                                       |
| python_startup           | 20.6 ms                                                     | 24.6 ms: 1.20x slower                                                       |
| coverage                 | 39.0 ms                                                     | 47.6 ms: 1.22x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 19.0 ms: 1.23x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 85.2 ms: 1.37x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.96 ms: 1.39x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.21 ms: 1.52x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.23x faster                                                                |
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (12) of results/bm-20250222-3.14.0a5+-5ec4bf8-JIT/bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.260x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: unknown