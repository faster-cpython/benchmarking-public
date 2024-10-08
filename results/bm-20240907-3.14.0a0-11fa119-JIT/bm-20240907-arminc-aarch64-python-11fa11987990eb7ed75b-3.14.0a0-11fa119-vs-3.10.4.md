# Results vs. 3.10.4

- fork: python
- ref: 11fa11987990eb7ed75b
- machine: linux-aarch64
- commit hash: 11fa119
- commit date: 2024-09-07
- overall geometric mean: 1.18x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 3.53 sec                                                              | 3.94 sec: 1.12x slower                                                  |
| html5lib       | 86.5 ms                                                               | 70.2 ms: 1.23x faster                                                   |
| tornado_http   | 178 ms                                                                | 147 ms: 1.21x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.08x faster                                                            |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 457 ms: 2.08x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 570 ms: 1.99x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 1.18 sec: 1.93x faster                                                  |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 748 ms: 1.70x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.92x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 89.1 ms: 1.51x faster                                                   |
| nbody          | 166 ms                                                                | 114 ms: 1.45x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 31.1 ms: 1.03x faster                                                   |
| regex_dna      | 257 ms                                                                | 254 ms: 1.01x faster                                                    |
| regex_compile  | 177 ms                                                                | 188 ms: 1.07x slower                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.94 ms: 1.16x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 265 us: 1.38x faster                                                    |
| pickle_pure_python   | 529 us                                                                | 393 us: 1.35x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.61 sec: 1.29x faster                                                  |
| xml_etree_process    | 99.5 ms                                                               | 78.7 ms: 1.26x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 13.5 ms: 1.24x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 187 ms: 1.13x faster                                                    |
| unpickle_list        | 6.99 us                                                               | 6.26 us: 1.12x faster                                                   |
| xml_etree_generate   | 123 ms                                                                | 111 ms: 1.11x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 148 ms: 1.05x faster                                                    |
| pickle_list          | 5.24 us                                                               | 5.28 us: 1.01x slower                                                   |
| json_loads           | 30.9 us                                                               | 32.5 us: 1.05x slower                                                   |
| pickle_dict          | 35.1 us                                                               | 37.5 us: 1.07x slower                                                   |
| pickle               | 12.5 us                                                               | 13.7 us: 1.10x slower                                                   |
| unpickle             | 17.5 us                                                               | 19.7 us: 1.13x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.10x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.2 ms: 1.18x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 8.90 ms: 1.29x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.23x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.2 ms: 1.43x faster                                                   |
| django_template | 53.3 ms                                                               | 51.4 ms: 1.04x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 34.1 ms: 1.03x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 80.1 ms: 1.15x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.08x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 214 us: 3.09x faster                                                    |
| async_tree_none          | 950 ms                                                                | 457 ms: 2.08x faster                                                    |
| deltablue                | 8.94 ms                                                               | 4.34 ms: 2.06x faster                                                   |
| async_tree_memoization   | 1.13 sec                                                              | 570 ms: 1.99x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.18 sec: 1.93x faster                                                  |
| bench_mp_pool            | 14.5 ms                                                               | 7.82 ms: 1.86x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 748 ms: 1.70x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 37.3 us: 1.66x faster                                                   |
| scimark_sor              | 246 ms                                                                | 150 ms: 1.64x faster                                                    |
| raytrace                 | 573 ms                                                                | 352 ms: 1.63x faster                                                    |
| logging_silent           | 222 ns                                                                | 137 ns: 1.62x faster                                                    |
| float                    | 135 ms                                                                | 89.1 ms: 1.51x faster                                                   |
| asyncio_tcp              | 944 ms                                                                | 625 ms: 1.51x faster                                                    |
| scimark_lu               | 227 ms                                                                | 151 ms: 1.51x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 89.3 ms: 1.50x faster                                                   |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.25 sec: 1.46x faster                                                  |
| nbody                    | 166 ms                                                                | 114 ms: 1.45x faster                                                    |
| richards_super           | 107 ms                                                                | 75.0 ms: 1.43x faster                                                   |
| mako                     | 18.9 ms                                                               | 13.2 ms: 1.43x faster                                                   |
| go                       | 264 ms                                                                | 188 ms: 1.40x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.73 ms: 1.39x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 265 us: 1.38x faster                                                    |
| richards                 | 91.7 ms                                                               | 66.8 ms: 1.37x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 93.7 ms: 1.36x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 393 us: 1.35x faster                                                    |
| comprehensions           | 33.1 us                                                               | 24.6 us: 1.35x faster                                                   |
| chaos                    | 121 ms                                                                | 91.4 ms: 1.32x faster                                                   |
| logging_simple           | 9.78 us                                                               | 7.42 us: 1.32x faster                                                   |
| deepcopy                 | 511 us                                                                | 388 us: 1.32x faster                                                    |
| logging_format           | 10.6 us                                                               | 8.09 us: 1.31x faster                                                   |
| coroutines               | 37.2 ms                                                               | 28.6 ms: 1.30x faster                                                   |
| sqlglot_transpile        | 2.84 ms                                                               | 2.19 ms: 1.30x faster                                                   |
| thrift                   | 1.26 ms                                                               | 971 us: 1.30x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.61 sec: 1.29x faster                                                  |
| spectral_norm            | 186 ms                                                                | 146 ms: 1.28x faster                                                    |
| pyflate                  | 795 ms                                                                | 627 ms: 1.27x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 78.7 ms: 1.26x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 13.5 ms: 1.24x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 70.2 ms: 1.23x faster                                                   |
| tornado_http             | 178 ms                                                                | 147 ms: 1.21x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.80 us: 1.21x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.32 ms: 1.21x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 22.0 ms: 1.20x faster                                                   |
| generators               | 68.1 ms                                                               | 57.3 ms: 1.19x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 187 ms: 1.13x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.49 sec: 1.13x faster                                                  |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.82 ms: 1.12x faster                                                   |
| unpickle_list            | 6.99 us                                                               | 6.26 us: 1.12x faster                                                   |
| xml_etree_generate       | 123 ms                                                                | 111 ms: 1.11x faster                                                    |
| scimark_fft              | 500 ms                                                                | 460 ms: 1.09x faster                                                    |
| fannkuch                 | 546 ms                                                                | 504 ms: 1.08x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 10.2 ms: 1.07x faster                                                   |
| mdp                      | 3.70 sec                                                              | 3.47 sec: 1.07x faster                                                  |
| sqlite_synth             | 4.12 us                                                               | 3.89 us: 1.06x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 148 ms: 1.05x faster                                                    |
| sqlglot_normalize        | 156 ms                                                                | 149 ms: 1.05x faster                                                    |
| django_template          | 53.3 ms                                                               | 51.4 ms: 1.04x faster                                                   |
| regex_v8                 | 32.2 ms                                                               | 31.1 ms: 1.03x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 34.1 ms: 1.03x faster                                                   |
| meteor_contest           | 126 ms                                                                | 124 ms: 1.02x faster                                                    |
| regex_dna                | 257 ms                                                                | 254 ms: 1.01x faster                                                    |
| pickle_list              | 5.24 us                                                               | 5.28 us: 1.01x slower                                                   |
| sqlglot_optimize         | 75.4 ms                                                               | 77.4 ms: 1.03x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 2.33 ms: 1.03x slower                                                   |
| json_loads               | 30.9 us                                                               | 32.5 us: 1.05x slower                                                   |
| nqueens                  | 117 ms                                                                | 124 ms: 1.05x slower                                                    |
| dulwich_log              | 73.5 ms                                                               | 77.7 ms: 1.06x slower                                                   |
| regex_compile            | 177 ms                                                                | 188 ms: 1.07x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 37.5 us: 1.07x slower                                                   |
| sympy_integrate          | 26.5 ms                                                               | 28.5 ms: 1.08x slower                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 1.25 sec: 1.09x slower                                                  |
| pickle                   | 12.5 us                                                               | 13.7 us: 1.10x slower                                                   |
| pprint_pformat           | 2.36 sec                                                              | 2.59 sec: 1.10x slower                                                  |
| async_generators         | 452 ms                                                                | 504 ms: 1.11x slower                                                    |
| sympy_str                | 329 ms                                                                | 366 ms: 1.11x slower                                                    |
| docutils                 | 3.53 sec                                                              | 3.94 sec: 1.12x slower                                                  |
| sympy_expand             | 543 ms                                                                | 606 ms: 1.12x slower                                                    |
| unpickle                 | 17.5 us                                                               | 19.7 us: 1.13x slower                                                   |
| genshi_xml               | 69.8 ms                                                               | 80.1 ms: 1.15x slower                                                   |
| sympy_sum                | 184 ms                                                                | 214 ms: 1.16x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.94 ms: 1.16x slower                                                   |
| python_startup           | 11.2 ms                                                               | 13.2 ms: 1.18x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 4.93 ms: 1.19x slower                                                   |
| coverage                 | 83.6 ms                                                               | 99.8 ms: 1.19x slower                                                   |
| telco                    | 8.49 ms                                                               | 10.4 ms: 1.22x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.90 ms: 1.29x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.18x faster                                                            |

Benchmark hidden because not significant (5): pylint, 2to3, pidigits, json, asyncio_websockets
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240907-3.14.0a0-11fa119-JIT/bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.25x