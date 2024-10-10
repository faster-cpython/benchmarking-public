# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: refactor_refcnt_mort
- machine: linux-x86_64
- commit hash: 2fbc12f
- commit date: 2024-10-10
- overall geometric mean: 1.02x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 256 ms: 1.07x faster                                                            |
| docutils       | 2.83 sec                                                   | 2.65 sec: 1.07x faster                                                          |
| html5lib       | 67.2 ms                                                    | 62.6 ms: 1.07x faster                                                           |
| tornado_http   | 94.6 ms                                                    | 91.3 ms: 1.04x faster                                                           |
| Geometric mean | (ref)                                                      | 1.06x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 327 ms: 1.16x faster                                                            |
| async_tree_memoization     | 463 ms                                                     | 408 ms: 1.14x faster                                                            |
| async_tree_memoization_tg  | 444 ms                                                     | 405 ms: 1.10x faster                                                            |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 561 ms: 1.09x faster                                                            |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 541 ms: 1.08x faster                                                            |
| async_tree_none_tg         | 336 ms                                                     | 311 ms: 1.08x faster                                                            |
| Geometric mean             | (ref)                                                      | 1.08x faster                                                                    |

Benchmark hidden because not significant (2): async_tree_io_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 189 ms: 1.01x faster                                                            |
| nbody          | 88.3 ms                                                    | 93.0 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                      | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 130 ms: 1.05x faster                                                            |
| regex_effbot   | 3.67 ms                                                    | 3.57 ms: 1.03x faster                                                           |
| regex_v8       | 25.1 ms                                                    | 24.4 ms: 1.03x faster                                                           |
| regex_dna      | 221 ms                                                     | 217 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                      | 1.03x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_loads           | 28.9 us                                                    | 26.7 us: 1.08x faster                                                           |
| xml_etree_parse      | 162 ms                                                     | 156 ms: 1.04x faster                                                            |
| pickle_dict          | 34.8 us                                                    | 34.0 us: 1.02x faster                                                           |
| pickle_list          | 5.11 us                                                    | 5.01 us: 1.02x faster                                                           |
| xml_etree_iterparse  | 107 ms                                                     | 105 ms: 1.02x faster                                                            |
| xml_etree_process    | 61.2 ms                                                    | 60.7 ms: 1.01x faster                                                           |
| xml_etree_generate   | 87.4 ms                                                    | 87.8 ms: 1.00x slower                                                           |
| unpickle_list        | 5.34 us                                                    | 5.38 us: 1.01x slower                                                           |
| pickle               | 11.5 us                                                    | 11.7 us: 1.02x slower                                                           |
| tomli_loads          | 2.12 sec                                                   | 2.17 sec: 1.03x slower                                                          |
| unpickle_pure_python | 218 us                                                     | 224 us: 1.03x slower                                                            |
| pickle_pure_python   | 305 us                                                     | 315 us: 1.03x slower                                                            |
| json_dumps           | 10.7 ms                                                    | 11.6 ms: 1.09x slower                                                           |
| Geometric mean       | (ref)                                                      | 1.00x slower                                                                    |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.01x faster                                                           |
| python_startup_no_site | 7.11 ms                                                    | 7.06 ms: 1.01x faster                                                           |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 23.5 ms: 1.01x faster                                                           |
| django_template | 34.8 ms                                                    | 35.0 ms: 1.01x slower                                                           |
| mako            | 11.2 ms                                                    | 11.6 ms: 1.04x slower                                                           |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 268 us: 1.37x faster                                                            |
| deepcopy_memo              | 39.7 us                                                    | 32.2 us: 1.24x faster                                                           |
| deepcopy_reduce            | 3.35 us                                                    | 2.76 us: 1.21x faster                                                           |
| go                         | 145 ms                                                     | 123 ms: 1.18x faster                                                            |
| async_tree_none            | 378 ms                                                     | 327 ms: 1.16x faster                                                            |
| async_tree_memoization     | 463 ms                                                     | 408 ms: 1.14x faster                                                            |
| mdp                        | 2.79 sec                                                   | 2.52 sec: 1.11x faster                                                          |
| async_tree_memoization_tg  | 444 ms                                                     | 405 ms: 1.10x faster                                                            |
| json                       | 5.31 ms                                                    | 4.85 ms: 1.10x faster                                                           |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 561 ms: 1.09x faster                                                            |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 541 ms: 1.08x faster                                                            |
| async_tree_none_tg         | 336 ms                                                     | 311 ms: 1.08x faster                                                            |
| json_loads                 | 28.9 us                                                    | 26.7 us: 1.08x faster                                                           |
| richards                   | 50.9 ms                                                    | 47.1 ms: 1.08x faster                                                           |
| pathlib                    | 17.3 ms                                                    | 16.1 ms: 1.08x faster                                                           |
| richards_super             | 57.4 ms                                                    | 53.3 ms: 1.08x faster                                                           |
| crypto_pyaes               | 77.5 ms                                                    | 72.1 ms: 1.07x faster                                                           |
| html5lib                   | 67.2 ms                                                    | 62.6 ms: 1.07x faster                                                           |
| 2to3                       | 274 ms                                                     | 256 ms: 1.07x faster                                                            |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.93 ms: 1.07x faster                                                           |
| docutils                   | 2.83 sec                                                   | 2.65 sec: 1.07x faster                                                          |
| asyncio_tcp                | 508 ms                                                     | 479 ms: 1.06x faster                                                            |
| regex_compile              | 137 ms                                                     | 130 ms: 1.05x faster                                                            |
| scimark_fft                | 392 ms                                                     | 373 ms: 1.05x faster                                                            |
| thrift                     | 823 us                                                     | 783 us: 1.05x faster                                                            |
| telco                      | 8.41 ms                                                    | 8.02 ms: 1.05x faster                                                           |
| generators                 | 29.6 ms                                                    | 28.2 ms: 1.05x faster                                                           |
| bpe_tokeniser              | 5.02 sec                                                   | 4.79 sec: 1.05x faster                                                          |
| sqlite_synth               | 2.99 us                                                    | 2.86 us: 1.05x faster                                                           |
| sympy_sum                  | 156 ms                                                     | 149 ms: 1.04x faster                                                            |
| sympy_str                  | 282 ms                                                     | 272 ms: 1.04x faster                                                            |
| tornado_http               | 94.6 ms                                                    | 91.3 ms: 1.04x faster                                                           |
| xml_etree_parse            | 162 ms                                                     | 156 ms: 1.04x faster                                                            |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.79 sec: 1.03x faster                                                          |
| pprint_safe_repr           | 758 ms                                                     | 736 ms: 1.03x faster                                                            |
| regex_effbot               | 3.67 ms                                                    | 3.57 ms: 1.03x faster                                                           |
| regex_v8                   | 25.1 ms                                                    | 24.4 ms: 1.03x faster                                                           |
| dulwich_log                | 67.2 ms                                                    | 65.4 ms: 1.03x faster                                                           |
| pprint_pformat             | 1.56 sec                                                   | 1.52 sec: 1.03x faster                                                          |
| scimark_lu                 | 122 ms                                                     | 119 ms: 1.02x faster                                                            |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.02x faster                                                            |
| pickle_dict                | 34.8 us                                                    | 34.0 us: 1.02x faster                                                           |
| regex_dna                  | 221 ms                                                     | 217 ms: 1.02x faster                                                            |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                                            |
| create_gc_cycles           | 1.82 ms                                                    | 1.78 ms: 1.02x faster                                                           |
| sympy_expand               | 473 ms                                                     | 463 ms: 1.02x faster                                                            |
| pickle_list                | 5.11 us                                                    | 5.01 us: 1.02x faster                                                           |
| logging_format             | 6.47 us                                                    | 6.35 us: 1.02x faster                                                           |
| sympy_integrate            | 20.5 ms                                                    | 20.1 ms: 1.02x faster                                                           |
| xml_etree_iterparse        | 107 ms                                                     | 105 ms: 1.02x faster                                                            |
| sqlglot_optimize           | 55.5 ms                                                    | 54.5 ms: 1.02x faster                                                           |
| pidigits                   | 191 ms                                                     | 189 ms: 1.01x faster                                                            |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.01x faster                                                           |
| coverage                   | 93.1 ms                                                    | 91.8 ms: 1.01x faster                                                           |
| nqueens                    | 81.4 ms                                                    | 80.3 ms: 1.01x faster                                                           |
| sqlglot_transpile          | 1.63 ms                                                    | 1.61 ms: 1.01x faster                                                           |
| logging_simple             | 5.74 us                                                    | 5.69 us: 1.01x faster                                                           |
| typing_runtime_protocols   | 165 us                                                     | 163 us: 1.01x faster                                                            |
| async_generators           | 442 ms                                                     | 438 ms: 1.01x faster                                                            |
| xml_etree_process          | 61.2 ms                                                    | 60.7 ms: 1.01x faster                                                           |
| python_startup_no_site     | 7.11 ms                                                    | 7.06 ms: 1.01x faster                                                           |
| sqlglot_parse              | 1.32 ms                                                    | 1.31 ms: 1.01x faster                                                           |
| genshi_text                | 23.7 ms                                                    | 23.5 ms: 1.01x faster                                                           |
| sqlglot_normalize          | 110 ms                                                     | 110 ms: 1.00x faster                                                            |
| xml_etree_generate         | 87.4 ms                                                    | 87.8 ms: 1.00x slower                                                           |
| django_template            | 34.8 ms                                                    | 35.0 ms: 1.01x slower                                                           |
| unpickle_list              | 5.34 us                                                    | 5.38 us: 1.01x slower                                                           |
| spectral_norm              | 116 ms                                                     | 117 ms: 1.01x slower                                                            |
| scimark_sor                | 127 ms                                                     | 129 ms: 1.01x slower                                                            |
| hexiom                     | 6.30 ms                                                    | 6.39 ms: 1.02x slower                                                           |
| pickle                     | 11.5 us                                                    | 11.7 us: 1.02x slower                                                           |
| bench_thread_pool          | 834 us                                                     | 850 us: 1.02x slower                                                            |
| comprehensions             | 16.6 us                                                    | 17.0 us: 1.02x slower                                                           |
| pycparser                  | 1.16 sec                                                   | 1.19 sec: 1.03x slower                                                          |
| tomli_loads                | 2.12 sec                                                   | 2.17 sec: 1.03x slower                                                          |
| unpickle_pure_python       | 218 us                                                     | 224 us: 1.03x slower                                                            |
| fannkuch                   | 402 ms                                                     | 413 ms: 1.03x slower                                                            |
| raytrace                   | 267 ms                                                     | 275 ms: 1.03x slower                                                            |
| pickle_pure_python         | 305 us                                                     | 315 us: 1.03x slower                                                            |
| deltablue                  | 3.25 ms                                                    | 3.36 ms: 1.03x slower                                                           |
| mako                       | 11.2 ms                                                    | 11.6 ms: 1.04x slower                                                           |
| coroutines                 | 23.2 ms                                                    | 24.2 ms: 1.04x slower                                                           |
| nbody                      | 88.3 ms                                                    | 93.0 ms: 1.05x slower                                                           |
| json_dumps                 | 10.7 ms                                                    | 11.6 ms: 1.09x slower                                                           |
| bench_mp_pool              | 23.9 ms                                                    | 56.3 ms: 2.36x slower                                                           |
| Geometric mean             | (ref)                                                      | 1.02x faster                                                                    |

Benchmark hidden because not significant (11): async_tree_io_tg, async_tree_io, unpickle, chaos, pyflate, scimark_monte_carlo, gc_traversal, float, genshi_xml, logging_silent, pylint
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241010-3.14.0a0-2fbc12f/bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.00x