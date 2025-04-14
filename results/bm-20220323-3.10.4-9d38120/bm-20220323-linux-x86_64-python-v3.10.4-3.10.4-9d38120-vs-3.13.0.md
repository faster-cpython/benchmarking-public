# Results vs. 3.13.0

- fork: python
- ref: v3.10.4
- machine: linux-x86_64
- commit hash: 9d38120
- commit date: 2022-03-23
- overall geometric mean: 1.275x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x slower
- Memory change: 0.83x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 348 ms: 1.31x slower                                   |
| chameleon      | 6.94 ms                                                | 9.68 ms: 1.40x slower                                  |
| docutils       | 2.59 sec                                               | 3.30 sec: 1.27x slower                                 |
| html5lib       | 64.2 ms                                                | 88.9 ms: 1.38x slower                                  |
| tornado_http   | 92.4 ms                                                | 136 ms: 1.48x slower                                   |
| Geometric mean | (ref)                                                  | 1.36x slower                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| asyncio_websockets      | 552 ms                                                 | 559 ms: 1.01x slower                                   |
| async_generators        | 436 ms                                                 | 444 ms: 1.02x slower                                   |
| coroutines              | 22.7 ms                                                | 35.1 ms: 1.55x slower                                  |
| async_tree_cpu_io_mixed | 577 ms                                                 | 1.02 sec: 1.76x slower                                 |
| async_tree_memoization  | 442 ms                                                 | 870 ms: 1.97x slower                                   |
| async_tree_none         | 351 ms                                                 | 728 ms: 2.08x slower                                   |
| async_tree_io           | 842 ms                                                 | 1.77 sec: 2.10x slower                                 |
| Geometric mean          | (ref)                                                  | 1.58x slower                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 191 ms: 1.02x slower                                   |
| float          | 79.2 ms                                                | 117 ms: 1.48x slower                                   |
| nbody          | 87.0 ms                                                | 154 ms: 1.77x slower                                   |
| Geometric mean | (ref)                                                  | 1.39x slower                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.73 ms                                                | 3.63 ms: 1.03x faster                                  |
| regex_dna      | 218 ms                                                 | 227 ms: 1.04x slower                                   |
| regex_v8       | 26.2 ms                                                | 27.8 ms: 1.06x slower                                  |
| regex_compile  | 132 ms                                                 | 188 ms: 1.43x slower                                   |
| Geometric mean | (ref)                                                  | 1.11x slower                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| xml_etree_parse      | 156 ms                                                 | 168 ms: 1.08x slower                                   |
| xml_etree_iterparse  | 101 ms                                                 | 115 ms: 1.14x slower                                   |
| xml_etree_generate   | 86.7 ms                                                | 99.4 ms: 1.15x slower                                  |
| json_loads           | 27.2 us                                                | 31.2 us: 1.15x slower                                  |
| xml_etree_process    | 60.6 ms                                                | 79.1 ms: 1.30x slower                                  |
| json_dumps           | 10.6 ms                                                | 14.2 ms: 1.34x slower                                  |
| tomli_loads          | 2.14 sec                                               | 3.14 sec: 1.47x slower                                 |
| unpickle_pure_python | 216 us                                                 | 331 us: 1.53x slower                                   |
| pickle_pure_python   | 310 us                                                 | 484 us: 1.56x slower                                   |
| Geometric mean       | (ref)                                                  | 1.29x slower                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                | 5.93 ms: 1.17x faster                                  |
| python_startup         | 12.5 ms                                                | 14.6 ms: 1.17x slower                                  |
| Geometric mean         | (ref)                                                  | 1.00x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml      | 50.9 ms                                                | 66.0 ms: 1.30x slower                                  |
| genshi_text     | 23.5 ms                                                | 31.8 ms: 1.35x slower                                  |
| django_template | 35.2 ms                                                | 48.2 ms: 1.37x slower                                  |
| mako            | 11.1 ms                                                | 16.3 ms: 1.47x slower                                  |
| Geometric mean  | (ref)                                                  | 1.37x slower                                           |

All benchmarks:
===============

| Benchmark                | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| create_gc_cycles         | 2.41 ms                                                | 1.62 ms: 1.49x faster                                  |
| gc_traversal             | 4.37 ms                                                | 3.62 ms: 1.21x faster                                  |
| telco                    | 8.54 ms                                                | 7.27 ms: 1.18x faster                                  |
| python_startup_no_site   | 6.96 ms                                                | 5.93 ms: 1.17x faster                                  |
| mypy2                    | 1.04 sec                                               | 894 ms: 1.17x faster                                   |
| coverage                 | 84.0 ms                                                | 79.4 ms: 1.06x faster                                  |
| regex_effbot             | 3.73 ms                                                | 3.63 ms: 1.03x faster                                  |
| asyncio_websockets       | 552 ms                                                 | 559 ms: 1.01x slower                                   |
| async_generators         | 436 ms                                                 | 444 ms: 1.02x slower                                   |
| pidigits                 | 186 ms                                                 | 191 ms: 1.02x slower                                   |
| regex_dna                | 218 ms                                                 | 227 ms: 1.04x slower                                   |
| mdp                      | 2.72 sec                                               | 2.85 sec: 1.05x slower                                 |
| regex_v8                 | 26.2 ms                                                | 27.8 ms: 1.06x slower                                  |
| json                     | 5.36 ms                                                | 5.69 ms: 1.06x slower                                  |
| xml_etree_parse          | 156 ms                                                 | 168 ms: 1.08x slower                                   |
| meteor_contest           | 109 ms                                                 | 120 ms: 1.10x slower                                   |
| xml_etree_iterparse      | 101 ms                                                 | 115 ms: 1.14x slower                                   |
| xml_etree_generate       | 86.7 ms                                                | 99.4 ms: 1.15x slower                                  |
| json_loads               | 27.2 us                                                | 31.2 us: 1.15x slower                                  |
| pathlib                  | 17.5 ms                                                | 20.5 ms: 1.17x slower                                  |
| python_startup           | 12.5 ms                                                | 14.6 ms: 1.17x slower                                  |
| bench_thread_pool        | 822 us                                                 | 986 us: 1.20x slower                                   |
| sympy_expand             | 463 ms                                                 | 566 ms: 1.22x slower                                   |
| sympy_str                | 275 ms                                                 | 346 ms: 1.26x slower                                   |
| docutils                 | 2.59 sec                                               | 3.30 sec: 1.27x slower                                 |
| scimark_fft              | 364 ms                                                 | 466 ms: 1.28x slower                                   |
| scimark_sparse_mat_mult  | 5.04 ms                                                | 6.47 ms: 1.28x slower                                  |
| sqlglot_optimize         | 53.7 ms                                                | 69.2 ms: 1.29x slower                                  |
| sqlalchemy_declarative   | 133 ms                                                 | 172 ms: 1.29x slower                                   |
| sympy_integrate          | 19.9 ms                                                | 25.8 ms: 1.30x slower                                  |
| genshi_xml               | 50.9 ms                                                | 66.0 ms: 1.30x slower                                  |
| deepcopy_reduce          | 3.20 us                                                | 4.17 us: 1.30x slower                                  |
| xml_etree_process        | 60.6 ms                                                | 79.1 ms: 1.30x slower                                  |
| sympy_sum                | 150 ms                                                 | 196 ms: 1.31x slower                                   |
| 2to3                     | 267 ms                                                 | 348 ms: 1.31x slower                                   |
| dulwich_log              | 64.3 ms                                                | 84.3 ms: 1.31x slower                                  |
| pycparser                | 1.20 sec                                               | 1.58 sec: 1.31x slower                                 |
| fannkuch                 | 404 ms                                                 | 532 ms: 1.31x slower                                   |
| thrift                   | 809 us                                                 | 1.07 ms: 1.32x slower                                  |
| sqlglot_normalize        | 108 ms                                                 | 143 ms: 1.33x slower                                   |
| deepcopy                 | 358 us                                                 | 479 us: 1.34x slower                                   |
| json_dumps               | 10.6 ms                                                | 14.2 ms: 1.34x slower                                  |
| nqueens                  | 78.4 ms                                                | 106 ms: 1.35x slower                                   |
| genshi_text              | 23.5 ms                                                | 31.8 ms: 1.35x slower                                  |
| sqlalchemy_imperative    | 17.1 ms                                                | 23.3 ms: 1.37x slower                                  |
| django_template          | 35.2 ms                                                | 48.2 ms: 1.37x slower                                  |
| html5lib                 | 64.2 ms                                                | 88.9 ms: 1.38x slower                                  |
| chameleon                | 6.94 ms                                                | 9.68 ms: 1.40x slower                                  |
| pprint_safe_repr         | 728 ms                                                 | 1.02 sec: 1.40x slower                                 |
| pprint_pformat           | 1.49 sec                                               | 2.10 sec: 1.41x slower                                 |
| logging_format           | 6.40 us                                                | 9.09 us: 1.42x slower                                  |
| regex_compile            | 132 ms                                                 | 188 ms: 1.43x slower                                   |
| logging_simple           | 5.72 us                                                | 8.30 us: 1.45x slower                                  |
| tomli_loads              | 2.14 sec                                               | 3.14 sec: 1.47x slower                                 |
| mako                     | 11.1 ms                                                | 16.3 ms: 1.47x slower                                  |
| spectral_norm            | 115 ms                                                 | 170 ms: 1.47x slower                                   |
| tornado_http             | 92.4 ms                                                | 136 ms: 1.48x slower                                   |
| float                    | 79.2 ms                                                | 117 ms: 1.48x slower                                   |
| deepcopy_memo            | 39.1 us                                                | 58.5 us: 1.50x slower                                  |
| pyflate                  | 471 ms                                                 | 716 ms: 1.52x slower                                   |
| unpickle_pure_python     | 216 us                                                 | 331 us: 1.53x slower                                   |
| coroutines               | 22.7 ms                                                | 35.1 ms: 1.55x slower                                  |
| pickle_pure_python       | 310 us                                                 | 484 us: 1.56x slower                                   |
| scimark_lu               | 113 ms                                                 | 176 ms: 1.56x slower                                   |
| sqlglot_transpile        | 1.58 ms                                                | 2.57 ms: 1.62x slower                                  |
| richards                 | 48.7 ms                                                | 79.3 ms: 1.63x slower                                  |
| go                       | 144 ms                                                 | 240 ms: 1.67x slower                                   |
| hexiom                   | 6.16 ms                                                | 10.4 ms: 1.69x slower                                  |
| crypto_pyaes             | 75.3 ms                                                | 128 ms: 1.70x slower                                   |
| sqlglot_parse            | 1.27 ms                                                | 2.17 ms: 1.70x slower                                  |
| richards_super           | 54.9 ms                                                | 94.7 ms: 1.73x slower                                  |
| comprehensions           | 16.5 us                                                | 28.8 us: 1.74x slower                                  |
| scimark_monte_carlo      | 67.4 ms                                                | 118 ms: 1.75x slower                                   |
| async_tree_cpu_io_mixed  | 577 ms                                                 | 1.02 sec: 1.76x slower                                 |
| pylint                   | 313 ms                                                 | 551 ms: 1.76x slower                                   |
| nbody                    | 87.0 ms                                                | 154 ms: 1.77x slower                                   |
| scimark_sor              | 124 ms                                                 | 220 ms: 1.78x slower                                   |
| logging_silent           | 102 ns                                                 | 190 ns: 1.86x slower                                   |
| raytrace                 | 267 ms                                                 | 507 ms: 1.90x slower                                   |
| async_tree_memoization   | 442 ms                                                 | 870 ms: 1.97x slower                                   |
| chaos                    | 58.1 ms                                                | 115 ms: 1.99x slower                                   |
| async_tree_none          | 351 ms                                                 | 728 ms: 2.08x slower                                   |
| async_tree_io            | 842 ms                                                 | 1.77 sec: 2.10x slower                                 |
| deltablue                | 3.23 ms                                                | 7.91 ms: 2.45x slower                                  |
| generators               | 29.0 ms                                                | 80.1 ms: 2.77x slower                                  |
| typing_runtime_protocols | 165 us                                                 | 544 us: 3.30x slower                                   |
| Geometric mean           | (ref)                                                  | 1.38x slower                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, gevent_hub, k_core, shortest_path, sphinx
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, djangocms, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.275x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.31x
- 95% likely to have a slowdown of 1.30x
- 99% likely to have a slowdown of 1.29x

# Memory
- memory change: 0.83x