# Results vs. 3.10.4

- fork: python
- ref: 880c9526f91960b9cba5
- machine: windows-amd64
- commit hash: 880c952
- commit date: 2025-10-04
- overall geometric mean: 1.201x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 218 ms: 1.13x faster                                                       |
| docutils       | 1.92 sec                                                    | 2.81 sec: 1.46x slower                                                     |
| html5lib       | 51.0 ms                                                     | 39.4 ms: 1.29x faster                                                      |
| Geometric mean | (ref)                                                       | 1.00x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 342 ms: 3.24x faster                                                       |
| async_tree_none         | 435 ms                                                      | 165 ms: 2.63x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 202 ms: 2.60x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 327 ms: 1.95x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.57x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 44.3 ms: 1.39x faster                                                      |
| pidigits       | 149 ms                                                      | 136 ms: 1.10x faster                                                       |
| nbody          | 71.3 ms                                                     | 78.1 ms: 1.10x slower                                                      |
| Geometric mean | (ref)                                                       | 1.12x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 112 ms: 1.21x faster                                                       |
| regex_compile  | 106 ms                                                      | 88.7 ms: 1.20x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 13.3 ms: 1.16x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.54 ms: 1.08x faster                                                      |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.07 ms: 1.51x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 151 us: 1.21x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 223 us: 1.21x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 58.5 ms: 1.11x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 90.5 ms: 1.07x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 43.4 ms: 1.02x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 61.6 ms: 1.11x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.13 us: 1.14x slower                                                      |
| json_loads           | 14.0 us                                                     | 16.0 us: 1.14x slower                                                      |
| pickle               | 6.85 us                                                     | 7.85 us: 1.15x slower                                                      |
| unpickle             | 9.09 us                                                     | 10.4 us: 1.15x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 3.13 us: 1.15x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 20.3 us: 1.18x slower                                                      |
| tomli_loads          | 1.67 sec                                                    | 2.31 sec: 1.38x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.2 ms: 1.24x slower                                                      |
| python_startup         | 20.6 ms                                                     | 25.8 ms: 1.25x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.24x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 28.9 ms                                                     | 25.7 ms: 1.13x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 37.8 ms: 1.08x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 18.5 ms: 1.07x faster                                                      |
| mako            | 9.03 ms                                                     | 9.68 ms: 1.07x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.05x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io            | 1.11 sec                                                    | 342 ms: 3.24x faster                                                       |
| typing_runtime_protocols | 336 us                                                      | 125 us: 2.69x faster                                                       |
| async_tree_none          | 435 ms                                                      | 165 ms: 2.63x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 202 ms: 2.60x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 29.2 ms: 2.59x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 327 ms: 1.95x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.31 ms: 1.81x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.00 sec: 1.77x faster                                                     |
| pylint                   | 350 ms                                                      | 203 ms: 1.73x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 58.6 ns: 1.62x faster                                                      |
| go                       | 139 ms                                                      | 86.4 ms: 1.61x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 457 ms: 1.60x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 18.1 us: 1.59x faster                                                      |
| generators               | 32.4 ms                                                     | 21.1 ms: 1.53x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.07 ms: 1.51x faster                                                      |
| richards_super           | 52.2 ms                                                     | 36.4 ms: 1.44x faster                                                      |
| comprehensions           | 16.5 us                                                     | 11.5 us: 1.43x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 60.8 ms: 1.41x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.36 us: 1.40x faster                                                      |
| deepcopy                 | 255 us                                                      | 183 us: 1.40x faster                                                       |
| float                    | 61.7 ms                                                     | 44.3 ms: 1.39x faster                                                      |
| pyflate                  | 409 ms                                                      | 298 ms: 1.37x faster                                                       |
| chaos                    | 61.7 ms                                                     | 45.0 ms: 1.37x faster                                                      |
| richards                 | 42.4 ms                                                     | 31.1 ms: 1.36x faster                                                      |
| pycparser                | 930 ms                                                      | 685 ms: 1.36x faster                                                       |
| raytrace                 | 273 ms                                                      | 202 ms: 1.35x faster                                                       |
| scimark_sor              | 106 ms                                                      | 80.2 ms: 1.32x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.34 ms: 1.32x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 39.4 ms: 1.29x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 40.8 ms: 1.24x faster                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.16 ms: 1.22x faster                                                      |
| regex_dna                | 136 ms                                                      | 112 ms: 1.21x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 151 us: 1.21x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 223 us: 1.21x faster                                                       |
| regex_compile            | 106 ms                                                      | 88.7 ms: 1.20x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 49.0 ms: 1.17x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 13.3 ms: 1.16x faster                                                      |
| sympy_sum                | 107 ms                                                      | 93.0 ms: 1.15x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 54.5 ms: 1.15x faster                                                      |
| 2to3                     | 246 ms                                                      | 218 ms: 1.13x faster                                                       |
| django_template          | 28.9 ms                                                     | 25.7 ms: 1.13x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 526 ms: 1.13x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.6 ms: 1.12x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.3 ms: 1.12x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 58.5 ms: 1.11x faster                                                      |
| pidigits                 | 149 ms                                                      | 136 ms: 1.10x faster                                                       |
| thrift                   | 617 us                                                      | 564 us: 1.09x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 2.02 us: 1.09x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 37.8 ms: 1.08x faster                                                      |
| sympy_str                | 194 ms                                                      | 180 ms: 1.08x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.54 ms: 1.08x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 71.7 ms: 1.08x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 18.5 ms: 1.07x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 90.5 ms: 1.07x faster                                                      |
| scimark_fft              | 187 ms                                                      | 179 ms: 1.05x faster                                                       |
| unpack_sequence          | 39.6 ns                                                     | 38.5 ns: 1.03x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 43.4 ms: 1.02x faster                                                      |
| json                     | 3.14 ms                                                     | 3.07 ms: 1.02x faster                                                      |
| sympy_expand             | 314 ms                                                      | 308 ms: 1.02x faster                                                       |
| logging_simple           | 6.22 us                                                     | 6.42 us: 1.03x slower                                                      |
| logging_format           | 6.76 us                                                     | 6.99 us: 1.03x slower                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.84 ms: 1.04x slower                                                      |
| nqueens                  | 66.6 ms                                                     | 70.9 ms: 1.06x slower                                                      |
| bench_thread_pool        | 958 us                                                      | 1.02 ms: 1.07x slower                                                      |
| mako                     | 9.03 ms                                                     | 9.68 ms: 1.07x slower                                                      |
| nbody                    | 71.3 ms                                                     | 78.1 ms: 1.10x slower                                                      |
| async_generators         | 222 ms                                                      | 246 ms: 1.11x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 61.6 ms: 1.11x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 85.2 ms: 1.12x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.13 us: 1.14x slower                                                      |
| json_loads               | 14.0 us                                                     | 16.0 us: 1.14x slower                                                      |
| fannkuch                 | 256 ms                                                      | 293 ms: 1.15x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.85 us: 1.15x slower                                                      |
| unpickle                 | 9.09 us                                                     | 10.4 us: 1.15x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 3.13 us: 1.15x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 20.3 us: 1.18x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 74.4 ms: 1.20x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.2 ms: 1.24x slower                                                      |
| python_startup           | 20.6 ms                                                     | 25.8 ms: 1.25x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.97 ms: 1.26x slower                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.57 sec: 1.28x slower                                                     |
| create_gc_cycles         | 800 us                                                      | 1.09 ms: 1.36x slower                                                      |
| tomli_loads              | 1.67 sec                                                    | 2.31 sec: 1.38x slower                                                     |
| docutils                 | 1.92 sec                                                    | 2.81 sec: 1.46x slower                                                     |
| coverage                 | 39.0 ms                                                     | 66.3 ms: 1.70x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.17x faster                                                               |

Benchmark hidden because not significant (1): asyncio_tcp_ssl
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20251004-3.15.0a0-880c952-NOGIL/bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.201x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: unknown