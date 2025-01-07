# Results vs. 3.10.4

- fork: kumaraditya303
- ref: fast_state
- machine: windows-amd64
- commit hash: 7de6e22
- commit date: 2025-01-07
- overall geometric mean: 1.192x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1-amd64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 225 ms: 1.09x faster                                                      |
| docutils       | 1.92 sec                                                    | 1.66 sec: 1.15x faster                                                    |
| html5lib       | 51.0 ms                                                     | 39.7 ms: 1.28x faster                                                     |
| Geometric mean | (ref)                                                       | 1.17x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1-amd64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|-------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 403 ms: 2.75x faster                                                      |
| async_tree_memoization  | 526 ms                                                      | 218 ms: 2.41x faster                                                      |
| async_tree_none         | 435 ms                                                      | 182 ms: 2.39x faster                                                      |
| async_tree_cpu_io_mixed | 638 ms                                                      | 347 ms: 1.84x faster                                                      |
| Geometric mean          | (ref)                                                       | 2.32x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1-amd64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 52.6 ms: 1.17x faster                                                     |
| pidigits       | 149 ms                                                      | 146 ms: 1.02x faster                                                      |
| nbody          | 71.3 ms                                                     | 77.8 ms: 1.09x slower                                                     |
| Geometric mean | (ref)                                                       | 1.03x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1-amd64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 88.0 ms: 1.20x faster                                                     |
| regex_dna      | 136 ms                                                      | 113 ms: 1.20x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.42 ms: 1.17x faster                                                     |
| regex_v8       | 15.4 ms                                                     | 20.1 ms: 1.30x slower                                                     |
| Geometric mean | (ref)                                                       | 1.07x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1-amd64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.76 ms: 1.36x faster                                                     |
| unpickle_pure_python | 183 us                                                      | 148 us: 1.24x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 225 us: 1.20x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.43 sec: 1.17x faster                                                    |
| xml_etree_parse      | 96.8 ms                                                     | 87.9 ms: 1.10x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 41.2 ms: 1.08x faster                                                     |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.8 ms: 1.04x faster                                                     |
| json_loads           | 14.0 us                                                     | 14.6 us: 1.04x slower                                                     |
| xml_etree_generate   | 55.5 ms                                                     | 58.0 ms: 1.04x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.12x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1-amd64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 18.0 ms: 1.16x slower                                                     |
| python_startup         | 20.6 ms                                                     | 24.1 ms: 1.17x slower                                                     |
| Geometric mean         | (ref)                                                       | 1.17x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1-amd64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.80 ms: 1.33x faster                                                     |
| genshi_text     | 19.8 ms                                                     | 16.8 ms: 1.18x faster                                                     |
| genshi_xml      | 41.0 ms                                                     | 35.1 ms: 1.17x faster                                                     |
| django_template | 28.9 ms                                                     | 25.6 ms: 1.13x faster                                                     |
| Geometric mean  | (ref)                                                       | 1.20x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1-amd64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|--------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 113 us: 2.98x faster                                                      |
| async_tree_io            | 1.11 sec                                                    | 403 ms: 2.75x faster                                                      |
| async_tree_memoization   | 526 ms                                                      | 218 ms: 2.41x faster                                                      |
| async_tree_none          | 435 ms                                                      | 182 ms: 2.39x faster                                                      |
| deltablue                | 4.19 ms                                                     | 2.26 ms: 1.86x faster                                                     |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 347 ms: 1.84x faster                                                      |
| pylint                   | 350 ms                                                      | 199 ms: 1.76x faster                                                      |
| go                       | 139 ms                                                      | 87.2 ms: 1.59x faster                                                     |
| generators               | 32.4 ms                                                     | 21.1 ms: 1.53x faster                                                     |
| logging_silent           | 94.6 ns                                                     | 62.3 ns: 1.52x faster                                                     |
| richards_super           | 52.2 ms                                                     | 34.8 ms: 1.50x faster                                                     |
| raytrace                 | 273 ms                                                      | 188 ms: 1.45x faster                                                      |
| chaos                    | 61.7 ms                                                     | 43.5 ms: 1.42x faster                                                     |
| scimark_lu               | 85.8 ms                                                     | 60.9 ms: 1.41x faster                                                     |
| richards                 | 42.4 ms                                                     | 30.5 ms: 1.39x faster                                                     |
| deepcopy_memo            | 28.8 us                                                     | 20.9 us: 1.38x faster                                                     |
| sqlglot_parse            | 1.22 ms                                                     | 887 us: 1.37x faster                                                      |
| deepcopy                 | 255 us                                                      | 187 us: 1.36x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.76 ms: 1.36x faster                                                     |
| comprehensions           | 16.5 us                                                     | 12.3 us: 1.34x faster                                                     |
| sqlglot_transpile        | 1.48 ms                                                     | 1.11 ms: 1.33x faster                                                     |
| mako                     | 9.03 ms                                                     | 6.80 ms: 1.33x faster                                                     |
| hexiom                   | 5.74 ms                                                     | 4.45 ms: 1.29x faster                                                     |
| html5lib                 | 51.0 ms                                                     | 39.7 ms: 1.28x faster                                                     |
| pyflate                  | 409 ms                                                      | 320 ms: 1.28x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 49.1 ms: 1.27x faster                                                     |
| pycparser                | 930 ms                                                      | 750 ms: 1.24x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 148 us: 1.24x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 41.8 ms: 1.21x faster                                                     |
| regex_compile            | 106 ms                                                      | 88.0 ms: 1.20x faster                                                     |
| regex_dna                | 136 ms                                                      | 113 ms: 1.20x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 225 us: 1.20x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.61 us: 1.19x faster                                                     |
| genshi_text              | 19.8 ms                                                     | 16.8 ms: 1.18x faster                                                     |
| sympy_sum                | 107 ms                                                      | 90.7 ms: 1.18x faster                                                     |
| coroutines               | 16.0 ms                                                     | 13.6 ms: 1.18x faster                                                     |
| float                    | 61.7 ms                                                     | 52.6 ms: 1.17x faster                                                     |
| scimark_monte_carlo      | 57.3 ms                                                     | 48.8 ms: 1.17x faster                                                     |
| regex_effbot             | 1.66 ms                                                     | 1.42 ms: 1.17x faster                                                     |
| tomli_loads              | 1.67 sec                                                    | 1.43 sec: 1.17x faster                                                    |
| mdp                      | 1.78 sec                                                    | 1.52 sec: 1.17x faster                                                    |
| bench_thread_pool        | 958 us                                                      | 820 us: 1.17x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 35.1 ms: 1.17x faster                                                     |
| scimark_sor              | 106 ms                                                      | 91.1 ms: 1.17x faster                                                     |
| spectral_norm            | 77.3 ms                                                     | 66.4 ms: 1.16x faster                                                     |
| thrift                   | 617 us                                                      | 531 us: 1.16x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.91 us: 1.16x faster                                                     |
| docutils                 | 1.92 sec                                                    | 1.66 sec: 1.15x faster                                                    |
| sympy_integrate          | 15.3 ms                                                     | 13.5 ms: 1.13x faster                                                     |
| django_template          | 28.9 ms                                                     | 25.6 ms: 1.13x faster                                                     |
| sqlglot_optimize         | 39.8 ms                                                     | 36.1 ms: 1.10x faster                                                     |
| xml_etree_parse          | 96.8 ms                                                     | 87.9 ms: 1.10x faster                                                     |
| pprint_pformat           | 1.22 sec                                                    | 1.11 sec: 1.10x faster                                                    |
| 2to3                     | 246 ms                                                      | 225 ms: 1.09x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 543 ms: 1.09x faster                                                      |
| sympy_str                | 194 ms                                                      | 179 ms: 1.09x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 41.2 ms: 1.08x faster                                                     |
| json                     | 3.14 ms                                                     | 2.97 ms: 1.06x faster                                                     |
| sqlglot_normalize        | 205 ms                                                      | 197 ms: 1.04x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.8 ms: 1.04x faster                                                     |
| nqueens                  | 66.6 ms                                                     | 64.4 ms: 1.03x faster                                                     |
| sympy_expand             | 314 ms                                                      | 306 ms: 1.03x faster                                                      |
| pidigits                 | 149 ms                                                      | 146 ms: 1.02x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.68 ms: 1.02x faster                                                     |
| logging_format           | 6.76 us                                                     | 6.84 us: 1.01x slower                                                     |
| logging_simple           | 6.22 us                                                     | 6.32 us: 1.02x slower                                                     |
| meteor_contest           | 75.9 ms                                                     | 77.7 ms: 1.02x slower                                                     |
| json_loads               | 14.0 us                                                     | 14.6 us: 1.04x slower                                                     |
| xml_etree_generate       | 55.5 ms                                                     | 58.0 ms: 1.04x slower                                                     |
| scimark_fft              | 187 ms                                                      | 196 ms: 1.05x slower                                                      |
| fannkuch                 | 256 ms                                                      | 276 ms: 1.08x slower                                                      |
| async_generators         | 222 ms                                                      | 241 ms: 1.09x slower                                                      |
| nbody                    | 71.3 ms                                                     | 77.8 ms: 1.09x slower                                                     |
| mypy2                    | 555 ms                                                      | 640 ms: 1.15x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 18.0 ms: 1.16x slower                                                     |
| python_startup           | 20.6 ms                                                     | 24.1 ms: 1.17x slower                                                     |
| coverage                 | 39.0 ms                                                     | 46.7 ms: 1.20x slower                                                     |
| telco                    | 3.94 ms                                                     | 4.82 ms: 1.22x slower                                                     |
| regex_v8                 | 15.4 ms                                                     | 20.1 ms: 1.30x slower                                                     |
| bench_mp_pool            | 62.0 ms                                                     | 82.3 ms: 1.33x slower                                                     |
| gc_traversal             | 1.41 ms                                                     | 1.96 ms: 1.39x slower                                                     |
| create_gc_cycles         | 800 us                                                      | 1.21 ms: 1.51x slower                                                     |
| Geometric mean           | (ref)                                                       | 1.19x faster                                                              |

Benchmark hidden because not significant (1): pathlib
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250107-3.14.0a3+-7de6e22/bm-20250107-pythonperf1-amd64-kumaraditya303-fast_state-3.14.0a3+-7de6e22.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.192x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown