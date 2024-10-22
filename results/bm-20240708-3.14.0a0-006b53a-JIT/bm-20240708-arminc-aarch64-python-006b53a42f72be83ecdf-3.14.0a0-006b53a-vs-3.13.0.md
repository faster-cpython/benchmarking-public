# Results vs. 3.13.0

- fork: python
- ref: 006b53a42f72be83ecdf
- machine: linux-aarch64
- commit hash: 006b53a
- commit date: 2024-07-08
- overall geometric mean: 1.07x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 359 ms: 1.17x slower                                                    |
| docutils       | 2.91 sec                                                 | 3.52 sec: 1.21x slower                                                  |
| html5lib       | 64.3 ms                                                  | 69.6 ms: 1.08x slower                                                   |
| tornado_http   | 131 ms                                                   | 139 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                    | 1.13x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 541 ms: 1.20x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 412 ms: 1.13x faster                                                    |
| async_tree_none            | 493 ms                                                   | 447 ms: 1.10x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 581 ms: 1.08x faster                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.06 sec: 1.04x faster                                                  |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 735 ms: 1.04x faster                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 712 ms: 1.03x faster                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.26 sec: 1.04x slower                                                  |
| coroutines                 | 28.2 ms                                                  | 29.4 ms: 1.04x slower                                                   |
| asyncio_tcp                | 568 ms                                                   | 624 ms: 1.10x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (3): asyncio_websockets, async_generators, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 94.4 ms                                                  | 89.1 ms: 1.06x faster                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 30.5 ms: 1.03x faster                                                   |
| regex_compile  | 128 ms                                                   | 180 ms: 1.40x slower                                                    |
| Geometric mean | (ref)                                                    | 1.08x slower                                                            |

Benchmark hidden because not significant (2): regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 188 ms                                                   | 189 ms: 1.01x slower                                                    |
| tomli_loads          | 2.53 sec                                                 | 2.63 sec: 1.04x slower                                                  |
| xml_etree_iterparse  | 147 ms                                                   | 153 ms: 1.04x slower                                                    |
| json_loads           | 31.4 us                                                  | 33.3 us: 1.06x slower                                                   |
| unpickle_pure_python | 254 us                                                   | 274 us: 1.08x slower                                                    |
| pickle_pure_python   | 359 us                                                   | 412 us: 1.15x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.04x slower                                                            |

Benchmark hidden because not significant (3): xml_etree_process, xml_etree_generate, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 13.3 ms                                                  | 13.1 ms: 1.01x faster                                                   |
| django_template | 42.3 ms                                                  | 50.2 ms: 1.19x slower                                                   |
| genshi_text     | 27.7 ms                                                  | 34.3 ms: 1.24x slower                                                   |
| genshi_xml      | 60.2 ms                                                  | 79.6 ms: 1.32x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.18x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 51.0 us                                                  | 38.1 us: 1.34x faster                                                   |
| deepcopy                   | 451 us                                                   | 374 us: 1.21x faster                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 541 ms: 1.20x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 412 ms: 1.13x faster                                                    |
| async_tree_none            | 493 ms                                                   | 447 ms: 1.10x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 581 ms: 1.08x faster                                                    |
| float                      | 94.4 ms                                                  | 89.1 ms: 1.06x faster                                                   |
| async_tree_io              | 1.11 sec                                                 | 1.06 sec: 1.04x faster                                                  |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 735 ms: 1.04x faster                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 712 ms: 1.03x faster                                                    |
| regex_v8                   | 31.5 ms                                                  | 30.5 ms: 1.03x faster                                                   |
| pathlib                    | 22.4 ms                                                  | 21.7 ms: 1.03x faster                                                   |
| python_startup             | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                   |
| mako                       | 13.3 ms                                                  | 13.1 ms: 1.01x faster                                                   |
| xml_etree_parse            | 188 ms                                                   | 189 ms: 1.01x slower                                                    |
| thrift                     | 946 us                                                   | 958 us: 1.01x slower                                                    |
| richards                   | 53.5 ms                                                  | 54.3 ms: 1.01x slower                                                   |
| logging_format             | 7.83 us                                                  | 7.98 us: 1.02x slower                                                   |
| spectral_norm              | 141 ms                                                   | 144 ms: 1.02x slower                                                    |
| richards_super             | 60.3 ms                                                  | 61.6 ms: 1.02x slower                                                   |
| generators                 | 37.8 ms                                                  | 38.6 ms: 1.02x slower                                                   |
| bpe_tokeniser              | 5.90 sec                                                 | 6.03 sec: 1.02x slower                                                  |
| mdp                        | 3.36 sec                                                 | 3.44 sec: 1.02x slower                                                  |
| coverage                   | 98.5 ms                                                  | 101 ms: 1.02x slower                                                    |
| logging_simple             | 7.04 us                                                  | 7.22 us: 1.03x slower                                                   |
| meteor_contest             | 113 ms                                                   | 117 ms: 1.03x slower                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.26 sec: 1.04x slower                                                  |
| coroutines                 | 28.2 ms                                                  | 29.4 ms: 1.04x slower                                                   |
| tomli_loads                | 2.53 sec                                                 | 2.63 sec: 1.04x slower                                                  |
| xml_etree_iterparse        | 147 ms                                                   | 153 ms: 1.04x slower                                                    |
| scimark_fft                | 447 ms                                                   | 467 ms: 1.04x slower                                                    |
| json                       | 5.61 ms                                                  | 5.87 ms: 1.05x slower                                                   |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 6.89 ms: 1.05x slower                                                   |
| bench_thread_pool          | 1.28 ms                                                  | 1.34 ms: 1.05x slower                                                   |
| fannkuch                   | 452 ms                                                   | 477 ms: 1.06x slower                                                    |
| tornado_http               | 131 ms                                                   | 139 ms: 1.06x slower                                                    |
| crypto_pyaes               | 82.7 ms                                                  | 87.5 ms: 1.06x slower                                                   |
| json_loads                 | 31.4 us                                                  | 33.3 us: 1.06x slower                                                   |
| scimark_monte_carlo        | 83.8 ms                                                  | 89.2 ms: 1.06x slower                                                   |
| pycparser                  | 1.26 sec                                                 | 1.35 sec: 1.07x slower                                                  |
| unpickle_pure_python       | 254 us                                                   | 274 us: 1.08x slower                                                    |
| pyflate                    | 556 ms                                                   | 599 ms: 1.08x slower                                                    |
| html5lib                   | 64.3 ms                                                  | 69.6 ms: 1.08x slower                                                   |
| typing_runtime_protocols   | 192 us                                                   | 208 us: 1.08x slower                                                    |
| telco                      | 9.73 ms                                                  | 10.6 ms: 1.08x slower                                                   |
| raytrace                   | 298 ms                                                   | 325 ms: 1.09x slower                                                    |
| create_gc_cycles           | 2.12 ms                                                  | 2.32 ms: 1.09x slower                                                   |
| asyncio_tcp                | 568 ms                                                   | 624 ms: 1.10x slower                                                    |
| gc_traversal               | 4.53 ms                                                  | 5.00 ms: 1.10x slower                                                   |
| go                         | 163 ms                                                   | 180 ms: 1.10x slower                                                    |
| dask                       | 350 ms                                                   | 388 ms: 1.11x slower                                                    |
| sqlglot_normalize          | 128 ms                                                   | 142 ms: 1.11x slower                                                    |
| bench_mp_pool              | 7.30 ms                                                  | 8.21 ms: 1.12x slower                                                   |
| sqlglot_optimize           | 62.4 ms                                                  | 70.2 ms: 1.13x slower                                                   |
| scimark_sor                | 159 ms                                                   | 179 ms: 1.13x slower                                                    |
| comprehensions             | 20.4 us                                                  | 23.3 us: 1.14x slower                                                   |
| pickle_pure_python         | 359 us                                                   | 412 us: 1.15x slower                                                    |
| sqlglot_parse              | 1.38 ms                                                  | 1.59 ms: 1.15x slower                                                   |
| deltablue                  | 3.85 ms                                                  | 4.47 ms: 1.16x slower                                                   |
| sqlglot_transpile          | 1.73 ms                                                  | 2.01 ms: 1.16x slower                                                   |
| 2to3                       | 306 ms                                                   | 359 ms: 1.17x slower                                                    |
| django_template            | 42.3 ms                                                  | 50.2 ms: 1.19x slower                                                   |
| nqueens                    | 98.7 ms                                                  | 118 ms: 1.20x slower                                                    |
| sympy_expand               | 455 ms                                                   | 550 ms: 1.21x slower                                                    |
| docutils                   | 2.91 sec                                                 | 3.52 sec: 1.21x slower                                                  |
| pylint                     | 343 ms                                                   | 416 ms: 1.21x slower                                                    |
| pprint_safe_repr           | 926 ms                                                   | 1.15 sec: 1.24x slower                                                  |
| genshi_text                | 27.7 ms                                                  | 34.3 ms: 1.24x slower                                                   |
| pprint_pformat             | 1.90 sec                                                 | 2.38 sec: 1.25x slower                                                  |
| sympy_str                  | 264 ms                                                   | 332 ms: 1.26x slower                                                    |
| hexiom                     | 7.13 ms                                                  | 9.01 ms: 1.26x slower                                                   |
| sympy_integrate            | 21.0 ms                                                  | 26.6 ms: 1.27x slower                                                   |
| chaos                      | 68.8 ms                                                  | 89.3 ms: 1.30x slower                                                   |
| scimark_lu                 | 139 ms                                                   | 183 ms: 1.31x slower                                                    |
| genshi_xml                 | 60.2 ms                                                  | 79.6 ms: 1.32x slower                                                   |
| sympy_sum                  | 143 ms                                                   | 192 ms: 1.34x slower                                                    |
| regex_compile              | 128 ms                                                   | 180 ms: 1.40x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.07x slower                                                            |

Benchmark hidden because not significant (13): xml_etree_process, xml_etree_generate, pidigits, nbody, deepcopy_reduce, regex_effbot, json_dumps, asyncio_websockets, regex_dna, logging_silent, async_generators, python_startup_no_site, async_tree_io_tg
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240708-3.14.0a0-006b53a-JIT/bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a.json: dulwich_log

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.09x