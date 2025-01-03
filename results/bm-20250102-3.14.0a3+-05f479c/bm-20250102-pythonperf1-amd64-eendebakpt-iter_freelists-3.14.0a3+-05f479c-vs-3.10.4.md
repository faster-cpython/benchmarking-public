# Results vs. 3.10.4

- fork: eendebakpt
- ref: iter_freelists
- machine: windows-amd64
- commit hash: 05f479c
- commit date: 2025-01-02
- overall geometric mean: 1.194x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-pythonperf1-amd64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 224 ms: 1.10x faster                                                      |
| docutils       | 1.92 sec                                                    | 1.65 sec: 1.16x faster                                                    |
| html5lib       | 51.0 ms                                                     | 39.3 ms: 1.30x faster                                                     |
| Geometric mean | (ref)                                                       | 1.18x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-pythonperf1-amd64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|-------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 403 ms: 2.75x faster                                                      |
| async_tree_memoization  | 526 ms                                                      | 221 ms: 2.38x faster                                                      |
| async_tree_none         | 435 ms                                                      | 184 ms: 2.36x faster                                                      |
| async_tree_cpu_io_mixed | 638 ms                                                      | 347 ms: 1.84x faster                                                      |
| Geometric mean          | (ref)                                                       | 2.31x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-pythonperf1-amd64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 52.7 ms: 1.17x faster                                                     |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                                      |
| nbody          | 71.3 ms                                                     | 77.4 ms: 1.09x slower                                                     |
| Geometric mean | (ref)                                                       | 1.03x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-pythonperf1-amd64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 86.5 ms: 1.23x faster                                                     |
| regex_dna      | 136 ms                                                      | 118 ms: 1.16x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.44 ms: 1.15x faster                                                     |
| regex_v8       | 15.4 ms                                                     | 20.8 ms: 1.35x slower                                                     |
| Geometric mean | (ref)                                                       | 1.05x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-pythonperf1-amd64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.73 ms: 1.36x faster                                                     |
| pickle_pure_python   | 270 us                                                      | 228 us: 1.18x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 157 us: 1.17x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.43 sec: 1.17x faster                                                    |
| xml_etree_process    | 44.5 ms                                                     | 40.0 ms: 1.11x faster                                                     |
| xml_etree_parse      | 96.8 ms                                                     | 88.8 ms: 1.09x faster                                                     |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.6 ms: 1.04x faster                                                     |
| xml_etree_generate   | 55.5 ms                                                     | 56.4 ms: 1.02x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.12x faster                                                              |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-pythonperf1-amd64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 17.4 ms: 1.12x slower                                                     |
| python_startup         | 20.6 ms                                                     | 23.4 ms: 1.14x slower                                                     |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-pythonperf1-amd64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.94 ms: 1.30x faster                                                     |
| genshi_text     | 19.8 ms                                                     | 15.7 ms: 1.26x faster                                                     |
| genshi_xml      | 41.0 ms                                                     | 34.4 ms: 1.19x faster                                                     |
| django_template | 28.9 ms                                                     | 24.4 ms: 1.18x faster                                                     |
| Geometric mean  | (ref)                                                       | 1.23x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-pythonperf1-amd64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|--------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 109 us: 3.07x faster                                                      |
| async_tree_io            | 1.11 sec                                                    | 403 ms: 2.75x faster                                                      |
| async_tree_memoization   | 526 ms                                                      | 221 ms: 2.38x faster                                                      |
| async_tree_none          | 435 ms                                                      | 184 ms: 2.36x faster                                                      |
| deltablue                | 4.19 ms                                                     | 2.22 ms: 1.89x faster                                                     |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 347 ms: 1.84x faster                                                      |
| pylint                   | 350 ms                                                      | 198 ms: 1.77x faster                                                      |
| go                       | 139 ms                                                      | 88.9 ms: 1.56x faster                                                     |
| generators               | 32.4 ms                                                     | 21.7 ms: 1.49x faster                                                     |
| richards_super           | 52.2 ms                                                     | 35.8 ms: 1.46x faster                                                     |
| chaos                    | 61.7 ms                                                     | 43.2 ms: 1.43x faster                                                     |
| logging_silent           | 94.6 ns                                                     | 66.4 ns: 1.43x faster                                                     |
| deepcopy                 | 255 us                                                      | 184 us: 1.39x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.73 ms: 1.36x faster                                                     |
| comprehensions           | 16.5 us                                                     | 12.1 us: 1.36x faster                                                     |
| sqlglot_parse            | 1.22 ms                                                     | 896 us: 1.36x faster                                                      |
| raytrace                 | 273 ms                                                      | 202 ms: 1.35x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 21.4 us: 1.34x faster                                                     |
| sqlglot_transpile        | 1.48 ms                                                     | 1.10 ms: 1.34x faster                                                     |
| richards                 | 42.4 ms                                                     | 31.8 ms: 1.33x faster                                                     |
| scimark_lu               | 85.8 ms                                                     | 65.0 ms: 1.32x faster                                                     |
| mako                     | 9.03 ms                                                     | 6.94 ms: 1.30x faster                                                     |
| html5lib                 | 51.0 ms                                                     | 39.3 ms: 1.30x faster                                                     |
| pyflate                  | 409 ms                                                      | 318 ms: 1.28x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 48.8 ms: 1.28x faster                                                     |
| hexiom                   | 5.74 ms                                                     | 4.53 ms: 1.27x faster                                                     |
| genshi_text              | 19.8 ms                                                     | 15.7 ms: 1.26x faster                                                     |
| pycparser                | 930 ms                                                      | 738 ms: 1.26x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 62.8 ms: 1.23x faster                                                     |
| regex_compile            | 106 ms                                                      | 86.5 ms: 1.23x faster                                                     |
| mdp                      | 1.78 sec                                                    | 1.46 sec: 1.22x faster                                                    |
| scimark_monte_carlo      | 57.3 ms                                                     | 47.3 ms: 1.21x faster                                                     |
| dulwich_log              | 50.5 ms                                                     | 42.3 ms: 1.19x faster                                                     |
| genshi_xml               | 41.0 ms                                                     | 34.4 ms: 1.19x faster                                                     |
| coroutines               | 16.0 ms                                                     | 13.4 ms: 1.19x faster                                                     |
| sympy_sum                | 107 ms                                                      | 89.9 ms: 1.19x faster                                                     |
| pickle_pure_python       | 270 us                                                      | 228 us: 1.18x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.4 ms: 1.18x faster                                                     |
| sqlite_synth             | 1.91 us                                                     | 1.62 us: 1.18x faster                                                     |
| bench_thread_pool        | 958 us                                                      | 814 us: 1.18x faster                                                      |
| float                    | 61.7 ms                                                     | 52.7 ms: 1.17x faster                                                     |
| scimark_sor              | 106 ms                                                      | 90.7 ms: 1.17x faster                                                     |
| unpickle_pure_python     | 183 us                                                      | 157 us: 1.17x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.43 sec: 1.17x faster                                                    |
| deepcopy_reduce          | 2.20 us                                                     | 1.89 us: 1.17x faster                                                     |
| docutils                 | 1.92 sec                                                    | 1.65 sec: 1.16x faster                                                    |
| thrift                   | 617 us                                                      | 533 us: 1.16x faster                                                      |
| regex_dna                | 136 ms                                                      | 118 ms: 1.16x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.2 ms: 1.15x faster                                                     |
| regex_effbot             | 1.66 ms                                                     | 1.44 ms: 1.15x faster                                                     |
| sqlglot_optimize         | 39.8 ms                                                     | 34.6 ms: 1.15x faster                                                     |
| xml_etree_process        | 44.5 ms                                                     | 40.0 ms: 1.11x faster                                                     |
| sympy_str                | 194 ms                                                      | 177 ms: 1.10x faster                                                      |
| 2to3                     | 246 ms                                                      | 224 ms: 1.10x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 88.8 ms: 1.09x faster                                                     |
| sqlglot_normalize        | 205 ms                                                      | 190 ms: 1.08x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 550 ms: 1.08x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.14 sec: 1.07x faster                                                    |
| nqueens                  | 66.6 ms                                                     | 62.9 ms: 1.06x faster                                                     |
| sympy_expand             | 314 ms                                                      | 301 ms: 1.04x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.6 ms: 1.04x faster                                                     |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.68 ms: 1.02x faster                                                     |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.83 us: 1.01x slower                                                     |
| json                     | 3.14 ms                                                     | 3.18 ms: 1.01x slower                                                     |
| meteor_contest           | 75.9 ms                                                     | 77.1 ms: 1.01x slower                                                     |
| xml_etree_generate       | 55.5 ms                                                     | 56.4 ms: 1.02x slower                                                     |
| scimark_fft              | 187 ms                                                      | 191 ms: 1.02x slower                                                      |
| logging_simple           | 6.22 us                                                     | 6.43 us: 1.03x slower                                                     |
| async_generators         | 222 ms                                                      | 240 ms: 1.08x slower                                                      |
| nbody                    | 71.3 ms                                                     | 77.4 ms: 1.09x slower                                                     |
| fannkuch                 | 256 ms                                                      | 281 ms: 1.10x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 17.4 ms: 1.12x slower                                                     |
| python_startup           | 20.6 ms                                                     | 23.4 ms: 1.14x slower                                                     |
| mypy2                    | 555 ms                                                      | 634 ms: 1.14x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.58 ms: 1.16x slower                                                     |
| coverage                 | 39.0 ms                                                     | 46.3 ms: 1.19x slower                                                     |
| bench_mp_pool            | 62.0 ms                                                     | 82.1 ms: 1.32x slower                                                     |
| regex_v8                 | 15.4 ms                                                     | 20.8 ms: 1.35x slower                                                     |
| gc_traversal             | 1.41 ms                                                     | 1.96 ms: 1.39x slower                                                     |
| create_gc_cycles         | 800 us                                                      | 1.21 ms: 1.51x slower                                                     |
| Geometric mean           | (ref)                                                       | 1.19x faster                                                              |

Benchmark hidden because not significant (2): pathlib, json_loads
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250102-3.14.0a3+-05f479c/bm-20250102-pythonperf1-amd64-eendebakpt-iter_freelists-3.14.0a3+-05f479c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.194x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown