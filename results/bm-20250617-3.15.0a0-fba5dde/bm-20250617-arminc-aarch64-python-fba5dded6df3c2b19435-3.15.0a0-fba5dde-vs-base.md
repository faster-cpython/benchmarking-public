# Results vs. base

- fork: python
- ref: fba5dded6df3c2b19435
- machine: linux-aarch64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.164x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250617-arminc-aarch64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 297 ms                                                                  | 357 ms: 1.20x slower                                                    |
| docutils       | 2.92 sec                                                                | 3.44 sec: 1.18x slower                                                  |
| html5lib       | 60.9 ms                                                                 | 67.3 ms: 1.11x slower                                                   |
| sphinx         | 1.13 sec                                                                | 1.36 sec: 1.21x slower                                                  |
| Geometric mean | (ref)                                                                   | 1.17x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250617-arminc-aarch64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| coroutines                 | 30.0 ms                                                                 | 33.0 ms: 1.10x slower                                                   |
| async_tree_memoization_tg  | 482 ms                                                                  | 534 ms: 1.11x slower                                                    |
| async_tree_io              | 910 ms                                                                  | 1.01 sec: 1.11x slower                                                  |
| async_tree_io_tg           | 928 ms                                                                  | 1.04 sec: 1.12x slower                                                  |
| async_tree_none_tg         | 388 ms                                                                  | 434 ms: 1.12x slower                                                    |
| async_tree_none            | 396 ms                                                                  | 449 ms: 1.14x slower                                                    |
| async_tree_memoization     | 468 ms                                                                  | 532 ms: 1.14x slower                                                    |
| async_generators           | 447 ms                                                                  | 515 ms: 1.15x slower                                                    |
| async_tree_cpu_io_mixed_tg | 655 ms                                                                  | 814 ms: 1.24x slower                                                    |
| async_tree_cpu_io_mixed    | 656 ms                                                                  | 823 ms: 1.25x slower                                                    |
| Geometric mean             | (ref)                                                                   | 1.13x slower                                                            |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250617-arminc-aarch64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 85.6 ms                                                                 | 96.7 ms: 1.13x slower                                                   |
| nbody          | 120 ms                                                                  | 141 ms: 1.18x slower                                                    |
| pidigits       | 236 ms                                                                  | 282 ms: 1.20x slower                                                    |
| Geometric mean | (ref)                                                                   | 1.17x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250617-arminc-aarch64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 221 ms                                                                  | 225 ms: 1.02x slower                                                    |
| regex_effbot   | 3.84 ms                                                                 | 4.08 ms: 1.06x slower                                                   |
| regex_v8       | 27.7 ms                                                                 | 30.3 ms: 1.10x slower                                                   |
| regex_compile  | 122 ms                                                                  | 155 ms: 1.27x slower                                                    |
| Geometric mean | (ref)                                                                   | 1.11x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250617-arminc-aarch64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_loads           | 33.0 us                                                                 | 38.5 us: 1.17x slower                                                   |
| tomli_loads          | 2.46 sec                                                                | 2.93 sec: 1.19x slower                                                  |
| pickle_pure_python   | 388 us                                                                  | 468 us: 1.21x slower                                                    |
| xml_etree_iterparse  | 141 ms                                                                  | 170 ms: 1.21x slower                                                    |
| json_dumps           | 14.0 ms                                                                 | 17.4 ms: 1.24x slower                                                   |
| unpickle_pure_python | 263 us                                                                  | 329 us: 1.25x slower                                                    |
| xml_etree_parse      | 179 ms                                                                  | 227 ms: 1.27x slower                                                    |
| xml_etree_process    | 79.1 ms                                                                 | 110 ms: 1.39x slower                                                    |
| xml_etree_generate   | 111 ms                                                                  | 163 ms: 1.47x slower                                                    |
| Geometric mean       | (ref)                                                                   | 1.26x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250617-arminc-aarch64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.60 ms                                                                 | 9.73 ms: 1.13x slower                                                   |
| python_startup         | 15.0 ms                                                                 | 17.1 ms: 1.14x slower                                                   |
| Geometric mean         | (ref)                                                                   | 1.14x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250617-arminc-aarch64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 14.0 ms                                                                 | 17.0 ms: 1.22x slower                                                   |
| genshi_xml      | 61.5 ms                                                                 | 75.1 ms: 1.22x slower                                                   |
| genshi_text     | 27.2 ms                                                                 | 33.3 ms: 1.22x slower                                                   |
| django_template | 39.8 ms                                                                 | 53.6 ms: 1.35x slower                                                   |
| Geometric mean  | (ref)                                                                   | 1.25x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20250617-arminc-aarch64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna                  | 221 ms                                                                  | 225 ms: 1.02x slower                                                    |
| shortest_path              | 587 ms                                                                  | 608 ms: 1.04x slower                                                    |
| create_gc_cycles           | 3.69 ms                                                                 | 3.86 ms: 1.05x slower                                                   |
| k_core                     | 2.81 sec                                                                | 2.95 sec: 1.05x slower                                                  |
| regex_effbot               | 3.84 ms                                                                 | 4.08 ms: 1.06x slower                                                   |
| gc_traversal               | 6.71 ms                                                                 | 7.30 ms: 1.09x slower                                                   |
| regex_v8                   | 27.7 ms                                                                 | 30.3 ms: 1.10x slower                                                   |
| coroutines                 | 30.0 ms                                                                 | 33.0 ms: 1.10x slower                                                   |
| html5lib                   | 60.9 ms                                                                 | 67.3 ms: 1.11x slower                                                   |
| pyflate                    | 525 ms                                                                  | 581 ms: 1.11x slower                                                    |
| async_tree_memoization_tg  | 482 ms                                                                  | 534 ms: 1.11x slower                                                    |
| generators                 | 35.8 ms                                                                 | 39.7 ms: 1.11x slower                                                   |
| go                         | 127 ms                                                                  | 141 ms: 1.11x slower                                                    |
| async_tree_io              | 910 ms                                                                  | 1.01 sec: 1.11x slower                                                  |
| async_tree_io_tg           | 928 ms                                                                  | 1.04 sec: 1.12x slower                                                  |
| async_tree_none_tg         | 388 ms                                                                  | 434 ms: 1.12x slower                                                    |
| scimark_sparse_mat_mult    | 6.93 ms                                                                 | 7.76 ms: 1.12x slower                                                   |
| deepcopy_memo              | 38.6 us                                                                 | 43.3 us: 1.12x slower                                                   |
| float                      | 85.6 ms                                                                 | 96.7 ms: 1.13x slower                                                   |
| deltablue                  | 4.01 ms                                                                 | 4.54 ms: 1.13x slower                                                   |
| python_startup_no_site     | 8.60 ms                                                                 | 9.73 ms: 1.13x slower                                                   |
| async_tree_none            | 396 ms                                                                  | 449 ms: 1.14x slower                                                    |
| comprehensions             | 20.3 us                                                                 | 23.1 us: 1.14x slower                                                   |
| async_tree_memoization     | 468 ms                                                                  | 532 ms: 1.14x slower                                                    |
| python_startup             | 15.0 ms                                                                 | 17.1 ms: 1.14x slower                                                   |
| scimark_fft                | 435 ms                                                                  | 498 ms: 1.14x slower                                                    |
| meteor_contest             | 112 ms                                                                  | 128 ms: 1.14x slower                                                    |
| pylint                     | 319 ms                                                                  | 367 ms: 1.15x slower                                                    |
| async_generators           | 447 ms                                                                  | 515 ms: 1.15x slower                                                    |
| json_loads                 | 33.0 us                                                                 | 38.5 us: 1.17x slower                                                   |
| scimark_sor                | 144 ms                                                                  | 169 ms: 1.17x slower                                                    |
| chaos                      | 70.3 ms                                                                 | 82.7 ms: 1.18x slower                                                   |
| docutils                   | 2.92 sec                                                                | 3.44 sec: 1.18x slower                                                  |
| nbody                      | 120 ms                                                                  | 141 ms: 1.18x slower                                                    |
| sympy_integrate            | 19.9 ms                                                                 | 23.5 ms: 1.18x slower                                                   |
| richards_super             | 60.9 ms                                                                 | 72.2 ms: 1.19x slower                                                   |
| mdp                        | 1.66 sec                                                                | 1.97 sec: 1.19x slower                                                  |
| tomli_loads                | 2.46 sec                                                                | 2.93 sec: 1.19x slower                                                  |
| pathlib                    | 22.4 ms                                                                 | 26.8 ms: 1.20x slower                                                   |
| pidigits                   | 236 ms                                                                  | 282 ms: 1.20x slower                                                    |
| raytrace                   | 325 ms                                                                  | 390 ms: 1.20x slower                                                    |
| scimark_monte_carlo        | 79.8 ms                                                                 | 95.9 ms: 1.20x slower                                                   |
| 2to3                       | 297 ms                                                                  | 357 ms: 1.20x slower                                                    |
| pickle_pure_python         | 388 us                                                                  | 468 us: 1.21x slower                                                    |
| pycparser                  | 1.23 sec                                                                | 1.49 sec: 1.21x slower                                                  |
| xml_etree_iterparse        | 141 ms                                                                  | 170 ms: 1.21x slower                                                    |
| sphinx                     | 1.13 sec                                                                | 1.36 sec: 1.21x slower                                                  |
| json                       | 5.67 ms                                                                 | 6.86 ms: 1.21x slower                                                   |
| deepcopy                   | 334 us                                                                  | 406 us: 1.21x slower                                                    |
| hexiom                     | 6.77 ms                                                                 | 8.23 ms: 1.21x slower                                                   |
| richards                   | 52.6 ms                                                                 | 64.0 ms: 1.22x slower                                                   |
| scimark_lu                 | 152 ms                                                                  | 186 ms: 1.22x slower                                                    |
| sqlglot_v2_transpile       | 1.82 ms                                                                 | 2.22 ms: 1.22x slower                                                   |
| bpe_tokeniser              | 5.52 sec                                                                | 6.73 sec: 1.22x slower                                                  |
| mako                       | 14.0 ms                                                                 | 17.0 ms: 1.22x slower                                                   |
| logging_simple             | 7.70 us                                                                 | 9.40 us: 1.22x slower                                                   |
| genshi_xml                 | 61.5 ms                                                                 | 75.1 ms: 1.22x slower                                                   |
| genshi_text                | 27.2 ms                                                                 | 33.3 ms: 1.22x slower                                                   |
| logging_format             | 8.38 us                                                                 | 10.3 us: 1.23x slower                                                   |
| fannkuch                   | 481 ms                                                                  | 590 ms: 1.23x slower                                                    |
| crypto_pyaes               | 84.9 ms                                                                 | 105 ms: 1.24x slower                                                    |
| json_dumps                 | 14.0 ms                                                                 | 17.4 ms: 1.24x slower                                                   |
| sympy_sum                  | 145 ms                                                                  | 180 ms: 1.24x slower                                                    |
| async_tree_cpu_io_mixed_tg | 655 ms                                                                  | 814 ms: 1.24x slower                                                    |
| sqlglot_v2_parse           | 1.42 ms                                                                 | 1.77 ms: 1.25x slower                                                   |
| unpickle_pure_python       | 263 us                                                                  | 329 us: 1.25x slower                                                    |
| async_tree_cpu_io_mixed    | 656 ms                                                                  | 823 ms: 1.25x slower                                                    |
| spectral_norm              | 124 ms                                                                  | 156 ms: 1.26x slower                                                    |
| nqueens                    | 99.0 ms                                                                 | 125 ms: 1.26x slower                                                    |
| xml_etree_parse            | 179 ms                                                                  | 227 ms: 1.27x slower                                                    |
| sqlite_synth               | 3.80 us                                                                 | 4.82 us: 1.27x slower                                                   |
| subparsers                 | 28.4 ms                                                                 | 36.2 ms: 1.27x slower                                                   |
| regex_compile              | 122 ms                                                                  | 155 ms: 1.27x slower                                                    |
| sympy_str                  | 265 ms                                                                  | 339 ms: 1.28x slower                                                    |
| thrift                     | 980 us                                                                  | 1.25 ms: 1.28x slower                                                   |
| deepcopy_reduce            | 3.59 us                                                                 | 4.59 us: 1.28x slower                                                   |
| sqlglot_v2_optimize        | 59.9 ms                                                                 | 77.0 ms: 1.29x slower                                                   |
| many_optionals             | 740 us                                                                  | 957 us: 1.29x slower                                                    |
| dulwich_log                | 50.8 ms                                                                 | 66.0 ms: 1.30x slower                                                   |
| sympy_expand               | 466 ms                                                                  | 606 ms: 1.30x slower                                                    |
| sqlglot_v2_normalize       | 123 ms                                                                  | 161 ms: 1.31x slower                                                    |
| typing_runtime_protocols   | 197 us                                                                  | 259 us: 1.32x slower                                                    |
| pprint_pformat             | 2.05 sec                                                                | 2.70 sec: 1.32x slower                                                  |
| pprint_safe_repr           | 1.00 sec                                                                | 1.34 sec: 1.34x slower                                                  |
| django_template            | 39.8 ms                                                                 | 53.6 ms: 1.35x slower                                                   |
| coverage                   | 103 ms                                                                  | 141 ms: 1.36x slower                                                    |
| xml_etree_process          | 79.1 ms                                                                 | 110 ms: 1.39x slower                                                    |
| telco                      | 9.29 ms                                                                 | 13.6 ms: 1.46x slower                                                   |
| xml_etree_generate         | 111 ms                                                                  | 163 ms: 1.47x slower                                                    |
| logging_silent             | 633 ns                                                                  | 946 ns: 1.49x slower                                                    |
| Geometric mean             | (ref)                                                                   | 1.20x slower                                                            |

Benchmark hidden because not significant (3): connected_components, asyncio_websockets, djangocms
Ignored benchmarks (10) of results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.164x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.18x
- 95% likely to have a slowdown of 1.18x
- 99% likely to have a slowdown of 1.16x

# Memory
- memory change: 1.00x