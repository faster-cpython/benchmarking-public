# Results vs. 3.10.4

- fork: python
- ref: cf4c4ecc26c7e3b89f2e
- machine: linux-x86_64
- commit hash: cf4c4ec
- commit date: 2025-02-01
- overall geometric mean: 1.447x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 254 ms: 1.37x faster                                                   |
| docutils       | 3.30 sec                                               | 2.62 sec: 1.26x faster                                                 |
| html5lib       | 88.9 ms                                                | 61.3 ms: 1.45x faster                                                  |
| Geometric mean | (ref)                                                  | 1.36x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 620 ms: 2.85x faster                                                   |
| async_tree_none         | 728 ms                                                 | 263 ms: 2.76x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 322 ms: 2.70x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 495 ms: 2.05x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.57x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 92.3 ms: 1.66x faster                                                  |
| float          | 117 ms                                                 | 71.4 ms: 1.64x faster                                                  |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                  | 1.41x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 126 ms: 1.49x faster                                                   |
| regex_v8       | 27.8 ms                                                | 25.7 ms: 1.08x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.40 ms: 1.07x faster                                                  |
| regex_dna      | 227 ms                                                 | 214 ms: 1.06x faster                                                   |
| Geometric mean | (ref)                                                  | 1.16x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                 |
| pickle_pure_python   | 484 us                                                 | 318 us: 1.52x faster                                                   |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.52x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 59.4 ms: 1.33x faster                                                  |
| json_dumps           | 14.2 ms                                                | 11.7 ms: 1.21x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 139 ms: 1.21x faster                                                   |
| xml_etree_iterparse  | 115 ms                                                 | 96.9 ms: 1.19x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 84.2 ms: 1.18x faster                                                  |
| json_loads           | 31.2 us                                                | 28.4 us: 1.10x faster                                                  |
| unpickle             | 14.4 us                                                | 13.9 us: 1.03x faster                                                  |
| pickle_list          | 5.08 us                                                | 5.42 us: 1.07x slower                                                  |
| unpickle_list        | 5.20 us                                                | 5.77 us: 1.11x slower                                                  |
| pickle               | 10.7 us                                                | 12.6 us: 1.18x slower                                                  |
| pickle_dict          | 29.6 us                                                | 35.3 us: 1.19x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.0 ms: 1.13x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 7.09 ms: 1.20x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.7 ms: 1.52x faster                                                  |
| genshi_text     | 31.8 ms                                                | 21.4 ms: 1.49x faster                                                  |
| mako            | 16.3 ms                                                | 11.5 ms: 1.42x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 48.2 ms: 1.37x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 158 us: 3.44x faster                                                   |
| generators               | 80.1 ms                                                | 27.5 ms: 2.91x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 620 ms: 2.85x faster                                                   |
| async_tree_none          | 728 ms                                                 | 263 ms: 2.76x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 322 ms: 2.70x faster                                                   |
| deltablue                | 7.91 ms                                                | 3.26 ms: 2.43x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 495 ms: 2.05x faster                                                   |
| go                       | 240 ms                                                 | 118 ms: 2.04x faster                                                   |
| pylint                   | 551 ms                                                 | 276 ms: 2.00x faster                                                   |
| chaos                    | 115 ms                                                 | 58.9 ms: 1.96x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 30.9 us: 1.89x faster                                                  |
| deepcopy                 | 479 us                                                 | 255 us: 1.88x faster                                                   |
| asyncio_tcp              | 922 ms                                                 | 491 ms: 1.88x faster                                                   |
| raytrace                 | 507 ms                                                 | 272 ms: 1.87x faster                                                   |
| richards_super           | 94.7 ms                                                | 51.1 ms: 1.85x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 70.3 ms: 1.82x faster                                                  |
| scimark_sor              | 220 ms                                                 | 123 ms: 1.79x faster                                                   |
| logging_silent           | 190 ns                                                 | 107 ns: 1.78x faster                                                   |
| richards                 | 79.3 ms                                                | 45.0 ms: 1.76x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 67.5 ms: 1.75x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.27 ms: 1.71x faster                                                  |
| spectral_norm            | 170 ms                                                 | 101 ms: 1.69x faster                                                   |
| hexiom                   | 10.4 ms                                                | 6.22 ms: 1.67x faster                                                  |
| nbody                    | 154 ms                                                 | 92.3 ms: 1.66x faster                                                  |
| float                    | 117 ms                                                 | 71.4 ms: 1.64x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.57 ms: 1.64x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 2.66 us: 1.57x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.43 us: 1.53x faster                                                  |
| pyflate                  | 716 ms                                                 | 470 ms: 1.53x faster                                                   |
| pickle_pure_python       | 484 us                                                 | 318 us: 1.52x faster                                                   |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.52x faster                                                   |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.52x faster                                                   |
| django_template          | 48.2 ms                                                | 31.7 ms: 1.52x faster                                                  |
| logging_format           | 9.09 us                                                | 6.06 us: 1.50x faster                                                  |
| regex_compile            | 188 ms                                                 | 126 ms: 1.49x faster                                                   |
| genshi_text              | 31.8 ms                                                | 21.4 ms: 1.49x faster                                                  |
| coroutines               | 35.1 ms                                                | 23.7 ms: 1.48x faster                                                  |
| html5lib                 | 88.9 ms                                                | 61.3 ms: 1.45x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.46 sec: 1.44x faster                                                 |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 714 ms: 1.43x faster                                                   |
| mako                     | 16.3 ms                                                | 11.5 ms: 1.42x faster                                                  |
| thrift                   | 1.07 ms                                                | 759 us: 1.41x faster                                                   |
| sqlglot_normalize        | 143 ms                                                 | 103 ms: 1.39x faster                                                   |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.67 ms: 1.39x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 48.2 ms: 1.37x faster                                                  |
| 2to3                     | 348 ms                                                 | 254 ms: 1.37x faster                                                   |
| scimark_fft              | 466 ms                                                 | 343 ms: 1.36x faster                                                   |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.35x faster                                                 |
| unpack_sequence          | 60.0 ns                                                | 44.5 ns: 1.35x faster                                                  |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.5 ms: 1.34x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 59.4 ms: 1.33x faster                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 52.0 ms: 1.33x faster                                                  |
| sqlalchemy_declarative   | 172 ms                                                 | 130 ms: 1.32x faster                                                   |
| nqueens                  | 106 ms                                                 | 80.1 ms: 1.32x faster                                                  |
| sympy_sum                | 196 ms                                                 | 150 ms: 1.31x faster                                                   |
| fannkuch                 | 532 ms                                                 | 409 ms: 1.30x faster                                                   |
| sympy_integrate          | 25.8 ms                                                | 19.9 ms: 1.30x faster                                                  |
| sympy_str                | 346 ms                                                 | 268 ms: 1.29x faster                                                   |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.28x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.62 sec: 1.26x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 67.0 ms: 1.26x faster                                                  |
| sympy_expand             | 566 ms                                                 | 455 ms: 1.24x faster                                                   |
| json_dumps               | 14.2 ms                                                | 11.7 ms: 1.21x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 139 ms: 1.21x faster                                                   |
| xml_etree_iterparse      | 115 ms                                                 | 96.9 ms: 1.19x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 84.2 ms: 1.18x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.48 sec: 1.15x faster                                                 |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.14x faster                                                   |
| bench_thread_pool        | 986 us                                                 | 871 us: 1.13x faster                                                   |
| async_generators         | 444 ms                                                 | 392 ms: 1.13x faster                                                   |
| python_startup           | 14.6 ms                                                | 13.0 ms: 1.13x faster                                                  |
| json                     | 5.69 ms                                                | 5.13 ms: 1.11x faster                                                  |
| json_loads               | 31.2 us                                                | 28.4 us: 1.10x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 2.77 us: 1.09x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 25.7 ms: 1.08x faster                                                  |
| regex_effbot             | 3.63 ms                                                | 3.40 ms: 1.07x faster                                                  |
| regex_dna                | 227 ms                                                 | 214 ms: 1.06x faster                                                   |
| unpickle                 | 14.4 us                                                | 13.9 us: 1.03x faster                                                  |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                   |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                   |
| pickle_list              | 5.08 us                                                | 5.42 us: 1.07x slower                                                  |
| telco                    | 7.27 ms                                                | 7.84 ms: 1.08x slower                                                  |
| unpickle_list            | 5.20 us                                                | 5.77 us: 1.11x slower                                                  |
| coverage                 | 79.4 ms                                                | 91.1 ms: 1.15x slower                                                  |
| pickle                   | 10.7 us                                                | 12.6 us: 1.18x slower                                                  |
| pickle_dict              | 29.6 us                                                | 35.3 us: 1.19x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 7.09 ms: 1.20x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 4.58 ms: 1.26x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.45 ms: 1.51x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 82.5 ms: 3.43x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.39x faster                                                           |
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, tornado_http
Ignored benchmarks (11) of results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.447x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.27x