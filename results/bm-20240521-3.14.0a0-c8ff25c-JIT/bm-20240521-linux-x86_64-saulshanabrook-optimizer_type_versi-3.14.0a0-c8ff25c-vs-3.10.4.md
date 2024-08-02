# Results vs. 3.10.4

- fork: saulshanabrook
- ref: optimizer_type_versi
- machine: linux-x86_64
- commit hash: c8ff25c
- commit date: 2024-05-21
- overall geometric mean: 1.34x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240521-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-c8ff25c |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 278 ms: 1.25x faster                                                          |
| chameleon      | 9.68 ms                                                | 7.04 ms: 1.38x faster                                                         |
| docutils       | 3.30 sec                                               | 2.93 sec: 1.12x faster                                                        |
| html5lib       | 88.9 ms                                                | 66.3 ms: 1.34x faster                                                         |
| tornado_http   | 136 ms                                                 | 97.0 ms: 1.41x faster                                                         |
| Geometric mean | (ref)                                                  | 1.30x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240521-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-c8ff25c |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 378 ms: 1.93x faster                                                          |
| async_tree_memoization  | 870 ms                                                 | 456 ms: 1.91x faster                                                          |
| async_tree_io           | 1.77 sec                                               | 937 ms: 1.89x faster                                                          |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 609 ms: 1.67x faster                                                          |
| Geometric mean          | (ref)                                                  | 1.84x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240521-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-c8ff25c |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 81.6 ms: 1.88x faster                                                         |
| float          | 117 ms                                                 | 72.6 ms: 1.61x faster                                                         |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                                          |
| Geometric mean | (ref)                                                  | 1.46x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240521-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-c8ff25c |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 138 ms: 1.36x faster                                                          |
| regex_v8       | 27.8 ms                                                | 24.5 ms: 1.13x faster                                                         |
| regex_dna      | 227 ms                                                 | 231 ms: 1.02x slower                                                          |
| regex_effbot   | 3.63 ms                                                | 3.71 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240521-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-c8ff25c |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                        |
| pickle_pure_python   | 484 us                                                 | 302 us: 1.61x faster                                                          |
| unpickle_pure_python | 331 us                                                 | 222 us: 1.49x faster                                                          |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.37x faster                                                         |
| xml_etree_process    | 79.1 ms                                                | 58.3 ms: 1.36x faster                                                         |
| xml_etree_generate   | 99.4 ms                                                | 82.4 ms: 1.21x faster                                                         |
| xml_etree_iterparse  | 115 ms                                                 | 101 ms: 1.14x faster                                                          |
| xml_etree_parse      | 168 ms                                                 | 152 ms: 1.11x faster                                                          |
| json_loads           | 31.2 us                                                | 28.6 us: 1.09x faster                                                         |
| pickle_list          | 5.08 us                                                | 5.10 us: 1.00x slower                                                         |
| unpickle_list        | 5.20 us                                                | 5.37 us: 1.03x slower                                                         |
| unpickle             | 14.4 us                                                | 15.4 us: 1.07x slower                                                         |
| pickle               | 10.7 us                                                | 11.7 us: 1.10x slower                                                         |
| pickle_dict          | 29.6 us                                                | 36.3 us: 1.23x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240521-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-c8ff25c |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.9 ms: 1.34x faster                                                         |
| python_startup_no_site | 5.93 ms                                                | 7.59 ms: 1.28x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240521-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-c8ff25c |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.1 ms: 1.61x faster                                                         |
| django_template | 48.2 ms                                                | 36.2 ms: 1.33x faster                                                         |
| genshi_text     | 31.8 ms                                                | 24.9 ms: 1.28x faster                                                         |
| genshi_xml      | 66.0 ms                                                | 58.0 ms: 1.14x faster                                                         |
| Geometric mean  | (ref)                                                  | 1.33x faster                                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240521-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-c8ff25c |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 172 us: 3.17x faster                                                          |
| generators               | 80.1 ms                                                | 36.3 ms: 2.21x faster                                                         |
| deltablue                | 7.91 ms                                                | 3.75 ms: 2.11x faster                                                         |
| richards_super           | 94.7 ms                                                | 48.0 ms: 1.97x faster                                                         |
| async_tree_none          | 728 ms                                                 | 378 ms: 1.93x faster                                                          |
| chaos                    | 115 ms                                                 | 60.5 ms: 1.91x faster                                                         |
| async_tree_memoization   | 870 ms                                                 | 456 ms: 1.91x faster                                                          |
| scimark_monte_carlo      | 118 ms                                                 | 62.1 ms: 1.90x faster                                                         |
| richards                 | 79.3 ms                                                | 41.8 ms: 1.89x faster                                                         |
| async_tree_io            | 1.77 sec                                               | 937 ms: 1.89x faster                                                          |
| crypto_pyaes             | 128 ms                                                 | 67.8 ms: 1.88x faster                                                         |
| nbody                    | 154 ms                                                 | 81.6 ms: 1.88x faster                                                         |
| raytrace                 | 507 ms                                                 | 280 ms: 1.81x faster                                                          |
| logging_silent           | 190 ns                                                 | 107 ns: 1.78x faster                                                          |
| asyncio_tcp              | 922 ms                                                 | 520 ms: 1.77x faster                                                          |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                                         |
| spectral_norm            | 170 ms                                                 | 100.0 ms: 1.70x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 609 ms: 1.67x faster                                                          |
| sqlglot_parse            | 2.17 ms                                                | 1.30 ms: 1.66x faster                                                         |
| float                    | 117 ms                                                 | 72.6 ms: 1.61x faster                                                         |
| tomli_loads              | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                        |
| mako                     | 16.3 ms                                                | 10.1 ms: 1.61x faster                                                         |
| go                       | 240 ms                                                 | 149 ms: 1.61x faster                                                          |
| pickle_pure_python       | 484 us                                                 | 302 us: 1.61x faster                                                          |
| scimark_sor              | 220 ms                                                 | 138 ms: 1.59x faster                                                          |
| pyflate                  | 716 ms                                                 | 453 ms: 1.58x faster                                                          |
| sqlglot_transpile        | 2.57 ms                                                | 1.64 ms: 1.57x faster                                                         |
| pylint                   | 551 ms                                                 | 354 ms: 1.56x faster                                                          |
| deepcopy_memo            | 58.5 us                                                | 37.7 us: 1.55x faster                                                         |
| coroutines               | 35.1 ms                                                | 22.9 ms: 1.53x faster                                                         |
| fannkuch                 | 532 ms                                                 | 356 ms: 1.49x faster                                                          |
| scimark_fft              | 466 ms                                                 | 313 ms: 1.49x faster                                                          |
| unpickle_pure_python     | 331 us                                                 | 222 us: 1.49x faster                                                          |
| pprint_pformat           | 2.10 sec                                               | 1.44 sec: 1.46x faster                                                        |
| logging_simple           | 8.30 us                                                | 5.70 us: 1.46x faster                                                         |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.45 ms: 1.45x faster                                                         |
| pprint_safe_repr         | 1.02 sec                                               | 702 ms: 1.45x faster                                                          |
| scimark_lu               | 176 ms                                                 | 123 ms: 1.43x faster                                                          |
| logging_format           | 9.09 us                                                | 6.40 us: 1.42x faster                                                         |
| tornado_http             | 136 ms                                                 | 97.0 ms: 1.41x faster                                                         |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.85 sec: 1.39x faster                                                        |
| chameleon                | 9.68 ms                                                | 7.04 ms: 1.38x faster                                                         |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.37x faster                                                         |
| regex_compile            | 188 ms                                                 | 138 ms: 1.36x faster                                                          |
| xml_etree_process        | 79.1 ms                                                | 58.3 ms: 1.36x faster                                                         |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                                        |
| python_startup           | 14.6 ms                                                | 10.9 ms: 1.34x faster                                                         |
| html5lib                 | 88.9 ms                                                | 66.3 ms: 1.34x faster                                                         |
| django_template          | 48.2 ms                                                | 36.2 ms: 1.33x faster                                                         |
| thrift                   | 1.07 ms                                                | 816 us: 1.31x faster                                                          |
| genshi_text              | 31.8 ms                                                | 24.9 ms: 1.28x faster                                                         |
| deepcopy                 | 479 us                                                 | 375 us: 1.28x faster                                                          |
| deepcopy_reduce          | 4.17 us                                                | 3.29 us: 1.27x faster                                                         |
| sqlglot_normalize        | 143 ms                                                 | 114 ms: 1.26x faster                                                          |
| 2to3                     | 348 ms                                                 | 278 ms: 1.25x faster                                                          |
| pathlib                  | 20.5 ms                                                | 16.5 ms: 1.24x faster                                                         |
| nqueens                  | 106 ms                                                 | 85.5 ms: 1.24x faster                                                         |
| sqlglot_optimize         | 69.2 ms                                                | 56.6 ms: 1.22x faster                                                         |
| dulwich_log              | 84.3 ms                                                | 69.3 ms: 1.22x faster                                                         |
| xml_etree_generate       | 99.4 ms                                                | 82.4 ms: 1.21x faster                                                         |
| dask                     | 441 ms                                                 | 375 ms: 1.17x faster                                                          |
| sympy_integrate          | 25.8 ms                                                | 22.5 ms: 1.15x faster                                                         |
| sympy_sum                | 196 ms                                                 | 171 ms: 1.15x faster                                                          |
| sympy_str                | 346 ms                                                 | 302 ms: 1.15x faster                                                          |
| xml_etree_iterparse      | 115 ms                                                 | 101 ms: 1.14x faster                                                          |
| bench_thread_pool        | 986 us                                                 | 866 us: 1.14x faster                                                          |
| genshi_xml               | 66.0 ms                                                | 58.0 ms: 1.14x faster                                                         |
| regex_v8                 | 27.8 ms                                                | 24.5 ms: 1.13x faster                                                         |
| docutils                 | 3.30 sec                                               | 2.93 sec: 1.12x faster                                                        |
| sympy_expand             | 566 ms                                                 | 509 ms: 1.11x faster                                                          |
| xml_etree_parse          | 168 ms                                                 | 152 ms: 1.11x faster                                                          |
| json                     | 5.69 ms                                                | 5.21 ms: 1.09x faster                                                         |
| json_loads               | 31.2 us                                                | 28.6 us: 1.09x faster                                                         |
| meteor_contest           | 120 ms                                                 | 111 ms: 1.08x faster                                                          |
| sqlite_synth             | 3.02 us                                                | 2.83 us: 1.07x faster                                                         |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                                          |
| pickle_list              | 5.08 us                                                | 5.10 us: 1.00x slower                                                         |
| asyncio_websockets       | 559 ms                                                 | 567 ms: 1.01x slower                                                          |
| regex_dna                | 227 ms                                                 | 231 ms: 1.02x slower                                                          |
| regex_effbot             | 3.63 ms                                                | 3.71 ms: 1.02x slower                                                         |
| unpickle_list            | 5.20 us                                                | 5.37 us: 1.03x slower                                                         |
| gc_traversal             | 3.62 ms                                                | 3.74 ms: 1.03x slower                                                         |
| async_generators         | 444 ms                                                 | 463 ms: 1.04x slower                                                          |
| unpickle                 | 14.4 us                                                | 15.4 us: 1.07x slower                                                         |
| flaskblogging            | 8.58 ms                                                | 9.23 ms: 1.08x slower                                                         |
| pickle                   | 10.7 us                                                | 11.7 us: 1.10x slower                                                         |
| create_gc_cycles         | 1.62 ms                                                | 1.79 ms: 1.11x slower                                                         |
| telco                    | 7.27 ms                                                | 8.22 ms: 1.13x slower                                                         |
| coverage                 | 79.4 ms                                                | 93.0 ms: 1.17x slower                                                         |
| pickle_dict              | 29.6 us                                                | 36.3 us: 1.23x slower                                                         |
| python_startup_no_site   | 5.93 ms                                                | 7.59 ms: 1.28x slower                                                         |
| Geometric mean           | (ref)                                                  | 1.34x faster                                                                  |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, djangocms, gunicorn, hexiom, mdp, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240521-3.14.0a0-c8ff25c-JIT/bm-20240521-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-c8ff25c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.20x