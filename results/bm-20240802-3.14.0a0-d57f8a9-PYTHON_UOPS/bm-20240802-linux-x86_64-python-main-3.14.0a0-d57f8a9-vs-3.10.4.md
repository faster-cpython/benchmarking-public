# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: d57f8a9
- commit date: 2024-08-02
- overall geometric mean: 1.23x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-linux-x86_64-python-main-3.14.0a0-d57f8a9 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 348 ms                                                 | 319 ms: 1.09x faster                                  |
| docutils       | 3.30 sec                                               | 3.17 sec: 1.04x faster                                |
| html5lib       | 88.9 ms                                                | 73.9 ms: 1.20x faster                                 |
| tornado_http   | 136 ms                                                 | 97.6 ms: 1.40x faster                                 |
| Geometric mean | (ref)                                                  | 1.18x faster                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-linux-x86_64-python-main-3.14.0a0-d57f8a9 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 345 ms: 2.11x faster                                  |
| async_tree_memoization  | 870 ms                                                 | 448 ms: 1.94x faster                                  |
| async_tree_io           | 1.77 sec                                               | 940 ms: 1.88x faster                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 579 ms: 1.76x faster                                  |
| Geometric mean          | (ref)                                                  | 1.92x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-linux-x86_64-python-main-3.14.0a0-d57f8a9 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| float          | 117 ms                                                 | 86.2 ms: 1.36x faster                                 |
| nbody          | 154 ms                                                 | 122 ms: 1.26x faster                                  |
| pidigits       | 191 ms                                                 | 188 ms: 1.01x faster                                  |
| Geometric mean | (ref)                                                  | 1.20x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-linux-x86_64-python-main-3.14.0a0-d57f8a9 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_v8       | 27.8 ms                                                | 24.8 ms: 1.12x faster                                 |
| regex_compile  | 188 ms                                                 | 184 ms: 1.02x faster                                  |
| regex_dna      | 227 ms                                                 | 224 ms: 1.01x faster                                  |
| regex_effbot   | 3.63 ms                                                | 3.70 ms: 1.02x slower                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-linux-x86_64-python-main-3.14.0a0-d57f8a9 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| json_dumps           | 14.2 ms                                                | 10.8 ms: 1.31x faster                                 |
| tomli_loads          | 3.14 sec                                               | 2.57 sec: 1.22x faster                                |
| xml_etree_process    | 79.1 ms                                                | 65.0 ms: 1.22x faster                                 |
| unpickle_pure_python | 331 us                                                 | 272 us: 1.22x faster                                  |
| pickle_pure_python   | 484 us                                                 | 404 us: 1.20x faster                                  |
| xml_etree_parse      | 168 ms                                                 | 149 ms: 1.13x faster                                  |
| json_loads           | 31.2 us                                                | 28.3 us: 1.10x faster                                 |
| xml_etree_generate   | 99.4 ms                                                | 93.7 ms: 1.06x faster                                 |
| xml_etree_iterparse  | 115 ms                                                 | 109 ms: 1.06x faster                                  |
| Geometric mean       | (ref)                                                  | 1.17x faster                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-linux-x86_64-python-main-3.14.0a0-d57f8a9 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.38x faster                                 |
| python_startup_no_site | 5.93 ms                                                | 7.15 ms: 1.20x slower                                 |
| Geometric mean         | (ref)                                                  | 1.07x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-linux-x86_64-python-main-3.14.0a0-d57f8a9 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako            | 16.3 ms                                                | 13.9 ms: 1.18x faster                                 |
| django_template | 48.2 ms                                                | 41.4 ms: 1.16x faster                                 |
| genshi_text     | 31.8 ms                                                | 28.0 ms: 1.14x faster                                 |
| genshi_xml      | 66.0 ms                                                | 64.1 ms: 1.03x faster                                 |
| Geometric mean  | (ref)                                                  | 1.13x faster                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-linux-x86_64-python-main-3.14.0a0-d57f8a9 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 187 us: 2.91x faster                                  |
| async_tree_none          | 728 ms                                                 | 345 ms: 2.11x faster                                  |
| deltablue                | 7.91 ms                                                | 4.04 ms: 1.96x faster                                 |
| async_tree_memoization   | 870 ms                                                 | 448 ms: 1.94x faster                                  |
| async_tree_io            | 1.77 sec                                               | 940 ms: 1.88x faster                                  |
| generators               | 80.1 ms                                                | 43.4 ms: 1.85x faster                                 |
| asyncio_tcp              | 922 ms                                                 | 509 ms: 1.81x faster                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 579 ms: 1.76x faster                                  |
| raytrace                 | 507 ms                                                 | 318 ms: 1.60x faster                                  |
| pylint                   | 551 ms                                                 | 362 ms: 1.52x faster                                  |
| coroutines               | 35.1 ms                                                | 23.2 ms: 1.51x faster                                 |
| richards_super           | 94.7 ms                                                | 64.0 ms: 1.48x faster                                 |
| chaos                    | 115 ms                                                 | 79.5 ms: 1.45x faster                                 |
| deepcopy                 | 479 us                                                 | 333 us: 1.44x faster                                  |
| deepcopy_memo            | 58.5 us                                                | 41.0 us: 1.42x faster                                 |
| crypto_pyaes             | 128 ms                                                 | 90.0 ms: 1.42x faster                                 |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.82 sec: 1.41x faster                                |
| scimark_monte_carlo      | 118 ms                                                 | 84.4 ms: 1.40x faster                                 |
| tornado_http             | 136 ms                                                 | 97.6 ms: 1.40x faster                                 |
| richards                 | 79.3 ms                                                | 56.9 ms: 1.39x faster                                 |
| scimark_sor              | 220 ms                                                 | 158 ms: 1.39x faster                                  |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.38x faster                                 |
| go                       | 240 ms                                                 | 177 ms: 1.36x faster                                  |
| float                    | 117 ms                                                 | 86.2 ms: 1.36x faster                                 |
| sqlglot_parse            | 2.17 ms                                                | 1.60 ms: 1.36x faster                                 |
| thrift                   | 1.07 ms                                                | 805 us: 1.33x faster                                  |
| logging_simple           | 8.30 us                                                | 6.33 us: 1.31x faster                                 |
| sqlglot_transpile        | 2.57 ms                                                | 1.96 ms: 1.31x faster                                 |
| json_dumps               | 14.2 ms                                                | 10.8 ms: 1.31x faster                                 |
| logging_silent           | 190 ns                                                 | 146 ns: 1.30x faster                                  |
| deepcopy_reduce          | 4.17 us                                                | 3.24 us: 1.29x faster                                 |
| scimark_lu               | 176 ms                                                 | 138 ms: 1.28x faster                                  |
| nbody                    | 154 ms                                                 | 122 ms: 1.26x faster                                  |
| logging_format           | 9.09 us                                                | 7.27 us: 1.25x faster                                 |
| pyflate                  | 716 ms                                                 | 574 ms: 1.25x faster                                  |
| pathlib                  | 20.5 ms                                                | 16.6 ms: 1.23x faster                                 |
| tomli_loads              | 3.14 sec                                               | 2.57 sec: 1.22x faster                                |
| xml_etree_process        | 79.1 ms                                                | 65.0 ms: 1.22x faster                                 |
| unpickle_pure_python     | 331 us                                                 | 272 us: 1.22x faster                                  |
| comprehensions           | 28.8 us                                                | 23.8 us: 1.21x faster                                 |
| html5lib                 | 88.9 ms                                                | 73.9 ms: 1.20x faster                                 |
| pickle_pure_python       | 484 us                                                 | 404 us: 1.20x faster                                  |
| spectral_norm            | 170 ms                                                 | 144 ms: 1.18x faster                                  |
| mako                     | 16.3 ms                                                | 13.9 ms: 1.18x faster                                 |
| dask                     | 441 ms                                                 | 377 ms: 1.17x faster                                  |
| django_template          | 48.2 ms                                                | 41.4 ms: 1.16x faster                                 |
| bench_thread_pool        | 986 us                                                 | 862 us: 1.14x faster                                  |
| genshi_text              | 31.8 ms                                                | 28.0 ms: 1.14x faster                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.71 ms: 1.13x faster                                 |
| xml_etree_parse          | 168 ms                                                 | 149 ms: 1.13x faster                                  |
| regex_v8                 | 27.8 ms                                                | 24.8 ms: 1.12x faster                                 |
| json_loads               | 31.2 us                                                | 28.3 us: 1.10x faster                                 |
| pycparser                | 1.58 sec                                               | 1.43 sec: 1.10x faster                                |
| sympy_sum                | 196 ms                                                 | 180 ms: 1.09x faster                                  |
| 2to3                     | 348 ms                                                 | 319 ms: 1.09x faster                                  |
| json                     | 5.69 ms                                                | 5.25 ms: 1.08x faster                                 |
| hexiom                   | 10.4 ms                                                | 9.64 ms: 1.08x faster                                 |
| pprint_safe_repr         | 1.02 sec                                               | 951 ms: 1.07x faster                                  |
| scimark_fft              | 466 ms                                                 | 436 ms: 1.07x faster                                  |
| fannkuch                 | 532 ms                                                 | 498 ms: 1.07x faster                                  |
| sympy_integrate          | 25.8 ms                                                | 24.3 ms: 1.06x faster                                 |
| pprint_pformat           | 2.10 sec                                               | 1.98 sec: 1.06x faster                                |
| xml_etree_generate       | 99.4 ms                                                | 93.7 ms: 1.06x faster                                 |
| sqlglot_optimize         | 69.2 ms                                                | 65.5 ms: 1.06x faster                                 |
| xml_etree_iterparse      | 115 ms                                                 | 109 ms: 1.06x faster                                  |
| sqlglot_normalize        | 143 ms                                                 | 136 ms: 1.05x faster                                  |
| docutils                 | 3.30 sec                                               | 3.17 sec: 1.04x faster                                |
| sympy_str                | 346 ms                                                 | 333 ms: 1.04x faster                                  |
| genshi_xml               | 66.0 ms                                                | 64.1 ms: 1.03x faster                                 |
| nqueens                  | 106 ms                                                 | 103 ms: 1.02x faster                                  |
| regex_compile            | 188 ms                                                 | 184 ms: 1.02x faster                                  |
| pidigits                 | 191 ms                                                 | 188 ms: 1.01x faster                                  |
| regex_dna                | 227 ms                                                 | 224 ms: 1.01x faster                                  |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                  |
| gc_traversal             | 3.62 ms                                                | 3.65 ms: 1.01x slower                                 |
| regex_effbot             | 3.63 ms                                                | 3.70 ms: 1.02x slower                                 |
| meteor_contest           | 120 ms                                                 | 123 ms: 1.03x slower                                  |
| async_generators         | 444 ms                                                 | 459 ms: 1.03x slower                                  |
| mdp                      | 2.85 sec                                               | 2.97 sec: 1.04x slower                                |
| coverage                 | 79.4 ms                                                | 83.6 ms: 1.05x slower                                 |
| create_gc_cycles         | 1.62 ms                                                | 1.77 ms: 1.09x slower                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.15 ms: 1.20x slower                                 |
| telco                    | 7.27 ms                                                | 8.79 ms: 1.21x slower                                 |
| Geometric mean           | (ref)                                                  | 1.23x faster                                          |

Benchmark hidden because not significant (2): sympy_expand, bench_mp_pool
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240802-3.14.0a0-d57f8a9-PYTHON_UOPS/bm-20240802-linux-x86_64-python-main-3.14.0a0-d57f8a9.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.14x