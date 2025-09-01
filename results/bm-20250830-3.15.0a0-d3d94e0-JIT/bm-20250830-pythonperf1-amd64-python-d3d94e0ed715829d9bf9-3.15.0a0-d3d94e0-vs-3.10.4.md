# Results vs. 3.10.4

- fork: python
- ref: d3d94e0ed715829d9bf9
- machine: windows-amd64
- commit hash: d3d94e0
- commit date: 2025-08-30
- overall geometric mean: 1.342x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 218 ms: 1.13x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.62 sec: 1.18x faster                                                     |
| html5lib       | 51.0 ms                                                     | 37.5 ms: 1.36x faster                                                      |
| Geometric mean | (ref)                                                       | 1.22x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 386 ms: 2.87x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 200 ms: 2.63x faster                                                       |
| async_tree_none         | 435 ms                                                      | 171 ms: 2.55x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 330 ms: 1.93x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.47x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 42.8 ms: 1.44x faster                                                      |
| nbody          | 71.3 ms                                                     | 52.3 ms: 1.36x faster                                                      |
| pidigits       | 149 ms                                                      | 144 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.27x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 78.3 ms: 1.35x faster                                                      |
| regex_dna      | 136 ms                                                      | 118 ms: 1.15x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 13.7 ms: 1.13x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.52 ms: 1.09x faster                                                      |
| Geometric mean | (ref)                                                       | 1.18x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 105 us: 1.75x faster                                                       |
| json_dumps           | 9.16 ms                                                     | 5.48 ms: 1.67x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.09 sec: 1.53x faster                                                     |
| pickle_pure_python   | 270 us                                                      | 203 us: 1.33x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 35.1 ms: 1.27x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 49.6 ms: 1.12x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 87.8 ms: 1.10x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.38 us: 1.09x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.0 ms: 1.05x faster                                                      |
| pickle               | 6.85 us                                                     | 7.53 us: 1.10x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 19.3 us: 1.12x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.19 us: 1.16x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.15x faster                                                               |

Benchmark hidden because not significant (2): unpickle_list, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.3 ms: 1.25x slower                                                      |
| python_startup         | 20.6 ms                                                     | 25.8 ms: 1.25x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.25 ms: 1.72x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.3 ms: 1.29x faster                                                      |
| django_template | 28.9 ms                                                     | 23.8 ms: 1.21x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 34.0 ms: 1.21x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.34x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 103 us: 3.25x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 386 ms: 2.87x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 200 ms: 2.63x faster                                                       |
| async_tree_none          | 435 ms                                                      | 171 ms: 2.55x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 29.7 ms: 2.55x faster                                                      |
| mdp                      | 1.78 sec                                                    | 783 ms: 2.27x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 330 ms: 1.93x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.21 ms: 1.90x faster                                                      |
| pylint                   | 350 ms                                                      | 193 ms: 1.82x faster                                                       |
| go                       | 139 ms                                                      | 77.4 ms: 1.79x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 54.1 ns: 1.75x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 105 us: 1.75x faster                                                       |
| mako                     | 9.03 ms                                                     | 5.25 ms: 1.72x faster                                                      |
| richards_super           | 52.2 ms                                                     | 30.9 ms: 1.69x faster                                                      |
| generators               | 32.4 ms                                                     | 19.2 ms: 1.69x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.48 ms: 1.67x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 455 ms: 1.61x faster                                                       |
| comprehensions           | 16.5 us                                                     | 10.3 us: 1.60x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.32 sec: 1.59x faster                                                     |
| raytrace                 | 273 ms                                                      | 172 ms: 1.59x faster                                                       |
| pyflate                  | 409 ms                                                      | 260 ms: 1.57x faster                                                       |
| richards                 | 42.4 ms                                                     | 27.1 ms: 1.56x faster                                                      |
| chaos                    | 61.7 ms                                                     | 40.2 ms: 1.53x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.09 sec: 1.53x faster                                                     |
| deepcopy_memo            | 28.8 us                                                     | 19.1 us: 1.51x faster                                                      |
| deepcopy                 | 255 us                                                      | 170 us: 1.50x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 58.2 ms: 1.47x faster                                                      |
| float                    | 61.7 ms                                                     | 42.8 ms: 1.44x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 849 ms: 1.44x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.2 ms: 1.42x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 424 ms: 1.40x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 44.9 ms: 1.39x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.13 ms: 1.39x faster                                                      |
| nbody                    | 71.3 ms                                                     | 52.3 ms: 1.36x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 37.5 ms: 1.36x faster                                                      |
| scimark_sor              | 106 ms                                                      | 78.2 ms: 1.36x faster                                                      |
| regex_compile            | 106 ms                                                      | 78.3 ms: 1.35x faster                                                      |
| pycparser                | 930 ms                                                      | 693 ms: 1.34x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 203 us: 1.33x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 38.7 ms: 1.30x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 15.3 ms: 1.29x faster                                                      |
| scimark_fft              | 187 ms                                                      | 146 ms: 1.28x faster                                                       |
| sympy_sum                | 107 ms                                                      | 84.4 ms: 1.27x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 35.1 ms: 1.27x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.53 us: 1.25x faster                                                      |
| thrift                   | 617 us                                                      | 495 us: 1.25x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 62.1 ms: 1.24x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.23 ms: 1.22x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 12.5 ms: 1.22x faster                                                      |
| django_template          | 28.9 ms                                                     | 23.8 ms: 1.21x faster                                                      |
| fannkuch                 | 256 ms                                                      | 211 ms: 1.21x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 34.0 ms: 1.21x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.83 us: 1.20x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.62 sec: 1.18x faster                                                     |
| sympy_str                | 194 ms                                                      | 166 ms: 1.17x faster                                                       |
| unpack_sequence          | 39.6 ns                                                     | 34.2 ns: 1.16x faster                                                      |
| regex_dna                | 136 ms                                                      | 118 ms: 1.15x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 838 us: 1.14x faster                                                       |
| coroutines               | 16.0 ms                                                     | 14.0 ms: 1.14x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 13.7 ms: 1.13x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 59.1 ms: 1.13x faster                                                      |
| 2to3                     | 246 ms                                                      | 218 ms: 1.13x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 49.6 ms: 1.12x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 87.8 ms: 1.10x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.52 ms: 1.09x faster                                                      |
| json                     | 3.14 ms                                                     | 2.88 ms: 1.09x faster                                                      |
| unpickle                 | 9.09 us                                                     | 8.38 us: 1.09x faster                                                      |
| sympy_expand             | 314 ms                                                      | 291 ms: 1.08x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 71.1 ms: 1.07x faster                                                      |
| telco                    | 3.94 ms                                                     | 3.75 ms: 1.05x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.0 ms: 1.05x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.46 us: 1.05x faster                                                      |
| pidigits                 | 149 ms                                                      | 144 ms: 1.04x faster                                                       |
| logging_simple           | 6.22 us                                                     | 6.01 us: 1.04x faster                                                      |
| async_generators         | 222 ms                                                      | 242 ms: 1.09x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.53 us: 1.10x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 19.3 us: 1.12x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.19 us: 1.16x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.3 ms: 1.25x slower                                                      |
| python_startup           | 20.6 ms                                                     | 25.8 ms: 1.25x slower                                                      |
| coverage                 | 39.0 ms                                                     | 49.3 ms: 1.26x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.11 ms: 1.50x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 93.3 ms: 1.50x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.28 ms: 1.60x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.31x faster                                                               |

Benchmark hidden because not significant (2): unpickle_list, json_loads
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250830-3.15.0a0-d3d94e0-JIT/bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.342x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: unknown