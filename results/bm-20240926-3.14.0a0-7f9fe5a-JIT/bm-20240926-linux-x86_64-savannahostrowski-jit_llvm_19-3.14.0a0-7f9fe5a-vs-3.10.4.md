# Results vs. 3.10.4

- fork: savannahostrowski
- ref: jit_llvm_19
- machine: linux-x86_64
- commit hash: 7f9fe5a
- commit date: 2024-09-26
- overall geometric mean: 1.38x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 274 ms: 1.27x faster                                                    |
| docutils       | 3.30 sec                                               | 2.94 sec: 1.12x faster                                                  |
| html5lib       | 88.9 ms                                                | 62.0 ms: 1.43x faster                                                   |
| tornado_http   | 136 ms                                                 | 94.6 ms: 1.44x faster                                                   |
| Geometric mean | (ref)                                                  | 1.31x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 315 ms: 2.31x faster                                                    |
| async_tree_memoization  | 870 ms                                                 | 397 ms: 2.19x faster                                                    |
| async_tree_io           | 1.77 sec                                               | 885 ms: 2.00x faster                                                    |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 572 ms: 1.78x faster                                                    |
| Geometric mean          | (ref)                                                  | 2.06x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 81.8 ms: 1.88x faster                                                   |
| float          | 117 ms                                                 | 70.1 ms: 1.67x faster                                                   |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                  | 1.48x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 142 ms: 1.32x faster                                                    |
| regex_v8       | 27.8 ms                                                | 24.2 ms: 1.15x faster                                                   |
| regex_dna      | 227 ms                                                 | 212 ms: 1.07x faster                                                    |
| regex_effbot   | 3.63 ms                                                | 3.72 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                  | 1.12x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.96 sec: 1.60x faster                                                  |
| pickle_pure_python   | 484 us                                                 | 307 us: 1.58x faster                                                    |
| unpickle_pure_python | 331 us                                                 | 215 us: 1.54x faster                                                    |
| xml_etree_process    | 79.1 ms                                                | 55.0 ms: 1.44x faster                                                   |
| json_dumps           | 14.2 ms                                                | 10.1 ms: 1.41x faster                                                   |
| xml_etree_generate   | 99.4 ms                                                | 78.1 ms: 1.27x faster                                                   |
| xml_etree_iterparse  | 115 ms                                                 | 98.6 ms: 1.17x faster                                                   |
| xml_etree_parse      | 168 ms                                                 | 147 ms: 1.15x faster                                                    |
| json_loads           | 31.2 us                                                | 27.2 us: 1.15x faster                                                   |
| unpickle_list        | 5.20 us                                                | 5.30 us: 1.02x slower                                                   |
| pickle_list          | 5.08 us                                                | 5.20 us: 1.02x slower                                                   |
| pickle               | 10.7 us                                                | 11.6 us: 1.09x slower                                                   |
| pickle_dict          | 29.6 us                                                | 33.3 us: 1.12x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                            |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                   |
| python_startup_no_site | 5.93 ms                                                | 7.08 ms: 1.19x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.1 ms: 1.62x faster                                                   |
| django_template | 48.2 ms                                                | 35.5 ms: 1.36x faster                                                   |
| genshi_text     | 31.8 ms                                                | 24.4 ms: 1.30x faster                                                   |
| genshi_xml      | 66.0 ms                                                | 57.2 ms: 1.15x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 162 us: 3.36x faster                                                    |
| deltablue                | 7.91 ms                                                | 3.19 ms: 2.48x faster                                                   |
| generators               | 80.1 ms                                                | 33.1 ms: 2.42x faster                                                   |
| async_tree_none          | 728 ms                                                 | 315 ms: 2.31x faster                                                    |
| deepcopy_memo            | 58.5 us                                                | 26.7 us: 2.19x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 397 ms: 2.19x faster                                                    |
| richards_super           | 94.7 ms                                                | 44.9 ms: 2.11x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 885 ms: 2.00x faster                                                    |
| richards                 | 79.3 ms                                                | 39.8 ms: 1.99x faster                                                   |
| chaos                    | 115 ms                                                 | 59.7 ms: 1.93x faster                                                   |
| crypto_pyaes             | 128 ms                                                 | 66.8 ms: 1.91x faster                                                   |
| scimark_monte_carlo      | 118 ms                                                 | 62.8 ms: 1.88x faster                                                   |
| scimark_sor              | 220 ms                                                 | 117 ms: 1.88x faster                                                    |
| asyncio_tcp              | 922 ms                                                 | 491 ms: 1.88x faster                                                    |
| nbody                    | 154 ms                                                 | 81.8 ms: 1.88x faster                                                   |
| raytrace                 | 507 ms                                                 | 276 ms: 1.84x faster                                                    |
| deepcopy                 | 479 us                                                 | 261 us: 1.83x faster                                                    |
| go                       | 240 ms                                                 | 132 ms: 1.82x faster                                                    |
| logging_silent           | 190 ns                                                 | 104 ns: 1.82x faster                                                    |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 572 ms: 1.78x faster                                                    |
| comprehensions           | 28.8 us                                                | 16.4 us: 1.75x faster                                                   |
| spectral_norm            | 170 ms                                                 | 101 ms: 1.68x faster                                                    |
| float                    | 117 ms                                                 | 70.1 ms: 1.67x faster                                                   |
| sqlglot_parse            | 2.17 ms                                                | 1.33 ms: 1.63x faster                                                   |
| mako                     | 16.3 ms                                                | 10.1 ms: 1.62x faster                                                   |
| scimark_lu               | 176 ms                                                 | 109 ms: 1.61x faster                                                    |
| tomli_loads              | 3.14 sec                                               | 1.96 sec: 1.60x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 307 us: 1.58x faster                                                    |
| deepcopy_reduce          | 4.17 us                                                | 2.65 us: 1.58x faster                                                   |
| pyflate                  | 716 ms                                                 | 458 ms: 1.57x faster                                                    |
| sqlglot_transpile        | 2.57 ms                                                | 1.67 ms: 1.54x faster                                                   |
| unpickle_pure_python     | 331 us                                                 | 215 us: 1.54x faster                                                    |
| coroutines               | 35.1 ms                                                | 23.0 ms: 1.52x faster                                                   |
| hexiom                   | 10.4 ms                                                | 6.87 ms: 1.51x faster                                                   |
| logging_format           | 9.09 us                                                | 6.05 us: 1.50x faster                                                   |
| scimark_fft              | 466 ms                                                 | 312 ms: 1.49x faster                                                    |
| pylint                   | 551 ms                                                 | 370 ms: 1.49x faster                                                    |
| logging_simple           | 8.30 us                                                | 5.58 us: 1.49x faster                                                   |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.39 ms: 1.47x faster                                                   |
| tornado_http             | 136 ms                                                 | 94.6 ms: 1.44x faster                                                   |
| xml_etree_process        | 79.1 ms                                                | 55.0 ms: 1.44x faster                                                   |
| html5lib                 | 88.9 ms                                                | 62.0 ms: 1.43x faster                                                   |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                                  |
| json_dumps               | 14.2 ms                                                | 10.1 ms: 1.41x faster                                                   |
| fannkuch                 | 532 ms                                                 | 384 ms: 1.39x faster                                                    |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                   |
| pprint_pformat           | 2.10 sec                                               | 1.54 sec: 1.37x faster                                                  |
| thrift                   | 1.07 ms                                                | 787 us: 1.36x faster                                                    |
| django_template          | 48.2 ms                                                | 35.5 ms: 1.36x faster                                                   |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.35x faster                                                  |
| regex_compile            | 188 ms                                                 | 142 ms: 1.32x faster                                                    |
| pprint_safe_repr         | 1.02 sec                                               | 772 ms: 1.32x faster                                                    |
| genshi_text              | 31.8 ms                                                | 24.4 ms: 1.30x faster                                                   |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.28x faster                                                   |
| sqlglot_normalize        | 143 ms                                                 | 112 ms: 1.28x faster                                                    |
| xml_etree_generate       | 99.4 ms                                                | 78.1 ms: 1.27x faster                                                   |
| 2to3                     | 348 ms                                                 | 274 ms: 1.27x faster                                                    |
| dulwich_log              | 84.3 ms                                                | 67.9 ms: 1.24x faster                                                   |
| nqueens                  | 106 ms                                                 | 85.6 ms: 1.24x faster                                                   |
| sqlglot_optimize         | 69.2 ms                                                | 57.7 ms: 1.20x faster                                                   |
| bench_thread_pool        | 986 us                                                 | 841 us: 1.17x faster                                                    |
| xml_etree_iterparse      | 115 ms                                                 | 98.6 ms: 1.17x faster                                                   |
| sympy_str                | 346 ms                                                 | 298 ms: 1.16x faster                                                    |
| genshi_xml               | 66.0 ms                                                | 57.2 ms: 1.15x faster                                                   |
| regex_v8                 | 27.8 ms                                                | 24.2 ms: 1.15x faster                                                   |
| xml_etree_parse          | 168 ms                                                 | 147 ms: 1.15x faster                                                    |
| json_loads               | 31.2 us                                                | 27.2 us: 1.15x faster                                                   |
| sympy_sum                | 196 ms                                                 | 172 ms: 1.14x faster                                                    |
| sympy_integrate          | 25.8 ms                                                | 22.7 ms: 1.14x faster                                                   |
| sympy_expand             | 566 ms                                                 | 502 ms: 1.13x faster                                                    |
| docutils                 | 3.30 sec                                               | 2.94 sec: 1.12x faster                                                  |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                    |
| json                     | 5.69 ms                                                | 5.11 ms: 1.11x faster                                                   |
| sqlite_synth             | 3.02 us                                                | 2.74 us: 1.10x faster                                                   |
| mdp                      | 2.85 sec                                               | 2.60 sec: 1.10x faster                                                  |
| regex_dna                | 227 ms                                                 | 212 ms: 1.07x faster                                                    |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                    |
| asyncio_websockets       | 559 ms                                                 | 556 ms: 1.01x faster                                                    |
| unpickle_list            | 5.20 us                                                | 5.30 us: 1.02x slower                                                   |
| pickle_list              | 5.08 us                                                | 5.20 us: 1.02x slower                                                   |
| async_generators         | 444 ms                                                 | 455 ms: 1.02x slower                                                    |
| regex_effbot             | 3.63 ms                                                | 3.72 ms: 1.03x slower                                                   |
| coverage                 | 79.4 ms                                                | 84.8 ms: 1.07x slower                                                   |
| telco                    | 7.27 ms                                                | 7.86 ms: 1.08x slower                                                   |
| create_gc_cycles         | 1.62 ms                                                | 1.76 ms: 1.08x slower                                                   |
| pickle                   | 10.7 us                                                | 11.6 us: 1.09x slower                                                   |
| gc_traversal             | 3.62 ms                                                | 3.97 ms: 1.10x slower                                                   |
| pickle_dict              | 29.6 us                                                | 33.3 us: 1.12x slower                                                   |
| python_startup_no_site   | 5.93 ms                                                | 7.08 ms: 1.19x slower                                                   |
| unpack_sequence          | 60.0 ns                                                | 112 ns: 1.86x slower                                                    |
| Geometric mean           | (ref)                                                  | 1.38x faster                                                            |

Benchmark hidden because not significant (2): bench_mp_pool, unpickle
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240926-3.14.0a0-7f9fe5a-JIT/bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.21x