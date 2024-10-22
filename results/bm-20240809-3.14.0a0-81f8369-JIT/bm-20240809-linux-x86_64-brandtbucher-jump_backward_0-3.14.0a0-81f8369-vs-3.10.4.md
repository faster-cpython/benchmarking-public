# Results vs. 3.10.4

- fork: brandtbucher
- ref: jump_backward_0
- machine: linux-x86_64
- commit hash: 81f8369
- commit date: 2024-08-09
- overall geometric mean: 1.40x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 283 ms: 1.23x faster                                                   |
| docutils       | 3.30 sec                                               | 3.08 sec: 1.07x faster                                                 |
| html5lib       | 88.9 ms                                                | 64.2 ms: 1.38x faster                                                  |
| tornado_http   | 136 ms                                                 | 107 ms: 1.27x faster                                                   |
| Geometric mean | (ref)                                                  | 1.23x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 333 ms: 2.19x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 434 ms: 2.00x faster                                                   |
| async_tree_io           | 1.77 sec                                               | 921 ms: 1.92x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 571 ms: 1.78x faster                                                   |
| Geometric mean          | (ref)                                                  | 1.97x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 79.6 ms: 1.93x faster                                                  |
| float          | 117 ms                                                 | 69.0 ms: 1.70x faster                                                  |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                  | 1.50x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 138 ms: 1.37x faster                                                   |
| regex_v8       | 27.8 ms                                                | 24.2 ms: 1.15x faster                                                  |
| regex_dna      | 227 ms                                                 | 212 ms: 1.07x faster                                                   |
| Geometric mean | (ref)                                                  | 1.14x faster                                                           |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 293 us: 1.65x faster                                                   |
| tomli_loads          | 3.14 sec                                               | 1.94 sec: 1.62x faster                                                 |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.52x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 54.7 ms: 1.45x faster                                                  |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.37x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 80.0 ms: 1.24x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 99.2 ms: 1.16x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                                   |
| json_loads           | 31.2 us                                                | 27.2 us: 1.15x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.36x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.37x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 7.16 ms: 1.21x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.84 ms: 1.66x faster                                                  |
| genshi_text     | 31.8 ms                                                | 23.9 ms: 1.33x faster                                                  |
| django_template | 48.2 ms                                                | 39.3 ms: 1.22x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 55.1 ms: 1.20x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.34x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 170 us: 3.20x faster                                                   |
| generators               | 80.1 ms                                                | 35.1 ms: 2.28x faster                                                  |
| async_tree_none          | 728 ms                                                 | 333 ms: 2.19x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 28.8 us: 2.03x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 434 ms: 2.00x faster                                                   |
| chaos                    | 115 ms                                                 | 57.7 ms: 2.00x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 59.8 ms: 1.98x faster                                                  |
| scimark_sor              | 220 ms                                                 | 113 ms: 1.94x faster                                                   |
| logging_silent           | 190 ns                                                 | 98.3 ns: 1.93x faster                                                  |
| nbody                    | 154 ms                                                 | 79.6 ms: 1.93x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 921 ms: 1.92x faster                                                   |
| crypto_pyaes             | 128 ms                                                 | 66.6 ms: 1.92x faster                                                  |
| deltablue                | 7.91 ms                                                | 4.24 ms: 1.87x faster                                                  |
| richards_super           | 94.7 ms                                                | 51.7 ms: 1.83x faster                                                  |
| raytrace                 | 507 ms                                                 | 277 ms: 1.83x faster                                                   |
| comprehensions           | 28.8 us                                                | 16.1 us: 1.78x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 571 ms: 1.78x faster                                                   |
| deepcopy                 | 479 us                                                 | 270 us: 1.77x faster                                                   |
| asyncio_tcp              | 922 ms                                                 | 530 ms: 1.74x faster                                                   |
| richards                 | 79.3 ms                                                | 46.0 ms: 1.72x faster                                                  |
| float                    | 117 ms                                                 | 69.0 ms: 1.70x faster                                                  |
| mako                     | 16.3 ms                                                | 9.84 ms: 1.66x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 293 us: 1.65x faster                                                   |
| spectral_norm            | 170 ms                                                 | 103 ms: 1.65x faster                                                   |
| tomli_loads              | 3.14 sec                                               | 1.94 sec: 1.62x faster                                                 |
| pyflate                  | 716 ms                                                 | 444 ms: 1.61x faster                                                   |
| scimark_lu               | 176 ms                                                 | 109 ms: 1.61x faster                                                   |
| go                       | 240 ms                                                 | 150 ms: 1.60x faster                                                   |
| sqlglot_parse            | 2.17 ms                                                | 1.37 ms: 1.58x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.52x faster                                                   |
| hexiom                   | 10.4 ms                                                | 6.83 ms: 1.52x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.30 ms: 1.51x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.80 us: 1.49x faster                                                  |
| scimark_fft              | 466 ms                                                 | 313 ms: 1.49x faster                                                   |
| logging_format           | 9.09 us                                                | 6.12 us: 1.49x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.73 ms: 1.49x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.66 us: 1.47x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 54.7 ms: 1.45x faster                                                  |
| fannkuch                 | 532 ms                                                 | 372 ms: 1.43x faster                                                   |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.83 sec: 1.41x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 728 ms: 1.40x faster                                                   |
| coroutines               | 35.1 ms                                                | 25.2 ms: 1.39x faster                                                  |
| html5lib                 | 88.9 ms                                                | 64.2 ms: 1.38x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.52 sec: 1.38x faster                                                 |
| pylint                   | 551 ms                                                 | 401 ms: 1.37x faster                                                   |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.37x faster                                                  |
| regex_compile            | 188 ms                                                 | 138 ms: 1.37x faster                                                   |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.37x faster                                                  |
| genshi_text              | 31.8 ms                                                | 23.9 ms: 1.33x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.19 sec: 1.32x faster                                                 |
| thrift                   | 1.07 ms                                                | 823 us: 1.30x faster                                                   |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.29x faster                                                  |
| tornado_http             | 136 ms                                                 | 107 ms: 1.27x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 80.0 ms: 1.24x faster                                                  |
| sqlglot_normalize        | 143 ms                                                 | 115 ms: 1.24x faster                                                   |
| nqueens                  | 106 ms                                                 | 85.4 ms: 1.24x faster                                                  |
| 2to3                     | 348 ms                                                 | 283 ms: 1.23x faster                                                   |
| django_template          | 48.2 ms                                                | 39.3 ms: 1.22x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 55.1 ms: 1.20x faster                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 58.1 ms: 1.19x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 99.2 ms: 1.16x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                                   |
| json_loads               | 31.2 us                                                | 27.2 us: 1.15x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 24.2 ms: 1.15x faster                                                  |
| json                     | 5.69 ms                                                | 5.03 ms: 1.13x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 883 us: 1.12x faster                                                   |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                   |
| sympy_str                | 346 ms                                                 | 320 ms: 1.08x faster                                                   |
| docutils                 | 3.30 sec                                               | 3.08 sec: 1.07x faster                                                 |
| regex_dna                | 227 ms                                                 | 212 ms: 1.07x faster                                                   |
| sympy_expand             | 566 ms                                                 | 530 ms: 1.07x faster                                                   |
| mdp                      | 2.85 sec                                               | 2.67 sec: 1.07x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 25.0 ms: 1.03x faster                                                  |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                   |
| gc_traversal             | 3.62 ms                                                | 3.71 ms: 1.02x slower                                                  |
| async_generators         | 444 ms                                                 | 457 ms: 1.03x slower                                                   |
| telco                    | 7.27 ms                                                | 7.75 ms: 1.07x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 1.79 ms: 1.10x slower                                                  |
| coverage                 | 79.4 ms                                                | 92.7 ms: 1.17x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 7.16 ms: 1.21x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                           |

Benchmark hidden because not significant (4): regex_effbot, bench_mp_pool, asyncio_websockets, sympy_sum
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240809-3.14.0a0-81f8369-JIT/bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.28x