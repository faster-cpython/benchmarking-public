# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: clang_hot
- machine: linux-x86_64
- commit hash: 37fb620
- commit date: 2025-03-06
- overall geometric mean: 1.496x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.35x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-linux-x86_64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 246 ms: 1.42x faster                                                  |
| docutils       | 3.30 sec                                               | 2.56 sec: 1.29x faster                                                |
| html5lib       | 88.9 ms                                                | 58.7 ms: 1.51x faster                                                 |
| Geometric mean | (ref)                                                  | 1.40x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-linux-x86_64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 596 ms: 2.97x faster                                                  |
| async_tree_none         | 728 ms                                                 | 254 ms: 2.86x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 319 ms: 2.73x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 489 ms: 2.08x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.63x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-linux-x86_64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 88.0 ms: 1.74x faster                                                 |
| float          | 117 ms                                                 | 67.8 ms: 1.73x faster                                                 |
| pidigits       | 191 ms                                                 | 202 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.42x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-linux-x86_64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 125 ms: 1.51x faster                                                  |
| regex_dna      | 227 ms                                                 | 195 ms: 1.16x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.39 ms: 1.07x faster                                                 |
| regex_v8       | 27.8 ms                                                | 26.2 ms: 1.06x faster                                                 |
| Geometric mean | (ref)                                                  | 1.19x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-linux-x86_64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.87 sec: 1.68x faster                                                |
| pickle_pure_python   | 484 us                                                 | 310 us: 1.56x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 57.4 ms: 1.38x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 85.5 ms: 1.16x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 101 ms: 1.15x faster                                                  |
| json_dumps           | 14.2 ms                                                | 12.6 ms: 1.13x faster                                                 |
| json_loads           | 31.2 us                                                | 28.5 us: 1.10x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 157 ms: 1.07x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.29x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-linux-x86_64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.05 ms: 1.19x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-linux-x86_64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 30.3 ms: 1.59x faster                                                 |
| genshi_text     | 31.8 ms                                                | 20.9 ms: 1.52x faster                                                 |
| mako            | 16.3 ms                                                | 11.5 ms: 1.42x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 47.7 ms: 1.38x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.48x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-linux-x86_64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 149 us: 3.65x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 596 ms: 2.97x faster                                                  |
| generators               | 80.1 ms                                                | 27.6 ms: 2.91x faster                                                 |
| async_tree_none          | 728 ms                                                 | 254 ms: 2.86x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 319 ms: 2.73x faster                                                  |
| deltablue                | 7.91 ms                                                | 2.90 ms: 2.73x faster                                                 |
| go                       | 240 ms                                                 | 111 ms: 2.17x faster                                                  |
| chaos                    | 115 ms                                                 | 53.3 ms: 2.17x faster                                                 |
| spectral_norm            | 170 ms                                                 | 81.0 ms: 2.10x faster                                                 |
| scimark_sor              | 220 ms                                                 | 105 ms: 2.09x faster                                                  |
| logging_silent           | 190 ns                                                 | 91.0 ns: 2.09x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 489 ms: 2.08x faster                                                  |
| pylint                   | 551 ms                                                 | 271 ms: 2.03x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 28.9 us: 2.02x faster                                                 |
| richards_super           | 94.7 ms                                                | 47.4 ms: 2.00x faster                                                 |
| raytrace                 | 507 ms                                                 | 255 ms: 1.99x faster                                                  |
| deepcopy                 | 479 us                                                 | 245 us: 1.95x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 60.9 ms: 1.94x faster                                                 |
| richards                 | 79.3 ms                                                | 40.9 ms: 1.94x faster                                                 |
| comprehensions           | 28.8 us                                                | 15.6 us: 1.85x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 70.9 ms: 1.80x faster                                                 |
| sqlglot_parse            | 2.17 ms                                                | 1.23 ms: 1.77x faster                                                 |
| hexiom                   | 10.4 ms                                                | 5.89 ms: 1.77x faster                                                 |
| nbody                    | 154 ms                                                 | 88.0 ms: 1.74x faster                                                 |
| pyflate                  | 716 ms                                                 | 412 ms: 1.74x faster                                                  |
| float                    | 117 ms                                                 | 67.8 ms: 1.73x faster                                                 |
| sqlglot_transpile        | 2.57 ms                                                | 1.53 ms: 1.69x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 1.87 sec: 1.68x faster                                                |
| scimark_lu               | 176 ms                                                 | 106 ms: 1.66x faster                                                  |
| coroutines               | 35.1 ms                                                | 21.2 ms: 1.65x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 2.55 us: 1.63x faster                                                 |
| django_template          | 48.2 ms                                                | 30.3 ms: 1.59x faster                                                 |
| scimark_fft              | 466 ms                                                 | 298 ms: 1.56x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.32 us: 1.56x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 310 us: 1.56x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.16 ms: 1.55x faster                                                 |
| logging_format           | 9.09 us                                                | 5.92 us: 1.53x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                                  |
| genshi_text              | 31.8 ms                                                | 20.9 ms: 1.52x faster                                                 |
| html5lib                 | 88.9 ms                                                | 58.7 ms: 1.51x faster                                                 |
| regex_compile            | 188 ms                                                 | 125 ms: 1.51x faster                                                  |
| thrift                   | 1.07 ms                                                | 733 us: 1.46x faster                                                  |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.0 ms: 1.46x faster                                                 |
| 2to3                     | 348 ms                                                 | 246 ms: 1.42x faster                                                  |
| mako                     | 16.3 ms                                                | 11.5 ms: 1.42x faster                                                 |
| nqueens                  | 106 ms                                                 | 74.8 ms: 1.41x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.40x faster                                                |
| sqlglot_normalize        | 143 ms                                                 | 102 ms: 1.39x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 47.7 ms: 1.38x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 57.4 ms: 1.38x faster                                                 |
| sympy_sum                | 196 ms                                                 | 143 ms: 1.37x faster                                                  |
| sqlalchemy_declarative   | 172 ms                                                 | 125 ms: 1.37x faster                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 743 ms: 1.37x faster                                                  |
| pathlib                  | 20.5 ms                                                | 14.9 ms: 1.37x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 18.9 ms: 1.36x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                                |
| dulwich_log              | 84.3 ms                                                | 62.2 ms: 1.36x faster                                                 |
| sympy_str                | 346 ms                                                 | 258 ms: 1.34x faster                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 51.9 ms: 1.33x faster                                                 |
| fannkuch                 | 532 ms                                                 | 402 ms: 1.32x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.56 sec: 1.29x faster                                                |
| sympy_expand             | 566 ms                                                 | 440 ms: 1.29x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 830 us: 1.19x faster                                                  |
| async_generators         | 444 ms                                                 | 375 ms: 1.18x faster                                                  |
| regex_dna                | 227 ms                                                 | 195 ms: 1.16x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 85.5 ms: 1.16x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 101 ms: 1.15x faster                                                  |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                 |
| sqlite_synth             | 3.02 us                                                | 2.65 us: 1.14x faster                                                 |
| json_dumps               | 14.2 ms                                                | 12.6 ms: 1.13x faster                                                 |
| json                     | 5.69 ms                                                | 5.17 ms: 1.10x faster                                                 |
| json_loads               | 31.2 us                                                | 28.5 us: 1.10x faster                                                 |
| meteor_contest           | 120 ms                                                 | 110 ms: 1.09x faster                                                  |
| regex_effbot             | 3.63 ms                                                | 3.39 ms: 1.07x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 157 ms: 1.07x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 26.2 ms: 1.06x faster                                                 |
| mdp                      | 2.85 sec                                               | 2.75 sec: 1.03x faster                                                |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                  |
| telco                    | 7.27 ms                                                | 7.40 ms: 1.02x slower                                                 |
| pidigits                 | 191 ms                                                 | 202 ms: 1.06x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 7.05 ms: 1.19x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 5.04 ms: 1.39x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 2.49 ms: 1.54x slower                                                 |
| bench_mp_pool            | 24.0 ms                                                | 79.9 ms: 3.33x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.47x faster                                                          |

Benchmark hidden because not significant (1): coverage
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250306-3.14.0a5+-37fb620-CLANG/bm-20250306-linux-x86_64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.496x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.38x
- 95% likely to have a speedup of 1.37x
- 99% likely to have a speedup of 1.35x

# Memory
- memory change: 1.27x