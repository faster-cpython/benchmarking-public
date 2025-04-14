# Results vs. 3.10.4

- fork: iritkatriel
- ref: subscr_stats
- machine: linux-x86_64
- commit hash: 325408b
- commit date: 2025-04-03
- overall geometric mean: 1.455x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.33x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-325408b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 255 ms: 1.37x faster                                                |
| docutils       | 3.30 sec                                               | 2.59 sec: 1.27x faster                                              |
| html5lib       | 88.9 ms                                                | 62.8 ms: 1.41x faster                                               |
| Geometric mean | (ref)                                                  | 1.35x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-325408b |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 619 ms: 2.86x faster                                                |
| async_tree_none         | 728 ms                                                 | 262 ms: 2.78x faster                                                |
| async_tree_memoization  | 870 ms                                                 | 314 ms: 2.77x faster                                                |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 487 ms: 2.09x faster                                                |
| Geometric mean          | (ref)                                                  | 2.60x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-325408b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 117 ms                                                 | 71.4 ms: 1.64x faster                                               |
| nbody          | 154 ms                                                 | 97.0 ms: 1.58x faster                                               |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                  | 1.38x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-325408b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 126 ms: 1.50x faster                                                |
| regex_v8       | 27.8 ms                                                | 22.8 ms: 1.22x faster                                               |
| regex_dna      | 227 ms                                                 | 203 ms: 1.12x faster                                                |
| regex_effbot   | 3.63 ms                                                | 3.74 ms: 1.03x slower                                               |
| Geometric mean | (ref)                                                  | 1.19x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-325408b |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.96 sec: 1.60x faster                                              |
| pickle_pure_python   | 484 us                                                 | 320 us: 1.52x faster                                                |
| unpickle_pure_python | 331 us                                                 | 219 us: 1.51x faster                                                |
| xml_etree_process    | 79.1 ms                                                | 59.5 ms: 1.33x faster                                               |
| json_dumps           | 14.2 ms                                                | 11.4 ms: 1.25x faster                                               |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                                |
| xml_etree_generate   | 99.4 ms                                                | 84.8 ms: 1.17x faster                                               |
| xml_etree_iterparse  | 115 ms                                                 | 98.8 ms: 1.17x faster                                               |
| json_loads           | 31.2 us                                                | 29.5 us: 1.06x faster                                               |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-325408b |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.12x faster                                               |
| python_startup_no_site | 5.93 ms                                                | 8.16 ms: 1.38x slower                                               |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-325408b |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 21.0 ms: 1.51x faster                                               |
| django_template | 48.2 ms                                                | 32.3 ms: 1.49x faster                                               |
| mako            | 16.3 ms                                                | 11.2 ms: 1.46x faster                                               |
| genshi_xml      | 66.0 ms                                                | 49.5 ms: 1.33x faster                                               |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-325408b |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 166 us: 3.29x faster                                                |
| async_tree_io            | 1.77 sec                                               | 619 ms: 2.86x faster                                                |
| generators               | 80.1 ms                                                | 28.6 ms: 2.80x faster                                               |
| async_tree_none          | 728 ms                                                 | 262 ms: 2.78x faster                                                |
| async_tree_memoization   | 870 ms                                                 | 314 ms: 2.77x faster                                                |
| deltablue                | 7.91 ms                                                | 3.19 ms: 2.48x faster                                               |
| mdp                      | 2.85 sec                                               | 1.23 sec: 2.32x faster                                              |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 487 ms: 2.09x faster                                                |
| go                       | 240 ms                                                 | 115 ms: 2.08x faster                                                |
| pylint                   | 551 ms                                                 | 276 ms: 1.99x faster                                                |
| deepcopy_memo            | 58.5 us                                                | 29.4 us: 1.99x faster                                               |
| chaos                    | 115 ms                                                 | 58.5 ms: 1.97x faster                                               |
| logging_silent           | 190 ns                                                 | 98.9 ns: 1.92x faster                                               |
| raytrace                 | 507 ms                                                 | 265 ms: 1.91x faster                                                |
| richards_super           | 94.7 ms                                                | 50.3 ms: 1.88x faster                                               |
| deepcopy                 | 479 us                                                 | 257 us: 1.86x faster                                                |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.83x faster                                                |
| richards                 | 79.3 ms                                                | 44.6 ms: 1.78x faster                                               |
| spectral_norm            | 170 ms                                                 | 96.3 ms: 1.76x faster                                               |
| crypto_pyaes             | 128 ms                                                 | 73.0 ms: 1.75x faster                                               |
| scimark_monte_carlo      | 118 ms                                                 | 68.0 ms: 1.74x faster                                               |
| comprehensions           | 28.8 us                                                | 17.0 us: 1.69x faster                                               |
| hexiom                   | 10.4 ms                                                | 6.23 ms: 1.67x faster                                               |
| float                    | 117 ms                                                 | 71.4 ms: 1.64x faster                                               |
| tomli_loads              | 3.14 sec                                               | 1.96 sec: 1.60x faster                                              |
| nbody                    | 154 ms                                                 | 97.0 ms: 1.58x faster                                               |
| scimark_lu               | 176 ms                                                 | 114 ms: 1.54x faster                                                |
| deepcopy_reduce          | 4.17 us                                                | 2.72 us: 1.53x faster                                               |
| pickle_pure_python       | 484 us                                                 | 320 us: 1.52x faster                                                |
| pyflate                  | 716 ms                                                 | 473 ms: 1.51x faster                                                |
| genshi_text              | 31.8 ms                                                | 21.0 ms: 1.51x faster                                               |
| logging_simple           | 8.30 us                                                | 5.49 us: 1.51x faster                                               |
| unpickle_pure_python     | 331 us                                                 | 219 us: 1.51x faster                                                |
| regex_compile            | 188 ms                                                 | 126 ms: 1.50x faster                                                |
| logging_format           | 9.09 us                                                | 6.07 us: 1.50x faster                                               |
| django_template          | 48.2 ms                                                | 32.3 ms: 1.49x faster                                               |
| coroutines               | 35.1 ms                                                | 23.8 ms: 1.47x faster                                               |
| mako                     | 16.3 ms                                                | 11.2 ms: 1.46x faster                                               |
| dulwich_log              | 84.3 ms                                                | 58.3 ms: 1.45x faster                                               |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                              |
| html5lib                 | 88.9 ms                                                | 62.8 ms: 1.41x faster                                               |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.6 ms: 1.41x faster                                               |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.40x faster                                              |
| pprint_safe_repr         | 1.02 sec                                               | 730 ms: 1.40x faster                                                |
| 2to3                     | 348 ms                                                 | 255 ms: 1.37x faster                                                |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.75 ms: 1.36x faster                                               |
| sympy_integrate          | 25.8 ms                                                | 19.1 ms: 1.35x faster                                               |
| genshi_xml               | 66.0 ms                                                | 49.5 ms: 1.33x faster                                               |
| scimark_fft              | 466 ms                                                 | 350 ms: 1.33x faster                                                |
| xml_etree_process        | 79.1 ms                                                | 59.5 ms: 1.33x faster                                               |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.33x faster                                                |
| sqlalchemy_declarative   | 172 ms                                                 | 130 ms: 1.32x faster                                                |
| nqueens                  | 106 ms                                                 | 81.7 ms: 1.30x faster                                               |
| sympy_str                | 346 ms                                                 | 267 ms: 1.29x faster                                                |
| docutils                 | 3.30 sec                                               | 2.59 sec: 1.27x faster                                              |
| json_dumps               | 14.2 ms                                                | 11.4 ms: 1.25x faster                                               |
| sympy_expand             | 566 ms                                                 | 455 ms: 1.24x faster                                                |
| fannkuch                 | 532 ms                                                 | 429 ms: 1.24x faster                                                |
| pathlib                  | 20.5 ms                                                | 16.6 ms: 1.23x faster                                               |
| regex_v8                 | 27.8 ms                                                | 22.8 ms: 1.22x faster                                               |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 84.8 ms: 1.17x faster                                               |
| xml_etree_iterparse      | 115 ms                                                 | 98.8 ms: 1.17x faster                                               |
| bench_thread_pool        | 986 us                                                 | 871 us: 1.13x faster                                                |
| async_generators         | 444 ms                                                 | 394 ms: 1.13x faster                                                |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                |
| regex_dna                | 227 ms                                                 | 203 ms: 1.12x faster                                                |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.12x faster                                               |
| sqlite_synth             | 3.02 us                                                | 2.79 us: 1.08x faster                                               |
| json                     | 5.69 ms                                                | 5.28 ms: 1.08x faster                                               |
| json_loads               | 31.2 us                                                | 29.5 us: 1.06x faster                                               |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                |
| regex_effbot             | 3.63 ms                                                | 3.74 ms: 1.03x slower                                               |
| coverage                 | 79.4 ms                                                | 83.2 ms: 1.05x slower                                               |
| telco                    | 7.27 ms                                                | 7.84 ms: 1.08x slower                                               |
| python_startup_no_site   | 5.93 ms                                                | 8.16 ms: 1.38x slower                                               |
| gc_traversal             | 3.62 ms                                                | 4.99 ms: 1.38x slower                                               |
| create_gc_cycles         | 1.62 ms                                                | 2.48 ms: 1.53x slower                                               |
| bench_mp_pool            | 24.0 ms                                                | 83.1 ms: 3.46x slower                                               |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                        |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250403-3.14.0a6+-325408b/bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-325408b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.455x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.36x
- 95% likely to have a speedup of 1.35x
- 99% likely to have a speedup of 1.33x

# Memory
- memory change: 1.29x