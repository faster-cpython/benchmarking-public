# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: tail_call
- machine: windows-amd64
- commit hash: f1d3190
- commit date: 2025-01-07
- overall geometric mean: 1.276x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 225 ms: 1.09x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.71 sec: 1.12x faster                                                     |
| html5lib       | 51.0 ms                                                     | 36.6 ms: 1.40x faster                                                      |
| Geometric mean | (ref)                                                       | 1.20x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 363 ms: 3.06x faster                                                       |
| async_tree_none         | 435 ms                                                      | 161 ms: 2.70x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 203 ms: 2.59x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 369 ms: 1.73x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.47x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 45.8 ms: 1.35x faster                                                      |
| nbody          | 71.3 ms                                                     | 55.8 ms: 1.28x faster                                                      |
| pidigits       | 149 ms                                                      | 155 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 77.2 ms: 1.37x faster                                                      |
| regex_dna      | 136 ms                                                      | 139 ms: 1.02x slower                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.99 ms: 1.20x slower                                                      |
| regex_v8       | 15.4 ms                                                     | 23.7 ms: 1.53x slower                                                      |
| Geometric mean | (ref)                                                       | 1.08x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.67 sec                                                    | 1.15 sec: 1.45x faster                                                     |
| unpickle_pure_python | 183 us                                                      | 126 us: 1.45x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 189 us: 1.43x faster                                                       |
| json_dumps           | 9.16 ms                                                     | 7.33 ms: 1.25x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 40.9 ms: 1.09x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 65.6 ms: 1.01x slower                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 97.9 ms: 1.01x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 61.4 ms: 1.11x slower                                                      |
| json_loads           | 14.0 us                                                     | 19.8 us: 1.41x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.11x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 18.9 ms: 1.22x slower                                                      |
| python_startup         | 20.6 ms                                                     | 25.5 ms: 1.24x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.23x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 19.8 ms                                                     | 13.8 ms: 1.43x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 30.5 ms: 1.35x faster                                                      |
| mako            | 9.03 ms                                                     | 7.19 ms: 1.26x faster                                                      |
| django_template | 28.9 ms                                                     | 23.3 ms: 1.24x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.32x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 107 us: 3.13x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 363 ms: 3.06x faster                                                       |
| async_tree_none          | 435 ms                                                      | 161 ms: 2.70x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 203 ms: 2.59x faster                                                       |
| deltablue                | 4.19 ms                                                     | 1.71 ms: 2.45x faster                                                      |
| generators               | 32.4 ms                                                     | 15.1 ms: 2.15x faster                                                      |
| go                       | 139 ms                                                      | 64.8 ms: 2.14x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 51.3 ns: 1.84x faster                                                      |
| richards_super           | 52.2 ms                                                     | 28.8 ms: 1.81x faster                                                      |
| pylint                   | 350 ms                                                      | 196 ms: 1.79x faster                                                       |
| scimark_sor              | 106 ms                                                      | 60.3 ms: 1.76x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 369 ms: 1.73x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 16.8 us: 1.72x faster                                                      |
| raytrace                 | 273 ms                                                      | 162 ms: 1.69x faster                                                       |
| richards                 | 42.4 ms                                                     | 25.3 ms: 1.68x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 726 us: 1.67x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 3.48 ms: 1.65x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 35.0 ms: 1.64x faster                                                      |
| chaos                    | 61.7 ms                                                     | 37.9 ms: 1.63x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 53.4 ms: 1.61x faster                                                      |
| deepcopy                 | 255 us                                                      | 163 us: 1.57x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 961 us: 1.53x faster                                                       |
| comprehensions           | 16.5 us                                                     | 10.8 us: 1.52x faster                                                      |
| pyflate                  | 409 ms                                                      | 279 ms: 1.47x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.15 sec: 1.45x faster                                                     |
| unpickle_pure_python     | 183 us                                                      | 126 us: 1.45x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 13.8 ms: 1.43x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 189 us: 1.43x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 36.6 ms: 1.40x faster                                                      |
| regex_compile            | 106 ms                                                      | 77.2 ms: 1.37x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 56.4 ms: 1.37x faster                                                      |
| pycparser                | 930 ms                                                      | 680 ms: 1.37x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 30.5 ms: 1.35x faster                                                      |
| float                    | 61.7 ms                                                     | 45.8 ms: 1.35x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 47.7 ms: 1.31x faster                                                      |
| coroutines               | 16.0 ms                                                     | 12.3 ms: 1.30x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 952 ms: 1.28x faster                                                       |
| nbody                    | 71.3 ms                                                     | 55.8 ms: 1.28x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.73 us: 1.27x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 39.9 ms: 1.27x faster                                                      |
| mako                     | 9.03 ms                                                     | 7.19 ms: 1.26x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 472 ms: 1.25x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 7.33 ms: 1.25x faster                                                      |
| django_template          | 28.9 ms                                                     | 23.3 ms: 1.24x faster                                                      |
| sympy_sum                | 107 ms                                                      | 87.0 ms: 1.23x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 12.9 ms: 1.19x faster                                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 33.9 ms: 1.17x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 57.4 ms: 1.16x faster                                                      |
| sympy_str                | 194 ms                                                      | 169 ms: 1.15x faster                                                       |
| scimark_fft              | 187 ms                                                      | 164 ms: 1.14x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 840 us: 1.14x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 181 ms: 1.13x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.69 us: 1.13x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.71 sec: 1.12x faster                                                     |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.42 ms: 1.12x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.62 sec: 1.10x faster                                                     |
| 2to3                     | 246 ms                                                      | 225 ms: 1.09x faster                                                       |
| thrift                   | 617 us                                                      | 568 us: 1.09x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 40.9 ms: 1.09x faster                                                      |
| fannkuch                 | 256 ms                                                      | 237 ms: 1.08x faster                                                       |
| sympy_expand             | 314 ms                                                      | 293 ms: 1.07x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.33 us: 1.07x faster                                                      |
| logging_simple           | 6.22 us                                                     | 5.84 us: 1.07x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 71.6 ms: 1.06x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 65.6 ms: 1.01x slower                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 97.9 ms: 1.01x slower                                                      |
| regex_dna                | 136 ms                                                      | 139 ms: 1.02x slower                                                       |
| pidigits                 | 149 ms                                                      | 155 ms: 1.04x slower                                                       |
| pathlib                  | 75.7 ms                                                     | 79.5 ms: 1.05x slower                                                      |
| async_generators         | 222 ms                                                      | 233 ms: 1.05x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 61.4 ms: 1.11x slower                                                      |
| json                     | 3.14 ms                                                     | 3.58 ms: 1.14x slower                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.99 ms: 1.20x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 18.9 ms: 1.22x slower                                                      |
| python_startup           | 20.6 ms                                                     | 25.5 ms: 1.24x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.92 ms: 1.25x slower                                                      |
| coverage                 | 39.0 ms                                                     | 50.5 ms: 1.29x slower                                                      |
| json_loads               | 14.0 us                                                     | 19.8 us: 1.41x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 93.3 ms: 1.50x slower                                                      |
| regex_v8                 | 15.4 ms                                                     | 23.7 ms: 1.53x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.37 ms: 1.71x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.85 ms: 2.03x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.27x faster                                                               |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250107-3.14.0a3+-f1d3190-CLANG/bm-20250107-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.276x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: unknown