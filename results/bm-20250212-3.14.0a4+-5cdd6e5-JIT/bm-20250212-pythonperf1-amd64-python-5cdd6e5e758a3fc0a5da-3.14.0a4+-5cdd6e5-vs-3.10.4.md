# Results vs. 3.10.4

- fork: python
- ref: 5cdd6e5e758a3fc0a5da
- machine: windows-amd64
- commit hash: 5cdd6e5
- commit date: 2025-02-12
- overall geometric mean: 1.247x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-pythonperf1-amd64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 221 ms: 1.11x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.76 sec: 1.09x faster                                                      |
| html5lib       | 51.0 ms                                                     | 38.3 ms: 1.33x faster                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-pythonperf1-amd64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 417 ms: 2.66x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 224 ms: 2.35x faster                                                        |
| async_tree_none         | 435 ms                                                      | 187 ms: 2.33x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 344 ms: 1.85x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.28x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-pythonperf1-amd64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 48.4 ms: 1.27x faster                                                       |
| nbody          | 71.3 ms                                                     | 60.4 ms: 1.18x faster                                                       |
| pidigits       | 149 ms                                                      | 150 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-pythonperf1-amd64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 80.8 ms: 1.31x faster                                                       |
| regex_dna      | 136 ms                                                      | 116 ms: 1.18x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.43 ms: 1.16x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.7 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-pythonperf1-amd64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 112 us: 1.63x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.20 sec: 1.40x faster                                                      |
| json_dumps           | 9.16 ms                                                     | 6.76 ms: 1.36x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 213 us: 1.27x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 36.2 ms: 1.23x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 50.3 ms: 1.10x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 89.9 ms: 1.08x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 60.8 ms: 1.07x faster                                                       |
| json_loads           | 14.0 us                                                     | 16.0 us: 1.14x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.21x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-pythonperf1-amd64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.1 ms: 1.22x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 19.3 ms: 1.25x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.23x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-pythonperf1-amd64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.33 ms: 1.70x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 16.8 ms: 1.18x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 36.5 ms: 1.13x faster                                                       |
| django_template | 28.9 ms                                                     | 25.8 ms: 1.12x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.26x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-pythonperf1-amd64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 112 us: 3.00x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 417 ms: 2.66x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 29.5 ms: 2.57x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 224 ms: 2.35x faster                                                        |
| async_tree_none          | 435 ms                                                      | 187 ms: 2.33x faster                                                        |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 344 ms: 1.85x faster                                                        |
| pylint                   | 350 ms                                                      | 202 ms: 1.74x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.42 ms: 1.73x faster                                                       |
| mako                     | 9.03 ms                                                     | 5.33 ms: 1.70x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 112 us: 1.63x faster                                                        |
| go                       | 139 ms                                                      | 87.1 ms: 1.59x faster                                                       |
| generators               | 32.4 ms                                                     | 20.7 ms: 1.57x faster                                                       |
| chaos                    | 61.7 ms                                                     | 42.1 ms: 1.46x faster                                                       |
| pyflate                  | 409 ms                                                      | 282 ms: 1.45x faster                                                        |
| richards_super           | 52.2 ms                                                     | 36.2 ms: 1.44x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 844 us: 1.44x faster                                                        |
| logging_silent           | 94.6 ns                                                     | 65.8 ns: 1.44x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.6 us: 1.42x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.20 sec: 1.40x faster                                                      |
| sqlglot_transpile        | 1.48 ms                                                     | 1.08 ms: 1.37x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 21.1 us: 1.36x faster                                                       |
| deepcopy                 | 255 us                                                      | 188 us: 1.36x faster                                                        |
| json_dumps               | 9.16 ms                                                     | 6.76 ms: 1.36x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 46.3 ms: 1.35x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 64.2 ms: 1.34x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 38.3 ms: 1.33x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.05 ms: 1.33x faster                                                       |
| richards                 | 42.4 ms                                                     | 32.1 ms: 1.32x faster                                                       |
| raytrace                 | 273 ms                                                      | 208 ms: 1.32x faster                                                        |
| pycparser                | 930 ms                                                      | 707 ms: 1.32x faster                                                        |
| regex_compile            | 106 ms                                                      | 80.8 ms: 1.31x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 38.8 ms: 1.30x faster                                                       |
| scimark_fft              | 187 ms                                                      | 147 ms: 1.28x faster                                                        |
| float                    | 61.7 ms                                                     | 48.4 ms: 1.27x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 213 us: 1.27x faster                                                        |
| scimark_monte_carlo      | 57.3 ms                                                     | 45.6 ms: 1.26x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.58 ms: 1.25x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 62.0 ms: 1.25x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.54 us: 1.24x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 36.2 ms: 1.23x faster                                                       |
| thrift                   | 617 us                                                      | 503 us: 1.23x faster                                                        |
| pprint_pformat           | 1.22 sec                                                    | 996 ms: 1.22x faster                                                        |
| scimark_sor              | 106 ms                                                      | 88.9 ms: 1.19x faster                                                       |
| sympy_sum                | 107 ms                                                      | 89.7 ms: 1.19x faster                                                       |
| nbody                    | 71.3 ms                                                     | 60.4 ms: 1.18x faster                                                       |
| regex_dna                | 136 ms                                                      | 116 ms: 1.18x faster                                                        |
| genshi_text              | 19.8 ms                                                     | 16.8 ms: 1.18x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.43 ms: 1.16x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 511 ms: 1.16x faster                                                        |
| genshi_xml               | 41.0 ms                                                     | 36.5 ms: 1.13x faster                                                       |
| django_template          | 28.9 ms                                                     | 25.8 ms: 1.12x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 858 us: 1.12x faster                                                        |
| deepcopy_reduce          | 2.20 us                                                     | 1.98 us: 1.12x faster                                                       |
| 2to3                     | 246 ms                                                      | 221 ms: 1.11x faster                                                        |
| sympy_str                | 194 ms                                                      | 175 ms: 1.11x faster                                                        |
| coroutines               | 16.0 ms                                                     | 14.4 ms: 1.11x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.8 ms: 1.10x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 50.3 ms: 1.10x faster                                                       |
| fannkuch                 | 256 ms                                                      | 232 ms: 1.10x faster                                                        |
| docutils                 | 1.92 sec                                                    | 1.76 sec: 1.09x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 89.9 ms: 1.08x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 37.1 ms: 1.07x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 60.8 ms: 1.07x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.67 sec: 1.07x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 14.7 ms: 1.05x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 63.5 ms: 1.05x faster                                                       |
| sympy_expand             | 314 ms                                                      | 301 ms: 1.05x faster                                                        |
| sqlglot_normalize        | 205 ms                                                      | 203 ms: 1.01x faster                                                        |
| pidigits                 | 149 ms                                                      | 150 ms: 1.01x slower                                                        |
| json                     | 3.14 ms                                                     | 3.17 ms: 1.01x slower                                                       |
| logging_format           | 6.76 us                                                     | 7.01 us: 1.04x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.58 us: 1.06x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.32 ms: 1.10x slower                                                       |
| async_generators         | 222 ms                                                      | 246 ms: 1.11x slower                                                        |
| json_loads               | 14.0 us                                                     | 16.0 us: 1.14x slower                                                       |
| python_startup           | 20.6 ms                                                     | 25.1 ms: 1.22x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 19.3 ms: 1.25x slower                                                       |
| coverage                 | 39.0 ms                                                     | 50.0 ms: 1.28x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 84.3 ms: 1.36x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.99 ms: 1.41x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.22 ms: 1.53x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.24x faster                                                                |

Benchmark hidden because not significant (1): meteor_contest
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250212-3.14.0a4+-5cdd6e5-JIT/bm-20250212-pythonperf1-amd64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.247x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown