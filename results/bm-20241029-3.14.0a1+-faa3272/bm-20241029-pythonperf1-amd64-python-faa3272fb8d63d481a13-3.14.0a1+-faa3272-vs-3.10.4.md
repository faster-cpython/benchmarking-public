# Results vs. 3.10.4

- fork: python
- ref: faa3272fb8d63d481a13
- machine: windows-amd64
- commit hash: faa3272
- commit date: 2024-10-29
- overall geometric mean: 1.178x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-pythonperf1-amd64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 224 ms: 1.10x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.71 sec: 1.12x faster                                                      |
| html5lib       | 51.0 ms                                                     | 40.1 ms: 1.27x faster                                                       |
| tornado_http   | 108 ms                                                      | 92.9 ms: 1.17x faster                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-pythonperf1-amd64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 559 ms: 1.98x faster                                                        |
| async_tree_none         | 435 ms                                                      | 220 ms: 1.98x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 279 ms: 1.89x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 383 ms: 1.66x faster                                                        |
| Geometric mean          | (ref)                                                       | 1.87x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-pythonperf1-amd64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 55.0 ms: 1.12x faster                                                       |
| pidigits       | 149 ms                                                      | 147 ms: 1.01x faster                                                        |
| nbody          | 71.3 ms                                                     | 76.9 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-pythonperf1-amd64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 90.6 ms: 1.17x faster                                                       |
| regex_dna      | 136 ms                                                      | 123 ms: 1.11x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 15.2 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-pythonperf1-amd64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.62 ms: 1.39x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 217 us: 1.25x faster                                                        |
| unpickle_pure_python | 183 us                                                      | 151 us: 1.22x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 40.2 ms: 1.11x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.58 sec: 1.06x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 65.7 ms: 1.01x slower                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 57.1 ms: 1.03x slower                                                       |
| json_loads           | 14.0 us                                                     | 14.7 us: 1.05x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.10x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-pythonperf1-amd64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 17.9 ms: 1.15x slower                                                       |
| python_startup         | 20.6 ms                                                     | 24.0 ms: 1.16x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.16x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-pythonperf1-amd64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.64 ms: 1.36x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 17.1 ms: 1.15x faster                                                       |
| django_template | 28.9 ms                                                     | 25.7 ms: 1.13x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 36.5 ms: 1.12x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.19x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-pythonperf1-amd64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 112 us: 2.99x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 559 ms: 1.98x faster                                                        |
| async_tree_none          | 435 ms                                                      | 220 ms: 1.98x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 279 ms: 1.89x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.31 ms: 1.82x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 383 ms: 1.66x faster                                                        |
| go                       | 139 ms                                                      | 86.7 ms: 1.60x faster                                                       |
| pylint                   | 350 ms                                                      | 224 ms: 1.56x faster                                                        |
| logging_silent           | 94.6 ns                                                     | 61.7 ns: 1.53x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 19.5 us: 1.47x faster                                                       |
| generators               | 32.4 ms                                                     | 22.0 ms: 1.47x faster                                                       |
| chaos                    | 61.7 ms                                                     | 43.3 ms: 1.43x faster                                                       |
| richards_super           | 52.2 ms                                                     | 36.6 ms: 1.43x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 61.3 ms: 1.40x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.8 us: 1.39x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.62 ms: 1.39x faster                                                       |
| raytrace                 | 273 ms                                                      | 198 ms: 1.38x faster                                                        |
| deepcopy                 | 255 us                                                      | 187 us: 1.36x faster                                                        |
| mako                     | 9.03 ms                                                     | 6.64 ms: 1.36x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 910 us: 1.34x faster                                                        |
| hexiom                   | 5.74 ms                                                     | 4.35 ms: 1.32x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.12 ms: 1.32x faster                                                       |
| richards                 | 42.4 ms                                                     | 32.3 ms: 1.32x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 47.9 ms: 1.31x faster                                                       |
| pyflate                  | 409 ms                                                      | 315 ms: 1.30x faster                                                        |
| pycparser                | 930 ms                                                      | 721 ms: 1.29x faster                                                        |
| html5lib                 | 51.0 ms                                                     | 40.1 ms: 1.27x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 217 us: 1.25x faster                                                        |
| mdp                      | 1.78 sec                                                    | 1.43 sec: 1.24x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 46.7 ms: 1.23x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 151 us: 1.22x faster                                                        |
| scimark_sor              | 106 ms                                                      | 88.0 ms: 1.21x faster                                                       |
| sympy_sum                | 107 ms                                                      | 89.2 ms: 1.20x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 64.7 ms: 1.19x faster                                                       |
| thrift                   | 617 us                                                      | 518 us: 1.19x faster                                                        |
| dulwich_log              | 50.5 ms                                                     | 42.5 ms: 1.19x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 811 us: 1.18x faster                                                        |
| coroutines               | 16.0 ms                                                     | 13.6 ms: 1.18x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.63 us: 1.18x faster                                                       |
| regex_compile            | 106 ms                                                      | 90.6 ms: 1.17x faster                                                       |
| tornado_http             | 108 ms                                                      | 92.9 ms: 1.17x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 17.1 ms: 1.15x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.3 ms: 1.15x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.94 us: 1.13x faster                                                       |
| django_template          | 28.9 ms                                                     | 25.7 ms: 1.13x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 36.5 ms: 1.12x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.71 sec: 1.12x faster                                                      |
| float                    | 61.7 ms                                                     | 55.0 ms: 1.12x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.09 sec: 1.12x faster                                                      |
| regex_dna                | 136 ms                                                      | 123 ms: 1.11x faster                                                        |
| xml_etree_process        | 44.5 ms                                                     | 40.2 ms: 1.11x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 535 ms: 1.11x faster                                                        |
| sympy_str                | 194 ms                                                      | 177 ms: 1.10x faster                                                        |
| 2to3                     | 246 ms                                                      | 224 ms: 1.10x faster                                                        |
| sqlglot_optimize         | 39.8 ms                                                     | 37.2 ms: 1.07x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 62.4 ms: 1.07x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.58 sec: 1.06x faster                                                      |
| sympy_expand             | 314 ms                                                      | 304 ms: 1.03x faster                                                        |
| sqlglot_normalize        | 205 ms                                                      | 199 ms: 1.03x faster                                                        |
| regex_v8                 | 15.4 ms                                                     | 15.2 ms: 1.02x faster                                                       |
| pidigits                 | 149 ms                                                      | 147 ms: 1.01x faster                                                        |
| logging_format           | 6.76 us                                                     | 6.82 us: 1.01x slower                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.75 ms: 1.01x slower                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 65.7 ms: 1.01x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.35 us: 1.02x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 57.1 ms: 1.03x slower                                                       |
| fannkuch                 | 256 ms                                                      | 265 ms: 1.03x slower                                                        |
| pathlib                  | 75.7 ms                                                     | 78.6 ms: 1.04x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.7 us: 1.05x slower                                                       |
| scimark_fft              | 187 ms                                                      | 196 ms: 1.05x slower                                                        |
| async_generators         | 222 ms                                                      | 238 ms: 1.07x slower                                                        |
| nbody                    | 71.3 ms                                                     | 76.9 ms: 1.08x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 17.9 ms: 1.15x slower                                                       |
| python_startup           | 20.6 ms                                                     | 24.0 ms: 1.16x slower                                                       |
| coverage                 | 39.0 ms                                                     | 45.8 ms: 1.17x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.91 ms: 1.25x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 83.1 ms: 1.34x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.91 ms: 1.36x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.37 ms: 1.72x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.17x faster                                                                |

Benchmark hidden because not significant (3): json, xml_etree_parse, meteor_contest
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (10) of results/bm-20241029-3.14.0a1+-faa3272/bm-20241029-pythonperf1-amd64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.178x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown