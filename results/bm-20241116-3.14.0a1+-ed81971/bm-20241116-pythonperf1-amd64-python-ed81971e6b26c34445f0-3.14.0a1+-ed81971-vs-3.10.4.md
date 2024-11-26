# Results vs. 3.10.4

- fork: python
- ref: ed81971e6b26c34445f0
- machine: windows-amd64
- commit hash: ed81971
- commit date: 2024-11-16
- overall geometric mean: 1.161x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 224 ms: 1.10x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.71 sec: 1.13x faster                                                      |
| html5lib       | 51.0 ms                                                     | 40.2 ms: 1.27x faster                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 558 ms: 1.99x faster                                                        |
| async_tree_none         | 435 ms                                                      | 221 ms: 1.97x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 277 ms: 1.90x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 385 ms: 1.66x faster                                                        |
| Geometric mean          | (ref)                                                       | 1.87x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 56.4 ms: 1.09x faster                                                       |
| pidigits       | 149 ms                                                      | 145 ms: 1.03x faster                                                        |
| nbody          | 71.3 ms                                                     | 82.8 ms: 1.16x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 91.2 ms: 1.16x faster                                                       |
| regex_dna      | 136 ms                                                      | 124 ms: 1.10x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.56 ms: 1.07x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 15.2 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.66 ms: 1.38x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 227 us: 1.19x faster                                                        |
| unpickle_pure_python | 183 us                                                      | 155 us: 1.18x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 41.2 ms: 1.08x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.58 sec: 1.06x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 65.9 ms: 1.01x slower                                                       |
| json_loads           | 14.0 us                                                     | 14.4 us: 1.03x slower                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 59.2 ms: 1.07x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.08x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 17.9 ms: 1.15x slower                                                       |
| python_startup         | 20.6 ms                                                     | 24.0 ms: 1.17x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.16x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.95 ms: 1.30x faster                                                       |
| django_template | 28.9 ms                                                     | 25.4 ms: 1.14x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 17.4 ms: 1.14x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 37.2 ms: 1.10x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.17x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 112 us: 2.99x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 558 ms: 1.99x faster                                                        |
| async_tree_none          | 435 ms                                                      | 221 ms: 1.97x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 277 ms: 1.90x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.29 ms: 1.83x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 385 ms: 1.66x faster                                                        |
| pylint                   | 350 ms                                                      | 224 ms: 1.57x faster                                                        |
| go                       | 139 ms                                                      | 90.2 ms: 1.54x faster                                                       |
| generators               | 32.4 ms                                                     | 21.9 ms: 1.48x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 65.5 ns: 1.44x faster                                                       |
| richards_super           | 52.2 ms                                                     | 36.4 ms: 1.43x faster                                                       |
| chaos                    | 61.7 ms                                                     | 43.4 ms: 1.42x faster                                                       |
| raytrace                 | 273 ms                                                      | 197 ms: 1.38x faster                                                        |
| json_dumps               | 9.16 ms                                                     | 6.66 ms: 1.38x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 21.3 us: 1.35x faster                                                       |
| comprehensions           | 16.5 us                                                     | 12.4 us: 1.33x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 64.9 ms: 1.32x faster                                                       |
| deepcopy                 | 255 us                                                      | 194 us: 1.32x faster                                                        |
| richards                 | 42.4 ms                                                     | 32.5 ms: 1.31x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 933 us: 1.30x faster                                                        |
| crypto_pyaes             | 62.5 ms                                                     | 48.1 ms: 1.30x faster                                                       |
| mako                     | 9.03 ms                                                     | 6.95 ms: 1.30x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.15 ms: 1.29x faster                                                       |
| pyflate                  | 409 ms                                                      | 321 ms: 1.27x faster                                                        |
| hexiom                   | 5.74 ms                                                     | 4.51 ms: 1.27x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 40.2 ms: 1.27x faster                                                       |
| pycparser                | 930 ms                                                      | 741 ms: 1.26x faster                                                        |
| scimark_monte_carlo      | 57.3 ms                                                     | 47.7 ms: 1.20x faster                                                       |
| sympy_sum                | 107 ms                                                      | 89.7 ms: 1.19x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 227 us: 1.19x faster                                                        |
| mdp                      | 1.78 sec                                                    | 1.50 sec: 1.18x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 155 us: 1.18x faster                                                        |
| dulwich_log              | 50.5 ms                                                     | 42.9 ms: 1.18x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 816 us: 1.17x faster                                                        |
| sqlite_synth             | 1.91 us                                                     | 1.63 us: 1.17x faster                                                       |
| thrift                   | 617 us                                                      | 528 us: 1.17x faster                                                        |
| coroutines               | 16.0 ms                                                     | 13.7 ms: 1.16x faster                                                       |
| scimark_sor              | 106 ms                                                      | 91.2 ms: 1.16x faster                                                       |
| regex_compile            | 106 ms                                                      | 91.2 ms: 1.16x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 67.8 ms: 1.14x faster                                                       |
| django_template          | 28.9 ms                                                     | 25.4 ms: 1.14x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 17.4 ms: 1.14x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.5 ms: 1.13x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.71 sec: 1.13x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.98 us: 1.11x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 37.2 ms: 1.10x faster                                                       |
| regex_dna                | 136 ms                                                      | 124 ms: 1.10x faster                                                        |
| 2to3                     | 246 ms                                                      | 224 ms: 1.10x faster                                                        |
| float                    | 61.7 ms                                                     | 56.4 ms: 1.09x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.12 sec: 1.09x faster                                                      |
| sympy_str                | 194 ms                                                      | 179 ms: 1.09x faster                                                        |
| xml_etree_process        | 44.5 ms                                                     | 41.2 ms: 1.08x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 37.1 ms: 1.07x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.56 ms: 1.07x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 558 ms: 1.06x faster                                                        |
| tomli_loads              | 1.67 sec                                                    | 1.58 sec: 1.06x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 63.3 ms: 1.05x faster                                                       |
| json                     | 3.14 ms                                                     | 3.03 ms: 1.04x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 200 ms: 1.03x faster                                                        |
| pidigits                 | 149 ms                                                      | 145 ms: 1.03x faster                                                        |
| sympy_expand             | 314 ms                                                      | 309 ms: 1.02x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 74.5 ms: 1.02x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 15.2 ms: 1.01x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.82 us: 1.01x slower                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 65.9 ms: 1.01x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.39 us: 1.03x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.4 us: 1.03x slower                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.81 ms: 1.03x slower                                                       |
| meteor_contest           | 75.9 ms                                                     | 79.3 ms: 1.04x slower                                                       |
| scimark_fft              | 187 ms                                                      | 200 ms: 1.07x slower                                                        |
| xml_etree_generate       | 55.5 ms                                                     | 59.2 ms: 1.07x slower                                                       |
| fannkuch                 | 256 ms                                                      | 278 ms: 1.09x slower                                                        |
| async_generators         | 222 ms                                                      | 245 ms: 1.11x slower                                                        |
| python_startup_no_site   | 15.5 ms                                                     | 17.9 ms: 1.15x slower                                                       |
| nbody                    | 71.3 ms                                                     | 82.8 ms: 1.16x slower                                                       |
| python_startup           | 20.6 ms                                                     | 24.0 ms: 1.17x slower                                                       |
| coverage                 | 39.0 ms                                                     | 46.3 ms: 1.19x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.81 ms: 1.22x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 82.0 ms: 1.32x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.91 ms: 1.35x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.38 ms: 1.73x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.16x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_parse
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241116-3.14.0a1+-ed81971/bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.161x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: unknown