# Results vs. 3.10.4

- fork: python
- ref: 6b10467fbc0b67bf217e
- machine: linux-aarch64
- commit hash: 6b10467
- commit date: 2024-06-03
- overall geometric mean: 1.28x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240603-arminc-aarch64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 305 ms: 1.25x faster                                                     |
| chameleon      | 10.8 ms                                                               | 8.89 ms: 1.22x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.08 sec: 1.15x faster                                                   |
| html5lib       | 86.5 ms                                                               | 67.4 ms: 1.28x faster                                                    |
| tornado_http   | 178 ms                                                                | 127 ms: 1.40x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.26x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240603-arminc-aarch64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 491 ms: 1.93x faster                                                     |
| async_tree_io           | 2.28 sec                                                              | 1.21 sec: 1.88x faster                                                   |
| async_tree_memoization  | 1.13 sec                                                              | 648 ms: 1.75x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 787 ms: 1.62x faster                                                     |
| Geometric mean          | (ref)                                                                 | 1.79x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240603-arminc-aarch64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 112 ms: 1.48x faster                                                     |
| float          | 135 ms                                                                | 91.9 ms: 1.47x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240603-arminc-aarch64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 129 ms: 1.37x faster                                                     |
| regex_v8       | 32.2 ms                                                               | 30.6 ms: 1.05x faster                                                    |
| regex_dna      | 257 ms                                                                | 247 ms: 1.04x faster                                                     |
| regex_effbot   | 4.25 ms                                                               | 4.84 ms: 1.14x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240603-arminc-aarch64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 363 us: 1.46x faster                                                     |
| unpickle_pure_python | 366 us                                                                | 253 us: 1.44x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.58 sec: 1.30x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 13.3 ms: 1.26x faster                                                    |
| xml_etree_process    | 99.5 ms                                                               | 82.1 ms: 1.21x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 191 ms: 1.11x faster                                                     |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.08x faster                                                     |
| unpickle_list        | 6.99 us                                                               | 6.45 us: 1.08x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 149 ms: 1.05x faster                                                     |
| pickle_list          | 5.24 us                                                               | 5.35 us: 1.02x slower                                                    |
| json_loads           | 30.9 us                                                               | 32.0 us: 1.03x slower                                                    |
| pickle_dict          | 35.1 us                                                               | 38.0 us: 1.08x slower                                                    |
| pickle               | 12.5 us                                                               | 13.7 us: 1.10x slower                                                    |
| unpickle             | 17.5 us                                                               | 19.7 us: 1.13x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.10x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240603-arminc-aarch64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.0 ms: 1.16x slower                                                    |
| python_startup_no_site | 6.89 ms                                                               | 8.64 ms: 1.25x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.21x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240603-arminc-aarch64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.2 ms: 1.44x faster                                                    |
| django_template | 53.3 ms                                                               | 41.5 ms: 1.28x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 27.9 ms: 1.26x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 60.4 ms: 1.16x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.28x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240603-arminc-aarch64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 197 us: 3.35x faster                                                     |
| deltablue                | 8.94 ms                                                               | 3.88 ms: 2.31x faster                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 7.11 ms: 2.05x faster                                                    |
| async_tree_none          | 950 ms                                                                | 491 ms: 1.93x faster                                                     |
| raytrace                 | 573 ms                                                                | 297 ms: 1.93x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 1.21 sec: 1.88x faster                                                   |
| generators               | 68.1 ms                                                               | 37.4 ms: 1.82x faster                                                    |
| chaos                    | 121 ms                                                                | 68.2 ms: 1.78x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 648 ms: 1.75x faster                                                     |
| richards_super           | 107 ms                                                                | 62.3 ms: 1.72x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.41 ms: 1.70x faster                                                    |
| logging_silent           | 222 ns                                                                | 134 ns: 1.66x faster                                                     |
| go                       | 264 ms                                                                | 161 ms: 1.65x faster                                                     |
| comprehensions           | 33.1 us                                                               | 20.2 us: 1.64x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 1.73 ms: 1.64x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 82.0 ms: 1.63x faster                                                    |
| richards                 | 91.7 ms                                                               | 56.5 ms: 1.62x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 787 ms: 1.62x faster                                                     |
| scimark_lu               | 227 ms                                                                | 142 ms: 1.60x faster                                                     |
| asyncio_tcp              | 944 ms                                                                | 590 ms: 1.60x faster                                                     |
| scimark_sor              | 246 ms                                                                | 161 ms: 1.53x faster                                                     |
| scimark_monte_carlo      | 128 ms                                                                | 84.2 ms: 1.52x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 7.20 ms: 1.52x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.20 sec: 1.49x faster                                                   |
| nbody                    | 166 ms                                                                | 112 ms: 1.48x faster                                                     |
| float                    | 135 ms                                                                | 91.9 ms: 1.47x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 363 us: 1.46x faster                                                     |
| unpickle_pure_python     | 366 us                                                                | 253 us: 1.44x faster                                                     |
| pylint                   | 485 ms                                                                | 337 ms: 1.44x faster                                                     |
| mako                     | 18.9 ms                                                               | 13.2 ms: 1.44x faster                                                    |
| pyflate                  | 795 ms                                                                | 559 ms: 1.42x faster                                                     |
| tornado_http             | 178 ms                                                                | 127 ms: 1.40x faster                                                     |
| logging_simple           | 9.78 us                                                               | 7.06 us: 1.38x faster                                                    |
| regex_compile            | 177 ms                                                                | 129 ms: 1.37x faster                                                     |
| logging_format           | 10.6 us                                                               | 7.75 us: 1.37x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.25 sec: 1.36x faster                                                   |
| spectral_norm            | 186 ms                                                                | 141 ms: 1.32x faster                                                     |
| thrift                   | 1.26 ms                                                               | 964 us: 1.31x faster                                                     |
| tomli_loads              | 3.36 sec                                                              | 2.58 sec: 1.30x faster                                                   |
| django_template          | 53.3 ms                                                               | 41.5 ms: 1.28x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 67.4 ms: 1.28x faster                                                    |
| sympy_sum                | 184 ms                                                                | 144 ms: 1.28x faster                                                     |
| coroutines               | 37.2 ms                                                               | 29.2 ms: 1.27x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 21.0 ms: 1.26x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 27.9 ms: 1.26x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 58.2 ms: 1.26x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.26 ms: 1.26x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 13.3 ms: 1.26x faster                                                    |
| 2to3                     | 381 ms                                                                | 305 ms: 1.25x faster                                                     |
| pprint_pformat           | 2.36 sec                                                              | 1.91 sec: 1.23x faster                                                   |
| sympy_str                | 329 ms                                                                | 267 ms: 1.23x faster                                                     |
| pprint_safe_repr         | 1.15 sec                                                              | 935 ms: 1.23x faster                                                     |
| gunicorn                 | 1.45 ms                                                               | 1.18 ms: 1.22x faster                                                    |
| chameleon                | 10.8 ms                                                               | 8.89 ms: 1.22x faster                                                    |
| mypy2                    | 936 ms                                                                | 770 ms: 1.21x faster                                                     |
| fannkuch                 | 546 ms                                                                | 450 ms: 1.21x faster                                                     |
| sqlglot_normalize        | 156 ms                                                                | 129 ms: 1.21x faster                                                     |
| xml_etree_process        | 99.5 ms                                                               | 82.1 ms: 1.21x faster                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 62.4 ms: 1.21x faster                                                    |
| dask                     | 450 ms                                                                | 373 ms: 1.21x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 52.0 us: 1.19x faster                                                    |
| nqueens                  | 117 ms                                                                | 99.6 ms: 1.18x faster                                                    |
| sympy_expand             | 543 ms                                                                | 463 ms: 1.17x faster                                                     |
| aiohttp                  | 1.39 ms                                                               | 1.19 ms: 1.17x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.53 ms: 1.17x faster                                                    |
| genshi_xml               | 69.8 ms                                                               | 60.4 ms: 1.16x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.08 sec: 1.15x faster                                                   |
| deepcopy                 | 511 us                                                                | 452 us: 1.13x faster                                                     |
| pathlib                  | 26.3 ms                                                               | 23.5 ms: 1.12x faster                                                    |
| scimark_fft              | 500 ms                                                                | 448 ms: 1.12x faster                                                     |
| deepcopy_reduce          | 4.60 us                                                               | 4.12 us: 1.12x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 191 ms: 1.11x faster                                                     |
| mdp                      | 3.70 sec                                                              | 3.33 sec: 1.11x faster                                                   |
| meteor_contest           | 126 ms                                                                | 114 ms: 1.11x faster                                                     |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.08x faster                                                     |
| unpickle_list            | 6.99 us                                                               | 6.45 us: 1.08x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.91 us: 1.05x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 30.6 ms: 1.05x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 149 ms: 1.05x faster                                                     |
| regex_dna                | 257 ms                                                                | 247 ms: 1.04x faster                                                     |
| json                     | 5.88 ms                                                               | 5.65 ms: 1.04x faster                                                    |
| pickle_list              | 5.24 us                                                               | 5.35 us: 1.02x slower                                                    |
| json_loads               | 30.9 us                                                               | 32.0 us: 1.03x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 2.37 ms: 1.05x slower                                                    |
| async_generators         | 452 ms                                                                | 487 ms: 1.08x slower                                                     |
| pickle_dict              | 35.1 us                                                               | 38.0 us: 1.08x slower                                                    |
| pickle                   | 12.5 us                                                               | 13.7 us: 1.10x slower                                                    |
| unpickle                 | 17.5 us                                                               | 19.7 us: 1.13x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.84 ms: 1.14x slower                                                    |
| python_startup           | 11.2 ms                                                               | 13.0 ms: 1.16x slower                                                    |
| coverage                 | 83.6 ms                                                               | 98.9 ms: 1.18x slower                                                    |
| telco                    | 8.49 ms                                                               | 10.0 ms: 1.18x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 5.07 ms: 1.22x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 8.64 ms: 1.25x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.28x faster                                                             |

Benchmark hidden because not significant (3): flaskblogging, pidigits, asyncio_websockets
Ignored benchmarks (2) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240603-3.13.0b1+-6b10467/bm-20240603-arminc-aarch64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.14x