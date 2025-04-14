# Results vs. 3.10.4

- fork: python
- ref: e82c2ca2a59235bc1965
- machine: linux-aarch64
- commit hash: e82c2ca
- commit date: 2025-03-15
- overall geometric mean: 1.349x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.35x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 291 ms: 1.31x faster                                                     |
| docutils       | 3.53 sec                                                              | 2.91 sec: 1.21x faster                                                   |
| html5lib       | 86.5 ms                                                               | 59.5 ms: 1.45x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.32x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 876 ms: 2.61x faster                                                     |
| async_tree_none         | 950 ms                                                                | 376 ms: 2.53x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 466 ms: 2.43x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 725 ms: 1.76x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.30x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 85.3 ms: 1.58x faster                                                    |
| nbody          | 166 ms                                                                | 119 ms: 1.40x faster                                                     |
| pidigits       | 235 ms                                                                | 291 ms: 1.24x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.21x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 123 ms: 1.43x faster                                                     |
| regex_dna      | 257 ms                                                                | 233 ms: 1.11x faster                                                     |
| regex_v8       | 32.2 ms                                                               | 30.3 ms: 1.06x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.14x faster                                                             |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 2.37 sec: 1.41x faster                                                   |
| unpickle_pure_python | 366 us                                                                | 260 us: 1.41x faster                                                     |
| pickle_pure_python   | 529 us                                                                | 392 us: 1.35x faster                                                     |
| xml_etree_process    | 99.5 ms                                                               | 74.1 ms: 1.34x faster                                                    |
| unpickle_list        | 6.99 us                                                               | 5.68 us: 1.23x faster                                                    |
| json_dumps           | 16.7 ms                                                               | 13.9 ms: 1.21x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 104 ms: 1.19x faster                                                     |
| xml_etree_iterparse  | 156 ms                                                                | 151 ms: 1.03x faster                                                     |
| unpickle             | 17.5 us                                                               | 17.2 us: 1.01x faster                                                    |
| pickle_dict          | 35.1 us                                                               | 36.7 us: 1.05x slower                                                    |
| pickle_list          | 5.24 us                                                               | 5.60 us: 1.07x slower                                                    |
| json_loads           | 30.9 us                                                               | 33.1 us: 1.07x slower                                                    |
| pickle               | 12.5 us                                                               | 15.0 us: 1.20x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.12x faster                                                             |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 16.1 ms: 1.44x slower                                                    |
| python_startup_no_site | 6.89 ms                                                               | 10.1 ms: 1.47x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.45x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 53.3 ms                                                               | 38.8 ms: 1.37x faster                                                    |
| mako            | 18.9 ms                                                               | 13.9 ms: 1.36x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 25.9 ms: 1.36x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 58.1 ms: 1.20x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.32x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 191 us: 3.46x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 876 ms: 2.61x faster                                                     |
| async_tree_none          | 950 ms                                                                | 376 ms: 2.53x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 466 ms: 2.43x faster                                                     |
| deltablue                | 8.94 ms                                                               | 3.88 ms: 2.30x faster                                                    |
| go                       | 264 ms                                                                | 136 ms: 1.94x faster                                                     |
| richards_super           | 107 ms                                                                | 56.1 ms: 1.91x faster                                                    |
| generators               | 68.1 ms                                                               | 36.1 ms: 1.89x faster                                                    |
| logging_silent           | 222 ns                                                                | 121 ns: 1.84x faster                                                     |
| raytrace                 | 573 ms                                                                | 311 ms: 1.84x faster                                                     |
| chaos                    | 121 ms                                                                | 66.2 ms: 1.83x faster                                                    |
| richards                 | 91.7 ms                                                               | 50.9 ms: 1.80x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 725 ms: 1.76x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 35.6 us: 1.73x faster                                                    |
| scimark_sor              | 246 ms                                                                | 143 ms: 1.72x faster                                                     |
| asyncio_tcp              | 944 ms                                                                | 556 ms: 1.70x faster                                                     |
| scimark_lu               | 227 ms                                                                | 137 ms: 1.65x faster                                                     |
| comprehensions           | 33.1 us                                                               | 20.2 us: 1.64x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 78.0 ms: 1.64x faster                                                    |
| deepcopy                 | 511 us                                                                | 312 us: 1.64x faster                                                     |
| spectral_norm            | 186 ms                                                                | 114 ms: 1.63x faster                                                     |
| pylint                   | 485 ms                                                                | 303 ms: 1.60x faster                                                     |
| float                    | 135 ms                                                                | 85.3 ms: 1.58x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.16 sec: 1.52x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 7.20 ms: 1.51x faster                                                    |
| pyflate                  | 795 ms                                                                | 528 ms: 1.51x faster                                                     |
| crypto_pyaes             | 134 ms                                                                | 90.1 ms: 1.49x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 59.5 ms: 1.45x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 50.7 ms: 1.45x faster                                                    |
| regex_compile            | 177 ms                                                                | 123 ms: 1.43x faster                                                     |
| tomli_loads              | 3.36 sec                                                              | 2.37 sec: 1.41x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 260 us: 1.41x faster                                                     |
| nbody                    | 166 ms                                                                | 119 ms: 1.40x faster                                                     |
| logging_simple           | 9.78 us                                                               | 7.00 us: 1.40x faster                                                    |
| sqlalchemy_declarative   | 197 ms                                                                | 143 ms: 1.38x faster                                                     |
| logging_format           | 10.6 us                                                               | 7.67 us: 1.38x faster                                                    |
| django_template          | 53.3 ms                                                               | 38.8 ms: 1.37x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.36 us: 1.37x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.9 ms: 1.36x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.24 sec: 1.36x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 25.9 ms: 1.36x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 392 us: 1.35x faster                                                     |
| xml_etree_process        | 99.5 ms                                                               | 74.1 ms: 1.34x faster                                                    |
| thrift                   | 1.26 ms                                                               | 949 us: 1.33x faster                                                     |
| 2to3                     | 381 ms                                                                | 291 ms: 1.31x faster                                                     |
| sympy_sum                | 184 ms                                                                | 141 ms: 1.30x faster                                                     |
| scimark_fft              | 500 ms                                                                | 388 ms: 1.29x faster                                                     |
| sympy_str                | 329 ms                                                                | 257 ms: 1.28x faster                                                     |
| sympy_integrate          | 26.5 ms                                                               | 20.9 ms: 1.27x faster                                                    |
| coroutines               | 37.2 ms                                                               | 29.3 ms: 1.27x faster                                                    |
| sqlalchemy_imperative    | 20.5 ms                                                               | 16.2 ms: 1.27x faster                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 910 ms: 1.26x faster                                                     |
| pprint_pformat           | 2.36 sec                                                              | 1.88 sec: 1.26x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 21.2 ms: 1.24x faster                                                    |
| unpickle_list            | 6.99 us                                                               | 5.68 us: 1.23x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.25 ms: 1.22x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.31 ms: 1.22x faster                                                    |
| docutils                 | 3.53 sec                                                              | 2.91 sec: 1.21x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 13.9 ms: 1.21x faster                                                    |
| genshi_xml               | 69.8 ms                                                               | 58.1 ms: 1.20x faster                                                    |
| sympy_expand             | 543 ms                                                                | 455 ms: 1.19x faster                                                     |
| xml_etree_generate       | 123 ms                                                                | 104 ms: 1.19x faster                                                     |
| nqueens                  | 117 ms                                                                | 100 ms: 1.17x faster                                                     |
| mdp                      | 3.70 sec                                                              | 3.22 sec: 1.15x faster                                                   |
| regex_dna                | 257 ms                                                                | 233 ms: 1.11x faster                                                     |
| async_generators         | 452 ms                                                                | 416 ms: 1.09x faster                                                     |
| fannkuch                 | 546 ms                                                                | 502 ms: 1.09x faster                                                     |
| meteor_contest           | 126 ms                                                                | 116 ms: 1.08x faster                                                     |
| sqlite_synth             | 4.12 us                                                               | 3.83 us: 1.07x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 30.3 ms: 1.06x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 151 ms: 1.03x faster                                                     |
| json                     | 5.88 ms                                                               | 5.78 ms: 1.02x faster                                                    |
| unpickle                 | 17.5 us                                                               | 17.2 us: 1.01x faster                                                    |
| pickle_dict              | 35.1 us                                                               | 36.7 us: 1.05x slower                                                    |
| pickle_list              | 5.24 us                                                               | 5.60 us: 1.07x slower                                                    |
| json_loads               | 30.9 us                                                               | 33.1 us: 1.07x slower                                                    |
| telco                    | 8.49 ms                                                               | 9.22 ms: 1.09x slower                                                    |
| coverage                 | 83.6 ms                                                               | 93.3 ms: 1.12x slower                                                    |
| pickle                   | 12.5 us                                                               | 15.0 us: 1.20x slower                                                    |
| pidigits                 | 235 ms                                                                | 291 ms: 1.24x slower                                                     |
| python_startup           | 11.2 ms                                                               | 16.1 ms: 1.44x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 10.1 ms: 1.47x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.52 ms: 1.57x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.65 ms: 1.61x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 2.37 sec: 163.13x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.24x faster                                                             |

Benchmark hidden because not significant (3): xml_etree_parse, regex_effbot, asyncio_websockets
Ignored benchmarks (11) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250315-3.14.0a6+-e82c2ca-CLANG/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.349x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.35x