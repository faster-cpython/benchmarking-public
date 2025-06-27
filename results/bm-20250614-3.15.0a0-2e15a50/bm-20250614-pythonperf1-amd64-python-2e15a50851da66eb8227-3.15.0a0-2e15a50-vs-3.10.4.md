# Results vs. 3.10.4

- fork: python
- ref: 2e15a50851da66eb8227
- machine: windows-amd64
- commit hash: 2e15a50
- commit date: 2025-06-14
- overall geometric mean: 1.285x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 220 ms: 1.12x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.63 sec: 1.18x faster                                                     |
| html5lib       | 51.0 ms                                                     | 38.5 ms: 1.32x faster                                                      |
| Geometric mean | (ref)                                                       | 1.20x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 396 ms: 2.80x faster                                                       |
| async_tree_none         | 435 ms                                                      | 169 ms: 2.57x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 206 ms: 2.55x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 330 ms: 1.93x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.44x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 43.4 ms: 1.42x faster                                                      |
| nbody          | 71.3 ms                                                     | 61.6 ms: 1.16x faster                                                      |
| pidigits       | 149 ms                                                      | 146 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.19x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 80.5 ms: 1.32x faster                                                      |
| regex_dna      | 136 ms                                                      | 115 ms: 1.18x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 13.2 ms: 1.17x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.51 ms: 1.10x faster                                                      |
| Geometric mean | (ref)                                                       | 1.19x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.20 ms: 1.48x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 132 us: 1.39x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 208 us: 1.29x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.37 sec: 1.22x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 39.1 ms: 1.14x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 88.2 ms: 1.10x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 64.1 ms: 1.01x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.2 us: 1.02x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 56.7 ms: 1.02x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.17x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.4 ms: 1.25x slower                                                      |
| python_startup         | 20.6 ms                                                     | 26.1 ms: 1.27x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.68 ms: 1.35x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.2 ms: 1.30x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 34.2 ms: 1.20x faster                                                      |
| django_template | 28.9 ms                                                     | 24.2 ms: 1.19x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.26x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 103 us: 3.27x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 396 ms: 2.80x faster                                                       |
| async_tree_none          | 435 ms                                                      | 169 ms: 2.57x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 206 ms: 2.55x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 32.0 ms: 2.37x faster                                                      |
| mdp                      | 1.78 sec                                                    | 804 ms: 2.21x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.14 ms: 1.95x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 330 ms: 1.93x faster                                                       |
| go                       | 139 ms                                                      | 74.7 ms: 1.86x faster                                                      |
| pylint                   | 350 ms                                                      | 199 ms: 1.76x faster                                                       |
| richards_super           | 52.2 ms                                                     | 30.6 ms: 1.71x faster                                                      |
| generators               | 32.4 ms                                                     | 19.4 ms: 1.67x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 18.0 us: 1.59x faster                                                      |
| richards                 | 42.4 ms                                                     | 26.9 ms: 1.58x faster                                                      |
| comprehensions           | 16.5 us                                                     | 10.6 us: 1.55x faster                                                      |
| chaos                    | 61.7 ms                                                     | 39.9 ms: 1.55x faster                                                      |
| raytrace                 | 273 ms                                                      | 183 ms: 1.49x faster                                                       |
| deepcopy                 | 255 us                                                      | 171 us: 1.49x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.20 ms: 1.48x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 58.1 ms: 1.48x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 3.95 ms: 1.45x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 39.9 ms: 1.44x faster                                                      |
| float                    | 61.7 ms                                                     | 43.4 ms: 1.42x faster                                                      |
| scimark_sor              | 106 ms                                                      | 74.8 ms: 1.42x faster                                                      |
| pyflate                  | 409 ms                                                      | 291 ms: 1.41x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 132 us: 1.39x faster                                                       |
| mako                     | 9.03 ms                                                     | 6.68 ms: 1.35x faster                                                      |
| pycparser                | 930 ms                                                      | 700 ms: 1.33x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 47.1 ms: 1.33x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 38.5 ms: 1.32x faster                                                      |
| regex_compile            | 106 ms                                                      | 80.5 ms: 1.32x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 15.2 ms: 1.30x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 208 us: 1.29x faster                                                       |
| thrift                   | 617 us                                                      | 491 us: 1.26x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 61.8 ms: 1.25x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 12.3 ms: 1.24x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.37 sec: 1.22x faster                                                     |
| sympy_sum                | 107 ms                                                      | 87.8 ms: 1.22x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 41.5 ms: 1.22x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.58 us: 1.21x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.83 us: 1.20x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 34.2 ms: 1.20x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.2 ms: 1.19x faster                                                      |
| regex_dna                | 136 ms                                                      | 115 ms: 1.18x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.63 sec: 1.18x faster                                                     |
| regex_v8                 | 15.4 ms                                                     | 13.2 ms: 1.17x faster                                                      |
| nbody                    | 71.3 ms                                                     | 61.6 ms: 1.16x faster                                                      |
| sympy_str                | 194 ms                                                      | 168 ms: 1.16x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 39.1 ms: 1.14x faster                                                      |
| 2to3                     | 246 ms                                                      | 220 ms: 1.12x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.09 sec: 1.12x faster                                                     |
| coroutines               | 16.0 ms                                                     | 14.4 ms: 1.11x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.51 ms: 1.10x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 88.2 ms: 1.10x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 544 ms: 1.09x faster                                                       |
| sympy_expand             | 314 ms                                                      | 289 ms: 1.09x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 61.3 ms: 1.09x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.51 ms: 1.09x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 72.5 ms: 1.05x faster                                                      |
| json                     | 3.14 ms                                                     | 3.01 ms: 1.04x faster                                                      |
| scimark_fft              | 187 ms                                                      | 183 ms: 1.02x faster                                                       |
| pidigits                 | 149 ms                                                      | 146 ms: 1.02x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 64.1 ms: 1.01x faster                                                      |
| fannkuch                 | 256 ms                                                      | 253 ms: 1.01x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.85 us: 1.01x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.2 us: 1.02x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 56.7 ms: 1.02x slower                                                      |
| async_generators         | 222 ms                                                      | 227 ms: 1.02x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.41 us: 1.03x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.61 ms: 1.17x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.4 ms: 1.25x slower                                                      |
| python_startup           | 20.6 ms                                                     | 26.1 ms: 1.27x slower                                                      |
| coverage                 | 39.0 ms                                                     | 52.5 ms: 1.35x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.15 ms: 1.53x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.34 ms: 1.68x slower                                                      |
| logging_silent           | 94.6 ns                                                     | 320 ns: 3.38x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.26x faster                                                               |
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250614-3.15.0a0-2e15a50/bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.285x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: unknown