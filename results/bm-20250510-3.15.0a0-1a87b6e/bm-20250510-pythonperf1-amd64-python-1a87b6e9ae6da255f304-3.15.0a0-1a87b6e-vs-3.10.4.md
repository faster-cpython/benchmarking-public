# Results vs. 3.10.4

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: windows-amd64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.166x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 225 ms: 1.09x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.66 sec: 1.16x faster                                                     |
| html5lib       | 51.0 ms                                                     | 39.0 ms: 1.31x faster                                                      |
| Geometric mean | (ref)                                                       | 1.18x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 398 ms: 2.78x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 207 ms: 2.54x faster                                                       |
| async_tree_none         | 435 ms                                                      | 173 ms: 2.52x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 329 ms: 1.94x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.42x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 43.3 ms: 1.43x faster                                                      |
| nbody          | 71.3 ms                                                     | 61.9 ms: 1.15x faster                                                      |
| Geometric mean | (ref)                                                       | 1.18x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 80.4 ms: 1.32x faster                                                      |
| regex_dna      | 136 ms                                                      | 120 ms: 1.13x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.3 ms: 1.08x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.54 ms: 1.08x faster                                                      |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 130 us: 1.40x faster                                                       |
| json_dumps           | 9.16 ms                                                     | 6.64 ms: 1.38x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 208 us: 1.30x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.37 sec: 1.22x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 39.8 ms: 1.12x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 90.7 ms: 1.07x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.54 us: 1.07x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 64.2 ms: 1.01x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 56.3 ms: 1.01x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 2.78 us: 1.02x slower                                                      |
| json_loads           | 14.0 us                                                     | 15.4 us: 1.10x slower                                                      |
| pickle               | 6.85 us                                                     | 7.89 us: 1.15x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 20.5 us: 1.20x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.59 us: 1.31x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.8 ms: 1.28x slower                                                      |
| python_startup         | 20.6 ms                                                     | 26.3 ms: 1.28x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.28x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.59 ms: 1.37x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.3 ms: 1.29x faster                                                      |
| django_template | 28.9 ms                                                     | 24.0 ms: 1.20x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 34.2 ms: 1.20x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.26x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 107 us: 3.14x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 398 ms: 2.78x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 207 ms: 2.54x faster                                                       |
| async_tree_none          | 435 ms                                                      | 173 ms: 2.52x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 32.6 ms: 2.32x faster                                                      |
| mdp                      | 1.78 sec                                                    | 792 ms: 2.25x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.10 ms: 1.99x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 329 ms: 1.94x faster                                                       |
| go                       | 139 ms                                                      | 77.2 ms: 1.80x faster                                                      |
| pylint                   | 350 ms                                                      | 201 ms: 1.74x faster                                                       |
| richards_super           | 52.2 ms                                                     | 30.9 ms: 1.69x faster                                                      |
| generators               | 32.4 ms                                                     | 19.5 ms: 1.66x faster                                                      |
| chaos                    | 61.7 ms                                                     | 38.0 ms: 1.62x faster                                                      |
| richards                 | 42.4 ms                                                     | 26.8 ms: 1.58x faster                                                      |
| raytrace                 | 273 ms                                                      | 179 ms: 1.53x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 18.9 us: 1.52x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 57.1 ms: 1.50x faster                                                      |
| deepcopy                 | 255 us                                                      | 173 us: 1.48x faster                                                       |
| scimark_sor              | 106 ms                                                      | 72.7 ms: 1.46x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 39.3 ms: 1.46x faster                                                      |
| comprehensions           | 16.5 us                                                     | 11.3 us: 1.46x faster                                                      |
| pyflate                  | 409 ms                                                      | 282 ms: 1.45x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.46 sec: 1.45x faster                                                     |
| hexiom                   | 5.74 ms                                                     | 3.98 ms: 1.44x faster                                                      |
| float                    | 61.7 ms                                                     | 43.3 ms: 1.43x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 130 us: 1.40x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 522 ms: 1.40x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.64 ms: 1.38x faster                                                      |
| mako                     | 9.03 ms                                                     | 6.59 ms: 1.37x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 57.0 ms: 1.36x faster                                                      |
| regex_compile            | 106 ms                                                      | 80.4 ms: 1.32x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 47.5 ms: 1.32x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 39.0 ms: 1.31x faster                                                      |
| pycparser                | 930 ms                                                      | 718 ms: 1.30x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 208 us: 1.30x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 15.3 ms: 1.29x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 990 ms: 1.23x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 12.5 ms: 1.22x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 486 ms: 1.22x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.37 sec: 1.22x faster                                                     |
| sympy_sum                | 107 ms                                                      | 88.3 ms: 1.21x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 41.9 ms: 1.21x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.0 ms: 1.20x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 34.2 ms: 1.20x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.60 us: 1.19x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.86 us: 1.19x faster                                                      |
| coroutines               | 16.0 ms                                                     | 13.6 ms: 1.17x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.66 sec: 1.16x faster                                                     |
| nbody                    | 71.3 ms                                                     | 61.9 ms: 1.15x faster                                                      |
| sympy_str                | 194 ms                                                      | 170 ms: 1.14x faster                                                       |
| regex_dna                | 136 ms                                                      | 120 ms: 1.13x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 39.8 ms: 1.12x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 60.0 ms: 1.11x faster                                                      |
| scimark_fft              | 187 ms                                                      | 170 ms: 1.10x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 872 us: 1.10x faster                                                       |
| 2to3                     | 246 ms                                                      | 225 ms: 1.09x faster                                                       |
| sympy_expand             | 314 ms                                                      | 292 ms: 1.08x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.53 ms: 1.08x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 14.3 ms: 1.08x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.54 ms: 1.08x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 90.7 ms: 1.07x faster                                                      |
| unpickle                 | 9.09 us                                                     | 8.54 us: 1.07x faster                                                      |
| fannkuch                 | 256 ms                                                      | 242 ms: 1.06x faster                                                       |
| unpack_sequence          | 39.6 ns                                                     | 38.2 ns: 1.04x faster                                                      |
| json                     | 3.14 ms                                                     | 3.06 ms: 1.02x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 74.4 ms: 1.02x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 64.2 ms: 1.01x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 56.3 ms: 1.01x slower                                                      |
| logging_format           | 6.76 us                                                     | 6.92 us: 1.02x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 2.78 us: 1.02x slower                                                      |
| logging_simple           | 6.22 us                                                     | 6.44 us: 1.03x slower                                                      |
| async_generators         | 222 ms                                                      | 234 ms: 1.05x slower                                                       |
| json_loads               | 14.0 us                                                     | 15.4 us: 1.10x slower                                                      |
| pickle                   | 6.85 us                                                     | 7.89 us: 1.15x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.59 ms: 1.16x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 20.5 us: 1.20x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.8 ms: 1.28x slower                                                      |
| python_startup           | 20.6 ms                                                     | 26.3 ms: 1.28x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.59 us: 1.31x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.17 ms: 1.54x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 97.2 ms: 1.57x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.31 ms: 1.64x slower                                                      |
| logging_silent           | 94.6 ns                                                     | 318 ns: 3.36x slower                                                       |
| coverage                 | 39.0 ms                                                     | 290 ms: 7.43x slower                                                       |
| thrift                   | 617 us                                                      | 102 ms: 165.85x slower                                                     |
| Geometric mean           | (ref)                                                       | 1.12x faster                                                               |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.166x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: unknown