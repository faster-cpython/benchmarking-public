# Results vs. 3.10.4

- fork: python
- ref: db6f5e193315a3bbfa7b
- machine: linux-x86_64
- commit hash: db6f5e1
- commit date: 2024-08-13
- overall geometric mean: 1.05x slower
- HPT reliability: 99.83%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-linux-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 395 ms: 1.13x slower                                                  |
| docutils       | 3.30 sec                                               | 3.34 sec: 1.01x slower                                                |
| html5lib       | 88.9 ms                                                | 98.3 ms: 1.11x slower                                                 |
| tornado_http   | 136 ms                                                 | 138 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.07x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-linux-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 906 ms: 1.95x faster                                                  |
| async_tree_none         | 728 ms                                                 | 412 ms: 1.77x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 517 ms: 1.68x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 662 ms: 1.53x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.73x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-linux-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 191 ms                                                 | 184 ms: 1.04x faster                                                  |
| float          | 117 ms                                                 | 142 ms: 1.21x slower                                                  |
| nbody          | 154 ms                                                 | 222 ms: 1.45x slower                                                  |
| Geometric mean | (ref)                                                  | 1.19x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-linux-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 27.8 ms                                                | 26.0 ms: 1.07x faster                                                 |
| regex_dna      | 227 ms                                                 | 218 ms: 1.04x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.51 ms: 1.04x faster                                                 |
| regex_compile  | 188 ms                                                 | 217 ms: 1.15x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-linux-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 168 ms                                                 | 149 ms: 1.13x faster                                                  |
| json_dumps           | 14.2 ms                                                | 13.5 ms: 1.05x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 113 ms: 1.02x faster                                                  |
| json_loads           | 31.2 us                                                | 32.4 us: 1.04x slower                                                 |
| tomli_loads          | 3.14 sec                                               | 3.26 sec: 1.04x slower                                                |
| xml_etree_generate   | 99.4 ms                                                | 110 ms: 1.11x slower                                                  |
| xml_etree_process    | 79.1 ms                                                | 88.8 ms: 1.12x slower                                                 |
| pickle_pure_python   | 484 us                                                 | 572 us: 1.18x slower                                                  |
| unpickle_pure_python | 331 us                                                 | 411 us: 1.24x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.06x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-linux-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.7 ms: 1.06x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 9.31 ms: 1.57x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.22x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-linux-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 59.2 ms: 1.23x slower                                                 |
| genshi_xml      | 66.0 ms                                                | 82.1 ms: 1.24x slower                                                 |
| genshi_text     | 31.8 ms                                                | 39.6 ms: 1.24x slower                                                 |
| mako            | 16.3 ms                                                | 21.0 ms: 1.28x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.25x slower                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-linux-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 249 us: 2.19x faster                                                  |
| generators               | 80.1 ms                                                | 37.4 ms: 2.14x faster                                                 |
| async_tree_io            | 1.77 sec                                               | 906 ms: 1.95x faster                                                  |
| async_tree_none          | 728 ms                                                 | 412 ms: 1.77x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 517 ms: 1.68x faster                                                  |
| asyncio_tcp              | 922 ms                                                 | 561 ms: 1.64x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 662 ms: 1.53x faster                                                  |
| pylint                   | 551 ms                                                 | 395 ms: 1.40x faster                                                  |
| asyncio_tcp_ssl          | 2.57 sec                                               | 2.07 sec: 1.24x faster                                                |
| gc_traversal             | 3.62 ms                                                | 3.02 ms: 1.20x faster                                                 |
| create_gc_cycles         | 1.62 ms                                                | 1.38 ms: 1.17x faster                                                 |
| deepcopy                 | 479 us                                                 | 417 us: 1.15x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 113 ms: 1.13x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 149 ms: 1.13x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 52.2 us: 1.12x faster                                                 |
| coroutines               | 35.1 ms                                                | 32.1 ms: 1.09x faster                                                 |
| pathlib                  | 20.5 ms                                                | 19.2 ms: 1.07x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 26.0 ms: 1.07x faster                                                 |
| python_startup           | 14.6 ms                                                | 13.7 ms: 1.06x faster                                                 |
| json_dumps               | 14.2 ms                                                | 13.5 ms: 1.05x faster                                                 |
| regex_dna                | 227 ms                                                 | 218 ms: 1.04x faster                                                  |
| regex_effbot             | 3.63 ms                                                | 3.51 ms: 1.04x faster                                                 |
| pidigits                 | 191 ms                                                 | 184 ms: 1.04x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 113 ms: 1.02x faster                                                  |
| richards                 | 79.3 ms                                                | 78.3 ms: 1.01x faster                                                 |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                  |
| bench_mp_pool            | 24.0 ms                                                | 23.9 ms: 1.00x faster                                                 |
| richards_super           | 94.7 ms                                                | 95.4 ms: 1.01x slower                                                 |
| docutils                 | 3.30 sec                                               | 3.34 sec: 1.01x slower                                                |
| tornado_http             | 136 ms                                                 | 138 ms: 1.01x slower                                                  |
| deepcopy_reduce          | 4.17 us                                                | 4.28 us: 1.03x slower                                                 |
| pycparser                | 1.58 sec                                               | 1.63 sec: 1.03x slower                                                |
| json_loads               | 31.2 us                                                | 32.4 us: 1.04x slower                                                 |
| tomli_loads              | 3.14 sec                                               | 3.26 sec: 1.04x slower                                                |
| scimark_fft              | 466 ms                                                 | 484 ms: 1.04x slower                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 124 ms: 1.05x slower                                                  |
| deltablue                | 7.91 ms                                                | 8.34 ms: 1.05x slower                                                 |
| json                     | 5.69 ms                                                | 6.04 ms: 1.06x slower                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 6.95 ms: 1.07x slower                                                 |
| pyflate                  | 716 ms                                                 | 773 ms: 1.08x slower                                                  |
| chaos                    | 115 ms                                                 | 125 ms: 1.08x slower                                                  |
| html5lib                 | 88.9 ms                                                | 98.3 ms: 1.11x slower                                                 |
| xml_etree_generate       | 99.4 ms                                                | 110 ms: 1.11x slower                                                  |
| spectral_norm            | 170 ms                                                 | 189 ms: 1.11x slower                                                  |
| sympy_integrate          | 25.8 ms                                                | 28.8 ms: 1.12x slower                                                 |
| xml_etree_process        | 79.1 ms                                                | 88.8 ms: 1.12x slower                                                 |
| nqueens                  | 106 ms                                                 | 119 ms: 1.12x slower                                                  |
| mdp                      | 2.85 sec                                               | 3.21 sec: 1.13x slower                                                |
| 2to3                     | 348 ms                                                 | 395 ms: 1.13x slower                                                  |
| thrift                   | 1.07 ms                                                | 1.22 ms: 1.14x slower                                                 |
| regex_compile            | 188 ms                                                 | 217 ms: 1.15x slower                                                  |
| hexiom                   | 10.4 ms                                                | 12.0 ms: 1.16x slower                                                 |
| fannkuch                 | 532 ms                                                 | 625 ms: 1.18x slower                                                  |
| pickle_pure_python       | 484 us                                                 | 572 us: 1.18x slower                                                  |
| raytrace                 | 507 ms                                                 | 598 ms: 1.18x slower                                                  |
| meteor_contest           | 120 ms                                                 | 143 ms: 1.20x slower                                                  |
| sqlglot_normalize        | 143 ms                                                 | 171 ms: 1.20x slower                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 3.08 ms: 1.20x slower                                                 |
| float                    | 117 ms                                                 | 142 ms: 1.21x slower                                                  |
| sqlglot_parse            | 2.17 ms                                                | 2.63 ms: 1.21x slower                                                 |
| scimark_sor              | 220 ms                                                 | 266 ms: 1.21x slower                                                  |
| django_template          | 48.2 ms                                                | 59.2 ms: 1.23x slower                                                 |
| sympy_str                | 346 ms                                                 | 425 ms: 1.23x slower                                                  |
| logging_simple           | 8.30 us                                                | 10.3 us: 1.24x slower                                                 |
| unpickle_pure_python     | 331 us                                                 | 411 us: 1.24x slower                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 85.9 ms: 1.24x slower                                                 |
| genshi_xml               | 66.0 ms                                                | 82.1 ms: 1.24x slower                                                 |
| genshi_text              | 31.8 ms                                                | 39.6 ms: 1.24x slower                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 1.27 sec: 1.25x slower                                                |
| pprint_pformat           | 2.10 sec                                               | 2.64 sec: 1.25x slower                                                |
| async_generators         | 444 ms                                                 | 559 ms: 1.26x slower                                                  |
| logging_format           | 9.09 us                                                | 11.6 us: 1.27x slower                                                 |
| go                       | 240 ms                                                 | 306 ms: 1.28x slower                                                  |
| mako                     | 16.3 ms                                                | 21.0 ms: 1.28x slower                                                 |
| sympy_sum                | 196 ms                                                 | 256 ms: 1.30x slower                                                  |
| sympy_expand             | 566 ms                                                 | 748 ms: 1.32x slower                                                  |
| scimark_lu               | 176 ms                                                 | 240 ms: 1.36x slower                                                  |
| coverage                 | 79.4 ms                                                | 111 ms: 1.40x slower                                                  |
| telco                    | 7.27 ms                                                | 10.4 ms: 1.43x slower                                                 |
| nbody                    | 154 ms                                                 | 222 ms: 1.45x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 9.31 ms: 1.57x slower                                                 |
| bench_thread_pool        | 986 us                                                 | 3.11 ms: 3.15x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.05x slower                                                          |

Benchmark hidden because not significant (2): comprehensions, logging_silent
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240813-3.14.0a0-db6f5e1-NOGIL/bm-20240813-linux-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 99.83% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.28x