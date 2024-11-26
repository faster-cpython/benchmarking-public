# Results vs. 3.10.4

- fork: python
- ref: v3.13.0
- machine: linux-x86_64
- commit hash: 60403a5
- commit date: 2024-10-07
- overall geometric mean: 1.384x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: 1.23x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 267 ms: 1.31x faster                                   |
| chameleon      | 9.68 ms                                                | 6.94 ms: 1.40x faster                                  |
| docutils       | 3.30 sec                                               | 2.59 sec: 1.27x faster                                 |
| html5lib       | 88.9 ms                                                | 64.2 ms: 1.38x faster                                  |
| tornado_http   | 136 ms                                                 | 92.4 ms: 1.48x faster                                  |
| Geometric mean | (ref)                                                  | 1.36x faster                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 842 ms: 2.10x faster                                   |
| async_tree_none         | 728 ms                                                 | 351 ms: 2.08x faster                                   |
| async_tree_memoization  | 870 ms                                                 | 442 ms: 1.97x faster                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 577 ms: 1.76x faster                                   |
| Geometric mean          | (ref)                                                  | 1.97x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 154 ms                                                 | 87.0 ms: 1.77x faster                                  |
| float          | 117 ms                                                 | 79.2 ms: 1.48x faster                                  |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                   |
| Geometric mean | (ref)                                                  | 1.39x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 132 ms: 1.43x faster                                   |
| regex_v8       | 27.8 ms                                                | 26.2 ms: 1.06x faster                                  |
| regex_dna      | 227 ms                                                 | 218 ms: 1.04x faster                                   |
| regex_effbot   | 3.63 ms                                                | 3.73 ms: 1.03x slower                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 310 us: 1.56x faster                                   |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                   |
| tomli_loads          | 3.14 sec                                               | 2.14 sec: 1.47x faster                                 |
| json_dumps           | 14.2 ms                                                | 10.6 ms: 1.34x faster                                  |
| xml_etree_process    | 79.1 ms                                                | 60.6 ms: 1.30x faster                                  |
| json_loads           | 31.2 us                                                | 27.2 us: 1.15x faster                                  |
| xml_etree_generate   | 99.4 ms                                                | 86.7 ms: 1.15x faster                                  |
| xml_etree_iterparse  | 115 ms                                                 | 101 ms: 1.14x faster                                   |
| xml_etree_parse      | 168 ms                                                 | 156 ms: 1.08x faster                                   |
| Geometric mean       | (ref)                                                  | 1.29x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.5 ms: 1.17x faster                                  |
| python_startup_no_site | 5.93 ms                                                | 6.96 ms: 1.17x slower                                  |
| Geometric mean         | (ref)                                                  | 1.00x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.1 ms: 1.47x faster                                  |
| django_template | 48.2 ms                                                | 35.2 ms: 1.37x faster                                  |
| genshi_text     | 31.8 ms                                                | 23.5 ms: 1.35x faster                                  |
| genshi_xml      | 66.0 ms                                                | 50.9 ms: 1.30x faster                                  |
| Geometric mean  | (ref)                                                  | 1.37x faster                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 165 us: 3.30x faster                                   |
| generators               | 80.1 ms                                                | 29.0 ms: 2.77x faster                                  |
| deltablue                | 7.91 ms                                                | 3.23 ms: 2.45x faster                                  |
| async_tree_io            | 1.77 sec                                               | 842 ms: 2.10x faster                                   |
| async_tree_none          | 728 ms                                                 | 351 ms: 2.08x faster                                   |
| chaos                    | 115 ms                                                 | 58.1 ms: 1.99x faster                                  |
| async_tree_memoization   | 870 ms                                                 | 442 ms: 1.97x faster                                   |
| raytrace                 | 507 ms                                                 | 267 ms: 1.90x faster                                   |
| logging_silent           | 190 ns                                                 | 102 ns: 1.86x faster                                   |
| scimark_sor              | 220 ms                                                 | 124 ms: 1.78x faster                                   |
| nbody                    | 154 ms                                                 | 87.0 ms: 1.77x faster                                  |
| pylint                   | 551 ms                                                 | 313 ms: 1.76x faster                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 577 ms: 1.76x faster                                   |
| scimark_monte_carlo      | 118 ms                                                 | 67.4 ms: 1.75x faster                                  |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                  |
| richards_super           | 94.7 ms                                                | 54.9 ms: 1.73x faster                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.27 ms: 1.70x faster                                  |
| crypto_pyaes             | 128 ms                                                 | 75.3 ms: 1.70x faster                                  |
| hexiom                   | 10.4 ms                                                | 6.16 ms: 1.69x faster                                  |
| go                       | 240 ms                                                 | 144 ms: 1.67x faster                                   |
| richards                 | 79.3 ms                                                | 48.7 ms: 1.63x faster                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.58 ms: 1.62x faster                                  |
| scimark_lu               | 176 ms                                                 | 113 ms: 1.56x faster                                   |
| pickle_pure_python       | 484 us                                                 | 310 us: 1.56x faster                                   |
| coroutines               | 35.1 ms                                                | 22.7 ms: 1.55x faster                                  |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                   |
| pyflate                  | 716 ms                                                 | 471 ms: 1.52x faster                                   |
| deepcopy_memo            | 58.5 us                                                | 39.1 us: 1.50x faster                                  |
| float                    | 117 ms                                                 | 79.2 ms: 1.48x faster                                  |
| tornado_http             | 136 ms                                                 | 92.4 ms: 1.48x faster                                  |
| spectral_norm            | 170 ms                                                 | 115 ms: 1.47x faster                                   |
| mako                     | 16.3 ms                                                | 11.1 ms: 1.47x faster                                  |
| tomli_loads              | 3.14 sec                                               | 2.14 sec: 1.47x faster                                 |
| logging_simple           | 8.30 us                                                | 5.72 us: 1.45x faster                                  |
| regex_compile            | 188 ms                                                 | 132 ms: 1.43x faster                                   |
| logging_format           | 9.09 us                                                | 6.40 us: 1.42x faster                                  |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.41x faster                                 |
| pprint_safe_repr         | 1.02 sec                                               | 728 ms: 1.40x faster                                   |
| chameleon                | 9.68 ms                                                | 6.94 ms: 1.40x faster                                  |
| html5lib                 | 88.9 ms                                                | 64.2 ms: 1.38x faster                                  |
| django_template          | 48.2 ms                                                | 35.2 ms: 1.37x faster                                  |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.1 ms: 1.37x faster                                  |
| genshi_text              | 31.8 ms                                                | 23.5 ms: 1.35x faster                                  |
| nqueens                  | 106 ms                                                 | 78.4 ms: 1.35x faster                                  |
| json_dumps               | 14.2 ms                                                | 10.6 ms: 1.34x faster                                  |
| deepcopy                 | 479 us                                                 | 358 us: 1.34x faster                                   |
| sqlglot_normalize        | 143 ms                                                 | 108 ms: 1.33x faster                                   |
| thrift                   | 1.07 ms                                                | 809 us: 1.32x faster                                   |
| fannkuch                 | 532 ms                                                 | 404 ms: 1.31x faster                                   |
| pycparser                | 1.58 sec                                               | 1.20 sec: 1.31x faster                                 |
| dulwich_log              | 84.3 ms                                                | 64.3 ms: 1.31x faster                                  |
| 2to3                     | 348 ms                                                 | 267 ms: 1.31x faster                                   |
| sympy_sum                | 196 ms                                                 | 150 ms: 1.31x faster                                   |
| xml_etree_process        | 79.1 ms                                                | 60.6 ms: 1.30x faster                                  |
| deepcopy_reduce          | 4.17 us                                                | 3.20 us: 1.30x faster                                  |
| genshi_xml               | 66.0 ms                                                | 50.9 ms: 1.30x faster                                  |
| sympy_integrate          | 25.8 ms                                                | 19.9 ms: 1.30x faster                                  |
| sqlalchemy_declarative   | 172 ms                                                 | 133 ms: 1.29x faster                                   |
| sqlglot_optimize         | 69.2 ms                                                | 53.7 ms: 1.29x faster                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.04 ms: 1.28x faster                                  |
| scimark_fft              | 466 ms                                                 | 364 ms: 1.28x faster                                   |
| docutils                 | 3.30 sec                                               | 2.59 sec: 1.27x faster                                 |
| sympy_str                | 346 ms                                                 | 275 ms: 1.26x faster                                   |
| sympy_expand             | 566 ms                                                 | 463 ms: 1.22x faster                                   |
| bench_thread_pool        | 986 us                                                 | 822 us: 1.20x faster                                   |
| python_startup           | 14.6 ms                                                | 12.5 ms: 1.17x faster                                  |
| pathlib                  | 20.5 ms                                                | 17.5 ms: 1.17x faster                                  |
| json_loads               | 31.2 us                                                | 27.2 us: 1.15x faster                                  |
| xml_etree_generate       | 99.4 ms                                                | 86.7 ms: 1.15x faster                                  |
| xml_etree_iterparse      | 115 ms                                                 | 101 ms: 1.14x faster                                   |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                   |
| xml_etree_parse          | 168 ms                                                 | 156 ms: 1.08x faster                                   |
| json                     | 5.69 ms                                                | 5.36 ms: 1.06x faster                                  |
| regex_v8                 | 27.8 ms                                                | 26.2 ms: 1.06x faster                                  |
| mdp                      | 2.85 sec                                               | 2.72 sec: 1.05x faster                                 |
| regex_dna                | 227 ms                                                 | 218 ms: 1.04x faster                                   |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                   |
| async_generators         | 444 ms                                                 | 436 ms: 1.02x faster                                   |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                   |
| regex_effbot             | 3.63 ms                                                | 3.73 ms: 1.03x slower                                  |
| coverage                 | 79.4 ms                                                | 84.0 ms: 1.06x slower                                  |
| mypy2                    | 894 ms                                                 | 1.04 sec: 1.17x slower                                 |
| python_startup_no_site   | 5.93 ms                                                | 6.96 ms: 1.17x slower                                  |
| telco                    | 7.27 ms                                                | 8.54 ms: 1.18x slower                                  |
| gc_traversal             | 3.62 ms                                                | 4.37 ms: 1.21x slower                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.41 ms: 1.49x slower                                  |
| Geometric mean           | (ref)                                                  | 1.38x faster                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, djangocms, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, gevent_hub, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.384x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: 1.23x