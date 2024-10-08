# Results vs. 3.10.4

- fork: brandtbucher
- ref: underflow_no_yield
- machine: linux-x86_64
- commit hash: f9222b1
- commit date: 2024-08-26
- overall geometric mean: 1.40x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-linux-x86_64-brandtbucher-underflow_no_yield-3.14.0a0-f9222b1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 277 ms: 1.26x faster                                                      |
| docutils       | 3.30 sec                                               | 3.34 sec: 1.01x slower                                                    |
| html5lib       | 88.9 ms                                                | 69.7 ms: 1.27x faster                                                     |
| tornado_http   | 136 ms                                                 | 102 ms: 1.34x faster                                                      |
| Geometric mean | (ref)                                                  | 1.21x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-linux-x86_64-brandtbucher-underflow_no_yield-3.14.0a0-f9222b1 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 326 ms: 2.24x faster                                                      |
| async_tree_memoization  | 870 ms                                                 | 410 ms: 2.12x faster                                                      |
| async_tree_io           | 1.77 sec                                               | 938 ms: 1.89x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 563 ms: 1.80x faster                                                      |
| Geometric mean          | (ref)                                                  | 2.01x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-linux-x86_64-brandtbucher-underflow_no_yield-3.14.0a0-f9222b1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.8 ms: 1.90x faster                                                     |
| float          | 117 ms                                                 | 71.2 ms: 1.64x faster                                                     |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                  | 1.48x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-linux-x86_64-brandtbucher-underflow_no_yield-3.14.0a0-f9222b1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 150 ms: 1.26x faster                                                      |
| regex_v8       | 27.8 ms                                                | 24.7 ms: 1.13x faster                                                     |
| regex_dna      | 227 ms                                                 | 213 ms: 1.07x faster                                                      |
| Geometric mean | (ref)                                                  | 1.11x faster                                                              |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-linux-x86_64-brandtbucher-underflow_no_yield-3.14.0a0-f9222b1 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 197 us: 1.68x faster                                                      |
| pickle_pure_python   | 484 us                                                 | 313 us: 1.55x faster                                                      |
| tomli_loads          | 3.14 sec                                               | 2.06 sec: 1.53x faster                                                    |
| xml_etree_process    | 79.1 ms                                                | 54.5 ms: 1.45x faster                                                     |
| json_dumps           | 14.2 ms                                                | 9.91 ms: 1.43x faster                                                     |
| xml_etree_generate   | 99.4 ms                                                | 77.5 ms: 1.28x faster                                                     |
| xml_etree_iterparse  | 115 ms                                                 | 98.3 ms: 1.17x faster                                                     |
| xml_etree_parse      | 168 ms                                                 | 145 ms: 1.16x faster                                                      |
| json_loads           | 31.2 us                                                | 29.6 us: 1.05x faster                                                     |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-linux-x86_64-brandtbucher-underflow_no_yield-3.14.0a0-f9222b1 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                     |
| python_startup_no_site | 5.93 ms                                                | 7.14 ms: 1.20x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-linux-x86_64-brandtbucher-underflow_no_yield-3.14.0a0-f9222b1 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.76 ms: 1.67x faster                                                     |
| django_template | 48.2 ms                                                | 38.5 ms: 1.25x faster                                                     |
| genshi_text     | 31.8 ms                                                | 25.5 ms: 1.25x faster                                                     |
| genshi_xml      | 66.0 ms                                                | 60.4 ms: 1.09x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.30x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-linux-x86_64-brandtbucher-underflow_no_yield-3.14.0a0-f9222b1 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.26x faster                                                      |
| deltablue                | 7.91 ms                                                | 3.24 ms: 2.44x faster                                                     |
| generators               | 80.1 ms                                                | 33.4 ms: 2.40x faster                                                     |
| async_tree_none          | 728 ms                                                 | 326 ms: 2.24x faster                                                      |
| deepcopy_memo            | 58.5 us                                                | 26.4 us: 2.21x faster                                                     |
| richards_super           | 94.7 ms                                                | 42.8 ms: 2.21x faster                                                     |
| async_tree_memoization   | 870 ms                                                 | 410 ms: 2.12x faster                                                      |
| richards                 | 79.3 ms                                                | 38.3 ms: 2.07x faster                                                     |
| scimark_monte_carlo      | 118 ms                                                 | 58.9 ms: 2.01x faster                                                     |
| chaos                    | 115 ms                                                 | 58.3 ms: 1.98x faster                                                     |
| crypto_pyaes             | 128 ms                                                 | 65.7 ms: 1.94x faster                                                     |
| logging_silent           | 190 ns                                                 | 99.5 ns: 1.91x faster                                                     |
| nbody                    | 154 ms                                                 | 80.8 ms: 1.90x faster                                                     |
| async_tree_io            | 1.77 sec                                               | 938 ms: 1.89x faster                                                      |
| raytrace                 | 507 ms                                                 | 274 ms: 1.85x faster                                                      |
| deepcopy                 | 479 us                                                 | 265 us: 1.81x faster                                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 563 ms: 1.80x faster                                                      |
| asyncio_tcp              | 922 ms                                                 | 513 ms: 1.80x faster                                                      |
| scimark_sor              | 220 ms                                                 | 123 ms: 1.79x faster                                                      |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.71x faster                                                     |
| unpickle_pure_python     | 331 us                                                 | 197 us: 1.68x faster                                                      |
| mako                     | 16.3 ms                                                | 9.76 ms: 1.67x faster                                                     |
| spectral_norm            | 170 ms                                                 | 103 ms: 1.65x faster                                                      |
| float                    | 117 ms                                                 | 71.2 ms: 1.64x faster                                                     |
| scimark_lu               | 176 ms                                                 | 111 ms: 1.58x faster                                                      |
| deepcopy_reduce          | 4.17 us                                                | 2.65 us: 1.58x faster                                                     |
| pyflate                  | 716 ms                                                 | 458 ms: 1.56x faster                                                      |
| coroutines               | 35.1 ms                                                | 22.7 ms: 1.55x faster                                                     |
| pickle_pure_python       | 484 us                                                 | 313 us: 1.55x faster                                                      |
| tomli_loads              | 3.14 sec                                               | 2.06 sec: 1.53x faster                                                    |
| hexiom                   | 10.4 ms                                                | 6.85 ms: 1.52x faster                                                     |
| scimark_fft              | 466 ms                                                 | 308 ms: 1.51x faster                                                      |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.30 ms: 1.51x faster                                                     |
| xml_etree_process        | 79.1 ms                                                | 54.5 ms: 1.45x faster                                                     |
| sqlglot_transpile        | 2.57 ms                                                | 1.78 ms: 1.45x faster                                                     |
| json_dumps               | 14.2 ms                                                | 9.91 ms: 1.43x faster                                                     |
| sqlglot_parse            | 2.17 ms                                                | 1.52 ms: 1.43x faster                                                     |
| fannkuch                 | 532 ms                                                 | 372 ms: 1.43x faster                                                      |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                                    |
| go                       | 240 ms                                                 | 170 ms: 1.41x faster                                                      |
| logging_simple           | 8.30 us                                                | 5.90 us: 1.41x faster                                                     |
| logging_format           | 9.09 us                                                | 6.47 us: 1.40x faster                                                     |
| pprint_safe_repr         | 1.02 sec                                               | 728 ms: 1.40x faster                                                      |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                     |
| thrift                   | 1.07 ms                                                | 781 us: 1.37x faster                                                      |
| pprint_pformat           | 2.10 sec                                               | 1.53 sec: 1.37x faster                                                    |
| pylint                   | 551 ms                                                 | 406 ms: 1.36x faster                                                      |
| tornado_http             | 136 ms                                                 | 102 ms: 1.34x faster                                                      |
| pathlib                  | 20.5 ms                                                | 15.8 ms: 1.30x faster                                                     |
| xml_etree_generate       | 99.4 ms                                                | 77.5 ms: 1.28x faster                                                     |
| html5lib                 | 88.9 ms                                                | 69.7 ms: 1.27x faster                                                     |
| 2to3                     | 348 ms                                                 | 277 ms: 1.26x faster                                                      |
| regex_compile            | 188 ms                                                 | 150 ms: 1.26x faster                                                      |
| django_template          | 48.2 ms                                                | 38.5 ms: 1.25x faster                                                     |
| genshi_text              | 31.8 ms                                                | 25.5 ms: 1.25x faster                                                     |
| pycparser                | 1.58 sec                                               | 1.27 sec: 1.25x faster                                                    |
| nqueens                  | 106 ms                                                 | 86.2 ms: 1.23x faster                                                     |
| bench_thread_pool        | 986 us                                                 | 826 us: 1.19x faster                                                      |
| sqlglot_normalize        | 143 ms                                                 | 120 ms: 1.19x faster                                                      |
| xml_etree_iterparse      | 115 ms                                                 | 98.3 ms: 1.17x faster                                                     |
| xml_etree_parse          | 168 ms                                                 | 145 ms: 1.16x faster                                                      |
| sqlglot_optimize         | 69.2 ms                                                | 60.4 ms: 1.15x faster                                                     |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                      |
| regex_v8                 | 27.8 ms                                                | 24.7 ms: 1.13x faster                                                     |
| genshi_xml               | 66.0 ms                                                | 60.4 ms: 1.09x faster                                                     |
| json                     | 5.69 ms                                                | 5.26 ms: 1.08x faster                                                     |
| sympy_str                | 346 ms                                                 | 321 ms: 1.08x faster                                                      |
| regex_dna                | 227 ms                                                 | 213 ms: 1.07x faster                                                      |
| sympy_expand             | 566 ms                                                 | 536 ms: 1.06x faster                                                      |
| json_loads               | 31.2 us                                                | 29.6 us: 1.05x faster                                                     |
| mdp                      | 2.85 sec                                               | 2.73 sec: 1.04x faster                                                    |
| sympy_sum                | 196 ms                                                 | 189 ms: 1.04x faster                                                      |
| sympy_integrate          | 25.8 ms                                                | 24.9 ms: 1.04x faster                                                     |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                                      |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                      |
| gc_traversal             | 3.62 ms                                                | 3.66 ms: 1.01x slower                                                     |
| docutils                 | 3.30 sec                                               | 3.34 sec: 1.01x slower                                                    |
| async_generators         | 444 ms                                                 | 459 ms: 1.04x slower                                                      |
| telco                    | 7.27 ms                                                | 7.63 ms: 1.05x slower                                                     |
| coverage                 | 79.4 ms                                                | 86.0 ms: 1.08x slower                                                     |
| create_gc_cycles         | 1.62 ms                                                | 1.78 ms: 1.10x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 7.14 ms: 1.20x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                              |

Benchmark hidden because not significant (2): regex_effbot, bench_mp_pool
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240826-3.14.0a0-f9222b1-JIT/bm-20240826-linux-x86_64-brandtbucher-underflow_no_yield-3.14.0a0-f9222b1.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.22x