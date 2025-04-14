# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: lto_fix
- machine: linux-x86_64
- commit hash: 8891cd2
- commit date: 2025-04-07
- overall geometric mean: 1.474x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.34x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250407-linux-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 250 ms: 1.39x faster                                                |
| docutils       | 3.30 sec                                               | 2.58 sec: 1.28x faster                                              |
| html5lib       | 88.9 ms                                                | 61.5 ms: 1.44x faster                                               |
| Geometric mean | (ref)                                                  | 1.37x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250407-linux-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 606 ms: 2.92x faster                                                |
| async_tree_none         | 728 ms                                                 | 255 ms: 2.85x faster                                                |
| async_tree_memoization  | 870 ms                                                 | 311 ms: 2.80x faster                                                |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 484 ms: 2.10x faster                                                |
| Geometric mean          | (ref)                                                  | 2.65x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250407-linux-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 117 ms                                                 | 67.3 ms: 1.74x faster                                               |
| nbody          | 154 ms                                                 | 91.0 ms: 1.69x faster                                               |
| pidigits       | 191 ms                                                 | 194 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                  | 1.42x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250407-linux-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 124 ms: 1.52x faster                                                |
| regex_v8       | 27.8 ms                                                | 22.7 ms: 1.23x faster                                               |
| regex_effbot   | 3.63 ms                                                | 3.04 ms: 1.19x faster                                               |
| regex_dna      | 227 ms                                                 | 205 ms: 1.11x faster                                                |
| Geometric mean | (ref)                                                  | 1.25x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250407-linux-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.97 sec: 1.59x faster                                              |
| unpickle_pure_python | 331 us                                                 | 211 us: 1.56x faster                                                |
| pickle_pure_python   | 484 us                                                 | 314 us: 1.54x faster                                                |
| xml_etree_process    | 79.1 ms                                                | 58.5 ms: 1.35x faster                                               |
| json_dumps           | 14.2 ms                                                | 11.3 ms: 1.25x faster                                               |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                                |
| xml_etree_generate   | 99.4 ms                                                | 84.2 ms: 1.18x faster                                               |
| xml_etree_iterparse  | 115 ms                                                 | 97.8 ms: 1.18x faster                                               |
| json_loads           | 31.2 us                                                | 29.0 us: 1.08x faster                                               |
| Geometric mean       | (ref)                                                  | 1.31x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250407-linux-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.2 ms: 1.11x faster                                               |
| python_startup_no_site | 5.93 ms                                                | 8.20 ms: 1.38x slower                                               |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250407-linux-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.5 ms: 1.53x faster                                               |
| genshi_text     | 31.8 ms                                                | 21.1 ms: 1.51x faster                                               |
| mako            | 16.3 ms                                                | 11.3 ms: 1.44x faster                                               |
| genshi_xml      | 66.0 ms                                                | 48.7 ms: 1.36x faster                                               |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250407-linux-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.31x faster                                                |
| async_tree_io            | 1.77 sec                                               | 606 ms: 2.92x faster                                                |
| async_tree_none          | 728 ms                                                 | 255 ms: 2.85x faster                                                |
| async_tree_memoization   | 870 ms                                                 | 311 ms: 2.80x faster                                                |
| generators               | 80.1 ms                                                | 29.2 ms: 2.75x faster                                               |
| deltablue                | 7.91 ms                                                | 3.33 ms: 2.37x faster                                               |
| mdp                      | 2.85 sec                                               | 1.22 sec: 2.33x faster                                              |
| go                       | 240 ms                                                 | 109 ms: 2.20x faster                                                |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 484 ms: 2.10x faster                                                |
| deepcopy_memo            | 58.5 us                                                | 28.2 us: 2.07x faster                                               |
| chaos                    | 115 ms                                                 | 56.2 ms: 2.05x faster                                               |
| pylint                   | 551 ms                                                 | 276 ms: 2.00x faster                                                |
| logging_silent           | 190 ns                                                 | 95.5 ns: 1.99x faster                                               |
| raytrace                 | 507 ms                                                 | 259 ms: 1.95x faster                                                |
| richards_super           | 94.7 ms                                                | 49.5 ms: 1.91x faster                                               |
| deepcopy                 | 479 us                                                 | 251 us: 1.91x faster                                                |
| scimark_sor              | 220 ms                                                 | 115 ms: 1.90x faster                                                |
| richards                 | 79.3 ms                                                | 43.1 ms: 1.84x faster                                               |
| scimark_monte_carlo      | 118 ms                                                 | 65.1 ms: 1.82x faster                                               |
| crypto_pyaes             | 128 ms                                                 | 72.7 ms: 1.76x faster                                               |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                               |
| float                    | 117 ms                                                 | 67.3 ms: 1.74x faster                                               |
| nbody                    | 154 ms                                                 | 91.0 ms: 1.69x faster                                               |
| hexiom                   | 10.4 ms                                                | 6.24 ms: 1.67x faster                                               |
| spectral_norm            | 170 ms                                                 | 102 ms: 1.66x faster                                                |
| pyflate                  | 716 ms                                                 | 439 ms: 1.63x faster                                                |
| tomli_loads              | 3.14 sec                                               | 1.97 sec: 1.59x faster                                              |
| deepcopy_reduce          | 4.17 us                                                | 2.64 us: 1.58x faster                                               |
| unpickle_pure_python     | 331 us                                                 | 211 us: 1.56x faster                                                |
| pickle_pure_python       | 484 us                                                 | 314 us: 1.54x faster                                                |
| django_template          | 48.2 ms                                                | 31.5 ms: 1.53x faster                                               |
| logging_simple           | 8.30 us                                                | 5.46 us: 1.52x faster                                               |
| regex_compile            | 188 ms                                                 | 124 ms: 1.52x faster                                                |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.52x faster                                                |
| genshi_text              | 31.8 ms                                                | 21.1 ms: 1.51x faster                                               |
| logging_format           | 9.09 us                                                | 6.03 us: 1.51x faster                                               |
| coroutines               | 35.1 ms                                                | 23.6 ms: 1.49x faster                                               |
| pprint_pformat           | 2.10 sec                                               | 1.45 sec: 1.45x faster                                              |
| pprint_safe_repr         | 1.02 sec                                               | 704 ms: 1.45x faster                                                |
| html5lib                 | 88.9 ms                                                | 61.5 ms: 1.44x faster                                               |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.44x faster                                               |
| dulwich_log              | 84.3 ms                                                | 59.3 ms: 1.42x faster                                               |
| pycparser                | 1.58 sec                                               | 1.11 sec: 1.41x faster                                              |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.7 ms: 1.40x faster                                               |
| 2to3                     | 348 ms                                                 | 250 ms: 1.39x faster                                                |
| genshi_xml               | 66.0 ms                                                | 48.7 ms: 1.36x faster                                               |
| xml_etree_process        | 79.1 ms                                                | 58.5 ms: 1.35x faster                                               |
| sympy_integrate          | 25.8 ms                                                | 19.2 ms: 1.35x faster                                               |
| scimark_fft              | 466 ms                                                 | 346 ms: 1.34x faster                                                |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.86 ms: 1.33x faster                                               |
| sympy_sum                | 196 ms                                                 | 149 ms: 1.32x faster                                                |
| fannkuch                 | 532 ms                                                 | 406 ms: 1.31x faster                                                |
| sqlalchemy_declarative   | 172 ms                                                 | 132 ms: 1.31x faster                                                |
| nqueens                  | 106 ms                                                 | 81.3 ms: 1.30x faster                                               |
| sympy_str                | 346 ms                                                 | 267 ms: 1.30x faster                                                |
| docutils                 | 3.30 sec                                               | 2.58 sec: 1.28x faster                                              |
| json_dumps               | 14.2 ms                                                | 11.3 ms: 1.25x faster                                               |
| sympy_expand             | 566 ms                                                 | 454 ms: 1.25x faster                                                |
| pathlib                  | 20.5 ms                                                | 16.5 ms: 1.24x faster                                               |
| regex_v8                 | 27.8 ms                                                | 22.7 ms: 1.23x faster                                               |
| regex_effbot             | 3.63 ms                                                | 3.04 ms: 1.19x faster                                               |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 84.2 ms: 1.18x faster                                               |
| xml_etree_iterparse      | 115 ms                                                 | 97.8 ms: 1.18x faster                                               |
| async_generators         | 444 ms                                                 | 392 ms: 1.13x faster                                                |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                |
| bench_thread_pool        | 986 us                                                 | 877 us: 1.13x faster                                                |
| regex_dna                | 227 ms                                                 | 205 ms: 1.11x faster                                                |
| python_startup           | 14.6 ms                                                | 13.2 ms: 1.11x faster                                               |
| json                     | 5.69 ms                                                | 5.21 ms: 1.09x faster                                               |
| sqlite_synth             | 3.02 us                                                | 2.79 us: 1.08x faster                                               |
| json_loads               | 31.2 us                                                | 29.0 us: 1.08x faster                                               |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                |
| pidigits                 | 191 ms                                                 | 194 ms: 1.02x slower                                                |
| telco                    | 7.27 ms                                                | 7.68 ms: 1.06x slower                                               |
| coverage                 | 79.4 ms                                                | 85.8 ms: 1.08x slower                                               |
| gc_traversal             | 3.62 ms                                                | 4.79 ms: 1.32x slower                                               |
| python_startup_no_site   | 5.93 ms                                                | 8.20 ms: 1.38x slower                                               |
| create_gc_cycles         | 1.62 ms                                                | 2.47 ms: 1.52x slower                                               |
| bench_mp_pool            | 24.0 ms                                                | 82.1 ms: 3.42x slower                                               |
| Geometric mean           | (ref)                                                  | 1.45x faster                                                        |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250407-3.14.0a6+-8891cd2/bm-20250407-linux-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.474x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.38x
- 95% likely to have a speedup of 1.37x
- 99% likely to have a speedup of 1.34x

# Memory
- memory change: 1.27x