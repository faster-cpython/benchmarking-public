# Results vs. 3.10.4

- fork: python
- ref: 2228e92da31ca7344a16
- machine: windows-amd64
- commit hash: 2228e92
- commit date: 2025-01-05
- overall geometric mean: 1.196x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 224 ms: 1.10x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.67 sec: 1.15x faster                                                      |
| html5lib       | 51.0 ms                                                     | 40.2 ms: 1.27x faster                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 404 ms: 2.74x faster                                                        |
| async_tree_none         | 435 ms                                                      | 182 ms: 2.39x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 224 ms: 2.35x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 350 ms: 1.82x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.30x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 53.0 ms: 1.16x faster                                                       |
| pidigits       | 149 ms                                                      | 146 ms: 1.02x faster                                                        |
| nbody          | 71.3 ms                                                     | 77.0 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 87.5 ms: 1.21x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.47 ms: 1.13x faster                                                       |
| regex_dna      | 136 ms                                                      | 127 ms: 1.07x faster                                                        |
| regex_v8       | 15.4 ms                                                     | 24.6 ms: 1.60x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.70 ms: 1.37x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 148 us: 1.24x faster                                                        |
| pickle_pure_python   | 270 us                                                      | 221 us: 1.22x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.39 sec: 1.20x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 87.5 ms: 1.11x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 40.2 ms: 1.10x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.7 ms: 1.04x faster                                                       |
| json_loads           | 14.0 us                                                     | 14.5 us: 1.03x slower                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 57.4 ms: 1.03x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.13x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 17.2 ms: 1.11x slower                                                       |
| python_startup         | 20.6 ms                                                     | 23.1 ms: 1.12x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.87 ms: 1.32x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 16.7 ms: 1.19x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 34.6 ms: 1.19x faster                                                       |
| django_template | 28.9 ms                                                     | 24.8 ms: 1.16x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.21x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 112 us: 2.99x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 404 ms: 2.74x faster                                                        |
| async_tree_none          | 435 ms                                                      | 182 ms: 2.39x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 224 ms: 2.35x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.26 ms: 1.86x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 350 ms: 1.82x faster                                                        |
| pylint                   | 350 ms                                                      | 199 ms: 1.76x faster                                                        |
| go                       | 139 ms                                                      | 87.2 ms: 1.59x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 61.6 ns: 1.54x faster                                                       |
| richards_super           | 52.2 ms                                                     | 34.1 ms: 1.53x faster                                                       |
| generators               | 32.4 ms                                                     | 21.1 ms: 1.53x faster                                                       |
| richards                 | 42.4 ms                                                     | 29.7 ms: 1.43x faster                                                       |
| chaos                    | 61.7 ms                                                     | 43.5 ms: 1.42x faster                                                       |
| raytrace                 | 273 ms                                                      | 193 ms: 1.41x faster                                                        |
| scimark_lu               | 85.8 ms                                                     | 61.5 ms: 1.40x faster                                                       |
| deepcopy                 | 255 us                                                      | 184 us: 1.39x faster                                                        |
| comprehensions           | 16.5 us                                                     | 11.9 us: 1.39x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 20.8 us: 1.38x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.70 ms: 1.37x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 889 us: 1.37x faster                                                        |
| hexiom                   | 5.74 ms                                                     | 4.27 ms: 1.35x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.11 ms: 1.33x faster                                                       |
| mako                     | 9.03 ms                                                     | 6.87 ms: 1.32x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 48.2 ms: 1.30x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 40.2 ms: 1.27x faster                                                       |
| pyflate                  | 409 ms                                                      | 326 ms: 1.26x faster                                                        |
| pycparser                | 930 ms                                                      | 742 ms: 1.25x faster                                                        |
| mdp                      | 1.78 sec                                                    | 1.43 sec: 1.25x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 148 us: 1.24x faster                                                        |
| pickle_pure_python       | 270 us                                                      | 221 us: 1.22x faster                                                        |
| regex_compile            | 106 ms                                                      | 87.5 ms: 1.21x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 64.1 ms: 1.21x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.39 sec: 1.20x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 47.8 ms: 1.20x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.4 ms: 1.19x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.61 us: 1.19x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 16.7 ms: 1.19x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 34.6 ms: 1.19x faster                                                       |
| sympy_sum                | 107 ms                                                      | 90.2 ms: 1.19x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 42.7 ms: 1.18x faster                                                       |
| thrift                   | 617 us                                                      | 524 us: 1.18x faster                                                        |
| scimark_sor              | 106 ms                                                      | 90.3 ms: 1.18x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 818 us: 1.17x faster                                                        |
| deepcopy_reduce          | 2.20 us                                                     | 1.89 us: 1.17x faster                                                       |
| django_template          | 28.9 ms                                                     | 24.8 ms: 1.16x faster                                                       |
| float                    | 61.7 ms                                                     | 53.0 ms: 1.16x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.67 sec: 1.15x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.4 ms: 1.14x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.07 sec: 1.14x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.47 ms: 1.13x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 531 ms: 1.12x faster                                                        |
| sqlglot_optimize         | 39.8 ms                                                     | 35.9 ms: 1.11x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 87.5 ms: 1.11x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 40.2 ms: 1.10x faster                                                       |
| 2to3                     | 246 ms                                                      | 224 ms: 1.10x faster                                                        |
| sympy_str                | 194 ms                                                      | 177 ms: 1.10x faster                                                        |
| regex_dna                | 136 ms                                                      | 127 ms: 1.07x faster                                                        |
| nqueens                  | 66.6 ms                                                     | 62.2 ms: 1.07x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.60 ms: 1.05x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 196 ms: 1.05x faster                                                        |
| json                     | 3.14 ms                                                     | 3.01 ms: 1.04x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.7 ms: 1.04x faster                                                       |
| sympy_expand             | 314 ms                                                      | 305 ms: 1.03x faster                                                        |
| pidigits                 | 149 ms                                                      | 146 ms: 1.02x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 76.6 ms: 1.01x slower                                                       |
| meteor_contest           | 75.9 ms                                                     | 77.0 ms: 1.01x slower                                                       |
| logging_format           | 6.76 us                                                     | 6.89 us: 1.02x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.38 us: 1.03x slower                                                       |
| scimark_fft              | 187 ms                                                      | 193 ms: 1.03x slower                                                        |
| json_loads               | 14.0 us                                                     | 14.5 us: 1.03x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 57.4 ms: 1.03x slower                                                       |
| fannkuch                 | 256 ms                                                      | 266 ms: 1.04x slower                                                        |
| async_generators         | 222 ms                                                      | 238 ms: 1.08x slower                                                        |
| nbody                    | 71.3 ms                                                     | 77.0 ms: 1.08x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 17.2 ms: 1.11x slower                                                       |
| python_startup           | 20.6 ms                                                     | 23.1 ms: 1.12x slower                                                       |
| mypy2                    | 555 ms                                                      | 639 ms: 1.15x slower                                                        |
| coverage                 | 39.0 ms                                                     | 46.5 ms: 1.19x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.82 ms: 1.22x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 82.5 ms: 1.33x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.96 ms: 1.39x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.21 ms: 1.51x slower                                                       |
| regex_v8                 | 15.4 ms                                                     | 24.6 ms: 1.60x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.19x faster                                                                |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250105-3.14.0a3+-2228e92/bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.196x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown