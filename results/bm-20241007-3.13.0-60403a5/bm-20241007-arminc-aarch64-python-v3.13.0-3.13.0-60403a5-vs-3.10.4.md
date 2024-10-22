# Results vs. 3.10.4

- fork: python
- ref: v3.13.0
- machine: linux-aarch64
- commit hash: 60403a5
- commit date: 2024-10-07
- overall geometric mean: 1.28x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 306 ms: 1.25x faster                                     |
| chameleon      | 10.8 ms                                                               | 9.02 ms: 1.20x faster                                    |
| docutils       | 3.53 sec                                                              | 2.91 sec: 1.21x faster                                   |
| html5lib       | 86.5 ms                                                               | 64.3 ms: 1.34x faster                                    |
| tornado_http   | 178 ms                                                                | 131 ms: 1.36x faster                                     |
| Geometric mean | (ref)                                                                 | 1.27x faster                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|-------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 1.11 sec: 2.07x faster                                   |
| async_tree_none         | 950 ms                                                                | 493 ms: 1.92x faster                                     |
| async_tree_memoization  | 1.13 sec                                                              | 626 ms: 1.81x faster                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 764 ms: 1.67x faster                                     |
| Geometric mean          | (ref)                                                                 | 1.86x faster                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| nbody          | 166 ms                                                                | 114 ms: 1.45x faster                                     |
| float          | 135 ms                                                                | 94.4 ms: 1.43x faster                                    |
| Geometric mean | (ref)                                                                 | 1.28x faster                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 128 ms: 1.37x faster                                     |
| regex_dna      | 257 ms                                                                | 246 ms: 1.04x faster                                     |
| regex_v8       | 32.2 ms                                                               | 31.5 ms: 1.02x faster                                    |
| regex_effbot   | 4.25 ms                                                               | 4.87 ms: 1.15x slower                                    |
| Geometric mean | (ref)                                                                 | 1.06x faster                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 359 us: 1.47x faster                                     |
| unpickle_pure_python | 366 us                                                                | 254 us: 1.44x faster                                     |
| tomli_loads          | 3.36 sec                                                              | 2.53 sec: 1.33x faster                                   |
| json_dumps           | 16.7 ms                                                               | 13.4 ms: 1.25x faster                                    |
| xml_etree_process    | 99.5 ms                                                               | 80.1 ms: 1.24x faster                                    |
| xml_etree_parse      | 212 ms                                                                | 188 ms: 1.13x faster                                     |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.09x faster                                     |
| xml_etree_iterparse  | 156 ms                                                                | 147 ms: 1.06x faster                                     |
| unpickle_list        | 6.99 us                                                               | 6.65 us: 1.05x faster                                    |
| json_loads           | 30.9 us                                                               | 31.4 us: 1.02x slower                                    |
| pickle_list          | 5.24 us                                                               | 5.34 us: 1.02x slower                                    |
| pickle               | 12.5 us                                                               | 13.5 us: 1.08x slower                                    |
| pickle_dict          | 35.1 us                                                               | 38.1 us: 1.09x slower                                    |
| unpickle             | 17.5 us                                                               | 20.2 us: 1.15x slower                                    |
| Geometric mean       | (ref)                                                                 | 1.11x faster                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.3 ms: 1.19x slower                                    |
| python_startup_no_site | 6.89 ms                                                               | 8.75 ms: 1.27x slower                                    |
| Geometric mean         | (ref)                                                                 | 1.23x slower                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.3 ms: 1.42x faster                                    |
| genshi_text     | 35.2 ms                                                               | 27.7 ms: 1.27x faster                                    |
| django_template | 53.3 ms                                                               | 42.3 ms: 1.26x faster                                    |
| genshi_xml      | 69.8 ms                                                               | 60.2 ms: 1.16x faster                                    |
| Geometric mean  | (ref)                                                                 | 1.28x faster                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 |
|--------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 192 us: 3.45x faster                                     |
| deltablue                | 8.94 ms                                                               | 3.85 ms: 2.32x faster                                    |
| async_tree_io            | 2.28 sec                                                              | 1.11 sec: 2.07x faster                                   |
| bench_mp_pool            | 14.5 ms                                                               | 7.30 ms: 1.99x faster                                    |
| async_tree_none          | 950 ms                                                                | 493 ms: 1.92x faster                                     |
| raytrace                 | 573 ms                                                                | 298 ms: 1.92x faster                                     |
| async_tree_memoization   | 1.13 sec                                                              | 626 ms: 1.81x faster                                     |
| generators               | 68.1 ms                                                               | 37.8 ms: 1.80x faster                                    |
| richards_super           | 107 ms                                                                | 60.3 ms: 1.78x faster                                    |
| chaos                    | 121 ms                                                                | 68.8 ms: 1.76x faster                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.38 ms: 1.74x faster                                    |
| richards                 | 91.7 ms                                                               | 53.5 ms: 1.71x faster                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 764 ms: 1.67x faster                                     |
| asyncio_tcp              | 944 ms                                                                | 568 ms: 1.66x faster                                     |
| logging_silent           | 222 ns                                                                | 135 ns: 1.64x faster                                     |
| sqlglot_transpile        | 2.84 ms                                                               | 1.73 ms: 1.64x faster                                    |
| scimark_lu               | 227 ms                                                                | 139 ms: 1.63x faster                                     |
| go                       | 264 ms                                                                | 163 ms: 1.63x faster                                     |
| comprehensions           | 33.1 us                                                               | 20.4 us: 1.62x faster                                    |
| crypto_pyaes             | 134 ms                                                                | 82.7 ms: 1.62x faster                                    |
| scimark_sor              | 246 ms                                                                | 159 ms: 1.55x faster                                     |
| hexiom                   | 10.9 ms                                                               | 7.13 ms: 1.53x faster                                    |
| scimark_monte_carlo      | 128 ms                                                                | 83.8 ms: 1.52x faster                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.18 sec: 1.51x faster                                   |
| pickle_pure_python       | 529 us                                                                | 359 us: 1.47x faster                                     |
| nbody                    | 166 ms                                                                | 114 ms: 1.45x faster                                     |
| unpickle_pure_python     | 366 us                                                                | 254 us: 1.44x faster                                     |
| pyflate                  | 795 ms                                                                | 556 ms: 1.43x faster                                     |
| float                    | 135 ms                                                                | 94.4 ms: 1.43x faster                                    |
| mako                     | 18.9 ms                                                               | 13.3 ms: 1.42x faster                                    |
| pylint                   | 485 ms                                                                | 343 ms: 1.41x faster                                     |
| logging_simple           | 9.78 us                                                               | 7.04 us: 1.39x faster                                    |
| regex_compile            | 177 ms                                                                | 128 ms: 1.37x faster                                     |
| tornado_http             | 178 ms                                                                | 131 ms: 1.36x faster                                     |
| logging_format           | 10.6 us                                                               | 7.83 us: 1.35x faster                                    |
| html5lib                 | 86.5 ms                                                               | 64.3 ms: 1.34x faster                                    |
| pycparser                | 1.69 sec                                                              | 1.26 sec: 1.34x faster                                   |
| thrift                   | 1.26 ms                                                               | 946 us: 1.33x faster                                     |
| tomli_loads              | 3.36 sec                                                              | 2.53 sec: 1.33x faster                                   |
| spectral_norm            | 186 ms                                                                | 141 ms: 1.32x faster                                     |
| coroutines               | 37.2 ms                                                               | 28.2 ms: 1.32x faster                                    |
| dask                     | 450 ms                                                                | 350 ms: 1.28x faster                                     |
| sympy_sum                | 184 ms                                                                | 143 ms: 1.28x faster                                     |
| genshi_text              | 35.2 ms                                                               | 27.7 ms: 1.27x faster                                    |
| sympy_integrate          | 26.5 ms                                                               | 21.0 ms: 1.27x faster                                    |
| django_template          | 53.3 ms                                                               | 42.3 ms: 1.26x faster                                    |
| json_dumps               | 16.7 ms                                                               | 13.4 ms: 1.25x faster                                    |
| sympy_str                | 329 ms                                                                | 264 ms: 1.25x faster                                     |
| 2to3                     | 381 ms                                                                | 306 ms: 1.25x faster                                     |
| bench_thread_pool        | 1.59 ms                                                               | 1.28 ms: 1.25x faster                                    |
| pprint_pformat           | 2.36 sec                                                              | 1.90 sec: 1.24x faster                                   |
| xml_etree_process        | 99.5 ms                                                               | 80.1 ms: 1.24x faster                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 926 ms: 1.24x faster                                     |
| sqlglot_normalize        | 156 ms                                                                | 128 ms: 1.22x faster                                     |
| docutils                 | 3.53 sec                                                              | 2.91 sec: 1.21x faster                                   |
| sqlglot_optimize         | 75.4 ms                                                               | 62.4 ms: 1.21x faster                                    |
| deepcopy_memo            | 61.7 us                                                               | 51.0 us: 1.21x faster                                    |
| fannkuch                 | 546 ms                                                                | 452 ms: 1.21x faster                                     |
| gunicorn                 | 1.45 ms                                                               | 1.20 ms: 1.21x faster                                    |
| chameleon                | 10.8 ms                                                               | 9.02 ms: 1.20x faster                                    |
| sympy_expand             | 543 ms                                                                | 455 ms: 1.19x faster                                     |
| nqueens                  | 117 ms                                                                | 98.7 ms: 1.19x faster                                    |
| pathlib                  | 26.3 ms                                                               | 22.4 ms: 1.17x faster                                    |
| aiohttp                  | 1.39 ms                                                               | 1.19 ms: 1.17x faster                                    |
| genshi_xml               | 69.8 ms                                                               | 60.2 ms: 1.16x faster                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.58 ms: 1.16x faster                                    |
| deepcopy                 | 511 us                                                                | 451 us: 1.13x faster                                     |
| deepcopy_reduce          | 4.60 us                                                               | 4.07 us: 1.13x faster                                    |
| xml_etree_parse          | 212 ms                                                                | 188 ms: 1.13x faster                                     |
| scimark_fft              | 500 ms                                                                | 447 ms: 1.12x faster                                     |
| meteor_contest           | 126 ms                                                                | 113 ms: 1.11x faster                                     |
| mdp                      | 3.70 sec                                                              | 3.36 sec: 1.10x faster                                   |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.09x faster                                     |
| sqlite_synth             | 4.12 us                                                               | 3.84 us: 1.07x faster                                    |
| create_gc_cycles         | 2.26 ms                                                               | 2.12 ms: 1.06x faster                                    |
| xml_etree_iterparse      | 156 ms                                                                | 147 ms: 1.06x faster                                     |
| unpickle_list            | 6.99 us                                                               | 6.65 us: 1.05x faster                                    |
| flaskblogging            | 4.83 ms                                                               | 4.60 ms: 1.05x faster                                    |
| json                     | 5.88 ms                                                               | 5.61 ms: 1.05x faster                                    |
| regex_dna                | 257 ms                                                                | 246 ms: 1.04x faster                                     |
| regex_v8                 | 32.2 ms                                                               | 31.5 ms: 1.02x faster                                    |
| json_loads               | 30.9 us                                                               | 31.4 us: 1.02x slower                                    |
| pickle_list              | 5.24 us                                                               | 5.34 us: 1.02x slower                                    |
| pickle                   | 12.5 us                                                               | 13.5 us: 1.08x slower                                    |
| pickle_dict              | 35.1 us                                                               | 38.1 us: 1.09x slower                                    |
| gc_traversal             | 4.15 ms                                                               | 4.53 ms: 1.09x slower                                    |
| async_generators         | 452 ms                                                                | 496 ms: 1.10x slower                                     |
| regex_effbot             | 4.25 ms                                                               | 4.87 ms: 1.15x slower                                    |
| telco                    | 8.49 ms                                                               | 9.73 ms: 1.15x slower                                    |
| unpickle                 | 17.5 us                                                               | 20.2 us: 1.15x slower                                    |
| coverage                 | 83.6 ms                                                               | 98.5 ms: 1.18x slower                                    |
| python_startup           | 11.2 ms                                                               | 13.3 ms: 1.19x slower                                    |
| mypy2                    | 936 ms                                                                | 1.18 sec: 1.26x slower                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.75 ms: 1.27x slower                                    |
| Geometric mean           | (ref)                                                                 | 1.28x faster                                             |

Benchmark hidden because not significant (2): pidigits, asyncio_websockets
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: dulwich_log, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.14x