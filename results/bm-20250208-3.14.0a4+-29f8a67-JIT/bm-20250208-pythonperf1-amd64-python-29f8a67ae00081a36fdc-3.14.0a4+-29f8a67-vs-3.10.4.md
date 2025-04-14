# Results vs. 3.10.4

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: windows-amd64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.248x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 225 ms: 1.09x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.74 sec: 1.11x faster                                                      |
| html5lib       | 51.0 ms                                                     | 39.3 ms: 1.30x faster                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 419 ms: 2.65x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 222 ms: 2.37x faster                                                        |
| async_tree_none         | 435 ms                                                      | 186 ms: 2.34x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 342 ms: 1.87x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.29x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 46.1 ms: 1.34x faster                                                       |
| nbody          | 71.3 ms                                                     | 57.1 ms: 1.25x faster                                                       |
| pidigits       | 149 ms                                                      | 152 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 82.2 ms: 1.29x faster                                                       |
| regex_dna      | 136 ms                                                      | 117 ms: 1.16x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.51 ms: 1.10x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 15.0 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 113 us: 1.61x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.19 sec: 1.41x faster                                                      |
| json_dumps           | 9.16 ms                                                     | 6.69 ms: 1.37x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 217 us: 1.24x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 36.7 ms: 1.21x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 50.8 ms: 1.09x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 90.1 ms: 1.07x faster                                                       |
| unpickle             | 9.09 us                                                     | 8.51 us: 1.07x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 61.1 ms: 1.06x faster                                                       |
| unpickle_list        | 2.71 us                                                     | 2.63 us: 1.03x faster                                                       |
| pickle_dict          | 17.2 us                                                     | 18.0 us: 1.05x slower                                                       |
| pickle_list          | 2.75 us                                                     | 3.00 us: 1.09x slower                                                       |
| json_loads           | 14.0 us                                                     | 15.5 us: 1.10x slower                                                       |
| pickle               | 6.85 us                                                     | 7.81 us: 1.14x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.11x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.7 ms: 1.27x slower                                                       |
| python_startup         | 20.6 ms                                                     | 26.4 ms: 1.28x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.28x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.24 ms: 1.72x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 16.0 ms: 1.24x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 35.4 ms: 1.16x faster                                                       |
| django_template | 28.9 ms                                                     | 25.8 ms: 1.12x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.29x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 108 us: 3.11x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 419 ms: 2.65x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 222 ms: 2.37x faster                                                        |
| async_tree_none          | 435 ms                                                      | 186 ms: 2.34x faster                                                        |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 342 ms: 1.87x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.34 ms: 1.79x faster                                                       |
| pylint                   | 350 ms                                                      | 203 ms: 1.73x faster                                                        |
| mako                     | 9.03 ms                                                     | 5.24 ms: 1.72x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 113 us: 1.61x faster                                                        |
| generators               | 32.4 ms                                                     | 20.2 ms: 1.61x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 59.5 ns: 1.59x faster                                                       |
| go                       | 139 ms                                                      | 87.6 ms: 1.59x faster                                                       |
| richards_super           | 52.2 ms                                                     | 33.6 ms: 1.56x faster                                                       |
| pyflate                  | 409 ms                                                      | 273 ms: 1.50x faster                                                        |
| deepcopy_memo            | 28.8 us                                                     | 19.4 us: 1.48x faster                                                       |
| chaos                    | 61.7 ms                                                     | 41.7 ms: 1.48x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.2 us: 1.47x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.44 sec: 1.47x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 842 us: 1.44x faster                                                        |
| richards                 | 42.4 ms                                                     | 29.7 ms: 1.43x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.19 sec: 1.41x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 61.1 ms: 1.40x faster                                                       |
| raytrace                 | 273 ms                                                      | 195 ms: 1.40x faster                                                        |
| sqlglot_transpile        | 1.48 ms                                                     | 1.06 ms: 1.39x faster                                                       |
| deepcopy                 | 255 us                                                      | 186 us: 1.37x faster                                                        |
| json_dumps               | 9.16 ms                                                     | 6.69 ms: 1.37x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 45.8 ms: 1.37x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 541 ms: 1.35x faster                                                        |
| float                    | 61.7 ms                                                     | 46.1 ms: 1.34x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 57.9 ms: 1.33x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.09 ms: 1.31x faster                                                       |
| pycparser                | 930 ms                                                      | 713 ms: 1.30x faster                                                        |
| hexiom                   | 5.74 ms                                                     | 4.42 ms: 1.30x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 39.3 ms: 1.30x faster                                                       |
| regex_compile            | 106 ms                                                      | 82.2 ms: 1.29x faster                                                       |
| scimark_fft              | 187 ms                                                      | 148 ms: 1.27x faster                                                        |
| scimark_monte_carlo      | 57.3 ms                                                     | 45.4 ms: 1.26x faster                                                       |
| scimark_sor              | 106 ms                                                      | 84.2 ms: 1.26x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 975 ms: 1.25x faster                                                        |
| nbody                    | 71.3 ms                                                     | 57.1 ms: 1.25x faster                                                       |
| coroutines               | 16.0 ms                                                     | 12.8 ms: 1.25x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.54 us: 1.24x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 217 us: 1.24x faster                                                        |
| genshi_text              | 19.8 ms                                                     | 16.0 ms: 1.24x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 62.1 ms: 1.22x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 36.7 ms: 1.21x faster                                                       |
| thrift                   | 617 us                                                      | 516 us: 1.20x faster                                                        |
| dulwich_log              | 50.5 ms                                                     | 42.5 ms: 1.19x faster                                                       |
| sympy_sum                | 107 ms                                                      | 90.5 ms: 1.18x faster                                                       |
| regex_dna                | 136 ms                                                      | 117 ms: 1.16x faster                                                        |
| genshi_xml               | 41.0 ms                                                     | 35.4 ms: 1.16x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 512 ms: 1.16x faster                                                        |
| deepcopy_reduce          | 2.20 us                                                     | 1.95 us: 1.13x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.5 ms: 1.13x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 855 us: 1.12x faster                                                        |
| django_template          | 28.9 ms                                                     | 25.8 ms: 1.12x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.60 sec: 1.11x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.74 sec: 1.11x faster                                                      |
| sympy_str                | 194 ms                                                      | 177 ms: 1.10x faster                                                        |
| regex_effbot             | 1.66 ms                                                     | 1.51 ms: 1.10x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 50.8 ms: 1.09x faster                                                       |
| 2to3                     | 246 ms                                                      | 225 ms: 1.09x faster                                                        |
| nqueens                  | 66.6 ms                                                     | 62.0 ms: 1.08x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 90.1 ms: 1.07x faster                                                       |
| fannkuch                 | 256 ms                                                      | 239 ms: 1.07x faster                                                        |
| unpickle                 | 9.09 us                                                     | 8.51 us: 1.07x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 61.1 ms: 1.06x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 37.6 ms: 1.06x faster                                                       |
| unpickle_list            | 2.71 us                                                     | 2.63 us: 1.03x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 15.0 ms: 1.03x faster                                                       |
| sympy_expand             | 314 ms                                                      | 307 ms: 1.02x faster                                                        |
| sqlglot_normalize        | 205 ms                                                      | 203 ms: 1.01x faster                                                        |
| logging_format           | 6.76 us                                                     | 6.83 us: 1.01x slower                                                       |
| pidigits                 | 149 ms                                                      | 152 ms: 1.02x slower                                                        |
| logging_simple           | 6.22 us                                                     | 6.41 us: 1.03x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 18.0 us: 1.05x slower                                                       |
| async_generators         | 222 ms                                                      | 240 ms: 1.08x slower                                                        |
| pickle_list              | 2.75 us                                                     | 3.00 us: 1.09x slower                                                       |
| unpack_sequence          | 39.6 ns                                                     | 43.6 ns: 1.10x slower                                                       |
| json_loads               | 14.0 us                                                     | 15.5 us: 1.10x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.81 us: 1.14x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.55 ms: 1.15x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 19.7 ms: 1.27x slower                                                       |
| coverage                 | 39.0 ms                                                     | 49.6 ms: 1.27x slower                                                       |
| python_startup           | 20.6 ms                                                     | 26.4 ms: 1.28x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 89.9 ms: 1.45x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.05 ms: 1.46x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.24 ms: 1.55x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.22x faster                                                                |

Benchmark hidden because not significant (2): json, meteor_contest
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (12) of results/bm-20250208-3.14.0a4+-29f8a67-JIT/bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.248x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: unknown