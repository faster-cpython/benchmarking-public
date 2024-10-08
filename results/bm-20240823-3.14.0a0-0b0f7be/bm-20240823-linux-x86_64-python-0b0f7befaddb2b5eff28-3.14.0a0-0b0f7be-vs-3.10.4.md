# Results vs. 3.10.4

- fork: python
- ref: 0b0f7befaddb2b5eff28
- machine: linux-x86_64
- commit hash: 0b0f7be
- commit date: 2024-08-23
- overall geometric mean: 1.44x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240823-linux-x86_64-python-0b0f7befaddb2b5eff28-3.14.0a0-0b0f7be |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 254 ms: 1.37x faster                                                  |
| docutils       | 3.30 sec                                               | 2.70 sec: 1.22x faster                                                |
| html5lib       | 88.9 ms                                                | 65.6 ms: 1.35x faster                                                 |
| tornado_http   | 136 ms                                                 | 90.4 ms: 1.51x faster                                                 |
| Geometric mean | (ref)                                                  | 1.36x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240823-linux-x86_64-python-0b0f7befaddb2b5eff28-3.14.0a0-0b0f7be |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 322 ms: 2.26x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 391 ms: 2.22x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 930 ms: 1.90x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 555 ms: 1.83x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.05x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240823-linux-x86_64-python-0b0f7befaddb2b5eff28-3.14.0a0-0b0f7be |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 86.9 ms: 1.77x faster                                                 |
| float          | 117 ms                                                 | 77.3 ms: 1.51x faster                                                 |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.40x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240823-linux-x86_64-python-0b0f7befaddb2b5eff28-3.14.0a0-0b0f7be |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.47x faster                                                  |
| regex_v8       | 27.8 ms                                                | 24.5 ms: 1.13x faster                                                 |
| regex_dna      | 227 ms                                                 | 220 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.14x faster                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240823-linux-x86_64-python-0b0f7befaddb2b5eff28-3.14.0a0-0b0f7be |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 302 us: 1.60x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 212 us: 1.56x faster                                                  |
| tomli_loads          | 3.14 sec                                               | 2.07 sec: 1.52x faster                                                |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.37x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 58.4 ms: 1.35x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 84.5 ms: 1.18x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 105 ms: 1.10x faster                                                  |
| json_loads           | 31.2 us                                                | 28.3 us: 1.10x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 155 ms: 1.09x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240823-linux-x86_64-python-0b0f7befaddb2b5eff28-3.14.0a0-0b0f7be |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240823-linux-x86_64-python-0b0f7befaddb2b5eff28-3.14.0a0-0b0f7be |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.3 ms: 1.44x faster                                                 |
| django_template | 48.2 ms                                                | 34.1 ms: 1.41x faster                                                 |
| genshi_text     | 31.8 ms                                                | 22.6 ms: 1.41x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 49.8 ms: 1.33x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240823-linux-x86_64-python-0b0f7befaddb2b5eff28-3.14.0a0-0b0f7be |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 158 us: 3.44x faster                                                  |
| generators               | 80.1 ms                                                | 27.9 ms: 2.87x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.18 ms: 2.49x faster                                                 |
| async_tree_none          | 728 ms                                                 | 322 ms: 2.26x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 391 ms: 2.22x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 29.6 us: 1.97x faster                                                 |
| chaos                    | 115 ms                                                 | 58.8 ms: 1.97x faster                                                 |
| raytrace                 | 507 ms                                                 | 260 ms: 1.95x faster                                                  |
| asyncio_tcp              | 922 ms                                                 | 482 ms: 1.91x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 930 ms: 1.90x faster                                                  |
| logging_silent           | 190 ns                                                 | 101 ns: 1.89x faster                                                  |
| deepcopy                 | 479 us                                                 | 259 us: 1.85x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 555 ms: 1.83x faster                                                  |
| richards_super           | 94.7 ms                                                | 52.1 ms: 1.82x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 71.9 ms: 1.78x faster                                                 |
| nbody                    | 154 ms                                                 | 86.9 ms: 1.77x faster                                                 |
| comprehensions           | 28.8 us                                                | 16.3 us: 1.76x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 67.6 ms: 1.75x faster                                                 |
| scimark_sor              | 220 ms                                                 | 126 ms: 1.74x faster                                                  |
| pylint                   | 551 ms                                                 | 320 ms: 1.72x faster                                                  |
| richards                 | 79.3 ms                                                | 46.1 ms: 1.72x faster                                                 |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.70x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.13 ms: 1.70x faster                                                 |
| sqlglot_transpile        | 2.57 ms                                                | 1.57 ms: 1.64x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 302 us: 1.60x faster                                                  |
| scimark_lu               | 176 ms                                                 | 113 ms: 1.57x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.67 us: 1.56x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 212 us: 1.56x faster                                                  |
| spectral_norm            | 170 ms                                                 | 110 ms: 1.54x faster                                                  |
| coroutines               | 35.1 ms                                                | 22.8 ms: 1.54x faster                                                 |
| pyflate                  | 716 ms                                                 | 470 ms: 1.52x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 2.07 sec: 1.52x faster                                                |
| float                    | 117 ms                                                 | 77.3 ms: 1.51x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.51 us: 1.51x faster                                                 |
| tornado_http             | 136 ms                                                 | 90.4 ms: 1.51x faster                                                 |
| go                       | 240 ms                                                 | 161 ms: 1.49x faster                                                  |
| logging_format           | 9.09 us                                                | 6.17 us: 1.47x faster                                                 |
| regex_compile            | 188 ms                                                 | 128 ms: 1.47x faster                                                  |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.44x faster                                                 |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.79 sec: 1.44x faster                                                |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                                |
| django_template          | 48.2 ms                                                | 34.1 ms: 1.41x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 722 ms: 1.41x faster                                                  |
| genshi_text              | 31.8 ms                                                | 22.6 ms: 1.41x faster                                                 |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                 |
| thrift                   | 1.07 ms                                                | 777 us: 1.38x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                                |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.37x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.72 ms: 1.37x faster                                                 |
| 2to3                     | 348 ms                                                 | 254 ms: 1.37x faster                                                  |
| html5lib                 | 88.9 ms                                                | 65.6 ms: 1.35x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 58.4 ms: 1.35x faster                                                 |
| nqueens                  | 106 ms                                                 | 78.8 ms: 1.34x faster                                                 |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.34x faster                                                  |
| fannkuch                 | 532 ms                                                 | 398 ms: 1.34x faster                                                  |
| sqlglot_normalize        | 143 ms                                                 | 108 ms: 1.33x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 49.8 ms: 1.33x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 19.5 ms: 1.32x faster                                                 |
| sympy_str                | 346 ms                                                 | 266 ms: 1.30x faster                                                  |
| scimark_fft              | 466 ms                                                 | 358 ms: 1.30x faster                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 53.4 ms: 1.29x faster                                                 |
| pathlib                  | 20.5 ms                                                | 15.8 ms: 1.29x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 785 us: 1.26x faster                                                  |
| sympy_expand             | 566 ms                                                 | 454 ms: 1.25x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.70 sec: 1.22x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 84.5 ms: 1.18x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 24.5 ms: 1.13x faster                                                 |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 105 ms: 1.10x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.58 sec: 1.10x faster                                                |
| json_loads               | 31.2 us                                                | 28.3 us: 1.10x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 155 ms: 1.09x faster                                                  |
| json                     | 5.69 ms                                                | 5.32 ms: 1.07x faster                                                 |
| regex_dna                | 227 ms                                                 | 220 ms: 1.03x faster                                                  |
| async_generators         | 444 ms                                                 | 433 ms: 1.03x faster                                                  |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                                  |
| gc_traversal             | 3.62 ms                                                | 3.72 ms: 1.03x slower                                                 |
| coverage                 | 79.4 ms                                                | 85.1 ms: 1.07x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 1.75 ms: 1.08x slower                                                 |
| telco                    | 7.27 ms                                                | 8.15 ms: 1.12x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.44x faster                                                          |

Benchmark hidden because not significant (3): asyncio_websockets, regex_effbot, bench_mp_pool
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240823-3.14.0a0-0b0f7be/bm-20240823-linux-x86_64-python-0b0f7befaddb2b5eff28-3.14.0a0-0b0f7be.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: 1.12x