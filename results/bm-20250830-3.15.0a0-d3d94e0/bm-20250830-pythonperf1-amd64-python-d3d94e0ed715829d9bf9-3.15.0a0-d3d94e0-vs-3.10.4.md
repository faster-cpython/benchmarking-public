# Results vs. 3.10.4

- fork: python
- ref: d3d94e0ed715829d9bf9
- machine: windows-amd64
- commit hash: d3d94e0
- commit date: 2025-08-30
- overall geometric mean: 1.294x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 220 ms: 1.12x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.58 sec: 1.21x faster                                                     |
| html5lib       | 51.0 ms                                                     | 37.8 ms: 1.35x faster                                                      |
| Geometric mean | (ref)                                                       | 1.22x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 392 ms: 2.83x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 205 ms: 2.56x faster                                                       |
| async_tree_none         | 435 ms                                                      | 174 ms: 2.50x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 326 ms: 1.95x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.44x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 45.0 ms: 1.37x faster                                                      |
| nbody          | 71.3 ms                                                     | 65.3 ms: 1.09x faster                                                      |
| pidigits       | 149 ms                                                      | 146 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 78.9 ms: 1.34x faster                                                      |
| regex_dna      | 136 ms                                                      | 113 ms: 1.21x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 13.1 ms: 1.18x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.45 ms: 1.14x faster                                                      |
| Geometric mean | (ref)                                                       | 1.21x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.41 ms: 1.70x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 135 us: 1.36x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 212 us: 1.27x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.39 sec: 1.20x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 38.9 ms: 1.14x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 85.4 ms: 1.13x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.31 us: 1.09x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.5 ms: 1.02x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.1 us: 1.01x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 56.5 ms: 1.02x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 2.96 us: 1.09x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 19.1 us: 1.11x slower                                                      |
| pickle               | 6.85 us                                                     | 7.73 us: 1.13x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.26 us: 1.18x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.08x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.6 ms: 1.24x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 19.6 ms: 1.26x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.79 ms: 1.33x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.4 ms: 1.28x faster                                                      |
| django_template | 28.9 ms                                                     | 24.2 ms: 1.19x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 34.5 ms: 1.19x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.25x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 103 us: 3.25x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 392 ms: 2.83x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 205 ms: 2.56x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 29.7 ms: 2.54x faster                                                      |
| async_tree_none          | 435 ms                                                      | 174 ms: 2.50x faster                                                       |
| mdp                      | 1.78 sec                                                    | 793 ms: 2.24x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 326 ms: 1.95x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.18 ms: 1.92x faster                                                      |
| pylint                   | 350 ms                                                      | 192 ms: 1.82x faster                                                       |
| go                       | 139 ms                                                      | 77.1 ms: 1.80x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 420 ms: 1.74x faster                                                       |
| richards_super           | 52.2 ms                                                     | 30.8 ms: 1.70x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.41 ms: 1.70x faster                                                      |
| generators               | 32.4 ms                                                     | 19.2 ms: 1.69x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 56.4 ns: 1.68x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.28 sec: 1.64x faster                                                     |
| deepcopy_memo            | 28.8 us                                                     | 18.3 us: 1.57x faster                                                      |
| raytrace                 | 273 ms                                                      | 177 ms: 1.55x faster                                                       |
| richards                 | 42.4 ms                                                     | 27.8 ms: 1.52x faster                                                      |
| deepcopy                 | 255 us                                                      | 168 us: 1.52x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.0 us: 1.50x faster                                                      |
| chaos                    | 61.7 ms                                                     | 41.2 ms: 1.50x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 58.4 ms: 1.47x faster                                                      |
| pyflate                  | 409 ms                                                      | 287 ms: 1.43x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.7 ms: 1.41x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.11 ms: 1.40x faster                                                      |
| float                    | 61.7 ms                                                     | 45.0 ms: 1.37x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 135 us: 1.36x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 37.8 ms: 1.35x faster                                                      |
| scimark_sor              | 106 ms                                                      | 78.7 ms: 1.35x faster                                                      |
| regex_compile            | 106 ms                                                      | 78.9 ms: 1.34x faster                                                      |
| pycparser                | 930 ms                                                      | 693 ms: 1.34x faster                                                       |
| mako                     | 9.03 ms                                                     | 6.79 ms: 1.33x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 47.5 ms: 1.32x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 38.5 ms: 1.31x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 15.4 ms: 1.28x faster                                                      |
| thrift                   | 617 us                                                      | 484 us: 1.27x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 212 us: 1.27x faster                                                       |
| sympy_sum                | 107 ms                                                      | 85.2 ms: 1.26x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 12.2 ms: 1.25x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.80 us: 1.22x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.00 sec: 1.22x faster                                                     |
| sqlite_synth             | 1.91 us                                                     | 1.57 us: 1.21x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.58 sec: 1.21x faster                                                     |
| regex_dna                | 136 ms                                                      | 113 ms: 1.21x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.39 sec: 1.20x faster                                                     |
| pprint_safe_repr         | 592 ms                                                      | 495 ms: 1.20x faster                                                       |
| django_template          | 28.9 ms                                                     | 24.2 ms: 1.19x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 64.8 ms: 1.19x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 34.5 ms: 1.19x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 13.1 ms: 1.18x faster                                                      |
| sympy_str                | 194 ms                                                      | 166 ms: 1.17x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 38.9 ms: 1.14x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.45 ms: 1.14x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 85.4 ms: 1.13x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 846 us: 1.13x faster                                                       |
| 2to3                     | 246 ms                                                      | 220 ms: 1.12x faster                                                       |
| sympy_expand             | 314 ms                                                      | 283 ms: 1.11x faster                                                       |
| unpickle                 | 9.09 us                                                     | 8.31 us: 1.09x faster                                                      |
| nbody                    | 71.3 ms                                                     | 65.3 ms: 1.09x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.7 ms: 1.09x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 62.1 ms: 1.07x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.56 ms: 1.06x faster                                                      |
| json                     | 3.14 ms                                                     | 2.97 ms: 1.06x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 72.3 ms: 1.05x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.43 us: 1.05x faster                                                      |
| unpack_sequence          | 39.6 ns                                                     | 37.8 ns: 1.05x faster                                                      |
| logging_simple           | 6.22 us                                                     | 6.07 us: 1.03x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.5 ms: 1.02x faster                                                      |
| pidigits                 | 149 ms                                                      | 146 ms: 1.02x faster                                                       |
| scimark_fft              | 187 ms                                                      | 184 ms: 1.02x faster                                                       |
| json_loads               | 14.0 us                                                     | 14.1 us: 1.01x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 56.5 ms: 1.02x slower                                                      |
| async_generators         | 222 ms                                                      | 230 ms: 1.04x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.10 ms: 1.04x slower                                                      |
| fannkuch                 | 256 ms                                                      | 269 ms: 1.05x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 2.96 us: 1.09x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 19.1 us: 1.11x slower                                                      |
| pickle                   | 6.85 us                                                     | 7.73 us: 1.13x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.26 us: 1.18x slower                                                      |
| python_startup           | 20.6 ms                                                     | 25.6 ms: 1.24x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.6 ms: 1.26x slower                                                      |
| coverage                 | 39.0 ms                                                     | 50.6 ms: 1.30x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 93.1 ms: 1.50x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.15 ms: 1.52x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.28 ms: 1.60x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.27x faster                                                               |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250830-3.15.0a0-d3d94e0/bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.294x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: unknown