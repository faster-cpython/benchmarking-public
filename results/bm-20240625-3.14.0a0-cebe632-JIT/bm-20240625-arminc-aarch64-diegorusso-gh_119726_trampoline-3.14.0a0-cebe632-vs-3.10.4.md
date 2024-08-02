# Results vs. 3.10.4

- fork: diegorusso
- ref: gh_119726_trampoline
- machine: linux-aarch64
- commit hash: cebe632
- commit date: 2024-06-25
- overall geometric mean: 1.21x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: 1.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240625-arminc-aarch64-diegorusso-gh_119726_trampoline-3.14.0a0-cebe632 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 364 ms: 1.05x faster                                                        |
| html5lib       | 86.5 ms                                                               | 70.5 ms: 1.23x faster                                                       |
| tornado_http   | 178 ms                                                                | 140 ms: 1.27x faster                                                        |
| Geometric mean | (ref)                                                                 | 1.13x faster                                                                |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240625-arminc-aarch64-diegorusso-gh_119726_trampoline-3.14.0a0-cebe632 |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 1.07 sec: 2.14x faster                                                      |
| async_tree_none         | 950 ms                                                                | 452 ms: 2.10x faster                                                        |
| async_tree_memoization  | 1.13 sec                                                              | 582 ms: 1.95x faster                                                        |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 739 ms: 1.72x faster                                                        |
| Geometric mean          | (ref)                                                                 | 1.97x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240625-arminc-aarch64-diegorusso-gh_119726_trampoline-3.14.0a0-cebe632 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 88.7 ms: 1.52x faster                                                       |
| nbody          | 166 ms                                                                | 114 ms: 1.45x faster                                                        |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240625-arminc-aarch64-diegorusso-gh_119726_trampoline-3.14.0a0-cebe632 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 30.4 ms: 1.06x faster                                                       |
| regex_dna      | 257 ms                                                                | 251 ms: 1.03x faster                                                        |
| regex_effbot   | 4.25 ms                                                               | 4.87 ms: 1.15x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240625-arminc-aarch64-diegorusso-gh_119726_trampoline-3.14.0a0-cebe632 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 396 us: 1.34x faster                                                        |
| unpickle_pure_python | 366 us                                                                | 279 us: 1.31x faster                                                        |
| xml_etree_process    | 99.5 ms                                                               | 78.9 ms: 1.26x faster                                                       |
| tomli_loads          | 3.36 sec                                                              | 2.68 sec: 1.25x faster                                                      |
| json_dumps           | 16.7 ms                                                               | 13.5 ms: 1.24x faster                                                       |
| xml_etree_parse      | 212 ms                                                                | 187 ms: 1.13x faster                                                        |
| xml_etree_generate   | 123 ms                                                                | 110 ms: 1.11x faster                                                        |
| xml_etree_iterparse  | 156 ms                                                                | 147 ms: 1.06x faster                                                        |
| unpickle_list        | 6.99 us                                                               | 6.67 us: 1.05x faster                                                       |
| pickle_list          | 5.24 us                                                               | 5.28 us: 1.01x slower                                                       |
| json_loads           | 30.9 us                                                               | 33.1 us: 1.07x slower                                                       |
| pickle_dict          | 35.1 us                                                               | 37.8 us: 1.08x slower                                                       |
| pickle               | 12.5 us                                                               | 14.0 us: 1.12x slower                                                       |
| unpickle             | 17.5 us                                                               | 19.9 us: 1.14x slower                                                       |
| Geometric mean       | (ref)                                                                 | 1.09x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240625-arminc-aarch64-diegorusso-gh_119726_trampoline-3.14.0a0-cebe632 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 15.4 ms: 1.38x slower                                                       |
| python_startup_no_site | 6.89 ms                                                               | 11.1 ms: 1.61x slower                                                       |
| Geometric mean         | (ref)                                                                 | 1.49x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240625-arminc-aarch64-diegorusso-gh_119726_trampoline-3.14.0a0-cebe632 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.2 ms: 1.43x faster                                                       |
| django_template | 53.3 ms                                                               | 50.2 ms: 1.06x faster                                                       |
| genshi_xml      | 69.8 ms                                                               | 82.6 ms: 1.18x slower                                                       |
| Geometric mean  | (ref)                                                                 | 1.07x faster                                                                |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240625-arminc-aarch64-diegorusso-gh_119726_trampoline-3.14.0a0-cebe632 |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 207 us: 3.19x faster                                                        |
| async_tree_io            | 2.28 sec                                                              | 1.07 sec: 2.14x faster                                                      |
| async_tree_none          | 950 ms                                                                | 452 ms: 2.10x faster                                                        |
| deltablue                | 8.94 ms                                                               | 4.47 ms: 2.00x faster                                                       |
| async_tree_memoization   | 1.13 sec                                                              | 582 ms: 1.95x faster                                                        |
| bench_mp_pool            | 14.5 ms                                                               | 7.88 ms: 1.84x faster                                                       |
| raytrace                 | 573 ms                                                                | 325 ms: 1.76x faster                                                        |
| generators               | 68.1 ms                                                               | 38.8 ms: 1.75x faster                                                       |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 739 ms: 1.72x faster                                                        |
| richards_super           | 107 ms                                                                | 63.1 ms: 1.70x faster                                                       |
| richards                 | 91.7 ms                                                               | 55.8 ms: 1.64x faster                                                       |
| logging_silent           | 222 ns                                                                | 139 ns: 1.59x faster                                                        |
| deepcopy_memo            | 61.7 us                                                               | 38.9 us: 1.58x faster                                                       |
| crypto_pyaes             | 134 ms                                                                | 85.8 ms: 1.56x faster                                                       |
| float                    | 135 ms                                                                | 88.7 ms: 1.52x faster                                                       |
| go                       | 264 ms                                                                | 178 ms: 1.48x faster                                                        |
| sqlglot_parse            | 2.40 ms                                                               | 1.64 ms: 1.47x faster                                                       |
| scimark_monte_carlo      | 128 ms                                                                | 87.5 ms: 1.46x faster                                                       |
| asyncio_tcp              | 944 ms                                                                | 647 ms: 1.46x faster                                                        |
| nbody                    | 166 ms                                                                | 114 ms: 1.45x faster                                                        |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.28 sec: 1.44x faster                                                      |
| mako                     | 18.9 ms                                                               | 13.2 ms: 1.43x faster                                                       |
| scimark_sor              | 246 ms                                                                | 174 ms: 1.41x faster                                                        |
| sqlglot_transpile        | 2.84 ms                                                               | 2.02 ms: 1.41x faster                                                       |
| comprehensions           | 33.1 us                                                               | 23.5 us: 1.41x faster                                                       |
| chaos                    | 121 ms                                                                | 88.1 ms: 1.37x faster                                                       |
| logging_simple           | 9.78 us                                                               | 7.19 us: 1.36x faster                                                       |
| pickle_pure_python       | 529 us                                                                | 396 us: 1.34x faster                                                        |
| logging_format           | 10.6 us                                                               | 8.01 us: 1.32x faster                                                       |
| deepcopy                 | 511 us                                                                | 386 us: 1.32x faster                                                        |
| unpickle_pure_python     | 366 us                                                                | 279 us: 1.31x faster                                                        |
| thrift                   | 1.26 ms                                                               | 970 us: 1.30x faster                                                        |
| pyflate                  | 795 ms                                                                | 619 ms: 1.28x faster                                                        |
| spectral_norm            | 186 ms                                                                | 146 ms: 1.27x faster                                                        |
| tornado_http             | 178 ms                                                                | 140 ms: 1.27x faster                                                        |
| pycparser                | 1.69 sec                                                              | 1.34 sec: 1.27x faster                                                      |
| xml_etree_process        | 99.5 ms                                                               | 78.9 ms: 1.26x faster                                                       |
| coroutines               | 37.2 ms                                                               | 29.5 ms: 1.26x faster                                                       |
| scimark_lu               | 227 ms                                                                | 181 ms: 1.25x faster                                                        |
| tomli_loads              | 3.36 sec                                                              | 2.68 sec: 1.25x faster                                                      |
| json_dumps               | 16.7 ms                                                               | 13.5 ms: 1.24x faster                                                       |
| html5lib                 | 86.5 ms                                                               | 70.5 ms: 1.23x faster                                                       |
| hexiom                   | 10.9 ms                                                               | 8.97 ms: 1.22x faster                                                       |
| bench_thread_pool        | 1.59 ms                                                               | 1.35 ms: 1.18x faster                                                       |
| fannkuch                 | 546 ms                                                                | 464 ms: 1.18x faster                                                        |
| dask                     | 450 ms                                                                | 385 ms: 1.17x faster                                                        |
| pathlib                  | 26.3 ms                                                               | 22.5 ms: 1.17x faster                                                       |
| pylint                   | 485 ms                                                                | 424 ms: 1.15x faster                                                        |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.71 ms: 1.14x faster                                                       |
| xml_etree_parse          | 212 ms                                                                | 187 ms: 1.13x faster                                                        |
| xml_etree_generate       | 123 ms                                                                | 110 ms: 1.11x faster                                                        |
| deepcopy_reduce          | 4.60 us                                                               | 4.17 us: 1.10x faster                                                       |
| meteor_contest           | 126 ms                                                                | 115 ms: 1.10x faster                                                        |
| sqlglot_normalize        | 156 ms                                                                | 144 ms: 1.09x faster                                                        |
| sqlglot_optimize         | 75.4 ms                                                               | 69.5 ms: 1.08x faster                                                       |
| scimark_fft              | 500 ms                                                                | 463 ms: 1.08x faster                                                        |
| dulwich_log              | 73.5 ms                                                               | 68.7 ms: 1.07x faster                                                       |
| django_template          | 53.3 ms                                                               | 50.2 ms: 1.06x faster                                                       |
| sqlite_synth             | 4.12 us                                                               | 3.88 us: 1.06x faster                                                       |
| mdp                      | 3.70 sec                                                              | 3.49 sec: 1.06x faster                                                      |
| xml_etree_iterparse      | 156 ms                                                                | 147 ms: 1.06x faster                                                        |
| regex_v8                 | 32.2 ms                                                               | 30.4 ms: 1.06x faster                                                       |
| 2to3                     | 381 ms                                                                | 364 ms: 1.05x faster                                                        |
| unpickle_list            | 6.99 us                                                               | 6.67 us: 1.05x faster                                                       |
| sympy_str                | 329 ms                                                                | 319 ms: 1.03x faster                                                        |
| regex_dna                | 257 ms                                                                | 251 ms: 1.03x faster                                                        |
| sympy_expand             | 543 ms                                                                | 537 ms: 1.01x faster                                                        |
| json                     | 5.88 ms                                                               | 5.82 ms: 1.01x faster                                                       |
| sympy_sum                | 184 ms                                                                | 183 ms: 1.01x faster                                                        |
| pprint_pformat           | 2.36 sec                                                              | 2.38 sec: 1.01x slower                                                      |
| pickle_list              | 5.24 us                                                               | 5.28 us: 1.01x slower                                                       |
| nqueens                  | 117 ms                                                                | 119 ms: 1.01x slower                                                        |
| asyncio_websockets       | 657 ms                                                                | 665 ms: 1.01x slower                                                        |
| create_gc_cycles         | 2.26 ms                                                               | 2.33 ms: 1.03x slower                                                       |
| json_loads               | 30.9 us                                                               | 33.1 us: 1.07x slower                                                       |
| pickle_dict              | 35.1 us                                                               | 37.8 us: 1.08x slower                                                       |
| async_generators         | 452 ms                                                                | 507 ms: 1.12x slower                                                        |
| pickle                   | 12.5 us                                                               | 14.0 us: 1.12x slower                                                       |
| unpickle                 | 17.5 us                                                               | 19.9 us: 1.14x slower                                                       |
| regex_effbot             | 4.25 ms                                                               | 4.87 ms: 1.15x slower                                                       |
| gc_traversal             | 4.15 ms                                                               | 4.82 ms: 1.16x slower                                                       |
| genshi_xml               | 69.8 ms                                                               | 82.6 ms: 1.18x slower                                                       |
| telco                    | 8.49 ms                                                               | 10.1 ms: 1.19x slower                                                       |
| coverage                 | 83.6 ms                                                               | 103 ms: 1.24x slower                                                        |
| python_startup           | 11.2 ms                                                               | 15.4 ms: 1.38x slower                                                       |
| python_startup_no_site   | 6.89 ms                                                               | 11.1 ms: 1.61x slower                                                       |
| Geometric mean           | (ref)                                                                 | 1.21x faster                                                                |

Benchmark hidden because not significant (6): regex_compile, sympy_integrate, pprint_safe_repr, pidigits, genshi_text, docutils
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240625-3.14.0a0-cebe632-JIT/bm-20240625-arminc-aarch64-diegorusso-gh_119726_trampoline-3.14.0a0-cebe632.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: 1.25x