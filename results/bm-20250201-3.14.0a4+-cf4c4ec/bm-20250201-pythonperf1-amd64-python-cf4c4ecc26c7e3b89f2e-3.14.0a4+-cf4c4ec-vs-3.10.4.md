# Results vs. 3.10.4

- fork: python
- ref: cf4c4ecc26c7e3b89f2e
- machine: windows-amd64
- commit hash: cf4c4ec
- commit date: 2025-02-01
- overall geometric mean: 1.263x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 222 ms: 1.11x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.64 sec: 1.17x faster                                                      |
| html5lib       | 51.0 ms                                                     | 37.4 ms: 1.36x faster                                                       |
| Geometric mean | (ref)                                                       | 1.21x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 400 ms: 2.77x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 217 ms: 2.42x faster                                                        |
| async_tree_none         | 435 ms                                                      | 181 ms: 2.41x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 339 ms: 1.88x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.35x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 45.0 ms: 1.37x faster                                                       |
| nbody          | 71.3 ms                                                     | 64.2 ms: 1.11x faster                                                       |
| pidigits       | 149 ms                                                      | 151 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 81.6 ms: 1.30x faster                                                       |
| regex_dna      | 136 ms                                                      | 117 ms: 1.17x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.48 ms: 1.12x faster                                                       |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.64 ms: 1.38x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 140 us: 1.31x faster                                                        |
| pickle_pure_python   | 270 us                                                      | 210 us: 1.28x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.31 sec: 1.27x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 38.6 ms: 1.15x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 89.4 ms: 1.08x faster                                                       |
| unpickle             | 9.09 us                                                     | 8.61 us: 1.06x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.8 ms: 1.03x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 54.8 ms: 1.01x faster                                                       |
| unpickle_list        | 2.71 us                                                     | 2.77 us: 1.02x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 18.1 us: 1.05x slower                                                       |
| json_loads           | 14.0 us                                                     | 15.4 us: 1.09x slower                                                       |
| pickle_list          | 2.75 us                                                     | 3.08 us: 1.12x slower                                                       |
| pickle               | 6.85 us                                                     | 8.01 us: 1.17x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.07x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 24.9 ms: 1.21x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 19.1 ms: 1.23x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.22x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 19.8 ms                                                     | 14.6 ms: 1.35x faster                                                       |
| mako            | 9.03 ms                                                     | 6.69 ms: 1.35x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 31.6 ms: 1.30x faster                                                       |
| django_template | 28.9 ms                                                     | 23.5 ms: 1.23x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.31x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 103 us: 3.27x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 400 ms: 2.77x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 217 ms: 2.42x faster                                                        |
| async_tree_none          | 435 ms                                                      | 181 ms: 2.41x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.08 ms: 2.02x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 339 ms: 1.88x faster                                                        |
| pylint                   | 350 ms                                                      | 191 ms: 1.84x faster                                                        |
| generators               | 32.4 ms                                                     | 18.0 ms: 1.80x faster                                                       |
| go                       | 139 ms                                                      | 80.7 ms: 1.72x faster                                                       |
| richards_super           | 52.2 ms                                                     | 31.8 ms: 1.64x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 452 ms: 1.62x faster                                                        |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.35 sec: 1.57x faster                                                      |
| chaos                    | 61.7 ms                                                     | 39.5 ms: 1.56x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 60.8 ns: 1.56x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 18.9 us: 1.52x faster                                                       |
| richards                 | 42.4 ms                                                     | 28.1 ms: 1.51x faster                                                       |
| raytrace                 | 273 ms                                                      | 182 ms: 1.50x faster                                                        |
| comprehensions           | 16.5 us                                                     | 11.0 us: 1.50x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 819 us: 1.48x faster                                                        |
| deepcopy                 | 255 us                                                      | 174 us: 1.47x faster                                                        |
| sqlglot_transpile        | 1.48 ms                                                     | 1.02 ms: 1.45x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 59.3 ms: 1.45x faster                                                       |
| pyflate                  | 409 ms                                                      | 290 ms: 1.41x faster                                                        |
| hexiom                   | 5.74 ms                                                     | 4.08 ms: 1.41x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.64 ms: 1.38x faster                                                       |
| float                    | 61.7 ms                                                     | 45.0 ms: 1.37x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 37.4 ms: 1.36x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 14.6 ms: 1.35x faster                                                       |
| mako                     | 9.03 ms                                                     | 6.69 ms: 1.35x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 46.8 ms: 1.34x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 57.8 ms: 1.34x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 140 us: 1.31x faster                                                        |
| pycparser                | 930 ms                                                      | 713 ms: 1.30x faster                                                        |
| scimark_monte_carlo      | 57.3 ms                                                     | 44.0 ms: 1.30x faster                                                       |
| regex_compile            | 106 ms                                                      | 81.6 ms: 1.30x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 31.6 ms: 1.30x faster                                                       |
| scimark_sor              | 106 ms                                                      | 82.2 ms: 1.29x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 210 us: 1.28x faster                                                        |
| tomli_loads              | 1.67 sec                                                    | 1.31 sec: 1.27x faster                                                      |
| pathlib                  | 75.7 ms                                                     | 60.6 ms: 1.25x faster                                                       |
| thrift                   | 617 us                                                      | 500 us: 1.24x faster                                                        |
| sympy_sum                | 107 ms                                                      | 87.0 ms: 1.23x faster                                                       |
| django_template          | 28.9 ms                                                     | 23.5 ms: 1.23x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 41.4 ms: 1.22x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.46 sec: 1.22x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.81 us: 1.22x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.57 us: 1.21x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.2 ms: 1.21x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 12.9 ms: 1.18x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 33.8 ms: 1.18x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.04 sec: 1.18x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.64 sec: 1.17x faster                                                      |
| regex_dna                | 136 ms                                                      | 117 ms: 1.17x faster                                                        |
| pprint_safe_repr         | 592 ms                                                      | 513 ms: 1.15x faster                                                        |
| xml_etree_process        | 44.5 ms                                                     | 38.6 ms: 1.15x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 836 us: 1.15x faster                                                        |
| sympy_str                | 194 ms                                                      | 170 ms: 1.14x faster                                                        |
| sqlglot_normalize        | 205 ms                                                      | 183 ms: 1.12x faster                                                        |
| nqueens                  | 66.6 ms                                                     | 59.4 ms: 1.12x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.48 ms: 1.12x faster                                                       |
| nbody                    | 71.3 ms                                                     | 64.2 ms: 1.11x faster                                                       |
| 2to3                     | 246 ms                                                      | 222 ms: 1.11x faster                                                        |
| xml_etree_parse          | 96.8 ms                                                     | 89.4 ms: 1.08x faster                                                       |
| sympy_expand             | 314 ms                                                      | 293 ms: 1.07x faster                                                        |
| unpickle                 | 9.09 us                                                     | 8.61 us: 1.06x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.61 ms: 1.04x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.8 ms: 1.03x faster                                                       |
| scimark_fft              | 187 ms                                                      | 182 ms: 1.03x faster                                                        |
| async_generators         | 222 ms                                                      | 216 ms: 1.02x faster                                                        |
| meteor_contest           | 75.9 ms                                                     | 74.2 ms: 1.02x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.61 us: 1.02x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 54.8 ms: 1.01x faster                                                       |
| logging_simple           | 6.22 us                                                     | 6.16 us: 1.01x faster                                                       |
| pidigits                 | 149 ms                                                      | 151 ms: 1.01x slower                                                        |
| fannkuch                 | 256 ms                                                      | 259 ms: 1.01x slower                                                        |
| unpickle_list            | 2.71 us                                                     | 2.77 us: 1.02x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 18.1 us: 1.05x slower                                                       |
| unpack_sequence          | 39.6 ns                                                     | 42.1 ns: 1.06x slower                                                       |
| json_loads               | 14.0 us                                                     | 15.4 us: 1.09x slower                                                       |
| pickle_list              | 2.75 us                                                     | 3.08 us: 1.12x slower                                                       |
| pickle                   | 6.85 us                                                     | 8.01 us: 1.17x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.66 ms: 1.18x slower                                                       |
| coverage                 | 39.0 ms                                                     | 47.1 ms: 1.21x slower                                                       |
| python_startup           | 20.6 ms                                                     | 24.9 ms: 1.21x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 19.1 ms: 1.23x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.02 ms: 1.43x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 89.2 ms: 1.44x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.22 ms: 1.52x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.24x faster                                                                |

Benchmark hidden because not significant (2): regex_v8, json
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (12) of results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.263x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: unknown