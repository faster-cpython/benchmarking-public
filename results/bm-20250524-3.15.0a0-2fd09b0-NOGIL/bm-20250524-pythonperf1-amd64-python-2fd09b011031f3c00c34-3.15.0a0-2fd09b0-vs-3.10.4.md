# Results vs. 3.10.4

- fork: python
- ref: 2fd09b011031f3c00c34
- machine: windows-amd64
- commit hash: 2fd09b0
- commit date: 2025-05-24
- overall geometric mean: 1.147x faster
- HPT reliability: 99.67%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 226 ms: 1.09x faster                                                       |
| docutils       | 1.92 sec                                                    | 2.93 sec: 1.53x slower                                                     |
| html5lib       | 51.0 ms                                                     | 40.7 ms: 1.26x faster                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 351 ms: 3.16x faster                                                       |
| async_tree_none         | 435 ms                                                      | 172 ms: 2.53x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 212 ms: 2.48x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 331 ms: 1.93x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.49x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 46.2 ms: 1.34x faster                                                      |
| pidigits       | 149 ms                                                      | 135 ms: 1.10x faster                                                       |
| nbody          | 71.3 ms                                                     | 81.6 ms: 1.14x slower                                                      |
| Geometric mean | (ref)                                                       | 1.09x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 114 ms: 1.19x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 13.3 ms: 1.16x faster                                                      |
| regex_compile  | 106 ms                                                      | 95.8 ms: 1.11x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.54 ms: 1.07x faster                                                      |
| Geometric mean | (ref)                                                       | 1.13x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.72 ms: 1.36x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 153 us: 1.20x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 232 us: 1.16x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 57.4 ms: 1.13x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 90.3 ms: 1.07x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 45.1 ms: 1.02x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.03 us: 1.10x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 3.04 us: 1.12x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 63.6 ms: 1.15x slower                                                      |
| unpickle             | 9.09 us                                                     | 10.6 us: 1.16x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 20.1 us: 1.17x slower                                                      |
| pickle               | 6.85 us                                                     | 8.01 us: 1.17x slower                                                      |
| json_loads           | 14.0 us                                                     | 16.8 us: 1.20x slower                                                      |
| tomli_loads          | 1.67 sec                                                    | 2.68 sec: 1.60x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.05x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 18.4 ms: 1.19x slower                                                      |
| python_startup         | 20.6 ms                                                     | 24.6 ms: 1.19x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.19x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 28.9 ms                                                     | 27.5 ms: 1.05x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 40.4 ms: 1.01x faster                                                      |
| mako            | 9.03 ms                                                     | 9.66 ms: 1.07x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.00x faster                                                               |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io            | 1.11 sec                                                    | 351 ms: 3.16x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 29.8 ms: 2.54x faster                                                      |
| async_tree_none          | 435 ms                                                      | 172 ms: 2.53x faster                                                       |
| typing_runtime_protocols | 336 us                                                      | 133 us: 2.52x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 212 ms: 2.48x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 331 ms: 1.93x faster                                                       |
| pylint                   | 350 ms                                                      | 205 ms: 1.71x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.46 ms: 1.71x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 439 ms: 1.67x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.17 sec: 1.52x faster                                                     |
| go                       | 139 ms                                                      | 93.4 ms: 1.49x faster                                                      |
| generators               | 32.4 ms                                                     | 22.2 ms: 1.46x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.33 us: 1.43x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.72 ms: 1.36x faster                                                      |
| chaos                    | 61.7 ms                                                     | 45.4 ms: 1.36x faster                                                      |
| float                    | 61.7 ms                                                     | 46.2 ms: 1.34x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 64.6 ms: 1.33x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 21.8 us: 1.32x faster                                                      |
| richards_super           | 52.2 ms                                                     | 39.7 ms: 1.32x faster                                                      |
| pycparser                | 930 ms                                                      | 725 ms: 1.28x faster                                                       |
| pyflate                  | 409 ms                                                      | 320 ms: 1.28x faster                                                       |
| raytrace                 | 273 ms                                                      | 214 ms: 1.28x faster                                                       |
| comprehensions           | 16.5 us                                                     | 13.1 us: 1.26x faster                                                      |
| deepcopy                 | 255 us                                                      | 203 us: 1.26x faster                                                       |
| richards                 | 42.4 ms                                                     | 33.8 ms: 1.26x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 40.7 ms: 1.26x faster                                                      |
| scimark_sor              | 106 ms                                                      | 86.4 ms: 1.23x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.69 ms: 1.22x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 41.3 ms: 1.22x faster                                                      |
| coroutines               | 16.0 ms                                                     | 13.3 ms: 1.20x faster                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.17 ms: 1.20x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 153 us: 1.20x faster                                                       |
| regex_dna                | 136 ms                                                      | 114 ms: 1.19x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 13.3 ms: 1.16x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 232 us: 1.16x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 57.4 ms: 1.13x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 55.5 ms: 1.13x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 69.2 ms: 1.12x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 51.4 ms: 1.11x faster                                                      |
| regex_compile            | 106 ms                                                      | 95.8 ms: 1.11x faster                                                      |
| pidigits                 | 149 ms                                                      | 135 ms: 1.10x faster                                                       |
| sympy_sum                | 107 ms                                                      | 97.4 ms: 1.10x faster                                                      |
| 2to3                     | 246 ms                                                      | 226 ms: 1.09x faster                                                       |
| thrift                   | 617 us                                                      | 571 us: 1.08x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.54 ms: 1.07x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 14.2 ms: 1.07x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 90.3 ms: 1.07x faster                                                      |
| django_template          | 28.9 ms                                                     | 27.5 ms: 1.05x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 2.14 us: 1.03x faster                                                      |
| unpack_sequence          | 39.6 ns                                                     | 38.8 ns: 1.02x faster                                                      |
| sympy_str                | 194 ms                                                      | 190 ms: 1.02x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 40.4 ms: 1.01x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 45.1 ms: 1.02x slower                                                      |
| json                     | 3.14 ms                                                     | 3.24 ms: 1.03x slower                                                      |
| sympy_expand             | 314 ms                                                      | 326 ms: 1.04x slower                                                       |
| pprint_safe_repr         | 592 ms                                                      | 628 ms: 1.06x slower                                                       |
| nqueens                  | 66.6 ms                                                     | 70.8 ms: 1.06x slower                                                      |
| mako                     | 9.03 ms                                                     | 9.66 ms: 1.07x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.03 us: 1.10x slower                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 3.04 ms: 1.11x slower                                                      |
| scimark_fft              | 187 ms                                                      | 209 ms: 1.12x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 3.04 us: 1.12x slower                                                      |
| logging_format           | 6.76 us                                                     | 7.60 us: 1.12x slower                                                      |
| nbody                    | 71.3 ms                                                     | 81.6 ms: 1.14x slower                                                      |
| logging_simple           | 6.22 us                                                     | 7.12 us: 1.14x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 63.6 ms: 1.15x slower                                                      |
| fannkuch                 | 256 ms                                                      | 296 ms: 1.16x slower                                                       |
| unpickle                 | 9.09 us                                                     | 10.6 us: 1.16x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 88.3 ms: 1.16x slower                                                      |
| bench_thread_pool        | 958 us                                                      | 1.12 ms: 1.17x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 20.1 us: 1.17x slower                                                      |
| pickle                   | 6.85 us                                                     | 8.01 us: 1.17x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 18.4 ms: 1.19x slower                                                      |
| python_startup           | 20.6 ms                                                     | 24.6 ms: 1.19x slower                                                      |
| json_loads               | 14.0 us                                                     | 16.8 us: 1.20x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 75.7 ms: 1.22x slower                                                      |
| async_generators         | 222 ms                                                      | 273 ms: 1.23x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.00 ms: 1.26x slower                                                      |
| telco                    | 3.94 ms                                                     | 5.32 ms: 1.35x slower                                                      |
| docutils                 | 1.92 sec                                                    | 2.93 sec: 1.53x slower                                                     |
| tomli_loads              | 1.67 sec                                                    | 2.68 sec: 1.60x slower                                                     |
| coverage                 | 39.0 ms                                                     | 66.7 ms: 1.71x slower                                                      |
| pprint_pformat           | 1.22 sec                                                    | 2.13 sec: 1.74x slower                                                     |
| logging_silent           | 94.6 ns                                                     | 371 ns: 3.93x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.10x faster                                                               |

Benchmark hidden because not significant (2): genshi_text, asyncio_tcp_ssl
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250524-3.15.0a0-2fd09b0-NOGIL/bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.147x faster

# HPT report

- Reliability score: 99.67% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown