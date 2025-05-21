# Results vs. 3.10.4

- fork: brandtbucher
- ref: cached_attributes
- machine: linux-x86_64
- commit hash: 0e20c44
- commit date: 2025-05-21
- overall geometric mean: 1.314x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250521-linux-x86_64-brandtbucher-cached_attributes-3.15.0a0-0e20c44 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 262 ms: 1.33x faster                                                     |
| docutils       | 3.30 sec                                               | 2.67 sec: 1.23x faster                                                   |
| html5lib       | 88.9 ms                                                | 62.9 ms: 1.41x faster                                                    |
| Geometric mean | (ref)                                                  | 1.32x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250521-linux-x86_64-brandtbucher-cached_attributes-3.15.0a0-0e20c44 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 595 ms: 2.97x faster                                                     |
| async_tree_none         | 728 ms                                                 | 260 ms: 2.80x faster                                                     |
| async_tree_memoization  | 870 ms                                                 | 312 ms: 2.78x faster                                                     |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 489 ms: 2.08x faster                                                     |
| Geometric mean          | (ref)                                                  | 2.63x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250521-linux-x86_64-brandtbucher-cached_attributes-3.15.0a0-0e20c44 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 64.2 ms: 1.82x faster                                                    |
| nbody          | 154 ms                                                 | 92.9 ms: 1.65x faster                                                    |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                  | 1.45x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250521-linux-x86_64-brandtbucher-cached_attributes-3.15.0a0-0e20c44 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.47x faster                                                     |
| regex_v8       | 27.8 ms                                                | 22.3 ms: 1.25x faster                                                    |
| regex_effbot   | 3.63 ms                                                | 3.08 ms: 1.18x faster                                                    |
| regex_dna      | 227 ms                                                 | 203 ms: 1.12x faster                                                     |
| Geometric mean | (ref)                                                  | 1.25x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250521-linux-x86_64-brandtbucher-cached_attributes-3.15.0a0-0e20c44 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.88 sec: 1.67x faster                                                   |
| unpickle_pure_python | 331 us                                                 | 203 us: 1.63x faster                                                     |
| pickle_pure_python   | 484 us                                                 | 322 us: 1.50x faster                                                     |
| xml_etree_process    | 79.1 ms                                                | 55.8 ms: 1.42x faster                                                    |
| json_dumps           | 14.2 ms                                                | 11.0 ms: 1.29x faster                                                    |
| xml_etree_generate   | 99.4 ms                                                | 80.6 ms: 1.23x faster                                                    |
| xml_etree_parse      | 168 ms                                                 | 139 ms: 1.21x faster                                                     |
| xml_etree_iterparse  | 115 ms                                                 | 97.4 ms: 1.19x faster                                                    |
| json_loads           | 31.2 us                                                | 29.8 us: 1.05x faster                                                    |
| Geometric mean       | (ref)                                                  | 1.34x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250521-linux-x86_64-brandtbucher-cached_attributes-3.15.0a0-0e20c44 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.19x faster                                                    |
| python_startup_no_site | 5.93 ms                                                | 6.94 ms: 1.17x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250521-linux-x86_64-brandtbucher-cached_attributes-3.15.0a0-0e20c44 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.7 ms: 1.53x faster                                                    |
| django_template | 48.2 ms                                                | 32.5 ms: 1.48x faster                                                    |
| genshi_text     | 31.8 ms                                                | 21.5 ms: 1.48x faster                                                    |
| genshi_xml      | 66.0 ms                                                | 49.8 ms: 1.33x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250521-linux-x86_64-brandtbucher-cached_attributes-3.15.0a0-0e20c44 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 173 us: 3.15x faster                                                     |
| async_tree_io            | 1.77 sec                                               | 595 ms: 2.97x faster                                                     |
| async_tree_none          | 728 ms                                                 | 260 ms: 2.80x faster                                                     |
| async_tree_memoization   | 870 ms                                                 | 312 ms: 2.78x faster                                                     |
| generators               | 80.1 ms                                                | 30.8 ms: 2.60x faster                                                    |
| deltablue                | 7.91 ms                                                | 3.08 ms: 2.57x faster                                                    |
| richards_super           | 94.7 ms                                                | 38.3 ms: 2.48x faster                                                    |
| richards                 | 79.3 ms                                                | 33.3 ms: 2.38x faster                                                    |
| mdp                      | 2.85 sec                                               | 1.24 sec: 2.29x faster                                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 489 ms: 2.08x faster                                                     |
| deepcopy_memo            | 58.5 us                                                | 29.9 us: 1.95x faster                                                    |
| pylint                   | 551 ms                                                 | 285 ms: 1.94x faster                                                     |
| go                       | 240 ms                                                 | 125 ms: 1.92x faster                                                     |
| chaos                    | 115 ms                                                 | 60.7 ms: 1.90x faster                                                    |
| deepcopy                 | 479 us                                                 | 260 us: 1.84x faster                                                     |
| raytrace                 | 507 ms                                                 | 277 ms: 1.83x faster                                                     |
| float                    | 117 ms                                                 | 64.2 ms: 1.82x faster                                                    |
| scimark_sor              | 220 ms                                                 | 121 ms: 1.81x faster                                                     |
| scimark_monte_carlo      | 118 ms                                                 | 67.2 ms: 1.76x faster                                                    |
| spectral_norm            | 170 ms                                                 | 97.9 ms: 1.74x faster                                                    |
| crypto_pyaes             | 128 ms                                                 | 75.3 ms: 1.70x faster                                                    |
| tomli_loads              | 3.14 sec                                               | 1.88 sec: 1.67x faster                                                   |
| nbody                    | 154 ms                                                 | 92.9 ms: 1.65x faster                                                    |
| unpickle_pure_python     | 331 us                                                 | 203 us: 1.63x faster                                                     |
| pyflate                  | 716 ms                                                 | 448 ms: 1.60x faster                                                     |
| comprehensions           | 28.8 us                                                | 18.0 us: 1.60x faster                                                    |
| hexiom                   | 10.4 ms                                                | 6.60 ms: 1.58x faster                                                    |
| deepcopy_reduce          | 4.17 us                                                | 2.71 us: 1.54x faster                                                    |
| mako                     | 16.3 ms                                                | 10.7 ms: 1.53x faster                                                    |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.50x faster                                                     |
| pickle_pure_python       | 484 us                                                 | 322 us: 1.50x faster                                                     |
| django_template          | 48.2 ms                                                | 32.5 ms: 1.48x faster                                                    |
| genshi_text              | 31.8 ms                                                | 21.5 ms: 1.48x faster                                                    |
| regex_compile            | 188 ms                                                 | 129 ms: 1.47x faster                                                     |
| coroutines               | 35.1 ms                                                | 24.2 ms: 1.45x faster                                                    |
| pycparser                | 1.58 sec                                               | 1.11 sec: 1.42x faster                                                   |
| xml_etree_process        | 79.1 ms                                                | 55.8 ms: 1.42x faster                                                    |
| html5lib                 | 88.9 ms                                                | 62.9 ms: 1.41x faster                                                    |
| scimark_fft              | 466 ms                                                 | 332 ms: 1.40x faster                                                     |
| dulwich_log              | 84.3 ms                                                | 61.2 ms: 1.38x faster                                                    |
| sympy_integrate          | 25.8 ms                                                | 19.4 ms: 1.33x faster                                                    |
| 2to3                     | 348 ms                                                 | 262 ms: 1.33x faster                                                     |
| genshi_xml               | 66.0 ms                                                | 49.8 ms: 1.33x faster                                                    |
| logging_simple           | 8.30 us                                                | 6.28 us: 1.32x faster                                                    |
| sympy_sum                | 196 ms                                                 | 150 ms: 1.31x faster                                                     |
| json_dumps               | 14.2 ms                                                | 11.0 ms: 1.29x faster                                                    |
| logging_format           | 9.09 us                                                | 7.08 us: 1.28x faster                                                    |
| sympy_str                | 346 ms                                                 | 273 ms: 1.27x faster                                                     |
| fannkuch                 | 532 ms                                                 | 420 ms: 1.27x faster                                                     |
| nqueens                  | 106 ms                                                 | 83.5 ms: 1.27x faster                                                    |
| pprint_pformat           | 2.10 sec                                               | 1.66 sec: 1.26x faster                                                   |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.16 ms: 1.25x faster                                                    |
| pprint_safe_repr         | 1.02 sec                                               | 812 ms: 1.25x faster                                                     |
| regex_v8                 | 27.8 ms                                                | 22.3 ms: 1.25x faster                                                    |
| docutils                 | 3.30 sec                                               | 2.67 sec: 1.23x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 80.6 ms: 1.23x faster                                                    |
| xml_etree_parse          | 168 ms                                                 | 139 ms: 1.21x faster                                                     |
| sympy_expand             | 566 ms                                                 | 472 ms: 1.20x faster                                                     |
| pathlib                  | 20.5 ms                                                | 17.1 ms: 1.19x faster                                                    |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.19x faster                                                    |
| xml_etree_iterparse      | 115 ms                                                 | 97.4 ms: 1.19x faster                                                    |
| regex_effbot             | 3.63 ms                                                | 3.08 ms: 1.18x faster                                                    |
| regex_dna                | 227 ms                                                 | 203 ms: 1.12x faster                                                     |
| bench_thread_pool        | 986 us                                                 | 902 us: 1.09x faster                                                     |
| meteor_contest           | 120 ms                                                 | 110 ms: 1.09x faster                                                     |
| sqlite_synth             | 3.02 us                                                | 2.80 us: 1.08x faster                                                    |
| json                     | 5.69 ms                                                | 5.37 ms: 1.06x faster                                                    |
| json_loads               | 31.2 us                                                | 29.8 us: 1.05x faster                                                    |
| async_generators         | 444 ms                                                 | 428 ms: 1.04x faster                                                     |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                     |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                     |
| telco                    | 7.27 ms                                                | 7.85 ms: 1.08x slower                                                    |
| python_startup_no_site   | 5.93 ms                                                | 6.94 ms: 1.17x slower                                                    |
| gc_traversal             | 3.62 ms                                                | 4.93 ms: 1.36x slower                                                    |
| create_gc_cycles         | 1.62 ms                                                | 2.57 ms: 1.59x slower                                                    |
| dask                     | 441 ms                                                 | 924 ms: 2.10x slower                                                     |
| logging_silent           | 190 ns                                                 | 469 ns: 2.47x slower                                                     |
| bench_mp_pool            | 24.0 ms                                                | 93.0 ms: 3.87x slower                                                    |
| coverage                 | 79.4 ms                                                | 427 ms: 5.38x slower                                                     |
| thrift                   | 1.07 ms                                                | 148 ms: 138.41x slower                                                   |
| Geometric mean           | (ref)                                                  | 1.27x faster                                                             |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250521-3.15.0a0-0e20c44-JIT/bm-20250521-linux-x86_64-brandtbucher-cached_attributes-3.15.0a0-0e20c44.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.314x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.32x