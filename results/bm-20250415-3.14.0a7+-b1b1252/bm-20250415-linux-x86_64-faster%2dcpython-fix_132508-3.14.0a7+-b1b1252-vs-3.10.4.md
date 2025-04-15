# Results vs. 3.10.4

- fork: faster-cpython
- ref: fix_132508
- machine: linux-x86_64
- commit hash: b1b1252
- commit date: 2025-04-15
- overall geometric mean: 1.465x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250415-linux-x86_64-faster%2dcpython-fix_132508-3.14.0a7+-b1b1252 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 250 ms: 1.39x faster                                                   |
| docutils       | 3.30 sec                                               | 2.60 sec: 1.27x faster                                                 |
| html5lib       | 88.9 ms                                                | 59.6 ms: 1.49x faster                                                  |
| Geometric mean | (ref)                                                  | 1.38x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250415-linux-x86_64-faster%2dcpython-fix_132508-3.14.0a7+-b1b1252 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 609 ms: 2.91x faster                                                   |
| async_tree_none         | 728 ms                                                 | 256 ms: 2.85x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 307 ms: 2.84x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 479 ms: 2.12x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.66x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250415-linux-x86_64-faster%2dcpython-fix_132508-3.14.0a7+-b1b1252 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 117 ms                                                 | 68.8 ms: 1.70x faster                                                  |
| nbody          | 154 ms                                                 | 96.6 ms: 1.59x faster                                                  |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.40x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250415-linux-x86_64-faster%2dcpython-fix_132508-3.14.0a7+-b1b1252 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 125 ms: 1.51x faster                                                   |
| regex_v8       | 27.8 ms                                                | 23.8 ms: 1.17x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.25 ms: 1.12x faster                                                  |
| regex_dna      | 227 ms                                                 | 209 ms: 1.09x faster                                                   |
| Geometric mean | (ref)                                                  | 1.21x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250415-linux-x86_64-faster%2dcpython-fix_132508-3.14.0a7+-b1b1252 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                 |
| unpickle_pure_python | 331 us                                                 | 215 us: 1.54x faster                                                   |
| pickle_pure_python   | 484 us                                                 | 316 us: 1.53x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 58.4 ms: 1.35x faster                                                  |
| json_dumps           | 14.2 ms                                                | 11.7 ms: 1.21x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                                   |
| xml_etree_generate   | 99.4 ms                                                | 84.5 ms: 1.18x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 98.7 ms: 1.17x faster                                                  |
| json_loads           | 31.2 us                                                | 29.8 us: 1.05x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250415-linux-x86_64-faster%2dcpython-fix_132508-3.14.0a7+-b1b1252 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.3 ms: 1.10x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 8.28 ms: 1.40x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250415-linux-x86_64-faster%2dcpython-fix_132508-3.14.0a7+-b1b1252 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 20.6 ms: 1.54x faster                                                  |
| django_template | 48.2 ms                                                | 32.2 ms: 1.50x faster                                                  |
| mako            | 16.3 ms                                                | 11.3 ms: 1.44x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 49.3 ms: 1.34x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250415-linux-x86_64-faster%2dcpython-fix_132508-3.14.0a7+-b1b1252 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 165 us: 3.30x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 609 ms: 2.91x faster                                                   |
| async_tree_none          | 728 ms                                                 | 256 ms: 2.85x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 307 ms: 2.84x faster                                                   |
| generators               | 80.1 ms                                                | 29.5 ms: 2.71x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.32 ms: 2.38x faster                                                  |
| mdp                      | 2.85 sec                                               | 1.20 sec: 2.37x faster                                                 |
| go                       | 240 ms                                                 | 110 ms: 2.19x faster                                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 479 ms: 2.12x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 28.4 us: 2.06x faster                                                  |
| chaos                    | 115 ms                                                 | 56.5 ms: 2.04x faster                                                  |
| logging_silent           | 190 ns                                                 | 94.9 ns: 2.00x faster                                                  |
| pylint                   | 551 ms                                                 | 278 ms: 1.98x faster                                                   |
| raytrace                 | 507 ms                                                 | 262 ms: 1.93x faster                                                   |
| richards_super           | 94.7 ms                                                | 49.1 ms: 1.93x faster                                                  |
| deepcopy                 | 479 us                                                 | 251 us: 1.91x faster                                                   |
| scimark_sor              | 220 ms                                                 | 117 ms: 1.88x faster                                                   |
| richards                 | 79.3 ms                                                | 42.9 ms: 1.85x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 65.8 ms: 1.79x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 73.5 ms: 1.74x faster                                                  |
| float                    | 117 ms                                                 | 68.8 ms: 1.70x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.13 ms: 1.70x faster                                                  |
| pyflate                  | 716 ms                                                 | 434 ms: 1.65x faster                                                   |
| spectral_norm            | 170 ms                                                 | 104 ms: 1.63x faster                                                   |
| tomli_loads              | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                 |
| nbody                    | 154 ms                                                 | 96.6 ms: 1.59x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.67 us: 1.56x faster                                                  |
| genshi_text              | 31.8 ms                                                | 20.6 ms: 1.54x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 215 us: 1.54x faster                                                   |
| pickle_pure_python       | 484 us                                                 | 316 us: 1.53x faster                                                   |
| regex_compile            | 188 ms                                                 | 125 ms: 1.51x faster                                                   |
| logging_simple           | 8.30 us                                                | 5.52 us: 1.50x faster                                                  |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.50x faster                                                   |
| django_template          | 48.2 ms                                                | 32.2 ms: 1.50x faster                                                  |
| html5lib                 | 88.9 ms                                                | 59.6 ms: 1.49x faster                                                  |
| logging_format           | 9.09 us                                                | 6.13 us: 1.48x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.44 sec: 1.46x faster                                                 |
| coroutines               | 35.1 ms                                                | 24.2 ms: 1.45x faster                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 703 ms: 1.45x faster                                                   |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.44x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 59.8 ms: 1.41x faster                                                  |
| 2to3                     | 348 ms                                                 | 250 ms: 1.39x faster                                                   |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.9 ms: 1.38x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 19.0 ms: 1.36x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 58.4 ms: 1.35x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 49.3 ms: 1.34x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.85 ms: 1.33x faster                                                  |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.33x faster                                                   |
| scimark_fft              | 466 ms                                                 | 356 ms: 1.31x faster                                                   |
| sympy_str                | 346 ms                                                 | 266 ms: 1.30x faster                                                   |
| sqlalchemy_declarative   | 172 ms                                                 | 133 ms: 1.29x faster                                                   |
| nqueens                  | 106 ms                                                 | 81.9 ms: 1.29x faster                                                  |
| fannkuch                 | 532 ms                                                 | 419 ms: 1.27x faster                                                   |
| docutils                 | 3.30 sec                                               | 2.60 sec: 1.27x faster                                                 |
| sympy_expand             | 566 ms                                                 | 451 ms: 1.25x faster                                                   |
| json_dumps               | 14.2 ms                                                | 11.7 ms: 1.21x faster                                                  |
| pathlib                  | 20.5 ms                                                | 16.9 ms: 1.21x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 84.5 ms: 1.18x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 98.7 ms: 1.17x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 23.8 ms: 1.17x faster                                                  |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.14x faster                                                   |
| async_generators         | 444 ms                                                 | 393 ms: 1.13x faster                                                   |
| regex_effbot             | 3.63 ms                                                | 3.25 ms: 1.12x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 886 us: 1.11x faster                                                   |
| python_startup           | 14.6 ms                                                | 13.3 ms: 1.10x faster                                                  |
| regex_dna                | 227 ms                                                 | 209 ms: 1.09x faster                                                   |
| sqlite_synth             | 3.02 us                                                | 2.79 us: 1.09x faster                                                  |
| json                     | 5.69 ms                                                | 5.28 ms: 1.08x faster                                                  |
| json_loads               | 31.2 us                                                | 29.8 us: 1.05x faster                                                  |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                   |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                   |
| telco                    | 7.27 ms                                                | 7.64 ms: 1.05x slower                                                  |
| coverage                 | 79.4 ms                                                | 87.4 ms: 1.10x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 4.65 ms: 1.28x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 8.28 ms: 1.40x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.47 ms: 1.53x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 82.9 ms: 3.45x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.44x faster                                                           |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250415-3.14.0a7+-b1b1252/bm-20250415-linux-x86_64-faster%2dcpython-fix_132508-3.14.0a7+-b1b1252.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.465x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.36x
- 95% likely to have a speedup of 1.35x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: 1.28x