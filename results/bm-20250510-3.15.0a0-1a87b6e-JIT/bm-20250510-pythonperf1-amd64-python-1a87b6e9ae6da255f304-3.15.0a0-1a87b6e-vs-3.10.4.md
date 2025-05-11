# Results vs. 3.10.4

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: windows-amd64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.172x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 227 ms: 1.08x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.69 sec: 1.14x faster                                                     |
| html5lib       | 51.0 ms                                                     | 37.6 ms: 1.36x faster                                                      |
| Geometric mean | (ref)                                                       | 1.19x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 398 ms: 2.79x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 208 ms: 2.53x faster                                                       |
| async_tree_none         | 435 ms                                                      | 173 ms: 2.52x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 330 ms: 1.93x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.42x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 44.4 ms: 1.39x faster                                                      |
| nbody          | 71.3 ms                                                     | 58.0 ms: 1.23x faster                                                      |
| Geometric mean | (ref)                                                       | 1.20x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 79.6 ms: 1.33x faster                                                      |
| regex_dna      | 136 ms                                                      | 118 ms: 1.15x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 13.9 ms: 1.11x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                      |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 118 us: 1.55x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.16 sec: 1.44x faster                                                     |
| json_dumps           | 9.16 ms                                                     | 6.75 ms: 1.36x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 209 us: 1.29x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 36.7 ms: 1.21x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 51.4 ms: 1.08x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.48 us: 1.07x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 90.8 ms: 1.07x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 64.3 ms: 1.01x faster                                                      |
| unpickle_list        | 2.71 us                                                     | 2.87 us: 1.06x slower                                                      |
| json_loads           | 14.0 us                                                     | 14.8 us: 1.06x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 20.6 us: 1.20x slower                                                      |
| pickle               | 6.85 us                                                     | 8.29 us: 1.21x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.47 us: 1.26x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.08x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 20.0 ms: 1.29x slower                                                      |
| python_startup         | 20.6 ms                                                     | 26.7 ms: 1.30x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.29x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.66 ms: 1.59x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.5 ms: 1.28x faster                                                      |
| django_template | 28.9 ms                                                     | 24.5 ms: 1.18x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 34.9 ms: 1.18x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.30x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 108 us: 3.10x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 398 ms: 2.79x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 208 ms: 2.53x faster                                                       |
| async_tree_none          | 435 ms                                                      | 173 ms: 2.52x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 32.6 ms: 2.32x faster                                                      |
| mdp                      | 1.78 sec                                                    | 802 ms: 2.22x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.16 ms: 1.94x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 330 ms: 1.93x faster                                                       |
| go                       | 139 ms                                                      | 79.6 ms: 1.74x faster                                                      |
| pylint                   | 350 ms                                                      | 203 ms: 1.73x faster                                                       |
| generators               | 32.4 ms                                                     | 19.4 ms: 1.67x faster                                                      |
| richards_super           | 52.2 ms                                                     | 31.6 ms: 1.65x faster                                                      |
| mako                     | 9.03 ms                                                     | 5.66 ms: 1.59x faster                                                      |
| chaos                    | 61.7 ms                                                     | 38.7 ms: 1.59x faster                                                      |
| raytrace                 | 273 ms                                                      | 175 ms: 1.56x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 118 us: 1.55x faster                                                       |
| richards                 | 42.4 ms                                                     | 27.6 ms: 1.54x faster                                                      |
| pyflate                  | 409 ms                                                      | 268 ms: 1.53x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 19.0 us: 1.52x faster                                                      |
| deepcopy                 | 255 us                                                      | 176 us: 1.46x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 59.5 ms: 1.44x faster                                                      |
| comprehensions           | 16.5 us                                                     | 11.5 us: 1.44x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.16 sec: 1.44x faster                                                     |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.47 sec: 1.44x faster                                                     |
| scimark_sor              | 106 ms                                                      | 74.9 ms: 1.42x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.9 ms: 1.40x faster                                                      |
| float                    | 61.7 ms                                                     | 44.4 ms: 1.39x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.20 ms: 1.37x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.75 ms: 1.36x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 37.6 ms: 1.36x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 548 ms: 1.34x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 46.9 ms: 1.33x faster                                                      |
| regex_compile            | 106 ms                                                      | 79.6 ms: 1.33x faster                                                      |
| pycparser                | 930 ms                                                      | 702 ms: 1.32x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 209 us: 1.29x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 15.5 ms: 1.28x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 60.9 ms: 1.27x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 481 ms: 1.23x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 991 ms: 1.23x faster                                                       |
| nbody                    | 71.3 ms                                                     | 58.0 ms: 1.23x faster                                                      |
| sympy_sum                | 107 ms                                                      | 87.8 ms: 1.22x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.58 us: 1.21x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 36.7 ms: 1.21x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 12.6 ms: 1.21x faster                                                      |
| scimark_fft              | 187 ms                                                      | 156 ms: 1.20x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 42.3 ms: 1.19x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.85 us: 1.19x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.30 ms: 1.19x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.5 ms: 1.18x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 34.9 ms: 1.18x faster                                                      |
| coroutines               | 16.0 ms                                                     | 13.8 ms: 1.16x faster                                                      |
| regex_dna                | 136 ms                                                      | 118 ms: 1.15x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.69 sec: 1.14x faster                                                     |
| sympy_str                | 194 ms                                                      | 171 ms: 1.13x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 13.9 ms: 1.11x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 60.1 ms: 1.11x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 876 us: 1.09x faster                                                       |
| 2to3                     | 246 ms                                                      | 227 ms: 1.08x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 51.4 ms: 1.08x faster                                                      |
| unpickle                 | 9.09 us                                                     | 8.48 us: 1.07x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 90.8 ms: 1.07x faster                                                      |
| sympy_expand             | 314 ms                                                      | 297 ms: 1.06x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                      |
| json                     | 3.14 ms                                                     | 2.99 ms: 1.05x faster                                                      |
| fannkuch                 | 256 ms                                                      | 249 ms: 1.03x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 64.3 ms: 1.01x faster                                                      |
| logging_format           | 6.76 us                                                     | 7.00 us: 1.04x slower                                                      |
| logging_simple           | 6.22 us                                                     | 6.50 us: 1.04x slower                                                      |
| unpack_sequence          | 39.6 ns                                                     | 41.8 ns: 1.05x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 2.87 us: 1.06x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.8 us: 1.06x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.40 ms: 1.12x slower                                                      |
| async_generators         | 222 ms                                                      | 256 ms: 1.15x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 20.6 us: 1.20x slower                                                      |
| pickle                   | 6.85 us                                                     | 8.29 us: 1.21x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.47 us: 1.26x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 20.0 ms: 1.29x slower                                                      |
| python_startup           | 20.6 ms                                                     | 26.7 ms: 1.30x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.19 ms: 1.55x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 97.1 ms: 1.56x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.34 ms: 1.67x slower                                                      |
| logging_silent           | 94.6 ns                                                     | 328 ns: 3.47x slower                                                       |
| coverage                 | 39.0 ms                                                     | 300 ms: 7.69x slower                                                       |
| thrift                   | 617 us                                                      | 100 ms: 162.74x slower                                                     |
| Geometric mean           | (ref)                                                       | 1.13x faster                                                               |

Benchmark hidden because not significant (2): meteor_contest, pidigits
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250510-3.15.0a0-1a87b6e-JIT/bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.172x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: unknown