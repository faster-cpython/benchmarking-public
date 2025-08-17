# Results vs. 3.10.4

- fork: python
- ref: 3663b2ad54c9e15775a6
- machine: windows-amd64
- commit hash: 3663b2a
- commit date: 2025-08-16
- overall geometric mean: 1.299x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 215 ms: 1.14x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.60 sec: 1.20x faster                                                     |
| html5lib       | 51.0 ms                                                     | 37.6 ms: 1.36x faster                                                      |
| Geometric mean | (ref)                                                       | 1.23x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 388 ms: 2.86x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 201 ms: 2.62x faster                                                       |
| async_tree_none         | 435 ms                                                      | 171 ms: 2.55x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 327 ms: 1.95x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.47x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 44.2 ms: 1.39x faster                                                      |
| nbody          | 71.3 ms                                                     | 63.6 ms: 1.12x faster                                                      |
| pidigits       | 149 ms                                                      | 145 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 78.8 ms: 1.35x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 13.9 ms: 1.11x faster                                                      |
| regex_dna      | 136 ms                                                      | 124 ms: 1.09x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                      |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.43 ms: 1.69x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 132 us: 1.38x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 212 us: 1.27x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.38 sec: 1.21x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 39.2 ms: 1.13x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 87.0 ms: 1.11x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.39 us: 1.08x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.5 ms: 1.02x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 56.3 ms: 1.01x slower                                                      |
| json_loads           | 14.0 us                                                     | 14.3 us: 1.02x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 2.82 us: 1.04x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 19.7 us: 1.15x slower                                                      |
| pickle               | 6.85 us                                                     | 8.25 us: 1.20x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.38 us: 1.23x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.08x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.3 ms: 1.23x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 19.2 ms: 1.24x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.23x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.64 ms: 1.36x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.3 ms: 1.30x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 33.4 ms: 1.23x faster                                                      |
| django_template | 28.9 ms                                                     | 24.3 ms: 1.19x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.27x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 106 us: 3.18x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 388 ms: 2.86x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 28.7 ms: 2.63x faster                                                      |
| async_tree_memoization   | 526 ms                                                      | 201 ms: 2.62x faster                                                       |
| async_tree_none          | 435 ms                                                      | 171 ms: 2.55x faster                                                       |
| mdp                      | 1.78 sec                                                    | 794 ms: 2.24x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 327 ms: 1.95x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.18 ms: 1.92x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 380 ms: 1.92x faster                                                       |
| go                       | 139 ms                                                      | 75.3 ms: 1.85x faster                                                      |
| pylint                   | 350 ms                                                      | 195 ms: 1.80x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 55.0 ns: 1.72x faster                                                      |
| richards_super           | 52.2 ms                                                     | 30.5 ms: 1.71x faster                                                      |
| generators               | 32.4 ms                                                     | 18.9 ms: 1.71x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.25 sec: 1.69x faster                                                     |
| json_dumps               | 9.16 ms                                                     | 5.43 ms: 1.69x faster                                                      |
| richards                 | 42.4 ms                                                     | 26.8 ms: 1.58x faster                                                      |
| raytrace                 | 273 ms                                                      | 174 ms: 1.57x faster                                                       |
| chaos                    | 61.7 ms                                                     | 39.5 ms: 1.56x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 55.8 ms: 1.54x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 18.7 us: 1.54x faster                                                      |
| comprehensions           | 16.5 us                                                     | 10.9 us: 1.51x faster                                                      |
| deepcopy                 | 255 us                                                      | 170 us: 1.50x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 39.5 ms: 1.45x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 3.99 ms: 1.44x faster                                                      |
| pyflate                  | 409 ms                                                      | 293 ms: 1.40x faster                                                       |
| float                    | 61.7 ms                                                     | 44.2 ms: 1.39x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 132 us: 1.38x faster                                                       |
| scimark_sor              | 106 ms                                                      | 77.0 ms: 1.38x faster                                                      |
| mako                     | 9.03 ms                                                     | 6.64 ms: 1.36x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 37.6 ms: 1.36x faster                                                      |
| regex_compile            | 106 ms                                                      | 78.8 ms: 1.35x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 47.7 ms: 1.31x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 15.3 ms: 1.30x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 39.0 ms: 1.29x faster                                                      |
| pycparser                | 930 ms                                                      | 723 ms: 1.29x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 212 us: 1.27x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 12.2 ms: 1.26x faster                                                      |
| thrift                   | 617 us                                                      | 494 us: 1.25x faster                                                       |
| sympy_sum                | 107 ms                                                      | 85.8 ms: 1.25x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.55 us: 1.24x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 33.4 ms: 1.23x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 994 ms: 1.23x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 489 ms: 1.21x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.38 sec: 1.21x faster                                                     |
| deepcopy_reduce          | 2.20 us                                                     | 1.83 us: 1.20x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.60 sec: 1.20x faster                                                     |
| spectral_norm            | 77.3 ms                                                     | 64.5 ms: 1.20x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.3 ms: 1.19x faster                                                      |
| sympy_str                | 194 ms                                                      | 166 ms: 1.17x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 835 us: 1.15x faster                                                       |
| 2to3                     | 246 ms                                                      | 215 ms: 1.14x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 39.2 ms: 1.13x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.2 ms: 1.13x faster                                                      |
| nbody                    | 71.3 ms                                                     | 63.6 ms: 1.12x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 13.9 ms: 1.11x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 87.0 ms: 1.11x faster                                                      |
| sympy_expand             | 314 ms                                                      | 283 ms: 1.11x faster                                                       |
| regex_dna                | 136 ms                                                      | 124 ms: 1.09x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 61.1 ms: 1.09x faster                                                      |
| unpickle                 | 9.09 us                                                     | 8.39 us: 1.08x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.53 ms: 1.08x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 70.8 ms: 1.07x faster                                                      |
| json                     | 3.14 ms                                                     | 2.95 ms: 1.06x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.37 us: 1.06x faster                                                      |
| scimark_fft              | 187 ms                                                      | 177 ms: 1.06x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                      |
| logging_simple           | 6.22 us                                                     | 5.93 us: 1.05x faster                                                      |
| pidigits                 | 149 ms                                                      | 145 ms: 1.03x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.5 ms: 1.02x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 56.3 ms: 1.01x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.3 us: 1.02x slower                                                      |
| unpack_sequence          | 39.6 ns                                                     | 40.5 ns: 1.02x slower                                                      |
| async_generators         | 222 ms                                                      | 227 ms: 1.02x slower                                                       |
| fannkuch                 | 256 ms                                                      | 263 ms: 1.03x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 2.82 us: 1.04x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.38 ms: 1.11x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 19.7 us: 1.15x slower                                                      |
| pickle                   | 6.85 us                                                     | 8.25 us: 1.20x slower                                                      |
| python_startup           | 20.6 ms                                                     | 25.3 ms: 1.23x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.38 us: 1.23x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.2 ms: 1.24x slower                                                      |
| coverage                 | 39.0 ms                                                     | 51.0 ms: 1.31x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 92.2 ms: 1.49x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.13 ms: 1.51x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.28 ms: 1.61x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.27x faster                                                               |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250816-3.15.0a0-3663b2a/bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.299x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: unknown