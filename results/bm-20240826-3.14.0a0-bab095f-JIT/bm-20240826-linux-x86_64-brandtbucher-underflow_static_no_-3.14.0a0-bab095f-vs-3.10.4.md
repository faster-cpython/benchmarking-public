# Results vs. 3.10.4

- fork: brandtbucher
- ref: underflow_static_no_
- machine: linux-x86_64
- commit hash: bab095f
- commit date: 2024-08-26
- overall geometric mean: 1.40x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.24x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 283 ms: 1.23x faster                                                        |
| docutils       | 3.30 sec                                               | 3.35 sec: 1.02x slower                                                      |
| html5lib       | 88.9 ms                                                | 71.2 ms: 1.25x faster                                                       |
| tornado_http   | 136 ms                                                 | 102 ms: 1.33x faster                                                        |
| Geometric mean | (ref)                                                  | 1.19x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 325 ms: 2.24x faster                                                        |
| async_tree_memoization  | 870 ms                                                 | 396 ms: 2.20x faster                                                        |
| async_tree_io           | 1.77 sec                                               | 939 ms: 1.88x faster                                                        |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 556 ms: 1.83x faster                                                        |
| Geometric mean          | (ref)                                                  | 2.03x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 81.7 ms: 1.88x faster                                                       |
| float          | 117 ms                                                 | 70.9 ms: 1.65x faster                                                       |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                  | 1.47x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 151 ms: 1.25x faster                                                        |
| regex_v8       | 27.8 ms                                                | 24.5 ms: 1.13x faster                                                       |
| regex_dna      | 227 ms                                                 | 218 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 205 us: 1.61x faster                                                        |
| tomli_loads          | 3.14 sec                                               | 1.99 sec: 1.58x faster                                                      |
| pickle_pure_python   | 484 us                                                 | 314 us: 1.54x faster                                                        |
| xml_etree_process    | 79.1 ms                                                | 54.1 ms: 1.46x faster                                                       |
| json_dumps           | 14.2 ms                                                | 9.96 ms: 1.42x faster                                                       |
| xml_etree_generate   | 99.4 ms                                                | 77.1 ms: 1.29x faster                                                       |
| xml_etree_iterparse  | 115 ms                                                 | 98.8 ms: 1.17x faster                                                       |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                                        |
| json_loads           | 31.2 us                                                | 28.4 us: 1.10x faster                                                       |
| Geometric mean       | (ref)                                                  | 1.36x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                       |
| python_startup_no_site | 5.93 ms                                                | 7.18 ms: 1.21x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.60 ms: 1.70x faster                                                       |
| django_template | 48.2 ms                                                | 37.2 ms: 1.29x faster                                                       |
| genshi_text     | 31.8 ms                                                | 24.8 ms: 1.28x faster                                                       |
| genshi_xml      | 66.0 ms                                                | 58.8 ms: 1.12x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.33x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.33x faster                                                        |
| deltablue                | 7.91 ms                                                | 3.26 ms: 2.42x faster                                                       |
| deepcopy_memo            | 58.5 us                                                | 25.7 us: 2.28x faster                                                       |
| async_tree_none          | 728 ms                                                 | 325 ms: 2.24x faster                                                        |
| async_tree_memoization   | 870 ms                                                 | 396 ms: 2.20x faster                                                        |
| richards_super           | 94.7 ms                                                | 43.2 ms: 2.19x faster                                                       |
| richards                 | 79.3 ms                                                | 37.7 ms: 2.10x faster                                                       |
| crypto_pyaes             | 128 ms                                                 | 65.5 ms: 1.95x faster                                                       |
| generators               | 80.1 ms                                                | 41.1 ms: 1.95x faster                                                       |
| scimark_sor              | 220 ms                                                 | 116 ms: 1.89x faster                                                        |
| chaos                    | 115 ms                                                 | 61.2 ms: 1.89x faster                                                       |
| async_tree_io            | 1.77 sec                                               | 939 ms: 1.88x faster                                                        |
| nbody                    | 154 ms                                                 | 81.7 ms: 1.88x faster                                                       |
| logging_silent           | 190 ns                                                 | 102 ns: 1.85x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 556 ms: 1.83x faster                                                        |
| scimark_monte_carlo      | 118 ms                                                 | 65.2 ms: 1.81x faster                                                       |
| raytrace                 | 507 ms                                                 | 280 ms: 1.81x faster                                                        |
| asyncio_tcp              | 922 ms                                                 | 522 ms: 1.77x faster                                                        |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                                       |
| deepcopy                 | 479 us                                                 | 278 us: 1.72x faster                                                        |
| spectral_norm            | 170 ms                                                 | 99.5 ms: 1.71x faster                                                       |
| mako                     | 16.3 ms                                                | 9.60 ms: 1.70x faster                                                       |
| float                    | 117 ms                                                 | 70.9 ms: 1.65x faster                                                       |
| pyflate                  | 716 ms                                                 | 442 ms: 1.62x faster                                                        |
| unpickle_pure_python     | 331 us                                                 | 205 us: 1.61x faster                                                        |
| scimark_lu               | 176 ms                                                 | 110 ms: 1.60x faster                                                        |
| tomli_loads              | 3.14 sec                                               | 1.99 sec: 1.58x faster                                                      |
| coroutines               | 35.1 ms                                                | 22.7 ms: 1.54x faster                                                       |
| pickle_pure_python       | 484 us                                                 | 314 us: 1.54x faster                                                        |
| deepcopy_reduce          | 4.17 us                                                | 2.71 us: 1.54x faster                                                       |
| hexiom                   | 10.4 ms                                                | 6.92 ms: 1.50x faster                                                       |
| logging_simple           | 8.30 us                                                | 5.54 us: 1.50x faster                                                       |
| scimark_fft              | 466 ms                                                 | 311 ms: 1.50x faster                                                        |
| logging_format           | 9.09 us                                                | 6.19 us: 1.47x faster                                                       |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.42 ms: 1.47x faster                                                       |
| xml_etree_process        | 79.1 ms                                                | 54.1 ms: 1.46x faster                                                       |
| fannkuch                 | 532 ms                                                 | 373 ms: 1.43x faster                                                        |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                                      |
| json_dumps               | 14.2 ms                                                | 9.96 ms: 1.42x faster                                                       |
| sqlglot_parse            | 2.17 ms                                                | 1.53 ms: 1.41x faster                                                       |
| pprint_safe_repr         | 1.02 sec                                               | 729 ms: 1.40x faster                                                        |
| go                       | 240 ms                                                 | 173 ms: 1.39x faster                                                        |
| pprint_pformat           | 2.10 sec                                               | 1.52 sec: 1.38x faster                                                      |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                       |
| thrift                   | 1.07 ms                                                | 779 us: 1.38x faster                                                        |
| sqlglot_transpile        | 2.57 ms                                                | 1.88 ms: 1.37x faster                                                       |
| pylint                   | 551 ms                                                 | 412 ms: 1.34x faster                                                        |
| tornado_http             | 136 ms                                                 | 102 ms: 1.33x faster                                                        |
| pycparser                | 1.58 sec                                               | 1.19 sec: 1.32x faster                                                      |
| pathlib                  | 20.5 ms                                                | 15.6 ms: 1.31x faster                                                       |
| django_template          | 48.2 ms                                                | 37.2 ms: 1.29x faster                                                       |
| xml_etree_generate       | 99.4 ms                                                | 77.1 ms: 1.29x faster                                                       |
| genshi_text              | 31.8 ms                                                | 24.8 ms: 1.28x faster                                                       |
| nqueens                  | 106 ms                                                 | 84.4 ms: 1.25x faster                                                       |
| regex_compile            | 188 ms                                                 | 151 ms: 1.25x faster                                                        |
| html5lib                 | 88.9 ms                                                | 71.2 ms: 1.25x faster                                                       |
| 2to3                     | 348 ms                                                 | 283 ms: 1.23x faster                                                        |
| sqlglot_normalize        | 143 ms                                                 | 120 ms: 1.19x faster                                                        |
| xml_etree_iterparse      | 115 ms                                                 | 98.8 ms: 1.17x faster                                                       |
| bench_thread_pool        | 986 us                                                 | 844 us: 1.17x faster                                                        |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                                        |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.14x faster                                                        |
| regex_v8                 | 27.8 ms                                                | 24.5 ms: 1.13x faster                                                       |
| sqlglot_optimize         | 69.2 ms                                                | 61.1 ms: 1.13x faster                                                       |
| genshi_xml               | 66.0 ms                                                | 58.8 ms: 1.12x faster                                                       |
| json_loads               | 31.2 us                                                | 28.4 us: 1.10x faster                                                       |
| sympy_expand             | 566 ms                                                 | 523 ms: 1.08x faster                                                        |
| json                     | 5.69 ms                                                | 5.29 ms: 1.08x faster                                                       |
| sympy_str                | 346 ms                                                 | 328 ms: 1.06x faster                                                        |
| sympy_integrate          | 25.8 ms                                                | 24.5 ms: 1.05x faster                                                       |
| mdp                      | 2.85 sec                                               | 2.73 sec: 1.04x faster                                                      |
| regex_dna                | 227 ms                                                 | 218 ms: 1.04x faster                                                        |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                        |
| sympy_sum                | 196 ms                                                 | 194 ms: 1.01x faster                                                        |
| asyncio_websockets       | 559 ms                                                 | 556 ms: 1.01x faster                                                        |
| gc_traversal             | 3.62 ms                                                | 3.66 ms: 1.01x slower                                                       |
| docutils                 | 3.30 sec                                               | 3.35 sec: 1.02x slower                                                      |
| async_generators         | 444 ms                                                 | 460 ms: 1.04x slower                                                        |
| telco                    | 7.27 ms                                                | 7.70 ms: 1.06x slower                                                       |
| coverage                 | 79.4 ms                                                | 85.6 ms: 1.08x slower                                                       |
| create_gc_cycles         | 1.62 ms                                                | 1.78 ms: 1.10x slower                                                       |
| python_startup_no_site   | 5.93 ms                                                | 7.18 ms: 1.21x slower                                                       |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                                |

Benchmark hidden because not significant (2): regex_effbot, bench_mp_pool
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240826-3.14.0a0-bab095f-JIT/bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.24x