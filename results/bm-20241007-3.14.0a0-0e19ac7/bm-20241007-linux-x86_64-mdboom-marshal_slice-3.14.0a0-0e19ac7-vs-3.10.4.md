# Results vs. 3.10.4

- fork: mdboom
- ref: marshal_slice
- machine: linux-x86_64
- commit hash: 0e19ac7
- commit date: 2024-10-07
- overall geometric mean: 1.435x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 253 ms: 1.38x faster                                           |
| docutils       | 3.30 sec                                               | 2.62 sec: 1.26x faster                                         |
| html5lib       | 88.9 ms                                                | 61.4 ms: 1.45x faster                                          |
| tornado_http   | 136 ms                                                 | 90.2 ms: 1.51x faster                                          |
| Geometric mean | (ref)                                                  | 1.39x faster                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 320 ms: 2.28x faster                                           |
| async_tree_memoization  | 870 ms                                                 | 389 ms: 2.24x faster                                           |
| async_tree_io           | 1.77 sec                                               | 924 ms: 1.91x faster                                           |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 555 ms: 1.83x faster                                           |
| Geometric mean          | (ref)                                                  | 2.06x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 86.8 ms: 1.77x faster                                          |
| float          | 117 ms                                                 | 76.1 ms: 1.54x faster                                          |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                           |
| Geometric mean | (ref)                                                  | 1.41x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.48x faster                                           |
| regex_v8       | 27.8 ms                                                | 25.2 ms: 1.10x faster                                          |
| regex_dna      | 227 ms                                                 | 220 ms: 1.03x faster                                           |
| regex_effbot   | 3.63 ms                                                | 3.70 ms: 1.02x slower                                          |
| Geometric mean | (ref)                                                  | 1.13x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 305 us: 1.59x faster                                           |
| unpickle_pure_python | 331 us                                                 | 215 us: 1.54x faster                                           |
| tomli_loads          | 3.14 sec                                               | 2.07 sec: 1.52x faster                                         |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.38x faster                                          |
| xml_etree_process    | 79.1 ms                                                | 59.0 ms: 1.34x faster                                          |
| xml_etree_generate   | 99.4 ms                                                | 86.1 ms: 1.16x faster                                          |
| json_loads           | 31.2 us                                                | 27.1 us: 1.15x faster                                          |
| xml_etree_iterparse  | 115 ms                                                 | 104 ms: 1.11x faster                                           |
| xml_etree_parse      | 168 ms                                                 | 157 ms: 1.07x faster                                           |
| pickle_list          | 5.08 us                                                | 5.01 us: 1.01x faster                                          |
| unpickle_list        | 5.20 us                                                | 5.41 us: 1.04x slower                                          |
| unpickle             | 14.4 us                                                | 15.0 us: 1.05x slower                                          |
| pickle               | 10.7 us                                                | 11.5 us: 1.08x slower                                          |
| pickle_dict          | 29.6 us                                                | 34.9 us: 1.18x slower                                          |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                          |
| python_startup_no_site | 5.93 ms                                                | 7.01 ms: 1.18x slower                                          |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 21.9 ms: 1.46x faster                                          |
| mako            | 16.3 ms                                                | 11.4 ms: 1.43x faster                                          |
| django_template | 48.2 ms                                                | 34.2 ms: 1.41x faster                                          |
| genshi_xml      | 66.0 ms                                                | 49.3 ms: 1.34x faster                                          |
| Geometric mean  | (ref)                                                  | 1.41x faster                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 159 us: 3.43x faster                                           |
| generators               | 80.1 ms                                                | 27.7 ms: 2.89x faster                                          |
| deltablue                | 7.91 ms                                                | 3.26 ms: 2.43x faster                                          |
| async_tree_none          | 728 ms                                                 | 320 ms: 2.28x faster                                           |
| async_tree_memoization   | 870 ms                                                 | 389 ms: 2.24x faster                                           |
| go                       | 240 ms                                                 | 119 ms: 2.02x faster                                           |
| deepcopy_memo            | 58.5 us                                                | 29.7 us: 1.97x faster                                          |
| asyncio_tcp              | 922 ms                                                 | 470 ms: 1.96x faster                                           |
| chaos                    | 115 ms                                                 | 59.8 ms: 1.93x faster                                          |
| raytrace                 | 507 ms                                                 | 264 ms: 1.92x faster                                           |
| async_tree_io            | 1.77 sec                                               | 924 ms: 1.91x faster                                           |
| deepcopy                 | 479 us                                                 | 260 us: 1.85x faster                                           |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 555 ms: 1.83x faster                                           |
| logging_silent           | 190 ns                                                 | 104 ns: 1.82x faster                                           |
| richards_super           | 94.7 ms                                                | 52.1 ms: 1.82x faster                                          |
| crypto_pyaes             | 128 ms                                                 | 71.7 ms: 1.78x faster                                          |
| scimark_sor              | 220 ms                                                 | 124 ms: 1.77x faster                                           |
| nbody                    | 154 ms                                                 | 86.8 ms: 1.77x faster                                          |
| pylint                   | 551 ms                                                 | 316 ms: 1.75x faster                                           |
| scimark_monte_carlo      | 118 ms                                                 | 67.8 ms: 1.74x faster                                          |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                          |
| richards                 | 79.3 ms                                                | 46.0 ms: 1.72x faster                                          |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.70x faster                                          |
| hexiom                   | 10.4 ms                                                | 6.24 ms: 1.67x faster                                          |
| sqlglot_transpile        | 2.57 ms                                                | 1.58 ms: 1.63x faster                                          |
| pickle_pure_python       | 484 us                                                 | 305 us: 1.59x faster                                           |
| scimark_lu               | 176 ms                                                 | 112 ms: 1.58x faster                                           |
| coroutines               | 35.1 ms                                                | 22.8 ms: 1.54x faster                                          |
| float                    | 117 ms                                                 | 76.1 ms: 1.54x faster                                          |
| deepcopy_reduce          | 4.17 us                                                | 2.71 us: 1.54x faster                                          |
| unpickle_pure_python     | 331 us                                                 | 215 us: 1.54x faster                                           |
| tomli_loads              | 3.14 sec                                               | 2.07 sec: 1.52x faster                                         |
| pyflate                  | 716 ms                                                 | 472 ms: 1.52x faster                                           |
| spectral_norm            | 170 ms                                                 | 112 ms: 1.51x faster                                           |
| tornado_http             | 136 ms                                                 | 90.2 ms: 1.51x faster                                          |
| logging_simple           | 8.30 us                                                | 5.55 us: 1.50x faster                                          |
| regex_compile            | 188 ms                                                 | 127 ms: 1.48x faster                                           |
| logging_format           | 9.09 us                                                | 6.15 us: 1.48x faster                                          |
| pprint_pformat           | 2.10 sec                                               | 1.44 sec: 1.46x faster                                         |
| genshi_text              | 31.8 ms                                                | 21.9 ms: 1.46x faster                                          |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.77 sec: 1.45x faster                                         |
| pprint_safe_repr         | 1.02 sec                                               | 703 ms: 1.45x faster                                           |
| html5lib                 | 88.9 ms                                                | 61.4 ms: 1.45x faster                                          |
| mako                     | 16.3 ms                                                | 11.4 ms: 1.43x faster                                          |
| django_template          | 48.2 ms                                                | 34.2 ms: 1.41x faster                                          |
| thrift                   | 1.07 ms                                                | 767 us: 1.40x faster                                           |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                          |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.38x faster                                          |
| 2to3                     | 348 ms                                                 | 253 ms: 1.38x faster                                           |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.82 ms: 1.34x faster                                          |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.34x faster                                         |
| sympy_sum                | 196 ms                                                 | 146 ms: 1.34x faster                                           |
| xml_etree_process        | 79.1 ms                                                | 59.0 ms: 1.34x faster                                          |
| genshi_xml               | 66.0 ms                                                | 49.3 ms: 1.34x faster                                          |
| sqlglot_normalize        | 143 ms                                                 | 107 ms: 1.34x faster                                           |
| fannkuch                 | 532 ms                                                 | 399 ms: 1.33x faster                                           |
| dulwich_log              | 84.3 ms                                                | 64.4 ms: 1.31x faster                                          |
| sympy_integrate          | 25.8 ms                                                | 19.8 ms: 1.31x faster                                          |
| sqlglot_optimize         | 69.2 ms                                                | 53.3 ms: 1.30x faster                                          |
| pathlib                  | 20.5 ms                                                | 15.8 ms: 1.30x faster                                          |
| sympy_str                | 346 ms                                                 | 267 ms: 1.29x faster                                           |
| nqueens                  | 106 ms                                                 | 82.2 ms: 1.29x faster                                          |
| scimark_fft              | 466 ms                                                 | 364 ms: 1.28x faster                                           |
| docutils                 | 3.30 sec                                               | 2.62 sec: 1.26x faster                                         |
| sympy_expand             | 566 ms                                                 | 450 ms: 1.26x faster                                           |
| unpack_sequence          | 60.0 ns                                                | 48.3 ns: 1.24x faster                                          |
| xml_etree_generate       | 99.4 ms                                                | 86.1 ms: 1.16x faster                                          |
| bench_thread_pool        | 986 us                                                 | 856 us: 1.15x faster                                           |
| json_loads               | 31.2 us                                                | 27.1 us: 1.15x faster                                          |
| mdp                      | 2.85 sec                                               | 2.52 sec: 1.13x faster                                         |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                           |
| json                     | 5.69 ms                                                | 5.07 ms: 1.12x faster                                          |
| xml_etree_iterparse      | 115 ms                                                 | 104 ms: 1.11x faster                                           |
| regex_v8                 | 27.8 ms                                                | 25.2 ms: 1.10x faster                                          |
| sqlite_synth             | 3.02 us                                                | 2.80 us: 1.08x faster                                          |
| xml_etree_parse          | 168 ms                                                 | 157 ms: 1.07x faster                                           |
| regex_dna                | 227 ms                                                 | 220 ms: 1.03x faster                                           |
| async_generators         | 444 ms                                                 | 433 ms: 1.02x faster                                           |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                           |
| pickle_list              | 5.08 us                                                | 5.01 us: 1.01x faster                                          |
| regex_effbot             | 3.63 ms                                                | 3.70 ms: 1.02x slower                                          |
| unpickle_list            | 5.20 us                                                | 5.41 us: 1.04x slower                                          |
| unpickle                 | 14.4 us                                                | 15.0 us: 1.05x slower                                          |
| coverage                 | 79.4 ms                                                | 84.5 ms: 1.06x slower                                          |
| pickle                   | 10.7 us                                                | 11.5 us: 1.08x slower                                          |
| gc_traversal             | 3.62 ms                                                | 3.95 ms: 1.09x slower                                          |
| telco                    | 7.27 ms                                                | 8.01 ms: 1.10x slower                                          |
| create_gc_cycles         | 1.62 ms                                                | 1.79 ms: 1.10x slower                                          |
| pickle_dict              | 29.6 us                                                | 34.9 us: 1.18x slower                                          |
| python_startup_no_site   | 5.93 ms                                                | 7.01 ms: 1.18x slower                                          |
| bench_mp_pool            | 24.0 ms                                                | 55.9 ms: 2.33x slower                                          |
| Geometric mean           | (ref)                                                  | 1.39x faster                                                   |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241007-3.14.0a0-0e19ac7/bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.435x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.12x