# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_up_11_7
- machine: linux-x86_64
- commit hash: a70757e
- commit date: 2025-03-28
- overall geometric mean: 1.440x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250328-linux-x86_64-brandtbucher-jit_up_11_7-3.14.0a6+-a70757e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 264 ms: 1.32x faster                                                |
| docutils       | 3.30 sec                                               | 2.68 sec: 1.23x faster                                              |
| html5lib       | 88.9 ms                                                | 63.2 ms: 1.41x faster                                               |
| Geometric mean | (ref)                                                  | 1.32x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250328-linux-x86_64-brandtbucher-jit_up_11_7-3.14.0a6+-a70757e |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 616 ms: 2.87x faster                                                |
| async_tree_none         | 728 ms                                                 | 260 ms: 2.80x faster                                                |
| async_tree_memoization  | 870 ms                                                 | 317 ms: 2.74x faster                                                |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 489 ms: 2.08x faster                                                |
| Geometric mean          | (ref)                                                  | 2.60x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250328-linux-x86_64-brandtbucher-jit_up_11_7-3.14.0a6+-a70757e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 117 ms                                                 | 65.3 ms: 1.79x faster                                               |
| nbody          | 154 ms                                                 | 88.9 ms: 1.73x faster                                               |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                                |
| Geometric mean | (ref)                                                  | 1.47x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250328-linux-x86_64-brandtbucher-jit_up_11_7-3.14.0a6+-a70757e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.47x faster                                                |
| regex_v8       | 27.8 ms                                                | 22.9 ms: 1.21x faster                                               |
| regex_effbot   | 3.63 ms                                                | 3.10 ms: 1.17x faster                                               |
| regex_dna      | 227 ms                                                 | 211 ms: 1.07x faster                                                |
| Geometric mean | (ref)                                                  | 1.22x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250328-linux-x86_64-brandtbucher-jit_up_11_7-3.14.0a6+-a70757e |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.87 sec: 1.68x faster                                              |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                                |
| pickle_pure_python   | 484 us                                                 | 325 us: 1.49x faster                                                |
| xml_etree_process    | 79.1 ms                                                | 56.6 ms: 1.40x faster                                               |
| xml_etree_generate   | 99.4 ms                                                | 80.5 ms: 1.23x faster                                               |
| json_dumps           | 14.2 ms                                                | 11.6 ms: 1.22x faster                                               |
| xml_etree_parse      | 168 ms                                                 | 140 ms: 1.20x faster                                                |
| xml_etree_iterparse  | 115 ms                                                 | 98.2 ms: 1.18x faster                                               |
| json_loads           | 31.2 us                                                | 30.0 us: 1.04x faster                                               |
| Geometric mean       | (ref)                                                  | 1.32x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250328-linux-x86_64-brandtbucher-jit_up_11_7-3.14.0a6+-a70757e |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.11x faster                                               |
| python_startup_no_site | 5.93 ms                                                | 8.21 ms: 1.38x slower                                               |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250328-linux-x86_64-brandtbucher-jit_up_11_7-3.14.0a6+-a70757e |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.9 ms: 1.49x faster                                               |
| genshi_text     | 31.8 ms                                                | 21.5 ms: 1.48x faster                                               |
| django_template | 48.2 ms                                                | 32.9 ms: 1.47x faster                                               |
| genshi_xml      | 66.0 ms                                                | 49.8 ms: 1.33x faster                                               |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250328-linux-x86_64-brandtbucher-jit_up_11_7-3.14.0a6+-a70757e |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 170 us: 3.21x faster                                                |
| async_tree_io            | 1.77 sec                                               | 616 ms: 2.87x faster                                                |
| async_tree_none          | 728 ms                                                 | 260 ms: 2.80x faster                                                |
| generators               | 80.1 ms                                                | 29.1 ms: 2.76x faster                                               |
| async_tree_memoization   | 870 ms                                                 | 317 ms: 2.74x faster                                                |
| deltablue                | 7.91 ms                                                | 3.08 ms: 2.57x faster                                               |
| richards_super           | 94.7 ms                                                | 41.2 ms: 2.30x faster                                               |
| richards                 | 79.3 ms                                                | 36.8 ms: 2.15x faster                                               |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 489 ms: 2.08x faster                                                |
| deepcopy_memo            | 58.5 us                                                | 29.5 us: 1.98x faster                                               |
| pylint                   | 551 ms                                                 | 282 ms: 1.95x faster                                                |
| logging_silent           | 190 ns                                                 | 98.1 ns: 1.93x faster                                               |
| chaos                    | 115 ms                                                 | 59.8 ms: 1.93x faster                                               |
| raytrace                 | 507 ms                                                 | 266 ms: 1.91x faster                                                |
| go                       | 240 ms                                                 | 127 ms: 1.89x faster                                                |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.83x faster                                                |
| deepcopy                 | 479 us                                                 | 264 us: 1.81x faster                                                |
| float                    | 117 ms                                                 | 65.3 ms: 1.79x faster                                               |
| spectral_norm            | 170 ms                                                 | 97.0 ms: 1.75x faster                                               |
| nbody                    | 154 ms                                                 | 88.9 ms: 1.73x faster                                               |
| scimark_monte_carlo      | 118 ms                                                 | 68.9 ms: 1.71x faster                                               |
| crypto_pyaes             | 128 ms                                                 | 75.5 ms: 1.69x faster                                               |
| tomli_loads              | 3.14 sec                                               | 1.87 sec: 1.68x faster                                              |
| pyflate                  | 716 ms                                                 | 429 ms: 1.67x faster                                                |
| comprehensions           | 28.8 us                                                | 18.7 us: 1.54x faster                                               |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                                |
| deepcopy_reduce          | 4.17 us                                                | 2.74 us: 1.52x faster                                               |
| mako                     | 16.3 ms                                                | 10.9 ms: 1.49x faster                                               |
| pickle_pure_python       | 484 us                                                 | 325 us: 1.49x faster                                                |
| scimark_fft              | 466 ms                                                 | 314 ms: 1.48x faster                                                |
| logging_simple           | 8.30 us                                                | 5.60 us: 1.48x faster                                               |
| logging_format           | 9.09 us                                                | 6.14 us: 1.48x faster                                               |
| genshi_text              | 31.8 ms                                                | 21.5 ms: 1.48x faster                                               |
| scimark_lu               | 176 ms                                                 | 119 ms: 1.48x faster                                                |
| regex_compile            | 188 ms                                                 | 128 ms: 1.47x faster                                                |
| django_template          | 48.2 ms                                                | 32.9 ms: 1.47x faster                                               |
| hexiom                   | 10.4 ms                                                | 7.11 ms: 1.46x faster                                               |
| coroutines               | 35.1 ms                                                | 24.2 ms: 1.45x faster                                               |
| html5lib                 | 88.9 ms                                                | 63.2 ms: 1.41x faster                                               |
| xml_etree_process        | 79.1 ms                                                | 56.6 ms: 1.40x faster                                               |
| dulwich_log              | 84.3 ms                                                | 60.9 ms: 1.38x faster                                               |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.38x faster                                              |
| thrift                   | 1.07 ms                                                | 775 us: 1.38x faster                                                |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.73 ms: 1.37x faster                                               |
| pprint_pformat           | 2.10 sec                                               | 1.55 sec: 1.35x faster                                              |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.4 ms: 1.34x faster                                               |
| genshi_xml               | 66.0 ms                                                | 49.8 ms: 1.33x faster                                               |
| 2to3                     | 348 ms                                                 | 264 ms: 1.32x faster                                                |
| pprint_safe_repr         | 1.02 sec                                               | 777 ms: 1.31x faster                                                |
| fannkuch                 | 532 ms                                                 | 414 ms: 1.28x faster                                                |
| sympy_integrate          | 25.8 ms                                                | 20.3 ms: 1.27x faster                                               |
| sqlalchemy_declarative   | 172 ms                                                 | 136 ms: 1.27x faster                                                |
| sympy_sum                | 196 ms                                                 | 155 ms: 1.27x faster                                                |
| sympy_str                | 346 ms                                                 | 277 ms: 1.25x faster                                                |
| nqueens                  | 106 ms                                                 | 85.5 ms: 1.24x faster                                               |
| xml_etree_generate       | 99.4 ms                                                | 80.5 ms: 1.23x faster                                               |
| pathlib                  | 20.5 ms                                                | 16.6 ms: 1.23x faster                                               |
| docutils                 | 3.30 sec                                               | 2.68 sec: 1.23x faster                                              |
| json_dumps               | 14.2 ms                                                | 11.6 ms: 1.22x faster                                               |
| regex_v8                 | 27.8 ms                                                | 22.9 ms: 1.21x faster                                               |
| xml_etree_parse          | 168 ms                                                 | 140 ms: 1.20x faster                                                |
| sympy_expand             | 566 ms                                                 | 478 ms: 1.18x faster                                                |
| xml_etree_iterparse      | 115 ms                                                 | 98.2 ms: 1.18x faster                                               |
| regex_effbot             | 3.63 ms                                                | 3.10 ms: 1.17x faster                                               |
| mdp                      | 2.85 sec                                               | 2.49 sec: 1.14x faster                                              |
| bench_thread_pool        | 986 us                                                 | 886 us: 1.11x faster                                                |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.11x faster                                               |
| sqlite_synth             | 3.02 us                                                | 2.72 us: 1.11x faster                                               |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                                |
| regex_dna                | 227 ms                                                 | 211 ms: 1.07x faster                                                |
| async_generators         | 444 ms                                                 | 414 ms: 1.07x faster                                                |
| json                     | 5.69 ms                                                | 5.35 ms: 1.06x faster                                               |
| json_loads               | 31.2 us                                                | 30.0 us: 1.04x faster                                               |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                                |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                |
| telco                    | 7.27 ms                                                | 7.78 ms: 1.07x slower                                               |
| coverage                 | 79.4 ms                                                | 86.0 ms: 1.08x slower                                               |
| gc_traversal             | 3.62 ms                                                | 4.85 ms: 1.34x slower                                               |
| python_startup_no_site   | 5.93 ms                                                | 8.21 ms: 1.38x slower                                               |
| create_gc_cycles         | 1.62 ms                                                | 2.48 ms: 1.53x slower                                               |
| bench_mp_pool            | 24.0 ms                                                | 83.3 ms: 3.47x slower                                               |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                        |
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250328-3.14.0a6+-a70757e-JIT/bm-20250328-linux-x86_64-brandtbucher-jit_up_11_7-3.14.0a6+-a70757e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.440x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.30x