# Results vs. 3.10.4

- fork: python
- ref: 48d0d0dd9733eae4935f
- machine: windows-amd64
- commit hash: 48d0d0d
- commit date: 2025-09-26
- overall geometric mean: 1.351x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 214 ms: 1.15x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.62 sec: 1.19x faster                                                     |
| html5lib       | 51.0 ms                                                     | 38.0 ms: 1.34x faster                                                      |
| Geometric mean | (ref)                                                       | 1.22x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 381 ms: 2.91x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 199 ms: 2.64x faster                                                       |
| async_tree_none         | 435 ms                                                      | 170 ms: 2.56x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 329 ms: 1.94x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.49x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 39.8 ms: 1.55x faster                                                      |
| nbody          | 71.3 ms                                                     | 55.8 ms: 1.28x faster                                                      |
| pidigits       | 149 ms                                                      | 146 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.26x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 77.3 ms: 1.37x faster                                                      |
| regex_dna      | 136 ms                                                      | 115 ms: 1.19x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 13.3 ms: 1.16x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.60 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                       | 1.18x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 105 us: 1.75x faster                                                       |
| json_dumps           | 9.16 ms                                                     | 5.31 ms: 1.73x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.08 sec: 1.55x faster                                                     |
| pickle_pure_python   | 270 us                                                      | 198 us: 1.36x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 35.7 ms: 1.25x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 50.0 ms: 1.11x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 87.6 ms: 1.11x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 61.5 ms: 1.06x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.69 us: 1.05x faster                                                      |
| json_loads           | 14.0 us                                                     | 13.8 us: 1.01x faster                                                      |
| pickle_dict          | 17.2 us                                                     | 19.2 us: 1.12x slower                                                      |
| pickle               | 6.85 us                                                     | 7.65 us: 1.12x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.26 us: 1.18x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.15x faster                                                               |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.2 ms: 1.23x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 19.1 ms: 1.23x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.23x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.34 ms: 1.69x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.7 ms: 1.26x faster                                                      |
| django_template | 28.9 ms                                                     | 24.0 ms: 1.20x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 34.9 ms: 1.17x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.32x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 102 us: 3.29x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 381 ms: 2.91x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 199 ms: 2.64x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 28.9 ms: 2.62x faster                                                      |
| async_tree_none          | 435 ms                                                      | 170 ms: 2.56x faster                                                       |
| mdp                      | 1.78 sec                                                    | 786 ms: 2.27x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 329 ms: 1.94x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.19 ms: 1.91x faster                                                      |
| go                       | 139 ms                                                      | 76.7 ms: 1.81x faster                                                      |
| pylint                   | 350 ms                                                      | 195 ms: 1.80x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 418 ms: 1.75x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 105 us: 1.75x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 54.3 ns: 1.74x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.31 ms: 1.73x faster                                                      |
| richards_super           | 52.2 ms                                                     | 30.6 ms: 1.71x faster                                                      |
| mako                     | 9.03 ms                                                     | 5.34 ms: 1.69x faster                                                      |
| generators               | 32.4 ms                                                     | 19.3 ms: 1.68x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 17.2 us: 1.68x faster                                                      |
| pyflate                  | 409 ms                                                      | 250 ms: 1.64x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.30 sec: 1.63x faster                                                     |
| richards                 | 42.4 ms                                                     | 26.8 ms: 1.58x faster                                                      |
| raytrace                 | 273 ms                                                      | 173 ms: 1.58x faster                                                       |
| comprehensions           | 16.5 us                                                     | 10.5 us: 1.57x faster                                                      |
| deepcopy                 | 255 us                                                      | 164 us: 1.56x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.08 sec: 1.55x faster                                                     |
| float                    | 61.7 ms                                                     | 39.8 ms: 1.55x faster                                                      |
| chaos                    | 61.7 ms                                                     | 40.2 ms: 1.54x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 56.7 ms: 1.51x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 3.92 ms: 1.47x faster                                                      |
| scimark_sor              | 106 ms                                                      | 75.0 ms: 1.41x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 44.6 ms: 1.40x faster                                                      |
| scimark_fft              | 187 ms                                                      | 134 ms: 1.40x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.9 ms: 1.40x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 886 ms: 1.38x faster                                                       |
| regex_compile            | 106 ms                                                      | 77.3 ms: 1.37x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 433 ms: 1.37x faster                                                       |
| pycparser                | 930 ms                                                      | 682 ms: 1.37x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 198 us: 1.36x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 38.0 ms: 1.34x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 38.6 ms: 1.31x faster                                                      |
| nbody                    | 71.3 ms                                                     | 55.8 ms: 1.28x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 60.5 ms: 1.28x faster                                                      |
| sympy_sum                | 107 ms                                                      | 84.2 ms: 1.27x faster                                                      |
| thrift                   | 617 us                                                      | 489 us: 1.26x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 15.7 ms: 1.26x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.76 us: 1.25x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 35.7 ms: 1.25x faster                                                      |
| fannkuch                 | 256 ms                                                      | 207 ms: 1.24x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 12.4 ms: 1.24x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.21 ms: 1.23x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.57 us: 1.22x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.0 ms: 1.20x faster                                                      |
| unpack_sequence          | 39.6 ns                                                     | 33.2 ns: 1.19x faster                                                      |
| regex_dna                | 136 ms                                                      | 115 ms: 1.19x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.62 sec: 1.19x faster                                                     |
| sympy_str                | 194 ms                                                      | 165 ms: 1.18x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 34.9 ms: 1.17x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 13.3 ms: 1.16x faster                                                      |
| coroutines               | 16.0 ms                                                     | 13.9 ms: 1.15x faster                                                      |
| 2to3                     | 246 ms                                                      | 214 ms: 1.15x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 834 us: 1.15x faster                                                       |
| json                     | 3.14 ms                                                     | 2.80 ms: 1.12x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 59.7 ms: 1.12x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 50.0 ms: 1.11x faster                                                      |
| sympy_expand             | 314 ms                                                      | 284 ms: 1.11x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 87.6 ms: 1.11x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 71.4 ms: 1.06x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 61.5 ms: 1.06x faster                                                      |
| unpickle                 | 9.09 us                                                     | 8.69 us: 1.05x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.60 ms: 1.03x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.57 us: 1.03x faster                                                      |
| logging_simple           | 6.22 us                                                     | 6.09 us: 1.02x faster                                                      |
| pidigits                 | 149 ms                                                      | 146 ms: 1.02x faster                                                       |
| json_loads               | 14.0 us                                                     | 13.8 us: 1.01x faster                                                      |
| async_generators         | 222 ms                                                      | 239 ms: 1.08x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 19.2 us: 1.12x slower                                                      |
| pickle                   | 6.85 us                                                     | 7.65 us: 1.12x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.26 us: 1.18x slower                                                      |
| python_startup           | 20.6 ms                                                     | 25.2 ms: 1.23x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.1 ms: 1.23x slower                                                      |
| coverage                 | 39.0 ms                                                     | 49.0 ms: 1.26x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 88.8 ms: 1.43x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.12 ms: 1.50x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.25 ms: 1.57x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.32x faster                                                               |

Benchmark hidden because not significant (2): unpickle_list, telco
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250926-3.15.0a0-48d0d0d-JIT/bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.351x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: unknown