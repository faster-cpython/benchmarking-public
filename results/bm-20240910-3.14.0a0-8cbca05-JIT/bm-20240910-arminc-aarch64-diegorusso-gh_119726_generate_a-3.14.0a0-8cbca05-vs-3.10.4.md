# Results vs. 3.10.4

- fork: diegorusso
- ref: gh_119726_generate_a
- machine: linux-aarch64
- commit hash: 8cbca05
- commit date: 2024-09-10
- overall geometric mean: 1.18x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.24x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 376 ms: 1.01x faster                                                        |
| docutils       | 3.53 sec                                                              | 3.94 sec: 1.12x slower                                                      |
| html5lib       | 86.5 ms                                                               | 71.4 ms: 1.21x faster                                                       |
| tornado_http   | 178 ms                                                                | 151 ms: 1.18x faster                                                        |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 449 ms: 2.11x faster                                                        |
| async_tree_io           | 2.28 sec                                                              | 1.15 sec: 1.99x faster                                                      |
| async_tree_memoization  | 1.13 sec                                                              | 583 ms: 1.94x faster                                                        |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 761 ms: 1.67x faster                                                        |
| Geometric mean          | (ref)                                                                 | 1.92x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 87.8 ms: 1.53x faster                                                       |
| nbody          | 166 ms                                                                | 111 ms: 1.50x faster                                                        |
| Geometric mean | (ref)                                                                 | 1.32x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 30.8 ms: 1.04x faster                                                       |
| regex_dna      | 257 ms                                                                | 255 ms: 1.01x faster                                                        |
| regex_compile  | 177 ms                                                                | 186 ms: 1.05x slower                                                        |
| regex_effbot   | 4.25 ms                                                               | 4.99 ms: 1.17x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 264 us: 1.38x faster                                                        |
| pickle_pure_python   | 529 us                                                                | 384 us: 1.38x faster                                                        |
| tomli_loads          | 3.36 sec                                                              | 2.63 sec: 1.28x faster                                                      |
| xml_etree_process    | 99.5 ms                                                               | 79.7 ms: 1.25x faster                                                       |
| json_dumps           | 16.7 ms                                                               | 13.9 ms: 1.20x faster                                                       |
| xml_etree_parse      | 212 ms                                                                | 187 ms: 1.14x faster                                                        |
| xml_etree_generate   | 123 ms                                                                | 110 ms: 1.11x faster                                                        |
| unpickle_list        | 6.99 us                                                               | 6.34 us: 1.10x faster                                                       |
| xml_etree_iterparse  | 156 ms                                                                | 149 ms: 1.05x faster                                                        |
| json_loads           | 30.9 us                                                               | 31.3 us: 1.01x slower                                                       |
| pickle_dict          | 35.1 us                                                               | 38.0 us: 1.08x slower                                                       |
| pickle               | 12.5 us                                                               | 13.7 us: 1.10x slower                                                       |
| unpickle             | 17.5 us                                                               | 19.3 us: 1.10x slower                                                       |
| Geometric mean       | (ref)                                                                 | 1.10x faster                                                                |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.1 ms: 1.17x slower                                                       |
| python_startup_no_site | 6.89 ms                                                               | 8.74 ms: 1.27x slower                                                       |
| Geometric mean         | (ref)                                                                 | 1.22x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.0 ms: 1.45x faster                                                       |
| django_template | 53.3 ms                                                               | 50.5 ms: 1.06x faster                                                       |
| genshi_xml      | 69.8 ms                                                               | 81.5 ms: 1.17x slower                                                       |
| Geometric mean  | (ref)                                                                 | 1.07x faster                                                                |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 206 us: 3.21x faster                                                        |
| async_tree_none          | 950 ms                                                                | 449 ms: 2.11x faster                                                        |
| deltablue                | 8.94 ms                                                               | 4.33 ms: 2.06x faster                                                       |
| async_tree_io            | 2.28 sec                                                              | 1.15 sec: 1.99x faster                                                      |
| async_tree_memoization   | 1.13 sec                                                              | 583 ms: 1.94x faster                                                        |
| bench_mp_pool            | 14.5 ms                                                               | 7.61 ms: 1.91x faster                                                       |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 761 ms: 1.67x faster                                                        |
| raytrace                 | 573 ms                                                                | 348 ms: 1.65x faster                                                        |
| scimark_sor              | 246 ms                                                                | 149 ms: 1.65x faster                                                        |
| deepcopy_memo            | 61.7 us                                                               | 37.7 us: 1.63x faster                                                       |
| logging_silent           | 222 ns                                                                | 137 ns: 1.62x faster                                                        |
| float                    | 135 ms                                                                | 87.8 ms: 1.53x faster                                                       |
| scimark_lu               | 227 ms                                                                | 149 ms: 1.52x faster                                                        |
| nbody                    | 166 ms                                                                | 111 ms: 1.50x faster                                                        |
| asyncio_tcp              | 944 ms                                                                | 632 ms: 1.49x faster                                                        |
| crypto_pyaes             | 134 ms                                                                | 90.5 ms: 1.48x faster                                                       |
| mako                     | 18.9 ms                                                               | 13.0 ms: 1.45x faster                                                       |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.28 sec: 1.44x faster                                                      |
| go                       | 264 ms                                                                | 184 ms: 1.43x faster                                                        |
| richards_super           | 107 ms                                                                | 75.5 ms: 1.42x faster                                                       |
| unpickle_pure_python     | 366 us                                                                | 264 us: 1.38x faster                                                        |
| pickle_pure_python       | 529 us                                                                | 384 us: 1.38x faster                                                        |
| scimark_monte_carlo      | 128 ms                                                                | 92.8 ms: 1.38x faster                                                       |
| sqlglot_parse            | 2.40 ms                                                               | 1.74 ms: 1.38x faster                                                       |
| richards                 | 91.7 ms                                                               | 67.3 ms: 1.36x faster                                                       |
| comprehensions           | 33.1 us                                                               | 24.6 us: 1.35x faster                                                       |
| logging_format           | 10.6 us                                                               | 8.00 us: 1.33x faster                                                       |
| logging_simple           | 9.78 us                                                               | 7.40 us: 1.32x faster                                                       |
| chaos                    | 121 ms                                                                | 92.4 ms: 1.31x faster                                                       |
| thrift                   | 1.26 ms                                                               | 966 us: 1.30x faster                                                        |
| coroutines               | 37.2 ms                                                               | 28.6 ms: 1.30x faster                                                       |
| sqlglot_transpile        | 2.84 ms                                                               | 2.20 ms: 1.29x faster                                                       |
| spectral_norm            | 186 ms                                                                | 146 ms: 1.28x faster                                                        |
| tomli_loads              | 3.36 sec                                                              | 2.63 sec: 1.28x faster                                                      |
| deepcopy                 | 511 us                                                                | 400 us: 1.28x faster                                                        |
| xml_etree_process        | 99.5 ms                                                               | 79.7 ms: 1.25x faster                                                       |
| pyflate                  | 795 ms                                                                | 641 ms: 1.24x faster                                                        |
| pathlib                  | 26.3 ms                                                               | 21.7 ms: 1.21x faster                                                       |
| html5lib                 | 86.5 ms                                                               | 71.4 ms: 1.21x faster                                                       |
| json_dumps               | 16.7 ms                                                               | 13.9 ms: 1.20x faster                                                       |
| deepcopy_reduce          | 4.60 us                                                               | 3.86 us: 1.19x faster                                                       |
| tornado_http             | 178 ms                                                                | 151 ms: 1.18x faster                                                        |
| bench_thread_pool        | 1.59 ms                                                               | 1.35 ms: 1.18x faster                                                       |
| generators               | 68.1 ms                                                               | 58.1 ms: 1.17x faster                                                       |
| xml_etree_parse          | 212 ms                                                                | 187 ms: 1.14x faster                                                        |
| pycparser                | 1.69 sec                                                              | 1.50 sec: 1.12x faster                                                      |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.80 ms: 1.12x faster                                                       |
| xml_etree_generate       | 123 ms                                                                | 110 ms: 1.11x faster                                                        |
| unpickle_list            | 6.99 us                                                               | 6.34 us: 1.10x faster                                                       |
| scimark_fft              | 500 ms                                                                | 454 ms: 1.10x faster                                                        |
| hexiom                   | 10.9 ms                                                               | 9.91 ms: 1.10x faster                                                       |
| fannkuch                 | 546 ms                                                                | 497 ms: 1.10x faster                                                        |
| sqlite_synth             | 4.12 us                                                               | 3.79 us: 1.09x faster                                                       |
| django_template          | 53.3 ms                                                               | 50.5 ms: 1.06x faster                                                       |
| mdp                      | 3.70 sec                                                              | 3.50 sec: 1.06x faster                                                      |
| json                     | 5.88 ms                                                               | 5.61 ms: 1.05x faster                                                       |
| xml_etree_iterparse      | 156 ms                                                                | 149 ms: 1.05x faster                                                        |
| sqlglot_normalize        | 156 ms                                                                | 149 ms: 1.05x faster                                                        |
| regex_v8                 | 32.2 ms                                                               | 30.8 ms: 1.04x faster                                                       |
| meteor_contest           | 126 ms                                                                | 124 ms: 1.02x faster                                                        |
| 2to3                     | 381 ms                                                                | 376 ms: 1.01x faster                                                        |
| regex_dna                | 257 ms                                                                | 255 ms: 1.01x faster                                                        |
| asyncio_websockets       | 657 ms                                                                | 663 ms: 1.01x slower                                                        |
| json_loads               | 30.9 us                                                               | 31.3 us: 1.01x slower                                                       |
| create_gc_cycles         | 2.26 ms                                                               | 2.34 ms: 1.04x slower                                                       |
| sqlglot_optimize         | 75.4 ms                                                               | 78.7 ms: 1.04x slower                                                       |
| nqueens                  | 117 ms                                                                | 123 ms: 1.04x slower                                                        |
| regex_compile            | 177 ms                                                                | 186 ms: 1.05x slower                                                        |
| sympy_integrate          | 26.5 ms                                                               | 28.2 ms: 1.06x slower                                                       |
| pprint_safe_repr         | 1.15 sec                                                              | 1.23 sec: 1.07x slower                                                      |
| sympy_str                | 329 ms                                                                | 355 ms: 1.08x slower                                                        |
| pickle_dict              | 35.1 us                                                               | 38.0 us: 1.08x slower                                                       |
| pprint_pformat           | 2.36 sec                                                              | 2.57 sec: 1.09x slower                                                      |
| dulwich_log              | 73.5 ms                                                               | 80.7 ms: 1.10x slower                                                       |
| pickle                   | 12.5 us                                                               | 13.7 us: 1.10x slower                                                       |
| unpickle                 | 17.5 us                                                               | 19.3 us: 1.10x slower                                                       |
| sympy_expand             | 543 ms                                                                | 601 ms: 1.11x slower                                                        |
| docutils                 | 3.53 sec                                                              | 3.94 sec: 1.12x slower                                                      |
| async_generators         | 452 ms                                                                | 510 ms: 1.13x slower                                                        |
| sympy_sum                | 184 ms                                                                | 208 ms: 1.13x slower                                                        |
| genshi_xml               | 69.8 ms                                                               | 81.5 ms: 1.17x slower                                                       |
| python_startup           | 11.2 ms                                                               | 13.1 ms: 1.17x slower                                                       |
| regex_effbot             | 4.25 ms                                                               | 4.99 ms: 1.17x slower                                                       |
| coverage                 | 83.6 ms                                                               | 100 ms: 1.20x slower                                                        |
| telco                    | 8.49 ms                                                               | 10.3 ms: 1.21x slower                                                       |
| gc_traversal             | 4.15 ms                                                               | 5.13 ms: 1.23x slower                                                       |
| python_startup_no_site   | 6.89 ms                                                               | 8.74 ms: 1.27x slower                                                       |
| Geometric mean           | (ref)                                                                 | 1.18x faster                                                                |

Benchmark hidden because not significant (4): pylint, genshi_text, pidigits, pickle_list
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240910-3.14.0a0-8cbca05-JIT/bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.24x