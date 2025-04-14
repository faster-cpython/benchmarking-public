# Results vs. 3.10.4

- fork: python
- ref: 425f60b9eb253c57bc32
- machine: windows-amd64
- commit hash: 425f60b
- commit date: 2025-03-29
- overall geometric mean: 1.264x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 220 ms: 1.12x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.65 sec: 1.16x faster                                                      |
| html5lib       | 51.0 ms                                                     | 39.0 ms: 1.31x faster                                                       |
| Geometric mean | (ref)                                                       | 1.19x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 416 ms: 2.66x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 216 ms: 2.44x faster                                                        |
| async_tree_none         | 435 ms                                                      | 185 ms: 2.35x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 337 ms: 1.90x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.32x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 44.7 ms: 1.38x faster                                                       |
| nbody          | 71.3 ms                                                     | 64.2 ms: 1.11x faster                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 82.3 ms: 1.29x faster                                                       |
| regex_dna      | 136 ms                                                      | 114 ms: 1.19x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.39 ms: 1.19x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 13.4 ms: 1.15x faster                                                       |
| Geometric mean | (ref)                                                       | 1.21x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.78 ms: 1.35x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 140 us: 1.31x faster                                                        |
| pickle_pure_python   | 270 us                                                      | 216 us: 1.25x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.41 sec: 1.18x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 87.6 ms: 1.10x faster                                                       |
| unpickle             | 9.09 us                                                     | 8.27 us: 1.10x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 40.9 ms: 1.09x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 64.1 ms: 1.01x faster                                                       |
| unpickle_list        | 2.71 us                                                     | 2.76 us: 1.02x slower                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 57.2 ms: 1.03x slower                                                       |
| json_loads           | 14.0 us                                                     | 15.1 us: 1.08x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 21.3 us: 1.24x slower                                                       |
| pickle               | 6.85 us                                                     | 8.52 us: 1.24x slower                                                       |
| pickle_list          | 2.75 us                                                     | 3.58 us: 1.30x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.8 ms: 1.25x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 20.4 ms: 1.32x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.29x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.71 ms: 1.35x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 15.8 ms: 1.25x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 34.2 ms: 1.20x faster                                                       |
| django_template | 28.9 ms                                                     | 25.4 ms: 1.14x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.23x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 107 us: 3.13x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 416 ms: 2.66x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 216 ms: 2.44x faster                                                        |
| async_tree_none          | 435 ms                                                      | 185 ms: 2.35x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 32.5 ms: 2.33x faster                                                       |
| mdp                      | 1.78 sec                                                    | 799 ms: 2.23x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.12 ms: 1.98x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 337 ms: 1.90x faster                                                        |
| generators               | 32.4 ms                                                     | 17.9 ms: 1.81x faster                                                       |
| pylint                   | 350 ms                                                      | 200 ms: 1.75x faster                                                        |
| go                       | 139 ms                                                      | 80.8 ms: 1.72x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 56.3 ns: 1.68x faster                                                       |
| richards_super           | 52.2 ms                                                     | 31.5 ms: 1.66x faster                                                       |
| chaos                    | 61.7 ms                                                     | 40.2 ms: 1.54x faster                                                       |
| richards                 | 42.4 ms                                                     | 27.8 ms: 1.52x faster                                                       |
| raytrace                 | 273 ms                                                      | 181 ms: 1.51x faster                                                        |
| deepcopy_memo            | 28.8 us                                                     | 19.1 us: 1.51x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.43 sec: 1.47x faster                                                      |
| comprehensions           | 16.5 us                                                     | 11.5 us: 1.44x faster                                                       |
| deepcopy                 | 255 us                                                      | 180 us: 1.42x faster                                                        |
| asyncio_tcp              | 732 ms                                                      | 520 ms: 1.41x faster                                                        |
| pyflate                  | 409 ms                                                      | 291 ms: 1.40x faster                                                        |
| spectral_norm            | 77.3 ms                                                     | 55.1 ms: 1.40x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.12 ms: 1.39x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 61.6 ms: 1.39x faster                                                       |
| scimark_sor              | 106 ms                                                      | 76.7 ms: 1.38x faster                                                       |
| float                    | 61.7 ms                                                     | 44.7 ms: 1.38x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.78 ms: 1.35x faster                                                       |
| mako                     | 9.03 ms                                                     | 6.71 ms: 1.35x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 47.3 ms: 1.32x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 43.5 ms: 1.32x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 140 us: 1.31x faster                                                        |
| html5lib                 | 51.0 ms                                                     | 39.0 ms: 1.31x faster                                                       |
| regex_compile            | 106 ms                                                      | 82.3 ms: 1.29x faster                                                       |
| pycparser                | 930 ms                                                      | 728 ms: 1.28x faster                                                        |
| genshi_text              | 19.8 ms                                                     | 15.8 ms: 1.25x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 216 us: 1.25x faster                                                        |
| sqlite_synth             | 1.91 us                                                     | 1.58 us: 1.21x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 34.2 ms: 1.20x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 42.1 ms: 1.20x faster                                                       |
| sympy_sum                | 107 ms                                                      | 89.6 ms: 1.19x faster                                                       |
| regex_dna                | 136 ms                                                      | 114 ms: 1.19x faster                                                        |
| coroutines               | 16.0 ms                                                     | 13.4 ms: 1.19x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.39 ms: 1.19x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 12.9 ms: 1.19x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.41 sec: 1.18x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.88 us: 1.17x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.65 sec: 1.16x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 13.4 ms: 1.15x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.07 sec: 1.14x faster                                                      |
| django_template          | 28.9 ms                                                     | 25.4 ms: 1.14x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 521 ms: 1.14x faster                                                        |
| 2to3                     | 246 ms                                                      | 220 ms: 1.12x faster                                                        |
| nbody                    | 71.3 ms                                                     | 64.2 ms: 1.11x faster                                                       |
| sympy_str                | 194 ms                                                      | 175 ms: 1.11x faster                                                        |
| bench_thread_pool        | 958 us                                                      | 864 us: 1.11x faster                                                        |
| xml_etree_parse          | 96.8 ms                                                     | 87.6 ms: 1.10x faster                                                       |
| unpickle                 | 9.09 us                                                     | 8.27 us: 1.10x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 40.9 ms: 1.09x faster                                                       |
| unpack_sequence          | 39.6 ns                                                     | 37.0 ns: 1.07x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 63.5 ms: 1.05x faster                                                       |
| sympy_expand             | 314 ms                                                      | 301 ms: 1.05x faster                                                        |
| json                     | 3.14 ms                                                     | 3.09 ms: 1.02x faster                                                       |
| scimark_fft              | 187 ms                                                      | 185 ms: 1.02x faster                                                        |
| xml_etree_iterparse      | 65.0 ms                                                     | 64.1 ms: 1.01x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.69 ms: 1.01x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 76.2 ms: 1.00x slower                                                       |
| async_generators         | 222 ms                                                      | 223 ms: 1.01x slower                                                        |
| logging_format           | 6.76 us                                                     | 6.88 us: 1.02x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 2.76 us: 1.02x slower                                                       |
| fannkuch                 | 256 ms                                                      | 260 ms: 1.02x slower                                                        |
| logging_simple           | 6.22 us                                                     | 6.39 us: 1.03x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 57.2 ms: 1.03x slower                                                       |
| json_loads               | 14.0 us                                                     | 15.1 us: 1.08x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.87 ms: 1.24x slower                                                       |
| coverage                 | 39.0 ms                                                     | 48.3 ms: 1.24x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 21.3 us: 1.24x slower                                                       |
| pickle                   | 6.85 us                                                     | 8.52 us: 1.24x slower                                                       |
| python_startup           | 20.6 ms                                                     | 25.8 ms: 1.25x slower                                                       |
| pickle_list              | 2.75 us                                                     | 3.58 us: 1.30x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 20.4 ms: 1.32x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 88.9 ms: 1.43x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.08 ms: 1.47x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.25 ms: 1.56x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.23x faster                                                                |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (16) of results/bm-20250329-3.14.0a6+-425f60b/bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.264x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: unknown