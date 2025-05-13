# Results vs. 3.10.4

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: windows-amd64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.343x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 212 ms: 1.16x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.56 sec: 1.23x faster                                                     |
| html5lib       | 51.0 ms                                                     | 34.4 ms: 1.48x faster                                                      |
| Geometric mean | (ref)                                                       | 1.28x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 366 ms: 3.03x faster                                                       |
| async_tree_none         | 435 ms                                                      | 151 ms: 2.88x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 188 ms: 2.80x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 315 ms: 2.02x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.65x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 38.0 ms: 1.62x faster                                                      |
| nbody          | 71.3 ms                                                     | 52.5 ms: 1.36x faster                                                      |
| pidigits       | 149 ms                                                      | 146 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.31x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 68.1 ms: 1.56x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 13.0 ms: 1.19x faster                                                      |
| regex_dna      | 136 ms                                                      | 119 ms: 1.15x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.63 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                       | 1.21x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 103 us: 1.78x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 167 us: 1.61x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.04 sec: 1.61x faster                                                     |
| json_dumps           | 9.16 ms                                                     | 5.90 ms: 1.55x faster                                                      |
| pickle_dict          | 17.2 us                                                     | 11.8 us: 1.46x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 33.2 ms: 1.34x faster                                                      |
| pickle_list          | 2.75 us                                                     | 2.22 us: 1.24x faster                                                      |
| unpickle_list        | 2.71 us                                                     | 2.22 us: 1.22x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 47.9 ms: 1.16x faster                                                      |
| unpickle             | 9.09 us                                                     | 7.86 us: 1.16x faster                                                      |
| pickle               | 6.85 us                                                     | 6.26 us: 1.09x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 90.9 ms: 1.07x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 61.8 ms: 1.05x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.6 us: 1.04x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.28x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 20.4 ms: 1.31x slower                                                      |
| python_startup         | 20.6 ms                                                     | 27.1 ms: 1.31x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.31x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 19.8 ms                                                     | 11.4 ms: 1.73x faster                                                      |
| mako            | 9.03 ms                                                     | 5.94 ms: 1.52x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 27.7 ms: 1.48x faster                                                      |
| django_template | 28.9 ms                                                     | 20.3 ms: 1.42x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.54x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 91.7 us: 3.67x faster                                                      |
| async_tree_io            | 1.11 sec                                                    | 366 ms: 3.03x faster                                                       |
| async_tree_none          | 435 ms                                                      | 151 ms: 2.88x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 188 ms: 2.80x faster                                                       |
| deltablue                | 4.19 ms                                                     | 1.56 ms: 2.68x faster                                                      |
| mdp                      | 1.78 sec                                                    | 684 ms: 2.60x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 30.9 ms: 2.45x faster                                                      |
| go                       | 139 ms                                                      | 59.5 ms: 2.34x faster                                                      |
| generators               | 32.4 ms                                                     | 14.7 ms: 2.20x faster                                                      |
| scimark_sor              | 106 ms                                                      | 49.0 ms: 2.17x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 13.3 us: 2.16x faster                                                      |
| richards_super           | 52.2 ms                                                     | 24.6 ms: 2.12x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 28.2 ms: 2.03x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 315 ms: 2.02x faster                                                       |
| richards                 | 42.4 ms                                                     | 21.4 ms: 1.98x faster                                                      |
| chaos                    | 61.7 ms                                                     | 31.2 ms: 1.98x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 2.92 ms: 1.97x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 45.1 ms: 1.90x faster                                                      |
| comprehensions           | 16.5 us                                                     | 8.73 us: 1.89x faster                                                      |
| deepcopy                 | 255 us                                                      | 137 us: 1.86x faster                                                       |
| pylint                   | 350 ms                                                      | 189 ms: 1.85x faster                                                       |
| raytrace                 | 273 ms                                                      | 151 ms: 1.81x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 103 us: 1.78x faster                                                       |
| pyflate                  | 409 ms                                                      | 234 ms: 1.75x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 11.4 ms: 1.73x faster                                                      |
| float                    | 61.7 ms                                                     | 38.0 ms: 1.62x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 167 us: 1.61x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.04 sec: 1.61x faster                                                     |
| spectral_norm            | 77.3 ms                                                     | 48.1 ms: 1.61x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 39.6 ms: 1.58x faster                                                      |
| regex_compile            | 106 ms                                                      | 68.1 ms: 1.56x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.90 ms: 1.55x faster                                                      |
| mako                     | 9.03 ms                                                     | 5.94 ms: 1.52x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 805 ms: 1.52x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 395 ms: 1.50x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.48 us: 1.49x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 27.7 ms: 1.48x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 34.4 ms: 1.48x faster                                                      |
| pickle_dict              | 17.2 us                                                     | 11.8 us: 1.46x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.45 sec: 1.46x faster                                                     |
| pycparser                | 930 ms                                                      | 651 ms: 1.43x faster                                                       |
| django_template          | 28.9 ms                                                     | 20.3 ms: 1.42x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 47.3 ms: 1.41x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 524 ms: 1.40x faster                                                       |
| coroutines               | 16.0 ms                                                     | 11.5 ms: 1.39x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 11.1 ms: 1.37x faster                                                      |
| sympy_sum                | 107 ms                                                      | 78.6 ms: 1.36x faster                                                      |
| nbody                    | 71.3 ms                                                     | 52.5 ms: 1.36x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 33.2 ms: 1.34x faster                                                      |
| unpack_sequence          | 39.6 ns                                                     | 29.8 ns: 1.33x faster                                                      |
| sympy_str                | 194 ms                                                      | 149 ms: 1.30x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 38.9 ms: 1.30x faster                                                      |
| scimark_fft              | 187 ms                                                      | 145 ms: 1.29x faster                                                       |
| fannkuch                 | 256 ms                                                      | 199 ms: 1.29x faster                                                       |
| pickle_list              | 2.75 us                                                     | 2.22 us: 1.24x faster                                                      |
| sympy_expand             | 314 ms                                                      | 255 ms: 1.23x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.56 sec: 1.23x faster                                                     |
| sqlite_synth             | 1.91 us                                                     | 1.56 us: 1.22x faster                                                      |
| unpickle_list            | 2.71 us                                                     | 2.22 us: 1.22x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 13.0 ms: 1.19x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.31 ms: 1.18x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 47.9 ms: 1.16x faster                                                      |
| 2to3                     | 246 ms                                                      | 212 ms: 1.16x faster                                                       |
| unpickle                 | 9.09 us                                                     | 7.86 us: 1.16x faster                                                      |
| regex_dna                | 136 ms                                                      | 119 ms: 1.15x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 66.3 ms: 1.15x faster                                                      |
| async_generators         | 222 ms                                                      | 194 ms: 1.14x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 853 us: 1.12x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.16 us: 1.10x faster                                                      |
| pickle                   | 6.85 us                                                     | 6.26 us: 1.09x faster                                                      |
| logging_simple           | 6.22 us                                                     | 5.74 us: 1.08x faster                                                      |
| json                     | 3.14 ms                                                     | 2.94 ms: 1.07x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 90.9 ms: 1.07x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 61.8 ms: 1.05x faster                                                      |
| pidigits                 | 149 ms                                                      | 146 ms: 1.02x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.63 ms: 1.02x faster                                                      |
| json_loads               | 14.0 us                                                     | 14.6 us: 1.04x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.12 ms: 1.05x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 20.4 ms: 1.31x slower                                                      |
| python_startup           | 20.6 ms                                                     | 27.1 ms: 1.31x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 98.4 ms: 1.59x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.45 ms: 1.81x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.89 ms: 2.05x slower                                                      |
| logging_silent           | 94.6 ns                                                     | 273 ns: 2.89x slower                                                       |
| coverage                 | 39.0 ms                                                     | 219 ms: 5.60x slower                                                       |
| thrift                   | 617 us                                                      | 95.0 ms: 153.84x slower                                                    |
| Geometric mean           | (ref)                                                       | 1.30x faster                                                               |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250510-3.15.0a0-1a87b6e-CLANG/bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.343x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.38x
- 95% likely to have a speedup of 1.36x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: unknown