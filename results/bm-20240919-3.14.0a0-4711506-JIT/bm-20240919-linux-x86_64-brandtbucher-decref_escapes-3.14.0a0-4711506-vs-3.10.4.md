# Results vs. 3.10.4

- fork: brandtbucher
- ref: decref_escapes
- machine: linux-x86_64
- commit hash: 4711506
- commit date: 2024-09-19
- overall geometric mean: 1.37x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 277 ms: 1.26x faster                                                  |
| docutils       | 3.30 sec                                               | 2.97 sec: 1.11x faster                                                |
| html5lib       | 88.9 ms                                                | 63.8 ms: 1.39x faster                                                 |
| tornado_http   | 136 ms                                                 | 95.1 ms: 1.43x faster                                                 |
| Geometric mean | (ref)                                                  | 1.29x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 319 ms: 2.29x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 403 ms: 2.16x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 858 ms: 2.06x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 571 ms: 1.78x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.06x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.2 ms: 1.91x faster                                                 |
| float          | 117 ms                                                 | 70.7 ms: 1.66x faster                                                 |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.48x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 142 ms: 1.33x faster                                                  |
| regex_v8       | 27.8 ms                                                | 25.1 ms: 1.11x faster                                                 |
| regex_dna      | 227 ms                                                 | 224 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                |
| pickle_pure_python   | 484 us                                                 | 305 us: 1.59x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 54.6 ms: 1.45x faster                                                 |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.38x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 77.9 ms: 1.28x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 98.0 ms: 1.18x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                                  |
| json_loads           | 31.2 us                                                | 27.5 us: 1.13x faster                                                 |
| pickle_list          | 5.08 us                                                | 5.37 us: 1.06x slower                                                 |
| unpickle             | 14.4 us                                                | 15.3 us: 1.07x slower                                                 |
| pickle               | 10.7 us                                                | 11.6 us: 1.08x slower                                                 |
| pickle_dict          | 29.6 us                                                | 35.2 us: 1.19x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                          |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.08 ms: 1.19x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.97 ms: 1.64x faster                                                 |
| django_template | 48.2 ms                                                | 35.4 ms: 1.36x faster                                                 |
| genshi_text     | 31.8 ms                                                | 24.5 ms: 1.30x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 58.0 ms: 1.14x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 160 us: 3.41x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.21 ms: 2.47x faster                                                 |
| generators               | 80.1 ms                                                | 33.1 ms: 2.42x faster                                                 |
| async_tree_none          | 728 ms                                                 | 319 ms: 2.29x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 26.9 us: 2.18x faster                                                 |
| async_tree_memoization   | 870 ms                                                 | 403 ms: 2.16x faster                                                  |
| richards_super           | 94.7 ms                                                | 45.6 ms: 2.08x faster                                                 |
| async_tree_io            | 1.77 sec                                               | 858 ms: 2.06x faster                                                  |
| richards                 | 79.3 ms                                                | 39.9 ms: 1.99x faster                                                 |
| nbody                    | 154 ms                                                 | 80.2 ms: 1.91x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 67.2 ms: 1.90x faster                                                 |
| chaos                    | 115 ms                                                 | 60.8 ms: 1.90x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 62.7 ms: 1.89x faster                                                 |
| scimark_sor              | 220 ms                                                 | 117 ms: 1.88x faster                                                  |
| asyncio_tcp              | 922 ms                                                 | 498 ms: 1.85x faster                                                  |
| logging_silent           | 190 ns                                                 | 103 ns: 1.83x faster                                                  |
| go                       | 240 ms                                                 | 132 ms: 1.82x faster                                                  |
| deepcopy                 | 479 us                                                 | 263 us: 1.82x faster                                                  |
| raytrace                 | 507 ms                                                 | 280 ms: 1.81x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 571 ms: 1.78x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.71x faster                                                 |
| spectral_norm            | 170 ms                                                 | 102 ms: 1.67x faster                                                  |
| float                    | 117 ms                                                 | 70.7 ms: 1.66x faster                                                 |
| mako                     | 16.3 ms                                                | 9.97 ms: 1.64x faster                                                 |
| sqlglot_parse            | 2.17 ms                                                | 1.34 ms: 1.62x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                |
| scimark_lu               | 176 ms                                                 | 110 ms: 1.60x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 305 us: 1.59x faster                                                  |
| pyflate                  | 716 ms                                                 | 451 ms: 1.59x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.66 us: 1.57x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.69 ms: 1.53x faster                                                 |
| coroutines               | 35.1 ms                                                | 23.0 ms: 1.52x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.29 ms: 1.51x faster                                                 |
| scimark_fft              | 466 ms                                                 | 310 ms: 1.50x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.98 ms: 1.49x faster                                                 |
| logging_format           | 9.09 us                                                | 6.13 us: 1.48x faster                                                 |
| pylint                   | 551 ms                                                 | 374 ms: 1.48x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.65 us: 1.47x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 54.6 ms: 1.45x faster                                                 |
| tornado_http             | 136 ms                                                 | 95.1 ms: 1.43x faster                                                 |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                                |
| fannkuch                 | 532 ms                                                 | 375 ms: 1.42x faster                                                  |
| html5lib                 | 88.9 ms                                                | 63.8 ms: 1.39x faster                                                 |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                 |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.38x faster                                                 |
| django_template          | 48.2 ms                                                | 35.4 ms: 1.36x faster                                                 |
| thrift                   | 1.07 ms                                                | 794 us: 1.35x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.56 sec: 1.34x faster                                                |
| pprint_safe_repr         | 1.02 sec                                               | 761 ms: 1.34x faster                                                  |
| regex_compile            | 188 ms                                                 | 142 ms: 1.33x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.21 sec: 1.30x faster                                                |
| genshi_text              | 31.8 ms                                                | 24.5 ms: 1.30x faster                                                 |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.28x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 77.9 ms: 1.28x faster                                                 |
| sqlglot_normalize        | 143 ms                                                 | 113 ms: 1.26x faster                                                  |
| 2to3                     | 348 ms                                                 | 277 ms: 1.26x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 68.3 ms: 1.23x faster                                                 |
| nqueens                  | 106 ms                                                 | 87.9 ms: 1.20x faster                                                 |
| sqlglot_optimize         | 69.2 ms                                                | 57.9 ms: 1.19x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 98.0 ms: 1.18x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 838 us: 1.18x faster                                                  |
| sympy_str                | 346 ms                                                 | 299 ms: 1.16x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                                  |
| sympy_sum                | 196 ms                                                 | 172 ms: 1.14x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 58.0 ms: 1.14x faster                                                 |
| json_loads               | 31.2 us                                                | 27.5 us: 1.13x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 22.8 ms: 1.13x faster                                                 |
| sympy_expand             | 566 ms                                                 | 504 ms: 1.12x faster                                                  |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.11x faster                                                  |
| json                     | 5.69 ms                                                | 5.14 ms: 1.11x faster                                                 |
| docutils                 | 3.30 sec                                               | 2.97 sec: 1.11x faster                                                |
| regex_v8                 | 27.8 ms                                                | 25.1 ms: 1.11x faster                                                 |
| sqlite_synth             | 3.02 us                                                | 2.76 us: 1.09x faster                                                 |
| mdp                      | 2.85 sec                                               | 2.70 sec: 1.06x faster                                                |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                  |
| regex_dna                | 227 ms                                                 | 224 ms: 1.01x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 556 ms: 1.01x faster                                                  |
| async_generators         | 444 ms                                                 | 451 ms: 1.02x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 3.83 ms: 1.06x slower                                                 |
| pickle_list              | 5.08 us                                                | 5.37 us: 1.06x slower                                                 |
| coverage                 | 79.4 ms                                                | 84.5 ms: 1.06x slower                                                 |
| unpickle                 | 14.4 us                                                | 15.3 us: 1.07x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 1.75 ms: 1.08x slower                                                 |
| pickle                   | 10.7 us                                                | 11.6 us: 1.08x slower                                                 |
| telco                    | 7.27 ms                                                | 7.94 ms: 1.09x slower                                                 |
| pickle_dict              | 29.6 us                                                | 35.2 us: 1.19x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.08 ms: 1.19x slower                                                 |
| unpack_sequence          | 60.0 ns                                                | 106 ns: 1.77x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.37x faster                                                          |

Benchmark hidden because not significant (3): unpickle_list, bench_mp_pool, regex_effbot
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240919-3.14.0a0-4711506-JIT/bm-20240919-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-4711506.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.21x