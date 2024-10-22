# Results vs. 3.10.4

- fork: mdboom
- ref: marshal_slice
- machine: linux-x86_64
- commit hash: 0e19ac7
- commit date: 2024-10-07
- overall geometric mean: 1.36x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.18x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 277 ms: 1.26x faster                                           |
| docutils       | 3.30 sec                                               | 2.93 sec: 1.13x faster                                         |
| html5lib       | 88.9 ms                                                | 64.5 ms: 1.38x faster                                          |
| tornado_http   | 136 ms                                                 | 94.5 ms: 1.44x faster                                          |
| Geometric mean | (ref)                                                  | 1.30x faster                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 331 ms: 2.20x faster                                           |
| async_tree_memoization  | 870 ms                                                 | 401 ms: 2.17x faster                                           |
| async_tree_io           | 1.77 sec                                               | 937 ms: 1.89x faster                                           |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 570 ms: 1.78x faster                                           |
| Geometric mean          | (ref)                                                  | 2.00x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.7 ms: 1.90x faster                                          |
| float          | 117 ms                                                 | 72.2 ms: 1.62x faster                                          |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                           |
| Geometric mean | (ref)                                                  | 1.47x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 143 ms: 1.32x faster                                           |
| regex_v8       | 27.8 ms                                                | 24.1 ms: 1.15x faster                                          |
| regex_dna      | 227 ms                                                 | 219 ms: 1.04x faster                                           |
| regex_effbot   | 3.63 ms                                                | 3.77 ms: 1.04x slower                                          |
| Geometric mean | (ref)                                                  | 1.11x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.91 sec: 1.64x faster                                         |
| pickle_pure_python   | 484 us                                                 | 307 us: 1.58x faster                                           |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.52x faster                                           |
| xml_etree_process    | 79.1 ms                                                | 54.4 ms: 1.45x faster                                          |
| json_dumps           | 14.2 ms                                                | 10.0 ms: 1.41x faster                                          |
| xml_etree_generate   | 99.4 ms                                                | 77.2 ms: 1.29x faster                                          |
| json_loads           | 31.2 us                                                | 26.6 us: 1.17x faster                                          |
| xml_etree_parse      | 168 ms                                                 | 144 ms: 1.17x faster                                           |
| xml_etree_iterparse  | 115 ms                                                 | 99.1 ms: 1.16x faster                                          |
| pickle_list          | 5.08 us                                                | 5.20 us: 1.02x slower                                          |
| pickle               | 10.7 us                                                | 11.5 us: 1.08x slower                                          |
| pickle_dict          | 29.6 us                                                | 34.1 us: 1.15x slower                                          |
| Geometric mean       | (ref)                                                  | 1.20x faster                                                   |

Benchmark hidden because not significant (2): unpickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                          |
| python_startup_no_site | 5.93 ms                                                | 7.09 ms: 1.20x slower                                          |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.0 ms: 1.63x faster                                          |
| django_template | 48.2 ms                                                | 35.5 ms: 1.36x faster                                          |
| genshi_text     | 31.8 ms                                                | 25.5 ms: 1.25x faster                                          |
| genshi_xml      | 66.0 ms                                                | 58.3 ms: 1.13x faster                                          |
| Geometric mean  | (ref)                                                  | 1.33x faster                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.26x faster                                           |
| deltablue                | 7.91 ms                                                | 3.23 ms: 2.45x faster                                          |
| generators               | 80.1 ms                                                | 35.0 ms: 2.29x faster                                          |
| async_tree_none          | 728 ms                                                 | 331 ms: 2.20x faster                                           |
| deepcopy_memo            | 58.5 us                                                | 26.9 us: 2.17x faster                                          |
| async_tree_memoization   | 870 ms                                                 | 401 ms: 2.17x faster                                           |
| richards_super           | 94.7 ms                                                | 46.9 ms: 2.02x faster                                          |
| chaos                    | 115 ms                                                 | 59.4 ms: 1.94x faster                                          |
| crypto_pyaes             | 128 ms                                                 | 65.8 ms: 1.94x faster                                          |
| nbody                    | 154 ms                                                 | 80.7 ms: 1.90x faster                                          |
| asyncio_tcp              | 922 ms                                                 | 485 ms: 1.90x faster                                           |
| async_tree_io            | 1.77 sec                                               | 937 ms: 1.89x faster                                           |
| logging_silent           | 190 ns                                                 | 101 ns: 1.88x faster                                           |
| scimark_monte_carlo      | 118 ms                                                 | 63.3 ms: 1.87x faster                                          |
| richards                 | 79.3 ms                                                | 42.6 ms: 1.86x faster                                          |
| scimark_sor              | 220 ms                                                 | 118 ms: 1.86x faster                                           |
| raytrace                 | 507 ms                                                 | 277 ms: 1.83x faster                                           |
| go                       | 240 ms                                                 | 132 ms: 1.82x faster                                           |
| deepcopy                 | 479 us                                                 | 266 us: 1.80x faster                                           |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 570 ms: 1.78x faster                                           |
| comprehensions           | 28.8 us                                                | 17.0 us: 1.69x faster                                          |
| spectral_norm            | 170 ms                                                 | 102 ms: 1.66x faster                                           |
| tomli_loads              | 3.14 sec                                               | 1.91 sec: 1.64x faster                                         |
| pyflate                  | 716 ms                                                 | 439 ms: 1.63x faster                                           |
| mako                     | 16.3 ms                                                | 10.0 ms: 1.63x faster                                          |
| float                    | 117 ms                                                 | 72.2 ms: 1.62x faster                                          |
| sqlglot_parse            | 2.17 ms                                                | 1.36 ms: 1.59x faster                                          |
| pickle_pure_python       | 484 us                                                 | 307 us: 1.58x faster                                           |
| scimark_lu               | 176 ms                                                 | 112 ms: 1.58x faster                                           |
| deepcopy_reduce          | 4.17 us                                                | 2.66 us: 1.57x faster                                          |
| coroutines               | 35.1 ms                                                | 22.7 ms: 1.55x faster                                          |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.52x faster                                           |
| sqlglot_transpile        | 2.57 ms                                                | 1.69 ms: 1.52x faster                                          |
| scimark_fft              | 466 ms                                                 | 310 ms: 1.50x faster                                           |
| hexiom                   | 10.4 ms                                                | 6.97 ms: 1.49x faster                                          |
| pylint                   | 551 ms                                                 | 375 ms: 1.47x faster                                           |
| logging_simple           | 8.30 us                                                | 5.66 us: 1.47x faster                                          |
| logging_format           | 9.09 us                                                | 6.20 us: 1.47x faster                                          |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.42 ms: 1.46x faster                                          |
| xml_etree_process        | 79.1 ms                                                | 54.4 ms: 1.45x faster                                          |
| tornado_http             | 136 ms                                                 | 94.5 ms: 1.44x faster                                          |
| fannkuch                 | 532 ms                                                 | 369 ms: 1.44x faster                                           |
| pprint_safe_repr         | 1.02 sec                                               | 712 ms: 1.43x faster                                           |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                         |
| json_dumps               | 14.2 ms                                                | 10.0 ms: 1.41x faster                                          |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.41x faster                                         |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                          |
| html5lib                 | 88.9 ms                                                | 64.5 ms: 1.38x faster                                          |
| thrift                   | 1.07 ms                                                | 783 us: 1.37x faster                                           |
| django_template          | 48.2 ms                                                | 35.5 ms: 1.36x faster                                          |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                         |
| regex_compile            | 188 ms                                                 | 143 ms: 1.32x faster                                           |
| xml_etree_generate       | 99.4 ms                                                | 77.2 ms: 1.29x faster                                          |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.29x faster                                          |
| 2to3                     | 348 ms                                                 | 277 ms: 1.26x faster                                           |
| dulwich_log              | 84.3 ms                                                | 67.3 ms: 1.25x faster                                          |
| genshi_text              | 31.8 ms                                                | 25.5 ms: 1.25x faster                                          |
| sqlglot_normalize        | 143 ms                                                 | 116 ms: 1.24x faster                                           |
| nqueens                  | 106 ms                                                 | 86.7 ms: 1.22x faster                                          |
| json_loads               | 31.2 us                                                | 26.6 us: 1.17x faster                                          |
| xml_etree_parse          | 168 ms                                                 | 144 ms: 1.17x faster                                           |
| xml_etree_iterparse      | 115 ms                                                 | 99.1 ms: 1.16x faster                                          |
| regex_v8                 | 27.8 ms                                                | 24.1 ms: 1.15x faster                                          |
| sympy_str                | 346 ms                                                 | 301 ms: 1.15x faster                                           |
| sqlglot_optimize         | 69.2 ms                                                | 60.4 ms: 1.15x faster                                          |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.14x faster                                           |
| genshi_xml               | 66.0 ms                                                | 58.3 ms: 1.13x faster                                          |
| sympy_expand             | 566 ms                                                 | 502 ms: 1.13x faster                                           |
| docutils                 | 3.30 sec                                               | 2.93 sec: 1.13x faster                                         |
| sympy_sum                | 196 ms                                                 | 175 ms: 1.12x faster                                           |
| mdp                      | 2.85 sec                                               | 2.54 sec: 1.12x faster                                         |
| bench_thread_pool        | 986 us                                                 | 890 us: 1.11x faster                                           |
| sympy_integrate          | 25.8 ms                                                | 23.3 ms: 1.11x faster                                          |
| sqlite_synth             | 3.02 us                                                | 2.75 us: 1.10x faster                                          |
| json                     | 5.69 ms                                                | 5.19 ms: 1.10x faster                                          |
| regex_dna                | 227 ms                                                 | 219 ms: 1.04x faster                                           |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                           |
| asyncio_websockets       | 559 ms                                                 | 556 ms: 1.00x faster                                           |
| pickle_list              | 5.08 us                                                | 5.20 us: 1.02x slower                                          |
| async_generators         | 444 ms                                                 | 460 ms: 1.04x slower                                           |
| regex_effbot             | 3.63 ms                                                | 3.77 ms: 1.04x slower                                          |
| telco                    | 7.27 ms                                                | 7.56 ms: 1.04x slower                                          |
| gc_traversal             | 3.62 ms                                                | 3.78 ms: 1.04x slower                                          |
| coverage                 | 79.4 ms                                                | 85.3 ms: 1.07x slower                                          |
| pickle                   | 10.7 us                                                | 11.5 us: 1.08x slower                                          |
| create_gc_cycles         | 1.62 ms                                                | 1.80 ms: 1.11x slower                                          |
| pickle_dict              | 29.6 us                                                | 34.1 us: 1.15x slower                                          |
| python_startup_no_site   | 5.93 ms                                                | 7.09 ms: 1.20x slower                                          |
| unpack_sequence          | 60.0 ns                                                | 108 ns: 1.80x slower                                           |
| bench_mp_pool            | 24.0 ms                                                | 61.2 ms: 2.55x slower                                          |
| Geometric mean           | (ref)                                                  | 1.36x faster                                                   |

Benchmark hidden because not significant (2): unpickle_list, unpickle
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241007-3.14.0a0-0e19ac7-JIT/bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.18x