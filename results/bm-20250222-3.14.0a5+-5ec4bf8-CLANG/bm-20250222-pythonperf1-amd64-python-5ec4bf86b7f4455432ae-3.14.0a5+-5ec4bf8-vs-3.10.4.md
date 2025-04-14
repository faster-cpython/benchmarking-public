# Results vs. 3.10.4

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: windows-amd64
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.231x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 225 ms: 1.09x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.74 sec: 1.11x faster                                                      |
| html5lib       | 51.0 ms                                                     | 38.8 ms: 1.32x faster                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 402 ms: 2.76x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 205 ms: 2.57x faster                                                        |
| async_tree_none         | 435 ms                                                      | 175 ms: 2.49x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 354 ms: 1.80x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.37x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 44.4 ms: 1.39x faster                                                       |
| nbody          | 71.3 ms                                                     | 62.8 ms: 1.14x faster                                                       |
| pidigits       | 149 ms                                                      | 154 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 84.2 ms: 1.26x faster                                                       |
| regex_dna      | 136 ms                                                      | 132 ms: 1.03x faster                                                        |
| regex_v8       | 15.4 ms                                                     | 16.7 ms: 1.08x slower                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.95 ms: 1.18x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 270 us                                                      | 210 us: 1.29x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.32 sec: 1.27x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 147 us: 1.24x faster                                                        |
| json_dumps           | 9.16 ms                                                     | 7.83 ms: 1.17x faster                                                       |
| pickle_dict          | 17.2 us                                                     | 15.6 us: 1.10x faster                                                       |
| unpickle_list        | 2.71 us                                                     | 2.47 us: 1.10x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 45.1 ms: 1.01x slower                                                       |
| unpickle             | 9.09 us                                                     | 9.50 us: 1.05x slower                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 68.8 ms: 1.06x slower                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 103 ms: 1.06x slower                                                        |
| pickle_list          | 2.75 us                                                     | 2.93 us: 1.06x slower                                                       |
| pickle               | 6.85 us                                                     | 7.80 us: 1.14x slower                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 63.8 ms: 1.15x slower                                                       |
| json_loads           | 14.0 us                                                     | 19.5 us: 1.39x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.4 ms: 1.25x slower                                                       |
| python_startup         | 20.6 ms                                                     | 25.8 ms: 1.25x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 19.8 ms                                                     | 14.7 ms: 1.35x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 31.8 ms: 1.29x faster                                                       |
| mako            | 9.03 ms                                                     | 7.32 ms: 1.23x faster                                                       |
| django_template | 28.9 ms                                                     | 24.2 ms: 1.19x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.26x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 112 us: 3.00x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 402 ms: 2.76x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 205 ms: 2.57x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 30.0 ms: 2.53x faster                                                       |
| async_tree_none          | 435 ms                                                      | 175 ms: 2.49x faster                                                        |
| deltablue                | 4.19 ms                                                     | 1.84 ms: 2.27x faster                                                       |
| go                       | 139 ms                                                      | 71.6 ms: 1.94x faster                                                       |
| generators               | 32.4 ms                                                     | 17.1 ms: 1.90x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 389 ms: 1.88x faster                                                        |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 354 ms: 1.80x faster                                                        |
| pylint                   | 350 ms                                                      | 201 ms: 1.74x faster                                                        |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.30 sec: 1.63x faster                                                      |
| raytrace                 | 273 ms                                                      | 168 ms: 1.62x faster                                                        |
| richards_super           | 52.2 ms                                                     | 32.2 ms: 1.62x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 60.0 ns: 1.58x faster                                                       |
| chaos                    | 61.7 ms                                                     | 39.1 ms: 1.58x faster                                                       |
| scimark_sor              | 106 ms                                                      | 69.2 ms: 1.54x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 18.9 us: 1.52x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 808 us: 1.50x faster                                                        |
| richards                 | 42.4 ms                                                     | 28.3 ms: 1.50x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 39.0 ms: 1.47x faster                                                       |
| unpack_sequence          | 39.6 ns                                                     | 27.0 ns: 1.47x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.4 us: 1.45x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 3.98 ms: 1.44x faster                                                       |
| deepcopy                 | 255 us                                                      | 177 us: 1.44x faster                                                        |
| sqlglot_transpile        | 1.48 ms                                                     | 1.02 ms: 1.44x faster                                                       |
| pyflate                  | 409 ms                                                      | 290 ms: 1.41x faster                                                        |
| float                    | 61.7 ms                                                     | 44.4 ms: 1.39x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 63.1 ms: 1.36x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 14.7 ms: 1.35x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 58.4 ms: 1.32x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 38.8 ms: 1.32x faster                                                       |
| pycparser                | 930 ms                                                      | 709 ms: 1.31x faster                                                        |
| genshi_xml               | 41.0 ms                                                     | 31.8 ms: 1.29x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 210 us: 1.29x faster                                                        |
| tomli_loads              | 1.67 sec                                                    | 1.32 sec: 1.27x faster                                                      |
| regex_compile            | 106 ms                                                      | 84.2 ms: 1.26x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 147 us: 1.24x faster                                                        |
| mako                     | 9.03 ms                                                     | 7.32 ms: 1.23x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.0 ms: 1.23x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 41.7 ms: 1.21x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 52.0 ms: 1.20x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.60 us: 1.19x faster                                                       |
| django_template          | 28.9 ms                                                     | 24.2 ms: 1.19x faster                                                       |
| sympy_sum                | 107 ms                                                      | 91.0 ms: 1.18x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 7.83 ms: 1.17x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.89 us: 1.17x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.06 sec: 1.15x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.3 ms: 1.15x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 520 ms: 1.14x faster                                                        |
| thrift                   | 617 us                                                      | 543 us: 1.14x faster                                                        |
| nbody                    | 71.3 ms                                                     | 62.8 ms: 1.14x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 35.3 ms: 1.13x faster                                                       |
| sympy_str                | 194 ms                                                      | 176 ms: 1.11x faster                                                        |
| docutils                 | 1.92 sec                                                    | 1.74 sec: 1.11x faster                                                      |
| pickle_dict              | 17.2 us                                                     | 15.6 us: 1.10x faster                                                       |
| unpickle_list            | 2.71 us                                                     | 2.47 us: 1.10x faster                                                       |
| 2to3                     | 246 ms                                                      | 225 ms: 1.09x faster                                                        |
| bench_thread_pool        | 958 us                                                      | 879 us: 1.09x faster                                                        |
| mdp                      | 1.78 sec                                                    | 1.65 sec: 1.08x faster                                                      |
| sqlglot_normalize        | 205 ms                                                      | 191 ms: 1.08x faster                                                        |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.55 ms: 1.07x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 62.9 ms: 1.06x faster                                                       |
| sympy_expand             | 314 ms                                                      | 301 ms: 1.05x faster                                                        |
| scimark_fft              | 187 ms                                                      | 181 ms: 1.04x faster                                                        |
| meteor_contest           | 75.9 ms                                                     | 73.3 ms: 1.04x faster                                                       |
| regex_dna                | 136 ms                                                      | 132 ms: 1.03x faster                                                        |
| logging_format           | 6.76 us                                                     | 6.61 us: 1.02x faster                                                       |
| async_generators         | 222 ms                                                      | 219 ms: 1.01x faster                                                        |
| logging_simple           | 6.22 us                                                     | 6.18 us: 1.01x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 45.1 ms: 1.01x slower                                                       |
| pidigits                 | 149 ms                                                      | 154 ms: 1.03x slower                                                        |
| unpickle                 | 9.09 us                                                     | 9.50 us: 1.05x slower                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 68.8 ms: 1.06x slower                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 103 ms: 1.06x slower                                                        |
| pickle_list              | 2.75 us                                                     | 2.93 us: 1.06x slower                                                       |
| regex_v8                 | 15.4 ms                                                     | 16.7 ms: 1.08x slower                                                       |
| fannkuch                 | 256 ms                                                      | 277 ms: 1.08x slower                                                        |
| json                     | 3.14 ms                                                     | 3.55 ms: 1.13x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.80 us: 1.14x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 63.8 ms: 1.15x slower                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.95 ms: 1.18x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 19.4 ms: 1.25x slower                                                       |
| python_startup           | 20.6 ms                                                     | 25.8 ms: 1.25x slower                                                       |
| telco                    | 3.94 ms                                                     | 5.10 ms: 1.29x slower                                                       |
| coverage                 | 39.0 ms                                                     | 53.1 ms: 1.36x slower                                                       |
| json_loads               | 14.0 us                                                     | 19.5 us: 1.39x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 89.9 ms: 1.45x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.33 ms: 1.66x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.55 ms: 1.81x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.22x faster                                                                |
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (12) of results/bm-20250222-3.14.0a5+-5ec4bf8-CLANG/bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.231x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown