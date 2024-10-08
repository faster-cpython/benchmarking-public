# Results vs. 3.10.4

- fork: brandtbucher
- ref: decref_escapes
- machine: linux-x86_64
- commit hash: 87cbfd7
- commit date: 2024-09-23
- overall geometric mean: 1.38x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 278 ms: 1.26x faster                                                  |
| docutils       | 3.30 sec                                               | 2.96 sec: 1.11x faster                                                |
| html5lib       | 88.9 ms                                                | 62.7 ms: 1.42x faster                                                 |
| tornado_http   | 136 ms                                                 | 94.9 ms: 1.44x faster                                                 |
| Geometric mean | (ref)                                                  | 1.30x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 317 ms: 2.30x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 395 ms: 2.20x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 862 ms: 2.05x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 574 ms: 1.77x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.07x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 81.4 ms: 1.89x faster                                                 |
| float          | 117 ms                                                 | 70.6 ms: 1.66x faster                                                 |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.47x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 142 ms: 1.33x faster                                                  |
| regex_v8       | 27.8 ms                                                | 24.1 ms: 1.15x faster                                                 |
| regex_dna      | 227 ms                                                 | 215 ms: 1.05x faster                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                |
| pickle_pure_python   | 484 us                                                 | 308 us: 1.58x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 55.0 ms: 1.44x faster                                                 |
| json_dumps           | 14.2 ms                                                | 10.1 ms: 1.41x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 78.2 ms: 1.27x faster                                                 |
| json_loads           | 31.2 us                                                | 26.7 us: 1.17x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 99.3 ms: 1.16x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                                  |
| pickle_list          | 5.08 us                                                | 5.04 us: 1.01x faster                                                 |
| unpickle_list        | 5.20 us                                                | 5.31 us: 1.02x slower                                                 |
| unpickle             | 14.4 us                                                | 14.9 us: 1.03x slower                                                 |
| pickle               | 10.7 us                                                | 11.4 us: 1.07x slower                                                 |
| pickle_dict          | 29.6 us                                                | 33.2 us: 1.12x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.20x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.77 ms: 1.67x faster                                                 |
| django_template | 48.2 ms                                                | 36.4 ms: 1.32x faster                                                 |
| genshi_text     | 31.8 ms                                                | 24.9 ms: 1.28x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 60.0 ms: 1.10x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.33x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 162 us: 3.36x faster                                                  |
| generators               | 80.1 ms                                                | 33.0 ms: 2.43x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.27 ms: 2.42x faster                                                 |
| async_tree_none          | 728 ms                                                 | 317 ms: 2.30x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 395 ms: 2.20x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 27.0 us: 2.16x faster                                                 |
| async_tree_io            | 1.77 sec                                               | 862 ms: 2.05x faster                                                  |
| richards_super           | 94.7 ms                                                | 47.2 ms: 2.01x faster                                                 |
| chaos                    | 115 ms                                                 | 59.4 ms: 1.94x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 67.6 ms: 1.89x faster                                                 |
| nbody                    | 154 ms                                                 | 81.4 ms: 1.89x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 63.1 ms: 1.87x faster                                                 |
| asyncio_tcp              | 922 ms                                                 | 494 ms: 1.87x faster                                                  |
| richards                 | 79.3 ms                                                | 42.7 ms: 1.86x faster                                                 |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.85x faster                                                  |
| deepcopy                 | 479 us                                                 | 260 us: 1.84x faster                                                  |
| logging_silent           | 190 ns                                                 | 103 ns: 1.84x faster                                                  |
| raytrace                 | 507 ms                                                 | 279 ms: 1.82x faster                                                  |
| go                       | 240 ms                                                 | 133 ms: 1.81x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 574 ms: 1.77x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.71x faster                                                 |
| mako                     | 16.3 ms                                                | 9.77 ms: 1.67x faster                                                 |
| float                    | 117 ms                                                 | 70.6 ms: 1.66x faster                                                 |
| spectral_norm            | 170 ms                                                 | 103 ms: 1.65x faster                                                  |
| pyflate                  | 716 ms                                                 | 443 ms: 1.62x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                |
| sqlglot_parse            | 2.17 ms                                                | 1.35 ms: 1.61x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 2.62 us: 1.59x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 308 us: 1.58x faster                                                  |
| scimark_lu               | 176 ms                                                 | 112 ms: 1.57x faster                                                  |
| coroutines               | 35.1 ms                                                | 22.6 ms: 1.55x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.71 ms: 1.51x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.32 ms: 1.50x faster                                                 |
| hexiom                   | 10.4 ms                                                | 7.00 ms: 1.49x faster                                                 |
| scimark_fft              | 466 ms                                                 | 315 ms: 1.48x faster                                                  |
| pylint                   | 551 ms                                                 | 374 ms: 1.47x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.69 us: 1.46x faster                                                 |
| logging_format           | 9.09 us                                                | 6.28 us: 1.45x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 55.0 ms: 1.44x faster                                                 |
| tornado_http             | 136 ms                                                 | 94.9 ms: 1.44x faster                                                 |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                                |
| html5lib                 | 88.9 ms                                                | 62.7 ms: 1.42x faster                                                 |
| json_dumps               | 14.2 ms                                                | 10.1 ms: 1.41x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 726 ms: 1.40x faster                                                  |
| fannkuch                 | 532 ms                                                 | 380 ms: 1.40x faster                                                  |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.53 sec: 1.37x faster                                                |
| thrift                   | 1.07 ms                                                | 786 us: 1.36x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.35x faster                                                |
| regex_compile            | 188 ms                                                 | 142 ms: 1.33x faster                                                  |
| django_template          | 48.2 ms                                                | 36.4 ms: 1.32x faster                                                 |
| genshi_text              | 31.8 ms                                                | 24.9 ms: 1.28x faster                                                 |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 78.2 ms: 1.27x faster                                                 |
| sqlglot_normalize        | 143 ms                                                 | 114 ms: 1.26x faster                                                  |
| 2to3                     | 348 ms                                                 | 278 ms: 1.26x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 68.5 ms: 1.23x faster                                                 |
| nqueens                  | 106 ms                                                 | 86.1 ms: 1.23x faster                                                 |
| sqlglot_optimize         | 69.2 ms                                                | 58.2 ms: 1.19x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 839 us: 1.18x faster                                                  |
| json_loads               | 31.2 us                                                | 26.7 us: 1.17x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 99.3 ms: 1.16x faster                                                 |
| sympy_str                | 346 ms                                                 | 299 ms: 1.16x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 24.1 ms: 1.15x faster                                                 |
| sympy_sum                | 196 ms                                                 | 172 ms: 1.14x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 22.7 ms: 1.14x faster                                                 |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                  |
| json                     | 5.69 ms                                                | 5.04 ms: 1.13x faster                                                 |
| mdp                      | 2.85 sec                                               | 2.52 sec: 1.13x faster                                                |
| sympy_expand             | 566 ms                                                 | 505 ms: 1.12x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.96 sec: 1.11x faster                                                |
| sqlite_synth             | 3.02 us                                                | 2.73 us: 1.11x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 60.0 ms: 1.10x faster                                                 |
| regex_dna                | 227 ms                                                 | 215 ms: 1.05x faster                                                  |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                  |
| pickle_list              | 5.08 us                                                | 5.04 us: 1.01x faster                                                 |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                  |
| unpickle_list            | 5.20 us                                                | 5.31 us: 1.02x slower                                                 |
| async_generators         | 444 ms                                                 | 457 ms: 1.03x slower                                                  |
| unpickle                 | 14.4 us                                                | 14.9 us: 1.03x slower                                                 |
| coverage                 | 79.4 ms                                                | 84.4 ms: 1.06x slower                                                 |
| pickle                   | 10.7 us                                                | 11.4 us: 1.07x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 3.91 ms: 1.08x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 1.76 ms: 1.09x slower                                                 |
| telco                    | 7.27 ms                                                | 8.06 ms: 1.11x slower                                                 |
| pickle_dict              | 29.6 us                                                | 33.2 us: 1.12x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                 |
| unpack_sequence          | 60.0 ns                                                | 112 ns: 1.87x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.38x faster                                                          |

Benchmark hidden because not significant (2): regex_effbot, bench_mp_pool
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240923-3.14.0a0-87cbfd7-JIT/bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.21x