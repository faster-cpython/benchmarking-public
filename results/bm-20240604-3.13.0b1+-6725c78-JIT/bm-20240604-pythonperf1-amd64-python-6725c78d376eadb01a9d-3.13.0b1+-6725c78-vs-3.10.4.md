# Results vs. 3.10.4

- fork: python
- ref: 6725c78d376eadb01a9d
- machine: windows-amd64
- commit hash: 6725c78
- commit date: 2024-06-04
- overall geometric mean: 1.20x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 229 ms: 1.07x faster                                                        |
| chameleon      | 5.79 ms                                                     | 4.94 ms: 1.17x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.78 sec: 1.08x faster                                                      |
| html5lib       | 51.0 ms                                                     | 37.5 ms: 1.36x faster                                                       |
| tornado_http   | 108 ms                                                      | 86.1 ms: 1.26x faster                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 230 ms: 1.90x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 278 ms: 1.89x faster                                                        |
| async_tree_io           | 1.11 sec                                                    | 589 ms: 1.88x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 402 ms: 1.59x faster                                                        |
| Geometric mean          | (ref)                                                       | 1.81x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 43.7 ms: 1.41x faster                                                       |
| nbody          | 71.3 ms                                                     | 51.1 ms: 1.39x faster                                                       |
| Geometric mean | (ref)                                                       | 1.25x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 87.7 ms: 1.21x faster                                                       |
| regex_dna      | 136 ms                                                      | 124 ms: 1.10x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.62 ms: 1.03x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 15.3 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.74 ms: 1.60x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 172 us: 1.57x faster                                                        |
| unpickle_pure_python | 183 us                                                      | 126 us: 1.45x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.22 sec: 1.37x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 36.3 ms: 1.22x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 51.1 ms: 1.09x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 60.5 ms: 1.07x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 90.2 ms: 1.07x faster                                                       |
| unpickle             | 9.09 us                                                     | 8.54 us: 1.06x faster                                                       |
| pickle_list          | 2.75 us                                                     | 2.81 us: 1.02x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 17.9 us: 1.04x slower                                                       |
| unpickle_list        | 2.71 us                                                     | 2.85 us: 1.05x slower                                                       |
| pickle               | 6.85 us                                                     | 7.42 us: 1.08x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.15x faster                                                                |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 21.9 ms: 1.06x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 17.9 ms: 1.16x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.02 ms: 1.80x faster                                                       |
| django_template | 28.9 ms                                                     | 25.8 ms: 1.12x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 17.8 ms: 1.11x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 44.6 ms: 1.09x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.20x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 113 us: 2.98x faster                                                        |
| async_tree_none          | 435 ms                                                      | 230 ms: 1.90x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 278 ms: 1.89x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 589 ms: 1.88x faster                                                        |
| mako                     | 9.03 ms                                                     | 5.02 ms: 1.80x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.35 ms: 1.78x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 44.8 ms: 1.72x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 55.3 ns: 1.71x faster                                                       |
| comprehensions           | 16.5 us                                                     | 10.2 us: 1.62x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 5.74 ms: 1.60x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 402 ms: 1.59x faster                                                        |
| pyflate                  | 409 ms                                                      | 259 ms: 1.58x faster                                                        |
| chaos                    | 61.7 ms                                                     | 39.1 ms: 1.58x faster                                                       |
| richards_super           | 52.2 ms                                                     | 33.1 ms: 1.58x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 172 us: 1.57x faster                                                        |
| crypto_pyaes             | 62.5 ms                                                     | 40.8 ms: 1.53x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 481 ms: 1.52x faster                                                        |
| scimark_monte_carlo      | 57.3 ms                                                     | 37.9 ms: 1.51x faster                                                       |
| raytrace                 | 273 ms                                                      | 181 ms: 1.51x faster                                                        |
| generators               | 32.4 ms                                                     | 21.5 ms: 1.51x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 807 us: 1.51x faster                                                        |
| go                       | 139 ms                                                      | 93.2 ms: 1.49x faster                                                       |
| pylint                   | 350 ms                                                      | 235 ms: 1.49x faster                                                        |
| unpickle_pure_python     | 183 us                                                      | 126 us: 1.45x faster                                                        |
| richards                 | 42.4 ms                                                     | 29.4 ms: 1.44x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.04 ms: 1.42x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.49 sec: 1.42x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 20.3 us: 1.42x faster                                                       |
| float                    | 61.7 ms                                                     | 43.7 ms: 1.41x faster                                                       |
| nbody                    | 71.3 ms                                                     | 51.1 ms: 1.39x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.22 sec: 1.37x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 37.5 ms: 1.36x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.04 ms: 1.33x faster                                                       |
| scimark_sor              | 106 ms                                                      | 80.7 ms: 1.32x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 930 ms: 1.31x faster                                                        |
| pprint_safe_repr         | 592 ms                                                      | 452 ms: 1.31x faster                                                        |
| pycparser                | 930 ms                                                      | 723 ms: 1.29x faster                                                        |
| scimark_fft              | 187 ms                                                      | 147 ms: 1.27x faster                                                        |
| tornado_http             | 108 ms                                                      | 86.1 ms: 1.26x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 40.5 ms: 1.25x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.68 ms: 1.23x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 36.3 ms: 1.22x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 70.2 ms: 1.22x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.57 us: 1.22x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.2 ms: 1.22x faster                                                       |
| regex_compile            | 106 ms                                                      | 87.7 ms: 1.21x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.48 sec: 1.20x faster                                                      |
| fannkuch                 | 256 ms                                                      | 215 ms: 1.19x faster                                                        |
| chameleon                | 5.79 ms                                                     | 4.94 ms: 1.17x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 820 us: 1.17x faster                                                        |
| mypy2                    | 555 ms                                                      | 485 ms: 1.15x faster                                                        |
| sympy_sum                | 107 ms                                                      | 94.0 ms: 1.14x faster                                                       |
| django_template          | 28.9 ms                                                     | 25.8 ms: 1.12x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 17.8 ms: 1.11x faster                                                       |
| regex_dna                | 136 ms                                                      | 124 ms: 1.10x faster                                                        |
| nqueens                  | 66.6 ms                                                     | 60.7 ms: 1.10x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 51.1 ms: 1.09x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 14.1 ms: 1.08x faster                                                       |
| json                     | 3.14 ms                                                     | 2.90 ms: 1.08x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.78 sec: 1.08x faster                                                      |
| sympy_str                | 194 ms                                                      | 180 ms: 1.08x faster                                                        |
| sqlglot_optimize         | 39.8 ms                                                     | 37.0 ms: 1.07x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.29 us: 1.07x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 60.5 ms: 1.07x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 90.2 ms: 1.07x faster                                                       |
| 2to3                     | 246 ms                                                      | 229 ms: 1.07x faster                                                        |
| aiohttp                  | 995 us                                                      | 930 us: 1.07x faster                                                        |
| logging_simple           | 6.22 us                                                     | 5.82 us: 1.07x faster                                                       |
| unpickle                 | 9.09 us                                                     | 8.54 us: 1.06x faster                                                       |
| deepcopy                 | 255 us                                                      | 241 us: 1.06x faster                                                        |
| meteor_contest           | 75.9 ms                                                     | 72.1 ms: 1.05x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 2.14 us: 1.03x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.62 ms: 1.03x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 15.3 ms: 1.01x faster                                                       |
| flaskblogging            | 2.03 sec                                                    | 2.04 sec: 1.00x slower                                                      |
| sympy_expand             | 314 ms                                                      | 319 ms: 1.01x slower                                                        |
| pickle_list              | 2.75 us                                                     | 2.81 us: 1.02x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 17.9 us: 1.04x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 2.85 us: 1.05x slower                                                       |
| python_startup           | 20.6 ms                                                     | 21.9 ms: 1.06x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.42 us: 1.08x slower                                                       |
| genshi_xml               | 41.0 ms                                                     | 44.6 ms: 1.09x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.56 ms: 1.11x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 69.6 ms: 1.12x slower                                                       |
| async_generators         | 222 ms                                                      | 252 ms: 1.14x slower                                                        |
| telco                    | 3.94 ms                                                     | 4.52 ms: 1.15x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 923 us: 1.15x slower                                                        |
| python_startup_no_site   | 15.5 ms                                                     | 17.9 ms: 1.16x slower                                                       |
| coverage                 | 39.0 ms                                                     | 45.7 ms: 1.17x slower                                                       |
| thrift                   | 617 us                                                      | 9.25 ms: 14.98x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.20x faster                                                                |

Benchmark hidden because not significant (3): pathlib, pidigits, json_loads
Ignored benchmarks (5) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (4) of results/bm-20240604-3.13.0b1+-6725c78-JIT/bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown