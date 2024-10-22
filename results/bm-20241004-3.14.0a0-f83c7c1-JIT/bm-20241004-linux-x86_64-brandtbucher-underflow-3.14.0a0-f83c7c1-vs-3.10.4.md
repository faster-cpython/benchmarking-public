# Results vs. 3.10.4

- fork: brandtbucher
- ref: underflow
- machine: linux-x86_64
- commit hash: f83c7c1
- commit date: 2024-10-04
- overall geometric mean: 1.33x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 291 ms: 1.20x faster                                             |
| docutils       | 3.30 sec                                               | 3.07 sec: 1.07x faster                                           |
| html5lib       | 88.9 ms                                                | 71.3 ms: 1.25x faster                                            |
| tornado_http   | 136 ms                                                 | 102 ms: 1.33x faster                                             |
| Geometric mean | (ref)                                                  | 1.21x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 324 ms: 2.24x faster                                             |
| async_tree_memoization  | 870 ms                                                 | 415 ms: 2.10x faster                                             |
| async_tree_io           | 1.77 sec                                               | 890 ms: 1.99x faster                                             |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 569 ms: 1.79x faster                                             |
| Geometric mean          | (ref)                                                  | 2.02x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 81.5 ms: 1.88x faster                                            |
| float          | 117 ms                                                 | 71.3 ms: 1.64x faster                                            |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                             |
| Geometric mean | (ref)                                                  | 1.47x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 155 ms: 1.22x faster                                             |
| regex_v8       | 27.8 ms                                                | 24.7 ms: 1.12x faster                                            |
| regex_dna      | 227 ms                                                 | 217 ms: 1.05x faster                                             |
| Geometric mean | (ref)                                                  | 1.09x faster                                                     |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 202 us: 1.63x faster                                             |
| pickle_pure_python   | 484 us                                                 | 318 us: 1.52x faster                                             |
| tomli_loads          | 3.14 sec                                               | 2.08 sec: 1.51x faster                                           |
| xml_etree_process    | 79.1 ms                                                | 55.4 ms: 1.43x faster                                            |
| json_dumps           | 14.2 ms                                                | 10.1 ms: 1.41x faster                                            |
| xml_etree_generate   | 99.4 ms                                                | 77.0 ms: 1.29x faster                                            |
| xml_etree_iterparse  | 115 ms                                                 | 97.4 ms: 1.19x faster                                            |
| xml_etree_parse      | 168 ms                                                 | 147 ms: 1.14x faster                                             |
| json_loads           | 31.2 us                                                | 28.3 us: 1.10x faster                                            |
| unpickle             | 14.4 us                                                | 14.6 us: 1.02x slower                                            |
| pickle               | 10.7 us                                                | 11.6 us: 1.09x slower                                            |
| pickle_dict          | 29.6 us                                                | 34.8 us: 1.17x slower                                            |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                     |

Benchmark hidden because not significant (2): unpickle_list, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.38x faster                                            |
| python_startup_no_site | 5.93 ms                                                | 7.07 ms: 1.19x slower                                            |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.86 ms: 1.66x faster                                            |
| genshi_text     | 31.8 ms                                                | 24.3 ms: 1.31x faster                                            |
| django_template | 48.2 ms                                                | 41.1 ms: 1.17x faster                                            |
| genshi_xml      | 66.0 ms                                                | 70.3 ms: 1.06x slower                                            |
| Geometric mean  | (ref)                                                  | 1.24x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.26x faster                                             |
| deltablue                | 7.91 ms                                                | 3.29 ms: 2.41x faster                                            |
| generators               | 80.1 ms                                                | 35.3 ms: 2.27x faster                                            |
| async_tree_none          | 728 ms                                                 | 324 ms: 2.24x faster                                             |
| deepcopy_memo            | 58.5 us                                                | 26.6 us: 2.20x faster                                            |
| async_tree_memoization   | 870 ms                                                 | 415 ms: 2.10x faster                                             |
| richards_super           | 94.7 ms                                                | 46.2 ms: 2.05x faster                                            |
| async_tree_io            | 1.77 sec                                               | 890 ms: 1.99x faster                                             |
| scimark_monte_carlo      | 118 ms                                                 | 60.0 ms: 1.97x faster                                            |
| richards                 | 79.3 ms                                                | 40.6 ms: 1.95x faster                                            |
| chaos                    | 115 ms                                                 | 60.4 ms: 1.91x faster                                            |
| crypto_pyaes             | 128 ms                                                 | 67.0 ms: 1.91x faster                                            |
| nbody                    | 154 ms                                                 | 81.5 ms: 1.88x faster                                            |
| asyncio_tcp              | 922 ms                                                 | 502 ms: 1.84x faster                                             |
| scimark_sor              | 220 ms                                                 | 122 ms: 1.81x faster                                             |
| raytrace                 | 507 ms                                                 | 282 ms: 1.80x faster                                             |
| deepcopy                 | 479 us                                                 | 267 us: 1.80x faster                                             |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 569 ms: 1.79x faster                                             |
| go                       | 240 ms                                                 | 136 ms: 1.76x faster                                             |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.71x faster                                            |
| logging_silent           | 190 ns                                                 | 111 ns: 1.70x faster                                             |
| spectral_norm            | 170 ms                                                 | 102 ms: 1.66x faster                                             |
| mako                     | 16.3 ms                                                | 9.86 ms: 1.66x faster                                            |
| float                    | 117 ms                                                 | 71.3 ms: 1.64x faster                                            |
| unpickle_pure_python     | 331 us                                                 | 202 us: 1.63x faster                                             |
| pyflate                  | 716 ms                                                 | 440 ms: 1.63x faster                                             |
| scimark_lu               | 176 ms                                                 | 112 ms: 1.57x faster                                             |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                            |
| pickle_pure_python       | 484 us                                                 | 318 us: 1.52x faster                                             |
| tomli_loads              | 3.14 sec                                               | 2.08 sec: 1.51x faster                                           |
| coroutines               | 35.1 ms                                                | 23.4 ms: 1.50x faster                                            |
| hexiom                   | 10.4 ms                                                | 6.97 ms: 1.49x faster                                            |
| scimark_fft              | 466 ms                                                 | 313 ms: 1.49x faster                                             |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.44 ms: 1.46x faster                                            |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                           |
| xml_etree_process        | 79.1 ms                                                | 55.4 ms: 1.43x faster                                            |
| sqlglot_parse            | 2.17 ms                                                | 1.54 ms: 1.41x faster                                            |
| sqlglot_transpile        | 2.57 ms                                                | 1.83 ms: 1.41x faster                                            |
| json_dumps               | 14.2 ms                                                | 10.1 ms: 1.41x faster                                            |
| fannkuch                 | 532 ms                                                 | 380 ms: 1.40x faster                                             |
| logging_format           | 9.09 us                                                | 6.52 us: 1.39x faster                                            |
| logging_simple           | 8.30 us                                                | 5.99 us: 1.39x faster                                            |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.38x faster                                            |
| pprint_safe_repr         | 1.02 sec                                               | 738 ms: 1.38x faster                                             |
| pylint                   | 551 ms                                                 | 400 ms: 1.38x faster                                             |
| thrift                   | 1.07 ms                                                | 784 us: 1.37x faster                                             |
| pprint_pformat           | 2.10 sec                                               | 1.56 sec: 1.35x faster                                           |
| tornado_http             | 136 ms                                                 | 102 ms: 1.33x faster                                             |
| genshi_text              | 31.8 ms                                                | 24.3 ms: 1.31x faster                                            |
| pathlib                  | 20.5 ms                                                | 15.7 ms: 1.31x faster                                            |
| xml_etree_generate       | 99.4 ms                                                | 77.0 ms: 1.29x faster                                            |
| html5lib                 | 88.9 ms                                                | 71.3 ms: 1.25x faster                                            |
| nqueens                  | 106 ms                                                 | 85.1 ms: 1.24x faster                                            |
| regex_compile            | 188 ms                                                 | 155 ms: 1.22x faster                                             |
| pycparser                | 1.58 sec                                               | 1.30 sec: 1.21x faster                                           |
| 2to3                     | 348 ms                                                 | 291 ms: 1.20x faster                                             |
| xml_etree_iterparse      | 115 ms                                                 | 97.4 ms: 1.19x faster                                            |
| django_template          | 48.2 ms                                                | 41.1 ms: 1.17x faster                                            |
| dulwich_log              | 84.3 ms                                                | 73.6 ms: 1.15x faster                                            |
| xml_etree_parse          | 168 ms                                                 | 147 ms: 1.14x faster                                             |
| sqlglot_normalize        | 143 ms                                                 | 126 ms: 1.14x faster                                             |
| mdp                      | 2.85 sec                                               | 2.52 sec: 1.13x faster                                           |
| json                     | 5.69 ms                                                | 5.05 ms: 1.13x faster                                            |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.12x faster                                             |
| regex_v8                 | 27.8 ms                                                | 24.7 ms: 1.12x faster                                            |
| sqlite_synth             | 3.02 us                                                | 2.74 us: 1.10x faster                                            |
| json_loads               | 31.2 us                                                | 28.3 us: 1.10x faster                                            |
| bench_thread_pool        | 986 us                                                 | 902 us: 1.09x faster                                             |
| sqlglot_optimize         | 69.2 ms                                                | 63.8 ms: 1.08x faster                                            |
| docutils                 | 3.30 sec                                               | 3.07 sec: 1.07x faster                                           |
| sympy_str                | 346 ms                                                 | 323 ms: 1.07x faster                                             |
| sympy_expand             | 566 ms                                                 | 537 ms: 1.05x faster                                             |
| regex_dna                | 227 ms                                                 | 217 ms: 1.05x faster                                             |
| sympy_sum                | 196 ms                                                 | 191 ms: 1.03x faster                                             |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                             |
| sympy_integrate          | 25.8 ms                                                | 26.1 ms: 1.01x slower                                            |
| unpickle                 | 14.4 us                                                | 14.6 us: 1.02x slower                                            |
| gc_traversal             | 3.62 ms                                                | 3.69 ms: 1.02x slower                                            |
| async_generators         | 444 ms                                                 | 454 ms: 1.02x slower                                             |
| telco                    | 7.27 ms                                                | 7.51 ms: 1.03x slower                                            |
| create_gc_cycles         | 1.62 ms                                                | 1.72 ms: 1.06x slower                                            |
| genshi_xml               | 66.0 ms                                                | 70.3 ms: 1.06x slower                                            |
| coverage                 | 79.4 ms                                                | 86.5 ms: 1.09x slower                                            |
| pickle                   | 10.7 us                                                | 11.6 us: 1.09x slower                                            |
| pickle_dict              | 29.6 us                                                | 34.8 us: 1.17x slower                                            |
| python_startup_no_site   | 5.93 ms                                                | 7.07 ms: 1.19x slower                                            |
| unpack_sequence          | 60.0 ns                                                | 106 ns: 1.77x slower                                             |
| bench_mp_pool            | 24.0 ms                                                | 60.9 ms: 2.54x slower                                            |
| Geometric mean           | (ref)                                                  | 1.33x faster                                                     |

Benchmark hidden because not significant (4): unpickle_list, asyncio_websockets, pickle_list, regex_effbot
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241004-3.14.0a0-f83c7c1-JIT/bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.19x