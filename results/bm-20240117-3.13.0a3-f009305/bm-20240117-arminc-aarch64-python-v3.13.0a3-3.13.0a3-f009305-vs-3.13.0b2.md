# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0a3
- machine: linux-aarch64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.00x faster
- HPT reliability: 60.04%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.95x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-arminc-aarch64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| docutils       | 3.10 sec                                                     | 2.90 sec: 1.07x faster                                       |
| tornado_http   | 128 ms                                                       | 137 ms: 1.07x slower                                         |
| Geometric mean | (ref)                                                        | 1.00x slower                                                 |

Benchmark hidden because not significant (3): 2to3, chameleon, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-arminc-aarch64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 791 ms                                                       | 888 ms: 1.12x slower                                         |
| async_tree_io_tg           | 1.27 sec                                                     | 1.44 sec: 1.13x slower                                       |
| async_tree_memoization     | 645 ms                                                       | 745 ms: 1.16x slower                                         |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 895 ms: 1.17x slower                                         |
| async_tree_none            | 492 ms                                                       | 582 ms: 1.18x slower                                         |
| async_tree_io              | 1.22 sec                                                     | 1.45 sec: 1.18x slower                                       |
| async_tree_none_tg         | 476 ms                                                       | 574 ms: 1.21x slower                                         |
| async_tree_memoization_tg  | 604 ms                                                       | 736 ms: 1.22x slower                                         |
| Geometric mean             | (ref)                                                        | 1.17x slower                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-arminc-aarch64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 104 ms: 1.10x faster                                         |
| pidigits       | 234 ms                                                       | 233 ms: 1.01x faster                                         |
| float          | 91.4 ms                                                      | 91.0 ms: 1.00x faster                                        |
| Geometric mean | (ref)                                                        | 1.04x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-arminc-aarch64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_effbot   | 4.98 ms                                                      | 4.65 ms: 1.07x faster                                        |
| regex_v8       | 31.1 ms                                                      | 30.1 ms: 1.03x faster                                        |
| regex_compile  | 128 ms                                                       | 125 ms: 1.02x faster                                         |
| regex_dna      | 259 ms                                                       | 255 ms: 1.01x faster                                         |
| Geometric mean | (ref)                                                        | 1.03x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-arminc-aarch64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| json_dumps           | 13.1 ms                                                      | 12.5 ms: 1.05x faster                                        |
| json_loads           | 32.1 us                                                      | 31.1 us: 1.03x faster                                        |
| pickle_pure_python   | 359 us                                                       | 347 us: 1.03x faster                                         |
| unpickle             | 19.8 us                                                      | 19.6 us: 1.01x faster                                        |
| pickle_dict          | 37.6 us                                                      | 37.3 us: 1.01x faster                                        |
| xml_etree_generate   | 114 ms                                                       | 114 ms: 1.01x slower                                         |
| tomli_loads          | 2.57 sec                                                     | 2.59 sec: 1.01x slower                                       |
| unpickle_pure_python | 251 us                                                       | 256 us: 1.02x slower                                         |
| xml_etree_iterparse  | 147 ms                                                       | 152 ms: 1.04x slower                                         |
| xml_etree_parse      | 191 ms                                                       | 206 ms: 1.08x slower                                         |
| Geometric mean       | (ref)                                                        | 1.00x faster                                                 |

Benchmark hidden because not significant (4): unpickle_list, xml_etree_process, pickle_list, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-arminc-aarch64-python-v3.13.0a3-3.13.0a3-f009305 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 12.1 ms: 1.08x faster                                        |
| python_startup_no_site | 8.60 ms                                                      | 10.3 ms: 1.20x slower                                        |
| Geometric mean         | (ref)                                                        | 1.06x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-arminc-aarch64-python-v3.13.0a3-3.13.0a3-f009305 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 42.3 ms                                                      | 40.7 ms: 1.04x faster                                        |
| mako            | 13.2 ms                                                      | 12.9 ms: 1.02x faster                                        |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                 |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-arminc-aarch64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols   | 193 us                                                       | 135 us: 1.44x faster                                         |
| create_gc_cycles           | 2.33 ms                                                      | 1.91 ms: 1.22x faster                                        |
| gc_traversal               | 5.17 ms                                                      | 4.36 ms: 1.19x faster                                        |
| nbody                      | 114 ms                                                       | 104 ms: 1.10x faster                                         |
| spectral_norm              | 141 ms                                                       | 129 ms: 1.10x faster                                         |
| python_startup             | 13.0 ms                                                      | 12.1 ms: 1.08x faster                                        |
| regex_effbot               | 4.98 ms                                                      | 4.65 ms: 1.07x faster                                        |
| docutils                   | 3.10 sec                                                     | 2.90 sec: 1.07x faster                                       |
| crypto_pyaes               | 82.0 ms                                                      | 77.3 ms: 1.06x faster                                        |
| json_dumps                 | 13.1 ms                                                      | 12.5 ms: 1.05x faster                                        |
| sqlglot_normalize          | 129 ms                                                       | 123 ms: 1.05x faster                                         |
| sqlglot_parse              | 1.42 ms                                                      | 1.36 ms: 1.04x faster                                        |
| sqlite_synth               | 3.90 us                                                      | 3.75 us: 1.04x faster                                        |
| django_template            | 42.3 ms                                                      | 40.7 ms: 1.04x faster                                        |
| thrift                     | 962 us                                                       | 925 us: 1.04x faster                                         |
| asyncio_tcp                | 584 ms                                                       | 562 ms: 1.04x faster                                         |
| comprehensions             | 20.5 us                                                      | 19.8 us: 1.04x faster                                        |
| scimark_fft                | 445 ms                                                       | 430 ms: 1.03x faster                                         |
| scimark_lu                 | 141 ms                                                       | 137 ms: 1.03x faster                                         |
| telco                      | 10.0 ms                                                      | 9.69 ms: 1.03x faster                                        |
| json_loads                 | 32.1 us                                                      | 31.1 us: 1.03x faster                                        |
| sympy_sum                  | 144 ms                                                       | 139 ms: 1.03x faster                                         |
| pickle_pure_python         | 359 us                                                       | 347 us: 1.03x faster                                         |
| sqlglot_optimize           | 62.6 ms                                                      | 60.7 ms: 1.03x faster                                        |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.34 ms: 1.03x faster                                        |
| regex_v8                   | 31.1 ms                                                      | 30.1 ms: 1.03x faster                                        |
| generators                 | 37.1 ms                                                      | 36.0 ms: 1.03x faster                                        |
| flaskblogging              | 4.70 ms                                                      | 4.56 ms: 1.03x faster                                        |
| deepcopy_memo              | 50.8 us                                                      | 49.3 us: 1.03x faster                                        |
| nqueens                    | 98.9 ms                                                      | 96.4 ms: 1.03x faster                                        |
| regex_compile              | 128 ms                                                       | 125 ms: 1.02x faster                                         |
| chaos                      | 68.3 ms                                                      | 66.7 ms: 1.02x faster                                        |
| sympy_str                  | 265 ms                                                       | 259 ms: 1.02x faster                                         |
| richards_super             | 62.3 ms                                                      | 60.9 ms: 1.02x faster                                        |
| sympy_expand               | 457 ms                                                       | 448 ms: 1.02x faster                                         |
| sympy_integrate            | 20.9 ms                                                      | 20.5 ms: 1.02x faster                                        |
| mako                       | 13.2 ms                                                      | 12.9 ms: 1.02x faster                                        |
| async_generators           | 488 ms                                                       | 480 ms: 1.02x faster                                         |
| richards                   | 55.9 ms                                                      | 55.0 ms: 1.02x faster                                        |
| aiohttp                    | 1.18 ms                                                      | 1.16 ms: 1.01x faster                                        |
| regex_dna                  | 259 ms                                                       | 255 ms: 1.01x faster                                         |
| unpickle                   | 19.8 us                                                      | 19.6 us: 1.01x faster                                        |
| deepcopy                   | 448 us                                                       | 444 us: 1.01x faster                                         |
| pprint_pformat             | 1.93 sec                                                     | 1.91 sec: 1.01x faster                                       |
| pickle_dict                | 37.6 us                                                      | 37.3 us: 1.01x faster                                        |
| pidigits                   | 234 ms                                                       | 233 ms: 1.01x faster                                         |
| float                      | 91.4 ms                                                      | 91.0 ms: 1.00x faster                                        |
| xml_etree_generate         | 114 ms                                                       | 114 ms: 1.01x slower                                         |
| logging_silent             | 133 ns                                                       | 134 ns: 1.01x slower                                         |
| tomli_loads                | 2.57 sec                                                     | 2.59 sec: 1.01x slower                                       |
| pyflate                    | 557 ms                                                       | 562 ms: 1.01x slower                                         |
| fannkuch                   | 451 ms                                                       | 456 ms: 1.01x slower                                         |
| coroutines                 | 29.0 ms                                                      | 29.4 ms: 1.01x slower                                        |
| scimark_monte_carlo        | 82.3 ms                                                      | 83.5 ms: 1.01x slower                                        |
| unpickle_pure_python       | 251 us                                                       | 256 us: 1.02x slower                                         |
| scimark_sor                | 159 ms                                                       | 163 ms: 1.02x slower                                         |
| logging_format             | 7.82 us                                                      | 8.00 us: 1.02x slower                                        |
| deltablue                  | 3.88 ms                                                      | 3.98 ms: 1.03x slower                                        |
| xml_etree_iterparse        | 147 ms                                                       | 152 ms: 1.04x slower                                         |
| coverage                   | 98.4 ms                                                      | 102 ms: 1.04x slower                                         |
| pycparser                  | 1.22 sec                                                     | 1.27 sec: 1.04x slower                                       |
| bench_thread_pool          | 1.26 ms                                                      | 1.31 ms: 1.04x slower                                        |
| dulwich_log                | 58.5 ms                                                      | 61.3 ms: 1.05x slower                                        |
| pathlib                    | 22.8 ms                                                      | 24.1 ms: 1.06x slower                                        |
| tornado_http               | 128 ms                                                       | 137 ms: 1.07x slower                                         |
| xml_etree_parse            | 191 ms                                                       | 206 ms: 1.08x slower                                         |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 888 ms: 1.12x slower                                         |
| async_tree_io_tg           | 1.27 sec                                                     | 1.44 sec: 1.13x slower                                       |
| async_tree_memoization     | 645 ms                                                       | 745 ms: 1.16x slower                                         |
| mypy2                      | 767 ms                                                       | 899 ms: 1.17x slower                                         |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 895 ms: 1.17x slower                                         |
| async_tree_none            | 492 ms                                                       | 582 ms: 1.18x slower                                         |
| async_tree_io              | 1.22 sec                                                     | 1.45 sec: 1.18x slower                                       |
| python_startup_no_site     | 8.60 ms                                                      | 10.3 ms: 1.20x slower                                        |
| async_tree_none_tg         | 476 ms                                                       | 574 ms: 1.21x slower                                         |
| async_tree_memoization_tg  | 604 ms                                                       | 736 ms: 1.22x slower                                         |
| Geometric mean             | (ref)                                                        | 1.00x faster                                                 |

Benchmark hidden because not significant (24): pylint, unpickle_list, json, xml_etree_process, bench_mp_pool, genshi_text, raytrace, mdp, meteor_contest, 2to3, deepcopy_reduce, pickle_list, pickle, asyncio_websockets, asyncio_tcp_ssl, go, html5lib, sqlglot_transpile, chameleon, pprint_safe_repr, gunicorn, logging_simple, genshi_xml, hexiom
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser, dask

# HPT report

- Reliability score: 60.04% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.95x