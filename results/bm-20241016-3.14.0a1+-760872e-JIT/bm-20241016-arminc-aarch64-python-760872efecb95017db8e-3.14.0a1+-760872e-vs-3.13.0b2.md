# Results vs. 3.13.0b2

- fork: python
- ref: 760872efecb95017db8e
- machine: linux-aarch64
- commit hash: 760872e
- commit date: 2024-10-16
- overall geometric mean: 1.16x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-arminc-aarch64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 381 ms: 1.25x slower                                                     |
| docutils       | 3.10 sec                                                     | 3.65 sec: 1.18x slower                                                   |
| html5lib       | 66.1 ms                                                      | 71.5 ms: 1.08x slower                                                    |
| tornado_http   | 128 ms                                                       | 147 ms: 1.15x slower                                                     |
| Geometric mean | (ref)                                                        | 1.16x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-arminc-aarch64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 604 ms                                                       | 540 ms: 1.12x faster                                                     |
| async_tree_none            | 492 ms                                                       | 455 ms: 1.08x faster                                                     |
| async_tree_memoization     | 645 ms                                                       | 597 ms: 1.08x faster                                                     |
| async_tree_none_tg         | 476 ms                                                       | 446 ms: 1.07x faster                                                     |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 752 ms: 1.05x faster                                                     |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 734 ms: 1.04x faster                                                     |
| async_tree_io              | 1.22 sec                                                     | 1.18 sec: 1.04x faster                                                   |
| async_tree_io_tg           | 1.27 sec                                                     | 1.25 sec: 1.02x faster                                                   |
| Geometric mean             | (ref)                                                        | 1.06x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-arminc-aarch64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 98.0 ms: 1.07x slower                                                    |
| Geometric mean | (ref)                                                        | 1.03x slower                                                             |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-arminc-aarch64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 244 ms: 1.06x faster                                                     |
| regex_effbot   | 4.98 ms                                                      | 4.85 ms: 1.03x faster                                                    |
| regex_v8       | 31.1 ms                                                      | 31.4 ms: 1.01x slower                                                    |
| regex_compile  | 128 ms                                                       | 169 ms: 1.32x slower                                                     |
| Geometric mean | (ref)                                                        | 1.05x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-arminc-aarch64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle             | 19.8 us                                                      | 19.0 us: 1.04x faster                                                    |
| json_loads           | 32.1 us                                                      | 31.4 us: 1.02x faster                                                    |
| xml_etree_generate   | 114 ms                                                       | 111 ms: 1.02x faster                                                     |
| xml_etree_iterparse  | 147 ms                                                       | 150 ms: 1.02x slower                                                     |
| unpickle_list        | 6.52 us                                                      | 6.67 us: 1.02x slower                                                    |
| pickle               | 13.4 us                                                      | 13.8 us: 1.03x slower                                                    |
| tomli_loads          | 2.57 sec                                                     | 2.64 sec: 1.03x slower                                                   |
| unpickle_pure_python | 251 us                                                       | 268 us: 1.07x slower                                                     |
| pickle_pure_python   | 359 us                                                       | 389 us: 1.08x slower                                                     |
| json_dumps           | 13.1 ms                                                      | 14.3 ms: 1.09x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                             |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_process, pickle_list, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-arminc-aarch64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.60 ms                                                      | 8.74 ms: 1.02x slower                                                    |
| python_startup         | 13.0 ms                                                      | 14.6 ms: 1.13x slower                                                    |
| Geometric mean         | (ref)                                                        | 1.07x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-arminc-aarch64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 42.3 ms                                                      | 51.1 ms: 1.21x slower                                                    |
| genshi_text     | 27.4 ms                                                      | 33.5 ms: 1.22x slower                                                    |
| genshi_xml      | 60.4 ms                                                      | 81.5 ms: 1.35x slower                                                    |
| Geometric mean  | (ref)                                                        | 1.19x slower                                                             |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-arminc-aarch64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy_memo              | 50.8 us                                                      | 38.9 us: 1.31x faster                                                    |
| deepcopy                   | 448 us                                                       | 377 us: 1.19x faster                                                     |
| async_tree_memoization_tg  | 604 ms                                                       | 540 ms: 1.12x faster                                                     |
| async_tree_none            | 492 ms                                                       | 455 ms: 1.08x faster                                                     |
| async_tree_memoization     | 645 ms                                                       | 597 ms: 1.08x faster                                                     |
| async_tree_none_tg         | 476 ms                                                       | 446 ms: 1.07x faster                                                     |
| regex_dna                  | 259 ms                                                       | 244 ms: 1.06x faster                                                     |
| pathlib                    | 22.8 ms                                                      | 21.6 ms: 1.05x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 752 ms: 1.05x faster                                                     |
| telco                      | 10.0 ms                                                      | 9.61 ms: 1.04x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 734 ms: 1.04x faster                                                     |
| unpickle                   | 19.8 us                                                      | 19.0 us: 1.04x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.18 sec: 1.04x faster                                                   |
| regex_effbot               | 4.98 ms                                                      | 4.85 ms: 1.03x faster                                                    |
| json_loads                 | 32.1 us                                                      | 31.4 us: 1.02x faster                                                    |
| deepcopy_reduce            | 4.04 us                                                      | 3.96 us: 1.02x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.25 sec: 1.02x faster                                                   |
| xml_etree_generate         | 114 ms                                                       | 111 ms: 1.02x faster                                                     |
| coroutines                 | 29.0 ms                                                      | 28.5 ms: 1.02x faster                                                    |
| regex_v8                   | 31.1 ms                                                      | 31.4 ms: 1.01x slower                                                    |
| python_startup_no_site     | 8.60 ms                                                      | 8.74 ms: 1.02x slower                                                    |
| bpe_tokeniser              | 5.83 sec                                                     | 5.92 sec: 1.02x slower                                                   |
| xml_etree_iterparse        | 147 ms                                                       | 150 ms: 1.02x slower                                                     |
| unpickle_list              | 6.52 us                                                      | 6.67 us: 1.02x slower                                                    |
| scimark_fft                | 445 ms                                                       | 456 ms: 1.02x slower                                                     |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.27 sec: 1.03x slower                                                   |
| pickle                     | 13.4 us                                                      | 13.8 us: 1.03x slower                                                    |
| tomli_loads                | 2.57 sec                                                     | 2.64 sec: 1.03x slower                                                   |
| logging_simple             | 7.21 us                                                      | 7.47 us: 1.04x slower                                                    |
| logging_format             | 7.82 us                                                      | 8.18 us: 1.05x slower                                                    |
| async_generators           | 488 ms                                                       | 510 ms: 1.05x slower                                                     |
| mdp                        | 3.33 sec                                                     | 3.49 sec: 1.05x slower                                                   |
| unpickle_pure_python       | 251 us                                                       | 268 us: 1.07x slower                                                     |
| scimark_lu                 | 141 ms                                                       | 151 ms: 1.07x slower                                                     |
| float                      | 91.4 ms                                                      | 98.0 ms: 1.07x slower                                                    |
| asyncio_tcp                | 584 ms                                                       | 629 ms: 1.08x slower                                                     |
| html5lib                   | 66.1 ms                                                      | 71.5 ms: 1.08x slower                                                    |
| pickle_pure_python         | 359 us                                                       | 389 us: 1.08x slower                                                     |
| bench_thread_pool          | 1.26 ms                                                      | 1.37 ms: 1.09x slower                                                    |
| json_dumps                 | 13.1 ms                                                      | 14.3 ms: 1.09x slower                                                    |
| scimark_monte_carlo        | 82.3 ms                                                      | 90.1 ms: 1.10x slower                                                    |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 7.19 ms: 1.10x slower                                                    |
| fannkuch                   | 451 ms                                                       | 495 ms: 1.10x slower                                                     |
| meteor_contest             | 113 ms                                                       | 125 ms: 1.10x slower                                                     |
| spectral_norm              | 141 ms                                                       | 155 ms: 1.10x slower                                                     |
| pyflate                    | 557 ms                                                       | 612 ms: 1.10x slower                                                     |
| crypto_pyaes               | 82.0 ms                                                      | 90.2 ms: 1.10x slower                                                    |
| typing_runtime_protocols   | 193 us                                                       | 214 us: 1.11x slower                                                     |
| python_startup             | 13.0 ms                                                      | 14.6 ms: 1.13x slower                                                    |
| go                         | 161 ms                                                       | 184 ms: 1.14x slower                                                     |
| richards_super             | 62.3 ms                                                      | 71.5 ms: 1.15x slower                                                    |
| tornado_http               | 128 ms                                                       | 147 ms: 1.15x slower                                                     |
| richards                   | 55.9 ms                                                      | 64.3 ms: 1.15x slower                                                    |
| deltablue                  | 3.88 ms                                                      | 4.52 ms: 1.16x slower                                                    |
| docutils                   | 3.10 sec                                                     | 3.65 sec: 1.18x slower                                                   |
| sqlglot_parse              | 1.42 ms                                                      | 1.70 ms: 1.19x slower                                                    |
| sqlglot_normalize          | 129 ms                                                       | 156 ms: 1.20x slower                                                     |
| comprehensions             | 20.5 us                                                      | 24.7 us: 1.21x slower                                                    |
| raytrace                   | 297 ms                                                       | 358 ms: 1.21x slower                                                     |
| django_template            | 42.3 ms                                                      | 51.1 ms: 1.21x slower                                                    |
| pycparser                  | 1.22 sec                                                     | 1.48 sec: 1.21x slower                                                   |
| genshi_text                | 27.4 ms                                                      | 33.5 ms: 1.22x slower                                                    |
| nqueens                    | 98.9 ms                                                      | 122 ms: 1.23x slower                                                     |
| gc_traversal               | 5.17 ms                                                      | 6.43 ms: 1.24x slower                                                    |
| chaos                      | 68.3 ms                                                      | 85.0 ms: 1.25x slower                                                    |
| 2to3                       | 305 ms                                                       | 381 ms: 1.25x slower                                                     |
| sqlglot_transpile          | 1.71 ms                                                      | 2.18 ms: 1.28x slower                                                    |
| pprint_safe_repr           | 933 ms                                                       | 1.20 sec: 1.28x slower                                                   |
| sympy_expand               | 457 ms                                                       | 592 ms: 1.29x slower                                                     |
| sqlglot_optimize           | 62.6 ms                                                      | 81.8 ms: 1.31x slower                                                    |
| pprint_pformat             | 1.93 sec                                                     | 2.54 sec: 1.32x slower                                                   |
| regex_compile              | 128 ms                                                       | 169 ms: 1.32x slower                                                     |
| dulwich_log                | 58.5 ms                                                      | 78.0 ms: 1.33x slower                                                    |
| sympy_str                  | 265 ms                                                       | 358 ms: 1.35x slower                                                     |
| genshi_xml                 | 60.4 ms                                                      | 81.5 ms: 1.35x slower                                                    |
| sympy_integrate            | 20.9 ms                                                      | 29.1 ms: 1.40x slower                                                    |
| hexiom                     | 7.08 ms                                                      | 10.2 ms: 1.45x slower                                                    |
| pylint                     | 337 ms                                                       | 492 ms: 1.46x slower                                                     |
| sympy_sum                  | 144 ms                                                       | 215 ms: 1.50x slower                                                     |
| generators                 | 37.1 ms                                                      | 59.0 ms: 1.59x slower                                                    |
| create_gc_cycles           | 2.33 ms                                                      | 3.71 ms: 1.59x slower                                                    |
| bench_mp_pool              | 7.03 ms                                                      | 1.59 sec: 226.01x slower                                                 |
| Geometric mean             | (ref)                                                        | 1.16x slower                                                             |

Benchmark hidden because not significant (14): xml_etree_parse, scimark_sor, json, logging_silent, thrift, xml_etree_process, pickle_list, mako, pidigits, sqlite_synth, pickle_dict, asyncio_websockets, nbody, coverage
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (2) of results/bm-20241016-3.14.0a1+-760872e-JIT/bm-20241016-arminc-aarch64-python-760872efecb95017db8e-3.14.0a1+-760872e.json: sphinx, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.20x