# Results vs. 3.10.4

- fork: python
- ref: cf4c4ecc26c7e3b89f2e
- machine: windows-amd64
- commit hash: cf4c4ec
- commit date: 2025-02-01
- overall geometric mean: 1.278x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 221 ms: 1.11x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.73 sec: 1.11x faster                                                      |
| html5lib       | 51.0 ms                                                     | 38.3 ms: 1.33x faster                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 404 ms: 2.75x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 213 ms: 2.47x faster                                                        |
| async_tree_none         | 435 ms                                                      | 178 ms: 2.45x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 339 ms: 1.88x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.36x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 37.0 ms: 1.67x faster                                                       |
| nbody          | 71.3 ms                                                     | 50.4 ms: 1.42x faster                                                       |
| pidigits       | 149 ms                                                      | 150 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                       | 1.33x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 81.1 ms: 1.31x faster                                                       |
| regex_dna      | 136 ms                                                      | 115 ms: 1.19x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.42 ms: 1.17x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.8 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 110 us: 1.67x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.13 sec: 1.48x faster                                                      |
| json_dumps           | 9.16 ms                                                     | 6.24 ms: 1.47x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 198 us: 1.36x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 35.8 ms: 1.24x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 50.3 ms: 1.10x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 88.1 ms: 1.10x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 59.6 ms: 1.09x faster                                                       |
| unpickle             | 9.09 us                                                     | 8.77 us: 1.04x faster                                                       |
| unpickle_list        | 2.71 us                                                     | 2.67 us: 1.02x faster                                                       |
| pickle_dict          | 17.2 us                                                     | 18.4 us: 1.07x slower                                                       |
| json_loads           | 14.0 us                                                     | 15.5 us: 1.11x slower                                                       |
| pickle_list          | 2.75 us                                                     | 3.08 us: 1.12x slower                                                       |
| pickle               | 6.85 us                                                     | 8.11 us: 1.18x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.13x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 26.1 ms: 1.26x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 19.7 ms: 1.27x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.27x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.26 ms: 1.72x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 17.1 ms: 1.16x faster                                                       |
| django_template | 28.9 ms                                                     | 26.1 ms: 1.11x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 43.3 ms: 1.05x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.20x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 105 us: 3.20x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 404 ms: 2.75x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 213 ms: 2.47x faster                                                        |
| async_tree_none          | 435 ms                                                      | 178 ms: 2.45x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.13 ms: 1.96x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 339 ms: 1.88x faster                                                        |
| scimark_sor              | 106 ms                                                      | 57.5 ms: 1.85x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 54.0 ns: 1.75x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 16.5 us: 1.74x faster                                                       |
| mako                     | 9.03 ms                                                     | 5.26 ms: 1.72x faster                                                       |
| pylint                   | 350 ms                                                      | 205 ms: 1.71x faster                                                        |
| spectral_norm            | 77.3 ms                                                     | 46.3 ms: 1.67x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 110 us: 1.67x faster                                                        |
| float                    | 61.7 ms                                                     | 37.0 ms: 1.67x faster                                                       |
| go                       | 139 ms                                                      | 87.0 ms: 1.60x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 35.9 ms: 1.60x faster                                                       |
| pyflate                  | 409 ms                                                      | 267 ms: 1.53x faster                                                        |
| chaos                    | 61.7 ms                                                     | 40.7 ms: 1.52x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 809 us: 1.50x faster                                                        |
| scimark_lu               | 85.8 ms                                                     | 57.3 ms: 1.50x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.13 sec: 1.48x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.24 ms: 1.47x faster                                                       |
| richards_super           | 52.2 ms                                                     | 35.8 ms: 1.46x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.3 us: 1.46x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.45 sec: 1.46x faster                                                      |
| sqlglot_transpile        | 1.48 ms                                                     | 1.03 ms: 1.43x faster                                                       |
| nbody                    | 71.3 ms                                                     | 50.4 ms: 1.42x faster                                                       |
| deepcopy                 | 255 us                                                      | 185 us: 1.38x faster                                                        |
| crypto_pyaes             | 62.5 ms                                                     | 45.4 ms: 1.38x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 198 us: 1.36x faster                                                        |
| asyncio_tcp              | 732 ms                                                      | 543 ms: 1.35x faster                                                        |
| generators               | 32.4 ms                                                     | 24.0 ms: 1.35x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 38.3 ms: 1.33x faster                                                       |
| raytrace                 | 273 ms                                                      | 206 ms: 1.33x faster                                                        |
| richards                 | 42.4 ms                                                     | 32.0 ms: 1.33x faster                                                       |
| pycparser                | 930 ms                                                      | 707 ms: 1.32x faster                                                        |
| regex_compile            | 106 ms                                                      | 81.1 ms: 1.31x faster                                                       |
| scimark_fft              | 187 ms                                                      | 146 ms: 1.28x faster                                                        |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.15 ms: 1.26x faster                                                       |
| coroutines               | 16.0 ms                                                     | 12.8 ms: 1.25x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 60.7 ms: 1.25x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 35.8 ms: 1.24x faster                                                       |
| thrift                   | 617 us                                                      | 502 us: 1.23x faster                                                        |
| sqlite_synth             | 1.91 us                                                     | 1.56 us: 1.23x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.01 sec: 1.21x faster                                                      |
| regex_dna                | 136 ms                                                      | 115 ms: 1.19x faster                                                        |
| sympy_sum                | 107 ms                                                      | 90.3 ms: 1.18x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 42.6 ms: 1.18x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.87 us: 1.18x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.89 ms: 1.17x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.42 ms: 1.17x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 17.1 ms: 1.16x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.3 ms: 1.15x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 843 us: 1.14x faster                                                        |
| pprint_safe_repr         | 592 ms                                                      | 532 ms: 1.11x faster                                                        |
| 2to3                     | 246 ms                                                      | 221 ms: 1.11x faster                                                        |
| docutils                 | 1.92 sec                                                    | 1.73 sec: 1.11x faster                                                      |
| sympy_str                | 194 ms                                                      | 176 ms: 1.11x faster                                                        |
| django_template          | 28.9 ms                                                     | 26.1 ms: 1.11x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 50.3 ms: 1.10x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 88.1 ms: 1.10x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 36.4 ms: 1.09x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 59.6 ms: 1.09x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 61.7 ms: 1.08x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.65 sec: 1.08x faster                                                      |
| fannkuch                 | 256 ms                                                      | 237 ms: 1.08x faster                                                        |
| sympy_expand             | 314 ms                                                      | 300 ms: 1.05x faster                                                        |
| sqlglot_normalize        | 205 ms                                                      | 196 ms: 1.05x faster                                                        |
| regex_v8                 | 15.4 ms                                                     | 14.8 ms: 1.05x faster                                                       |
| unpickle                 | 9.09 us                                                     | 8.77 us: 1.04x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.59 us: 1.03x faster                                                       |
| json                     | 3.14 ms                                                     | 3.08 ms: 1.02x faster                                                       |
| unpickle_list            | 2.71 us                                                     | 2.67 us: 1.02x faster                                                       |
| logging_simple           | 6.22 us                                                     | 6.15 us: 1.01x faster                                                       |
| pidigits                 | 149 ms                                                      | 150 ms: 1.01x slower                                                        |
| async_generators         | 222 ms                                                      | 233 ms: 1.05x slower                                                        |
| genshi_xml               | 41.0 ms                                                     | 43.3 ms: 1.05x slower                                                       |
| unpack_sequence          | 39.6 ns                                                     | 41.9 ns: 1.06x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 18.4 us: 1.07x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.33 ms: 1.10x slower                                                       |
| json_loads               | 14.0 us                                                     | 15.5 us: 1.11x slower                                                       |
| pickle_list              | 2.75 us                                                     | 3.08 us: 1.12x slower                                                       |
| coverage                 | 39.0 ms                                                     | 46.1 ms: 1.18x slower                                                       |
| pickle                   | 6.85 us                                                     | 8.11 us: 1.18x slower                                                       |
| python_startup           | 20.6 ms                                                     | 26.1 ms: 1.26x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 19.7 ms: 1.27x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.03 ms: 1.44x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 89.6 ms: 1.44x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.23 ms: 1.53x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.25x faster                                                                |

Benchmark hidden because not significant (1): meteor_contest
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (12) of results/bm-20250201-3.14.0a4+-cf4c4ec-JIT/bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.278x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: unknown