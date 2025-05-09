# Results vs. 3.10.4

- fork: python
- ref: 0cd4befb02df07c0b320
- machine: linux-x86_64
- commit hash: 0cd4bef
- commit date: 2025-03-31
- overall geometric mean: 1.453x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 254 ms: 1.37x faster                                                   |
| docutils       | 3.30 sec                                               | 2.60 sec: 1.27x faster                                                 |
| html5lib       | 88.9 ms                                                | 63.0 ms: 1.41x faster                                                  |
| Geometric mean | (ref)                                                  | 1.35x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 610 ms: 2.90x faster                                                   |
| async_tree_none         | 728 ms                                                 | 259 ms: 2.82x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 312 ms: 2.79x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 483 ms: 2.10x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.63x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 117 ms                                                 | 69.3 ms: 1.69x faster                                                  |
| nbody          | 154 ms                                                 | 96.4 ms: 1.59x faster                                                  |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.40x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.49x faster                                                   |
| regex_v8       | 27.8 ms                                                | 22.9 ms: 1.21x faster                                                  |
| regex_dna      | 227 ms                                                 | 215 ms: 1.05x faster                                                   |
| regex_effbot   | 3.63 ms                                                | 3.80 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                  | 1.16x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                 |
| unpickle_pure_python | 331 us                                                 | 219 us: 1.51x faster                                                   |
| pickle_pure_python   | 484 us                                                 | 321 us: 1.51x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 58.9 ms: 1.34x faster                                                  |
| json_dumps           | 14.2 ms                                                | 11.5 ms: 1.24x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.20x faster                                                   |
| xml_etree_generate   | 99.4 ms                                                | 85.0 ms: 1.17x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 99.1 ms: 1.17x faster                                                  |
| json_loads           | 31.2 us                                                | 29.9 us: 1.04x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.12x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 8.16 ms: 1.38x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.9 ms: 1.51x faster                                                  |
| genshi_text     | 31.8 ms                                                | 21.5 ms: 1.48x faster                                                  |
| mako            | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 49.6 ms: 1.33x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 161 us: 3.38x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 610 ms: 2.90x faster                                                   |
| async_tree_none          | 728 ms                                                 | 259 ms: 2.82x faster                                                   |
| generators               | 80.1 ms                                                | 28.6 ms: 2.80x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 312 ms: 2.79x faster                                                   |
| deltablue                | 7.91 ms                                                | 3.15 ms: 2.51x faster                                                  |
| mdp                      | 2.85 sec                                               | 1.24 sec: 2.30x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 483 ms: 2.10x faster                                                   |
| go                       | 240 ms                                                 | 115 ms: 2.09x faster                                                   |
| pylint                   | 551 ms                                                 | 276 ms: 2.00x faster                                                   |
| chaos                    | 115 ms                                                 | 58.1 ms: 1.99x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 30.0 us: 1.95x faster                                                  |
| logging_silent           | 190 ns                                                 | 98.9 ns: 1.92x faster                                                  |
| raytrace                 | 507 ms                                                 | 266 ms: 1.91x faster                                                   |
| richards_super           | 94.7 ms                                                | 50.6 ms: 1.87x faster                                                  |
| deepcopy                 | 479 us                                                 | 258 us: 1.86x faster                                                   |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.85x faster                                                   |
| spectral_norm            | 170 ms                                                 | 96.3 ms: 1.76x faster                                                  |
| richards                 | 79.3 ms                                                | 44.9 ms: 1.76x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 67.9 ms: 1.74x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 73.8 ms: 1.73x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.73x faster                                                  |
| float                    | 117 ms                                                 | 69.3 ms: 1.69x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.25 ms: 1.66x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                 |
| pyflate                  | 716 ms                                                 | 449 ms: 1.59x faster                                                   |
| nbody                    | 154 ms                                                 | 96.4 ms: 1.59x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.70 us: 1.55x faster                                                  |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.53x faster                                                   |
| unpickle_pure_python     | 331 us                                                 | 219 us: 1.51x faster                                                   |
| pickle_pure_python       | 484 us                                                 | 321 us: 1.51x faster                                                   |
| django_template          | 48.2 ms                                                | 31.9 ms: 1.51x faster                                                  |
| coroutines               | 35.1 ms                                                | 23.4 ms: 1.50x faster                                                  |
| regex_compile            | 188 ms                                                 | 127 ms: 1.49x faster                                                   |
| genshi_text              | 31.8 ms                                                | 21.5 ms: 1.48x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.66 us: 1.47x faster                                                  |
| logging_format           | 9.09 us                                                | 6.21 us: 1.46x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 58.4 ms: 1.44x faster                                                  |
| mako                     | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                                 |
| html5lib                 | 88.9 ms                                                | 63.0 ms: 1.41x faster                                                  |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.6 ms: 1.40x faster                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 726 ms: 1.40x faster                                                   |
| 2to3                     | 348 ms                                                 | 254 ms: 1.37x faster                                                   |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.35x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 19.2 ms: 1.35x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 58.9 ms: 1.34x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 49.6 ms: 1.33x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.86 ms: 1.33x faster                                                  |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.33x faster                                                   |
| sqlalchemy_declarative   | 172 ms                                                 | 130 ms: 1.32x faster                                                   |
| scimark_fft              | 466 ms                                                 | 355 ms: 1.31x faster                                                   |
| sympy_str                | 346 ms                                                 | 268 ms: 1.29x faster                                                   |
| nqueens                  | 106 ms                                                 | 82.6 ms: 1.28x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.60 sec: 1.27x faster                                                 |
| pathlib                  | 20.5 ms                                                | 16.3 ms: 1.26x faster                                                  |
| fannkuch                 | 532 ms                                                 | 426 ms: 1.25x faster                                                   |
| json_dumps               | 14.2 ms                                                | 11.5 ms: 1.24x faster                                                  |
| sympy_expand             | 566 ms                                                 | 461 ms: 1.23x faster                                                   |
| regex_v8                 | 27.8 ms                                                | 22.9 ms: 1.21x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.20x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 85.0 ms: 1.17x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 99.1 ms: 1.17x faster                                                  |
| async_generators         | 444 ms                                                 | 389 ms: 1.14x faster                                                   |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.13x faster                                                   |
| bench_thread_pool        | 986 us                                                 | 872 us: 1.13x faster                                                   |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.12x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 2.81 us: 1.08x faster                                                  |
| json                     | 5.69 ms                                                | 5.35 ms: 1.06x faster                                                  |
| regex_dna                | 227 ms                                                 | 215 ms: 1.05x faster                                                   |
| json_loads               | 31.2 us                                                | 29.9 us: 1.04x faster                                                  |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                   |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                   |
| regex_effbot             | 3.63 ms                                                | 3.80 ms: 1.05x slower                                                  |
| coverage                 | 79.4 ms                                                | 84.3 ms: 1.06x slower                                                  |
| telco                    | 7.27 ms                                                | 7.86 ms: 1.08x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 8.16 ms: 1.38x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 5.02 ms: 1.38x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.50 ms: 1.54x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 82.5 ms: 3.44x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                           |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250331-3.14.0a6+-0cd4bef/bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.453x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.36x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.28x