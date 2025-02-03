# Results vs. 3.10.4

- fork: python
- ref: cf4c4ecc26c7e3b89f2e
- machine: linux-x86_64
- commit hash: cf4c4ec
- commit date: 2025-02-01
- overall geometric mean: 1.437x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 260 ms: 1.34x faster                                                   |
| docutils       | 3.30 sec                                               | 2.67 sec: 1.23x faster                                                 |
| html5lib       | 88.9 ms                                                | 64.8 ms: 1.37x faster                                                  |
| Geometric mean | (ref)                                                  | 1.31x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 626 ms: 2.83x faster                                                   |
| async_tree_none         | 728 ms                                                 | 270 ms: 2.69x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 328 ms: 2.65x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 492 ms: 2.07x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.54x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 117 ms                                                 | 67.0 ms: 1.75x faster                                                  |
| nbody          | 154 ms                                                 | 88.0 ms: 1.75x faster                                                  |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                  | 1.46x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.47x faster                                                   |
| regex_v8       | 27.8 ms                                                | 23.5 ms: 1.18x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.17 ms: 1.15x faster                                                  |
| regex_dna      | 227 ms                                                 | 208 ms: 1.09x faster                                                   |
| Geometric mean | (ref)                                                  | 1.21x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.84 sec: 1.71x faster                                                 |
| unpickle_pure_python | 331 us                                                 | 196 us: 1.68x faster                                                   |
| pickle_pure_python   | 484 us                                                 | 309 us: 1.57x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 55.3 ms: 1.43x faster                                                  |
| json_dumps           | 14.2 ms                                                | 11.3 ms: 1.26x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 79.4 ms: 1.25x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 95.0 ms: 1.21x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 139 ms: 1.21x faster                                                   |
| json_loads           | 31.2 us                                                | 28.8 us: 1.09x faster                                                  |
| unpickle_list        | 5.20 us                                                | 5.60 us: 1.08x slower                                                  |
| pickle_list          | 5.08 us                                                | 5.70 us: 1.12x slower                                                  |
| pickle               | 10.7 us                                                | 12.7 us: 1.19x slower                                                  |
| pickle_dict          | 29.6 us                                                | 36.6 us: 1.24x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.0 ms: 1.63x faster                                                  |
| django_template | 48.2 ms                                                | 33.8 ms: 1.43x faster                                                  |
| genshi_text     | 31.8 ms                                                | 23.1 ms: 1.38x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 58.4 ms: 1.13x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.38x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.25x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 626 ms: 2.83x faster                                                   |
| async_tree_none          | 728 ms                                                 | 270 ms: 2.69x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 328 ms: 2.65x faster                                                   |
| deltablue                | 7.91 ms                                                | 3.47 ms: 2.28x faster                                                  |
| generators               | 80.1 ms                                                | 37.4 ms: 2.14x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 492 ms: 2.07x faster                                                   |
| chaos                    | 115 ms                                                 | 58.6 ms: 1.97x faster                                                  |
| go                       | 240 ms                                                 | 124 ms: 1.93x faster                                                   |
| richards_super           | 94.7 ms                                                | 49.2 ms: 1.93x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 30.4 us: 1.92x faster                                                  |
| pylint                   | 551 ms                                                 | 287 ms: 1.92x faster                                                   |
| scimark_sor              | 220 ms                                                 | 115 ms: 1.91x faster                                                   |
| scimark_monte_carlo      | 118 ms                                                 | 62.7 ms: 1.89x faster                                                  |
| asyncio_tcp              | 922 ms                                                 | 490 ms: 1.88x faster                                                   |
| richards                 | 79.3 ms                                                | 43.0 ms: 1.84x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 70.0 ms: 1.83x faster                                                  |
| spectral_norm            | 170 ms                                                 | 94.4 ms: 1.80x faster                                                  |
| raytrace                 | 507 ms                                                 | 288 ms: 1.76x faster                                                   |
| float                    | 117 ms                                                 | 67.0 ms: 1.75x faster                                                  |
| nbody                    | 154 ms                                                 | 88.0 ms: 1.75x faster                                                  |
| logging_silent           | 190 ns                                                 | 109 ns: 1.74x faster                                                   |
| deepcopy                 | 479 us                                                 | 279 us: 1.72x faster                                                   |
| tomli_loads              | 3.14 sec                                               | 1.84 sec: 1.71x faster                                                 |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.69x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 196 us: 1.68x faster                                                   |
| comprehensions           | 28.8 us                                                | 17.2 us: 1.67x faster                                                  |
| mako                     | 16.3 ms                                                | 10.0 ms: 1.63x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.59 ms: 1.62x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 309 us: 1.57x faster                                                   |
| deepcopy_reduce          | 4.17 us                                                | 2.70 us: 1.54x faster                                                  |
| pyflate                  | 716 ms                                                 | 465 ms: 1.54x faster                                                   |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.52x faster                                                   |
| scimark_fft              | 466 ms                                                 | 310 ms: 1.50x faster                                                   |
| coroutines               | 35.1 ms                                                | 23.5 ms: 1.50x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.33 ms: 1.49x faster                                                  |
| regex_compile            | 188 ms                                                 | 128 ms: 1.47x faster                                                   |
| xml_etree_process        | 79.1 ms                                                | 55.3 ms: 1.43x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.81 us: 1.43x faster                                                  |
| django_template          | 48.2 ms                                                | 33.8 ms: 1.43x faster                                                  |
| logging_format           | 9.09 us                                                | 6.38 us: 1.42x faster                                                  |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.82 sec: 1.41x faster                                                 |
| thrift                   | 1.07 ms                                                | 760 us: 1.41x faster                                                   |
| hexiom                   | 10.4 ms                                                | 7.40 ms: 1.40x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.39x faster                                                 |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.8 ms: 1.39x faster                                                  |
| genshi_text              | 31.8 ms                                                | 23.1 ms: 1.38x faster                                                  |
| html5lib                 | 88.9 ms                                                | 64.8 ms: 1.37x faster                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 744 ms: 1.37x faster                                                   |
| fannkuch                 | 532 ms                                                 | 390 ms: 1.36x faster                                                   |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                                 |
| 2to3                     | 348 ms                                                 | 260 ms: 1.34x faster                                                   |
| sqlalchemy_declarative   | 172 ms                                                 | 131 ms: 1.31x faster                                                   |
| sqlglot_normalize        | 143 ms                                                 | 109 ms: 1.31x faster                                                   |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.29x faster                                                  |
| sympy_sum                | 196 ms                                                 | 155 ms: 1.27x faster                                                   |
| dulwich_log              | 84.3 ms                                                | 66.7 ms: 1.26x faster                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 55.0 ms: 1.26x faster                                                  |
| json_dumps               | 14.2 ms                                                | 11.3 ms: 1.26x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 20.5 ms: 1.26x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 79.4 ms: 1.25x faster                                                  |
| sympy_str                | 346 ms                                                 | 280 ms: 1.23x faster                                                   |
| docutils                 | 3.30 sec                                               | 2.67 sec: 1.23x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 95.0 ms: 1.21x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 139 ms: 1.21x faster                                                   |
| sympy_expand             | 566 ms                                                 | 471 ms: 1.20x faster                                                   |
| nqueens                  | 106 ms                                                 | 89.2 ms: 1.19x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 23.5 ms: 1.18x faster                                                  |
| regex_effbot             | 3.63 ms                                                | 3.17 ms: 1.15x faster                                                  |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 58.4 ms: 1.13x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.56 sec: 1.11x faster                                                 |
| sqlite_synth             | 3.02 us                                                | 2.72 us: 1.11x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 891 us: 1.11x faster                                                   |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                   |
| json                     | 5.69 ms                                                | 5.19 ms: 1.10x faster                                                  |
| async_generators         | 444 ms                                                 | 407 ms: 1.09x faster                                                   |
| regex_dna                | 227 ms                                                 | 208 ms: 1.09x faster                                                   |
| json_loads               | 31.2 us                                                | 28.8 us: 1.09x faster                                                  |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                   |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                   |
| telco                    | 7.27 ms                                                | 7.62 ms: 1.05x slower                                                  |
| unpickle_list            | 5.20 us                                                | 5.60 us: 1.08x slower                                                  |
| pickle_list              | 5.08 us                                                | 5.70 us: 1.12x slower                                                  |
| coverage                 | 79.4 ms                                                | 89.6 ms: 1.13x slower                                                  |
| unpack_sequence          | 60.0 ns                                                | 70.4 ns: 1.17x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                  |
| pickle                   | 10.7 us                                                | 12.7 us: 1.19x slower                                                  |
| pickle_dict              | 29.6 us                                                | 36.6 us: 1.24x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 4.72 ms: 1.30x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.46 ms: 1.52x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 80.8 ms: 3.36x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.37x faster                                                           |

Benchmark hidden because not significant (1): unpickle
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, tornado_http
Ignored benchmarks (11) of results/bm-20250201-3.14.0a4+-cf4c4ec-JIT/bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.437x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: 1.28x