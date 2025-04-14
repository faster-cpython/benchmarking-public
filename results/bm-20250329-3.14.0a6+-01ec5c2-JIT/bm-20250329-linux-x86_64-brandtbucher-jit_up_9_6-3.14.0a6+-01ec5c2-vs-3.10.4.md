# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_up_9_6
- machine: linux-x86_64
- commit hash: 01ec5c2
- commit date: 2025-03-29
- overall geometric mean: 1.433x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-linux-x86_64-brandtbucher-jit_up_9_6-3.14.0a6+-01ec5c2 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 270 ms: 1.29x faster                                               |
| docutils       | 3.30 sec                                               | 2.73 sec: 1.21x faster                                             |
| html5lib       | 88.9 ms                                                | 63.0 ms: 1.41x faster                                              |
| Geometric mean | (ref)                                                  | 1.30x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-linux-x86_64-brandtbucher-jit_up_9_6-3.14.0a6+-01ec5c2 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 621 ms: 2.85x faster                                               |
| async_tree_none         | 728 ms                                                 | 263 ms: 2.76x faster                                               |
| async_tree_memoization  | 870 ms                                                 | 319 ms: 2.73x faster                                               |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 504 ms: 2.01x faster                                               |
| Geometric mean          | (ref)                                                  | 2.56x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-linux-x86_64-brandtbucher-jit_up_9_6-3.14.0a6+-01ec5c2 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 117 ms                                                 | 65.8 ms: 1.78x faster                                              |
| nbody          | 154 ms                                                 | 87.6 ms: 1.75x faster                                              |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                  | 1.47x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-linux-x86_64-brandtbucher-jit_up_9_6-3.14.0a6+-01ec5c2 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 130 ms: 1.45x faster                                               |
| regex_v8       | 27.8 ms                                                | 23.2 ms: 1.20x faster                                              |
| regex_effbot   | 3.63 ms                                                | 3.40 ms: 1.07x faster                                              |
| regex_dna      | 227 ms                                                 | 216 ms: 1.05x faster                                               |
| Geometric mean | (ref)                                                  | 1.18x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-linux-x86_64-brandtbucher-jit_up_9_6-3.14.0a6+-01ec5c2 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.89 sec: 1.66x faster                                             |
| unpickle_pure_python | 331 us                                                 | 215 us: 1.54x faster                                               |
| pickle_pure_python   | 484 us                                                 | 326 us: 1.48x faster                                               |
| xml_etree_process    | 79.1 ms                                                | 57.0 ms: 1.39x faster                                              |
| xml_etree_generate   | 99.4 ms                                                | 80.1 ms: 1.24x faster                                              |
| json_dumps           | 14.2 ms                                                | 11.6 ms: 1.23x faster                                              |
| xml_etree_parse      | 168 ms                                                 | 140 ms: 1.20x faster                                               |
| xml_etree_iterparse  | 115 ms                                                 | 98.0 ms: 1.18x faster                                              |
| json_loads           | 31.2 us                                                | 29.9 us: 1.04x faster                                              |
| Geometric mean       | (ref)                                                  | 1.32x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-linux-x86_64-brandtbucher-jit_up_9_6-3.14.0a6+-01ec5c2 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.11x faster                                              |
| python_startup_no_site | 5.93 ms                                                | 8.18 ms: 1.38x slower                                              |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-linux-x86_64-brandtbucher-jit_up_9_6-3.14.0a6+-01ec5c2 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.1 ms: 1.50x faster                                              |
| genshi_text     | 31.8 ms                                                | 21.4 ms: 1.49x faster                                              |
| mako            | 16.3 ms                                                | 11.0 ms: 1.48x faster                                              |
| genshi_xml      | 66.0 ms                                                | 50.1 ms: 1.32x faster                                              |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-linux-x86_64-brandtbucher-jit_up_9_6-3.14.0a6+-01ec5c2 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 169 us: 3.22x faster                                               |
| async_tree_io            | 1.77 sec                                               | 621 ms: 2.85x faster                                               |
| async_tree_none          | 728 ms                                                 | 263 ms: 2.76x faster                                               |
| generators               | 80.1 ms                                                | 29.0 ms: 2.76x faster                                              |
| async_tree_memoization   | 870 ms                                                 | 319 ms: 2.73x faster                                               |
| deltablue                | 7.91 ms                                                | 3.05 ms: 2.59x faster                                              |
| richards_super           | 94.7 ms                                                | 40.8 ms: 2.32x faster                                              |
| richards                 | 79.3 ms                                                | 35.8 ms: 2.21x faster                                              |
| deepcopy_memo            | 58.5 us                                                | 28.2 us: 2.08x faster                                              |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 504 ms: 2.01x faster                                               |
| logging_silent           | 190 ns                                                 | 98.6 ns: 1.92x faster                                              |
| pylint                   | 551 ms                                                 | 287 ms: 1.92x faster                                               |
| chaos                    | 115 ms                                                 | 60.7 ms: 1.90x faster                                              |
| raytrace                 | 507 ms                                                 | 270 ms: 1.87x faster                                               |
| go                       | 240 ms                                                 | 130 ms: 1.85x faster                                               |
| deepcopy                 | 479 us                                                 | 262 us: 1.83x faster                                               |
| scimark_sor              | 220 ms                                                 | 123 ms: 1.78x faster                                               |
| float                    | 117 ms                                                 | 65.8 ms: 1.78x faster                                              |
| nbody                    | 154 ms                                                 | 87.6 ms: 1.75x faster                                              |
| scimark_monte_carlo      | 118 ms                                                 | 68.6 ms: 1.72x faster                                              |
| spectral_norm            | 170 ms                                                 | 98.7 ms: 1.72x faster                                              |
| crypto_pyaes             | 128 ms                                                 | 75.4 ms: 1.70x faster                                              |
| tomli_loads              | 3.14 sec                                               | 1.89 sec: 1.66x faster                                             |
| pyflate                  | 716 ms                                                 | 434 ms: 1.65x faster                                               |
| unpickle_pure_python     | 331 us                                                 | 215 us: 1.54x faster                                               |
| comprehensions           | 28.8 us                                                | 18.7 us: 1.53x faster                                              |
| deepcopy_reduce          | 4.17 us                                                | 2.73 us: 1.53x faster                                              |
| coroutines               | 35.1 ms                                                | 23.3 ms: 1.50x faster                                              |
| django_template          | 48.2 ms                                                | 32.1 ms: 1.50x faster                                              |
| genshi_text              | 31.8 ms                                                | 21.4 ms: 1.49x faster                                              |
| hexiom                   | 10.4 ms                                                | 6.99 ms: 1.49x faster                                              |
| mako                     | 16.3 ms                                                | 11.0 ms: 1.48x faster                                              |
| pickle_pure_python       | 484 us                                                 | 326 us: 1.48x faster                                               |
| scimark_lu               | 176 ms                                                 | 119 ms: 1.48x faster                                               |
| scimark_fft              | 466 ms                                                 | 316 ms: 1.47x faster                                               |
| logging_format           | 9.09 us                                                | 6.18 us: 1.47x faster                                              |
| logging_simple           | 8.30 us                                                | 5.66 us: 1.47x faster                                              |
| regex_compile            | 188 ms                                                 | 130 ms: 1.45x faster                                               |
| html5lib                 | 88.9 ms                                                | 63.0 ms: 1.41x faster                                              |
| dulwich_log              | 84.3 ms                                                | 60.7 ms: 1.39x faster                                              |
| xml_etree_process        | 79.1 ms                                                | 57.0 ms: 1.39x faster                                              |
| thrift                   | 1.07 ms                                                | 787 us: 1.36x faster                                               |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.76 ms: 1.36x faster                                              |
| pprint_safe_repr         | 1.02 sec                                               | 754 ms: 1.35x faster                                               |
| pprint_pformat           | 2.10 sec                                               | 1.58 sec: 1.33x faster                                             |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.6 ms: 1.33x faster                                              |
| genshi_xml               | 66.0 ms                                                | 50.1 ms: 1.32x faster                                              |
| pycparser                | 1.58 sec                                               | 1.20 sec: 1.32x faster                                             |
| 2to3                     | 348 ms                                                 | 270 ms: 1.29x faster                                               |
| sympy_sum                | 196 ms                                                 | 155 ms: 1.27x faster                                               |
| sympy_integrate          | 25.8 ms                                                | 20.5 ms: 1.26x faster                                              |
| fannkuch                 | 532 ms                                                 | 424 ms: 1.25x faster                                               |
| sympy_str                | 346 ms                                                 | 278 ms: 1.25x faster                                               |
| nqueens                  | 106 ms                                                 | 85.0 ms: 1.24x faster                                              |
| xml_etree_generate       | 99.4 ms                                                | 80.1 ms: 1.24x faster                                              |
| json_dumps               | 14.2 ms                                                | 11.6 ms: 1.23x faster                                              |
| pathlib                  | 20.5 ms                                                | 16.7 ms: 1.22x faster                                              |
| sqlalchemy_declarative   | 172 ms                                                 | 141 ms: 1.22x faster                                               |
| docutils                 | 3.30 sec                                               | 2.73 sec: 1.21x faster                                             |
| xml_etree_parse          | 168 ms                                                 | 140 ms: 1.20x faster                                               |
| regex_v8                 | 27.8 ms                                                | 23.2 ms: 1.20x faster                                              |
| sympy_expand             | 566 ms                                                 | 477 ms: 1.19x faster                                               |
| xml_etree_iterparse      | 115 ms                                                 | 98.0 ms: 1.18x faster                                              |
| mdp                      | 2.85 sec                                               | 2.50 sec: 1.14x faster                                             |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.11x faster                                              |
| sqlite_synth             | 3.02 us                                                | 2.72 us: 1.11x faster                                              |
| bench_thread_pool        | 986 us                                                 | 891 us: 1.11x faster                                               |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                               |
| json                     | 5.69 ms                                                | 5.30 ms: 1.07x faster                                              |
| async_generators         | 444 ms                                                 | 415 ms: 1.07x faster                                               |
| regex_effbot             | 3.63 ms                                                | 3.40 ms: 1.07x faster                                              |
| regex_dna                | 227 ms                                                 | 216 ms: 1.05x faster                                               |
| json_loads               | 31.2 us                                                | 29.9 us: 1.04x faster                                              |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                               |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                               |
| coverage                 | 79.4 ms                                                | 85.3 ms: 1.07x slower                                              |
| telco                    | 7.27 ms                                                | 8.25 ms: 1.14x slower                                              |
| gc_traversal             | 3.62 ms                                                | 4.83 ms: 1.33x slower                                              |
| python_startup_no_site   | 5.93 ms                                                | 8.18 ms: 1.38x slower                                              |
| create_gc_cycles         | 1.62 ms                                                | 2.48 ms: 1.53x slower                                              |
| bench_mp_pool            | 24.0 ms                                                | 83.5 ms: 3.48x slower                                              |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                       |
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250329-3.14.0a6+-01ec5c2-JIT/bm-20250329-linux-x86_64-brandtbucher-jit_up_9_6-3.14.0a6+-01ec5c2.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.433x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.30x