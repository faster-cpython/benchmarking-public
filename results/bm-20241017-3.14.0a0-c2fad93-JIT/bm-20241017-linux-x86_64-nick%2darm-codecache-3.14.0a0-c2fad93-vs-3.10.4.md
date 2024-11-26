# Results vs. 3.10.4

- fork: nick-arm
- ref: codecache
- machine: linux-x86_64
- commit hash: c2fad93
- commit date: 2024-10-17
- overall geometric mean: 1.401x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.35x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 278 ms: 1.25x faster                                           |
| docutils       | 3.30 sec                                               | 2.96 sec: 1.11x faster                                         |
| html5lib       | 88.9 ms                                                | 64.4 ms: 1.38x faster                                          |
| tornado_http   | 136 ms                                                 | 94.9 ms: 1.44x faster                                          |
| Geometric mean | (ref)                                                  | 1.29x faster                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 331 ms: 2.20x faster                                           |
| async_tree_memoization  | 870 ms                                                 | 429 ms: 2.03x faster                                           |
| async_tree_io           | 1.77 sec                                               | 897 ms: 1.97x faster                                           |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 555 ms: 1.83x faster                                           |
| Geometric mean          | (ref)                                                  | 2.00x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 79.3 ms: 1.94x faster                                          |
| float          | 117 ms                                                 | 74.3 ms: 1.58x faster                                          |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                           |
| Geometric mean | (ref)                                                  | 1.46x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 138 ms: 1.36x faster                                           |
| regex_v8       | 27.8 ms                                                | 26.8 ms: 1.04x faster                                          |
| regex_dna      | 227 ms                                                 | 229 ms: 1.01x slower                                           |
| regex_effbot   | 3.63 ms                                                | 3.81 ms: 1.05x slower                                          |
| Geometric mean | (ref)                                                  | 1.07x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.93 sec: 1.63x faster                                         |
| pickle_pure_python   | 484 us                                                 | 304 us: 1.60x faster                                           |
| unpickle_pure_python | 331 us                                                 | 215 us: 1.54x faster                                           |
| xml_etree_process    | 79.1 ms                                                | 54.8 ms: 1.44x faster                                          |
| json_dumps           | 14.2 ms                                                | 10.1 ms: 1.40x faster                                          |
| xml_etree_generate   | 99.4 ms                                                | 78.6 ms: 1.26x faster                                          |
| json_loads           | 31.2 us                                                | 26.8 us: 1.16x faster                                          |
| xml_etree_iterparse  | 115 ms                                                 | 99.5 ms: 1.16x faster                                          |
| xml_etree_parse      | 168 ms                                                 | 147 ms: 1.14x faster                                           |
| unpickle_list        | 5.20 us                                                | 5.11 us: 1.02x faster                                          |
| pickle               | 10.7 us                                                | 11.8 us: 1.11x slower                                          |
| pickle_dict          | 29.6 us                                                | 35.0 us: 1.18x slower                                          |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                   |

Benchmark hidden because not significant (2): pickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.9 ms: 1.23x faster                                          |
| python_startup_no_site | 5.93 ms                                                | 7.07 ms: 1.19x slower                                          |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.87 ms: 1.65x faster                                          |
| django_template | 48.2 ms                                                | 36.7 ms: 1.31x faster                                          |
| genshi_text     | 31.8 ms                                                | 25.0 ms: 1.27x faster                                          |
| genshi_xml      | 66.0 ms                                                | 59.7 ms: 1.11x faster                                          |
| Geometric mean  | (ref)                                                  | 1.32x faster                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 166 us: 3.28x faster                                           |
| deltablue                | 7.91 ms                                                | 3.22 ms: 2.45x faster                                          |
| generators               | 80.1 ms                                                | 35.4 ms: 2.27x faster                                          |
| async_tree_none          | 728 ms                                                 | 331 ms: 2.20x faster                                           |
| deepcopy_memo            | 58.5 us                                                | 26.8 us: 2.18x faster                                          |
| async_tree_memoization   | 870 ms                                                 | 429 ms: 2.03x faster                                           |
| richards_super           | 94.7 ms                                                | 46.9 ms: 2.02x faster                                          |
| logging_silent           | 190 ns                                                 | 96.0 ns: 1.98x faster                                          |
| async_tree_io            | 1.77 sec                                               | 897 ms: 1.97x faster                                           |
| chaos                    | 115 ms                                                 | 59.5 ms: 1.94x faster                                          |
| nbody                    | 154 ms                                                 | 79.3 ms: 1.94x faster                                          |
| crypto_pyaes             | 128 ms                                                 | 67.0 ms: 1.91x faster                                          |
| scimark_monte_carlo      | 118 ms                                                 | 62.8 ms: 1.88x faster                                          |
| richards                 | 79.3 ms                                                | 42.6 ms: 1.86x faster                                          |
| asyncio_tcp              | 922 ms                                                 | 498 ms: 1.85x faster                                           |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 555 ms: 1.83x faster                                           |
| raytrace                 | 507 ms                                                 | 277 ms: 1.83x faster                                           |
| deepcopy                 | 479 us                                                 | 262 us: 1.83x faster                                           |
| go                       | 240 ms                                                 | 132 ms: 1.82x faster                                           |
| scimark_sor              | 220 ms                                                 | 124 ms: 1.77x faster                                           |
| comprehensions           | 28.8 us                                                | 17.1 us: 1.68x faster                                          |
| mako                     | 16.3 ms                                                | 9.87 ms: 1.65x faster                                          |
| sqlglot_parse            | 2.17 ms                                                | 1.32 ms: 1.64x faster                                          |
| tomli_loads              | 3.14 sec                                               | 1.93 sec: 1.63x faster                                         |
| scimark_lu               | 176 ms                                                 | 109 ms: 1.61x faster                                           |
| pickle_pure_python       | 484 us                                                 | 304 us: 1.60x faster                                           |
| pyflate                  | 716 ms                                                 | 453 ms: 1.58x faster                                           |
| deepcopy_reduce          | 4.17 us                                                | 2.64 us: 1.58x faster                                          |
| float                    | 117 ms                                                 | 74.3 ms: 1.58x faster                                          |
| coroutines               | 35.1 ms                                                | 22.6 ms: 1.55x faster                                          |
| scimark_fft              | 466 ms                                                 | 303 ms: 1.54x faster                                           |
| unpickle_pure_python     | 331 us                                                 | 215 us: 1.54x faster                                           |
| sqlglot_transpile        | 2.57 ms                                                | 1.68 ms: 1.53x faster                                          |
| spectral_norm            | 170 ms                                                 | 111 ms: 1.53x faster                                           |
| logging_simple           | 8.30 us                                                | 5.58 us: 1.49x faster                                          |
| hexiom                   | 10.4 ms                                                | 6.99 ms: 1.49x faster                                          |
| logging_format           | 9.09 us                                                | 6.14 us: 1.48x faster                                          |
| pylint                   | 551 ms                                                 | 374 ms: 1.47x faster                                           |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.40 ms: 1.47x faster                                          |
| pprint_safe_repr         | 1.02 sec                                               | 697 ms: 1.46x faster                                           |
| xml_etree_process        | 79.1 ms                                                | 54.8 ms: 1.44x faster                                          |
| tornado_http             | 136 ms                                                 | 94.9 ms: 1.44x faster                                          |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                         |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                         |
| json_dumps               | 14.2 ms                                                | 10.1 ms: 1.40x faster                                          |
| html5lib                 | 88.9 ms                                                | 64.4 ms: 1.38x faster                                          |
| fannkuch                 | 532 ms                                                 | 385 ms: 1.38x faster                                           |
| thrift                   | 1.07 ms                                                | 780 us: 1.37x faster                                           |
| regex_compile            | 188 ms                                                 | 138 ms: 1.36x faster                                           |
| django_template          | 48.2 ms                                                | 36.7 ms: 1.31x faster                                          |
| pathlib                  | 20.5 ms                                                | 15.8 ms: 1.29x faster                                          |
| pycparser                | 1.58 sec                                               | 1.22 sec: 1.29x faster                                         |
| genshi_text              | 31.8 ms                                                | 25.0 ms: 1.27x faster                                          |
| xml_etree_generate       | 99.4 ms                                                | 78.6 ms: 1.26x faster                                          |
| dulwich_log              | 84.3 ms                                                | 66.9 ms: 1.26x faster                                          |
| 2to3                     | 348 ms                                                 | 278 ms: 1.25x faster                                           |
| sqlglot_normalize        | 143 ms                                                 | 115 ms: 1.25x faster                                           |
| python_startup           | 14.6 ms                                                | 11.9 ms: 1.23x faster                                          |
| nqueens                  | 106 ms                                                 | 89.3 ms: 1.19x faster                                          |
| json_loads               | 31.2 us                                                | 26.8 us: 1.16x faster                                          |
| xml_etree_iterparse      | 115 ms                                                 | 99.5 ms: 1.16x faster                                          |
| sqlglot_optimize         | 69.2 ms                                                | 59.7 ms: 1.16x faster                                          |
| sympy_str                | 346 ms                                                 | 301 ms: 1.15x faster                                           |
| xml_etree_parse          | 168 ms                                                 | 147 ms: 1.14x faster                                           |
| sympy_expand             | 566 ms                                                 | 502 ms: 1.13x faster                                           |
| json                     | 5.69 ms                                                | 5.06 ms: 1.12x faster                                          |
| mdp                      | 2.85 sec                                               | 2.54 sec: 1.12x faster                                         |
| sympy_sum                | 196 ms                                                 | 176 ms: 1.11x faster                                           |
| docutils                 | 3.30 sec                                               | 2.96 sec: 1.11x faster                                         |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                           |
| genshi_xml               | 66.0 ms                                                | 59.7 ms: 1.11x faster                                          |
| sympy_integrate          | 25.8 ms                                                | 23.4 ms: 1.10x faster                                          |
| bench_thread_pool        | 986 us                                                 | 897 us: 1.10x faster                                           |
| sqlite_synth             | 3.02 us                                                | 2.81 us: 1.08x faster                                          |
| regex_v8                 | 27.8 ms                                                | 26.8 ms: 1.04x faster                                          |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                           |
| unpickle_list            | 5.20 us                                                | 5.11 us: 1.02x faster                                          |
| regex_dna                | 227 ms                                                 | 229 ms: 1.01x slower                                           |
| async_generators         | 444 ms                                                 | 463 ms: 1.04x slower                                           |
| regex_effbot             | 3.63 ms                                                | 3.81 ms: 1.05x slower                                          |
| telco                    | 7.27 ms                                                | 7.64 ms: 1.05x slower                                          |
| coverage                 | 79.4 ms                                                | 84.9 ms: 1.07x slower                                          |
| pickle                   | 10.7 us                                                | 11.8 us: 1.11x slower                                          |
| gc_traversal             | 3.62 ms                                                | 4.29 ms: 1.18x slower                                          |
| pickle_dict              | 29.6 us                                                | 35.0 us: 1.18x slower                                          |
| python_startup_no_site   | 5.93 ms                                                | 7.07 ms: 1.19x slower                                          |
| create_gc_cycles         | 1.62 ms                                                | 2.60 ms: 1.60x slower                                          |
| unpack_sequence          | 60.0 ns                                                | 108 ns: 1.80x slower                                           |
| bench_mp_pool            | 24.0 ms                                                | 84.4 ms: 3.51x slower                                          |
| Geometric mean           | (ref)                                                  | 1.34x faster                                                   |

Benchmark hidden because not significant (3): asyncio_websockets, pickle_list, unpickle
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241017-3.14.0a0-c2fad93-JIT/bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.401x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.35x