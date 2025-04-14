# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_up_8_6
- machine: linux-x86_64
- commit hash: 008b481
- commit date: 2025-03-31
- overall geometric mean: 1.432x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250331-linux-x86_64-brandtbucher-jit_up_8_6-3.14.0a6+-008b481 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 270 ms: 1.29x faster                                               |
| docutils       | 3.30 sec                                               | 2.72 sec: 1.21x faster                                             |
| html5lib       | 88.9 ms                                                | 62.8 ms: 1.41x faster                                              |
| Geometric mean | (ref)                                                  | 1.30x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250331-linux-x86_64-brandtbucher-jit_up_8_6-3.14.0a6+-008b481 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 618 ms: 2.86x faster                                               |
| async_tree_none         | 728 ms                                                 | 259 ms: 2.81x faster                                               |
| async_tree_memoization  | 870 ms                                                 | 316 ms: 2.75x faster                                               |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 495 ms: 2.05x faster                                               |
| Geometric mean          | (ref)                                                  | 2.60x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250331-linux-x86_64-brandtbucher-jit_up_8_6-3.14.0a6+-008b481 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 117 ms                                                 | 66.3 ms: 1.77x faster                                              |
| nbody          | 154 ms                                                 | 88.6 ms: 1.73x faster                                              |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                  | 1.47x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250331-linux-x86_64-brandtbucher-jit_up_8_6-3.14.0a6+-008b481 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 130 ms: 1.45x faster                                               |
| regex_v8       | 27.8 ms                                                | 22.8 ms: 1.22x faster                                              |
| regex_effbot   | 3.63 ms                                                | 3.23 ms: 1.12x faster                                              |
| regex_dna      | 227 ms                                                 | 213 ms: 1.07x faster                                               |
| Geometric mean | (ref)                                                  | 1.21x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250331-linux-x86_64-brandtbucher-jit_up_8_6-3.14.0a6+-008b481 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.87 sec: 1.68x faster                                             |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                               |
| pickle_pure_python   | 484 us                                                 | 325 us: 1.49x faster                                               |
| xml_etree_process    | 79.1 ms                                                | 56.8 ms: 1.39x faster                                              |
| xml_etree_generate   | 99.4 ms                                                | 80.9 ms: 1.23x faster                                              |
| json_dumps           | 14.2 ms                                                | 11.6 ms: 1.23x faster                                              |
| xml_etree_parse      | 168 ms                                                 | 140 ms: 1.20x faster                                               |
| xml_etree_iterparse  | 115 ms                                                 | 98.4 ms: 1.17x faster                                              |
| json_loads           | 31.2 us                                                | 29.7 us: 1.05x faster                                              |
| Geometric mean       | (ref)                                                  | 1.32x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250331-linux-x86_64-brandtbucher-jit_up_8_6-3.14.0a6+-008b481 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.12x faster                                              |
| python_startup_no_site | 5.93 ms                                                | 8.18 ms: 1.38x slower                                              |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250331-linux-x86_64-brandtbucher-jit_up_8_6-3.14.0a6+-008b481 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 21.3 ms: 1.50x faster                                              |
| django_template | 48.2 ms                                                | 32.3 ms: 1.49x faster                                              |
| mako            | 16.3 ms                                                | 11.1 ms: 1.48x faster                                              |
| genshi_xml      | 66.0 ms                                                | 50.6 ms: 1.31x faster                                              |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250331-linux-x86_64-brandtbucher-jit_up_8_6-3.14.0a6+-008b481 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 169 us: 3.23x faster                                               |
| async_tree_io            | 1.77 sec                                               | 618 ms: 2.86x faster                                               |
| async_tree_none          | 728 ms                                                 | 259 ms: 2.81x faster                                               |
| async_tree_memoization   | 870 ms                                                 | 316 ms: 2.75x faster                                               |
| generators               | 80.1 ms                                                | 29.4 ms: 2.73x faster                                              |
| deltablue                | 7.91 ms                                                | 3.05 ms: 2.59x faster                                              |
| richards_super           | 94.7 ms                                                | 43.0 ms: 2.20x faster                                              |
| richards                 | 79.3 ms                                                | 37.4 ms: 2.12x faster                                              |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 495 ms: 2.05x faster                                               |
| deepcopy_memo            | 58.5 us                                                | 29.2 us: 2.01x faster                                              |
| logging_silent           | 190 ns                                                 | 96.8 ns: 1.96x faster                                              |
| chaos                    | 115 ms                                                 | 59.7 ms: 1.94x faster                                              |
| pylint                   | 551 ms                                                 | 288 ms: 1.91x faster                                               |
| raytrace                 | 507 ms                                                 | 268 ms: 1.89x faster                                               |
| go                       | 240 ms                                                 | 129 ms: 1.86x faster                                               |
| scimark_sor              | 220 ms                                                 | 121 ms: 1.82x faster                                               |
| deepcopy                 | 479 us                                                 | 265 us: 1.81x faster                                               |
| spectral_norm            | 170 ms                                                 | 95.5 ms: 1.78x faster                                              |
| float                    | 117 ms                                                 | 66.3 ms: 1.77x faster                                              |
| nbody                    | 154 ms                                                 | 88.6 ms: 1.73x faster                                              |
| scimark_monte_carlo      | 118 ms                                                 | 68.5 ms: 1.72x faster                                              |
| crypto_pyaes             | 128 ms                                                 | 76.2 ms: 1.68x faster                                              |
| tomli_loads              | 3.14 sec                                               | 1.87 sec: 1.68x faster                                             |
| pyflate                  | 716 ms                                                 | 460 ms: 1.56x faster                                               |
| comprehensions           | 28.8 us                                                | 18.6 us: 1.55x faster                                              |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                               |
| logging_simple           | 8.30 us                                                | 5.51 us: 1.51x faster                                              |
| hexiom                   | 10.4 ms                                                | 6.94 ms: 1.50x faster                                              |
| genshi_text              | 31.8 ms                                                | 21.3 ms: 1.50x faster                                              |
| deepcopy_reduce          | 4.17 us                                                | 2.79 us: 1.49x faster                                              |
| django_template          | 48.2 ms                                                | 32.3 ms: 1.49x faster                                              |
| pickle_pure_python       | 484 us                                                 | 325 us: 1.49x faster                                               |
| logging_format           | 9.09 us                                                | 6.14 us: 1.48x faster                                              |
| scimark_fft              | 466 ms                                                 | 315 ms: 1.48x faster                                               |
| mako                     | 16.3 ms                                                | 11.1 ms: 1.48x faster                                              |
| coroutines               | 35.1 ms                                                | 23.8 ms: 1.47x faster                                              |
| scimark_lu               | 176 ms                                                 | 120 ms: 1.47x faster                                               |
| regex_compile            | 188 ms                                                 | 130 ms: 1.45x faster                                               |
| html5lib                 | 88.9 ms                                                | 62.8 ms: 1.41x faster                                              |
| dulwich_log              | 84.3 ms                                                | 60.4 ms: 1.40x faster                                              |
| thrift                   | 1.07 ms                                                | 769 us: 1.39x faster                                               |
| xml_etree_process        | 79.1 ms                                                | 56.8 ms: 1.39x faster                                              |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.66 ms: 1.39x faster                                              |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.4 ms: 1.34x faster                                              |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.34x faster                                             |
| pprint_safe_repr         | 1.02 sec                                               | 766 ms: 1.33x faster                                               |
| pprint_pformat           | 2.10 sec                                               | 1.61 sec: 1.31x faster                                             |
| genshi_xml               | 66.0 ms                                                | 50.6 ms: 1.31x faster                                              |
| 2to3                     | 348 ms                                                 | 270 ms: 1.29x faster                                               |
| sympy_sum                | 196 ms                                                 | 156 ms: 1.26x faster                                               |
| sympy_integrate          | 25.8 ms                                                | 20.5 ms: 1.26x faster                                              |
| nqueens                  | 106 ms                                                 | 84.9 ms: 1.25x faster                                              |
| fannkuch                 | 532 ms                                                 | 428 ms: 1.24x faster                                               |
| sympy_str                | 346 ms                                                 | 280 ms: 1.24x faster                                               |
| xml_etree_generate       | 99.4 ms                                                | 80.9 ms: 1.23x faster                                              |
| json_dumps               | 14.2 ms                                                | 11.6 ms: 1.23x faster                                              |
| sqlalchemy_declarative   | 172 ms                                                 | 141 ms: 1.22x faster                                               |
| regex_v8                 | 27.8 ms                                                | 22.8 ms: 1.22x faster                                              |
| pathlib                  | 20.5 ms                                                | 16.8 ms: 1.22x faster                                              |
| docutils                 | 3.30 sec                                               | 2.72 sec: 1.21x faster                                             |
| xml_etree_parse          | 168 ms                                                 | 140 ms: 1.20x faster                                               |
| sympy_expand             | 566 ms                                                 | 480 ms: 1.18x faster                                               |
| xml_etree_iterparse      | 115 ms                                                 | 98.4 ms: 1.17x faster                                              |
| mdp                      | 2.85 sec                                               | 2.52 sec: 1.13x faster                                             |
| regex_effbot             | 3.63 ms                                                | 3.23 ms: 1.12x faster                                              |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.12x faster                                              |
| sqlite_synth             | 3.02 us                                                | 2.72 us: 1.11x faster                                              |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                               |
| bench_thread_pool        | 986 us                                                 | 897 us: 1.10x faster                                               |
| json                     | 5.69 ms                                                | 5.29 ms: 1.08x faster                                              |
| regex_dna                | 227 ms                                                 | 213 ms: 1.07x faster                                               |
| async_generators         | 444 ms                                                 | 420 ms: 1.06x faster                                               |
| json_loads               | 31.2 us                                                | 29.7 us: 1.05x faster                                              |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                               |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                               |
| coverage                 | 79.4 ms                                                | 86.1 ms: 1.08x slower                                              |
| telco                    | 7.27 ms                                                | 7.89 ms: 1.09x slower                                              |
| python_startup_no_site   | 5.93 ms                                                | 8.18 ms: 1.38x slower                                              |
| gc_traversal             | 3.62 ms                                                | 5.00 ms: 1.38x slower                                              |
| create_gc_cycles         | 1.62 ms                                                | 2.50 ms: 1.54x slower                                              |
| bench_mp_pool            | 24.0 ms                                                | 83.8 ms: 3.49x slower                                              |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                       |
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250331-3.14.0a6+-008b481-JIT/bm-20250331-linux-x86_64-brandtbucher-jit_up_8_6-3.14.0a6+-008b481.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.432x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.31x