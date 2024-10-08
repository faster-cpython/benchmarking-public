# Results vs. 3.13.0b2

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: linux-aarch64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.09x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 380 ms: 1.25x slower                                                    |
| docutils       | 3.10 sec                                                     | 3.98 sec: 1.28x slower                                                  |
| html5lib       | 66.1 ms                                                      | 71.3 ms: 1.08x slower                                                   |
| tornado_http   | 128 ms                                                       | 147 ms: 1.15x slower                                                    |
| Geometric mean | (ref)                                                        | 1.19x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 476 ms                                                       | 426 ms: 1.12x faster                                                    |
| async_tree_none            | 492 ms                                                       | 444 ms: 1.11x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 588 ms: 1.10x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.17 sec: 1.09x faster                                                  |
| async_tree_memoization_tg  | 604 ms                                                       | 564 ms: 1.07x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.14 sec: 1.07x faster                                                  |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 757 ms: 1.05x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 742 ms: 1.03x faster                                                    |
| Geometric mean             | (ref)                                                        | 1.08x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 87.5 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                        | 1.02x faster                                                            |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 242 ms: 1.07x faster                                                    |
| regex_effbot   | 4.98 ms                                                      | 4.88 ms: 1.02x faster                                                   |
| regex_v8       | 31.1 ms                                                      | 31.5 ms: 1.01x slower                                                   |
| regex_compile  | 128 ms                                                       | 190 ms: 1.49x slower                                                    |
| Geometric mean | (ref)                                                        | 1.08x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate   | 114 ms                                                       | 111 ms: 1.03x faster                                                    |
| json_loads           | 32.1 us                                                      | 31.5 us: 1.02x faster                                                   |
| unpickle             | 19.8 us                                                      | 19.4 us: 1.02x faster                                                   |
| unpickle_list        | 6.52 us                                                      | 6.41 us: 1.02x faster                                                   |
| xml_etree_process    | 80.8 ms                                                      | 79.9 ms: 1.01x faster                                                   |
| pickle_dict          | 37.6 us                                                      | 38.2 us: 1.01x slower                                                   |
| xml_etree_iterparse  | 147 ms                                                       | 149 ms: 1.02x slower                                                    |
| tomli_loads          | 2.57 sec                                                     | 2.63 sec: 1.02x slower                                                  |
| pickle               | 13.4 us                                                      | 13.8 us: 1.03x slower                                                   |
| json_dumps           | 13.1 ms                                                      | 13.5 ms: 1.03x slower                                                   |
| pickle_pure_python   | 359 us                                                       | 380 us: 1.06x slower                                                    |
| unpickle_pure_python | 251 us                                                       | 267 us: 1.06x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (2): xml_etree_parse, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.60 ms                                                      | 8.80 ms: 1.02x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 13.2 ms                                                      | 13.1 ms: 1.01x faster                                                   |
| django_template | 42.3 ms                                                      | 50.8 ms: 1.20x slower                                                   |
| genshi_text     | 27.4 ms                                                      | 35.7 ms: 1.30x slower                                                   |
| genshi_xml      | 60.4 ms                                                      | 82.2 ms: 1.36x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.21x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 50.8 us                                                      | 37.2 us: 1.37x faster                                                   |
| deepcopy                   | 448 us                                                       | 394 us: 1.14x faster                                                    |
| async_tree_none_tg         | 476 ms                                                       | 426 ms: 1.12x faster                                                    |
| async_tree_none            | 492 ms                                                       | 444 ms: 1.11x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 588 ms: 1.10x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.17 sec: 1.09x faster                                                  |
| async_tree_memoization_tg  | 604 ms                                                       | 564 ms: 1.07x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.14 sec: 1.07x faster                                                  |
| regex_dna                  | 259 ms                                                       | 242 ms: 1.07x faster                                                    |
| pathlib                    | 22.8 ms                                                      | 21.5 ms: 1.06x faster                                                   |
| scimark_sor                | 159 ms                                                       | 152 ms: 1.05x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 757 ms: 1.05x faster                                                    |
| float                      | 91.4 ms                                                      | 87.5 ms: 1.04x faster                                                   |
| deepcopy_reduce            | 4.04 us                                                      | 3.86 us: 1.04x faster                                                   |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 742 ms: 1.03x faster                                                    |
| xml_etree_generate         | 114 ms                                                       | 111 ms: 1.03x faster                                                    |
| regex_effbot               | 4.98 ms                                                      | 4.88 ms: 1.02x faster                                                   |
| json_loads                 | 32.1 us                                                      | 31.5 us: 1.02x faster                                                   |
| unpickle                   | 19.8 us                                                      | 19.4 us: 1.02x faster                                                   |
| unpickle_list              | 6.52 us                                                      | 6.41 us: 1.02x faster                                                   |
| coroutines                 | 29.0 ms                                                      | 28.6 ms: 1.01x faster                                                   |
| xml_etree_process          | 80.8 ms                                                      | 79.9 ms: 1.01x faster                                                   |
| mako                       | 13.2 ms                                                      | 13.1 ms: 1.01x faster                                                   |
| asyncio_websockets         | 657 ms                                                       | 663 ms: 1.01x slower                                                    |
| regex_v8                   | 31.1 ms                                                      | 31.5 ms: 1.01x slower                                                   |
| pickle_dict                | 37.6 us                                                      | 38.2 us: 1.01x slower                                                   |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.25 sec: 1.02x slower                                                  |
| xml_etree_iterparse        | 147 ms                                                       | 149 ms: 1.02x slower                                                    |
| bpe_tokeniser              | 5.83 sec                                                     | 5.94 sec: 1.02x slower                                                  |
| thrift                     | 962 us                                                       | 981 us: 1.02x slower                                                    |
| coverage                   | 98.4 ms                                                      | 101 ms: 1.02x slower                                                    |
| tomli_loads                | 2.57 sec                                                     | 2.63 sec: 1.02x slower                                                  |
| python_startup_no_site     | 8.60 ms                                                      | 8.80 ms: 1.02x slower                                                   |
| async_generators           | 488 ms                                                       | 501 ms: 1.03x slower                                                    |
| pickle                     | 13.4 us                                                      | 13.8 us: 1.03x slower                                                   |
| spectral_norm              | 141 ms                                                       | 145 ms: 1.03x slower                                                    |
| scimark_fft                | 445 ms                                                       | 459 ms: 1.03x slower                                                    |
| json_dumps                 | 13.1 ms                                                      | 13.5 ms: 1.03x slower                                                   |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.82 ms: 1.04x slower                                                   |
| logging_simple             | 7.21 us                                                      | 7.52 us: 1.04x slower                                                   |
| telco                      | 10.0 ms                                                      | 10.5 ms: 1.05x slower                                                   |
| logging_silent             | 133 ns                                                       | 140 ns: 1.05x slower                                                    |
| logging_format             | 7.82 us                                                      | 8.20 us: 1.05x slower                                                   |
| mdp                        | 3.33 sec                                                     | 3.50 sec: 1.05x slower                                                  |
| scimark_lu                 | 141 ms                                                       | 149 ms: 1.05x slower                                                    |
| asyncio_tcp                | 584 ms                                                       | 619 ms: 1.06x slower                                                    |
| pickle_pure_python         | 359 us                                                       | 380 us: 1.06x slower                                                    |
| unpickle_pure_python       | 251 us                                                       | 267 us: 1.06x slower                                                    |
| typing_runtime_protocols   | 193 us                                                       | 207 us: 1.07x slower                                                    |
| bench_mp_pool              | 7.03 ms                                                      | 7.57 ms: 1.08x slower                                                   |
| html5lib                   | 66.1 ms                                                      | 71.3 ms: 1.08x slower                                                   |
| bench_thread_pool          | 1.26 ms                                                      | 1.36 ms: 1.08x slower                                                   |
| crypto_pyaes               | 82.0 ms                                                      | 89.4 ms: 1.09x slower                                                   |
| meteor_contest             | 113 ms                                                       | 124 ms: 1.10x slower                                                    |
| fannkuch                   | 451 ms                                                       | 503 ms: 1.11x slower                                                    |
| deltablue                  | 3.88 ms                                                      | 4.36 ms: 1.12x slower                                                   |
| scimark_monte_carlo        | 82.3 ms                                                      | 92.5 ms: 1.12x slower                                                   |
| tornado_http               | 128 ms                                                       | 147 ms: 1.15x slower                                                    |
| go                         | 161 ms                                                       | 186 ms: 1.16x slower                                                    |
| sqlglot_normalize          | 129 ms                                                       | 151 ms: 1.17x slower                                                    |
| pyflate                    | 557 ms                                                       | 654 ms: 1.17x slower                                                    |
| raytrace                   | 297 ms                                                       | 350 ms: 1.18x slower                                                    |
| richards                   | 55.9 ms                                                      | 66.3 ms: 1.19x slower                                                   |
| comprehensions             | 20.5 us                                                      | 24.5 us: 1.19x slower                                                   |
| django_template            | 42.3 ms                                                      | 50.8 ms: 1.20x slower                                                   |
| richards_super             | 62.3 ms                                                      | 75.3 ms: 1.21x slower                                                   |
| sqlglot_parse              | 1.42 ms                                                      | 1.77 ms: 1.24x slower                                                   |
| 2to3                       | 305 ms                                                       | 380 ms: 1.25x slower                                                    |
| sqlglot_optimize           | 62.6 ms                                                      | 78.9 ms: 1.26x slower                                                   |
| pycparser                  | 1.22 sec                                                     | 1.54 sec: 1.26x slower                                                  |
| docutils                   | 3.10 sec                                                     | 3.98 sec: 1.28x slower                                                  |
| sqlglot_transpile          | 1.71 ms                                                      | 2.21 ms: 1.29x slower                                                   |
| nqueens                    | 98.9 ms                                                      | 128 ms: 1.30x slower                                                    |
| genshi_text                | 27.4 ms                                                      | 35.7 ms: 1.30x slower                                                   |
| pprint_safe_repr           | 933 ms                                                       | 1.25 sec: 1.34x slower                                                  |
| chaos                      | 68.3 ms                                                      | 92.1 ms: 1.35x slower                                                   |
| pprint_pformat             | 1.93 sec                                                     | 2.60 sec: 1.35x slower                                                  |
| sympy_expand               | 457 ms                                                       | 618 ms: 1.35x slower                                                    |
| genshi_xml                 | 60.4 ms                                                      | 82.2 ms: 1.36x slower                                                   |
| dulwich_log                | 58.5 ms                                                      | 80.8 ms: 1.38x slower                                                   |
| sympy_str                  | 265 ms                                                       | 368 ms: 1.39x slower                                                    |
| sympy_integrate            | 20.9 ms                                                      | 29.0 ms: 1.39x slower                                                   |
| pylint                     | 337 ms                                                       | 473 ms: 1.40x slower                                                    |
| hexiom                     | 7.08 ms                                                      | 10.2 ms: 1.45x slower                                                   |
| regex_compile              | 128 ms                                                       | 190 ms: 1.49x slower                                                    |
| sympy_sum                  | 144 ms                                                       | 216 ms: 1.50x slower                                                    |
| generators                 | 37.1 ms                                                      | 57.4 ms: 1.54x slower                                                   |
| Geometric mean             | (ref)                                                        | 1.09x slower                                                            |

Benchmark hidden because not significant (9): create_gc_cycles, xml_etree_parse, gc_traversal, pickle_list, sqlite_synth, nbody, pidigits, python_startup, json
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240914-3.14.0a0-401fff7-JIT/bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.09x