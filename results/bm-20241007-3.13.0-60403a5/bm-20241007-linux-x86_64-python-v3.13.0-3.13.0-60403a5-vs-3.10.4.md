# Results vs. 3.10.4

- fork: python
- ref: v3.13.0
- machine: linux-x86_64
- commit hash: 60403a5
- commit date: 2024-10-07
- overall geometric mean: 1.397x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.23x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 266 ms: 1.31x faster                                   |
| chameleon      | 9.68 ms                                                | 6.81 ms: 1.42x faster                                  |
| docutils       | 3.30 sec                                               | 2.58 sec: 1.27x faster                                 |
| html5lib       | 88.9 ms                                                | 63.4 ms: 1.40x faster                                  |
| tornado_http   | 136 ms                                                 | 91.2 ms: 1.49x faster                                  |
| Geometric mean | (ref)                                                  | 1.38x faster                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 838 ms: 2.11x faster                                   |
| async_tree_none         | 728 ms                                                 | 350 ms: 2.08x faster                                   |
| async_tree_memoization  | 870 ms                                                 | 437 ms: 1.99x faster                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 573 ms: 1.77x faster                                   |
| Geometric mean          | (ref)                                                  | 1.98x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 154 ms                                                 | 87.7 ms: 1.75x faster                                  |
| float          | 117 ms                                                 | 78.7 ms: 1.49x faster                                  |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                   |
| Geometric mean | (ref)                                                  | 1.39x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 132 ms: 1.43x faster                                   |
| regex_v8       | 27.8 ms                                                | 26.9 ms: 1.03x faster                                  |
| regex_dna      | 227 ms                                                 | 220 ms: 1.03x faster                                   |
| regex_effbot   | 3.63 ms                                                | 3.77 ms: 1.04x slower                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 302 us: 1.60x faster                                   |
| unpickle_pure_python | 331 us                                                 | 213 us: 1.55x faster                                   |
| tomli_loads          | 3.14 sec                                               | 2.12 sec: 1.48x faster                                 |
| json_dumps           | 14.2 ms                                                | 10.1 ms: 1.40x faster                                  |
| xml_etree_process    | 79.1 ms                                                | 60.5 ms: 1.31x faster                                  |
| json_loads           | 31.2 us                                                | 27.2 us: 1.15x faster                                  |
| xml_etree_generate   | 99.4 ms                                                | 86.8 ms: 1.14x faster                                  |
| xml_etree_iterparse  | 115 ms                                                 | 101 ms: 1.14x faster                                   |
| xml_etree_parse      | 168 ms                                                 | 154 ms: 1.09x faster                                   |
| Geometric mean       | (ref)                                                  | 1.31x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.7 ms: 1.15x faster                                  |
| python_startup_no_site | 5.93 ms                                                | 7.00 ms: 1.18x slower                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.7 ms: 1.53x faster                                  |
| django_template | 48.2 ms                                                | 31.7 ms: 1.52x faster                                  |
| genshi_text     | 31.8 ms                                                | 22.6 ms: 1.41x faster                                  |
| genshi_xml      | 66.0 ms                                                | 50.5 ms: 1.31x faster                                  |
| Geometric mean  | (ref)                                                  | 1.44x faster                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 160 us: 3.40x faster                                   |
| generators               | 80.1 ms                                                | 28.8 ms: 2.78x faster                                  |
| deltablue                | 7.91 ms                                                | 3.19 ms: 2.48x faster                                  |
| async_tree_io            | 1.77 sec                                               | 838 ms: 2.11x faster                                   |
| async_tree_none          | 728 ms                                                 | 350 ms: 2.08x faster                                   |
| async_tree_memoization   | 870 ms                                                 | 437 ms: 1.99x faster                                   |
| chaos                    | 115 ms                                                 | 58.0 ms: 1.99x faster                                  |
| raytrace                 | 507 ms                                                 | 262 ms: 1.94x faster                                   |
| logging_silent           | 190 ns                                                 | 101 ns: 1.88x faster                                   |
| scimark_sor              | 220 ms                                                 | 122 ms: 1.80x faster                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 573 ms: 1.77x faster                                   |
| scimark_monte_carlo      | 118 ms                                                 | 66.8 ms: 1.77x faster                                  |
| pylint                   | 551 ms                                                 | 312 ms: 1.77x faster                                   |
| richards_super           | 94.7 ms                                                | 53.7 ms: 1.76x faster                                  |
| nbody                    | 154 ms                                                 | 87.7 ms: 1.75x faster                                  |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                  |
| djangocms                | 38.4 us                                                | 22.3 us: 1.72x faster                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.26 ms: 1.71x faster                                  |
| crypto_pyaes             | 128 ms                                                 | 74.7 ms: 1.71x faster                                  |
| hexiom                   | 10.4 ms                                                | 6.08 ms: 1.71x faster                                  |
| go                       | 240 ms                                                 | 141 ms: 1.71x faster                                   |
| richards                 | 79.3 ms                                                | 47.5 ms: 1.67x faster                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.57 ms: 1.64x faster                                  |
| pickle_pure_python       | 484 us                                                 | 302 us: 1.60x faster                                   |
| coroutines               | 35.1 ms                                                | 22.2 ms: 1.58x faster                                  |
| unpickle_pure_python     | 331 us                                                 | 213 us: 1.55x faster                                   |
| scimark_lu               | 176 ms                                                 | 114 ms: 1.54x faster                                   |
| mako                     | 16.3 ms                                                | 10.7 ms: 1.53x faster                                  |
| pyflate                  | 716 ms                                                 | 470 ms: 1.53x faster                                   |
| deepcopy_memo            | 58.5 us                                                | 38.4 us: 1.52x faster                                  |
| django_template          | 48.2 ms                                                | 31.7 ms: 1.52x faster                                  |
| spectral_norm            | 170 ms                                                 | 113 ms: 1.50x faster                                   |
| tornado_http             | 136 ms                                                 | 91.2 ms: 1.49x faster                                  |
| float                    | 117 ms                                                 | 78.7 ms: 1.49x faster                                  |
| tomli_loads              | 3.14 sec                                               | 2.12 sec: 1.48x faster                                 |
| logging_simple           | 8.30 us                                                | 5.65 us: 1.47x faster                                  |
| logging_format           | 9.09 us                                                | 6.23 us: 1.46x faster                                  |
| regex_compile            | 188 ms                                                 | 132 ms: 1.43x faster                                   |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                 |
| chameleon                | 9.68 ms                                                | 6.81 ms: 1.42x faster                                  |
| genshi_text              | 31.8 ms                                                | 22.6 ms: 1.41x faster                                  |
| html5lib                 | 88.9 ms                                                | 63.4 ms: 1.40x faster                                  |
| json_dumps               | 14.2 ms                                                | 10.1 ms: 1.40x faster                                  |
| pprint_safe_repr         | 1.02 sec                                               | 727 ms: 1.40x faster                                   |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.9 ms: 1.38x faster                                  |
| deepcopy                 | 479 us                                                 | 354 us: 1.35x faster                                   |
| fannkuch                 | 532 ms                                                 | 394 ms: 1.35x faster                                   |
| thrift                   | 1.07 ms                                                | 800 us: 1.34x faster                                   |
| sqlglot_normalize        | 143 ms                                                 | 108 ms: 1.32x faster                                   |
| pycparser                | 1.58 sec                                               | 1.20 sec: 1.31x faster                                 |
| 2to3                     | 348 ms                                                 | 266 ms: 1.31x faster                                   |
| genshi_xml               | 66.0 ms                                                | 50.5 ms: 1.31x faster                                  |
| xml_etree_process        | 79.1 ms                                                | 60.5 ms: 1.31x faster                                  |
| nqueens                  | 106 ms                                                 | 80.9 ms: 1.31x faster                                  |
| sympy_sum                | 196 ms                                                 | 150 ms: 1.31x faster                                   |
| dulwich_log              | 84.3 ms                                                | 64.6 ms: 1.31x faster                                  |
| sympy_integrate          | 25.8 ms                                                | 19.8 ms: 1.30x faster                                  |
| sqlglot_optimize         | 69.2 ms                                                | 53.4 ms: 1.30x faster                                  |
| sqlalchemy_declarative   | 172 ms                                                 | 133 ms: 1.30x faster                                   |
| gunicorn                 | 1.53 ms                                                | 1.18 ms: 1.29x faster                                  |
| deepcopy_reduce          | 4.17 us                                                | 3.24 us: 1.29x faster                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.03 ms: 1.29x faster                                  |
| docutils                 | 3.30 sec                                               | 2.58 sec: 1.27x faster                                 |
| scimark_fft              | 466 ms                                                 | 367 ms: 1.27x faster                                   |
| sympy_str                | 346 ms                                                 | 273 ms: 1.27x faster                                   |
| sympy_expand             | 566 ms                                                 | 456 ms: 1.24x faster                                   |
| bench_thread_pool        | 986 us                                                 | 818 us: 1.21x faster                                   |
| pathlib                  | 20.5 ms                                                | 17.4 ms: 1.18x faster                                  |
| python_startup           | 14.6 ms                                                | 12.7 ms: 1.15x faster                                  |
| json_loads               | 31.2 us                                                | 27.2 us: 1.15x faster                                  |
| xml_etree_generate       | 99.4 ms                                                | 86.8 ms: 1.14x faster                                  |
| xml_etree_iterparse      | 115 ms                                                 | 101 ms: 1.14x faster                                   |
| mdp                      | 2.85 sec                                               | 2.54 sec: 1.12x faster                                 |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.10x faster                                   |
| xml_etree_parse          | 168 ms                                                 | 154 ms: 1.09x faster                                   |
| json                     | 5.69 ms                                                | 5.32 ms: 1.07x faster                                  |
| sqlite_synth             | 3.02 us                                                | 2.90 us: 1.04x faster                                  |
| regex_v8                 | 27.8 ms                                                | 26.9 ms: 1.03x faster                                  |
| regex_dna                | 227 ms                                                 | 220 ms: 1.03x faster                                   |
| async_generators         | 444 ms                                                 | 433 ms: 1.02x faster                                   |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                   |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                   |
| regex_effbot             | 3.63 ms                                                | 3.77 ms: 1.04x slower                                  |
| coverage                 | 79.4 ms                                                | 82.8 ms: 1.04x slower                                  |
| telco                    | 7.27 ms                                                | 8.40 ms: 1.16x slower                                  |
| python_startup_no_site   | 5.93 ms                                                | 7.00 ms: 1.18x slower                                  |
| gc_traversal             | 3.62 ms                                                | 4.90 ms: 1.35x slower                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.45 ms: 1.51x slower                                  |
| Geometric mean           | (ref)                                                  | 1.39x faster                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, gevent_hub, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.397x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.23x