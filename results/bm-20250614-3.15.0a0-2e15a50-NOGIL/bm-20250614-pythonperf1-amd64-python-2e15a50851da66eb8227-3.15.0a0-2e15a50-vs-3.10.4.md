# Results vs. 3.10.4

- fork: python
- ref: 2e15a50851da66eb8227
- machine: windows-amd64
- commit hash: 2e15a50
- commit date: 2025-06-14
- overall geometric mean: 1.309x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.40x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 337 ms: 1.37x slower                                                       |
| docutils       | 1.92 sec                                                    | 4.15 sec: 2.16x slower                                                     |
| html5lib       | 51.0 ms                                                     | 63.8 ms: 1.25x slower                                                      |
| Geometric mean | (ref)                                                       | 1.55x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 580 ms: 1.91x faster                                                       |
| async_tree_none         | 435 ms                                                      | 273 ms: 1.60x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 332 ms: 1.58x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 480 ms: 1.33x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.59x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 149 ms                                                      | 140 ms: 1.06x faster                                                       |
| float          | 61.7 ms                                                     | 98.6 ms: 1.60x slower                                                      |
| nbody          | 71.3 ms                                                     | 176 ms: 2.47x slower                                                       |
| Geometric mean | (ref)                                                       | 1.55x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 114 ms: 1.20x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.82 ms: 1.10x slower                                                      |
| regex_v8       | 15.4 ms                                                     | 17.0 ms: 1.10x slower                                                      |
| regex_compile  | 106 ms                                                      | 160 ms: 1.51x slower                                                       |
| Geometric mean | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 9.45 ms: 1.03x slower                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 112 ms: 1.16x slower                                                       |
| unpickle_list        | 2.71 us                                                     | 3.44 us: 1.27x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 22.0 us: 1.28x slower                                                      |
| unpickle             | 9.09 us                                                     | 12.2 us: 1.34x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.75 us: 1.36x slower                                                      |
| pickle               | 6.85 us                                                     | 9.80 us: 1.43x slower                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 93.0 ms: 1.43x slower                                                      |
| json_loads           | 14.0 us                                                     | 22.5 us: 1.60x slower                                                      |
| pickle_pure_python   | 270 us                                                      | 455 us: 1.69x slower                                                       |
| xml_etree_process    | 44.5 ms                                                     | 78.8 ms: 1.77x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 107 ms: 1.92x slower                                                       |
| unpickle_pure_python | 183 us                                                      | 357 us: 1.95x slower                                                       |
| tomli_loads          | 1.67 sec                                                    | 5.02 sec: 3.00x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.53x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 20.2 ms: 1.30x slower                                                      |
| python_startup         | 20.6 ms                                                     | 27.5 ms: 1.33x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.32x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 28.9 ms                                                     | 45.3 ms: 1.57x slower                                                      |
| genshi_xml      | 41.0 ms                                                     | 66.0 ms: 1.61x slower                                                      |
| genshi_text     | 19.8 ms                                                     | 33.4 ms: 1.69x slower                                                      |
| mako            | 9.03 ms                                                     | 16.4 ms: 1.81x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.67x slower                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                  | 75.7 ms                                                     | 35.8 ms: 2.11x faster                                                      |
| async_tree_io            | 1.11 sec                                                    | 580 ms: 1.91x faster                                                       |
| typing_runtime_protocols | 336 us                                                      | 198 us: 1.69x faster                                                       |
| async_tree_none          | 435 ms                                                      | 273 ms: 1.60x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 332 ms: 1.58x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 519 ms: 1.41x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 480 ms: 1.33x faster                                                       |
| pylint                   | 350 ms                                                      | 279 ms: 1.25x faster                                                       |
| regex_dna                | 136 ms                                                      | 114 ms: 1.20x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.68 us: 1.14x faster                                                      |
| pidigits                 | 149 ms                                                      | 140 ms: 1.06x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 9.45 ms: 1.03x slower                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.82 ms: 1.10x slower                                                      |
| regex_v8                 | 15.4 ms                                                     | 17.0 ms: 1.10x slower                                                      |
| dulwich_log              | 50.5 ms                                                     | 56.2 ms: 1.11x slower                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 112 ms: 1.16x slower                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 2.46 sec: 1.17x slower                                                     |
| html5lib                 | 51.0 ms                                                     | 63.8 ms: 1.25x slower                                                      |
| mdp                      | 1.78 sec                                                    | 2.23 sec: 1.25x slower                                                     |
| gc_traversal             | 1.41 ms                                                     | 1.79 ms: 1.27x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 3.44 us: 1.27x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 22.0 us: 1.28x slower                                                      |
| generators               | 32.4 ms                                                     | 41.8 ms: 1.29x slower                                                      |
| deepcopy                 | 255 us                                                      | 332 us: 1.30x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 20.2 ms: 1.30x slower                                                      |
| bench_thread_pool        | 958 us                                                      | 1.25 ms: 1.30x slower                                                      |
| sympy_sum                | 107 ms                                                      | 142 ms: 1.33x slower                                                       |
| python_startup           | 20.6 ms                                                     | 27.5 ms: 1.33x slower                                                      |
| json                     | 3.14 ms                                                     | 4.18 ms: 1.33x slower                                                      |
| unpickle                 | 9.09 us                                                     | 12.2 us: 1.34x slower                                                      |
| thrift                   | 617 us                                                      | 836 us: 1.35x slower                                                       |
| pickle_list              | 2.75 us                                                     | 3.75 us: 1.36x slower                                                      |
| 2to3                     | 246 ms                                                      | 337 ms: 1.37x slower                                                       |
| sympy_integrate          | 15.3 ms                                                     | 21.0 ms: 1.37x slower                                                      |
| go                       | 139 ms                                                      | 191 ms: 1.37x slower                                                       |
| deltablue                | 4.19 ms                                                     | 5.89 ms: 1.41x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.13 ms: 1.41x slower                                                      |
| pickle                   | 6.85 us                                                     | 9.80 us: 1.43x slower                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 93.0 ms: 1.43x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 89.5 ms: 1.44x slower                                                      |
| sympy_str                | 194 ms                                                      | 291 ms: 1.50x slower                                                       |
| raytrace                 | 273 ms                                                      | 409 ms: 1.50x slower                                                       |
| deepcopy_memo            | 28.8 us                                                     | 43.2 us: 1.50x slower                                                      |
| pyflate                  | 409 ms                                                      | 617 ms: 1.51x slower                                                       |
| regex_compile            | 106 ms                                                      | 160 ms: 1.51x slower                                                       |
| richards_super           | 52.2 ms                                                     | 79.2 ms: 1.52x slower                                                      |
| comprehensions           | 16.5 us                                                     | 25.4 us: 1.54x slower                                                      |
| chaos                    | 61.7 ms                                                     | 95.4 ms: 1.55x slower                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 3.41 us: 1.55x slower                                                      |
| django_template          | 28.9 ms                                                     | 45.3 ms: 1.57x slower                                                      |
| sympy_expand             | 314 ms                                                      | 494 ms: 1.57x slower                                                       |
| meteor_contest           | 75.9 ms                                                     | 119 ms: 1.57x slower                                                       |
| float                    | 61.7 ms                                                     | 98.6 ms: 1.60x slower                                                      |
| json_loads               | 14.0 us                                                     | 22.5 us: 1.60x slower                                                      |
| genshi_xml               | 41.0 ms                                                     | 66.0 ms: 1.61x slower                                                      |
| richards                 | 42.4 ms                                                     | 69.7 ms: 1.64x slower                                                      |
| genshi_text              | 19.8 ms                                                     | 33.4 ms: 1.69x slower                                                      |
| pickle_pure_python       | 270 us                                                      | 455 us: 1.69x slower                                                       |
| logging_format           | 6.76 us                                                     | 11.5 us: 1.70x slower                                                      |
| scimark_sor              | 106 ms                                                      | 187 ms: 1.76x slower                                                       |
| logging_simple           | 6.22 us                                                     | 11.0 us: 1.77x slower                                                      |
| xml_etree_process        | 44.5 ms                                                     | 78.8 ms: 1.77x slower                                                      |
| mako                     | 9.03 ms                                                     | 16.4 ms: 1.81x slower                                                      |
| pycparser                | 930 ms                                                      | 1.70 sec: 1.83x slower                                                     |
| async_generators         | 222 ms                                                      | 407 ms: 1.84x slower                                                       |
| hexiom                   | 5.74 ms                                                     | 10.6 ms: 1.84x slower                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 107 ms: 1.86x slower                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 118 ms: 1.88x slower                                                       |
| nqueens                  | 66.6 ms                                                     | 126 ms: 1.90x slower                                                       |
| scimark_lu               | 85.8 ms                                                     | 163 ms: 1.90x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 107 ms: 1.92x slower                                                       |
| unpickle_pure_python     | 183 us                                                      | 357 us: 1.95x slower                                                       |
| telco                    | 3.94 ms                                                     | 7.95 ms: 2.02x slower                                                      |
| unpack_sequence          | 39.6 ns                                                     | 80.2 ns: 2.02x slower                                                      |
| coroutines               | 16.0 ms                                                     | 32.8 ms: 2.05x slower                                                      |
| coverage                 | 39.0 ms                                                     | 83.7 ms: 2.15x slower                                                      |
| spectral_norm            | 77.3 ms                                                     | 166 ms: 2.15x slower                                                       |
| docutils                 | 1.92 sec                                                    | 4.15 sec: 2.16x slower                                                     |
| scimark_fft              | 187 ms                                                      | 412 ms: 2.20x slower                                                       |
| fannkuch                 | 256 ms                                                      | 581 ms: 2.27x slower                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 6.39 ms: 2.34x slower                                                      |
| pprint_safe_repr         | 592 ms                                                      | 1.40 sec: 2.37x slower                                                     |
| nbody                    | 71.3 ms                                                     | 176 ms: 2.47x slower                                                       |
| tomli_loads              | 1.67 sec                                                    | 5.02 sec: 3.00x slower                                                     |
| pprint_pformat           | 1.22 sec                                                    | 4.05 sec: 3.32x slower                                                     |
| logging_silent           | 94.6 ns                                                     | 583 ns: 6.16x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.46x slower                                                               |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250614-3.15.0a0-2e15a50-NOGIL/bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.309x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.47x
- 95% likely to have a slowdown of 1.44x
- 99% likely to have a slowdown of 1.40x

# Memory
- memory change: unknown