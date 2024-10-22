# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a3
- machine: linux-aarch64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.00x slower
- HPT reliability: 82.20%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.95x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-arminc-aarch64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| html5lib       | 64.3 ms                                                  | 66.2 ms: 1.03x slower                                        |
| tornado_http   | 131 ms                                                   | 137 ms: 1.04x slower                                         |
| Geometric mean | (ref)                                                    | 1.01x slower                                                 |

Benchmark hidden because not significant (3): 2to3, chameleon, docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-arminc-aarch64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| async_generators           | 496 ms                                                   | 480 ms: 1.03x faster                                         |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.22 sec: 1.02x slower                                       |
| coroutines                 | 28.2 ms                                                  | 29.4 ms: 1.04x slower                                        |
| async_tree_memoization_tg  | 649 ms                                                   | 736 ms: 1.13x slower                                         |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 888 ms: 1.16x slower                                         |
| async_tree_none            | 493 ms                                                   | 582 ms: 1.18x slower                                         |
| async_tree_memoization     | 626 ms                                                   | 745 ms: 1.19x slower                                         |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 895 ms: 1.22x slower                                         |
| async_tree_none_tg         | 467 ms                                                   | 574 ms: 1.23x slower                                         |
| async_tree_io              | 1.11 sec                                                 | 1.45 sec: 1.31x slower                                       |
| async_tree_io_tg           | 1.09 sec                                                 | 1.44 sec: 1.32x slower                                       |
| Geometric mean             | (ref)                                                    | 1.13x slower                                                 |

Benchmark hidden because not significant (2): asyncio_tcp, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-arminc-aarch64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 104 ms: 1.10x faster                                         |
| float          | 94.4 ms                                                  | 91.0 ms: 1.04x faster                                        |
| Geometric mean | (ref)                                                    | 1.05x faster                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-arminc-aarch64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| regex_effbot   | 4.87 ms                                                  | 4.65 ms: 1.05x faster                                        |
| regex_v8       | 31.5 ms                                                  | 30.1 ms: 1.05x faster                                        |
| regex_compile  | 128 ms                                                   | 125 ms: 1.03x faster                                         |
| regex_dna      | 246 ms                                                   | 255 ms: 1.04x slower                                         |
| Geometric mean | (ref)                                                    | 1.02x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-arminc-aarch64-python-v3.13.0a3-3.13.0a3-f009305 |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| json_dumps          | 13.4 ms                                                  | 12.5 ms: 1.07x faster                                        |
| pickle_pure_python  | 359 us                                                   | 347 us: 1.03x faster                                         |
| unpickle_list       | 6.65 us                                                  | 6.45 us: 1.03x faster                                        |
| unpickle            | 20.2 us                                                  | 19.6 us: 1.03x faster                                        |
| pickle_dict         | 38.1 us                                                  | 37.3 us: 1.02x faster                                        |
| json_loads          | 31.4 us                                                  | 31.1 us: 1.01x faster                                        |
| pickle_list         | 5.34 us                                                  | 5.28 us: 1.01x faster                                        |
| tomli_loads         | 2.53 sec                                                 | 2.59 sec: 1.03x slower                                       |
| xml_etree_iterparse | 147 ms                                                   | 152 ms: 1.04x slower                                         |
| xml_etree_parse     | 188 ms                                                   | 206 ms: 1.10x slower                                         |
| Geometric mean      | (ref)                                                    | 1.00x faster                                                 |

Benchmark hidden because not significant (4): pickle, xml_etree_process, unpickle_pure_python, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-arminc-aarch64-python-v3.13.0a3-3.13.0a3-f009305 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                  | 12.1 ms: 1.10x faster                                        |
| python_startup_no_site | 8.75 ms                                                  | 10.3 ms: 1.18x slower                                        |
| Geometric mean         | (ref)                                                    | 1.03x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-arminc-aarch64-python-v3.13.0a3-3.13.0a3-f009305 |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 42.3 ms                                                  | 40.7 ms: 1.04x faster                                        |
| mako            | 13.3 ms                                                  | 12.9 ms: 1.03x faster                                        |
| genshi_text     | 27.7 ms                                                  | 27.3 ms: 1.01x faster                                        |
| genshi_xml      | 60.2 ms                                                  | 60.8 ms: 1.01x slower                                        |
| Geometric mean  | (ref)                                                    | 1.02x faster                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-arminc-aarch64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols   | 192 us                                                   | 135 us: 1.42x faster                                         |
| mypy2                      | 1.18 sec                                                 | 899 ms: 1.32x faster                                         |
| create_gc_cycles           | 2.12 ms                                                  | 1.91 ms: 1.11x faster                                        |
| python_startup             | 13.3 ms                                                  | 12.1 ms: 1.10x faster                                        |
| nbody                      | 114 ms                                                   | 104 ms: 1.10x faster                                         |
| spectral_norm              | 141 ms                                                   | 129 ms: 1.09x faster                                         |
| json_dumps                 | 13.4 ms                                                  | 12.5 ms: 1.07x faster                                        |
| crypto_pyaes               | 82.7 ms                                                  | 77.3 ms: 1.07x faster                                        |
| generators                 | 37.8 ms                                                  | 36.0 ms: 1.05x faster                                        |
| regex_effbot               | 4.87 ms                                                  | 4.65 ms: 1.05x faster                                        |
| regex_v8                   | 31.5 ms                                                  | 30.1 ms: 1.05x faster                                        |
| bench_mp_pool              | 7.30 ms                                                  | 6.98 ms: 1.05x faster                                        |
| sqlglot_normalize          | 128 ms                                                   | 123 ms: 1.04x faster                                         |
| scimark_fft                | 447 ms                                                   | 430 ms: 1.04x faster                                         |
| gc_traversal               | 4.53 ms                                                  | 4.36 ms: 1.04x faster                                        |
| django_template            | 42.3 ms                                                  | 40.7 ms: 1.04x faster                                        |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 6.34 ms: 1.04x faster                                        |
| float                      | 94.4 ms                                                  | 91.0 ms: 1.04x faster                                        |
| pickle_pure_python         | 359 us                                                   | 347 us: 1.03x faster                                         |
| deepcopy_memo              | 51.0 us                                                  | 49.3 us: 1.03x faster                                        |
| async_generators           | 496 ms                                                   | 480 ms: 1.03x faster                                         |
| mako                       | 13.3 ms                                                  | 12.9 ms: 1.03x faster                                        |
| chaos                      | 68.8 ms                                                  | 66.7 ms: 1.03x faster                                        |
| comprehensions             | 20.4 us                                                  | 19.8 us: 1.03x faster                                        |
| sympy_sum                  | 143 ms                                                   | 139 ms: 1.03x faster                                         |
| unpickle_list              | 6.65 us                                                  | 6.45 us: 1.03x faster                                        |
| unpickle                   | 20.2 us                                                  | 19.6 us: 1.03x faster                                        |
| regex_compile              | 128 ms                                                   | 125 ms: 1.03x faster                                         |
| sqlglot_optimize           | 62.4 ms                                                  | 60.7 ms: 1.03x faster                                        |
| sympy_integrate            | 21.0 ms                                                  | 20.5 ms: 1.03x faster                                        |
| sqlite_synth               | 3.84 us                                                  | 3.75 us: 1.02x faster                                        |
| nqueens                    | 98.7 ms                                                  | 96.4 ms: 1.02x faster                                        |
| thrift                     | 946 us                                                   | 925 us: 1.02x faster                                         |
| pickle_dict                | 38.1 us                                                  | 37.3 us: 1.02x faster                                        |
| scimark_lu                 | 139 ms                                                   | 137 ms: 1.02x faster                                         |
| sympy_str                  | 264 ms                                                   | 259 ms: 1.02x faster                                         |
| deepcopy                   | 451 us                                                   | 444 us: 1.02x faster                                         |
| sympy_expand               | 455 ms                                                   | 448 ms: 1.02x faster                                         |
| genshi_text                | 27.7 ms                                                  | 27.3 ms: 1.01x faster                                        |
| mdp                        | 3.36 sec                                                 | 3.32 sec: 1.01x faster                                       |
| sqlglot_parse              | 1.38 ms                                                  | 1.36 ms: 1.01x faster                                        |
| json_loads                 | 31.4 us                                                  | 31.1 us: 1.01x faster                                        |
| pickle_list                | 5.34 us                                                  | 5.28 us: 1.01x faster                                        |
| deepcopy_reduce            | 4.07 us                                                  | 4.04 us: 1.01x faster                                        |
| fannkuch                   | 452 ms                                                   | 456 ms: 1.01x slower                                         |
| pprint_pformat             | 1.90 sec                                                 | 1.91 sec: 1.01x slower                                       |
| pyflate                    | 556 ms                                                   | 562 ms: 1.01x slower                                         |
| pprint_safe_repr           | 926 ms                                                   | 936 ms: 1.01x slower                                         |
| genshi_xml                 | 60.2 ms                                                  | 60.8 ms: 1.01x slower                                        |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.22 sec: 1.02x slower                                       |
| logging_format             | 7.83 us                                                  | 8.00 us: 1.02x slower                                        |
| scimark_sor                | 159 ms                                                   | 163 ms: 1.02x slower                                         |
| bench_thread_pool          | 1.28 ms                                                  | 1.31 ms: 1.02x slower                                        |
| tomli_loads                | 2.53 sec                                                 | 2.59 sec: 1.03x slower                                       |
| richards                   | 53.5 ms                                                  | 55.0 ms: 1.03x slower                                        |
| html5lib                   | 64.3 ms                                                  | 66.2 ms: 1.03x slower                                        |
| logging_simple             | 7.04 us                                                  | 7.26 us: 1.03x slower                                        |
| deltablue                  | 3.85 ms                                                  | 3.98 ms: 1.03x slower                                        |
| xml_etree_iterparse        | 147 ms                                                   | 152 ms: 1.04x slower                                         |
| coverage                   | 98.5 ms                                                  | 102 ms: 1.04x slower                                         |
| regex_dna                  | 246 ms                                                   | 255 ms: 1.04x slower                                         |
| coroutines                 | 28.2 ms                                                  | 29.4 ms: 1.04x slower                                        |
| tornado_http               | 131 ms                                                   | 137 ms: 1.04x slower                                         |
| pathlib                    | 22.4 ms                                                  | 24.1 ms: 1.08x slower                                        |
| xml_etree_parse            | 188 ms                                                   | 206 ms: 1.10x slower                                         |
| async_tree_memoization_tg  | 649 ms                                                   | 736 ms: 1.13x slower                                         |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 888 ms: 1.16x slower                                         |
| python_startup_no_site     | 8.75 ms                                                  | 10.3 ms: 1.18x slower                                        |
| async_tree_none            | 493 ms                                                   | 582 ms: 1.18x slower                                         |
| async_tree_memoization     | 626 ms                                                   | 745 ms: 1.19x slower                                         |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 895 ms: 1.22x slower                                         |
| async_tree_none_tg         | 467 ms                                                   | 574 ms: 1.23x slower                                         |
| async_tree_io              | 1.11 sec                                                 | 1.45 sec: 1.31x slower                                       |
| async_tree_io_tg           | 1.09 sec                                                 | 1.44 sec: 1.32x slower                                       |
| Geometric mean             | (ref)                                                    | 1.00x slower                                                 |

Benchmark hidden because not significant (25): pylint, aiohttp, asyncio_tcp, sqlglot_transpile, flaskblogging, go, gunicorn, raytrace, logging_silent, pickle, pidigits, chameleon, telco, json, scimark_monte_carlo, 2to3, docutils, meteor_contest, hexiom, xml_etree_process, asyncio_websockets, unpickle_pure_python, pycparser, xml_etree_generate, richards_super
Ignored benchmarks (3) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, dask, unpack_sequence
Ignored benchmarks (1) of results/bm-20240117-3.13.0a3-f009305/bm-20240117-arminc-aarch64-python-v3.13.0a3-3.13.0a3-f009305.json: dulwich_log

# HPT report

- Reliability score: 82.20% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.95x