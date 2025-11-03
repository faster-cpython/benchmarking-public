# Results vs. 3.10.4

- fork: python
- ref: 2f60b8f02fe7cb83dd58
- machine: windows-amd64
- commit hash: 2f60b8f
- commit date: 2025-11-01
- overall geometric mean: 1.366x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 213 ms: 1.16x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.62 sec: 1.18x faster                                                      |
| html5lib       | 51.0 ms                                                     | 35.8 ms: 1.42x faster                                                       |
| Geometric mean | (ref)                                                       | 1.25x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 360 ms: 3.08x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 190 ms: 2.77x faster                                                        |
| async_tree_none         | 435 ms                                                      | 164 ms: 2.65x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 321 ms: 1.99x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.59x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 38.9 ms: 1.58x faster                                                       |
| nbody          | 71.3 ms                                                     | 53.1 ms: 1.34x faster                                                       |
| pidigits       | 149 ms                                                      | 147 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                       | 1.29x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 77.5 ms: 1.37x faster                                                       |
| regex_dna      | 136 ms                                                      | 117 ms: 1.16x faster                                                        |
| regex_v8       | 15.4 ms                                                     | 14.0 ms: 1.10x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 103 us: 1.78x faster                                                        |
| json_dumps           | 9.16 ms                                                     | 5.38 ms: 1.70x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.06 sec: 1.58x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 193 us: 1.40x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 34.2 ms: 1.30x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 56.6 ms: 1.15x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 48.6 ms: 1.14x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 85.3 ms: 1.13x faster                                                       |
| unpickle             | 9.09 us                                                     | 8.28 us: 1.10x faster                                                       |
| json_loads           | 14.0 us                                                     | 13.9 us: 1.01x faster                                                       |
| unpickle_list        | 2.71 us                                                     | 2.75 us: 1.01x slower                                                       |
| pickle               | 6.85 us                                                     | 7.35 us: 1.07x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 19.3 us: 1.12x slower                                                       |
| pickle_list          | 2.75 us                                                     | 3.25 us: 1.18x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.18x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.0 ms: 1.22x slower                                                       |
| python_startup         | 20.6 ms                                                     | 25.4 ms: 1.23x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.23x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.12 ms: 1.77x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 15.3 ms: 1.29x faster                                                       |
| django_template | 28.9 ms                                                     | 23.7 ms: 1.22x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 34.3 ms: 1.19x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.35x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 105 us: 3.19x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 360 ms: 3.08x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 190 ms: 2.77x faster                                                        |
| async_tree_none          | 435 ms                                                      | 164 ms: 2.65x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 29.0 ms: 2.61x faster                                                       |
| mdp                      | 1.78 sec                                                    | 779 ms: 2.28x faster                                                        |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 321 ms: 1.99x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.16 ms: 1.94x faster                                                       |
| go                       | 139 ms                                                      | 75.0 ms: 1.85x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 103 us: 1.78x faster                                                        |
| pylint                   | 350 ms                                                      | 198 ms: 1.77x faster                                                        |
| mako                     | 9.03 ms                                                     | 5.12 ms: 1.77x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 54.8 ns: 1.73x faster                                                       |
| richards_super           | 52.2 ms                                                     | 30.3 ms: 1.73x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 5.38 ms: 1.70x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 17.0 us: 1.69x faster                                                       |
| generators               | 32.4 ms                                                     | 19.2 ms: 1.68x faster                                                       |
| pyflate                  | 409 ms                                                      | 246 ms: 1.66x faster                                                        |
| comprehensions           | 16.5 us                                                     | 10.2 us: 1.62x faster                                                       |
| chaos                    | 61.7 ms                                                     | 38.2 ms: 1.61x faster                                                       |
| raytrace                 | 273 ms                                                      | 170 ms: 1.61x faster                                                        |
| deepcopy                 | 255 us                                                      | 160 us: 1.60x faster                                                        |
| float                    | 61.7 ms                                                     | 38.9 ms: 1.58x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.06 sec: 1.58x faster                                                      |
| richards                 | 42.4 ms                                                     | 27.0 ms: 1.57x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.38 sec: 1.53x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 57.4 ms: 1.50x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 3.87 ms: 1.48x faster                                                       |
| pycparser                | 930 ms                                                      | 646 ms: 1.44x faster                                                        |
| scimark_monte_carlo      | 57.3 ms                                                     | 39.9 ms: 1.44x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 413 ms: 1.43x faster                                                        |
| pprint_pformat           | 1.22 sec                                                    | 854 ms: 1.43x faster                                                        |
| html5lib                 | 51.0 ms                                                     | 35.8 ms: 1.42x faster                                                       |
| scimark_sor              | 106 ms                                                      | 74.8 ms: 1.42x faster                                                       |
| scimark_fft              | 187 ms                                                      | 132 ms: 1.42x faster                                                        |
| pickle_pure_python       | 270 us                                                      | 193 us: 1.40x faster                                                        |
| crypto_pyaes             | 62.5 ms                                                     | 45.7 ms: 1.37x faster                                                       |
| regex_compile            | 106 ms                                                      | 77.5 ms: 1.37x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 541 ms: 1.35x faster                                                        |
| nbody                    | 71.3 ms                                                     | 53.1 ms: 1.34x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 34.2 ms: 1.30x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 38.9 ms: 1.30x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 15.3 ms: 1.29x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.73 us: 1.27x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.15 ms: 1.27x faster                                                       |
| thrift                   | 617 us                                                      | 491 us: 1.26x faster                                                        |
| sympy_sum                | 107 ms                                                      | 85.1 ms: 1.26x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.53 us: 1.25x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 12.4 ms: 1.23x faster                                                       |
| django_template          | 28.9 ms                                                     | 23.7 ms: 1.22x faster                                                       |
| fannkuch                 | 256 ms                                                      | 210 ms: 1.22x faster                                                        |
| unpack_sequence          | 39.6 ns                                                     | 32.6 ns: 1.22x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 64.0 ms: 1.21x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 34.3 ms: 1.19x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.62 sec: 1.18x faster                                                      |
| regex_dna                | 136 ms                                                      | 117 ms: 1.16x faster                                                        |
| bench_thread_pool        | 958 us                                                      | 826 us: 1.16x faster                                                        |
| 2to3                     | 246 ms                                                      | 213 ms: 1.16x faster                                                        |
| xml_etree_iterparse      | 65.0 ms                                                     | 56.6 ms: 1.15x faster                                                       |
| sympy_str                | 194 ms                                                      | 170 ms: 1.15x faster                                                        |
| xml_etree_generate       | 55.5 ms                                                     | 48.6 ms: 1.14x faster                                                       |
| coroutines               | 16.0 ms                                                     | 14.0 ms: 1.14x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 85.3 ms: 1.13x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 59.4 ms: 1.12x faster                                                       |
| sympy_expand             | 314 ms                                                      | 284 ms: 1.11x faster                                                        |
| regex_v8                 | 15.4 ms                                                     | 14.0 ms: 1.10x faster                                                       |
| unpickle                 | 9.09 us                                                     | 8.28 us: 1.10x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 69.3 ms: 1.10x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.36 us: 1.06x faster                                                       |
| logging_simple           | 6.22 us                                                     | 5.86 us: 1.06x faster                                                       |
| json                     | 3.14 ms                                                     | 3.00 ms: 1.05x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                                       |
| pidigits                 | 149 ms                                                      | 147 ms: 1.02x faster                                                        |
| telco                    | 3.94 ms                                                     | 3.88 ms: 1.02x faster                                                       |
| json_loads               | 14.0 us                                                     | 13.9 us: 1.01x faster                                                       |
| unpickle_list            | 2.71 us                                                     | 2.75 us: 1.01x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.35 us: 1.07x slower                                                       |
| async_generators         | 222 ms                                                      | 243 ms: 1.09x slower                                                        |
| pickle_dict              | 17.2 us                                                     | 19.3 us: 1.12x slower                                                       |
| pickle_list              | 2.75 us                                                     | 3.25 us: 1.18x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 19.0 ms: 1.22x slower                                                       |
| python_startup           | 20.6 ms                                                     | 25.4 ms: 1.23x slower                                                       |
| coverage                 | 39.0 ms                                                     | 48.6 ms: 1.25x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 88.6 ms: 1.43x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.12 ms: 1.51x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.29 ms: 1.61x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.33x faster                                                                |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20251101-3.15.0a1+-2f60b8f-JIT/bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.366x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: unknown