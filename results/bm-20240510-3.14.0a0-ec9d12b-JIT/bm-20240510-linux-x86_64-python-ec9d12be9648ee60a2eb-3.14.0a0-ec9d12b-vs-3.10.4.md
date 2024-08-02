# Results vs. 3.10.4

- fork: python
- ref: ec9d12be9648ee60a2eb
- machine: linux-x86_64
- commit hash: ec9d12b
- commit date: 2024-05-10
- overall geometric mean: 1.29x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 280 ms: 1.25x faster                                                  |
| chameleon      | 9.68 ms                                                | 7.00 ms: 1.38x faster                                                 |
| docutils       | 3.30 sec                                               | 2.97 sec: 1.11x faster                                                |
| html5lib       | 88.9 ms                                                | 67.7 ms: 1.31x faster                                                 |
| tornado_http   | 136 ms                                                 | 97.6 ms: 1.40x faster                                                 |
| Geometric mean | (ref)                                                  | 1.29x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 365 ms: 1.99x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 943 ms: 1.88x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 480 ms: 1.81x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 627 ms: 1.62x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.82x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.9 ms: 1.90x faster                                                 |
| float          | 117 ms                                                 | 71.6 ms: 1.64x faster                                                 |
| pidigits       | 191 ms                                                 | 188 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.47x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 139 ms: 1.35x faster                                                  |
| regex_v8       | 27.8 ms                                                | 24.3 ms: 1.15x faster                                                 |
| regex_dna      | 227 ms                                                 | 214 ms: 1.06x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.55 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.14x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 300 us: 1.61x faster                                                  |
| tomli_loads          | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                |
| unpickle_pure_python | 331 us                                                 | 222 us: 1.49x faster                                                  |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 59.1 ms: 1.34x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 83.1 ms: 1.20x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 101 ms: 1.14x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 152 ms: 1.11x faster                                                  |
| json_loads           | 31.2 us                                                | 29.1 us: 1.07x faster                                                 |
| unpickle_list        | 5.20 us                                                | 5.44 us: 1.05x slower                                                 |
| pickle_list          | 5.08 us                                                | 5.47 us: 1.08x slower                                                 |
| unpickle             | 14.4 us                                                | 15.6 us: 1.09x slower                                                 |
| pickle               | 10.7 us                                                | 11.8 us: 1.11x slower                                                 |
| pickle_dict          | 29.6 us                                                | 33.5 us: 1.13x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.0 ms: 1.33x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.63 ms: 1.29x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.56 ms: 1.71x faster                                                 |
| django_template | 48.2 ms                                                | 36.3 ms: 1.33x faster                                                 |
| genshi_text     | 31.8 ms                                                | 24.7 ms: 1.29x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 57.9 ms: 1.14x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 171 us: 3.18x faster                                                  |
| generators               | 80.1 ms                                                | 30.3 ms: 2.64x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.73 ms: 2.12x faster                                                 |
| async_tree_none          | 728 ms                                                 | 365 ms: 1.99x faster                                                  |
| richards_super           | 94.7 ms                                                | 47.6 ms: 1.99x faster                                                 |
| chaos                    | 115 ms                                                 | 59.3 ms: 1.95x faster                                                 |
| nbody                    | 154 ms                                                 | 80.9 ms: 1.90x faster                                                 |
| richards                 | 79.3 ms                                                | 41.8 ms: 1.90x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 67.9 ms: 1.88x faster                                                 |
| async_tree_io            | 1.77 sec                                               | 943 ms: 1.88x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 63.4 ms: 1.87x faster                                                 |
| raytrace                 | 507 ms                                                 | 278 ms: 1.82x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 480 ms: 1.81x faster                                                  |
| logging_silent           | 190 ns                                                 | 106 ns: 1.80x faster                                                  |
| asyncio_tcp              | 922 ms                                                 | 522 ms: 1.77x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                                 |
| mako                     | 16.3 ms                                                | 9.56 ms: 1.71x faster                                                 |
| spectral_norm            | 170 ms                                                 | 102 ms: 1.66x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.31 ms: 1.66x faster                                                 |
| float                    | 117 ms                                                 | 71.6 ms: 1.64x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 627 ms: 1.62x faster                                                  |
| scimark_sor              | 220 ms                                                 | 136 ms: 1.62x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 300 us: 1.61x faster                                                  |
| go                       | 240 ms                                                 | 149 ms: 1.61x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                |
| hexiom                   | 10.4 ms                                                | 6.58 ms: 1.58x faster                                                 |
| sqlglot_transpile        | 2.57 ms                                                | 1.64 ms: 1.57x faster                                                 |
| pyflate                  | 716 ms                                                 | 459 ms: 1.56x faster                                                  |
| pylint                   | 551 ms                                                 | 354 ms: 1.56x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 37.9 us: 1.54x faster                                                 |
| coroutines               | 35.1 ms                                                | 22.9 ms: 1.53x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 222 us: 1.49x faster                                                  |
| scimark_fft              | 466 ms                                                 | 319 ms: 1.46x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.73 us: 1.45x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.45 sec: 1.45x faster                                                |
| logging_format           | 9.09 us                                                | 6.28 us: 1.45x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.49 ms: 1.44x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 708 ms: 1.44x faster                                                  |
| fannkuch                 | 532 ms                                                 | 371 ms: 1.43x faster                                                  |
| scimark_lu               | 176 ms                                                 | 125 ms: 1.41x faster                                                  |
| tornado_http             | 136 ms                                                 | 97.6 ms: 1.40x faster                                                 |
| chameleon                | 9.68 ms                                                | 7.00 ms: 1.38x faster                                                 |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.86 sec: 1.38x faster                                                |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                                |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                 |
| regex_compile            | 188 ms                                                 | 139 ms: 1.35x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 59.1 ms: 1.34x faster                                                 |
| python_startup           | 14.6 ms                                                | 11.0 ms: 1.33x faster                                                 |
| django_template          | 48.2 ms                                                | 36.3 ms: 1.33x faster                                                 |
| html5lib                 | 88.9 ms                                                | 67.7 ms: 1.31x faster                                                 |
| thrift                   | 1.07 ms                                                | 830 us: 1.29x faster                                                  |
| genshi_text              | 31.8 ms                                                | 24.7 ms: 1.29x faster                                                 |
| sqlglot_normalize        | 143 ms                                                 | 112 ms: 1.27x faster                                                  |
| deepcopy                 | 479 us                                                 | 378 us: 1.27x faster                                                  |
| 2to3                     | 348 ms                                                 | 280 ms: 1.25x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 3.36 us: 1.24x faster                                                 |
| sqlglot_optimize         | 69.2 ms                                                | 56.5 ms: 1.22x faster                                                 |
| nqueens                  | 106 ms                                                 | 87.0 ms: 1.22x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 69.6 ms: 1.21x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 83.1 ms: 1.20x faster                                                 |
| dask                     | 441 ms                                                 | 379 ms: 1.16x faster                                                  |
| pathlib                  | 20.5 ms                                                | 17.7 ms: 1.15x faster                                                 |
| sympy_str                | 346 ms                                                 | 301 ms: 1.15x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 24.3 ms: 1.15x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 22.6 ms: 1.14x faster                                                 |
| sympy_sum                | 196 ms                                                 | 172 ms: 1.14x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 57.9 ms: 1.14x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 101 ms: 1.14x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 877 us: 1.12x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.97 sec: 1.11x faster                                                |
| sympy_expand             | 566 ms                                                 | 510 ms: 1.11x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 152 ms: 1.11x faster                                                  |
| meteor_contest           | 120 ms                                                 | 110 ms: 1.08x faster                                                  |
| json_loads               | 31.2 us                                                | 29.1 us: 1.07x faster                                                 |
| regex_dna                | 227 ms                                                 | 214 ms: 1.06x faster                                                  |
| json                     | 5.69 ms                                                | 5.39 ms: 1.06x faster                                                 |
| sqlite_synth             | 3.02 us                                                | 2.87 us: 1.05x faster                                                 |
| mdp                      | 2.85 sec                                               | 2.72 sec: 1.05x faster                                                |
| regex_effbot             | 3.63 ms                                                | 3.55 ms: 1.02x faster                                                 |
| pidigits                 | 191 ms                                                 | 188 ms: 1.01x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 567 ms: 1.01x slower                                                  |
| unpickle_list            | 5.20 us                                                | 5.44 us: 1.05x slower                                                 |
| async_generators         | 444 ms                                                 | 466 ms: 1.05x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 3.87 ms: 1.07x slower                                                 |
| flaskblogging            | 8.58 ms                                                | 9.23 ms: 1.08x slower                                                 |
| pickle_list              | 5.08 us                                                | 5.47 us: 1.08x slower                                                 |
| unpickle                 | 14.4 us                                                | 15.6 us: 1.09x slower                                                 |
| pickle                   | 10.7 us                                                | 11.8 us: 1.11x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 1.83 ms: 1.13x slower                                                 |
| pickle_dict              | 29.6 us                                                | 33.5 us: 1.13x slower                                                 |
| coverage                 | 79.4 ms                                                | 95.1 ms: 1.20x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.63 ms: 1.29x slower                                                 |
| telco                    | 7.27 ms                                                | 173 ms: 23.79x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.29x faster                                                          |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, djangocms, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240510-3.14.0a0-ec9d12b-JIT/bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.21x