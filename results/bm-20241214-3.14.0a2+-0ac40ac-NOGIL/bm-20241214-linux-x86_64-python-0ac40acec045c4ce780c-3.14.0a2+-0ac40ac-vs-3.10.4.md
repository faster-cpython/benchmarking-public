# Results vs. 3.10.4

- fork: python
- ref: 0ac40acec045c4ce780c
- machine: linux-x86_64
- commit hash: 0ac40ac
- commit date: 2024-12-14
- overall geometric mean: 1.077x faster
- HPT reliability: 99.91%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.49x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 353 ms: 1.01x slower                                                   |
| docutils       | 3.30 sec                                               | 3.01 sec: 1.10x faster                                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 782 ms: 2.26x faster                                                   |
| async_tree_none         | 728 ms                                                 | 368 ms: 1.98x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 464 ms: 1.88x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 619 ms: 1.64x faster                                                   |
| Geometric mean          | (ref)                                                  | 1.93x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 139 ms: 1.10x faster                                                   |
| pidigits       | 191 ms                                                 | 191 ms: 1.00x slower                                                   |
| float          | 117 ms                                                 | 129 ms: 1.10x slower                                                   |
| Geometric mean | (ref)                                                  | 1.00x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 170 ms: 1.11x faster                                                   |
| regex_v8       | 27.8 ms                                                | 25.7 ms: 1.08x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.51 ms: 1.04x faster                                                  |
| regex_dna      | 227 ms                                                 | 224 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.62 sec: 1.20x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 96.5 ms: 1.20x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.13x faster                                                   |
| json_dumps           | 14.2 ms                                                | 13.4 ms: 1.06x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 75.0 ms: 1.05x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 316 us: 1.05x faster                                                   |
| json_loads           | 31.2 us                                                | 30.1 us: 1.04x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 96.9 ms: 1.03x faster                                                  |
| pickle_pure_python   | 484 us                                                 | 479 us: 1.01x faster                                                   |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 16.1 ms: 1.10x slower                                                  |
| python_startup_no_site | 5.93 ms                                                | 9.81 ms: 1.65x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.35x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 30.5 ms: 1.04x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 64.3 ms: 1.03x faster                                                  |
| django_template | 48.2 ms                                                | 47.1 ms: 1.02x faster                                                  |
| mako            | 16.3 ms                                                | 18.0 ms: 1.10x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 209 us: 2.60x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 782 ms: 2.26x faster                                                   |
| generators               | 80.1 ms                                                | 36.2 ms: 2.21x faster                                                  |
| async_tree_none          | 728 ms                                                 | 368 ms: 1.98x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 464 ms: 1.88x faster                                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 619 ms: 1.64x faster                                                   |
| pylint                   | 551 ms                                                 | 353 ms: 1.56x faster                                                   |
| deepcopy                 | 479 us                                                 | 316 us: 1.52x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 40.6 us: 1.44x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 92.9 ms: 1.38x faster                                                  |
| spectral_norm            | 170 ms                                                 | 124 ms: 1.37x faster                                                   |
| coroutines               | 35.1 ms                                                | 26.8 ms: 1.31x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 3.46 us: 1.20x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 2.62 sec: 1.20x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 96.5 ms: 1.20x faster                                                  |
| richards_super           | 94.7 ms                                                | 80.0 ms: 1.18x faster                                                  |
| chaos                    | 115 ms                                                 | 98.7 ms: 1.17x faster                                                  |
| pathlib                  | 20.5 ms                                                | 17.5 ms: 1.17x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.13x faster                                                   |
| comprehensions           | 28.8 us                                                | 25.7 us: 1.12x faster                                                  |
| scimark_fft              | 466 ms                                                 | 416 ms: 1.12x faster                                                   |
| regex_compile            | 188 ms                                                 | 170 ms: 1.11x faster                                                   |
| nbody                    | 154 ms                                                 | 139 ms: 1.10x faster                                                   |
| sqlglot_normalize        | 143 ms                                                 | 130 ms: 1.10x faster                                                   |
| docutils                 | 3.30 sec                                               | 3.01 sec: 1.10x faster                                                 |
| pyflate                  | 716 ms                                                 | 655 ms: 1.09x faster                                                   |
| pycparser                | 1.58 sec                                               | 1.45 sec: 1.09x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 25.7 ms: 1.08x faster                                                  |
| nqueens                  | 106 ms                                                 | 98.2 ms: 1.08x faster                                                  |
| richards                 | 79.3 ms                                                | 74.0 ms: 1.07x faster                                                  |
| logging_silent           | 190 ns                                                 | 178 ns: 1.07x faster                                                   |
| sqlite_synth             | 3.02 us                                                | 2.84 us: 1.06x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 79.5 ms: 1.06x faster                                                  |
| hexiom                   | 10.4 ms                                                | 9.82 ms: 1.06x faster                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 65.5 ms: 1.06x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 6.12 ms: 1.06x faster                                                  |
| json_dumps               | 14.2 ms                                                | 13.4 ms: 1.06x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 75.0 ms: 1.05x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 316 us: 1.05x faster                                                   |
| json                     | 5.69 ms                                                | 5.44 ms: 1.05x faster                                                  |
| deltablue                | 7.91 ms                                                | 7.57 ms: 1.05x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 113 ms: 1.05x faster                                                   |
| genshi_text              | 31.8 ms                                                | 30.5 ms: 1.04x faster                                                  |
| json_loads               | 31.2 us                                                | 30.1 us: 1.04x faster                                                  |
| regex_effbot             | 3.63 ms                                                | 3.51 ms: 1.04x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 64.3 ms: 1.03x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 96.9 ms: 1.03x faster                                                  |
| django_template          | 48.2 ms                                                | 47.1 ms: 1.02x faster                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 1000 ms: 1.02x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 2.07 sec: 1.02x faster                                                 |
| fannkuch                 | 532 ms                                                 | 524 ms: 1.01x faster                                                   |
| pickle_pure_python       | 484 us                                                 | 479 us: 1.01x faster                                                   |
| regex_dna                | 227 ms                                                 | 224 ms: 1.01x faster                                                   |
| raytrace                 | 507 ms                                                 | 502 ms: 1.01x faster                                                   |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                   |
| pidigits                 | 191 ms                                                 | 191 ms: 1.00x slower                                                   |
| gc_traversal             | 3.62 ms                                                | 3.65 ms: 1.01x slower                                                  |
| 2to3                     | 348 ms                                                 | 353 ms: 1.01x slower                                                   |
| thrift                   | 1.07 ms                                                | 1.09 ms: 1.01x slower                                                  |
| sympy_integrate          | 25.8 ms                                                | 26.2 ms: 1.01x slower                                                  |
| scimark_sor              | 220 ms                                                 | 226 ms: 1.03x slower                                                   |
| logging_simple           | 8.30 us                                                | 8.55 us: 1.03x slower                                                  |
| logging_format           | 9.09 us                                                | 9.52 us: 1.05x slower                                                  |
| sqlalchemy_imperative    | 23.3 ms                                                | 24.5 ms: 1.05x slower                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 2.76 ms: 1.07x slower                                                  |
| mdp                      | 2.85 sec                                               | 3.05 sec: 1.07x slower                                                 |
| meteor_contest           | 120 ms                                                 | 130 ms: 1.08x slower                                                   |
| sympy_str                | 346 ms                                                 | 376 ms: 1.09x slower                                                   |
| float                    | 117 ms                                                 | 129 ms: 1.10x slower                                                   |
| sqlalchemy_declarative   | 172 ms                                                 | 190 ms: 1.10x slower                                                   |
| mako                     | 16.3 ms                                                | 18.0 ms: 1.10x slower                                                  |
| python_startup           | 14.6 ms                                                | 16.1 ms: 1.10x slower                                                  |
| sqlglot_parse            | 2.17 ms                                                | 2.39 ms: 1.10x slower                                                  |
| async_generators         | 444 ms                                                 | 501 ms: 1.13x slower                                                   |
| sympy_sum                | 196 ms                                                 | 235 ms: 1.20x slower                                                   |
| sympy_expand             | 566 ms                                                 | 682 ms: 1.21x slower                                                   |
| telco                    | 7.27 ms                                                | 9.21 ms: 1.27x slower                                                  |
| coverage                 | 79.4 ms                                                | 109 ms: 1.37x slower                                                   |
| create_gc_cycles         | 1.62 ms                                                | 2.31 ms: 1.43x slower                                                  |
| mypy2                    | 894 ms                                                 | 1.28 sec: 1.43x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 9.81 ms: 1.65x slower                                                  |
| bench_thread_pool        | 986 us                                                 | 3.57 ms: 3.62x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 102 ms: 4.23x slower                                                   |
| Geometric mean           | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (3): scimark_lu, go, html5lib
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241214-3.14.0a2+-0ac40ac-NOGIL/bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.077x faster

# HPT report

- Reliability score: 99.91% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.49x