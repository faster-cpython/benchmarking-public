# Results vs. 3.10.4

- fork: python
- ref: 7363e8d24d14abf65163
- machine: windows-amd64
- commit hash: 7363e8d
- commit date: 2025-05-03
- overall geometric mean: 1.170x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.05x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 227 ms: 1.08x faster                                                        |
| docutils       | 1.92 sec                                                    | 2.98 sec: 1.55x slower                                                      |
| html5lib       | 51.0 ms                                                     | 39.8 ms: 1.28x faster                                                       |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 354 ms: 3.13x faster                                                        |
| async_tree_none         | 435 ms                                                      | 169 ms: 2.57x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 209 ms: 2.51x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 332 ms: 1.92x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.50x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 45.3 ms: 1.36x faster                                                       |
| pidigits       | 149 ms                                                      | 139 ms: 1.07x faster                                                        |
| nbody          | 71.3 ms                                                     | 78.9 ms: 1.11x slower                                                       |
| Geometric mean | (ref)                                                       | 1.10x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 113 ms: 1.20x faster                                                        |
| regex_v8       | 15.4 ms                                                     | 13.1 ms: 1.17x faster                                                       |
| regex_compile  | 106 ms                                                      | 90.8 ms: 1.17x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 7.22 ms: 1.27x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 148 us: 1.24x faster                                                        |
| pickle_pure_python   | 270 us                                                      | 223 us: 1.21x faster                                                        |
| xml_etree_iterparse  | 65.0 ms                                                     | 58.4 ms: 1.11x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 90.6 ms: 1.07x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 43.3 ms: 1.03x faster                                                       |
| unpickle             | 9.09 us                                                     | 9.83 us: 1.08x slower                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 60.7 ms: 1.09x slower                                                       |
| json_loads           | 14.0 us                                                     | 17.0 us: 1.21x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 20.9 us: 1.22x slower                                                       |
| pickle_list          | 2.75 us                                                     | 3.39 us: 1.23x slower                                                       |
| pickle               | 6.85 us                                                     | 8.47 us: 1.24x slower                                                       |
| unpickle_list        | 2.71 us                                                     | 3.38 us: 1.25x slower                                                       |
| tomli_loads          | 1.67 sec                                                    | 2.59 sec: 1.55x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.06x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.8 ms: 1.25x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 19.5 ms: 1.25x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 28.9 ms                                                     | 26.2 ms: 1.10x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 37.9 ms: 1.08x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 18.7 ms: 1.06x faster                                                       |
| mako            | 9.03 ms                                                     | 9.76 ms: 1.08x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.04x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io            | 1.11 sec                                                    | 354 ms: 3.13x faster                                                        |
| typing_runtime_protocols | 336 us                                                      | 130 us: 2.58x faster                                                        |
| async_tree_none          | 435 ms                                                      | 169 ms: 2.57x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 209 ms: 2.51x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 32.2 ms: 2.35x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 332 ms: 1.92x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.36 ms: 1.78x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.08 sec: 1.65x faster                                                      |
| pylint                   | 350 ms                                                      | 213 ms: 1.64x faster                                                        |
| logging_silent           | 94.6 ns                                                     | 59.5 ns: 1.59x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 485 ms: 1.51x faster                                                        |
| go                       | 139 ms                                                      | 92.6 ms: 1.50x faster                                                       |
| generators               | 32.4 ms                                                     | 22.1 ms: 1.47x faster                                                       |
| chaos                    | 61.7 ms                                                     | 43.2 ms: 1.43x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.37 us: 1.40x faster                                                       |
| richards_super           | 52.2 ms                                                     | 37.5 ms: 1.39x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 20.7 us: 1.39x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 62.2 ms: 1.38x faster                                                       |
| float                    | 61.7 ms                                                     | 45.3 ms: 1.36x faster                                                       |
| raytrace                 | 273 ms                                                      | 203 ms: 1.35x faster                                                        |
| deepcopy                 | 255 us                                                      | 192 us: 1.33x faster                                                        |
| richards                 | 42.4 ms                                                     | 32.2 ms: 1.32x faster                                                       |
| pycparser                | 930 ms                                                      | 719 ms: 1.29x faster                                                        |
| comprehensions           | 16.5 us                                                     | 12.8 us: 1.29x faster                                                       |
| pyflate                  | 409 ms                                                      | 318 ms: 1.29x faster                                                        |
| html5lib                 | 51.0 ms                                                     | 39.8 ms: 1.28x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.52 ms: 1.27x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 7.22 ms: 1.27x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 148 us: 1.24x faster                                                        |
| scimark_sor              | 106 ms                                                      | 85.8 ms: 1.24x faster                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.14 ms: 1.24x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.2 ms: 1.21x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 223 us: 1.21x faster                                                        |
| regex_dna                | 136 ms                                                      | 113 ms: 1.20x faster                                                        |
| dulwich_log              | 50.5 ms                                                     | 42.4 ms: 1.19x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 48.3 ms: 1.19x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 13.1 ms: 1.17x faster                                                       |
| regex_compile            | 106 ms                                                      | 90.8 ms: 1.17x faster                                                       |
| sympy_sum                | 107 ms                                                      | 94.8 ms: 1.13x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 68.5 ms: 1.13x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 58.4 ms: 1.11x faster                                                       |
| django_template          | 28.9 ms                                                     | 26.2 ms: 1.10x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.9 ms: 1.10x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 57.1 ms: 1.10x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 37.9 ms: 1.08x faster                                                       |
| 2to3                     | 246 ms                                                      | 227 ms: 1.08x faster                                                        |
| deepcopy_reduce          | 2.20 us                                                     | 2.04 us: 1.08x faster                                                       |
| thrift                   | 617 us                                                      | 573 us: 1.08x faster                                                        |
| pidigits                 | 149 ms                                                      | 139 ms: 1.07x faster                                                        |
| xml_etree_parse          | 96.8 ms                                                     | 90.6 ms: 1.07x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 18.7 ms: 1.06x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                       |
| sympy_str                | 194 ms                                                      | 186 ms: 1.04x faster                                                        |
| pprint_safe_repr         | 592 ms                                                      | 569 ms: 1.04x faster                                                        |
| xml_etree_process        | 44.5 ms                                                     | 43.3 ms: 1.03x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.89 us: 1.02x slower                                                       |
| json                     | 3.14 ms                                                     | 3.21 ms: 1.02x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.41 us: 1.03x slower                                                       |
| nqueens                  | 66.6 ms                                                     | 69.2 ms: 1.04x slower                                                       |
| scimark_fft              | 187 ms                                                      | 196 ms: 1.05x slower                                                        |
| unpack_sequence          | 39.6 ns                                                     | 42.6 ns: 1.08x slower                                                       |
| mako                     | 9.03 ms                                                     | 9.76 ms: 1.08x slower                                                       |
| unpickle                 | 9.09 us                                                     | 9.83 us: 1.08x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 60.7 ms: 1.09x slower                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.98 ms: 1.09x slower                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 2.33 sec: 1.11x slower                                                      |
| nbody                    | 71.3 ms                                                     | 78.9 ms: 1.11x slower                                                       |
| bench_thread_pool        | 958 us                                                      | 1.10 ms: 1.15x slower                                                       |
| fannkuch                 | 256 ms                                                      | 295 ms: 1.15x slower                                                        |
| meteor_contest           | 75.9 ms                                                     | 88.8 ms: 1.17x slower                                                       |
| async_generators         | 222 ms                                                      | 264 ms: 1.19x slower                                                        |
| json_loads               | 14.0 us                                                     | 17.0 us: 1.21x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 20.9 us: 1.22x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 982 us: 1.23x slower                                                        |
| pickle_list              | 2.75 us                                                     | 3.39 us: 1.23x slower                                                       |
| pickle                   | 6.85 us                                                     | 8.47 us: 1.24x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 76.7 ms: 1.24x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 3.38 us: 1.25x slower                                                       |
| python_startup           | 20.6 ms                                                     | 25.8 ms: 1.25x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 19.5 ms: 1.25x slower                                                       |
| telco                    | 3.94 ms                                                     | 5.17 ms: 1.31x slower                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.85 sec: 1.52x slower                                                      |
| tomli_loads              | 1.67 sec                                                    | 2.59 sec: 1.55x slower                                                      |
| docutils                 | 1.92 sec                                                    | 2.98 sec: 1.55x slower                                                      |
| coverage                 | 39.0 ms                                                     | 67.2 ms: 1.72x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.13x faster                                                                |

Benchmark hidden because not significant (1): sympy_expand
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250503-3.14.0a7+-7363e8d-NOGIL/bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.170x faster

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: unknown