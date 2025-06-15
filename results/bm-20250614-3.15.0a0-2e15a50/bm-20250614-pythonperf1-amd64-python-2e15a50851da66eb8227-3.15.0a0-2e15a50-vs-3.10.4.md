# Results vs. 3.10.4

- fork: python
- ref: 2e15a50851da66eb8227
- machine: windows-amd64
- commit hash: 2e15a50
- commit date: 2025-06-14
- overall geometric mean: 1.217x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 296 ms: 1.20x slower                                                       |
| docutils       | 1.92 sec                                                    | 2.10 sec: 1.09x slower                                                     |
| Geometric mean | (ref)                                                       | 1.10x slower                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 547 ms: 2.03x faster                                                       |
| async_tree_none         | 435 ms                                                      | 243 ms: 1.79x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 296 ms: 1.78x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 442 ms: 1.44x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.75x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 149 ms                                                      | 147 ms: 1.02x faster                                                       |
| float          | 61.7 ms                                                     | 76.8 ms: 1.24x slower                                                      |
| nbody          | 71.3 ms                                                     | 107 ms: 1.50x slower                                                       |
| Geometric mean | (ref)                                                       | 1.22x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 117 ms: 1.17x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.73 ms: 1.04x slower                                                      |
| regex_v8       | 15.4 ms                                                     | 17.0 ms: 1.10x slower                                                      |
| regex_compile  | 106 ms                                                      | 124 ms: 1.17x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 8.45 ms: 1.08x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 108 ms: 1.12x slower                                                       |
| unpickle_list        | 2.71 us                                                     | 3.11 us: 1.14x slower                                                      |
| tomli_loads          | 1.67 sec                                                    | 2.08 sec: 1.25x slower                                                     |
| unpickle             | 9.09 us                                                     | 11.3 us: 1.25x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 22.6 us: 1.32x slower                                                      |
| pickle_pure_python   | 270 us                                                      | 363 us: 1.35x slower                                                       |
| pickle               | 6.85 us                                                     | 9.60 us: 1.40x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.86 us: 1.40x slower                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 91.6 ms: 1.41x slower                                                      |
| json_loads           | 14.0 us                                                     | 20.5 us: 1.46x slower                                                      |
| xml_etree_process    | 44.5 ms                                                     | 65.7 ms: 1.48x slower                                                      |
| unpickle_pure_python | 183 us                                                      | 279 us: 1.52x slower                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 91.2 ms: 1.64x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.32x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 20.0 ms: 1.29x slower                                                      |
| python_startup         | 20.6 ms                                                     | 27.0 ms: 1.31x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.30x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 41.0 ms                                                     | 50.0 ms: 1.22x slower                                                      |
| genshi_text     | 19.8 ms                                                     | 24.3 ms: 1.23x slower                                                      |
| django_template | 28.9 ms                                                     | 37.3 ms: 1.29x slower                                                      |
| mako            | 9.03 ms                                                     | 13.1 ms: 1.44x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.29x slower                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                  | 75.7 ms                                                     | 34.3 ms: 2.20x faster                                                      |
| typing_runtime_protocols | 336 us                                                      | 155 us: 2.16x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 547 ms: 2.03x faster                                                       |
| async_tree_none          | 435 ms                                                      | 243 ms: 1.79x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 296 ms: 1.78x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 459 ms: 1.59x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.17 sec: 1.52x faster                                                     |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.39 sec: 1.52x faster                                                     |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 442 ms: 1.44x faster                                                       |
| pylint                   | 350 ms                                                      | 248 ms: 1.41x faster                                                       |
| regex_dna                | 136 ms                                                      | 117 ms: 1.17x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 8.45 ms: 1.08x faster                                                      |
| go                       | 139 ms                                                      | 134 ms: 1.04x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.85 us: 1.03x faster                                                      |
| pidigits                 | 149 ms                                                      | 147 ms: 1.02x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 52.1 ms: 1.03x slower                                                      |
| deepcopy                 | 255 us                                                      | 267 us: 1.04x slower                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.73 ms: 1.04x slower                                                      |
| deltablue                | 4.19 ms                                                     | 4.38 ms: 1.05x slower                                                      |
| bench_thread_pool        | 958 us                                                      | 1.01 ms: 1.05x slower                                                      |
| pycparser                | 930 ms                                                      | 988 ms: 1.06x slower                                                       |
| chaos                    | 61.7 ms                                                     | 65.8 ms: 1.07x slower                                                      |
| sympy_sum                | 107 ms                                                      | 116 ms: 1.08x slower                                                       |
| docutils                 | 1.92 sec                                                    | 2.10 sec: 1.09x slower                                                     |
| sympy_integrate          | 15.3 ms                                                     | 16.7 ms: 1.09x slower                                                      |
| regex_v8                 | 15.4 ms                                                     | 17.0 ms: 1.10x slower                                                      |
| raytrace                 | 273 ms                                                      | 303 ms: 1.11x slower                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 108 ms: 1.12x slower                                                       |
| richards_super           | 52.2 ms                                                     | 58.7 ms: 1.12x slower                                                      |
| generators               | 32.4 ms                                                     | 36.4 ms: 1.13x slower                                                      |
| pyflate                  | 409 ms                                                      | 462 ms: 1.13x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 3.11 us: 1.14x slower                                                      |
| regex_compile            | 106 ms                                                      | 124 ms: 1.17x slower                                                       |
| deepcopy_memo            | 28.8 us                                                     | 33.6 us: 1.17x slower                                                      |
| comprehensions           | 16.5 us                                                     | 19.8 us: 1.20x slower                                                      |
| sympy_str                | 194 ms                                                      | 234 ms: 1.20x slower                                                       |
| 2to3                     | 246 ms                                                      | 296 ms: 1.20x slower                                                       |
| genshi_xml               | 41.0 ms                                                     | 50.0 ms: 1.22x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 93.2 ms: 1.23x slower                                                      |
| genshi_text              | 19.8 ms                                                     | 24.3 ms: 1.23x slower                                                      |
| richards                 | 42.4 ms                                                     | 52.3 ms: 1.23x slower                                                      |
| float                    | 61.7 ms                                                     | 76.8 ms: 1.24x slower                                                      |
| tomli_loads              | 1.67 sec                                                    | 2.08 sec: 1.25x slower                                                     |
| unpickle                 | 9.09 us                                                     | 11.3 us: 1.25x slower                                                      |
| scimark_sor              | 106 ms                                                      | 133 ms: 1.26x slower                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 2.78 us: 1.26x slower                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 79.8 ms: 1.28x slower                                                      |
| sympy_expand             | 314 ms                                                      | 402 ms: 1.28x slower                                                       |
| json                     | 3.14 ms                                                     | 4.01 ms: 1.28x slower                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 73.9 ms: 1.29x slower                                                      |
| django_template          | 28.9 ms                                                     | 37.3 ms: 1.29x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 20.0 ms: 1.29x slower                                                      |
| hexiom                   | 5.74 ms                                                     | 7.46 ms: 1.30x slower                                                      |
| python_startup           | 20.6 ms                                                     | 27.0 ms: 1.31x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 22.6 us: 1.32x slower                                                      |
| pickle_pure_python       | 270 us                                                      | 363 us: 1.35x slower                                                       |
| pickle                   | 6.85 us                                                     | 9.60 us: 1.40x slower                                                      |
| scimark_lu               | 85.8 ms                                                     | 120 ms: 1.40x slower                                                       |
| pickle_list              | 2.75 us                                                     | 3.86 us: 1.40x slower                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 91.6 ms: 1.41x slower                                                      |
| nqueens                  | 66.6 ms                                                     | 94.5 ms: 1.42x slower                                                      |
| spectral_norm            | 77.3 ms                                                     | 111 ms: 1.44x slower                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.76 sec: 1.44x slower                                                     |
| mako                     | 9.03 ms                                                     | 13.1 ms: 1.44x slower                                                      |
| pprint_safe_repr         | 592 ms                                                      | 856 ms: 1.45x slower                                                       |
| json_loads               | 14.0 us                                                     | 20.5 us: 1.46x slower                                                      |
| logging_format           | 6.76 us                                                     | 9.91 us: 1.47x slower                                                      |
| xml_etree_process        | 44.5 ms                                                     | 65.7 ms: 1.48x slower                                                      |
| scimark_fft              | 187 ms                                                      | 277 ms: 1.48x slower                                                       |
| nbody                    | 71.3 ms                                                     | 107 ms: 1.50x slower                                                       |
| logging_simple           | 6.22 us                                                     | 9.42 us: 1.51x slower                                                      |
| unpickle_pure_python     | 183 us                                                      | 279 us: 1.52x slower                                                       |
| async_generators         | 222 ms                                                      | 341 ms: 1.54x slower                                                       |
| telco                    | 3.94 ms                                                     | 6.26 ms: 1.59x slower                                                      |
| fannkuch                 | 256 ms                                                      | 413 ms: 1.61x slower                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 4.41 ms: 1.62x slower                                                      |
| coroutines               | 16.0 ms                                                     | 26.1 ms: 1.63x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 91.2 ms: 1.64x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 104 ms: 1.68x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.45 ms: 1.81x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.93 ms: 2.08x slower                                                      |
| unpack_sequence          | 39.6 ns                                                     | 83.6 ns: 2.11x slower                                                      |
| logging_silent           | 94.6 ns                                                     | 501 ns: 5.30x slower                                                       |
| coverage                 | 39.0 ms                                                     | 471 ms: 12.08x slower                                                      |
| thrift                   | 617 us                                                      | 103 ms: 166.27x slower                                                     |
| Geometric mean           | (ref)                                                       | 1.29x slower                                                               |

Benchmark hidden because not significant (1): html5lib
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250614-3.15.0a0-2e15a50/bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.217x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.15x
- 95% likely to have a slowdown of 1.13x
- 99% likely to have a slowdown of 1.10x

# Memory
- memory change: unknown