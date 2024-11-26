# Results vs. 3.10.4

- fork: python
- ref: ed81971e6b26c34445f0
- machine: windows-amd64
- commit hash: ed81971
- commit date: 2024-11-16
- overall geometric mean: 1.213x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 244 ms: 1.01x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.89 sec: 1.02x faster                                                      |
| html5lib       | 51.0 ms                                                     | 38.7 ms: 1.32x faster                                                       |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 208 ms: 2.10x faster                                                        |
| async_tree_io           | 1.11 sec                                                    | 546 ms: 2.03x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 263 ms: 2.00x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 391 ms: 1.63x faster                                                        |
| Geometric mean          | (ref)                                                       | 1.93x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 47.4 ms: 1.30x faster                                                       |
| nbody          | 71.3 ms                                                     | 55.9 ms: 1.28x faster                                                       |
| pidigits       | 149 ms                                                      | 147 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                       | 1.19x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 90.3 ms: 1.17x faster                                                       |
| regex_dna      | 136 ms                                                      | 117 ms: 1.16x faster                                                        |
| regex_v8       | 15.4 ms                                                     | 14.4 ms: 1.07x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.25 ms: 1.47x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.25 sec: 1.34x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 205 us: 1.31x faster                                                        |
| unpickle_pure_python | 183 us                                                      | 141 us: 1.30x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 35.7 ms: 1.25x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 50.7 ms: 1.09x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.1 ms: 1.05x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 92.6 ms: 1.05x faster                                                       |
| json_loads           | 14.0 us                                                     | 14.2 us: 1.01x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.19x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 23.3 ms: 1.13x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 17.6 ms: 1.14x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.12 ms: 1.76x faster                                                       |
| django_template | 28.9 ms                                                     | 26.8 ms: 1.08x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 47.2 ms: 1.15x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.14x faster                                                                |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 116 us: 2.89x faster                                                        |
| async_tree_none          | 435 ms                                                      | 208 ms: 2.10x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 546 ms: 2.03x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 263 ms: 2.00x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.33 ms: 1.80x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 16.1 us: 1.79x faster                                                       |
| mako                     | 9.03 ms                                                     | 5.12 ms: 1.76x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 55.0 ns: 1.72x faster                                                       |
| scimark_sor              | 106 ms                                                      | 63.3 ms: 1.68x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 52.3 ms: 1.64x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 391 ms: 1.63x faster                                                        |
| crypto_pyaes             | 62.5 ms                                                     | 39.9 ms: 1.57x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 37.1 ms: 1.54x faster                                                       |
| go                       | 139 ms                                                      | 90.2 ms: 1.54x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 51.6 ms: 1.50x faster                                                       |
| chaos                    | 61.7 ms                                                     | 41.3 ms: 1.50x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.25 ms: 1.47x faster                                                       |
| generators               | 32.4 ms                                                     | 22.8 ms: 1.42x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.9 us: 1.39x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 880 us: 1.38x faster                                                        |
| deepcopy                 | 255 us                                                      | 187 us: 1.37x faster                                                        |
| richards_super           | 52.2 ms                                                     | 38.5 ms: 1.36x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.25 sec: 1.34x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 38.7 ms: 1.32x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 205 us: 1.31x faster                                                        |
| pycparser                | 930 ms                                                      | 714 ms: 1.30x faster                                                        |
| unpickle_pure_python     | 183 us                                                      | 141 us: 1.30x faster                                                        |
| float                    | 61.7 ms                                                     | 47.4 ms: 1.30x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 942 ms: 1.29x faster                                                        |
| pprint_safe_repr         | 592 ms                                                      | 461 ms: 1.28x faster                                                        |
| pylint                   | 350 ms                                                      | 274 ms: 1.28x faster                                                        |
| dulwich_log              | 50.5 ms                                                     | 39.5 ms: 1.28x faster                                                       |
| nbody                    | 71.3 ms                                                     | 55.9 ms: 1.28x faster                                                       |
| pyflate                  | 409 ms                                                      | 321 ms: 1.27x faster                                                        |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.14 ms: 1.27x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.16 ms: 1.27x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 35.7 ms: 1.25x faster                                                       |
| richards                 | 42.4 ms                                                     | 34.2 ms: 1.24x faster                                                       |
| raytrace                 | 273 ms                                                      | 221 ms: 1.24x faster                                                        |
| scimark_fft              | 187 ms                                                      | 155 ms: 1.21x faster                                                        |
| thrift                   | 617 us                                                      | 515 us: 1.20x faster                                                        |
| coroutines               | 16.0 ms                                                     | 13.4 ms: 1.19x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.61 us: 1.19x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.86 us: 1.19x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 811 us: 1.18x faster                                                        |
| regex_compile            | 106 ms                                                      | 90.3 ms: 1.17x faster                                                       |
| regex_dna                | 136 ms                                                      | 117 ms: 1.16x faster                                                        |
| hexiom                   | 5.74 ms                                                     | 5.18 ms: 1.11x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 50.7 ms: 1.09x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.63 sec: 1.09x faster                                                      |
| django_template          | 28.9 ms                                                     | 26.8 ms: 1.08x faster                                                       |
| json                     | 3.14 ms                                                     | 2.92 ms: 1.08x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 14.4 ms: 1.07x faster                                                       |
| sympy_sum                | 107 ms                                                      | 101 ms: 1.06x faster                                                        |
| fannkuch                 | 256 ms                                                      | 241 ms: 1.06x faster                                                        |
| meteor_contest           | 75.9 ms                                                     | 72.0 ms: 1.05x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.1 ms: 1.05x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 92.6 ms: 1.05x faster                                                       |
| sympy_str                | 194 ms                                                      | 188 ms: 1.04x faster                                                        |
| logging_format           | 6.76 us                                                     | 6.54 us: 1.03x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 65.3 ms: 1.02x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.89 sec: 1.02x faster                                                      |
| pidigits                 | 149 ms                                                      | 147 ms: 1.02x faster                                                        |
| logging_simple           | 6.22 us                                                     | 6.14 us: 1.01x faster                                                       |
| 2to3                     | 246 ms                                                      | 244 ms: 1.01x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 75.0 ms: 1.01x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 15.4 ms: 1.01x slower                                                       |
| sympy_expand             | 314 ms                                                      | 318 ms: 1.01x slower                                                        |
| json_loads               | 14.0 us                                                     | 14.2 us: 1.01x slower                                                       |
| sqlglot_normalize        | 205 ms                                                      | 208 ms: 1.01x slower                                                        |
| sqlglot_optimize         | 39.8 ms                                                     | 42.9 ms: 1.08x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.32 ms: 1.10x slower                                                       |
| python_startup           | 20.6 ms                                                     | 23.3 ms: 1.13x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 17.6 ms: 1.14x slower                                                       |
| genshi_xml               | 41.0 ms                                                     | 47.2 ms: 1.15x slower                                                       |
| async_generators         | 222 ms                                                      | 263 ms: 1.19x slower                                                        |
| coverage                 | 39.0 ms                                                     | 47.2 ms: 1.21x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.91 ms: 1.35x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 87.0 ms: 1.40x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.39 ms: 1.74x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.21x faster                                                                |

Benchmark hidden because not significant (1): genshi_text
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241116-3.14.0a1+-ed81971-JIT/bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.213x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown