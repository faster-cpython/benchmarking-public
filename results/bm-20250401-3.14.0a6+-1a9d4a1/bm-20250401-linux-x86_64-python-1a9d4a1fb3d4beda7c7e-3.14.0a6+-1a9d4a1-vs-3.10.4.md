# Results vs. 3.10.4

- fork: python
- ref: 1a9d4a1fb3d4beda7c7e
- machine: linux-x86_64
- commit hash: 1a9d4a1
- commit date: 2025-04-01
- overall geometric mean: 1.464x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.33x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 252 ms: 1.39x faster                                                   |
| docutils       | 3.30 sec                                               | 2.60 sec: 1.27x faster                                                 |
| html5lib       | 88.9 ms                                                | 60.6 ms: 1.47x faster                                                  |
| Geometric mean | (ref)                                                  | 1.37x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 615 ms: 2.88x faster                                                   |
| async_tree_none         | 728 ms                                                 | 259 ms: 2.81x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 313 ms: 2.78x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 491 ms: 2.07x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.61x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 117 ms                                                 | 68.6 ms: 1.71x faster                                                  |
| nbody          | 154 ms                                                 | 93.8 ms: 1.64x faster                                                  |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                  | 1.42x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 125 ms: 1.51x faster                                                   |
| regex_v8       | 27.8 ms                                                | 23.1 ms: 1.20x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.29 ms: 1.10x faster                                                  |
| regex_dna      | 227 ms                                                 | 220 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                  | 1.20x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.94 sec: 1.62x faster                                                 |
| pickle_pure_python   | 484 us                                                 | 313 us: 1.55x faster                                                   |
| unpickle_pure_python | 331 us                                                 | 218 us: 1.52x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 58.7 ms: 1.35x faster                                                  |
| json_dumps           | 14.2 ms                                                | 11.4 ms: 1.25x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 84.1 ms: 1.18x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 98.8 ms: 1.17x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 144 ms: 1.17x faster                                                   |
| json_loads           | 31.2 us                                                | 29.8 us: 1.05x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 8.18 ms: 1.38x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.3 ms: 1.54x faster                                                  |
| genshi_text     | 31.8 ms                                                | 21.5 ms: 1.48x faster                                                  |
| mako            | 16.3 ms                                                | 11.3 ms: 1.44x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 49.2 ms: 1.34x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.33x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 615 ms: 2.88x faster                                                   |
| async_tree_none          | 728 ms                                                 | 259 ms: 2.81x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 313 ms: 2.78x faster                                                   |
| generators               | 80.1 ms                                                | 30.9 ms: 2.59x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.37 ms: 2.35x faster                                                  |
| mdp                      | 2.85 sec                                               | 1.22 sec: 2.34x faster                                                 |
| go                       | 240 ms                                                 | 111 ms: 2.16x faster                                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 491 ms: 2.07x faster                                                   |
| chaos                    | 115 ms                                                 | 56.3 ms: 2.05x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 28.9 us: 2.02x faster                                                  |
| pylint                   | 551 ms                                                 | 277 ms: 1.99x faster                                                   |
| raytrace                 | 507 ms                                                 | 256 ms: 1.98x faster                                                   |
| logging_silent           | 190 ns                                                 | 96.5 ns: 1.97x faster                                                  |
| richards_super           | 94.7 ms                                                | 49.4 ms: 1.92x faster                                                  |
| deepcopy                 | 479 us                                                 | 251 us: 1.91x faster                                                   |
| scimark_sor              | 220 ms                                                 | 116 ms: 1.90x faster                                                   |
| scimark_monte_carlo      | 118 ms                                                 | 64.3 ms: 1.84x faster                                                  |
| richards                 | 79.3 ms                                                | 43.3 ms: 1.83x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 72.6 ms: 1.76x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                                  |
| spectral_norm            | 170 ms                                                 | 98.9 ms: 1.72x faster                                                  |
| float                    | 117 ms                                                 | 68.6 ms: 1.71x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.18 ms: 1.68x faster                                                  |
| nbody                    | 154 ms                                                 | 93.8 ms: 1.64x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 1.94 sec: 1.62x faster                                                 |
| pyflate                  | 716 ms                                                 | 444 ms: 1.61x faster                                                   |
| scimark_lu               | 176 ms                                                 | 113 ms: 1.56x faster                                                   |
| pickle_pure_python       | 484 us                                                 | 313 us: 1.55x faster                                                   |
| django_template          | 48.2 ms                                                | 31.3 ms: 1.54x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.72 us: 1.53x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 218 us: 1.52x faster                                                   |
| regex_compile            | 188 ms                                                 | 125 ms: 1.51x faster                                                   |
| coroutines               | 35.1 ms                                                | 23.3 ms: 1.50x faster                                                  |
| logging_format           | 9.09 us                                                | 6.13 us: 1.48x faster                                                  |
| genshi_text              | 31.8 ms                                                | 21.5 ms: 1.48x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.61 us: 1.48x faster                                                  |
| html5lib                 | 88.9 ms                                                | 60.6 ms: 1.47x faster                                                  |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.44x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 58.9 ms: 1.43x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.41x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 725 ms: 1.40x faster                                                   |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.66 ms: 1.39x faster                                                  |
| 2to3                     | 348 ms                                                 | 252 ms: 1.39x faster                                                   |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.0 ms: 1.37x faster                                                  |
| scimark_fft              | 466 ms                                                 | 340 ms: 1.37x faster                                                   |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 58.7 ms: 1.35x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 49.2 ms: 1.34x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 19.2 ms: 1.34x faster                                                  |
| sympy_sum                | 196 ms                                                 | 149 ms: 1.32x faster                                                   |
| sqlalchemy_declarative   | 172 ms                                                 | 131 ms: 1.31x faster                                                   |
| sympy_str                | 346 ms                                                 | 268 ms: 1.29x faster                                                   |
| fannkuch                 | 532 ms                                                 | 413 ms: 1.29x faster                                                   |
| nqueens                  | 106 ms                                                 | 82.3 ms: 1.29x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.60 sec: 1.27x faster                                                 |
| json_dumps               | 14.2 ms                                                | 11.4 ms: 1.25x faster                                                  |
| pathlib                  | 20.5 ms                                                | 16.4 ms: 1.25x faster                                                  |
| sympy_expand             | 566 ms                                                 | 459 ms: 1.23x faster                                                   |
| regex_v8                 | 27.8 ms                                                | 23.1 ms: 1.20x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 84.1 ms: 1.18x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 98.8 ms: 1.17x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 144 ms: 1.17x faster                                                   |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                   |
| async_generators         | 444 ms                                                 | 394 ms: 1.13x faster                                                   |
| bench_thread_pool        | 986 us                                                 | 878 us: 1.12x faster                                                   |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                  |
| regex_effbot             | 3.63 ms                                                | 3.29 ms: 1.10x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 2.80 us: 1.08x faster                                                  |
| json                     | 5.69 ms                                                | 5.33 ms: 1.07x faster                                                  |
| json_loads               | 31.2 us                                                | 29.8 us: 1.05x faster                                                  |
| regex_dna                | 227 ms                                                 | 220 ms: 1.03x faster                                                   |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                   |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                   |
| coverage                 | 79.4 ms                                                | 84.6 ms: 1.06x slower                                                  |
| telco                    | 7.27 ms                                                | 7.80 ms: 1.07x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 4.98 ms: 1.37x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 8.18 ms: 1.38x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.48 ms: 1.53x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 83.3 ms: 3.47x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.44x faster                                                           |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250401-3.14.0a6+-1a9d4a1/bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.464x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.37x
- 95% likely to have a speedup of 1.36x
- 99% likely to have a speedup of 1.33x

# Memory
- memory change: 1.28x