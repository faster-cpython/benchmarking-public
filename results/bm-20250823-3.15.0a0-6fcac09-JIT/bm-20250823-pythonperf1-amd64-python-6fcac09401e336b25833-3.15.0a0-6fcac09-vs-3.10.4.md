# Results vs. 3.10.4

- fork: python
- ref: 6fcac09401e336b25833
- machine: windows-amd64
- commit hash: 6fcac09
- commit date: 2025-08-23
- overall geometric mean: 1.350x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 214 ms: 1.15x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.61 sec: 1.19x faster                                                     |
| html5lib       | 51.0 ms                                                     | 37.3 ms: 1.37x faster                                                      |
| Geometric mean | (ref)                                                       | 1.23x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 383 ms: 2.90x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 197 ms: 2.67x faster                                                       |
| async_tree_none         | 435 ms                                                      | 168 ms: 2.59x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 330 ms: 1.93x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.49x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 42.9 ms: 1.44x faster                                                      |
| nbody          | 71.3 ms                                                     | 60.0 ms: 1.19x faster                                                      |
| pidigits       | 149 ms                                                      | 144 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.21x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 77.4 ms: 1.37x faster                                                      |
| regex_dna      | 136 ms                                                      | 116 ms: 1.18x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 13.5 ms: 1.14x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                                      |
| Geometric mean | (ref)                                                       | 1.18x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 104 us: 1.77x faster                                                       |
| json_dumps           | 9.16 ms                                                     | 5.31 ms: 1.73x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.08 sec: 1.55x faster                                                     |
| pickle_pure_python   | 270 us                                                      | 197 us: 1.37x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 34.7 ms: 1.28x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 85.5 ms: 1.13x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 49.8 ms: 1.11x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.43 us: 1.08x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 61.6 ms: 1.05x faster                                                      |
| pickle               | 6.85 us                                                     | 7.46 us: 1.09x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 19.3 us: 1.13x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.30 us: 1.20x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.16x faster                                                               |

Benchmark hidden because not significant (2): unpickle_list, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.2 ms: 1.22x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 19.2 ms: 1.24x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.23x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.21 ms: 1.73x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.3 ms: 1.29x faster                                                      |
| django_template | 28.9 ms                                                     | 23.9 ms: 1.21x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 34.7 ms: 1.18x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.34x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 100 us: 3.35x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 383 ms: 2.90x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 197 ms: 2.67x faster                                                       |
| async_tree_none          | 435 ms                                                      | 168 ms: 2.59x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 30.1 ms: 2.52x faster                                                      |
| mdp                      | 1.78 sec                                                    | 777 ms: 2.29x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.15 ms: 1.95x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 330 ms: 1.93x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 389 ms: 1.88x faster                                                       |
| go                       | 139 ms                                                      | 74.9 ms: 1.86x faster                                                      |
| pylint                   | 350 ms                                                      | 193 ms: 1.82x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 53.5 ns: 1.77x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 104 us: 1.77x faster                                                       |
| mako                     | 9.03 ms                                                     | 5.21 ms: 1.73x faster                                                      |
| richards_super           | 52.2 ms                                                     | 30.1 ms: 1.73x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.31 ms: 1.73x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.24 sec: 1.70x faster                                                     |
| generators               | 32.4 ms                                                     | 19.1 ms: 1.69x faster                                                      |
| richards                 | 42.4 ms                                                     | 26.3 ms: 1.61x faster                                                      |
| comprehensions           | 16.5 us                                                     | 10.3 us: 1.61x faster                                                      |
| pyflate                  | 409 ms                                                      | 256 ms: 1.60x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 18.2 us: 1.58x faster                                                      |
| chaos                    | 61.7 ms                                                     | 39.6 ms: 1.56x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.08 sec: 1.55x faster                                                     |
| raytrace                 | 273 ms                                                      | 176 ms: 1.55x faster                                                       |
| deepcopy                 | 255 us                                                      | 168 us: 1.52x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 57.8 ms: 1.48x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 3.91 ms: 1.47x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 39.1 ms: 1.46x faster                                                      |
| float                    | 61.7 ms                                                     | 42.9 ms: 1.44x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 849 ms: 1.44x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 414 ms: 1.43x faster                                                       |
| scimark_sor              | 106 ms                                                      | 74.7 ms: 1.42x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 44.2 ms: 1.42x faster                                                      |
| regex_compile            | 106 ms                                                      | 77.4 ms: 1.37x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 37.3 ms: 1.37x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 197 us: 1.37x faster                                                       |
| pycparser                | 930 ms                                                      | 694 ms: 1.34x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 15.3 ms: 1.29x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 39.1 ms: 1.29x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 34.7 ms: 1.28x faster                                                      |
| thrift                   | 617 us                                                      | 484 us: 1.28x faster                                                       |
| sympy_sum                | 107 ms                                                      | 84.5 ms: 1.27x faster                                                      |
| scimark_fft              | 187 ms                                                      | 148 ms: 1.27x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.52 us: 1.26x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 62.1 ms: 1.24x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 12.3 ms: 1.24x faster                                                      |
| fannkuch                 | 256 ms                                                      | 210 ms: 1.22x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.82 us: 1.21x faster                                                      |
| django_template          | 28.9 ms                                                     | 23.9 ms: 1.21x faster                                                      |
| unpack_sequence          | 39.6 ns                                                     | 33.0 ns: 1.20x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.61 sec: 1.19x faster                                                     |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.28 ms: 1.19x faster                                                      |
| nbody                    | 71.3 ms                                                     | 60.0 ms: 1.19x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 34.7 ms: 1.18x faster                                                      |
| regex_dna                | 136 ms                                                      | 116 ms: 1.18x faster                                                       |
| sympy_str                | 194 ms                                                      | 167 ms: 1.16x faster                                                       |
| 2to3                     | 246 ms                                                      | 214 ms: 1.15x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 13.5 ms: 1.14x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 842 us: 1.14x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 85.5 ms: 1.13x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 59.2 ms: 1.13x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 49.8 ms: 1.11x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.5 ms: 1.10x faster                                                      |
| sympy_expand             | 314 ms                                                      | 288 ms: 1.09x faster                                                       |
| unpickle                 | 9.09 us                                                     | 8.43 us: 1.08x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 70.5 ms: 1.08x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.35 us: 1.06x faster                                                      |
| logging_simple           | 6.22 us                                                     | 5.89 us: 1.06x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 61.6 ms: 1.05x faster                                                      |
| pidigits                 | 149 ms                                                      | 144 ms: 1.04x faster                                                       |
| json                     | 3.14 ms                                                     | 3.02 ms: 1.04x faster                                                      |
| telco                    | 3.94 ms                                                     | 3.82 ms: 1.03x faster                                                      |
| async_generators         | 222 ms                                                      | 237 ms: 1.07x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.46 us: 1.09x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 19.3 us: 1.13x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.30 us: 1.20x slower                                                      |
| coverage                 | 39.0 ms                                                     | 47.4 ms: 1.21x slower                                                      |
| python_startup           | 20.6 ms                                                     | 25.2 ms: 1.22x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.2 ms: 1.24x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 92.2 ms: 1.49x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.11 ms: 1.50x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.28 ms: 1.60x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.32x faster                                                               |

Benchmark hidden because not significant (2): unpickle_list, json_loads
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250823-3.15.0a0-6fcac09-JIT/bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.350x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: unknown