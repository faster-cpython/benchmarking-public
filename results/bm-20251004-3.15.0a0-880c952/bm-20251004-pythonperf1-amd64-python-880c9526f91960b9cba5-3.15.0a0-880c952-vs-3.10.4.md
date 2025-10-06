# Results vs. 3.10.4

- fork: python
- ref: 880c9526f91960b9cba5
- machine: windows-amd64
- commit hash: 880c952
- commit date: 2025-10-04
- overall geometric mean: 1.306x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 213 ms: 1.15x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.58 sec: 1.21x faster                                                     |
| html5lib       | 51.0 ms                                                     | 37.0 ms: 1.38x faster                                                      |
| Geometric mean | (ref)                                                       | 1.24x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 384 ms: 2.89x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 201 ms: 2.61x faster                                                       |
| async_tree_none         | 435 ms                                                      | 170 ms: 2.55x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 324 ms: 1.97x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.48x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 43.7 ms: 1.41x faster                                                      |
| nbody          | 71.3 ms                                                     | 64.4 ms: 1.11x faster                                                      |
| pidigits       | 149 ms                                                      | 147 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 78.8 ms: 1.35x faster                                                      |
| regex_dna      | 136 ms                                                      | 119 ms: 1.14x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.48 ms: 1.12x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 14.6 ms: 1.05x faster                                                      |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.42 ms: 1.69x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 133 us: 1.38x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 206 us: 1.31x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.36 sec: 1.23x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 38.6 ms: 1.15x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 87.9 ms: 1.10x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 61.9 ms: 1.05x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.77 us: 1.04x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.2 us: 1.02x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 2.87 us: 1.06x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 19.2 us: 1.12x slower                                                      |
| pickle               | 6.85 us                                                     | 7.83 us: 1.14x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.26 us: 1.18x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.09x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.0 ms: 1.22x slower                                                      |
| python_startup         | 20.6 ms                                                     | 25.5 ms: 1.24x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.23x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.60 ms: 1.37x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.1 ms: 1.31x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 33.9 ms: 1.21x faster                                                      |
| django_template | 28.9 ms                                                     | 24.3 ms: 1.19x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.27x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 102 us: 3.29x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 384 ms: 2.89x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 201 ms: 2.61x faster                                                       |
| async_tree_none          | 435 ms                                                      | 170 ms: 2.55x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 29.8 ms: 2.54x faster                                                      |
| mdp                      | 1.78 sec                                                    | 786 ms: 2.26x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 324 ms: 1.97x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.18 ms: 1.92x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 384 ms: 1.91x faster                                                       |
| pylint                   | 350 ms                                                      | 190 ms: 1.84x faster                                                       |
| go                       | 139 ms                                                      | 75.7 ms: 1.84x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 16.8 us: 1.71x faster                                                      |
| richards_super           | 52.2 ms                                                     | 30.7 ms: 1.70x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 55.6 ns: 1.70x faster                                                      |
| generators               | 32.4 ms                                                     | 19.1 ms: 1.69x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.42 ms: 1.69x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.25 sec: 1.68x faster                                                     |
| richards                 | 42.4 ms                                                     | 26.8 ms: 1.58x faster                                                      |
| deepcopy                 | 255 us                                                      | 164 us: 1.56x faster                                                       |
| comprehensions           | 16.5 us                                                     | 10.7 us: 1.54x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 56.0 ms: 1.53x faster                                                      |
| raytrace                 | 273 ms                                                      | 180 ms: 1.52x faster                                                       |
| chaos                    | 61.7 ms                                                     | 40.9 ms: 1.51x faster                                                      |
| pyflate                  | 409 ms                                                      | 280 ms: 1.46x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 39.5 ms: 1.45x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.02 ms: 1.43x faster                                                      |
| float                    | 61.7 ms                                                     | 43.7 ms: 1.41x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 37.0 ms: 1.38x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 133 us: 1.38x faster                                                       |
| scimark_sor              | 106 ms                                                      | 77.2 ms: 1.37x faster                                                      |
| mako                     | 9.03 ms                                                     | 6.60 ms: 1.37x faster                                                      |
| regex_compile            | 106 ms                                                      | 78.8 ms: 1.35x faster                                                      |
| pycparser                | 930 ms                                                      | 696 ms: 1.34x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 47.4 ms: 1.32x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 15.1 ms: 1.31x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 206 us: 1.31x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 38.8 ms: 1.30x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 12.1 ms: 1.26x faster                                                      |
| sympy_sum                | 107 ms                                                      | 85.0 ms: 1.26x faster                                                      |
| thrift                   | 617 us                                                      | 498 us: 1.24x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.36 sec: 1.23x faster                                                     |
| sqlite_synth             | 1.91 us                                                     | 1.56 us: 1.23x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.81 us: 1.22x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.00 sec: 1.22x faster                                                     |
| docutils                 | 1.92 sec                                                    | 1.58 sec: 1.21x faster                                                     |
| genshi_xml               | 41.0 ms                                                     | 33.9 ms: 1.21x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 491 ms: 1.21x faster                                                       |
| django_template          | 28.9 ms                                                     | 24.3 ms: 1.19x faster                                                      |
| sympy_str                | 194 ms                                                      | 166 ms: 1.17x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 65.9 ms: 1.17x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 829 us: 1.16x faster                                                       |
| 2to3                     | 246 ms                                                      | 213 ms: 1.15x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 38.6 ms: 1.15x faster                                                      |
| coroutines               | 16.0 ms                                                     | 13.9 ms: 1.15x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.39 ms: 1.14x faster                                                      |
| regex_dna                | 136 ms                                                      | 119 ms: 1.14x faster                                                       |
| scimark_fft              | 187 ms                                                      | 168 ms: 1.12x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.48 ms: 1.12x faster                                                      |
| sympy_expand             | 314 ms                                                      | 283 ms: 1.11x faster                                                       |
| nbody                    | 71.3 ms                                                     | 64.4 ms: 1.11x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 87.9 ms: 1.10x faster                                                      |
| json                     | 3.14 ms                                                     | 2.90 ms: 1.08x faster                                                      |
| unpack_sequence          | 39.6 ns                                                     | 36.8 ns: 1.08x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 61.8 ms: 1.08x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 14.6 ms: 1.05x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 61.9 ms: 1.05x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.44 us: 1.05x faster                                                      |
| unpickle                 | 9.09 us                                                     | 8.77 us: 1.04x faster                                                      |
| logging_simple           | 6.22 us                                                     | 6.02 us: 1.03x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 74.0 ms: 1.03x faster                                                      |
| pidigits                 | 149 ms                                                      | 147 ms: 1.01x faster                                                       |
| json_loads               | 14.0 us                                                     | 14.2 us: 1.02x slower                                                      |
| async_generators         | 222 ms                                                      | 228 ms: 1.03x slower                                                       |
| fannkuch                 | 256 ms                                                      | 264 ms: 1.03x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.14 ms: 1.05x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 2.87 us: 1.06x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 19.2 us: 1.12x slower                                                      |
| pickle                   | 6.85 us                                                     | 7.83 us: 1.14x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.26 us: 1.18x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.0 ms: 1.22x slower                                                      |
| python_startup           | 20.6 ms                                                     | 25.5 ms: 1.24x slower                                                      |
| coverage                 | 39.0 ms                                                     | 50.6 ms: 1.30x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 88.1 ms: 1.42x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.21 ms: 1.56x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.27 ms: 1.59x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.28x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_generate
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20251004-3.15.0a0-880c952/bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.306x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: unknown