# Results vs. 3.10.4

- fork: python
- ref: cb640b659e14cb0a0576
- machine: windows-amd64
- commit hash: cb640b6
- commit date: 2025-02-06
- overall geometric mean: 1.229x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250206-pythonperf1-amd64-python-cb640b659e14cb0a0576-3.14.0a4+-cb640b6 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 228 ms: 1.08x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.64 sec: 1.17x faster                                                      |
| html5lib       | 51.0 ms                                                     | 39.6 ms: 1.29x faster                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250206-pythonperf1-amd64-python-cb640b659e14cb0a0576-3.14.0a4+-cb640b6 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 417 ms: 2.66x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 220 ms: 2.39x faster                                                        |
| async_tree_none         | 435 ms                                                      | 185 ms: 2.35x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 336 ms: 1.90x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.31x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250206-pythonperf1-amd64-python-cb640b659e14cb0a0576-3.14.0a4+-cb640b6 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 45.7 ms: 1.35x faster                                                       |
| nbody          | 71.3 ms                                                     | 72.2 ms: 1.01x slower                                                       |
| pidigits       | 149 ms                                                      | 152 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                       | 1.10x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250206-pythonperf1-amd64-python-cb640b659e14cb0a0576-3.14.0a4+-cb640b6 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 84.7 ms: 1.25x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.46 ms: 1.13x faster                                                       |
| regex_dna      | 136 ms                                                      | 124 ms: 1.10x faster                                                        |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250206-pythonperf1-amd64-python-cb640b659e14cb0a0576-3.14.0a4+-cb640b6 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.78 ms: 1.35x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 140 us: 1.31x faster                                                        |
| pickle_pure_python   | 270 us                                                      | 214 us: 1.26x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.36 sec: 1.23x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 39.1 ms: 1.14x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 94.1 ms: 1.03x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 67.3 ms: 1.04x slower                                                       |
| json_loads           | 14.0 us                                                     | 15.3 us: 1.09x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.12x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250206-pythonperf1-amd64-python-cb640b659e14cb0a0576-3.14.0a4+-cb640b6 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.4 ms: 1.25x slower                                                       |
| python_startup         | 20.6 ms                                                     | 26.2 ms: 1.27x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250206-pythonperf1-amd64-python-cb640b659e14cb0a0576-3.14.0a4+-cb640b6 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.61 ms: 1.37x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 15.5 ms: 1.28x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 34.3 ms: 1.20x faster                                                       |
| django_template | 28.9 ms                                                     | 25.5 ms: 1.13x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.24x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250206-pythonperf1-amd64-python-cb640b659e14cb0a0576-3.14.0a4+-cb640b6 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 106 us: 3.16x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 417 ms: 2.66x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 220 ms: 2.39x faster                                                        |
| async_tree_none          | 435 ms                                                      | 185 ms: 2.35x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.15 ms: 1.94x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 336 ms: 1.90x faster                                                        |
| pylint                   | 350 ms                                                      | 200 ms: 1.75x faster                                                        |
| generators               | 32.4 ms                                                     | 19.7 ms: 1.65x faster                                                       |
| go                       | 139 ms                                                      | 86.1 ms: 1.61x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 58.9 ns: 1.61x faster                                                       |
| richards_super           | 52.2 ms                                                     | 32.5 ms: 1.61x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 18.9 us: 1.52x faster                                                       |
| comprehensions           | 16.5 us                                                     | 10.9 us: 1.51x faster                                                       |
| chaos                    | 61.7 ms                                                     | 41.8 ms: 1.48x faster                                                       |
| richards                 | 42.4 ms                                                     | 29.2 ms: 1.45x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 60.2 ms: 1.43x faster                                                       |
| raytrace                 | 273 ms                                                      | 193 ms: 1.41x faster                                                        |
| sqlglot_parse            | 1.22 ms                                                     | 863 us: 1.41x faster                                                        |
| deepcopy                 | 255 us                                                      | 182 us: 1.41x faster                                                        |
| pyflate                  | 409 ms                                                      | 294 ms: 1.39x faster                                                        |
| sqlglot_transpile        | 1.48 ms                                                     | 1.06 ms: 1.39x faster                                                       |
| mako                     | 9.03 ms                                                     | 6.61 ms: 1.37x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.78 ms: 1.35x faster                                                       |
| float                    | 61.7 ms                                                     | 45.7 ms: 1.35x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.27 ms: 1.34x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 43.7 ms: 1.31x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 59.0 ms: 1.31x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 140 us: 1.31x faster                                                        |
| crypto_pyaes             | 62.5 ms                                                     | 48.1 ms: 1.30x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 39.6 ms: 1.29x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 15.5 ms: 1.28x faster                                                       |
| pycparser                | 930 ms                                                      | 728 ms: 1.28x faster                                                        |
| scimark_sor              | 106 ms                                                      | 83.5 ms: 1.27x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 214 us: 1.26x faster                                                        |
| regex_compile            | 106 ms                                                      | 84.7 ms: 1.25x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.36 sec: 1.23x faster                                                      |
| coroutines               | 16.0 ms                                                     | 13.0 ms: 1.23x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 61.5 ms: 1.23x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.57 us: 1.22x faster                                                       |
| thrift                   | 617 us                                                      | 515 us: 1.20x faster                                                        |
| genshi_xml               | 41.0 ms                                                     | 34.3 ms: 1.20x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 42.3 ms: 1.19x faster                                                       |
| sympy_sum                | 107 ms                                                      | 90.0 ms: 1.19x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.87 us: 1.18x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.64 sec: 1.17x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.2 ms: 1.16x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.06 sec: 1.15x faster                                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 35.0 ms: 1.14x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 39.1 ms: 1.14x faster                                                       |
| django_template          | 28.9 ms                                                     | 25.5 ms: 1.13x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.46 ms: 1.13x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 850 us: 1.13x faster                                                        |
| pprint_safe_repr         | 592 ms                                                      | 528 ms: 1.12x faster                                                        |
| mdp                      | 1.78 sec                                                    | 1.59 sec: 1.12x faster                                                      |
| sympy_str                | 194 ms                                                      | 175 ms: 1.11x faster                                                        |
| regex_dna                | 136 ms                                                      | 124 ms: 1.10x faster                                                        |
| sqlglot_normalize        | 205 ms                                                      | 188 ms: 1.09x faster                                                        |
| 2to3                     | 246 ms                                                      | 228 ms: 1.08x faster                                                        |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.55 ms: 1.07x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 63.2 ms: 1.05x faster                                                       |
| sympy_expand             | 314 ms                                                      | 299 ms: 1.05x faster                                                        |
| xml_etree_parse          | 96.8 ms                                                     | 94.1 ms: 1.03x faster                                                       |
| scimark_fft              | 187 ms                                                      | 183 ms: 1.02x faster                                                        |
| logging_format           | 6.76 us                                                     | 6.62 us: 1.02x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 75.3 ms: 1.01x faster                                                       |
| nbody                    | 71.3 ms                                                     | 72.2 ms: 1.01x slower                                                       |
| pidigits                 | 149 ms                                                      | 152 ms: 1.02x slower                                                        |
| json                     | 3.14 ms                                                     | 3.18 ms: 1.02x slower                                                       |
| async_generators         | 222 ms                                                      | 227 ms: 1.02x slower                                                        |
| xml_etree_iterparse      | 65.0 ms                                                     | 67.3 ms: 1.04x slower                                                       |
| fannkuch                 | 256 ms                                                      | 272 ms: 1.06x slower                                                        |
| json_loads               | 14.0 us                                                     | 15.3 us: 1.09x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.72 ms: 1.20x slower                                                       |
| coverage                 | 39.0 ms                                                     | 47.6 ms: 1.22x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 19.4 ms: 1.25x slower                                                       |
| python_startup           | 20.6 ms                                                     | 26.2 ms: 1.27x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.03 ms: 1.44x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 89.4 ms: 1.44x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.22 ms: 1.52x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.22x faster                                                                |

Benchmark hidden because not significant (3): logging_simple, xml_etree_generate, regex_v8
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250206-3.14.0a4+-cb640b6/bm-20250206-pythonperf1-amd64-python-cb640b659e14cb0a0576-3.14.0a4+-cb640b6.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.229x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown