# Results vs. 3.10.4

- fork: brandtbucher
- ref: nojit
- machine: linux-x86_64
- commit hash: f098037
- commit date: 2025-01-07
- overall geometric mean: 1.432x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 260 ms: 1.34x faster                                          |
| docutils       | 3.30 sec                                               | 2.70 sec: 1.22x faster                                        |
| html5lib       | 88.9 ms                                                | 64.1 ms: 1.39x faster                                         |
| Geometric mean | (ref)                                                  | 1.31x faster                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 608 ms: 2.91x faster                                          |
| async_tree_none         | 728 ms                                                 | 259 ms: 2.82x faster                                          |
| async_tree_memoization  | 870 ms                                                 | 326 ms: 2.67x faster                                          |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 493 ms: 2.06x faster                                          |
| Geometric mean          | (ref)                                                  | 2.59x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 85.0 ms: 1.81x faster                                         |
| float          | 117 ms                                                 | 68.1 ms: 1.72x faster                                         |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                          |
| Geometric mean | (ref)                                                  | 1.46x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.47x faster                                          |
| regex_v8       | 27.8 ms                                                | 24.9 ms: 1.11x faster                                         |
| regex_effbot   | 3.63 ms                                                | 3.41 ms: 1.06x faster                                         |
| regex_dna      | 227 ms                                                 | 214 ms: 1.06x faster                                          |
| Geometric mean | (ref)                                                  | 1.16x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 193 us: 1.71x faster                                          |
| tomli_loads          | 3.14 sec                                               | 1.85 sec: 1.70x faster                                        |
| pickle_pure_python   | 484 us                                                 | 325 us: 1.49x faster                                          |
| xml_etree_process    | 79.1 ms                                                | 54.9 ms: 1.44x faster                                         |
| xml_etree_generate   | 99.4 ms                                                | 77.8 ms: 1.28x faster                                         |
| json_dumps           | 14.2 ms                                                | 11.1 ms: 1.27x faster                                         |
| xml_etree_parse      | 168 ms                                                 | 137 ms: 1.22x faster                                          |
| xml_etree_iterparse  | 115 ms                                                 | 94.8 ms: 1.22x faster                                         |
| json_loads           | 31.2 us                                                | 27.1 us: 1.15x faster                                         |
| Geometric mean       | (ref)                                                  | 1.37x faster                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                         |
| python_startup_no_site | 5.93 ms                                                | 7.06 ms: 1.19x slower                                         |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.1 ms: 1.61x faster                                         |
| django_template | 48.2 ms                                                | 32.8 ms: 1.47x faster                                         |
| genshi_text     | 31.8 ms                                                | 24.0 ms: 1.33x faster                                         |
| genshi_xml      | 66.0 ms                                                | 57.4 ms: 1.15x faster                                         |
| Geometric mean  | (ref)                                                  | 1.38x faster                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 166 us: 3.28x faster                                          |
| async_tree_io            | 1.77 sec                                               | 608 ms: 2.91x faster                                          |
| async_tree_none          | 728 ms                                                 | 259 ms: 2.82x faster                                          |
| async_tree_memoization   | 870 ms                                                 | 326 ms: 2.67x faster                                          |
| deltablue                | 7.91 ms                                                | 3.50 ms: 2.26x faster                                         |
| generators               | 80.1 ms                                                | 36.7 ms: 2.18x faster                                         |
| deepcopy_memo            | 58.5 us                                                | 27.8 us: 2.10x faster                                         |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 493 ms: 2.06x faster                                          |
| go                       | 240 ms                                                 | 124 ms: 1.93x faster                                          |
| scimark_sor              | 220 ms                                                 | 115 ms: 1.92x faster                                          |
| scimark_monte_carlo      | 118 ms                                                 | 61.8 ms: 1.91x faster                                         |
| richards_super           | 94.7 ms                                                | 49.7 ms: 1.91x faster                                         |
| chaos                    | 115 ms                                                 | 60.6 ms: 1.91x faster                                         |
| pylint                   | 551 ms                                                 | 291 ms: 1.90x faster                                          |
| crypto_pyaes             | 128 ms                                                 | 68.3 ms: 1.87x faster                                         |
| richards                 | 79.3 ms                                                | 43.1 ms: 1.84x faster                                         |
| deepcopy                 | 479 us                                                 | 265 us: 1.81x faster                                          |
| nbody                    | 154 ms                                                 | 85.0 ms: 1.81x faster                                         |
| raytrace                 | 507 ms                                                 | 282 ms: 1.80x faster                                          |
| logging_silent           | 190 ns                                                 | 108 ns: 1.76x faster                                          |
| float                    | 117 ms                                                 | 68.1 ms: 1.72x faster                                         |
| unpickle_pure_python     | 331 us                                                 | 193 us: 1.71x faster                                          |
| sqlglot_parse            | 2.17 ms                                                | 1.27 ms: 1.71x faster                                         |
| tomli_loads              | 3.14 sec                                               | 1.85 sec: 1.70x faster                                        |
| comprehensions           | 28.8 us                                                | 17.0 us: 1.69x faster                                         |
| sqlglot_transpile        | 2.57 ms                                                | 1.58 ms: 1.63x faster                                         |
| spectral_norm            | 170 ms                                                 | 105 ms: 1.62x faster                                          |
| mako                     | 16.3 ms                                                | 10.1 ms: 1.61x faster                                         |
| pyflate                  | 716 ms                                                 | 449 ms: 1.60x faster                                          |
| scimark_lu               | 176 ms                                                 | 112 ms: 1.57x faster                                          |
| deepcopy_reduce          | 4.17 us                                                | 2.71 us: 1.54x faster                                         |
| scimark_fft              | 466 ms                                                 | 308 ms: 1.51x faster                                          |
| pickle_pure_python       | 484 us                                                 | 325 us: 1.49x faster                                          |
| coroutines               | 35.1 ms                                                | 23.9 ms: 1.47x faster                                         |
| django_template          | 48.2 ms                                                | 32.8 ms: 1.47x faster                                         |
| regex_compile            | 188 ms                                                 | 129 ms: 1.47x faster                                          |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.46 ms: 1.45x faster                                         |
| xml_etree_process        | 79.1 ms                                                | 54.9 ms: 1.44x faster                                         |
| pprint_safe_repr         | 1.02 sec                                               | 709 ms: 1.44x faster                                          |
| hexiom                   | 10.4 ms                                                | 7.24 ms: 1.44x faster                                         |
| logging_format           | 9.09 us                                                | 6.38 us: 1.42x faster                                         |
| logging_simple           | 8.30 us                                                | 5.83 us: 1.42x faster                                         |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.42x faster                                        |
| fannkuch                 | 532 ms                                                 | 379 ms: 1.40x faster                                          |
| html5lib                 | 88.9 ms                                                | 64.1 ms: 1.39x faster                                         |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.0 ms: 1.38x faster                                         |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                        |
| thrift                   | 1.07 ms                                                | 786 us: 1.36x faster                                          |
| 2to3                     | 348 ms                                                 | 260 ms: 1.34x faster                                          |
| genshi_text              | 31.8 ms                                                | 24.0 ms: 1.33x faster                                         |
| sqlglot_normalize        | 143 ms                                                 | 108 ms: 1.32x faster                                          |
| sqlalchemy_declarative   | 172 ms                                                 | 132 ms: 1.30x faster                                          |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                         |
| xml_etree_generate       | 99.4 ms                                                | 77.8 ms: 1.28x faster                                         |
| sqlglot_optimize         | 69.2 ms                                                | 54.2 ms: 1.28x faster                                         |
| json_dumps               | 14.2 ms                                                | 11.1 ms: 1.27x faster                                         |
| dulwich_log              | 84.3 ms                                                | 66.8 ms: 1.26x faster                                         |
| sympy_sum                | 196 ms                                                 | 156 ms: 1.26x faster                                          |
| sympy_integrate          | 25.8 ms                                                | 20.6 ms: 1.25x faster                                         |
| sympy_str                | 346 ms                                                 | 282 ms: 1.23x faster                                          |
| xml_etree_parse          | 168 ms                                                 | 137 ms: 1.22x faster                                          |
| docutils                 | 3.30 sec                                               | 2.70 sec: 1.22x faster                                        |
| xml_etree_iterparse      | 115 ms                                                 | 94.8 ms: 1.22x faster                                         |
| nqueens                  | 106 ms                                                 | 87.4 ms: 1.21x faster                                         |
| sympy_expand             | 566 ms                                                 | 478 ms: 1.18x faster                                          |
| genshi_xml               | 66.0 ms                                                | 57.4 ms: 1.15x faster                                         |
| json_loads               | 31.2 us                                                | 27.1 us: 1.15x faster                                         |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                         |
| json                     | 5.69 ms                                                | 5.03 ms: 1.13x faster                                         |
| regex_v8                 | 27.8 ms                                                | 24.9 ms: 1.11x faster                                         |
| bench_thread_pool        | 986 us                                                 | 891 us: 1.11x faster                                          |
| mdp                      | 2.85 sec                                               | 2.57 sec: 1.11x faster                                        |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                          |
| sqlite_synth             | 3.02 us                                                | 2.76 us: 1.10x faster                                         |
| regex_effbot             | 3.63 ms                                                | 3.41 ms: 1.06x faster                                         |
| regex_dna                | 227 ms                                                 | 214 ms: 1.06x faster                                          |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                          |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                          |
| async_generators         | 444 ms                                                 | 447 ms: 1.01x slower                                          |
| telco                    | 7.27 ms                                                | 7.54 ms: 1.04x slower                                         |
| coverage                 | 79.4 ms                                                | 85.1 ms: 1.07x slower                                         |
| mypy2                    | 894 ms                                                 | 959 ms: 1.07x slower                                          |
| python_startup_no_site   | 5.93 ms                                                | 7.06 ms: 1.19x slower                                         |
| gc_traversal             | 3.62 ms                                                | 4.79 ms: 1.32x slower                                         |
| create_gc_cycles         | 1.62 ms                                                | 2.46 ms: 1.52x slower                                         |
| bench_mp_pool            | 24.0 ms                                                | 81.5 ms: 3.39x slower                                         |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                  |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250107-3.14.0a3+-f098037-JIT/bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.432x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.29x