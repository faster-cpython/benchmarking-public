# Results vs. 3.10.4

- fork: faster-cpython
- ref: experimental_gc_fix
- machine: linux-x86_64
- commit hash: 198dcfc
- commit date: 2024-09-26
- overall geometric mean: 1.37x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 271 ms: 1.29x faster                                                           |
| docutils       | 3.30 sec                                               | 2.70 sec: 1.22x faster                                                         |
| html5lib       | 88.9 ms                                                | 68.1 ms: 1.31x faster                                                          |
| tornado_http   | 136 ms                                                 | 91.8 ms: 1.49x faster                                                          |
| Geometric mean | (ref)                                                  | 1.32x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization  | 870 ms                                                 | 481 ms: 1.81x faster                                                           |
| async_tree_io           | 1.77 sec                                               | 987 ms: 1.79x faster                                                           |
| async_tree_none         | 728 ms                                                 | 424 ms: 1.72x faster                                                           |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 644 ms: 1.58x faster                                                           |
| Geometric mean          | (ref)                                                  | 1.72x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 86.4 ms: 1.78x faster                                                          |
| float          | 117 ms                                                 | 95.9 ms: 1.22x faster                                                          |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                  | 1.30x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.47x faster                                                           |
| regex_v8       | 27.8 ms                                                | 25.1 ms: 1.11x faster                                                          |
| regex_dna      | 227 ms                                                 | 222 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                  | 1.14x faster                                                                   |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 303 us: 1.60x faster                                                           |
| unpickle_pure_python | 331 us                                                 | 211 us: 1.56x faster                                                           |
| tomli_loads          | 3.14 sec                                               | 2.07 sec: 1.52x faster                                                         |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.37x faster                                                          |
| xml_etree_process    | 79.1 ms                                                | 65.2 ms: 1.21x faster                                                          |
| json_loads           | 31.2 us                                                | 27.2 us: 1.15x faster                                                          |
| xml_etree_generate   | 99.4 ms                                                | 91.0 ms: 1.09x faster                                                          |
| pickle_list          | 5.08 us                                                | 5.13 us: 1.01x slower                                                          |
| unpickle             | 14.4 us                                                | 14.6 us: 1.02x slower                                                          |
| xml_etree_parse      | 168 ms                                                 | 171 ms: 1.02x slower                                                           |
| pickle               | 10.7 us                                                | 11.6 us: 1.08x slower                                                          |
| pickle_dict          | 29.6 us                                                | 34.4 us: 1.16x slower                                                          |
| xml_etree_iterparse  | 115 ms                                                 | 157 ms: 1.36x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                                   |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.7 ms: 1.37x faster                                                          |
| python_startup_no_site | 5.93 ms                                                | 7.01 ms: 1.18x slower                                                          |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.2 ms: 1.45x faster                                                          |
| genshi_text     | 31.8 ms                                                | 22.1 ms: 1.44x faster                                                          |
| django_template | 48.2 ms                                                | 34.2 ms: 1.41x faster                                                          |
| genshi_xml      | 66.0 ms                                                | 54.5 ms: 1.21x faster                                                          |
| Geometric mean  | (ref)                                                  | 1.38x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 160 us: 3.41x faster                                                           |
| generators               | 80.1 ms                                                | 27.6 ms: 2.90x faster                                                          |
| deltablue                | 7.91 ms                                                | 3.29 ms: 2.41x faster                                                          |
| go                       | 240 ms                                                 | 117 ms: 2.05x faster                                                           |
| deepcopy_memo            | 58.5 us                                                | 29.6 us: 1.98x faster                                                          |
| chaos                    | 115 ms                                                 | 58.5 ms: 1.97x faster                                                          |
| raytrace                 | 507 ms                                                 | 261 ms: 1.94x faster                                                           |
| asyncio_tcp              | 922 ms                                                 | 480 ms: 1.92x faster                                                           |
| logging_silent           | 190 ns                                                 | 101 ns: 1.88x faster                                                           |
| deepcopy                 | 479 us                                                 | 256 us: 1.87x faster                                                           |
| richards_super           | 94.7 ms                                                | 51.9 ms: 1.83x faster                                                          |
| async_tree_memoization   | 870 ms                                                 | 481 ms: 1.81x faster                                                           |
| async_tree_io            | 1.77 sec                                               | 987 ms: 1.79x faster                                                           |
| scimark_sor              | 220 ms                                                 | 123 ms: 1.78x faster                                                           |
| nbody                    | 154 ms                                                 | 86.4 ms: 1.78x faster                                                          |
| crypto_pyaes             | 128 ms                                                 | 71.9 ms: 1.78x faster                                                          |
| scimark_monte_carlo      | 118 ms                                                 | 66.8 ms: 1.77x faster                                                          |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                                          |
| pylint                   | 551 ms                                                 | 319 ms: 1.73x faster                                                           |
| richards                 | 79.3 ms                                                | 45.9 ms: 1.73x faster                                                          |
| async_tree_none          | 728 ms                                                 | 424 ms: 1.72x faster                                                           |
| hexiom                   | 10.4 ms                                                | 6.18 ms: 1.68x faster                                                          |
| sqlglot_parse            | 2.17 ms                                                | 1.31 ms: 1.66x faster                                                          |
| pickle_pure_python       | 484 us                                                 | 303 us: 1.60x faster                                                           |
| sqlglot_transpile        | 2.57 ms                                                | 1.62 ms: 1.59x faster                                                          |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 644 ms: 1.58x faster                                                           |
| deepcopy_reduce          | 4.17 us                                                | 2.65 us: 1.57x faster                                                          |
| unpickle_pure_python     | 331 us                                                 | 211 us: 1.56x faster                                                           |
| scimark_lu               | 176 ms                                                 | 114 ms: 1.55x faster                                                           |
| coroutines               | 35.1 ms                                                | 23.0 ms: 1.52x faster                                                          |
| spectral_norm            | 170 ms                                                 | 112 ms: 1.52x faster                                                           |
| tomli_loads              | 3.14 sec                                               | 2.07 sec: 1.52x faster                                                         |
| pyflate                  | 716 ms                                                 | 472 ms: 1.52x faster                                                           |
| tornado_http             | 136 ms                                                 | 91.8 ms: 1.49x faster                                                          |
| logging_simple           | 8.30 us                                                | 5.61 us: 1.48x faster                                                          |
| regex_compile            | 188 ms                                                 | 128 ms: 1.47x faster                                                           |
| logging_format           | 9.09 us                                                | 6.20 us: 1.47x faster                                                          |
| mako                     | 16.3 ms                                                | 11.2 ms: 1.45x faster                                                          |
| pprint_pformat           | 2.10 sec                                               | 1.45 sec: 1.45x faster                                                         |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.78 sec: 1.44x faster                                                         |
| genshi_text              | 31.8 ms                                                | 22.1 ms: 1.44x faster                                                          |
| pprint_safe_repr         | 1.02 sec                                               | 708 ms: 1.44x faster                                                           |
| django_template          | 48.2 ms                                                | 34.2 ms: 1.41x faster                                                          |
| thrift                   | 1.07 ms                                                | 776 us: 1.38x faster                                                           |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.37x faster                                                          |
| python_startup           | 14.6 ms                                                | 10.7 ms: 1.37x faster                                                          |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.74 ms: 1.36x faster                                                          |
| sqlglot_normalize        | 143 ms                                                 | 106 ms: 1.35x faster                                                           |
| nqueens                  | 106 ms                                                 | 79.5 ms: 1.33x faster                                                          |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.33x faster                                                           |
| sympy_integrate          | 25.8 ms                                                | 19.5 ms: 1.33x faster                                                          |
| unpack_sequence          | 60.0 ns                                                | 45.5 ns: 1.32x faster                                                          |
| fannkuch                 | 532 ms                                                 | 404 ms: 1.31x faster                                                           |
| dulwich_log              | 84.3 ms                                                | 64.5 ms: 1.31x faster                                                          |
| html5lib                 | 88.9 ms                                                | 68.1 ms: 1.31x faster                                                          |
| scimark_fft              | 466 ms                                                 | 358 ms: 1.30x faster                                                           |
| pycparser                | 1.58 sec                                               | 1.22 sec: 1.30x faster                                                         |
| sympy_str                | 346 ms                                                 | 268 ms: 1.29x faster                                                           |
| 2to3                     | 348 ms                                                 | 271 ms: 1.29x faster                                                           |
| sqlglot_optimize         | 69.2 ms                                                | 54.1 ms: 1.28x faster                                                          |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                                          |
| sympy_expand             | 566 ms                                                 | 453 ms: 1.25x faster                                                           |
| bench_thread_pool        | 986 us                                                 | 790 us: 1.25x faster                                                           |
| docutils                 | 3.30 sec                                               | 2.70 sec: 1.22x faster                                                         |
| float                    | 117 ms                                                 | 95.9 ms: 1.22x faster                                                          |
| xml_etree_process        | 79.1 ms                                                | 65.2 ms: 1.21x faster                                                          |
| genshi_xml               | 66.0 ms                                                | 54.5 ms: 1.21x faster                                                          |
| json_loads               | 31.2 us                                                | 27.2 us: 1.15x faster                                                          |
| mdp                      | 2.85 sec                                               | 2.53 sec: 1.13x faster                                                         |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                           |
| regex_v8                 | 27.8 ms                                                | 25.1 ms: 1.11x faster                                                          |
| json                     | 5.69 ms                                                | 5.17 ms: 1.10x faster                                                          |
| xml_etree_generate       | 99.4 ms                                                | 91.0 ms: 1.09x faster                                                          |
| sqlite_synth             | 3.02 us                                                | 2.82 us: 1.07x faster                                                          |
| gc_traversal             | 3.62 ms                                                | 3.53 ms: 1.03x faster                                                          |
| regex_dna                | 227 ms                                                 | 222 ms: 1.02x faster                                                           |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                           |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                           |
| pickle_list              | 5.08 us                                                | 5.13 us: 1.01x slower                                                          |
| unpickle                 | 14.4 us                                                | 14.6 us: 1.02x slower                                                          |
| xml_etree_parse          | 168 ms                                                 | 171 ms: 1.02x slower                                                           |
| async_generators         | 444 ms                                                 | 455 ms: 1.03x slower                                                           |
| create_gc_cycles         | 1.62 ms                                                | 1.71 ms: 1.05x slower                                                          |
| coverage                 | 79.4 ms                                                | 85.3 ms: 1.07x slower                                                          |
| pickle                   | 10.7 us                                                | 11.6 us: 1.08x slower                                                          |
| telco                    | 7.27 ms                                                | 8.30 ms: 1.14x slower                                                          |
| pickle_dict              | 29.6 us                                                | 34.4 us: 1.16x slower                                                          |
| python_startup_no_site   | 5.93 ms                                                | 7.01 ms: 1.18x slower                                                          |
| xml_etree_iterparse      | 115 ms                                                 | 157 ms: 1.36x slower                                                           |
| Geometric mean           | (ref)                                                  | 1.37x faster                                                                   |

Benchmark hidden because not significant (3): bench_mp_pool, regex_effbot, unpickle_list
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240926-3.14.0a0-198dcfc/bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.11x