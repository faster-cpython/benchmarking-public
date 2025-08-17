# Results vs. 3.10.4

- fork: python
- ref: 3663b2ad54c9e15775a6
- machine: windows-amd64
- commit hash: 3663b2a
- commit date: 2025-08-16
- overall geometric mean: 1.335x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 217 ms: 1.13x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.62 sec: 1.19x faster                                                     |
| html5lib       | 51.0 ms                                                     | 38.4 ms: 1.33x faster                                                      |
| Geometric mean | (ref)                                                       | 1.21x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 382 ms: 2.90x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 201 ms: 2.62x faster                                                       |
| async_tree_none         | 435 ms                                                      | 172 ms: 2.53x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 330 ms: 1.94x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.47x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 43.7 ms: 1.41x faster                                                      |
| nbody          | 71.3 ms                                                     | 57.5 ms: 1.24x faster                                                      |
| pidigits       | 149 ms                                                      | 143 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.22x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 78.0 ms: 1.36x faster                                                      |
| regex_dna      | 136 ms                                                      | 118 ms: 1.16x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 13.7 ms: 1.13x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.60 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                       | 1.17x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 104 us: 1.76x faster                                                       |
| json_dumps           | 9.16 ms                                                     | 5.42 ms: 1.69x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.12 sec: 1.50x faster                                                     |
| pickle_pure_python   | 270 us                                                      | 200 us: 1.35x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 35.3 ms: 1.26x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 85.3 ms: 1.14x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 50.0 ms: 1.11x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.43 us: 1.08x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 61.8 ms: 1.05x faster                                                      |
| unpickle_list        | 2.71 us                                                     | 2.76 us: 1.02x slower                                                      |
| pickle               | 6.85 us                                                     | 7.60 us: 1.11x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 19.2 us: 1.12x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.23 us: 1.17x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.15x faster                                                               |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.1 ms: 1.22x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 19.0 ms: 1.23x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.22x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.28 ms: 1.71x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.5 ms: 1.28x faster                                                      |
| django_template | 28.9 ms                                                     | 24.0 ms: 1.20x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 34.6 ms: 1.18x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.33x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 103 us: 3.27x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 382 ms: 2.90x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 201 ms: 2.62x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 29.2 ms: 2.59x faster                                                      |
| async_tree_none          | 435 ms                                                      | 172 ms: 2.53x faster                                                       |
| mdp                      | 1.78 sec                                                    | 809 ms: 2.20x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 330 ms: 1.94x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.25 ms: 1.86x faster                                                      |
| go                       | 139 ms                                                      | 76.7 ms: 1.81x faster                                                      |
| pylint                   | 350 ms                                                      | 195 ms: 1.80x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 104 us: 1.76x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 54.9 ns: 1.72x faster                                                      |
| mako                     | 9.03 ms                                                     | 5.28 ms: 1.71x faster                                                      |
| richards_super           | 52.2 ms                                                     | 30.6 ms: 1.71x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.42 ms: 1.69x faster                                                      |
| generators               | 32.4 ms                                                     | 19.4 ms: 1.67x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 18.0 us: 1.60x faster                                                      |
| richards                 | 42.4 ms                                                     | 27.0 ms: 1.57x faster                                                      |
| comprehensions           | 16.5 us                                                     | 10.5 us: 1.57x faster                                                      |
| chaos                    | 61.7 ms                                                     | 39.7 ms: 1.56x faster                                                      |
| pyflate                  | 409 ms                                                      | 265 ms: 1.54x faster                                                       |
| raytrace                 | 273 ms                                                      | 179 ms: 1.52x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.39 sec: 1.52x faster                                                     |
| deepcopy                 | 255 us                                                      | 169 us: 1.51x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.12 sec: 1.50x faster                                                     |
| scimark_lu               | 85.8 ms                                                     | 57.7 ms: 1.49x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 497 ms: 1.47x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 3.99 ms: 1.44x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.3 ms: 1.42x faster                                                      |
| float                    | 61.7 ms                                                     | 43.7 ms: 1.41x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 44.9 ms: 1.39x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 884 ms: 1.38x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 435 ms: 1.36x faster                                                       |
| regex_compile            | 106 ms                                                      | 78.0 ms: 1.36x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 200 us: 1.35x faster                                                       |
| pycparser                | 930 ms                                                      | 691 ms: 1.35x faster                                                       |
| scimark_sor              | 106 ms                                                      | 79.6 ms: 1.33x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 38.4 ms: 1.33x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 39.0 ms: 1.29x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 15.5 ms: 1.28x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.52 us: 1.26x faster                                                      |
| scimark_fft              | 187 ms                                                      | 149 ms: 1.26x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 35.3 ms: 1.26x faster                                                      |
| thrift                   | 617 us                                                      | 491 us: 1.26x faster                                                       |
| sympy_sum                | 107 ms                                                      | 85.6 ms: 1.25x faster                                                      |
| nbody                    | 71.3 ms                                                     | 57.5 ms: 1.24x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 12.4 ms: 1.23x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 63.1 ms: 1.22x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.24 ms: 1.22x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.82 us: 1.21x faster                                                      |
| unpack_sequence          | 39.6 ns                                                     | 32.7 ns: 1.21x faster                                                      |
| fannkuch                 | 256 ms                                                      | 211 ms: 1.21x faster                                                       |
| django_template          | 28.9 ms                                                     | 24.0 ms: 1.20x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.62 sec: 1.19x faster                                                     |
| genshi_xml               | 41.0 ms                                                     | 34.6 ms: 1.18x faster                                                      |
| regex_dna                | 136 ms                                                      | 118 ms: 1.16x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 829 us: 1.16x faster                                                       |
| sympy_str                | 194 ms                                                      | 170 ms: 1.15x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 85.3 ms: 1.14x faster                                                      |
| 2to3                     | 246 ms                                                      | 217 ms: 1.13x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 13.7 ms: 1.13x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.2 ms: 1.13x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 50.0 ms: 1.11x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 69.1 ms: 1.10x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 60.9 ms: 1.09x faster                                                      |
| sympy_expand             | 314 ms                                                      | 288 ms: 1.09x faster                                                       |
| json                     | 3.14 ms                                                     | 2.90 ms: 1.08x faster                                                      |
| unpickle                 | 9.09 us                                                     | 8.43 us: 1.08x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 61.8 ms: 1.05x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.45 us: 1.05x faster                                                      |
| pidigits                 | 149 ms                                                      | 143 ms: 1.04x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.60 ms: 1.04x faster                                                      |
| unpickle_list            | 2.71 us                                                     | 2.76 us: 1.02x slower                                                      |
| async_generators         | 222 ms                                                      | 245 ms: 1.11x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.60 us: 1.11x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 19.2 us: 1.12x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.23 us: 1.17x slower                                                      |
| python_startup           | 20.6 ms                                                     | 25.1 ms: 1.22x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.0 ms: 1.23x slower                                                      |
| coverage                 | 39.0 ms                                                     | 48.4 ms: 1.24x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 92.4 ms: 1.49x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.17 ms: 1.54x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.29 ms: 1.61x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.30x faster                                                               |

Benchmark hidden because not significant (3): logging_simple, telco, json_loads
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250816-3.15.0a0-3663b2a-JIT/bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.335x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: unknown