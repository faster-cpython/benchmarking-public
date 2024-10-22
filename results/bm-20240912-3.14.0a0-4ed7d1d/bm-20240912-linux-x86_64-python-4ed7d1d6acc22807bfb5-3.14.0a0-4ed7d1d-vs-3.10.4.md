# Results vs. 3.10.4

- fork: python
- ref: 4ed7d1d6acc22807bfb5
- machine: linux-x86_64
- commit hash: 4ed7d1d
- commit date: 2024-09-12
- overall geometric mean: 1.40x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 254 ms: 1.37x faster                                                  |
| docutils       | 3.30 sec                                               | 2.66 sec: 1.24x faster                                                |
| html5lib       | 88.9 ms                                                | 63.3 ms: 1.40x faster                                                 |
| tornado_http   | 136 ms                                                 | 90.8 ms: 1.50x faster                                                 |
| Geometric mean | (ref)                                                  | 1.38x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 314 ms: 2.32x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 395 ms: 2.20x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 864 ms: 2.05x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 566 ms: 1.79x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.08x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 86.5 ms: 1.77x faster                                                 |
| float          | 117 ms                                                 | 78.1 ms: 1.50x faster                                                 |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.39x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.47x faster                                                  |
| regex_v8       | 27.8 ms                                                | 24.6 ms: 1.13x faster                                                 |
| regex_dna      | 227 ms                                                 | 218 ms: 1.04x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.72 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.14x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 303 us: 1.60x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 211 us: 1.56x faster                                                  |
| tomli_loads          | 3.14 sec                                               | 2.11 sec: 1.49x faster                                                |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 58.9 ms: 1.34x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 85.0 ms: 1.17x faster                                                 |
| json_loads           | 31.2 us                                                | 26.7 us: 1.17x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 104 ms: 1.11x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 154 ms: 1.09x faster                                                  |
| pickle_list          | 5.08 us                                                | 5.14 us: 1.01x slower                                                 |
| unpickle             | 14.4 us                                                | 14.9 us: 1.04x slower                                                 |
| pickle               | 10.7 us                                                | 11.5 us: 1.08x slower                                                 |
| pickle_dict          | 29.6 us                                                | 33.9 us: 1.15x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                          |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 6.99 ms: 1.18x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.1 ms: 1.47x faster                                                 |
| django_template | 48.2 ms                                                | 34.1 ms: 1.41x faster                                                 |
| genshi_text     | 31.8 ms                                                | 22.8 ms: 1.40x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 50.9 ms: 1.30x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.39x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 162 us: 3.35x faster                                                  |
| generators               | 80.1 ms                                                | 27.5 ms: 2.91x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.22 ms: 2.46x faster                                                 |
| async_tree_none          | 728 ms                                                 | 314 ms: 2.32x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 395 ms: 2.20x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 864 ms: 2.05x faster                                                  |
| go                       | 240 ms                                                 | 118 ms: 2.04x faster                                                  |
| chaos                    | 115 ms                                                 | 58.5 ms: 1.97x faster                                                 |
| deepcopy_memo            | 58.5 us                                                | 29.7 us: 1.97x faster                                                 |
| raytrace                 | 507 ms                                                 | 259 ms: 1.96x faster                                                  |
| asyncio_tcp              | 922 ms                                                 | 472 ms: 1.95x faster                                                  |
| logging_silent           | 190 ns                                                 | 98.2 ns: 1.93x faster                                                 |
| deepcopy                 | 479 us                                                 | 257 us: 1.86x faster                                                  |
| richards_super           | 94.7 ms                                                | 52.7 ms: 1.80x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 566 ms: 1.79x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 71.7 ms: 1.78x faster                                                 |
| nbody                    | 154 ms                                                 | 86.5 ms: 1.77x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 67.1 ms: 1.76x faster                                                 |
| comprehensions           | 28.8 us                                                | 16.3 us: 1.76x faster                                                 |
| scimark_sor              | 220 ms                                                 | 126 ms: 1.74x faster                                                  |
| pylint                   | 551 ms                                                 | 320 ms: 1.72x faster                                                  |
| richards                 | 79.3 ms                                                | 46.8 ms: 1.70x faster                                                 |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.69x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.17 ms: 1.68x faster                                                 |
| sqlglot_transpile        | 2.57 ms                                                | 1.58 ms: 1.63x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 303 us: 1.60x faster                                                  |
| pyflate                  | 716 ms                                                 | 454 ms: 1.58x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.65 us: 1.58x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 211 us: 1.56x faster                                                  |
| scimark_lu               | 176 ms                                                 | 113 ms: 1.56x faster                                                  |
| spectral_norm            | 170 ms                                                 | 111 ms: 1.53x faster                                                  |
| coroutines               | 35.1 ms                                                | 23.2 ms: 1.51x faster                                                 |
| tornado_http             | 136 ms                                                 | 90.8 ms: 1.50x faster                                                 |
| float                    | 117 ms                                                 | 78.1 ms: 1.50x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 2.11 sec: 1.49x faster                                                |
| logging_simple           | 8.30 us                                                | 5.61 us: 1.48x faster                                                 |
| regex_compile            | 188 ms                                                 | 128 ms: 1.47x faster                                                  |
| mako                     | 16.3 ms                                                | 11.1 ms: 1.47x faster                                                 |
| logging_format           | 9.09 us                                                | 6.22 us: 1.46x faster                                                 |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.79 sec: 1.44x faster                                                |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                                |
| django_template          | 48.2 ms                                                | 34.1 ms: 1.41x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 725 ms: 1.40x faster                                                  |
| html5lib                 | 88.9 ms                                                | 63.3 ms: 1.40x faster                                                 |
| thrift                   | 1.07 ms                                                | 764 us: 1.40x faster                                                  |
| genshi_text              | 31.8 ms                                                | 22.8 ms: 1.40x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.39x faster                                                |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.67 ms: 1.38x faster                                                 |
| 2to3                     | 348 ms                                                 | 254 ms: 1.37x faster                                                  |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 58.9 ms: 1.34x faster                                                 |
| fannkuch                 | 532 ms                                                 | 397 ms: 1.34x faster                                                  |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.33x faster                                                  |
| sqlglot_normalize        | 143 ms                                                 | 107 ms: 1.33x faster                                                  |
| nqueens                  | 106 ms                                                 | 80.5 ms: 1.32x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 19.6 ms: 1.31x faster                                                 |
| unpack_sequence          | 60.0 ns                                                | 45.7 ns: 1.31x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 64.6 ms: 1.30x faster                                                 |
| sqlglot_optimize         | 69.2 ms                                                | 53.2 ms: 1.30x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 50.9 ms: 1.30x faster                                                 |
| pathlib                  | 20.5 ms                                                | 15.8 ms: 1.29x faster                                                 |
| scimark_fft              | 466 ms                                                 | 362 ms: 1.29x faster                                                  |
| sympy_str                | 346 ms                                                 | 269 ms: 1.28x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 792 us: 1.25x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.66 sec: 1.24x faster                                                |
| sympy_expand             | 566 ms                                                 | 456 ms: 1.24x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 85.0 ms: 1.17x faster                                                 |
| json_loads               | 31.2 us                                                | 26.7 us: 1.17x faster                                                 |
| json                     | 5.69 ms                                                | 4.96 ms: 1.15x faster                                                 |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 24.6 ms: 1.13x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 104 ms: 1.11x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 154 ms: 1.09x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.65 sec: 1.07x faster                                                |
| sqlite_synth             | 3.02 us                                                | 2.87 us: 1.06x faster                                                 |
| regex_dna                | 227 ms                                                 | 218 ms: 1.04x faster                                                  |
| async_generators         | 444 ms                                                 | 432 ms: 1.03x faster                                                  |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 554 ms: 1.01x faster                                                  |
| pickle_list              | 5.08 us                                                | 5.14 us: 1.01x slower                                                 |
| regex_effbot             | 3.63 ms                                                | 3.72 ms: 1.02x slower                                                 |
| unpickle                 | 14.4 us                                                | 14.9 us: 1.04x slower                                                 |
| coverage                 | 79.4 ms                                                | 84.6 ms: 1.07x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 1.73 ms: 1.07x slower                                                 |
| pickle                   | 10.7 us                                                | 11.5 us: 1.08x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 3.98 ms: 1.10x slower                                                 |
| pickle_dict              | 29.6 us                                                | 33.9 us: 1.15x slower                                                 |
| telco                    | 7.27 ms                                                | 8.53 ms: 1.17x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 6.99 ms: 1.18x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                          |

Benchmark hidden because not significant (2): unpickle_list, bench_mp_pool
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240912-3.14.0a0-4ed7d1d/bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.35x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.12x