# Results vs. 3.10.4

- fork: python
- ref: 09d6f5dc7824c74672ad
- machine: windows-amd64
- commit hash: 09d6f5d
- commit date: 2024-11-07
- overall geometric mean: 1.212x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241107-pythonperf1-amd64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 243 ms: 1.01x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.89 sec: 1.01x faster                                                      |
| html5lib       | 51.0 ms                                                     | 39.4 ms: 1.29x faster                                                       |
| Geometric mean | (ref)                                                       | 1.10x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241107-pythonperf1-amd64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 517 ms: 2.15x faster                                                        |
| async_tree_none         | 435 ms                                                      | 204 ms: 2.14x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 253 ms: 2.08x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 395 ms: 1.61x faster                                                        |
| Geometric mean          | (ref)                                                       | 1.98x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241107-pythonperf1-amd64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 47.1 ms: 1.31x faster                                                       |
| nbody          | 71.3 ms                                                     | 56.3 ms: 1.27x faster                                                       |
| pidigits       | 149 ms                                                      | 147 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                       | 1.19x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241107-pythonperf1-amd64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 116 ms: 1.18x faster                                                        |
| regex_compile  | 106 ms                                                      | 91.2 ms: 1.16x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.5 ms: 1.07x faster                                                       |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241107-pythonperf1-amd64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.12 ms: 1.50x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.28 sec: 1.31x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 207 us: 1.30x faster                                                        |
| unpickle_pure_python | 183 us                                                      | 144 us: 1.27x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 35.6 ms: 1.25x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 50.5 ms: 1.10x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.0 ms: 1.05x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 92.8 ms: 1.04x faster                                                       |
| json_loads           | 14.0 us                                                     | 14.2 us: 1.01x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.19x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241107-pythonperf1-amd64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 17.6 ms: 1.14x slower                                                       |
| python_startup         | 20.6 ms                                                     | 23.5 ms: 1.14x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241107-pythonperf1-amd64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.06 ms: 1.78x faster                                                       |
| django_template | 28.9 ms                                                     | 27.3 ms: 1.06x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 46.8 ms: 1.14x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.14x faster                                                                |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241107-pythonperf1-amd64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 113 us: 2.98x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 517 ms: 2.15x faster                                                        |
| async_tree_none          | 435 ms                                                      | 204 ms: 2.14x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 253 ms: 2.08x faster                                                        |
| mako                     | 9.03 ms                                                     | 5.06 ms: 1.78x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.35 ms: 1.78x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 55.0 ns: 1.72x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 16.7 us: 1.72x faster                                                       |
| scimark_sor              | 106 ms                                                      | 63.3 ms: 1.68x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 51.8 ms: 1.66x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 395 ms: 1.61x faster                                                        |
| crypto_pyaes             | 62.5 ms                                                     | 40.3 ms: 1.55x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 37.0 ms: 1.55x faster                                                       |
| go                       | 139 ms                                                      | 91.2 ms: 1.52x faster                                                       |
| chaos                    | 61.7 ms                                                     | 40.9 ms: 1.51x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.12 ms: 1.50x faster                                                       |
| generators               | 32.4 ms                                                     | 22.5 ms: 1.44x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 54.1 ms: 1.43x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.8 us: 1.40x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 888 us: 1.37x faster                                                        |
| richards_super           | 52.2 ms                                                     | 38.6 ms: 1.35x faster                                                       |
| pyflate                  | 409 ms                                                      | 303 ms: 1.35x faster                                                        |
| deepcopy                 | 255 us                                                      | 191 us: 1.33x faster                                                        |
| pprint_pformat           | 1.22 sec                                                    | 922 ms: 1.32x faster                                                        |
| tomli_loads              | 1.67 sec                                                    | 1.28 sec: 1.31x faster                                                      |
| float                    | 61.7 ms                                                     | 47.1 ms: 1.31x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 207 us: 1.30x faster                                                        |
| pprint_safe_repr         | 592 ms                                                      | 455 ms: 1.30x faster                                                        |
| html5lib                 | 51.0 ms                                                     | 39.4 ms: 1.29x faster                                                       |
| pycparser                | 930 ms                                                      | 720 ms: 1.29x faster                                                        |
| raytrace                 | 273 ms                                                      | 214 ms: 1.28x faster                                                        |
| pylint                   | 350 ms                                                      | 275 ms: 1.28x faster                                                        |
| unpickle_pure_python     | 183 us                                                      | 144 us: 1.27x faster                                                        |
| dulwich_log              | 50.5 ms                                                     | 39.6 ms: 1.27x faster                                                       |
| nbody                    | 71.3 ms                                                     | 56.3 ms: 1.27x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.18 ms: 1.25x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 35.6 ms: 1.25x faster                                                       |
| richards                 | 42.4 ms                                                     | 34.5 ms: 1.23x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.25 ms: 1.21x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.59 us: 1.21x faster                                                       |
| scimark_fft              | 187 ms                                                      | 157 ms: 1.19x faster                                                        |
| coroutines               | 16.0 ms                                                     | 13.4 ms: 1.19x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.87 us: 1.18x faster                                                       |
| regex_dna                | 136 ms                                                      | 116 ms: 1.18x faster                                                        |
| bench_thread_pool        | 958 us                                                      | 819 us: 1.17x faster                                                        |
| thrift                   | 617 us                                                      | 530 us: 1.17x faster                                                        |
| regex_compile            | 106 ms                                                      | 91.2 ms: 1.16x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.54 sec: 1.16x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 5.20 ms: 1.10x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 50.5 ms: 1.10x faster                                                       |
| json                     | 3.14 ms                                                     | 2.93 ms: 1.07x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 14.5 ms: 1.07x faster                                                       |
| django_template          | 28.9 ms                                                     | 27.3 ms: 1.06x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 63.2 ms: 1.05x faster                                                       |
| sympy_sum                | 107 ms                                                      | 102 ms: 1.05x faster                                                        |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.0 ms: 1.05x faster                                                       |
| fannkuch                 | 256 ms                                                      | 244 ms: 1.05x faster                                                        |
| xml_etree_parse          | 96.8 ms                                                     | 92.8 ms: 1.04x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.52 us: 1.04x faster                                                       |
| sympy_str                | 194 ms                                                      | 190 ms: 1.02x faster                                                        |
| logging_simple           | 6.22 us                                                     | 6.11 us: 1.02x faster                                                       |
| pidigits                 | 149 ms                                                      | 147 ms: 1.02x faster                                                        |
| docutils                 | 1.92 sec                                                    | 1.89 sec: 1.01x faster                                                      |
| 2to3                     | 246 ms                                                      | 243 ms: 1.01x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 75.2 ms: 1.01x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 207 ms: 1.01x slower                                                        |
| json_loads               | 14.0 us                                                     | 14.2 us: 1.01x slower                                                       |
| sympy_integrate          | 15.3 ms                                                     | 15.7 ms: 1.03x slower                                                       |
| sympy_expand             | 314 ms                                                      | 323 ms: 1.03x slower                                                        |
| sqlglot_optimize         | 39.8 ms                                                     | 42.5 ms: 1.07x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.46 ms: 1.13x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 17.6 ms: 1.14x slower                                                       |
| genshi_xml               | 41.0 ms                                                     | 46.8 ms: 1.14x slower                                                       |
| python_startup           | 20.6 ms                                                     | 23.5 ms: 1.14x slower                                                       |
| coverage                 | 39.0 ms                                                     | 46.1 ms: 1.18x slower                                                       |
| async_generators         | 222 ms                                                      | 267 ms: 1.21x slower                                                        |
| gc_traversal             | 1.41 ms                                                     | 1.92 ms: 1.36x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 87.1 ms: 1.40x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.37 ms: 1.72x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.21x faster                                                                |

Benchmark hidden because not significant (2): genshi_text, meteor_contest
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241107-3.14.0a1+-09d6f5d-JIT/bm-20241107-pythonperf1-amd64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.212x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown