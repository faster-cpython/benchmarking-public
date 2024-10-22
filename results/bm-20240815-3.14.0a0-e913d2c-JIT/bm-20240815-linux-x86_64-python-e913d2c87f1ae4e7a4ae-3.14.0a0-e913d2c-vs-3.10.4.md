# Results vs. 3.10.4

- fork: python
- ref: e913d2c87f1ae4e7a4ae
- machine: linux-x86_64
- commit hash: e913d2c
- commit date: 2024-08-15
- overall geometric mean: 1.42x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 279 ms: 1.25x faster                                                  |
| docutils       | 3.30 sec                                               | 3.01 sec: 1.10x faster                                                |
| html5lib       | 88.9 ms                                                | 67.2 ms: 1.32x faster                                                 |
| tornado_http   | 136 ms                                                 | 93.4 ms: 1.46x faster                                                 |
| Geometric mean | (ref)                                                  | 1.27x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 323 ms: 2.25x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 427 ms: 2.04x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 905 ms: 1.95x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 570 ms: 1.78x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.00x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.0 ms: 1.92x faster                                                 |
| float          | 117 ms                                                 | 70.7 ms: 1.66x faster                                                 |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.49x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 142 ms: 1.32x faster                                                  |
| regex_v8       | 27.8 ms                                                | 24.5 ms: 1.13x faster                                                 |
| regex_dna      | 227 ms                                                 | 221 ms: 1.03x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.75 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.93 sec: 1.63x faster                                                |
| pickle_pure_python   | 484 us                                                 | 302 us: 1.60x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 212 us: 1.56x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 57.5 ms: 1.38x faster                                                 |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 81.6 ms: 1.22x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 98.4 ms: 1.17x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 147 ms: 1.14x faster                                                  |
| json_loads           | 31.2 us                                                | 28.6 us: 1.09x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.34x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.12 ms: 1.20x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.98 ms: 1.63x faster                                                 |
| django_template | 48.2 ms                                                | 36.8 ms: 1.31x faster                                                 |
| genshi_text     | 31.8 ms                                                | 26.6 ms: 1.20x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 59.9 ms: 1.10x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.30x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 174 us: 3.13x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.11 ms: 2.54x faster                                                 |
| generators               | 80.1 ms                                                | 32.6 ms: 2.46x faster                                                 |
| async_tree_none          | 728 ms                                                 | 323 ms: 2.25x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 27.0 us: 2.17x faster                                                 |
| richards_super           | 94.7 ms                                                | 44.7 ms: 2.12x faster                                                 |
| async_tree_memoization   | 870 ms                                                 | 427 ms: 2.04x faster                                                  |
| richards                 | 79.3 ms                                                | 39.4 ms: 2.01x faster                                                 |
| chaos                    | 115 ms                                                 | 58.3 ms: 1.98x faster                                                 |
| async_tree_io            | 1.77 sec                                               | 905 ms: 1.95x faster                                                  |
| scimark_sor              | 220 ms                                                 | 114 ms: 1.93x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 66.4 ms: 1.92x faster                                                 |
| raytrace                 | 507 ms                                                 | 264 ms: 1.92x faster                                                  |
| nbody                    | 154 ms                                                 | 80.0 ms: 1.92x faster                                                 |
| logging_silent           | 190 ns                                                 | 101 ns: 1.87x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 63.6 ms: 1.86x faster                                                 |
| asyncio_tcp              | 922 ms                                                 | 499 ms: 1.85x faster                                                  |
| deepcopy                 | 479 us                                                 | 263 us: 1.82x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 570 ms: 1.78x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.74x faster                                                 |
| spectral_norm            | 170 ms                                                 | 102 ms: 1.66x faster                                                  |
| float                    | 117 ms                                                 | 70.7 ms: 1.66x faster                                                 |
| go                       | 240 ms                                                 | 145 ms: 1.66x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.32 ms: 1.65x faster                                                 |
| mako                     | 16.3 ms                                                | 9.98 ms: 1.63x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 1.93 sec: 1.63x faster                                                |
| scimark_lu               | 176 ms                                                 | 109 ms: 1.62x faster                                                  |
| pyflate                  | 716 ms                                                 | 445 ms: 1.61x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 302 us: 1.60x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.64 us: 1.58x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 212 us: 1.56x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.68 ms: 1.53x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.81 ms: 1.53x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.47 us: 1.52x faster                                                 |
| logging_format           | 9.09 us                                                | 6.00 us: 1.52x faster                                                 |
| scimark_fft              | 466 ms                                                 | 308 ms: 1.51x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.31 ms: 1.50x faster                                                 |
| coroutines               | 35.1 ms                                                | 23.4 ms: 1.50x faster                                                 |
| pylint                   | 551 ms                                                 | 368 ms: 1.50x faster                                                  |
| tornado_http             | 136 ms                                                 | 93.4 ms: 1.46x faster                                                 |
| fannkuch                 | 532 ms                                                 | 369 ms: 1.44x faster                                                  |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.42x faster                                                |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 57.5 ms: 1.38x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 743 ms: 1.37x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.54 sec: 1.36x faster                                                |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                 |
| thrift                   | 1.07 ms                                                | 797 us: 1.34x faster                                                  |
| regex_compile            | 188 ms                                                 | 142 ms: 1.32x faster                                                  |
| html5lib                 | 88.9 ms                                                | 67.2 ms: 1.32x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.20 sec: 1.32x faster                                                |
| django_template          | 48.2 ms                                                | 36.8 ms: 1.31x faster                                                 |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                                 |
| sqlglot_normalize        | 143 ms                                                 | 113 ms: 1.26x faster                                                  |
| 2to3                     | 348 ms                                                 | 279 ms: 1.25x faster                                                  |
| nqueens                  | 106 ms                                                 | 85.2 ms: 1.24x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 81.6 ms: 1.22x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 817 us: 1.21x faster                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 57.8 ms: 1.20x faster                                                 |
| genshi_text              | 31.8 ms                                                | 26.6 ms: 1.20x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 98.4 ms: 1.17x faster                                                 |
| sympy_str                | 346 ms                                                 | 301 ms: 1.15x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 147 ms: 1.14x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 24.5 ms: 1.13x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 22.9 ms: 1.13x faster                                                 |
| mdp                      | 2.85 sec                                               | 2.54 sec: 1.12x faster                                                |
| sympy_sum                | 196 ms                                                 | 175 ms: 1.12x faster                                                  |
| sympy_expand             | 566 ms                                                 | 506 ms: 1.12x faster                                                  |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.11x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 59.9 ms: 1.10x faster                                                 |
| docutils                 | 3.30 sec                                               | 3.01 sec: 1.10x faster                                                |
| json_loads               | 31.2 us                                                | 28.6 us: 1.09x faster                                                 |
| json                     | 5.69 ms                                                | 5.32 ms: 1.07x faster                                                 |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                                  |
| regex_dna                | 227 ms                                                 | 221 ms: 1.03x faster                                                  |
| gc_traversal             | 3.62 ms                                                | 3.67 ms: 1.01x slower                                                 |
| async_generators         | 444 ms                                                 | 452 ms: 1.02x slower                                                  |
| regex_effbot             | 3.63 ms                                                | 3.75 ms: 1.03x slower                                                 |
| telco                    | 7.27 ms                                                | 7.76 ms: 1.07x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 1.75 ms: 1.08x slower                                                 |
| coverage                 | 79.4 ms                                                | 87.5 ms: 1.10x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.12 ms: 1.20x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                          |

Benchmark hidden because not significant (2): asyncio_websockets, bench_mp_pool
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240815-3.14.0a0-e913d2c-JIT/bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.21x