# Results vs. 3.10.4

- fork: python
- ref: d6dd64ac654898b4ce71
- machine: windows-amd64
- commit hash: d6dd64a
- commit date: 2025-10-12
- overall geometric mean: 1.362x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 212 ms: 1.16x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.60 sec: 1.20x faster                                                     |
| html5lib       | 51.0 ms                                                     | 37.6 ms: 1.36x faster                                                      |
| Geometric mean | (ref)                                                       | 1.23x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 385 ms: 2.88x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 198 ms: 2.65x faster                                                       |
| async_tree_none         | 435 ms                                                      | 172 ms: 2.53x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 334 ms: 1.91x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.46x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 43.8 ms: 1.41x faster                                                      |
| nbody          | 71.3 ms                                                     | 54.5 ms: 1.31x faster                                                      |
| pidigits       | 149 ms                                                      | 147 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.23x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 75.9 ms: 1.40x faster                                                      |
| regex_dna      | 136 ms                                                      | 118 ms: 1.16x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 13.6 ms: 1.14x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                                      |
| Geometric mean | (ref)                                                       | 1.18x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 107 us: 1.72x faster                                                       |
| json_dumps           | 9.16 ms                                                     | 5.52 ms: 1.66x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.09 sec: 1.53x faster                                                     |
| pickle_pure_python   | 270 us                                                      | 194 us: 1.39x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 34.8 ms: 1.28x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 49.2 ms: 1.13x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 87.9 ms: 1.10x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.48 us: 1.07x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.7 ms: 1.04x faster                                                      |
| json_loads           | 14.0 us                                                     | 13.9 us: 1.01x faster                                                      |
| unpickle_list        | 2.71 us                                                     | 2.75 us: 1.01x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 19.1 us: 1.11x slower                                                      |
| pickle               | 6.85 us                                                     | 7.67 us: 1.12x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.22 us: 1.17x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 18.9 ms: 1.22x slower                                                      |
| python_startup         | 20.6 ms                                                     | 25.1 ms: 1.22x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.22x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.28 ms: 1.71x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.5 ms: 1.28x faster                                                      |
| django_template | 28.9 ms                                                     | 24.2 ms: 1.20x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 34.4 ms: 1.19x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.33x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 105 us: 3.21x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 385 ms: 2.88x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 198 ms: 2.65x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 28.8 ms: 2.63x faster                                                      |
| async_tree_none          | 435 ms                                                      | 172 ms: 2.53x faster                                                       |
| mdp                      | 1.78 sec                                                    | 781 ms: 2.28x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 13.5 us: 2.13x faster                                                      |
| deltablue                | 4.19 ms                                                     | 2.14 ms: 1.96x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 334 ms: 1.91x faster                                                       |
| go                       | 139 ms                                                      | 74.6 ms: 1.86x faster                                                      |
| pylint                   | 350 ms                                                      | 192 ms: 1.82x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 43.0 ms: 1.80x faster                                                      |
| richards_super           | 52.2 ms                                                     | 30.0 ms: 1.74x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 54.7 ns: 1.73x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 107 us: 1.72x faster                                                       |
| mako                     | 9.03 ms                                                     | 5.28 ms: 1.71x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.52 ms: 1.66x faster                                                      |
| generators               | 32.4 ms                                                     | 19.6 ms: 1.65x faster                                                      |
| pyflate                  | 409 ms                                                      | 250 ms: 1.64x faster                                                       |
| deepcopy                 | 255 us                                                      | 159 us: 1.61x faster                                                       |
| richards                 | 42.4 ms                                                     | 26.6 ms: 1.60x faster                                                      |
| raytrace                 | 273 ms                                                      | 172 ms: 1.59x faster                                                       |
| comprehensions           | 16.5 us                                                     | 10.5 us: 1.57x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.09 sec: 1.53x faster                                                     |
| chaos                    | 61.7 ms                                                     | 40.6 ms: 1.52x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.40 sec: 1.51x faster                                                     |
| asyncio_tcp              | 732 ms                                                      | 489 ms: 1.50x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 834 ms: 1.46x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 411 ms: 1.44x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.00 ms: 1.43x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.6 ms: 1.41x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 44.4 ms: 1.41x faster                                                      |
| float                    | 61.7 ms                                                     | 43.8 ms: 1.41x faster                                                      |
| scimark_fft              | 187 ms                                                      | 134 ms: 1.40x faster                                                       |
| scimark_sor              | 106 ms                                                      | 76.0 ms: 1.40x faster                                                      |
| regex_compile            | 106 ms                                                      | 75.9 ms: 1.40x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 194 us: 1.39x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 62.2 ms: 1.38x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 37.6 ms: 1.36x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 38.0 ms: 1.33x faster                                                      |
| pycparser                | 930 ms                                                      | 703 ms: 1.32x faster                                                       |
| nbody                    | 71.3 ms                                                     | 54.5 ms: 1.31x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.72 us: 1.28x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 15.5 ms: 1.28x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 34.8 ms: 1.28x faster                                                      |
| sympy_sum                | 107 ms                                                      | 84.4 ms: 1.27x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.53 us: 1.25x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.19 ms: 1.24x faster                                                      |
| thrift                   | 617 us                                                      | 499 us: 1.24x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 12.4 ms: 1.23x faster                                                      |
| fannkuch                 | 256 ms                                                      | 213 ms: 1.20x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.60 sec: 1.20x faster                                                     |
| django_template          | 28.9 ms                                                     | 24.2 ms: 1.20x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 34.4 ms: 1.19x faster                                                      |
| sympy_str                | 194 ms                                                      | 165 ms: 1.18x faster                                                       |
| 2to3                     | 246 ms                                                      | 212 ms: 1.16x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 828 us: 1.16x faster                                                       |
| regex_dna                | 136 ms                                                      | 118 ms: 1.16x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 13.6 ms: 1.14x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 49.2 ms: 1.13x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 59.4 ms: 1.12x faster                                                      |
| unpack_sequence          | 39.6 ns                                                     | 35.6 ns: 1.11x faster                                                      |
| sympy_expand             | 314 ms                                                      | 285 ms: 1.10x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 87.9 ms: 1.10x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.6 ms: 1.10x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.20 us: 1.09x faster                                                      |
| json                     | 3.14 ms                                                     | 2.89 ms: 1.08x faster                                                      |
| logging_simple           | 6.22 us                                                     | 5.77 us: 1.08x faster                                                      |
| unpickle                 | 9.09 us                                                     | 8.48 us: 1.07x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 71.8 ms: 1.06x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.7 ms: 1.04x faster                                                      |
| pidigits                 | 149 ms                                                      | 147 ms: 1.02x faster                                                       |
| telco                    | 3.94 ms                                                     | 3.90 ms: 1.01x faster                                                      |
| json_loads               | 14.0 us                                                     | 13.9 us: 1.01x faster                                                      |
| unpickle_list            | 2.71 us                                                     | 2.75 us: 1.01x slower                                                      |
| async_generators         | 222 ms                                                      | 236 ms: 1.06x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 19.1 us: 1.11x slower                                                      |
| pickle                   | 6.85 us                                                     | 7.67 us: 1.12x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.22 us: 1.17x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 18.9 ms: 1.22x slower                                                      |
| python_startup           | 20.6 ms                                                     | 25.1 ms: 1.22x slower                                                      |
| coverage                 | 39.0 ms                                                     | 50.3 ms: 1.29x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 88.5 ms: 1.43x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.09 ms: 1.48x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.25 ms: 1.57x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.32x faster                                                               |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20251012-3.15.0a0-d6dd64a-JIT/bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.362x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: unknown