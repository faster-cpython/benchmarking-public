# Results vs. 3.10.4

- fork: fluhus
- ref: amit
- machine: linux-x86_64
- commit hash: 138f037
- commit date: 2025-03-29
- overall geometric mean: 1.465x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-linux-x86_64-fluhus-amit-3.14.0a6+-138f037 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 262 ms: 1.33x faster                                   |
| docutils       | 3.30 sec                                               | 2.69 sec: 1.22x faster                                 |
| html5lib       | 88.9 ms                                                | 61.5 ms: 1.45x faster                                  |
| Geometric mean | (ref)                                                  | 1.33x faster                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-linux-x86_64-fluhus-amit-3.14.0a6+-138f037 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 613 ms: 2.89x faster                                   |
| async_tree_none         | 728 ms                                                 | 261 ms: 2.79x faster                                   |
| async_tree_memoization  | 870 ms                                                 | 313 ms: 2.78x faster                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 490 ms: 2.08x faster                                   |
| Geometric mean          | (ref)                                                  | 2.61x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-linux-x86_64-fluhus-amit-3.14.0a6+-138f037 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 117 ms                                                 | 63.0 ms: 1.86x faster                                  |
| nbody          | 154 ms                                                 | 84.9 ms: 1.81x faster                                  |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                   |
| Geometric mean | (ref)                                                  | 1.51x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-linux-x86_64-fluhus-amit-3.14.0a6+-138f037 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.48x faster                                   |
| regex_v8       | 27.8 ms                                                | 23.1 ms: 1.20x faster                                  |
| regex_effbot   | 3.63 ms                                                | 3.47 ms: 1.05x faster                                  |
| regex_dna      | 227 ms                                                 | 223 ms: 1.02x faster                                   |
| Geometric mean | (ref)                                                  | 1.17x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-linux-x86_64-fluhus-amit-3.14.0a6+-138f037 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.85 sec: 1.69x faster                                 |
| unpickle_pure_python | 331 us                                                 | 211 us: 1.57x faster                                   |
| pickle_pure_python   | 484 us                                                 | 321 us: 1.51x faster                                   |
| xml_etree_process    | 79.1 ms                                                | 55.7 ms: 1.42x faster                                  |
| xml_etree_generate   | 99.4 ms                                                | 80.2 ms: 1.24x faster                                  |
| json_dumps           | 14.2 ms                                                | 11.6 ms: 1.22x faster                                  |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                   |
| xml_etree_iterparse  | 115 ms                                                 | 97.7 ms: 1.18x faster                                  |
| json_loads           | 31.2 us                                                | 30.0 us: 1.04x faster                                  |
| Geometric mean       | (ref)                                                  | 1.33x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-linux-x86_64-fluhus-amit-3.14.0a6+-138f037 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.11x faster                                  |
| python_startup_no_site | 5.93 ms                                                | 8.20 ms: 1.38x slower                                  |
| Geometric mean         | (ref)                                                  | 1.11x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-linux-x86_64-fluhus-amit-3.14.0a6+-138f037 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 21.1 ms: 1.51x faster                                  |
| django_template | 48.2 ms                                                | 32.3 ms: 1.49x faster                                  |
| mako            | 16.3 ms                                                | 11.1 ms: 1.48x faster                                  |
| genshi_xml      | 66.0 ms                                                | 49.9 ms: 1.32x faster                                  |
| Geometric mean  | (ref)                                                  | 1.45x faster                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-linux-x86_64-fluhus-amit-3.14.0a6+-138f037 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 166 us: 3.27x faster                                   |
| async_tree_io            | 1.77 sec                                               | 613 ms: 2.89x faster                                   |
| generators               | 80.1 ms                                                | 28.4 ms: 2.82x faster                                  |
| async_tree_none          | 728 ms                                                 | 261 ms: 2.79x faster                                   |
| async_tree_memoization   | 870 ms                                                 | 313 ms: 2.78x faster                                   |
| deltablue                | 7.91 ms                                                | 3.01 ms: 2.63x faster                                  |
| richards_super           | 94.7 ms                                                | 40.7 ms: 2.32x faster                                  |
| mdp                      | 2.85 sec                                               | 1.24 sec: 2.29x faster                                 |
| richards                 | 79.3 ms                                                | 35.2 ms: 2.25x faster                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 490 ms: 2.08x faster                                   |
| deepcopy_memo            | 58.5 us                                                | 29.0 us: 2.02x faster                                  |
| pylint                   | 551 ms                                                 | 281 ms: 1.96x faster                                   |
| chaos                    | 115 ms                                                 | 58.8 ms: 1.96x faster                                  |
| logging_silent           | 190 ns                                                 | 97.6 ns: 1.94x faster                                  |
| raytrace                 | 507 ms                                                 | 266 ms: 1.91x faster                                   |
| go                       | 240 ms                                                 | 127 ms: 1.89x faster                                   |
| deepcopy                 | 479 us                                                 | 257 us: 1.86x faster                                   |
| float                    | 117 ms                                                 | 63.0 ms: 1.86x faster                                  |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.85x faster                                   |
| spectral_norm            | 170 ms                                                 | 92.9 ms: 1.83x faster                                  |
| nbody                    | 154 ms                                                 | 84.9 ms: 1.81x faster                                  |
| scimark_monte_carlo      | 118 ms                                                 | 68.0 ms: 1.74x faster                                  |
| tomli_loads              | 3.14 sec                                               | 1.85 sec: 1.69x faster                                 |
| crypto_pyaes             | 128 ms                                                 | 75.7 ms: 1.69x faster                                  |
| pyflate                  | 716 ms                                                 | 443 ms: 1.62x faster                                   |
| unpickle_pure_python     | 331 us                                                 | 211 us: 1.57x faster                                   |
| deepcopy_reduce          | 4.17 us                                                | 2.71 us: 1.54x faster                                  |
| hexiom                   | 10.4 ms                                                | 6.78 ms: 1.53x faster                                  |
| comprehensions           | 28.8 us                                                | 18.8 us: 1.53x faster                                  |
| coroutines               | 35.1 ms                                                | 23.0 ms: 1.52x faster                                  |
| genshi_text              | 31.8 ms                                                | 21.1 ms: 1.51x faster                                  |
| logging_simple           | 8.30 us                                                | 5.50 us: 1.51x faster                                  |
| pickle_pure_python       | 484 us                                                 | 321 us: 1.51x faster                                   |
| scimark_fft              | 466 ms                                                 | 309 ms: 1.51x faster                                   |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.50x faster                                   |
| django_template          | 48.2 ms                                                | 32.3 ms: 1.49x faster                                  |
| regex_compile            | 188 ms                                                 | 128 ms: 1.48x faster                                   |
| mako                     | 16.3 ms                                                | 11.1 ms: 1.48x faster                                  |
| logging_format           | 9.09 us                                                | 6.18 us: 1.47x faster                                  |
| html5lib                 | 88.9 ms                                                | 61.5 ms: 1.45x faster                                  |
| xml_etree_process        | 79.1 ms                                                | 55.7 ms: 1.42x faster                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.63 ms: 1.40x faster                                  |
| dulwich_log              | 84.3 ms                                                | 60.4 ms: 1.40x faster                                  |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.0 ms: 1.37x faster                                  |
| pprint_pformat           | 2.10 sec                                               | 1.57 sec: 1.34x faster                                 |
| pprint_safe_repr         | 1.02 sec                                               | 764 ms: 1.33x faster                                   |
| 2to3                     | 348 ms                                                 | 262 ms: 1.33x faster                                   |
| pycparser                | 1.58 sec                                               | 1.19 sec: 1.33x faster                                 |
| genshi_xml               | 66.0 ms                                                | 49.9 ms: 1.32x faster                                  |
| sqlalchemy_declarative   | 172 ms                                                 | 131 ms: 1.31x faster                                   |
| sympy_integrate          | 25.8 ms                                                | 20.0 ms: 1.29x faster                                  |
| sympy_sum                | 196 ms                                                 | 153 ms: 1.29x faster                                   |
| nqueens                  | 106 ms                                                 | 83.2 ms: 1.27x faster                                  |
| fannkuch                 | 532 ms                                                 | 419 ms: 1.27x faster                                   |
| sympy_str                | 346 ms                                                 | 275 ms: 1.26x faster                                   |
| pathlib                  | 20.5 ms                                                | 16.5 ms: 1.24x faster                                  |
| xml_etree_generate       | 99.4 ms                                                | 80.2 ms: 1.24x faster                                  |
| json_dumps               | 14.2 ms                                                | 11.6 ms: 1.22x faster                                  |
| docutils                 | 3.30 sec                                               | 2.69 sec: 1.22x faster                                 |
| regex_v8                 | 27.8 ms                                                | 23.1 ms: 1.20x faster                                  |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                   |
| sympy_expand             | 566 ms                                                 | 476 ms: 1.19x faster                                   |
| xml_etree_iterparse      | 115 ms                                                 | 97.7 ms: 1.18x faster                                  |
| bench_thread_pool        | 986 us                                                 | 882 us: 1.12x faster                                   |
| sqlite_synth             | 3.02 us                                                | 2.71 us: 1.12x faster                                  |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.11x faster                                  |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                   |
| async_generators         | 444 ms                                                 | 412 ms: 1.08x faster                                   |
| json                     | 5.69 ms                                                | 5.33 ms: 1.07x faster                                  |
| regex_effbot             | 3.63 ms                                                | 3.47 ms: 1.05x faster                                  |
| json_loads               | 31.2 us                                                | 30.0 us: 1.04x faster                                  |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                   |
| regex_dna                | 227 ms                                                 | 223 ms: 1.02x faster                                   |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                   |
| coverage                 | 79.4 ms                                                | 84.6 ms: 1.06x slower                                  |
| telco                    | 7.27 ms                                                | 7.76 ms: 1.07x slower                                  |
| gc_traversal             | 3.62 ms                                                | 4.76 ms: 1.31x slower                                  |
| python_startup_no_site   | 5.93 ms                                                | 8.20 ms: 1.38x slower                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.48 ms: 1.53x slower                                  |
| bench_mp_pool            | 24.0 ms                                                | 83.0 ms: 3.46x slower                                  |
| Geometric mean           | (ref)                                                  | 1.43x faster                                           |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250329-3.14.0a6+-138f037-JIT/bm-20250329-linux-x86_64-fluhus-amit-3.14.0a6+-138f037.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.465x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.30x