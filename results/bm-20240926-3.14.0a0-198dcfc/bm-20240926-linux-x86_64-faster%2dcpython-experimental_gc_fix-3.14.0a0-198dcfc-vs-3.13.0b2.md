# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: experimental_gc_fix
- machine: linux-x86_64
- commit hash: 198dcfc
- commit date: 2024-09-26
- overall geometric mean: 1.02x faster
- HPT reliability: 99.95%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 271 ms: 1.01x faster                                                           |
| docutils       | 2.83 sec                                                   | 2.70 sec: 1.05x faster                                                         |
| html5lib       | 67.2 ms                                                    | 68.1 ms: 1.01x slower                                                          |
| tornado_http   | 94.6 ms                                                    | 91.8 ms: 1.03x faster                                                          |
| Geometric mean | (ref)                                                      | 1.02x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc |
|----------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization     | 463 ms                                                     | 481 ms: 1.04x slower                                                           |
| async_tree_io              | 939 ms                                                     | 987 ms: 1.05x slower                                                           |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 644 ms: 1.05x slower                                                           |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 627 ms: 1.07x slower                                                           |
| async_tree_memoization_tg  | 444 ms                                                     | 498 ms: 1.12x slower                                                           |
| async_tree_none            | 378 ms                                                     | 424 ms: 1.12x slower                                                           |
| async_tree_none_tg         | 336 ms                                                     | 386 ms: 1.15x slower                                                           |
| Geometric mean             | (ref)                                                      | 1.08x slower                                                                   |

Benchmark hidden because not significant (1): async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 86.4 ms: 1.02x faster                                                          |
| pidigits       | 191 ms                                                     | 187 ms: 1.02x faster                                                           |
| float          | 78.9 ms                                                    | 95.9 ms: 1.22x slower                                                          |
| Geometric mean | (ref)                                                      | 1.05x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 128 ms: 1.07x faster                                                           |
| regex_effbot   | 3.67 ms                                                    | 3.64 ms: 1.01x faster                                                          |
| regex_dna      | 221 ms                                                     | 222 ms: 1.00x slower                                                           |
| Geometric mean | (ref)                                                      | 1.02x faster                                                                   |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc |
|----------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_loads           | 28.9 us                                                    | 27.2 us: 1.06x faster                                                          |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.04x faster                                                          |
| unpickle             | 15.1 us                                                    | 14.6 us: 1.03x faster                                                          |
| unpickle_pure_python | 218 us                                                     | 211 us: 1.03x faster                                                           |
| tomli_loads          | 2.12 sec                                                   | 2.07 sec: 1.03x faster                                                         |
| unpickle_list        | 5.34 us                                                    | 5.25 us: 1.02x faster                                                          |
| pickle_dict          | 34.8 us                                                    | 34.4 us: 1.01x faster                                                          |
| pickle_pure_python   | 305 us                                                     | 303 us: 1.01x faster                                                           |
| pickle_list          | 5.11 us                                                    | 5.13 us: 1.01x slower                                                          |
| pickle               | 11.5 us                                                    | 11.6 us: 1.01x slower                                                          |
| xml_etree_generate   | 87.4 ms                                                    | 91.0 ms: 1.04x slower                                                          |
| xml_etree_parse      | 162 ms                                                     | 171 ms: 1.06x slower                                                           |
| xml_etree_process    | 61.2 ms                                                    | 65.2 ms: 1.07x slower                                                          |
| xml_etree_iterparse  | 107 ms                                                     | 157 ms: 1.46x slower                                                           |
| Geometric mean       | (ref)                                                      | 1.02x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc |
|------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 7.11 ms                                                    | 7.01 ms: 1.01x faster                                                          |
| python_startup         | 10.8 ms                                                    | 10.7 ms: 1.01x faster                                                          |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc |
|-----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 22.1 ms: 1.07x faster                                                          |
| django_template | 34.8 ms                                                    | 34.2 ms: 1.02x faster                                                          |
| genshi_xml      | 51.6 ms                                                    | 54.5 ms: 1.06x slower                                                          |
| Geometric mean  | (ref)                                                      | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc |
|----------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 256 us: 1.44x faster                                                           |
| deepcopy_memo              | 39.7 us                                                    | 29.6 us: 1.34x faster                                                          |
| deepcopy_reduce            | 3.35 us                                                    | 2.65 us: 1.26x faster                                                          |
| go                         | 145 ms                                                     | 117 ms: 1.23x faster                                                           |
| gc_traversal               | 3.98 ms                                                    | 3.53 ms: 1.13x faster                                                          |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.74 ms: 1.11x faster                                                          |
| richards                   | 50.9 ms                                                    | 45.9 ms: 1.11x faster                                                          |
| richards_super             | 57.4 ms                                                    | 51.9 ms: 1.11x faster                                                          |
| mdp                        | 2.79 sec                                                   | 2.53 sec: 1.10x faster                                                         |
| scimark_fft                | 392 ms                                                     | 358 ms: 1.10x faster                                                           |
| coverage                   | 93.1 ms                                                    | 85.3 ms: 1.09x faster                                                          |
| crypto_pyaes               | 77.5 ms                                                    | 71.9 ms: 1.08x faster                                                          |
| pathlib                    | 17.3 ms                                                    | 16.1 ms: 1.07x faster                                                          |
| generators                 | 29.6 ms                                                    | 27.6 ms: 1.07x faster                                                          |
| genshi_text                | 23.7 ms                                                    | 22.1 ms: 1.07x faster                                                          |
| pprint_safe_repr           | 758 ms                                                     | 708 ms: 1.07x faster                                                           |
| pprint_pformat             | 1.56 sec                                                   | 1.45 sec: 1.07x faster                                                         |
| scimark_lu                 | 122 ms                                                     | 114 ms: 1.07x faster                                                           |
| regex_compile              | 137 ms                                                     | 128 ms: 1.07x faster                                                           |
| create_gc_cycles           | 1.82 ms                                                    | 1.71 ms: 1.06x faster                                                          |
| json_loads                 | 28.9 us                                                    | 27.2 us: 1.06x faster                                                          |
| sqlite_synth               | 2.99 us                                                    | 2.82 us: 1.06x faster                                                          |
| thrift                     | 823 us                                                     | 776 us: 1.06x faster                                                           |
| asyncio_tcp                | 508 ms                                                     | 480 ms: 1.06x faster                                                           |
| bench_thread_pool          | 834 us                                                     | 790 us: 1.06x faster                                                           |
| sympy_str                  | 282 ms                                                     | 268 ms: 1.05x faster                                                           |
| sympy_integrate            | 20.5 ms                                                    | 19.5 ms: 1.05x faster                                                          |
| sympy_sum                  | 156 ms                                                     | 148 ms: 1.05x faster                                                           |
| docutils                   | 2.83 sec                                                   | 2.70 sec: 1.05x faster                                                         |
| chaos                      | 61.3 ms                                                    | 58.5 ms: 1.05x faster                                                          |
| sympy_expand               | 473 ms                                                     | 453 ms: 1.04x faster                                                           |
| logging_format             | 6.47 us                                                    | 6.20 us: 1.04x faster                                                          |
| dulwich_log                | 67.2 ms                                                    | 64.5 ms: 1.04x faster                                                          |
| sqlglot_normalize          | 110 ms                                                     | 106 ms: 1.04x faster                                                           |
| spectral_norm              | 116 ms                                                     | 112 ms: 1.04x faster                                                           |
| logging_silent             | 105 ns                                                     | 101 ns: 1.04x faster                                                           |
| scimark_monte_carlo        | 69.2 ms                                                    | 66.8 ms: 1.04x faster                                                          |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.04x faster                                                          |
| scimark_sor                | 127 ms                                                     | 123 ms: 1.03x faster                                                           |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.78 sec: 1.03x faster                                                         |
| unpickle                   | 15.1 us                                                    | 14.6 us: 1.03x faster                                                          |
| typing_runtime_protocols   | 165 us                                                     | 160 us: 1.03x faster                                                           |
| unpickle_pure_python       | 218 us                                                     | 211 us: 1.03x faster                                                           |
| tornado_http               | 94.6 ms                                                    | 91.8 ms: 1.03x faster                                                          |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.03x faster                                                           |
| json                       | 5.31 ms                                                    | 5.17 ms: 1.03x faster                                                          |
| sqlglot_optimize           | 55.5 ms                                                    | 54.1 ms: 1.03x faster                                                          |
| tomli_loads                | 2.12 sec                                                   | 2.07 sec: 1.03x faster                                                         |
| pyflate                    | 484 ms                                                     | 472 ms: 1.03x faster                                                           |
| nqueens                    | 81.4 ms                                                    | 79.5 ms: 1.02x faster                                                          |
| logging_simple             | 5.74 us                                                    | 5.61 us: 1.02x faster                                                          |
| nbody                      | 88.3 ms                                                    | 86.4 ms: 1.02x faster                                                          |
| pidigits                   | 191 ms                                                     | 187 ms: 1.02x faster                                                           |
| raytrace                   | 267 ms                                                     | 261 ms: 1.02x faster                                                           |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                                           |
| hexiom                     | 6.30 ms                                                    | 6.18 ms: 1.02x faster                                                          |
| django_template            | 34.8 ms                                                    | 34.2 ms: 1.02x faster                                                          |
| unpickle_list              | 5.34 us                                                    | 5.25 us: 1.02x faster                                                          |
| python_startup_no_site     | 7.11 ms                                                    | 7.01 ms: 1.01x faster                                                          |
| telco                      | 8.41 ms                                                    | 8.30 ms: 1.01x faster                                                          |
| 2to3                       | 274 ms                                                     | 271 ms: 1.01x faster                                                           |
| sqlglot_transpile          | 1.63 ms                                                    | 1.62 ms: 1.01x faster                                                          |
| pickle_dict                | 34.8 us                                                    | 34.4 us: 1.01x faster                                                          |
| regex_effbot               | 3.67 ms                                                    | 3.64 ms: 1.01x faster                                                          |
| pickle_pure_python         | 305 us                                                     | 303 us: 1.01x faster                                                           |
| sqlglot_parse              | 1.32 ms                                                    | 1.31 ms: 1.01x faster                                                          |
| python_startup             | 10.8 ms                                                    | 10.7 ms: 1.01x faster                                                          |
| coroutines                 | 23.2 ms                                                    | 23.0 ms: 1.01x faster                                                          |
| comprehensions             | 16.6 us                                                    | 16.5 us: 1.00x faster                                                          |
| regex_dna                  | 221 ms                                                     | 222 ms: 1.00x slower                                                           |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                          |
| pickle_list                | 5.11 us                                                    | 5.13 us: 1.01x slower                                                          |
| fannkuch                   | 402 ms                                                     | 404 ms: 1.01x slower                                                           |
| pickle                     | 11.5 us                                                    | 11.6 us: 1.01x slower                                                          |
| deltablue                  | 3.25 ms                                                    | 3.29 ms: 1.01x slower                                                          |
| html5lib                   | 67.2 ms                                                    | 68.1 ms: 1.01x slower                                                          |
| async_generators           | 442 ms                                                     | 455 ms: 1.03x slower                                                           |
| async_tree_memoization     | 463 ms                                                     | 481 ms: 1.04x slower                                                           |
| xml_etree_generate         | 87.4 ms                                                    | 91.0 ms: 1.04x slower                                                          |
| pycparser                  | 1.16 sec                                                   | 1.22 sec: 1.05x slower                                                         |
| async_tree_io              | 939 ms                                                     | 987 ms: 1.05x slower                                                           |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 644 ms: 1.05x slower                                                           |
| genshi_xml                 | 51.6 ms                                                    | 54.5 ms: 1.06x slower                                                          |
| xml_etree_parse            | 162 ms                                                     | 171 ms: 1.06x slower                                                           |
| xml_etree_process          | 61.2 ms                                                    | 65.2 ms: 1.07x slower                                                          |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 627 ms: 1.07x slower                                                           |
| async_tree_memoization_tg  | 444 ms                                                     | 498 ms: 1.12x slower                                                           |
| async_tree_none            | 378 ms                                                     | 424 ms: 1.12x slower                                                           |
| bpe_tokeniser              | 5.02 sec                                                   | 5.76 sec: 1.15x slower                                                         |
| async_tree_none_tg         | 336 ms                                                     | 386 ms: 1.15x slower                                                           |
| float                      | 78.9 ms                                                    | 95.9 ms: 1.22x slower                                                          |
| xml_etree_iterparse        | 107 ms                                                     | 157 ms: 1.46x slower                                                           |
| Geometric mean             | (ref)                                                      | 1.02x faster                                                                   |

Benchmark hidden because not significant (4): mako, regex_v8, pylint, async_tree_io_tg
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240926-3.14.0a0-198dcfc/bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc.json: unpack_sequence

# HPT report

- Reliability score: 99.95% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x