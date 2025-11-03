# Results vs. 3.10.4

- fork: python
- ref: 2f60b8f02fe7cb83dd58
- machine: windows-amd64
- commit hash: 2f60b8f
- commit date: 2025-11-01
- overall geometric mean: 1.204x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 217 ms: 1.13x faster                                                        |
| docutils       | 1.92 sec                                                    | 2.72 sec: 1.42x slower                                                      |
| html5lib       | 51.0 ms                                                     | 39.2 ms: 1.30x faster                                                       |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 336 ms: 3.30x faster                                                        |
| async_tree_none         | 435 ms                                                      | 163 ms: 2.67x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 208 ms: 2.53x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 329 ms: 1.94x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.56x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 45.0 ms: 1.37x faster                                                       |
| pidigits       | 149 ms                                                      | 134 ms: 1.11x faster                                                        |
| nbody          | 71.3 ms                                                     | 76.9 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 111 ms: 1.22x faster                                                        |
| regex_compile  | 106 ms                                                      | 88.6 ms: 1.20x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 13.1 ms: 1.18x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.57 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.95 ms: 1.54x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 148 us: 1.24x faster                                                        |
| pickle_pure_python   | 270 us                                                      | 225 us: 1.20x faster                                                        |
| xml_etree_iterparse  | 65.0 ms                                                     | 57.7 ms: 1.13x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 87.2 ms: 1.11x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 42.5 ms: 1.05x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 60.1 ms: 1.08x slower                                                       |
| unpickle             | 9.09 us                                                     | 9.86 us: 1.08x slower                                                       |
| pickle_list          | 2.75 us                                                     | 3.03 us: 1.10x slower                                                       |
| unpickle_list        | 2.71 us                                                     | 3.00 us: 1.10x slower                                                       |
| json_loads           | 14.0 us                                                     | 15.8 us: 1.12x slower                                                       |
| pickle               | 6.85 us                                                     | 7.91 us: 1.16x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 20.1 us: 1.17x slower                                                       |
| tomli_loads          | 1.67 sec                                                    | 2.17 sec: 1.30x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.00x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 18.9 ms: 1.22x slower                                                       |
| python_startup         | 20.6 ms                                                     | 25.2 ms: 1.22x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.22x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 28.9 ms                                                     | 26.0 ms: 1.11x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 37.6 ms: 1.09x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 18.4 ms: 1.08x faster                                                       |
| mako            | 9.03 ms                                                     | 9.63 ms: 1.07x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.05x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io            | 1.11 sec                                                    | 336 ms: 3.30x faster                                                        |
| typing_runtime_protocols | 336 us                                                      | 123 us: 2.73x faster                                                        |
| async_tree_none          | 435 ms                                                      | 163 ms: 2.67x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 29.0 ms: 2.61x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 208 ms: 2.53x faster                                                        |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 329 ms: 1.94x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.31 ms: 1.82x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.01 sec: 1.77x faster                                                      |
| pylint                   | 350 ms                                                      | 203 ms: 1.72x faster                                                        |
| logging_silent           | 94.6 ns                                                     | 58.0 ns: 1.63x faster                                                       |
| go                       | 139 ms                                                      | 86.2 ms: 1.61x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 18.6 us: 1.55x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 5.95 ms: 1.54x faster                                                       |
| generators               | 32.4 ms                                                     | 21.1 ms: 1.54x faster                                                       |
| richards_super           | 52.2 ms                                                     | 36.2 ms: 1.44x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.34 us: 1.43x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.6 us: 1.43x faster                                                       |
| deepcopy                 | 255 us                                                      | 179 us: 1.42x faster                                                        |
| chaos                    | 61.7 ms                                                     | 44.5 ms: 1.39x faster                                                       |
| richards                 | 42.4 ms                                                     | 30.9 ms: 1.37x faster                                                       |
| float                    | 61.7 ms                                                     | 45.0 ms: 1.37x faster                                                       |
| pyflate                  | 409 ms                                                      | 302 ms: 1.36x faster                                                        |
| pycparser                | 930 ms                                                      | 691 ms: 1.35x faster                                                        |
| asyncio_tcp              | 732 ms                                                      | 544 ms: 1.35x faster                                                        |
| scimark_lu               | 85.8 ms                                                     | 63.9 ms: 1.34x faster                                                       |
| raytrace                 | 273 ms                                                      | 205 ms: 1.33x faster                                                        |
| html5lib                 | 51.0 ms                                                     | 39.2 ms: 1.30x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.45 ms: 1.29x faster                                                       |
| scimark_sor              | 106 ms                                                      | 83.4 ms: 1.27x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 40.1 ms: 1.26x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 148 us: 1.24x faster                                                        |
| regex_dna                | 136 ms                                                      | 111 ms: 1.22x faster                                                        |
| pickle_pure_python       | 270 us                                                      | 225 us: 1.20x faster                                                        |
| regex_compile            | 106 ms                                                      | 88.6 ms: 1.20x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 13.1 ms: 1.18x faster                                                       |
| sympy_sum                | 107 ms                                                      | 91.2 ms: 1.17x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 49.4 ms: 1.16x faster                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.22 ms: 1.16x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.4 ms: 1.14x faster                                                       |
| coroutines               | 16.0 ms                                                     | 14.1 ms: 1.13x faster                                                       |
| 2to3                     | 246 ms                                                      | 217 ms: 1.13x faster                                                        |
| xml_etree_iterparse      | 65.0 ms                                                     | 57.7 ms: 1.13x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 68.6 ms: 1.13x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 55.9 ms: 1.12x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.98 us: 1.11x faster                                                       |
| thrift                   | 617 us                                                      | 555 us: 1.11x faster                                                        |
| django_template          | 28.9 ms                                                     | 26.0 ms: 1.11x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 87.2 ms: 1.11x faster                                                       |
| pidigits                 | 149 ms                                                      | 134 ms: 1.11x faster                                                        |
| pprint_safe_repr         | 592 ms                                                      | 534 ms: 1.11x faster                                                        |
| genshi_xml               | 41.0 ms                                                     | 37.6 ms: 1.09x faster                                                       |
| sympy_str                | 194 ms                                                      | 178 ms: 1.09x faster                                                        |
| genshi_text              | 19.8 ms                                                     | 18.4 ms: 1.08x faster                                                       |
| unpack_sequence          | 39.6 ns                                                     | 37.0 ns: 1.07x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.57 ms: 1.05x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 42.5 ms: 1.05x faster                                                       |
| json                     | 3.14 ms                                                     | 3.00 ms: 1.04x faster                                                       |
| sympy_expand             | 314 ms                                                      | 305 ms: 1.03x faster                                                        |
| logging_format           | 6.76 us                                                     | 6.87 us: 1.02x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.40 us: 1.03x slower                                                       |
| nqueens                  | 66.6 ms                                                     | 70.1 ms: 1.05x slower                                                       |
| bench_thread_pool        | 958 us                                                      | 1.01 ms: 1.05x slower                                                       |
| mako                     | 9.03 ms                                                     | 9.63 ms: 1.07x slower                                                       |
| nbody                    | 71.3 ms                                                     | 76.9 ms: 1.08x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 60.1 ms: 1.08x slower                                                       |
| unpickle                 | 9.09 us                                                     | 9.86 us: 1.08x slower                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.96 ms: 1.09x slower                                                       |
| meteor_contest           | 75.9 ms                                                     | 83.3 ms: 1.10x slower                                                       |
| pickle_list              | 2.75 us                                                     | 3.03 us: 1.10x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 3.00 us: 1.10x slower                                                       |
| json_loads               | 14.0 us                                                     | 15.8 us: 1.12x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.91 us: 1.16x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 20.1 us: 1.17x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 72.7 ms: 1.17x slower                                                       |
| async_generators         | 222 ms                                                      | 262 ms: 1.18x slower                                                        |
| fannkuch                 | 256 ms                                                      | 306 ms: 1.20x slower                                                        |
| python_startup_no_site   | 15.5 ms                                                     | 18.9 ms: 1.22x slower                                                       |
| python_startup           | 20.6 ms                                                     | 25.2 ms: 1.22x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.91 ms: 1.25x slower                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.55 sec: 1.27x slower                                                      |
| tomli_loads              | 1.67 sec                                                    | 2.17 sec: 1.30x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.07 ms: 1.33x slower                                                       |
| docutils                 | 1.92 sec                                                    | 2.72 sec: 1.42x slower                                                      |
| coverage                 | 39.0 ms                                                     | 67.1 ms: 1.72x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.17x faster                                                                |

Benchmark hidden because not significant (2): scimark_fft, asyncio_tcp_ssl
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20251101-3.15.0a1+-2f60b8f-NOGIL/bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.204x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown