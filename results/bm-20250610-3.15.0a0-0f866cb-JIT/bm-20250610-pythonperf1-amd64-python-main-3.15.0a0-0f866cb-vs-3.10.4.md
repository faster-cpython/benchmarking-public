# Results vs. 3.10.4

- fork: python
- ref: main
- machine: windows-amd64
- commit hash: 0f866cb
- commit date: 2025-06-10
- overall geometric mean: 1.183x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-pythonperf1-amd64-python-main-3.15.0a0-0f866cb |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 220 ms: 1.12x faster                                       |
| docutils       | 1.92 sec                                                    | 1.66 sec: 1.16x faster                                     |
| html5lib       | 51.0 ms                                                     | 38.4 ms: 1.33x faster                                      |
| Geometric mean | (ref)                                                       | 1.20x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-pythonperf1-amd64-python-main-3.15.0a0-0f866cb |
|-------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 395 ms: 2.81x faster                                       |
| async_tree_none         | 435 ms                                                      | 170 ms: 2.56x faster                                       |
| async_tree_memoization  | 526 ms                                                      | 207 ms: 2.55x faster                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 332 ms: 1.92x faster                                       |
| Geometric mean          | (ref)                                                       | 2.43x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-pythonperf1-amd64-python-main-3.15.0a0-0f866cb |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 61.7 ms                                                     | 43.4 ms: 1.42x faster                                      |
| nbody          | 71.3 ms                                                     | 60.6 ms: 1.18x faster                                      |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                       |
| Geometric mean | (ref)                                                       | 1.19x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-pythonperf1-amd64-python-main-3.15.0a0-0f866cb |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 78.0 ms: 1.36x faster                                      |
| regex_dna      | 136 ms                                                      | 116 ms: 1.18x faster                                       |
| regex_v8       | 15.4 ms                                                     | 13.8 ms: 1.12x faster                                      |
| regex_effbot   | 1.66 ms                                                     | 1.54 ms: 1.08x faster                                      |
| Geometric mean | (ref)                                                       | 1.18x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-pythonperf1-amd64-python-main-3.15.0a0-0f866cb |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 112 us: 1.64x faster                                       |
| json_dumps           | 9.16 ms                                                     | 6.18 ms: 1.48x faster                                      |
| tomli_loads          | 1.67 sec                                                    | 1.14 sec: 1.47x faster                                     |
| pickle_pure_python   | 270 us                                                      | 206 us: 1.31x faster                                       |
| xml_etree_process    | 44.5 ms                                                     | 36.7 ms: 1.21x faster                                      |
| xml_etree_parse      | 96.8 ms                                                     | 88.0 ms: 1.10x faster                                      |
| xml_etree_generate   | 55.5 ms                                                     | 53.3 ms: 1.04x faster                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 64.0 ms: 1.02x faster                                      |
| json_loads           | 14.0 us                                                     | 14.5 us: 1.03x slower                                      |
| Geometric mean       | (ref)                                                       | 1.23x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-pythonperf1-amd64-python-main-3.15.0a0-0f866cb |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.5 ms: 1.26x slower                                      |
| python_startup         | 20.6 ms                                                     | 26.1 ms: 1.27x slower                                      |
| Geometric mean         | (ref)                                                       | 1.26x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-pythonperf1-amd64-python-main-3.15.0a0-0f866cb |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.50 ms: 1.64x faster                                      |
| genshi_text     | 19.8 ms                                                     | 15.4 ms: 1.29x faster                                      |
| django_template | 28.9 ms                                                     | 23.8 ms: 1.21x faster                                      |
| genshi_xml      | 41.0 ms                                                     | 34.7 ms: 1.18x faster                                      |
| Geometric mean  | (ref)                                                       | 1.32x faster                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-pythonperf1-amd64-python-main-3.15.0a0-0f866cb |
|--------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 105 us: 3.21x faster                                       |
| async_tree_io            | 1.11 sec                                                    | 395 ms: 2.81x faster                                       |
| async_tree_none          | 435 ms                                                      | 170 ms: 2.56x faster                                       |
| async_tree_memoization   | 526 ms                                                      | 207 ms: 2.55x faster                                       |
| pathlib                  | 75.7 ms                                                     | 32.2 ms: 2.35x faster                                      |
| mdp                      | 1.78 sec                                                    | 812 ms: 2.19x faster                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 332 ms: 1.92x faster                                       |
| deltablue                | 4.19 ms                                                     | 2.21 ms: 1.90x faster                                      |
| go                       | 139 ms                                                      | 75.6 ms: 1.84x faster                                      |
| pylint                   | 350 ms                                                      | 202 ms: 1.74x faster                                       |
| richards_super           | 52.2 ms                                                     | 30.5 ms: 1.71x faster                                      |
| mako                     | 9.03 ms                                                     | 5.50 ms: 1.64x faster                                      |
| unpickle_pure_python     | 183 us                                                      | 112 us: 1.64x faster                                       |
| generators               | 32.4 ms                                                     | 19.9 ms: 1.63x faster                                      |
| pyflate                  | 409 ms                                                      | 256 ms: 1.60x faster                                       |
| richards                 | 42.4 ms                                                     | 26.7 ms: 1.59x faster                                      |
| chaos                    | 61.7 ms                                                     | 39.3 ms: 1.57x faster                                      |
| deepcopy_memo            | 28.8 us                                                     | 18.5 us: 1.56x faster                                      |
| raytrace                 | 273 ms                                                      | 177 ms: 1.54x faster                                       |
| comprehensions           | 16.5 us                                                     | 10.9 us: 1.51x faster                                      |
| deepcopy                 | 255 us                                                      | 170 us: 1.51x faster                                       |
| json_dumps               | 9.16 ms                                                     | 6.18 ms: 1.48x faster                                      |
| tomli_loads              | 1.67 sec                                                    | 1.14 sec: 1.47x faster                                     |
| scimark_lu               | 85.8 ms                                                     | 59.2 ms: 1.45x faster                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 39.9 ms: 1.44x faster                                      |
| float                    | 61.7 ms                                                     | 43.4 ms: 1.42x faster                                      |
| hexiom                   | 5.74 ms                                                     | 4.10 ms: 1.40x faster                                      |
| scimark_sor              | 106 ms                                                      | 76.2 ms: 1.39x faster                                      |
| regex_compile            | 106 ms                                                      | 78.0 ms: 1.36x faster                                      |
| crypto_pyaes             | 62.5 ms                                                     | 46.5 ms: 1.34x faster                                      |
| html5lib                 | 51.0 ms                                                     | 38.4 ms: 1.33x faster                                      |
| pycparser                | 930 ms                                                      | 703 ms: 1.32x faster                                       |
| pickle_pure_python       | 270 us                                                      | 206 us: 1.31x faster                                       |
| genshi_text              | 19.8 ms                                                     | 15.4 ms: 1.29x faster                                      |
| spectral_norm            | 77.3 ms                                                     | 62.0 ms: 1.25x faster                                      |
| sqlite_synth             | 1.91 us                                                     | 1.56 us: 1.23x faster                                      |
| sympy_sum                | 107 ms                                                      | 87.9 ms: 1.22x faster                                      |
| django_template          | 28.9 ms                                                     | 23.8 ms: 1.21x faster                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.82 us: 1.21x faster                                      |
| xml_etree_process        | 44.5 ms                                                     | 36.7 ms: 1.21x faster                                      |
| sympy_integrate          | 15.3 ms                                                     | 12.7 ms: 1.21x faster                                      |
| dulwich_log              | 50.5 ms                                                     | 41.8 ms: 1.21x faster                                      |
| scimark_fft              | 187 ms                                                      | 158 ms: 1.19x faster                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.30 ms: 1.18x faster                                      |
| genshi_xml               | 41.0 ms                                                     | 34.7 ms: 1.18x faster                                      |
| regex_dna                | 136 ms                                                      | 116 ms: 1.18x faster                                       |
| nbody                    | 71.3 ms                                                     | 60.6 ms: 1.18x faster                                      |
| docutils                 | 1.92 sec                                                    | 1.66 sec: 1.16x faster                                     |
| pprint_pformat           | 1.22 sec                                                    | 1.06 sec: 1.15x faster                                     |
| pprint_safe_repr         | 592 ms                                                      | 519 ms: 1.14x faster                                       |
| sympy_str                | 194 ms                                                      | 171 ms: 1.14x faster                                       |
| regex_v8                 | 15.4 ms                                                     | 13.8 ms: 1.12x faster                                      |
| 2to3                     | 246 ms                                                      | 220 ms: 1.12x faster                                       |
| nqueens                  | 66.6 ms                                                     | 60.1 ms: 1.11x faster                                      |
| coroutines               | 16.0 ms                                                     | 14.5 ms: 1.10x faster                                      |
| xml_etree_parse          | 96.8 ms                                                     | 88.0 ms: 1.10x faster                                      |
| regex_effbot             | 1.66 ms                                                     | 1.54 ms: 1.08x faster                                      |
| sympy_expand             | 314 ms                                                      | 296 ms: 1.06x faster                                       |
| fannkuch                 | 256 ms                                                      | 242 ms: 1.06x faster                                       |
| xml_etree_generate       | 55.5 ms                                                     | 53.3 ms: 1.04x faster                                      |
| meteor_contest           | 75.9 ms                                                     | 73.6 ms: 1.03x faster                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 64.0 ms: 1.02x faster                                      |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                       |
| logging_simple           | 6.22 us                                                     | 6.34 us: 1.02x slower                                      |
| json_loads               | 14.0 us                                                     | 14.5 us: 1.03x slower                                      |
| async_generators         | 222 ms                                                      | 247 ms: 1.12x slower                                       |
| telco                    | 3.94 ms                                                     | 4.44 ms: 1.13x slower                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.5 ms: 1.26x slower                                      |
| python_startup           | 20.6 ms                                                     | 26.1 ms: 1.27x slower                                      |
| gc_traversal             | 1.41 ms                                                     | 2.13 ms: 1.51x slower                                      |
| create_gc_cycles         | 800 us                                                      | 1.32 ms: 1.65x slower                                      |
| logging_silent           | 94.6 ns                                                     | 314 ns: 3.32x slower                                       |
| coverage                 | 39.0 ms                                                     | 298 ms: 7.63x slower                                       |
| thrift                   | 617 us                                                      | 95.2 ms: 154.13x slower                                    |
| Geometric mean           | (ref)                                                       | 1.16x faster                                               |

Benchmark hidden because not significant (2): json, logging_format
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250610-3.15.0a0-0f866cb-JIT/bm-20250610-pythonperf1-amd64-python-main-3.15.0a0-0f866cb.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.183x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: unknown