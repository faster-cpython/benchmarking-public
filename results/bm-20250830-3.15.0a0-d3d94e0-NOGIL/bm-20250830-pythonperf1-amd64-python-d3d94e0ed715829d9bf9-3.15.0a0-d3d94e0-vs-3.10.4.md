# Results vs. 3.10.4

- fork: python
- ref: d3d94e0ed715829d9bf9
- machine: windows-amd64
- commit hash: d3d94e0
- commit date: 2025-08-30
- overall geometric mean: 1.148x faster
- HPT reliability: 99.88%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 227 ms: 1.09x faster                                                       |
| docutils       | 1.92 sec                                                    | 2.87 sec: 1.49x slower                                                     |
| html5lib       | 51.0 ms                                                     | 40.7 ms: 1.25x faster                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 350 ms: 3.16x faster                                                       |
| async_tree_none         | 435 ms                                                      | 170 ms: 2.57x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 209 ms: 2.51x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 333 ms: 1.92x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.50x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 47.0 ms: 1.31x faster                                                      |
| pidigits       | 149 ms                                                      | 136 ms: 1.10x faster                                                       |
| nbody          | 71.3 ms                                                     | 82.6 ms: 1.16x slower                                                      |
| Geometric mean | (ref)                                                       | 1.08x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 115 ms: 1.18x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 13.2 ms: 1.17x faster                                                      |
| regex_compile  | 106 ms                                                      | 94.6 ms: 1.12x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                                      |
| Geometric mean | (ref)                                                       | 1.13x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.99 ms: 1.53x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 237 us: 1.14x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 161 us: 1.13x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 59.8 ms: 1.09x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 93.4 ms: 1.04x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 44.7 ms: 1.01x slower                                                      |
| pickle_list          | 2.75 us                                                     | 2.93 us: 1.06x slower                                                      |
| unpickle             | 9.09 us                                                     | 10.3 us: 1.14x slower                                                      |
| json_loads           | 14.0 us                                                     | 16.0 us: 1.14x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 63.5 ms: 1.14x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 3.13 us: 1.15x slower                                                      |
| pickle               | 6.85 us                                                     | 8.04 us: 1.17x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 21.6 us: 1.25x slower                                                      |
| tomli_loads          | 1.67 sec                                                    | 2.41 sec: 1.44x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.9 ms: 1.25x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 19.7 ms: 1.27x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 28.9 ms                                                     | 27.4 ms: 1.06x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 40.6 ms: 1.01x faster                                                      |
| mako            | 9.03 ms                                                     | 9.98 ms: 1.10x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io            | 1.11 sec                                                    | 350 ms: 3.16x faster                                                       |
| async_tree_none          | 435 ms                                                      | 170 ms: 2.57x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 209 ms: 2.51x faster                                                       |
| typing_runtime_protocols | 336 us                                                      | 134 us: 2.51x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 30.2 ms: 2.50x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 333 ms: 1.92x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.39 ms: 1.75x faster                                                      |
| pylint                   | 350 ms                                                      | 205 ms: 1.71x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.16 sec: 1.53x faster                                                     |
| json_dumps               | 9.16 ms                                                     | 5.99 ms: 1.53x faster                                                      |
| go                       | 139 ms                                                      | 92.7 ms: 1.50x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 63.1 ns: 1.50x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.35 us: 1.41x faster                                                      |
| generators               | 32.4 ms                                                     | 23.1 ms: 1.40x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 21.2 us: 1.36x faster                                                      |
| comprehensions           | 16.5 us                                                     | 12.3 us: 1.34x faster                                                      |
| chaos                    | 61.7 ms                                                     | 46.4 ms: 1.33x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 553 ms: 1.32x faster                                                       |
| richards_super           | 52.2 ms                                                     | 39.6 ms: 1.32x faster                                                      |
| float                    | 61.7 ms                                                     | 47.0 ms: 1.31x faster                                                      |
| pyflate                  | 409 ms                                                      | 312 ms: 1.31x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 65.9 ms: 1.30x faster                                                      |
| pycparser                | 930 ms                                                      | 715 ms: 1.30x faster                                                       |
| deepcopy                 | 255 us                                                      | 202 us: 1.26x faster                                                       |
| raytrace                 | 273 ms                                                      | 217 ms: 1.26x faster                                                       |
| richards                 | 42.4 ms                                                     | 33.8 ms: 1.26x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 40.7 ms: 1.25x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.71 ms: 1.22x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 42.0 ms: 1.20x faster                                                      |
| scimark_sor              | 106 ms                                                      | 88.4 ms: 1.20x faster                                                      |
| regex_dna                | 136 ms                                                      | 115 ms: 1.18x faster                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.20 ms: 1.18x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 13.2 ms: 1.17x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 237 us: 1.14x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 161 us: 1.13x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 51.0 ms: 1.12x faster                                                      |
| regex_compile            | 106 ms                                                      | 94.6 ms: 1.12x faster                                                      |
| sympy_sum                | 107 ms                                                      | 97.3 ms: 1.10x faster                                                      |
| pidigits                 | 149 ms                                                      | 136 ms: 1.10x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 57.0 ms: 1.10x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 59.8 ms: 1.09x faster                                                      |
| 2to3                     | 246 ms                                                      | 227 ms: 1.09x faster                                                       |
| thrift                   | 617 us                                                      | 570 us: 1.08x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 14.2 ms: 1.08x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 72.4 ms: 1.07x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                                      |
| django_template          | 28.9 ms                                                     | 27.4 ms: 1.06x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 564 ms: 1.05x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 93.4 ms: 1.04x faster                                                      |
| coroutines               | 16.0 ms                                                     | 15.5 ms: 1.03x faster                                                      |
| sympy_str                | 194 ms                                                      | 188 ms: 1.03x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 2.15 us: 1.02x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 40.6 ms: 1.01x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 44.7 ms: 1.01x slower                                                      |
| sympy_expand             | 314 ms                                                      | 321 ms: 1.02x slower                                                       |
| logging_format           | 6.76 us                                                     | 7.12 us: 1.05x slower                                                      |
| pickle_list              | 2.75 us                                                     | 2.93 us: 1.06x slower                                                      |
| logging_simple           | 6.22 us                                                     | 6.64 us: 1.07x slower                                                      |
| mako                     | 9.03 ms                                                     | 9.98 ms: 1.10x slower                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 2.36 sec: 1.12x slower                                                     |
| scimark_fft              | 187 ms                                                      | 210 ms: 1.12x slower                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 3.08 ms: 1.13x slower                                                      |
| nqueens                  | 66.6 ms                                                     | 75.8 ms: 1.14x slower                                                      |
| unpickle                 | 9.09 us                                                     | 10.3 us: 1.14x slower                                                      |
| json_loads               | 14.0 us                                                     | 16.0 us: 1.14x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 63.5 ms: 1.14x slower                                                      |
| bench_thread_pool        | 958 us                                                      | 1.10 ms: 1.15x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 3.13 us: 1.15x slower                                                      |
| async_generators         | 222 ms                                                      | 256 ms: 1.16x slower                                                       |
| nbody                    | 71.3 ms                                                     | 82.6 ms: 1.16x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 88.2 ms: 1.16x slower                                                      |
| pickle                   | 6.85 us                                                     | 8.04 us: 1.17x slower                                                      |
| fannkuch                 | 256 ms                                                      | 301 ms: 1.18x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 979 us: 1.22x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.87 ms: 1.24x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 21.6 us: 1.25x slower                                                      |
| python_startup           | 20.6 ms                                                     | 25.9 ms: 1.25x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.7 ms: 1.27x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 79.4 ms: 1.28x slower                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.71 sec: 1.40x slower                                                     |
| tomli_loads              | 1.67 sec                                                    | 2.41 sec: 1.44x slower                                                     |
| docutils                 | 1.92 sec                                                    | 2.87 sec: 1.49x slower                                                     |
| coverage                 | 39.0 ms                                                     | 66.8 ms: 1.71x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.12x faster                                                               |

Benchmark hidden because not significant (3): json, genshi_text, unpack_sequence
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250830-3.15.0a0-d3d94e0-NOGIL/bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.148x faster

# HPT report

- Reliability score: 99.88% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown