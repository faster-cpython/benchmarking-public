# Results vs. 3.10.4

- fork: python
- ref: 0ac40acec045c4ce780c
- machine: linux-x86_64
- commit hash: 0ac40ac
- commit date: 2024-12-14
- overall geometric mean: 1.426x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 257 ms: 1.36x faster                                                   |
| docutils       | 3.30 sec                                               | 2.59 sec: 1.27x faster                                                 |
| html5lib       | 88.9 ms                                                | 64.1 ms: 1.39x faster                                                  |
| Geometric mean | (ref)                                                  | 1.34x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 627 ms: 2.82x faster                                                   |
| async_tree_none         | 728 ms                                                 | 271 ms: 2.69x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 339 ms: 2.56x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 500 ms: 2.03x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.51x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 95.5 ms: 1.61x faster                                                  |
| float          | 117 ms                                                 | 77.5 ms: 1.51x faster                                                  |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.36x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.48x faster                                                   |
| regex_v8       | 27.8 ms                                                | 25.0 ms: 1.11x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.31 ms: 1.10x faster                                                  |
| regex_dna      | 227 ms                                                 | 221 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                  | 1.17x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.04 sec: 1.54x faster                                                 |
| unpickle_pure_python | 331 us                                                 | 219 us: 1.51x faster                                                   |
| pickle_pure_python   | 484 us                                                 | 324 us: 1.50x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 59.9 ms: 1.32x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 138 ms: 1.22x faster                                                   |
| json_dumps           | 14.2 ms                                                | 11.6 ms: 1.22x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 97.3 ms: 1.19x faster                                                  |
| json_loads           | 31.2 us                                                | 27.1 us: 1.15x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 86.6 ms: 1.15x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 7.09 ms: 1.20x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.0 ms: 1.50x faster                                                  |
| genshi_text     | 31.8 ms                                                | 22.2 ms: 1.43x faster                                                  |
| mako            | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 49.8 ms: 1.33x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 162 us: 3.36x faster                                                   |
| generators               | 80.1 ms                                                | 28.2 ms: 2.84x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 627 ms: 2.82x faster                                                   |
| async_tree_none          | 728 ms                                                 | 271 ms: 2.69x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 339 ms: 2.56x faster                                                   |
| deltablue                | 7.91 ms                                                | 3.25 ms: 2.43x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 500 ms: 2.03x faster                                                   |
| go                       | 240 ms                                                 | 120 ms: 1.99x faster                                                   |
| pylint                   | 551 ms                                                 | 277 ms: 1.99x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 31.0 us: 1.89x faster                                                  |
| chaos                    | 115 ms                                                 | 61.4 ms: 1.88x faster                                                  |
| raytrace                 | 507 ms                                                 | 272 ms: 1.86x faster                                                   |
| richards_super           | 94.7 ms                                                | 52.4 ms: 1.81x faster                                                  |
| logging_silent           | 190 ns                                                 | 106 ns: 1.79x faster                                                   |
| deepcopy                 | 479 us                                                 | 268 us: 1.79x faster                                                   |
| djangocms                | 38.4 us                                                | 21.8 us: 1.76x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 72.8 ms: 1.76x faster                                                  |
| scimark_sor              | 220 ms                                                 | 125 ms: 1.76x faster                                                   |
| scimark_monte_carlo      | 118 ms                                                 | 68.1 ms: 1.74x faster                                                  |
| richards                 | 79.3 ms                                                | 45.8 ms: 1.73x faster                                                  |
| comprehensions           | 28.8 us                                                | 17.0 us: 1.69x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.68x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.23 ms: 1.67x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.60 ms: 1.61x faster                                                  |
| nbody                    | 154 ms                                                 | 95.5 ms: 1.61x faster                                                  |
| spectral_norm            | 170 ms                                                 | 108 ms: 1.57x faster                                                   |
| tomli_loads              | 3.14 sec                                               | 2.04 sec: 1.54x faster                                                 |
| pyflate                  | 716 ms                                                 | 467 ms: 1.54x faster                                                   |
| coroutines               | 35.1 ms                                                | 23.2 ms: 1.51x faster                                                  |
| float                    | 117 ms                                                 | 77.5 ms: 1.51x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 219 us: 1.51x faster                                                   |
| django_template          | 48.2 ms                                                | 32.0 ms: 1.50x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 324 us: 1.50x faster                                                   |
| logging_simple           | 8.30 us                                                | 5.56 us: 1.49x faster                                                  |
| scimark_lu               | 176 ms                                                 | 118 ms: 1.49x faster                                                   |
| logging_format           | 9.09 us                                                | 6.11 us: 1.49x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.81 us: 1.48x faster                                                  |
| regex_compile            | 188 ms                                                 | 128 ms: 1.48x faster                                                   |
| genshi_text              | 31.8 ms                                                | 22.2 ms: 1.43x faster                                                  |
| mako                     | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                  |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.4 ms: 1.42x faster                                                  |
| thrift                   | 1.07 ms                                                | 761 us: 1.41x faster                                                   |
| pprint_safe_repr         | 1.02 sec                                               | 734 ms: 1.39x faster                                                   |
| html5lib                 | 88.9 ms                                                | 64.1 ms: 1.39x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.52 sec: 1.38x faster                                                 |
| sqlglot_normalize        | 143 ms                                                 | 104 ms: 1.37x faster                                                   |
| 2to3                     | 348 ms                                                 | 257 ms: 1.36x faster                                                   |
| sqlalchemy_declarative   | 172 ms                                                 | 127 ms: 1.35x faster                                                   |
| scimark_fft              | 466 ms                                                 | 347 ms: 1.34x faster                                                   |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.34x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.87 ms: 1.33x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 49.8 ms: 1.33x faster                                                  |
| fannkuch                 | 532 ms                                                 | 401 ms: 1.32x faster                                                   |
| nqueens                  | 106 ms                                                 | 80.0 ms: 1.32x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 59.9 ms: 1.32x faster                                                  |
| sympy_sum                | 196 ms                                                 | 149 ms: 1.32x faster                                                   |
| sqlglot_optimize         | 69.2 ms                                                | 52.8 ms: 1.31x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 64.7 ms: 1.30x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 20.1 ms: 1.29x faster                                                  |
| sympy_str                | 346 ms                                                 | 270 ms: 1.28x faster                                                   |
| docutils                 | 3.30 sec                                               | 2.59 sec: 1.27x faster                                                 |
| pathlib                  | 20.5 ms                                                | 16.5 ms: 1.24x faster                                                  |
| sympy_expand             | 566 ms                                                 | 457 ms: 1.24x faster                                                   |
| xml_etree_parse          | 168 ms                                                 | 138 ms: 1.22x faster                                                   |
| json_dumps               | 14.2 ms                                                | 11.6 ms: 1.22x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 97.3 ms: 1.19x faster                                                  |
| json_loads               | 31.2 us                                                | 27.1 us: 1.15x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 86.6 ms: 1.15x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 862 us: 1.14x faster                                                   |
| python_startup           | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                  |
| json                     | 5.69 ms                                                | 5.05 ms: 1.13x faster                                                  |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                   |
| mdp                      | 2.85 sec                                               | 2.54 sec: 1.12x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 25.0 ms: 1.11x faster                                                  |
| regex_effbot             | 3.63 ms                                                | 3.31 ms: 1.10x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 2.83 us: 1.07x faster                                                  |
| async_generators         | 444 ms                                                 | 417 ms: 1.06x faster                                                   |
| regex_dna                | 227 ms                                                 | 221 ms: 1.03x faster                                                   |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                                   |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                   |
| coverage                 | 79.4 ms                                                | 83.2 ms: 1.05x slower                                                  |
| mypy2                    | 894 ms                                                 | 953 ms: 1.07x slower                                                   |
| telco                    | 7.27 ms                                                | 7.85 ms: 1.08x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 7.09 ms: 1.20x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 4.94 ms: 1.36x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.47 ms: 1.52x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 81.5 ms: 3.39x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                           |
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.426x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.27x