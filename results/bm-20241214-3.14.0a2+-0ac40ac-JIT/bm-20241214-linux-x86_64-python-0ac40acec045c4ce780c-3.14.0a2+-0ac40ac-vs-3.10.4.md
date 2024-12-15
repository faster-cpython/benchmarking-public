# Results vs. 3.10.4

- fork: python
- ref: 0ac40acec045c4ce780c
- machine: linux-x86_64
- commit hash: 0ac40ac
- commit date: 2024-12-14
- overall geometric mean: 1.429x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 259 ms: 1.34x faster                                                   |
| docutils       | 3.30 sec                                               | 2.70 sec: 1.22x faster                                                 |
| html5lib       | 88.9 ms                                                | 65.3 ms: 1.36x faster                                                  |
| Geometric mean | (ref)                                                  | 1.31x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 619 ms: 2.86x faster                                                   |
| async_tree_none         | 728 ms                                                 | 266 ms: 2.73x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 336 ms: 2.59x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 496 ms: 2.05x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.54x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 82.6 ms: 1.86x faster                                                  |
| float          | 117 ms                                                 | 73.3 ms: 1.60x faster                                                  |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                  | 1.45x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.47x faster                                                   |
| regex_v8       | 27.8 ms                                                | 24.7 ms: 1.12x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.24 ms: 1.12x faster                                                  |
| regex_dna      | 227 ms                                                 | 219 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                  | 1.18x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 193 us: 1.71x faster                                                   |
| tomli_loads          | 3.14 sec                                               | 1.85 sec: 1.70x faster                                                 |
| pickle_pure_python   | 484 us                                                 | 321 us: 1.51x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 55.7 ms: 1.42x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 78.3 ms: 1.27x faster                                                  |
| json_dumps           | 14.2 ms                                                | 11.4 ms: 1.25x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 137 ms: 1.23x faster                                                   |
| xml_etree_iterparse  | 115 ms                                                 | 94.5 ms: 1.22x faster                                                  |
| json_loads           | 31.2 us                                                | 26.0 us: 1.20x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.38x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.3 ms: 1.58x faster                                                  |
| django_template | 48.2 ms                                                | 33.9 ms: 1.42x faster                                                  |
| genshi_text     | 31.8 ms                                                | 23.8 ms: 1.34x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 58.6 ms: 1.13x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.36x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 166 us: 3.28x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 619 ms: 2.86x faster                                                   |
| async_tree_none          | 728 ms                                                 | 266 ms: 2.73x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 336 ms: 2.59x faster                                                   |
| deltablue                | 7.91 ms                                                | 3.29 ms: 2.41x faster                                                  |
| generators               | 80.1 ms                                                | 34.6 ms: 2.32x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 496 ms: 2.05x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 29.8 us: 1.96x faster                                                  |
| scimark_sor              | 220 ms                                                 | 114 ms: 1.93x faster                                                   |
| go                       | 240 ms                                                 | 125 ms: 1.91x faster                                                   |
| scimark_monte_carlo      | 118 ms                                                 | 62.0 ms: 1.91x faster                                                  |
| pylint                   | 551 ms                                                 | 290 ms: 1.90x faster                                                   |
| crypto_pyaes             | 128 ms                                                 | 68.0 ms: 1.88x faster                                                  |
| chaos                    | 115 ms                                                 | 61.5 ms: 1.88x faster                                                  |
| nbody                    | 154 ms                                                 | 82.6 ms: 1.86x faster                                                  |
| richards_super           | 94.7 ms                                                | 51.4 ms: 1.84x faster                                                  |
| raytrace                 | 507 ms                                                 | 284 ms: 1.79x faster                                                   |
| deepcopy                 | 479 us                                                 | 270 us: 1.77x faster                                                   |
| richards                 | 79.3 ms                                                | 44.7 ms: 1.77x faster                                                  |
| logging_silent           | 190 ns                                                 | 107 ns: 1.77x faster                                                   |
| djangocms                | 38.4 us                                                | 22.3 us: 1.73x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 193 us: 1.71x faster                                                   |
| tomli_loads              | 3.14 sec                                               | 1.85 sec: 1.70x faster                                                 |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.70x faster                                                  |
| comprehensions           | 28.8 us                                                | 17.1 us: 1.68x faster                                                  |
| spectral_norm            | 170 ms                                                 | 103 ms: 1.65x faster                                                   |
| sqlglot_transpile        | 2.57 ms                                                | 1.61 ms: 1.60x faster                                                  |
| float                    | 117 ms                                                 | 73.3 ms: 1.60x faster                                                  |
| pyflate                  | 716 ms                                                 | 452 ms: 1.59x faster                                                   |
| mako                     | 16.3 ms                                                | 10.3 ms: 1.58x faster                                                  |
| coroutines               | 35.1 ms                                                | 23.2 ms: 1.51x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.76 us: 1.51x faster                                                  |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.51x faster                                                   |
| pickle_pure_python       | 484 us                                                 | 321 us: 1.51x faster                                                   |
| scimark_fft              | 466 ms                                                 | 313 ms: 1.49x faster                                                   |
| hexiom                   | 10.4 ms                                                | 7.03 ms: 1.48x faster                                                  |
| regex_compile            | 188 ms                                                 | 128 ms: 1.47x faster                                                   |
| logging_simple           | 8.30 us                                                | 5.71 us: 1.46x faster                                                  |
| logging_format           | 9.09 us                                                | 6.27 us: 1.45x faster                                                  |
| django_template          | 48.2 ms                                                | 33.9 ms: 1.42x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 55.7 ms: 1.42x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.41x faster                                                 |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.7 ms: 1.40x faster                                                  |
| thrift                   | 1.07 ms                                                | 769 us: 1.39x faster                                                   |
| fannkuch                 | 532 ms                                                 | 385 ms: 1.38x faster                                                   |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.74 ms: 1.36x faster                                                  |
| html5lib                 | 88.9 ms                                                | 65.3 ms: 1.36x faster                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 752 ms: 1.35x faster                                                   |
| 2to3                     | 348 ms                                                 | 259 ms: 1.34x faster                                                   |
| genshi_text              | 31.8 ms                                                | 23.8 ms: 1.34x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.33x faster                                                 |
| sqlalchemy_declarative   | 172 ms                                                 | 129 ms: 1.33x faster                                                   |
| sqlglot_normalize        | 143 ms                                                 | 109 ms: 1.31x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 78.3 ms: 1.27x faster                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 54.8 ms: 1.26x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 66.9 ms: 1.26x faster                                                  |
| sympy_sum                | 196 ms                                                 | 156 ms: 1.26x faster                                                   |
| json_dumps               | 14.2 ms                                                | 11.4 ms: 1.25x faster                                                  |
| pathlib                  | 20.5 ms                                                | 16.4 ms: 1.24x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 20.8 ms: 1.24x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 137 ms: 1.23x faster                                                   |
| docutils                 | 3.30 sec                                               | 2.70 sec: 1.22x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 94.5 ms: 1.22x faster                                                  |
| sympy_str                | 346 ms                                                 | 283 ms: 1.22x faster                                                   |
| json_loads               | 31.2 us                                                | 26.0 us: 1.20x faster                                                  |
| nqueens                  | 106 ms                                                 | 89.1 ms: 1.19x faster                                                  |
| sympy_expand             | 566 ms                                                 | 478 ms: 1.18x faster                                                   |
| json                     | 5.69 ms                                                | 4.81 ms: 1.18x faster                                                  |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 58.6 ms: 1.13x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 24.7 ms: 1.12x faster                                                  |
| regex_effbot             | 3.63 ms                                                | 3.24 ms: 1.12x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 887 us: 1.11x faster                                                   |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                   |
| sqlite_synth             | 3.02 us                                                | 2.77 us: 1.09x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.69 sec: 1.06x faster                                                 |
| regex_dna                | 227 ms                                                 | 219 ms: 1.04x faster                                                   |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                   |
| asyncio_websockets       | 559 ms                                                 | 556 ms: 1.00x faster                                                   |
| async_generators         | 444 ms                                                 | 446 ms: 1.00x slower                                                   |
| telco                    | 7.27 ms                                                | 7.59 ms: 1.04x slower                                                  |
| coverage                 | 79.4 ms                                                | 84.1 ms: 1.06x slower                                                  |
| mypy2                    | 894 ms                                                 | 965 ms: 1.08x slower                                                   |
| python_startup_no_site   | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 4.95 ms: 1.37x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.47 ms: 1.52x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 81.2 ms: 3.38x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                           |
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241214-3.14.0a2+-0ac40ac-JIT/bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.429x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.29x