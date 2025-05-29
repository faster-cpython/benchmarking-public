# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: clang_hot
- machine: windows-amd64
- commit hash: 37fb620
- commit date: 2025-03-06
- overall geometric mean: 1.196x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-pythonperf1-amd64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 229 ms: 1.07x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.77 sec: 1.09x faster                                                     |
| html5lib       | 51.0 ms                                                     | 39.3 ms: 1.30x faster                                                      |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-pythonperf1-amd64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 409 ms: 2.71x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 210 ms: 2.50x faster                                                       |
| async_tree_none         | 435 ms                                                      | 181 ms: 2.41x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 362 ms: 1.76x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.32x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-pythonperf1-amd64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 46.4 ms: 1.33x faster                                                      |
| nbody          | 71.3 ms                                                     | 69.2 ms: 1.03x faster                                                      |
| pidigits       | 149 ms                                                      | 156 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                       | 1.09x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-pythonperf1-amd64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 86.3 ms: 1.23x faster                                                      |
| regex_dna      | 136 ms                                                      | 131 ms: 1.04x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 16.7 ms: 1.08x slower                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.87 ms: 1.13x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-pythonperf1-amd64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.67 sec                                                    | 1.34 sec: 1.25x faster                                                     |
| unpickle_pure_python | 183 us                                                      | 149 us: 1.23x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 219 us: 1.23x faster                                                       |
| json_dumps           | 9.16 ms                                                     | 7.86 ms: 1.17x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 46.1 ms: 1.04x slower                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 102 ms: 1.05x slower                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 70.3 ms: 1.08x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 66.5 ms: 1.20x slower                                                      |
| json_loads           | 14.0 us                                                     | 20.3 us: 1.45x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-pythonperf1-amd64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 20.4 ms: 1.32x slower                                                      |
| python_startup         | 20.6 ms                                                     | 27.3 ms: 1.32x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.32x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-pythonperf1-amd64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 19.8 ms                                                     | 15.2 ms: 1.30x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 33.1 ms: 1.24x faster                                                      |
| django_template | 28.9 ms                                                     | 25.6 ms: 1.13x faster                                                      |
| mako            | 9.03 ms                                                     | 8.19 ms: 1.10x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.19x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-pythonperf1-amd64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 111 us: 3.02x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 409 ms: 2.71x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 210 ms: 2.50x faster                                                       |
| async_tree_none          | 435 ms                                                      | 181 ms: 2.41x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 31.9 ms: 2.37x faster                                                      |
| deltablue                | 4.19 ms                                                     | 1.89 ms: 2.22x faster                                                      |
| generators               | 32.4 ms                                                     | 17.6 ms: 1.84x faster                                                      |
| go                       | 139 ms                                                      | 76.6 ms: 1.81x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 362 ms: 1.76x faster                                                       |
| pylint                   | 350 ms                                                      | 206 ms: 1.70x faster                                                       |
| richards_super           | 52.2 ms                                                     | 33.4 ms: 1.56x faster                                                      |
| raytrace                 | 273 ms                                                      | 175 ms: 1.56x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 61.6 ns: 1.54x faster                                                      |
| chaos                    | 61.7 ms                                                     | 41.1 ms: 1.50x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 19.8 us: 1.46x faster                                                      |
| scimark_sor              | 106 ms                                                      | 73.2 ms: 1.45x faster                                                      |
| richards                 | 42.4 ms                                                     | 29.3 ms: 1.45x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 843 us: 1.44x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.6 us: 1.42x faster                                                      |
| deepcopy                 | 255 us                                                      | 181 us: 1.41x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.9 ms: 1.40x faster                                                      |
| sqlglot_transpile        | 1.48 ms                                                     | 1.05 ms: 1.40x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.13 ms: 1.39x faster                                                      |
| pyflate                  | 409 ms                                                      | 304 ms: 1.35x faster                                                       |
| float                    | 61.7 ms                                                     | 46.4 ms: 1.33x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 59.3 ms: 1.30x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 65.9 ms: 1.30x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 15.2 ms: 1.30x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 39.3 ms: 1.30x faster                                                      |
| pycparser                | 930 ms                                                      | 724 ms: 1.29x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.34 sec: 1.25x faster                                                     |
| genshi_xml               | 41.0 ms                                                     | 33.1 ms: 1.24x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 149 us: 1.23x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 219 us: 1.23x faster                                                       |
| regex_compile            | 106 ms                                                      | 86.3 ms: 1.23x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 51.7 ms: 1.21x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 42.4 ms: 1.19x faster                                                      |
| coroutines               | 16.0 ms                                                     | 13.5 ms: 1.19x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.63 us: 1.17x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 7.86 ms: 1.17x faster                                                      |
| sympy_sum                | 107 ms                                                      | 92.5 ms: 1.16x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.94 us: 1.14x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.07 sec: 1.13x faster                                                     |
| thrift                   | 617 us                                                      | 546 us: 1.13x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.6 ms: 1.13x faster                                                      |
| django_template          | 28.9 ms                                                     | 25.6 ms: 1.13x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 534 ms: 1.11x faster                                                       |
| mako                     | 9.03 ms                                                     | 8.19 ms: 1.10x faster                                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 36.1 ms: 1.10x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.63 sec: 1.09x faster                                                     |
| bench_thread_pool        | 958 us                                                      | 881 us: 1.09x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.77 sec: 1.09x faster                                                     |
| sympy_str                | 194 ms                                                      | 181 ms: 1.08x faster                                                       |
| 2to3                     | 246 ms                                                      | 229 ms: 1.07x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 195 ms: 1.05x faster                                                       |
| regex_dna                | 136 ms                                                      | 131 ms: 1.04x faster                                                       |
| nbody                    | 71.3 ms                                                     | 69.2 ms: 1.03x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 64.7 ms: 1.03x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 74.1 ms: 1.02x faster                                                      |
| sympy_expand             | 314 ms                                                      | 308 ms: 1.02x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.67 ms: 1.02x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.81 us: 1.01x slower                                                      |
| scimark_fft              | 187 ms                                                      | 190 ms: 1.01x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.34 us: 1.02x slower                                                      |
| async_generators         | 222 ms                                                      | 227 ms: 1.02x slower                                                       |
| xml_etree_process        | 44.5 ms                                                     | 46.1 ms: 1.04x slower                                                      |
| pidigits                 | 149 ms                                                      | 156 ms: 1.05x slower                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 102 ms: 1.05x slower                                                       |
| regex_v8                 | 15.4 ms                                                     | 16.7 ms: 1.08x slower                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 70.3 ms: 1.08x slower                                                      |
| fannkuch                 | 256 ms                                                      | 286 ms: 1.12x slower                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.87 ms: 1.13x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 66.5 ms: 1.20x slower                                                      |
| json                     | 3.14 ms                                                     | 3.82 ms: 1.22x slower                                                      |
| telco                    | 3.94 ms                                                     | 5.18 ms: 1.32x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 20.4 ms: 1.32x slower                                                      |
| python_startup           | 20.6 ms                                                     | 27.3 ms: 1.32x slower                                                      |
| coverage                 | 39.0 ms                                                     | 53.2 ms: 1.36x slower                                                      |
| json_loads               | 14.0 us                                                     | 20.3 us: 1.45x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 92.2 ms: 1.49x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.37 ms: 1.71x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.77 ms: 1.96x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.19x faster                                                               |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250306-3.14.0a5+-37fb620-CLANG/bm-20250306-pythonperf1-amd64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.196x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: unknown