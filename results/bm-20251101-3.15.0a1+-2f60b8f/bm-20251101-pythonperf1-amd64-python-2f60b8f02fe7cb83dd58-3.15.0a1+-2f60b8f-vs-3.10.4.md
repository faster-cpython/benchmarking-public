# Results vs. 3.10.4

- fork: python
- ref: 2f60b8f02fe7cb83dd58
- machine: windows-amd64
- commit hash: 2f60b8f
- commit date: 2025-11-01
- overall geometric mean: 1.287x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 220 ms: 1.12x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.62 sec: 1.18x faster                                                      |
| html5lib       | 51.0 ms                                                     | 37.2 ms: 1.37x faster                                                       |
| Geometric mean | (ref)                                                       | 1.22x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 371 ms: 2.99x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 198 ms: 2.66x faster                                                        |
| async_tree_none         | 435 ms                                                      | 169 ms: 2.58x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 321 ms: 1.98x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.53x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 44.3 ms: 1.39x faster                                                       |
| nbody          | 71.3 ms                                                     | 65.2 ms: 1.09x faster                                                       |
| pidigits       | 149 ms                                                      | 144 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 81.7 ms: 1.30x faster                                                       |
| regex_dna      | 136 ms                                                      | 121 ms: 1.13x faster                                                        |
| regex_v8       | 15.4 ms                                                     | 14.5 ms: 1.07x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                       |
| Geometric mean | (ref)                                                       | 1.13x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.54 ms: 1.65x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 134 us: 1.36x faster                                                        |
| pickle_pure_python   | 270 us                                                      | 215 us: 1.25x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.40 sec: 1.20x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 38.9 ms: 1.14x faster                                                       |
| unpickle             | 9.09 us                                                     | 8.29 us: 1.10x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 59.4 ms: 1.09x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 88.5 ms: 1.09x faster                                                       |
| json_loads           | 14.0 us                                                     | 14.2 us: 1.01x slower                                                       |
| unpickle_list        | 2.71 us                                                     | 2.80 us: 1.03x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 19.5 us: 1.13x slower                                                       |
| pickle_list          | 2.75 us                                                     | 3.20 us: 1.16x slower                                                       |
| pickle               | 6.85 us                                                     | 8.07 us: 1.18x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.09x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.8 ms: 1.25x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 19.4 ms: 1.25x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.73 ms: 1.34x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 15.8 ms: 1.25x faster                                                       |
| django_template | 28.9 ms                                                     | 23.9 ms: 1.21x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 34.6 ms: 1.19x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.25x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 102 us: 3.28x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 371 ms: 2.99x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 198 ms: 2.66x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 28.8 ms: 2.62x faster                                                       |
| async_tree_none          | 435 ms                                                      | 169 ms: 2.58x faster                                                        |
| mdp                      | 1.78 sec                                                    | 826 ms: 2.16x faster                                                        |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 321 ms: 1.98x faster                                                        |
| asyncio_tcp              | 732 ms                                                      | 379 ms: 1.93x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.23 ms: 1.88x faster                                                       |
| go                       | 139 ms                                                      | 77.3 ms: 1.80x faster                                                       |
| pylint                   | 350 ms                                                      | 201 ms: 1.74x faster                                                        |
| logging_silent           | 94.6 ns                                                     | 56.0 ns: 1.69x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 17.2 us: 1.67x faster                                                       |
| richards_super           | 52.2 ms                                                     | 31.6 ms: 1.65x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 5.54 ms: 1.65x faster                                                       |
| generators               | 32.4 ms                                                     | 19.8 ms: 1.64x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.29 sec: 1.63x faster                                                      |
| deepcopy                 | 255 us                                                      | 165 us: 1.55x faster                                                        |
| chaos                    | 61.7 ms                                                     | 40.4 ms: 1.53x faster                                                       |
| raytrace                 | 273 ms                                                      | 179 ms: 1.53x faster                                                        |
| richards                 | 42.4 ms                                                     | 28.0 ms: 1.52x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.2 us: 1.47x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 59.9 ms: 1.43x faster                                                       |
| pyflate                  | 409 ms                                                      | 288 ms: 1.42x faster                                                        |
| scimark_monte_carlo      | 57.3 ms                                                     | 41.0 ms: 1.40x faster                                                       |
| float                    | 61.7 ms                                                     | 44.3 ms: 1.39x faster                                                       |
| scimark_sor              | 106 ms                                                      | 76.4 ms: 1.39x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.18 ms: 1.37x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 37.2 ms: 1.37x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 134 us: 1.36x faster                                                        |
| mako                     | 9.03 ms                                                     | 6.73 ms: 1.34x faster                                                       |
| pycparser                | 930 ms                                                      | 696 ms: 1.34x faster                                                        |
| crypto_pyaes             | 62.5 ms                                                     | 47.8 ms: 1.31x faster                                                       |
| regex_compile            | 106 ms                                                      | 81.7 ms: 1.30x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 215 us: 1.25x faster                                                        |
| genshi_text              | 19.8 ms                                                     | 15.8 ms: 1.25x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.77 us: 1.24x faster                                                       |
| sympy_sum                | 107 ms                                                      | 87.4 ms: 1.22x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 41.3 ms: 1.22x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 12.5 ms: 1.22x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 997 ms: 1.22x faster                                                        |
| thrift                   | 617 us                                                      | 506 us: 1.22x faster                                                        |
| pprint_safe_repr         | 592 ms                                                      | 488 ms: 1.21x faster                                                        |
| django_template          | 28.9 ms                                                     | 23.9 ms: 1.21x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.59 us: 1.21x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 64.5 ms: 1.20x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.40 sec: 1.20x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 34.6 ms: 1.19x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.62 sec: 1.18x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 38.9 ms: 1.14x faster                                                       |
| sympy_str                | 194 ms                                                      | 170 ms: 1.14x faster                                                        |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.40 ms: 1.14x faster                                                       |
| regex_dna                | 136 ms                                                      | 121 ms: 1.13x faster                                                        |
| scimark_fft              | 187 ms                                                      | 167 ms: 1.12x faster                                                        |
| 2to3                     | 246 ms                                                      | 220 ms: 1.12x faster                                                        |
| coroutines               | 16.0 ms                                                     | 14.5 ms: 1.11x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 869 us: 1.10x faster                                                        |
| unpickle                 | 9.09 us                                                     | 8.29 us: 1.10x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 59.4 ms: 1.09x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 88.5 ms: 1.09x faster                                                       |
| nbody                    | 71.3 ms                                                     | 65.2 ms: 1.09x faster                                                       |
| sympy_expand             | 314 ms                                                      | 290 ms: 1.08x faster                                                        |
| json                     | 3.14 ms                                                     | 2.92 ms: 1.08x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 14.5 ms: 1.07x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 63.6 ms: 1.05x faster                                                       |
| unpack_sequence          | 39.6 ns                                                     | 37.9 ns: 1.05x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 73.1 ms: 1.04x faster                                                       |
| pidigits                 | 149 ms                                                      | 144 ms: 1.03x faster                                                        |
| logging_format           | 6.76 us                                                     | 6.54 us: 1.03x faster                                                       |
| logging_simple           | 6.22 us                                                     | 6.05 us: 1.03x faster                                                       |
| json_loads               | 14.0 us                                                     | 14.2 us: 1.01x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 2.80 us: 1.03x slower                                                       |
| async_generators         | 222 ms                                                      | 233 ms: 1.05x slower                                                        |
| fannkuch                 | 256 ms                                                      | 274 ms: 1.07x slower                                                        |
| telco                    | 3.94 ms                                                     | 4.26 ms: 1.08x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 19.5 us: 1.13x slower                                                       |
| pickle_list              | 2.75 us                                                     | 3.20 us: 1.16x slower                                                       |
| pickle                   | 6.85 us                                                     | 8.07 us: 1.18x slower                                                       |
| python_startup           | 20.6 ms                                                     | 25.8 ms: 1.25x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 19.4 ms: 1.25x slower                                                       |
| coverage                 | 39.0 ms                                                     | 49.9 ms: 1.28x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 90.9 ms: 1.46x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.10 ms: 1.49x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.31 ms: 1.64x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.26x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_generate
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20251101-3.15.0a1+-2f60b8f/bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.287x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: unknown