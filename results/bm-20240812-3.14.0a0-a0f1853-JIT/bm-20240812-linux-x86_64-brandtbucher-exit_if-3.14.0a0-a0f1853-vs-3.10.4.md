# Results vs. 3.10.4

- fork: brandtbucher
- ref: exit_if
- machine: linux-x86_64
- commit hash: a0f1853
- commit date: 2024-08-12
- overall geometric mean: 1.43x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240812-linux-x86_64-brandtbucher-exit_if-3.14.0a0-a0f1853 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 274 ms: 1.27x faster                                           |
| docutils       | 3.30 sec                                               | 2.99 sec: 1.10x faster                                         |
| html5lib       | 88.9 ms                                                | 66.1 ms: 1.34x faster                                          |
| tornado_http   | 136 ms                                                 | 92.3 ms: 1.48x faster                                          |
| Geometric mean | (ref)                                                  | 1.29x faster                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240812-linux-x86_64-brandtbucher-exit_if-3.14.0a0-a0f1853 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 329 ms: 2.21x faster                                           |
| async_tree_memoization  | 870 ms                                                 | 412 ms: 2.11x faster                                           |
| async_tree_io           | 1.77 sec                                               | 910 ms: 1.94x faster                                           |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 564 ms: 1.80x faster                                           |
| Geometric mean          | (ref)                                                  | 2.01x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240812-linux-x86_64-brandtbucher-exit_if-3.14.0a0-a0f1853 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.0 ms: 1.92x faster                                          |
| float          | 117 ms                                                 | 70.3 ms: 1.67x faster                                          |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                           |
| Geometric mean | (ref)                                                  | 1.49x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240812-linux-x86_64-brandtbucher-exit_if-3.14.0a0-a0f1853 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 136 ms: 1.38x faster                                           |
| regex_v8       | 27.8 ms                                                | 24.4 ms: 1.14x faster                                          |
| regex_dna      | 227 ms                                                 | 217 ms: 1.04x faster                                           |
| regex_effbot   | 3.63 ms                                                | 3.70 ms: 1.02x slower                                          |
| Geometric mean | (ref)                                                  | 1.13x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240812-linux-x86_64-brandtbucher-exit_if-3.14.0a0-a0f1853 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.90 sec: 1.65x faster                                         |
| pickle_pure_python   | 484 us                                                 | 300 us: 1.62x faster                                           |
| unpickle_pure_python | 331 us                                                 | 210 us: 1.57x faster                                           |
| xml_etree_process    | 79.1 ms                                                | 56.4 ms: 1.40x faster                                          |
| json_dumps           | 14.2 ms                                                | 10.2 ms: 1.39x faster                                          |
| xml_etree_generate   | 99.4 ms                                                | 80.6 ms: 1.23x faster                                          |
| xml_etree_iterparse  | 115 ms                                                 | 98.5 ms: 1.17x faster                                          |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                           |
| json_loads           | 31.2 us                                                | 27.7 us: 1.13x faster                                          |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240812-linux-x86_64-brandtbucher-exit_if-3.14.0a0-a0f1853 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                          |
| python_startup_no_site | 5.93 ms                                                | 7.13 ms: 1.20x slower                                          |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240812-linux-x86_64-brandtbucher-exit_if-3.14.0a0-a0f1853 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.82 ms: 1.66x faster                                          |
| django_template | 48.2 ms                                                | 35.2 ms: 1.37x faster                                          |
| genshi_text     | 31.8 ms                                                | 24.7 ms: 1.29x faster                                          |
| genshi_xml      | 66.0 ms                                                | 55.7 ms: 1.19x faster                                          |
| Geometric mean  | (ref)                                                  | 1.37x faster                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240812-linux-x86_64-brandtbucher-exit_if-3.14.0a0-a0f1853 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 168 us: 3.23x faster                                           |
| deltablue                | 7.91 ms                                                | 3.11 ms: 2.54x faster                                          |
| generators               | 80.1 ms                                                | 33.2 ms: 2.42x faster                                          |
| deepcopy_memo            | 58.5 us                                                | 26.3 us: 2.22x faster                                          |
| async_tree_none          | 728 ms                                                 | 329 ms: 2.21x faster                                           |
| async_tree_memoization   | 870 ms                                                 | 412 ms: 2.11x faster                                           |
| richards_super           | 94.7 ms                                                | 46.1 ms: 2.05x faster                                          |
| chaos                    | 115 ms                                                 | 58.0 ms: 1.99x faster                                          |
| richards                 | 79.3 ms                                                | 40.0 ms: 1.98x faster                                          |
| crypto_pyaes             | 128 ms                                                 | 65.7 ms: 1.95x faster                                          |
| async_tree_io            | 1.77 sec                                               | 910 ms: 1.94x faster                                           |
| logging_silent           | 190 ns                                                 | 98.0 ns: 1.94x faster                                          |
| scimark_sor              | 220 ms                                                 | 114 ms: 1.93x faster                                           |
| raytrace                 | 507 ms                                                 | 264 ms: 1.92x faster                                           |
| nbody                    | 154 ms                                                 | 80.0 ms: 1.92x faster                                          |
| scimark_monte_carlo      | 118 ms                                                 | 62.0 ms: 1.91x faster                                          |
| asyncio_tcp              | 922 ms                                                 | 501 ms: 1.84x faster                                           |
| deepcopy                 | 479 us                                                 | 261 us: 1.83x faster                                           |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 564 ms: 1.80x faster                                           |
| comprehensions           | 28.8 us                                                | 16.2 us: 1.77x faster                                          |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.68x faster                                          |
| spectral_norm            | 170 ms                                                 | 102 ms: 1.67x faster                                           |
| float                    | 117 ms                                                 | 70.3 ms: 1.67x faster                                          |
| go                       | 240 ms                                                 | 144 ms: 1.66x faster                                           |
| mako                     | 16.3 ms                                                | 9.82 ms: 1.66x faster                                          |
| tomli_loads              | 3.14 sec                                               | 1.90 sec: 1.65x faster                                         |
| scimark_lu               | 176 ms                                                 | 109 ms: 1.62x faster                                           |
| pickle_pure_python       | 484 us                                                 | 300 us: 1.62x faster                                           |
| pyflate                  | 716 ms                                                 | 452 ms: 1.59x faster                                           |
| unpickle_pure_python     | 331 us                                                 | 210 us: 1.57x faster                                           |
| deepcopy_reduce          | 4.17 us                                                | 2.65 us: 1.57x faster                                          |
| sqlglot_transpile        | 2.57 ms                                                | 1.64 ms: 1.57x faster                                          |
| hexiom                   | 10.4 ms                                                | 6.73 ms: 1.54x faster                                          |
| logging_simple           | 8.30 us                                                | 5.42 us: 1.53x faster                                          |
| logging_format           | 9.09 us                                                | 5.97 us: 1.52x faster                                          |
| scimark_fft              | 466 ms                                                 | 309 ms: 1.51x faster                                           |
| pylint                   | 551 ms                                                 | 366 ms: 1.51x faster                                           |
| coroutines               | 35.1 ms                                                | 23.3 ms: 1.51x faster                                          |
| tornado_http             | 136 ms                                                 | 92.3 ms: 1.48x faster                                          |
| fannkuch                 | 532 ms                                                 | 365 ms: 1.46x faster                                           |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.50 ms: 1.44x faster                                          |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                         |
| xml_etree_process        | 79.1 ms                                                | 56.4 ms: 1.40x faster                                          |
| json_dumps               | 14.2 ms                                                | 10.2 ms: 1.39x faster                                          |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                          |
| regex_compile            | 188 ms                                                 | 136 ms: 1.38x faster                                           |
| django_template          | 48.2 ms                                                | 35.2 ms: 1.37x faster                                          |
| thrift                   | 1.07 ms                                                | 786 us: 1.36x faster                                           |
| pprint_safe_repr         | 1.02 sec                                               | 751 ms: 1.35x faster                                           |
| pprint_pformat           | 2.10 sec                                               | 1.56 sec: 1.35x faster                                         |
| html5lib                 | 88.9 ms                                                | 66.1 ms: 1.34x faster                                          |
| pycparser                | 1.58 sec                                               | 1.19 sec: 1.32x faster                                         |
| genshi_text              | 31.8 ms                                                | 24.7 ms: 1.29x faster                                          |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                          |
| 2to3                     | 348 ms                                                 | 274 ms: 1.27x faster                                           |
| sqlglot_normalize        | 143 ms                                                 | 113 ms: 1.27x faster                                           |
| nqueens                  | 106 ms                                                 | 84.9 ms: 1.25x faster                                          |
| xml_etree_generate       | 99.4 ms                                                | 80.6 ms: 1.23x faster                                          |
| bench_thread_pool        | 986 us                                                 | 813 us: 1.21x faster                                           |
| sqlglot_optimize         | 69.2 ms                                                | 57.3 ms: 1.21x faster                                          |
| genshi_xml               | 66.0 ms                                                | 55.7 ms: 1.19x faster                                          |
| xml_etree_iterparse      | 115 ms                                                 | 98.5 ms: 1.17x faster                                          |
| sympy_str                | 346 ms                                                 | 298 ms: 1.16x faster                                           |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                           |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.14x faster                                           |
| regex_v8                 | 27.8 ms                                                | 24.4 ms: 1.14x faster                                          |
| sympy_integrate          | 25.8 ms                                                | 22.7 ms: 1.14x faster                                          |
| json_loads               | 31.2 us                                                | 27.7 us: 1.13x faster                                          |
| sympy_sum                | 196 ms                                                 | 175 ms: 1.13x faster                                           |
| sympy_expand             | 566 ms                                                 | 504 ms: 1.12x faster                                           |
| mdp                      | 2.85 sec                                               | 2.55 sec: 1.12x faster                                         |
| json                     | 5.69 ms                                                | 5.13 ms: 1.11x faster                                          |
| docutils                 | 3.30 sec                                               | 2.99 sec: 1.10x faster                                         |
| regex_dna                | 227 ms                                                 | 217 ms: 1.04x faster                                           |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                           |
| regex_effbot             | 3.63 ms                                                | 3.70 ms: 1.02x slower                                          |
| async_generators         | 444 ms                                                 | 457 ms: 1.03x slower                                           |
| gc_traversal             | 3.62 ms                                                | 3.76 ms: 1.04x slower                                          |
| telco                    | 7.27 ms                                                | 7.83 ms: 1.08x slower                                          |
| create_gc_cycles         | 1.62 ms                                                | 1.76 ms: 1.09x slower                                          |
| coverage                 | 79.4 ms                                                | 92.0 ms: 1.16x slower                                          |
| python_startup_no_site   | 5.93 ms                                                | 7.13 ms: 1.20x slower                                          |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                   |

Benchmark hidden because not significant (2): asyncio_websockets, bench_mp_pool
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240812-3.14.0a0-a0f1853-JIT/bm-20240812-linux-x86_64-brandtbucher-exit_if-3.14.0a0-a0f1853.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.21x