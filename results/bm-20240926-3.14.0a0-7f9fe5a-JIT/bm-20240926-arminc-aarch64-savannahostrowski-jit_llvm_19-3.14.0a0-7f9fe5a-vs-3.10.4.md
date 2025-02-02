# Results vs. 3.10.4

- fork: savannahostrowski
- ref: jit_llvm_19
- machine: linux-aarch64
- commit hash: 7f9fe5a
- commit date: 2024-09-26
- overall geometric mean: 1.193x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 374 ms: 1.02x faster                                                      |
| docutils       | 3.53 sec                                                              | 3.85 sec: 1.09x slower                                                    |
| html5lib       | 86.5 ms                                                               | 71.3 ms: 1.21x faster                                                     |
| tornado_http   | 178 ms                                                                | 146 ms: 1.22x faster                                                      |
| Geometric mean | (ref)                                                                 | 1.08x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|-------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 435 ms: 2.19x faster                                                      |
| async_tree_io           | 2.28 sec                                                              | 1.15 sec: 1.99x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 582 ms: 1.95x faster                                                      |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 746 ms: 1.70x faster                                                      |
| Geometric mean          | (ref)                                                                 | 1.95x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 87.4 ms: 1.54x faster                                                     |
| nbody          | 166 ms                                                                | 113 ms: 1.46x faster                                                      |
| Geometric mean | (ref)                                                                 | 1.31x faster                                                              |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 31.0 ms: 1.04x faster                                                     |
| regex_dna      | 257 ms                                                                | 259 ms: 1.01x slower                                                      |
| regex_compile  | 177 ms                                                                | 189 ms: 1.07x slower                                                      |
| regex_effbot   | 4.25 ms                                                               | 5.00 ms: 1.18x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 377 us: 1.40x faster                                                      |
| unpickle_pure_python | 366 us                                                                | 263 us: 1.39x faster                                                      |
| tomli_loads          | 3.36 sec                                                              | 2.58 sec: 1.30x faster                                                    |
| xml_etree_process    | 99.5 ms                                                               | 79.0 ms: 1.26x faster                                                     |
| json_dumps           | 16.7 ms                                                               | 13.5 ms: 1.24x faster                                                     |
| xml_etree_parse      | 212 ms                                                                | 191 ms: 1.11x faster                                                      |
| unpickle_list        | 6.99 us                                                               | 6.40 us: 1.09x faster                                                     |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.08x faster                                                      |
| xml_etree_iterparse  | 156 ms                                                                | 148 ms: 1.05x faster                                                      |
| pickle_list          | 5.24 us                                                               | 5.16 us: 1.02x faster                                                     |
| json_loads           | 30.9 us                                                               | 31.4 us: 1.01x slower                                                     |
| pickle_dict          | 35.1 us                                                               | 38.4 us: 1.09x slower                                                     |
| pickle               | 12.5 us                                                               | 13.6 us: 1.09x slower                                                     |
| unpickle             | 17.5 us                                                               | 19.3 us: 1.10x slower                                                     |
| Geometric mean       | (ref)                                                                 | 1.11x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.1 ms: 1.17x slower                                                     |
| python_startup_no_site | 6.89 ms                                                               | 8.72 ms: 1.27x slower                                                     |
| Geometric mean         | (ref)                                                                 | 1.22x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.0 ms: 1.45x faster                                                     |
| django_template | 53.3 ms                                                               | 50.0 ms: 1.07x faster                                                     |
| genshi_text     | 35.2 ms                                                               | 34.6 ms: 1.02x faster                                                     |
| genshi_xml      | 69.8 ms                                                               | 80.5 ms: 1.15x slower                                                     |
| Geometric mean  | (ref)                                                                 | 1.08x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 207 us: 3.20x faster                                                      |
| async_tree_none          | 950 ms                                                                | 435 ms: 2.19x faster                                                      |
| deltablue                | 8.94 ms                                                               | 4.34 ms: 2.06x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 1.15 sec: 1.99x faster                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 7.42 ms: 1.96x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 582 ms: 1.95x faster                                                      |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 746 ms: 1.70x faster                                                      |
| deepcopy_memo            | 61.7 us                                                               | 36.5 us: 1.69x faster                                                     |
| raytrace                 | 573 ms                                                                | 342 ms: 1.68x faster                                                      |
| scimark_sor              | 246 ms                                                                | 150 ms: 1.65x faster                                                      |
| logging_silent           | 222 ns                                                                | 136 ns: 1.63x faster                                                      |
| asyncio_tcp              | 944 ms                                                                | 610 ms: 1.55x faster                                                      |
| float                    | 135 ms                                                                | 87.4 ms: 1.54x faster                                                     |
| crypto_pyaes             | 134 ms                                                                | 87.9 ms: 1.52x faster                                                     |
| scimark_lu               | 227 ms                                                                | 149 ms: 1.52x faster                                                      |
| richards_super           | 107 ms                                                                | 72.8 ms: 1.47x faster                                                     |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.23 sec: 1.47x faster                                                    |
| nbody                    | 166 ms                                                                | 113 ms: 1.46x faster                                                      |
| mako                     | 18.9 ms                                                               | 13.0 ms: 1.45x faster                                                     |
| go                       | 264 ms                                                                | 185 ms: 1.43x faster                                                      |
| richards                 | 91.7 ms                                                               | 64.8 ms: 1.42x faster                                                     |
| pickle_pure_python       | 529 us                                                                | 377 us: 1.40x faster                                                      |
| scimark_monte_carlo      | 128 ms                                                                | 91.0 ms: 1.40x faster                                                     |
| sqlglot_parse            | 2.40 ms                                                               | 1.72 ms: 1.40x faster                                                     |
| unpickle_pure_python     | 366 us                                                                | 263 us: 1.39x faster                                                      |
| comprehensions           | 33.1 us                                                               | 24.1 us: 1.38x faster                                                     |
| chaos                    | 121 ms                                                                | 88.7 ms: 1.37x faster                                                     |
| deepcopy                 | 511 us                                                                | 385 us: 1.32x faster                                                      |
| sqlglot_transpile        | 2.84 ms                                                               | 2.16 ms: 1.32x faster                                                     |
| thrift                   | 1.26 ms                                                               | 961 us: 1.31x faster                                                      |
| logging_simple           | 9.78 us                                                               | 7.48 us: 1.31x faster                                                     |
| coroutines               | 37.2 ms                                                               | 28.4 ms: 1.31x faster                                                     |
| tomli_loads              | 3.36 sec                                                              | 2.58 sec: 1.30x faster                                                    |
| logging_format           | 10.6 us                                                               | 8.19 us: 1.30x faster                                                     |
| spectral_norm            | 186 ms                                                                | 144 ms: 1.29x faster                                                      |
| pyflate                  | 795 ms                                                                | 623 ms: 1.28x faster                                                      |
| xml_etree_process        | 99.5 ms                                                               | 79.0 ms: 1.26x faster                                                     |
| json_dumps               | 16.7 ms                                                               | 13.5 ms: 1.24x faster                                                     |
| tornado_http             | 178 ms                                                                | 146 ms: 1.22x faster                                                      |
| deepcopy_reduce          | 4.60 us                                                               | 3.79 us: 1.21x faster                                                     |
| html5lib                 | 86.5 ms                                                               | 71.3 ms: 1.21x faster                                                     |
| pathlib                  | 26.3 ms                                                               | 21.8 ms: 1.21x faster                                                     |
| generators               | 68.1 ms                                                               | 56.9 ms: 1.20x faster                                                     |
| bench_thread_pool        | 1.59 ms                                                               | 1.33 ms: 1.19x faster                                                     |
| pycparser                | 1.69 sec                                                              | 1.48 sec: 1.15x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.80 ms: 1.12x faster                                                     |
| scimark_fft              | 500 ms                                                                | 448 ms: 1.12x faster                                                      |
| fannkuch                 | 546 ms                                                                | 490 ms: 1.11x faster                                                      |
| xml_etree_parse          | 212 ms                                                                | 191 ms: 1.11x faster                                                      |
| hexiom                   | 10.9 ms                                                               | 9.84 ms: 1.11x faster                                                     |
| unpickle_list            | 6.99 us                                                               | 6.40 us: 1.09x faster                                                     |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.08x faster                                                      |
| sqlite_synth             | 4.12 us                                                               | 3.80 us: 1.08x faster                                                     |
| django_template          | 53.3 ms                                                               | 50.0 ms: 1.07x faster                                                     |
| mdp                      | 3.70 sec                                                              | 3.47 sec: 1.07x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 148 ms: 1.05x faster                                                      |
| sqlglot_normalize        | 156 ms                                                                | 149 ms: 1.05x faster                                                      |
| json                     | 5.88 ms                                                               | 5.65 ms: 1.04x faster                                                     |
| regex_v8                 | 32.2 ms                                                               | 31.0 ms: 1.04x faster                                                     |
| meteor_contest           | 126 ms                                                                | 123 ms: 1.02x faster                                                      |
| 2to3                     | 381 ms                                                                | 374 ms: 1.02x faster                                                      |
| genshi_text              | 35.2 ms                                                               | 34.6 ms: 1.02x faster                                                     |
| pickle_list              | 5.24 us                                                               | 5.16 us: 1.02x faster                                                     |
| regex_dna                | 257 ms                                                                | 259 ms: 1.01x slower                                                      |
| asyncio_websockets       | 657 ms                                                                | 661 ms: 1.01x slower                                                      |
| json_loads               | 30.9 us                                                               | 31.4 us: 1.01x slower                                                     |
| nqueens                  | 117 ms                                                                | 119 ms: 1.01x slower                                                      |
| create_gc_cycles         | 2.26 ms                                                               | 2.32 ms: 1.03x slower                                                     |
| sqlglot_optimize         | 75.4 ms                                                               | 79.0 ms: 1.05x slower                                                     |
| pprint_safe_repr         | 1.15 sec                                                              | 1.21 sec: 1.06x slower                                                    |
| pprint_pformat           | 2.36 sec                                                              | 2.50 sec: 1.06x slower                                                    |
| sympy_integrate          | 26.5 ms                                                               | 28.2 ms: 1.06x slower                                                     |
| regex_compile            | 177 ms                                                                | 189 ms: 1.07x slower                                                      |
| sympy_str                | 329 ms                                                                | 359 ms: 1.09x slower                                                      |
| docutils                 | 3.53 sec                                                              | 3.85 sec: 1.09x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 38.4 us: 1.09x slower                                                     |
| pickle                   | 12.5 us                                                               | 13.6 us: 1.09x slower                                                     |
| unpickle                 | 17.5 us                                                               | 19.3 us: 1.10x slower                                                     |
| sympy_expand             | 543 ms                                                                | 600 ms: 1.11x slower                                                      |
| async_generators         | 452 ms                                                                | 506 ms: 1.12x slower                                                      |
| dulwich_log              | 73.5 ms                                                               | 82.2 ms: 1.12x slower                                                     |
| sympy_sum                | 184 ms                                                                | 208 ms: 1.13x slower                                                      |
| genshi_xml               | 69.8 ms                                                               | 80.5 ms: 1.15x slower                                                     |
| python_startup           | 11.2 ms                                                               | 13.1 ms: 1.17x slower                                                     |
| regex_effbot             | 4.25 ms                                                               | 5.00 ms: 1.18x slower                                                     |
| telco                    | 8.49 ms                                                               | 10.0 ms: 1.18x slower                                                     |
| coverage                 | 83.6 ms                                                               | 100 ms: 1.20x slower                                                      |
| gc_traversal             | 4.15 ms                                                               | 5.19 ms: 1.25x slower                                                     |
| python_startup_no_site   | 6.89 ms                                                               | 8.72 ms: 1.27x slower                                                     |
| Geometric mean           | (ref)                                                                 | 1.19x faster                                                              |

Benchmark hidden because not significant (2): pylint, pidigits
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240926-3.14.0a0-7f9fe5a-JIT/bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence

- Geometric mean (including insignificant results): 1.193x faster
# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.25x