# Results vs. 3.10.4

- fork: python
- ref: 6725c78d376eadb01a9d
- machine: windows-amd64
- commit hash: 6725c78
- commit date: 2024-06-04
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 236 ms: 1.04x faster                                                        |
| chameleon      | 5.79 ms                                                     | 5.40 ms: 1.07x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.86 sec: 1.03x faster                                                      |
| html5lib       | 51.0 ms                                                     | 41.7 ms: 1.22x faster                                                       |
| tornado_http   | 108 ms                                                      | 87.8 ms: 1.23x faster                                                       |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 234 ms: 1.86x faster                                                        |
| async_tree_io           | 1.11 sec                                                    | 602 ms: 1.84x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 293 ms: 1.80x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 402 ms: 1.59x faster                                                        |
| Geometric mean          | (ref)                                                       | 1.77x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 56.5 ms: 1.09x faster                                                       |
| pidigits       | 149 ms                                                      | 151 ms: 1.01x slower                                                        |
| nbody          | 71.3 ms                                                     | 80.1 ms: 1.12x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 121 ms: 1.13x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.60 ms: 1.03x faster                                                       |
| regex_compile  | 106 ms                                                      | 110 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.90 ms: 1.55x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 228 us: 1.18x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 40.2 ms: 1.10x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 169 us: 1.08x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.54 sec: 1.08x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 89.8 ms: 1.08x faster                                                       |
| unpickle             | 9.09 us                                                     | 8.44 us: 1.08x faster                                                       |
| json_loads           | 14.0 us                                                     | 14.2 us: 1.01x slower                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 67.6 ms: 1.04x slower                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 58.0 ms: 1.04x slower                                                       |
| unpickle_list        | 2.71 us                                                     | 2.84 us: 1.05x slower                                                       |
| pickle_list          | 2.75 us                                                     | 2.89 us: 1.05x slower                                                       |
| pickle               | 6.85 us                                                     | 7.19 us: 1.05x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 18.3 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 16.4 ms: 1.06x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.03x slower                                                                |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 7.78 ms: 1.16x faster                                                       |
| django_template | 28.9 ms                                                     | 25.6 ms: 1.13x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 18.2 ms: 1.09x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 38.5 ms: 1.07x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.11x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 116 us: 2.88x faster                                                        |
| async_tree_none          | 435 ms                                                      | 234 ms: 1.86x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 602 ms: 1.84x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 293 ms: 1.80x faster                                                        |
| generators               | 32.4 ms                                                     | 19.7 ms: 1.64x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 402 ms: 1.59x faster                                                        |
| json_dumps               | 9.16 ms                                                     | 5.90 ms: 1.55x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.71 ms: 1.55x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 478 ms: 1.53x faster                                                        |
| richards_super           | 52.2 ms                                                     | 34.1 ms: 1.53x faster                                                       |
| pylint                   | 350 ms                                                      | 230 ms: 1.52x faster                                                        |
| raytrace                 | 273 ms                                                      | 186 ms: 1.47x faster                                                        |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.50 sec: 1.41x faster                                                      |
| richards                 | 42.4 ms                                                     | 30.4 ms: 1.40x faster                                                       |
| chaos                    | 61.7 ms                                                     | 45.5 ms: 1.36x faster                                                       |
| go                       | 139 ms                                                      | 104 ms: 1.34x faster                                                        |
| sqlglot_parse            | 1.22 ms                                                     | 926 us: 1.31x faster                                                        |
| sqlglot_transpile        | 1.48 ms                                                     | 1.16 ms: 1.27x faster                                                       |
| coroutines               | 16.0 ms                                                     | 12.7 ms: 1.26x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 76.2 ns: 1.24x faster                                                       |
| tornado_http             | 108 ms                                                      | 87.8 ms: 1.23x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 41.7 ms: 1.22x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.48 sec: 1.20x faster                                                      |
| pyflate                  | 409 ms                                                      | 345 ms: 1.19x faster                                                        |
| pickle_pure_python       | 270 us                                                      | 228 us: 1.18x faster                                                        |
| crypto_pyaes             | 62.5 ms                                                     | 53.0 ms: 1.18x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.63 us: 1.18x faster                                                       |
| scimark_sor              | 106 ms                                                      | 90.8 ms: 1.17x faster                                                       |
| mako                     | 9.03 ms                                                     | 7.78 ms: 1.16x faster                                                       |
| mypy2                    | 555 ms                                                      | 481 ms: 1.15x faster                                                        |
| comprehensions           | 16.5 us                                                     | 14.4 us: 1.14x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 841 us: 1.14x faster                                                        |
| django_template          | 28.9 ms                                                     | 25.6 ms: 1.13x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 44.7 ms: 1.13x faster                                                       |
| regex_dna                | 136 ms                                                      | 121 ms: 1.13x faster                                                        |
| xml_etree_process        | 44.5 ms                                                     | 40.2 ms: 1.10x faster                                                       |
| float                    | 61.7 ms                                                     | 56.5 ms: 1.09x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 18.2 ms: 1.09x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 169 us: 1.08x faster                                                        |
| tomli_loads              | 1.67 sec                                                    | 1.54 sec: 1.08x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 89.8 ms: 1.08x faster                                                       |
| unpickle                 | 9.09 us                                                     | 8.44 us: 1.08x faster                                                       |
| sympy_sum                | 107 ms                                                      | 99.8 ms: 1.07x faster                                                       |
| chameleon                | 5.79 ms                                                     | 5.40 ms: 1.07x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 53.5 ms: 1.07x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 38.5 ms: 1.07x faster                                                       |
| json                     | 3.14 ms                                                     | 2.95 ms: 1.06x faster                                                       |
| aiohttp                  | 995 us                                                      | 937 us: 1.06x faster                                                        |
| pycparser                | 930 ms                                                      | 876 ms: 1.06x faster                                                        |
| pprint_pformat           | 1.22 sec                                                    | 1.16 sec: 1.05x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 81.9 ms: 1.05x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 567 ms: 1.04x faster                                                        |
| 2to3                     | 246 ms                                                      | 236 ms: 1.04x faster                                                        |
| regex_effbot             | 1.66 ms                                                     | 1.60 ms: 1.03x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 14.8 ms: 1.03x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.86 sec: 1.03x faster                                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 38.9 ms: 1.02x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.60 us: 1.02x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 5.66 ms: 1.02x faster                                                       |
| flaskblogging            | 2.03 sec                                                    | 2.03 sec: 1.00x slower                                                      |
| spectral_norm            | 77.3 ms                                                     | 77.8 ms: 1.01x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.2 us: 1.01x slower                                                       |
| pidigits                 | 149 ms                                                      | 151 ms: 1.01x slower                                                        |
| sympy_str                | 194 ms                                                      | 197 ms: 1.01x slower                                                        |
| deepcopy_reduce          | 2.20 us                                                     | 2.26 us: 1.03x slower                                                       |
| deepcopy                 | 255 us                                                      | 263 us: 1.03x slower                                                        |
| meteor_contest           | 75.9 ms                                                     | 78.4 ms: 1.03x slower                                                       |
| regex_compile            | 106 ms                                                      | 110 ms: 1.04x slower                                                        |
| xml_etree_iterparse      | 65.0 ms                                                     | 67.6 ms: 1.04x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 58.0 ms: 1.04x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 2.84 us: 1.05x slower                                                       |
| nqueens                  | 66.6 ms                                                     | 69.7 ms: 1.05x slower                                                       |
| pickle_list              | 2.75 us                                                     | 2.89 us: 1.05x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.19 us: 1.05x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 16.4 ms: 1.06x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 18.3 us: 1.06x slower                                                       |
| sympy_expand             | 314 ms                                                      | 336 ms: 1.07x slower                                                        |
| bench_mp_pool            | 62.0 ms                                                     | 67.0 ms: 1.08x slower                                                       |
| async_generators         | 222 ms                                                      | 241 ms: 1.09x slower                                                        |
| deepcopy_memo            | 28.8 us                                                     | 31.9 us: 1.11x slower                                                       |
| fannkuch                 | 256 ms                                                      | 285 ms: 1.11x slower                                                        |
| gc_traversal             | 1.41 ms                                                     | 1.58 ms: 1.12x slower                                                       |
| nbody                    | 71.3 ms                                                     | 80.1 ms: 1.12x slower                                                       |
| scimark_fft              | 187 ms                                                      | 212 ms: 1.13x slower                                                        |
| coverage                 | 39.0 ms                                                     | 44.4 ms: 1.14x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 915 us: 1.14x slower                                                        |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 3.20 ms: 1.17x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.98 ms: 1.26x slower                                                       |
| thrift                   | 617 us                                                      | 9.82 ms: 15.91x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.08x faster                                                                |

Benchmark hidden because not significant (4): python_startup, regex_v8, pathlib, logging_simple
Ignored benchmarks (5) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (4) of results/bm-20240604-3.13.0b1+-6725c78-PYTHON_UOPS/bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown