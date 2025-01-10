# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: tail_call
- machine: windows-amd64
- commit hash: ac80cdd
- commit date: 2025-01-10
- overall geometric mean: 1.167x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250110-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-ac80cdd |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 231 ms: 1.07x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.71 sec: 1.12x faster                                                     |
| html5lib       | 51.0 ms                                                     | 41.1 ms: 1.24x faster                                                      |
| Geometric mean | (ref)                                                       | 1.14x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250110-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-ac80cdd |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 421 ms: 2.63x faster                                                       |
| async_tree_none         | 435 ms                                                      | 189 ms: 2.31x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 233 ms: 2.26x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 354 ms: 1.80x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.23x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250110-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-ac80cdd |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 53.0 ms: 1.16x faster                                                      |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                                       |
| nbody          | 71.3 ms                                                     | 79.7 ms: 1.12x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250110-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-ac80cdd |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 89.7 ms: 1.18x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.48 ms: 1.12x faster                                                      |
| regex_dna      | 136 ms                                                      | 122 ms: 1.12x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 24.6 ms: 1.59x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250110-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-ac80cdd |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.81 ms: 1.35x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 153 us: 1.20x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 234 us: 1.15x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.47 sec: 1.14x faster                                                     |
| xml_etree_parse      | 96.8 ms                                                     | 89.9 ms: 1.08x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 41.5 ms: 1.07x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.8 ms: 1.02x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 58.1 ms: 1.05x slower                                                      |
| json_loads           | 14.0 us                                                     | 14.8 us: 1.06x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.09x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250110-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-ac80cdd |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 18.1 ms: 1.17x slower                                                      |
| python_startup         | 20.6 ms                                                     | 24.6 ms: 1.19x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.18x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250110-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-ac80cdd |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 7.09 ms: 1.27x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 16.8 ms: 1.18x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 35.3 ms: 1.16x faster                                                      |
| django_template | 28.9 ms                                                     | 25.7 ms: 1.12x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.18x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250110-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-ac80cdd |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 111 us: 3.03x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 421 ms: 2.63x faster                                                       |
| async_tree_none          | 435 ms                                                      | 189 ms: 2.31x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 233 ms: 2.26x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 354 ms: 1.80x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.40 ms: 1.74x faster                                                      |
| pylint                   | 350 ms                                                      | 202 ms: 1.73x faster                                                       |
| generators               | 32.4 ms                                                     | 21.6 ms: 1.50x faster                                                      |
| go                       | 139 ms                                                      | 94.3 ms: 1.47x faster                                                      |
| richards_super           | 52.2 ms                                                     | 36.9 ms: 1.41x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 69.1 ns: 1.37x faster                                                      |
| deepcopy                 | 255 us                                                      | 188 us: 1.36x faster                                                       |
| chaos                    | 61.7 ms                                                     | 45.6 ms: 1.35x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.81 ms: 1.35x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 912 us: 1.33x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 64.8 ms: 1.32x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 21.9 us: 1.32x faster                                                      |
| sqlglot_transpile        | 1.48 ms                                                     | 1.12 ms: 1.31x faster                                                      |
| comprehensions           | 16.5 us                                                     | 12.7 us: 1.30x faster                                                      |
| raytrace                 | 273 ms                                                      | 211 ms: 1.30x faster                                                       |
| richards                 | 42.4 ms                                                     | 33.1 ms: 1.28x faster                                                      |
| mako                     | 9.03 ms                                                     | 7.09 ms: 1.27x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 50.0 ms: 1.25x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 41.1 ms: 1.24x faster                                                      |
| pyflate                  | 409 ms                                                      | 331 ms: 1.24x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.69 ms: 1.22x faster                                                      |
| pycparser                | 930 ms                                                      | 760 ms: 1.22x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.47 sec: 1.21x faster                                                     |
| unpickle_pure_python     | 183 us                                                      | 153 us: 1.20x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.5 ms: 1.19x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 65.1 ms: 1.19x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.61 us: 1.18x faster                                                      |
| regex_compile            | 106 ms                                                      | 89.7 ms: 1.18x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 16.8 ms: 1.18x faster                                                      |
| sympy_sum                | 107 ms                                                      | 91.7 ms: 1.17x faster                                                      |
| float                    | 61.7 ms                                                     | 53.0 ms: 1.16x faster                                                      |
| thrift                   | 617 us                                                      | 530 us: 1.16x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 35.3 ms: 1.16x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 43.4 ms: 1.16x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 234 us: 1.15x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.92 us: 1.15x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 50.0 ms: 1.15x faster                                                      |
| scimark_sor              | 106 ms                                                      | 92.9 ms: 1.14x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 838 us: 1.14x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.47 sec: 1.14x faster                                                     |
| docutils                 | 1.92 sec                                                    | 1.71 sec: 1.12x faster                                                     |
| django_template          | 28.9 ms                                                     | 25.7 ms: 1.12x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.48 ms: 1.12x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.7 ms: 1.12x faster                                                      |
| regex_dna                | 136 ms                                                      | 122 ms: 1.12x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 36.2 ms: 1.10x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.13 sec: 1.08x faster                                                     |
| xml_etree_parse          | 96.8 ms                                                     | 89.9 ms: 1.08x faster                                                      |
| sympy_str                | 194 ms                                                      | 181 ms: 1.08x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 552 ms: 1.07x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 41.5 ms: 1.07x faster                                                      |
| 2to3                     | 246 ms                                                      | 231 ms: 1.07x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 197 ms: 1.04x faster                                                       |
| json                     | 3.14 ms                                                     | 3.04 ms: 1.03x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.64 ms: 1.03x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 64.9 ms: 1.03x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.8 ms: 1.02x faster                                                      |
| sympy_expand             | 314 ms                                                      | 310 ms: 1.02x faster                                                       |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                                       |
| scimark_fft              | 187 ms                                                      | 193 ms: 1.03x slower                                                       |
| meteor_contest           | 75.9 ms                                                     | 78.9 ms: 1.04x slower                                                      |
| logging_format           | 6.76 us                                                     | 7.07 us: 1.05x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 58.1 ms: 1.05x slower                                                      |
| pathlib                  | 75.7 ms                                                     | 79.8 ms: 1.05x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.8 us: 1.06x slower                                                      |
| async_generators         | 222 ms                                                      | 236 ms: 1.07x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.65 us: 1.07x slower                                                      |
| fannkuch                 | 256 ms                                                      | 277 ms: 1.08x slower                                                       |
| nbody                    | 71.3 ms                                                     | 79.7 ms: 1.12x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 18.1 ms: 1.17x slower                                                      |
| python_startup           | 20.6 ms                                                     | 24.6 ms: 1.19x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.81 ms: 1.22x slower                                                      |
| coverage                 | 39.0 ms                                                     | 49.3 ms: 1.26x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.99 ms: 1.41x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 89.4 ms: 1.44x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.24 ms: 1.55x slower                                                      |
| regex_v8                 | 15.4 ms                                                     | 24.6 ms: 1.59x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.16x faster                                                               |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250110-3.14.0a3+-ac80cdd/bm-20250110-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-ac80cdd.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.167x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: unknown