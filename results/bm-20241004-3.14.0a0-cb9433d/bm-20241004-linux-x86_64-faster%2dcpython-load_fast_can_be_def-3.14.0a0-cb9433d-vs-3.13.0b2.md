# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: load_fast_can_be_def
- machine: linux-x86_64
- commit hash: cb9433d
- commit date: 2024-10-04
- overall geometric mean: 1.04x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 257 ms: 1.07x faster                                                            |
| docutils       | 2.83 sec                                                   | 2.64 sec: 1.07x faster                                                          |
| html5lib       | 67.2 ms                                                    | 62.2 ms: 1.08x faster                                                           |
| tornado_http   | 94.6 ms                                                    | 91.7 ms: 1.03x faster                                                           |
| Geometric mean | (ref)                                                      | 1.06x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 312 ms: 1.21x faster                                                            |
| async_tree_memoization     | 463 ms                                                     | 392 ms: 1.18x faster                                                            |
| async_tree_memoization_tg  | 444 ms                                                     | 386 ms: 1.15x faster                                                            |
| async_tree_none_tg         | 336 ms                                                     | 304 ms: 1.11x faster                                                            |
| async_tree_io_tg           | 936 ms                                                     | 859 ms: 1.09x faster                                                            |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 562 ms: 1.09x faster                                                            |
| async_tree_io              | 939 ms                                                     | 874 ms: 1.07x faster                                                            |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 550 ms: 1.07x faster                                                            |
| Geometric mean             | (ref)                                                      | 1.12x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 77.1 ms: 1.02x faster                                                           |
| pidigits       | 191 ms                                                     | 187 ms: 1.02x faster                                                            |
| nbody          | 88.3 ms                                                    | 88.0 ms: 1.00x faster                                                           |
| Geometric mean | (ref)                                                      | 1.02x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 131 ms: 1.04x faster                                                            |
| regex_v8       | 25.1 ms                                                    | 25.3 ms: 1.01x slower                                                           |
| regex_dna      | 221 ms                                                     | 223 ms: 1.01x slower                                                            |
| regex_effbot   | 3.67 ms                                                    | 3.75 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                      | 1.00x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_loads           | 28.9 us                                                    | 27.1 us: 1.07x faster                                                           |
| json_dumps           | 10.7 ms                                                    | 10.2 ms: 1.06x faster                                                           |
| xml_etree_parse      | 162 ms                                                     | 155 ms: 1.04x faster                                                            |
| xml_etree_process    | 61.2 ms                                                    | 59.3 ms: 1.03x faster                                                           |
| unpickle             | 15.1 us                                                    | 14.7 us: 1.03x faster                                                           |
| xml_etree_iterparse  | 107 ms                                                     | 104 ms: 1.03x faster                                                            |
| pickle_dict          | 34.8 us                                                    | 34.1 us: 1.02x faster                                                           |
| xml_etree_generate   | 87.4 ms                                                    | 86.3 ms: 1.01x faster                                                           |
| unpickle_pure_python | 218 us                                                     | 216 us: 1.01x faster                                                            |
| tomli_loads          | 2.12 sec                                                   | 2.10 sec: 1.01x faster                                                          |
| pickle_list          | 5.11 us                                                    | 5.06 us: 1.01x faster                                                           |
| pickle_pure_python   | 305 us                                                     | 308 us: 1.01x slower                                                            |
| pickle               | 11.5 us                                                    | 11.7 us: 1.02x slower                                                           |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                                    |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                           |
| python_startup_no_site | 7.11 ms                                                    | 6.99 ms: 1.02x faster                                                           |
| Geometric mean         | (ref)                                                      | 1.02x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 22.7 ms: 1.04x faster                                                           |
| genshi_xml      | 51.6 ms                                                    | 50.5 ms: 1.02x faster                                                           |
| django_template | 34.8 ms                                                    | 34.5 ms: 1.01x faster                                                           |
| mako            | 11.2 ms                                                    | 11.3 ms: 1.01x slower                                                           |
| Geometric mean  | (ref)                                                      | 1.02x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 262 us: 1.40x faster                                                            |
| deepcopy_memo              | 39.7 us                                                    | 30.3 us: 1.31x faster                                                           |
| deepcopy_reduce            | 3.35 us                                                    | 2.75 us: 1.22x faster                                                           |
| async_tree_none            | 378 ms                                                     | 312 ms: 1.21x faster                                                            |
| go                         | 145 ms                                                     | 120 ms: 1.21x faster                                                            |
| async_tree_memoization     | 463 ms                                                     | 392 ms: 1.18x faster                                                            |
| async_tree_memoization_tg  | 444 ms                                                     | 386 ms: 1.15x faster                                                            |
| mdp                        | 2.79 sec                                                   | 2.51 sec: 1.11x faster                                                          |
| async_tree_none_tg         | 336 ms                                                     | 304 ms: 1.11x faster                                                            |
| pathlib                    | 17.3 ms                                                    | 15.9 ms: 1.09x faster                                                           |
| async_tree_io_tg           | 936 ms                                                     | 859 ms: 1.09x faster                                                            |
| coverage                   | 93.1 ms                                                    | 85.6 ms: 1.09x faster                                                           |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 562 ms: 1.09x faster                                                            |
| richards                   | 50.9 ms                                                    | 46.9 ms: 1.09x faster                                                           |
| asyncio_tcp                | 508 ms                                                     | 469 ms: 1.08x faster                                                            |
| html5lib                   | 67.2 ms                                                    | 62.2 ms: 1.08x faster                                                           |
| thrift                     | 823 us                                                     | 763 us: 1.08x faster                                                            |
| richards_super             | 57.4 ms                                                    | 53.2 ms: 1.08x faster                                                           |
| async_tree_io              | 939 ms                                                     | 874 ms: 1.07x faster                                                            |
| crypto_pyaes               | 77.5 ms                                                    | 72.3 ms: 1.07x faster                                                           |
| scimark_lu                 | 122 ms                                                     | 114 ms: 1.07x faster                                                            |
| gc_traversal               | 3.98 ms                                                    | 3.72 ms: 1.07x faster                                                           |
| docutils                   | 2.83 sec                                                   | 2.64 sec: 1.07x faster                                                          |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 550 ms: 1.07x faster                                                            |
| sqlite_synth               | 2.99 us                                                    | 2.80 us: 1.07x faster                                                           |
| json_loads                 | 28.9 us                                                    | 27.1 us: 1.07x faster                                                           |
| generators                 | 29.6 ms                                                    | 27.8 ms: 1.07x faster                                                           |
| scimark_fft                | 392 ms                                                     | 368 ms: 1.07x faster                                                            |
| 2to3                       | 274 ms                                                     | 257 ms: 1.07x faster                                                            |
| create_gc_cycles           | 1.82 ms                                                    | 1.71 ms: 1.06x faster                                                           |
| pprint_safe_repr           | 758 ms                                                     | 716 ms: 1.06x faster                                                            |
| json_dumps                 | 10.7 ms                                                    | 10.2 ms: 1.06x faster                                                           |
| pprint_pformat             | 1.56 sec                                                   | 1.48 sec: 1.05x faster                                                          |
| telco                      | 8.41 ms                                                    | 8.00 ms: 1.05x faster                                                           |
| sympy_sum                  | 156 ms                                                     | 148 ms: 1.05x faster                                                            |
| genshi_text                | 23.7 ms                                                    | 22.7 ms: 1.04x faster                                                           |
| xml_etree_parse            | 162 ms                                                     | 155 ms: 1.04x faster                                                            |
| regex_compile              | 137 ms                                                     | 131 ms: 1.04x faster                                                            |
| sympy_str                  | 282 ms                                                     | 271 ms: 1.04x faster                                                            |
| bpe_tokeniser              | 5.02 sec                                                   | 4.83 sec: 1.04x faster                                                          |
| json                       | 5.31 ms                                                    | 5.11 ms: 1.04x faster                                                           |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.77 sec: 1.04x faster                                                          |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 5.08 ms: 1.04x faster                                                           |
| coroutines                 | 23.2 ms                                                    | 22.4 ms: 1.04x faster                                                           |
| sqlglot_optimize           | 55.5 ms                                                    | 53.6 ms: 1.04x faster                                                           |
| sqlglot_transpile          | 1.63 ms                                                    | 1.58 ms: 1.03x faster                                                           |
| tornado_http               | 94.6 ms                                                    | 91.7 ms: 1.03x faster                                                           |
| xml_etree_process          | 61.2 ms                                                    | 59.3 ms: 1.03x faster                                                           |
| sqlglot_parse              | 1.32 ms                                                    | 1.28 ms: 1.03x faster                                                           |
| unpickle                   | 15.1 us                                                    | 14.7 us: 1.03x faster                                                           |
| xml_etree_iterparse        | 107 ms                                                     | 104 ms: 1.03x faster                                                            |
| sympy_expand               | 473 ms                                                     | 460 ms: 1.03x faster                                                            |
| logging_format             | 6.47 us                                                    | 6.30 us: 1.03x faster                                                           |
| sympy_integrate            | 20.5 ms                                                    | 20.0 ms: 1.03x faster                                                           |
| dulwich_log                | 67.2 ms                                                    | 65.5 ms: 1.03x faster                                                           |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                           |
| float                      | 78.9 ms                                                    | 77.1 ms: 1.02x faster                                                           |
| genshi_xml                 | 51.6 ms                                                    | 50.5 ms: 1.02x faster                                                           |
| sqlglot_normalize          | 110 ms                                                     | 108 ms: 1.02x faster                                                            |
| pidigits                   | 191 ms                                                     | 187 ms: 1.02x faster                                                            |
| async_generators           | 442 ms                                                     | 433 ms: 1.02x faster                                                            |
| pickle_dict                | 34.8 us                                                    | 34.1 us: 1.02x faster                                                           |
| asyncio_websockets         | 567 ms                                                     | 557 ms: 1.02x faster                                                            |
| python_startup_no_site     | 7.11 ms                                                    | 6.99 ms: 1.02x faster                                                           |
| pyflate                    | 484 ms                                                     | 477 ms: 1.02x faster                                                            |
| scimark_monte_carlo        | 69.2 ms                                                    | 68.3 ms: 1.01x faster                                                           |
| xml_etree_generate         | 87.4 ms                                                    | 86.3 ms: 1.01x faster                                                           |
| spectral_norm              | 116 ms                                                     | 115 ms: 1.01x faster                                                            |
| unpickle_pure_python       | 218 us                                                     | 216 us: 1.01x faster                                                            |
| tomli_loads                | 2.12 sec                                                   | 2.10 sec: 1.01x faster                                                          |
| django_template            | 34.8 ms                                                    | 34.5 ms: 1.01x faster                                                           |
| logging_simple             | 5.74 us                                                    | 5.69 us: 1.01x faster                                                           |
| typing_runtime_protocols   | 165 us                                                     | 163 us: 1.01x faster                                                            |
| logging_silent             | 105 ns                                                     | 104 ns: 1.01x faster                                                            |
| pickle_list                | 5.11 us                                                    | 5.06 us: 1.01x faster                                                           |
| nbody                      | 88.3 ms                                                    | 88.0 ms: 1.00x faster                                                           |
| scimark_sor                | 127 ms                                                     | 127 ms: 1.00x faster                                                            |
| raytrace                   | 267 ms                                                     | 267 ms: 1.00x slower                                                            |
| fannkuch                   | 402 ms                                                     | 403 ms: 1.00x slower                                                            |
| chaos                      | 61.3 ms                                                    | 61.7 ms: 1.01x slower                                                           |
| regex_v8                   | 25.1 ms                                                    | 25.3 ms: 1.01x slower                                                           |
| regex_dna                  | 221 ms                                                     | 223 ms: 1.01x slower                                                            |
| deltablue                  | 3.25 ms                                                    | 3.28 ms: 1.01x slower                                                           |
| mako                       | 11.2 ms                                                    | 11.3 ms: 1.01x slower                                                           |
| pickle_pure_python         | 305 us                                                     | 308 us: 1.01x slower                                                            |
| bench_thread_pool          | 834 us                                                     | 850 us: 1.02x slower                                                            |
| regex_effbot               | 3.67 ms                                                    | 3.75 ms: 1.02x slower                                                           |
| pickle                     | 11.5 us                                                    | 11.7 us: 1.02x slower                                                           |
| bench_mp_pool              | 23.9 ms                                                    | 56.1 ms: 2.35x slower                                                           |
| Geometric mean             | (ref)                                                      | 1.04x faster                                                                    |

Benchmark hidden because not significant (7): unpickle_list, pycparser, hexiom, comprehensions, nqueens, pylint, meteor_contest
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241004-3.14.0a0-cb9433d/bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.00x