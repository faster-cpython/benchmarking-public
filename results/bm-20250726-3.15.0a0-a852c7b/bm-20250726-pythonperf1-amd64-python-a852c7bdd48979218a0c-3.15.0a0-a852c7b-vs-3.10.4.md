# Results vs. 3.10.4

- fork: python
- ref: a852c7bdd48979218a0c
- machine: windows-amd64
- commit hash: a852c7b
- commit date: 2025-07-26
- overall geometric mean: 1.258x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 224 ms: 1.10x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.64 sec: 1.17x faster                                                     |
| html5lib       | 51.0 ms                                                     | 39.3 ms: 1.30x faster                                                      |
| Geometric mean | (ref)                                                       | 1.19x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 405 ms: 2.74x faster                                                       |
| async_tree_none         | 435 ms                                                      | 177 ms: 2.46x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 214 ms: 2.46x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 335 ms: 1.91x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.37x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 43.3 ms: 1.43x faster                                                      |
| nbody          | 71.3 ms                                                     | 65.3 ms: 1.09x faster                                                      |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 82.8 ms: 1.28x faster                                                      |
| regex_dna      | 136 ms                                                      | 122 ms: 1.12x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.6 ms: 1.06x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                      |
| Geometric mean | (ref)                                                       | 1.12x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.24 ms: 1.47x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 140 us: 1.31x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 219 us: 1.23x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.45 sec: 1.15x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 40.8 ms: 1.09x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 90.0 ms: 1.08x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.59 us: 1.06x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 66.4 ms: 1.02x slower                                                      |
| json_loads           | 14.0 us                                                     | 14.4 us: 1.03x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 59.1 ms: 1.06x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 2.99 us: 1.10x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 19.7 us: 1.14x slower                                                      |
| pickle               | 6.85 us                                                     | 7.94 us: 1.16x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.24 us: 1.18x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 20.1 ms: 1.29x slower                                                      |
| python_startup         | 20.6 ms                                                     | 27.0 ms: 1.31x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.30x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.82 ms: 1.32x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.7 ms: 1.26x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 34.5 ms: 1.19x faster                                                      |
| django_template | 28.9 ms                                                     | 25.2 ms: 1.15x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.23x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 105 us: 3.20x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 405 ms: 2.74x faster                                                       |
| async_tree_none          | 435 ms                                                      | 177 ms: 2.46x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 214 ms: 2.46x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 32.6 ms: 2.32x faster                                                      |
| mdp                      | 1.78 sec                                                    | 816 ms: 2.18x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 335 ms: 1.91x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.29 ms: 1.83x faster                                                      |
| go                       | 139 ms                                                      | 77.4 ms: 1.80x faster                                                      |
| pylint                   | 350 ms                                                      | 203 ms: 1.73x faster                                                       |
| generators               | 32.4 ms                                                     | 19.4 ms: 1.67x faster                                                      |
| richards_super           | 52.2 ms                                                     | 31.5 ms: 1.66x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 57.6 ns: 1.64x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 447 ms: 1.64x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.30 sec: 1.63x faster                                                     |
| deepcopy_memo            | 28.8 us                                                     | 18.7 us: 1.54x faster                                                      |
| comprehensions           | 16.5 us                                                     | 11.0 us: 1.50x faster                                                      |
| richards                 | 42.4 ms                                                     | 28.7 ms: 1.48x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.24 ms: 1.47x faster                                                      |
| deepcopy                 | 255 us                                                      | 174 us: 1.46x faster                                                       |
| raytrace                 | 273 ms                                                      | 187 ms: 1.46x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 58.8 ms: 1.46x faster                                                      |
| chaos                    | 61.7 ms                                                     | 42.3 ms: 1.46x faster                                                      |
| float                    | 61.7 ms                                                     | 43.3 ms: 1.43x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.9 ms: 1.40x faster                                                      |
| pyflate                  | 409 ms                                                      | 295 ms: 1.39x faster                                                       |
| scimark_sor              | 106 ms                                                      | 77.3 ms: 1.37x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.23 ms: 1.36x faster                                                      |
| mako                     | 9.03 ms                                                     | 6.82 ms: 1.32x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 140 us: 1.31x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 39.3 ms: 1.30x faster                                                      |
| pycparser                | 930 ms                                                      | 723 ms: 1.29x faster                                                       |
| regex_compile            | 106 ms                                                      | 82.8 ms: 1.28x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 49.4 ms: 1.27x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 15.7 ms: 1.26x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 61.6 ms: 1.26x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 40.8 ms: 1.24x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 219 us: 1.23x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 12.5 ms: 1.22x faster                                                      |
| sympy_sum                | 107 ms                                                      | 88.3 ms: 1.21x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.58 us: 1.21x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.03 sec: 1.19x faster                                                     |
| genshi_xml               | 41.0 ms                                                     | 34.5 ms: 1.19x faster                                                      |
| thrift                   | 617 us                                                      | 523 us: 1.18x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.64 sec: 1.17x faster                                                     |
| deepcopy_reduce          | 2.20 us                                                     | 1.90 us: 1.16x faster                                                      |
| unpack_sequence          | 39.6 ns                                                     | 34.3 ns: 1.15x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.45 sec: 1.15x faster                                                     |
| pprint_safe_repr         | 592 ms                                                      | 515 ms: 1.15x faster                                                       |
| django_template          | 28.9 ms                                                     | 25.2 ms: 1.15x faster                                                      |
| regex_dna                | 136 ms                                                      | 122 ms: 1.12x faster                                                       |
| sympy_str                | 194 ms                                                      | 174 ms: 1.12x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 864 us: 1.11x faster                                                       |
| 2to3                     | 246 ms                                                      | 224 ms: 1.10x faster                                                       |
| sympy_expand             | 314 ms                                                      | 287 ms: 1.10x faster                                                       |
| nbody                    | 71.3 ms                                                     | 65.3 ms: 1.09x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.7 ms: 1.09x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 40.8 ms: 1.09x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 90.0 ms: 1.08x faster                                                      |
| unpickle                 | 9.09 us                                                     | 8.59 us: 1.06x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.58 ms: 1.06x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 14.6 ms: 1.06x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 72.4 ms: 1.05x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.58 us: 1.03x faster                                                      |
| scimark_fft              | 187 ms                                                      | 183 ms: 1.02x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 65.2 ms: 1.02x faster                                                      |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 66.4 ms: 1.02x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.4 us: 1.03x slower                                                      |
| fannkuch                 | 256 ms                                                      | 264 ms: 1.03x slower                                                       |
| async_generators         | 222 ms                                                      | 230 ms: 1.04x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 59.1 ms: 1.06x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 2.99 us: 1.10x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 19.7 us: 1.14x slower                                                      |
| pickle                   | 6.85 us                                                     | 7.94 us: 1.16x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.24 us: 1.18x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.69 ms: 1.19x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 20.1 ms: 1.29x slower                                                      |
| python_startup           | 20.6 ms                                                     | 27.0 ms: 1.31x slower                                                      |
| coverage                 | 39.0 ms                                                     | 51.9 ms: 1.33x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.11 ms: 1.50x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 96.6 ms: 1.56x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.30 ms: 1.63x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.23x faster                                                               |

Benchmark hidden because not significant (2): json, logging_simple
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.258x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: unknown