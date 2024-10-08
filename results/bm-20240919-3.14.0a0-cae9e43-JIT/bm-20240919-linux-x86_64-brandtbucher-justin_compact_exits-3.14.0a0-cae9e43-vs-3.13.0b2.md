# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: justin_compact_exits
- machine: linux-x86_64
- commit hash: cae9e43
- commit date: 2024-09-19
- overall geometric mean: 1.06x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 277 ms: 1.01x slower                                                        |
| docutils       | 2.83 sec                                                   | 2.92 sec: 1.03x slower                                                      |
| tornado_http   | 94.6 ms                                                    | 94.0 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                      | 1.01x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization     | 463 ms                                                     | 380 ms: 1.22x faster                                                        |
| async_tree_memoization_tg  | 444 ms                                                     | 371 ms: 1.20x faster                                                        |
| async_tree_none            | 378 ms                                                     | 320 ms: 1.18x faster                                                        |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 536 ms: 1.14x faster                                                        |
| async_tree_none_tg         | 336 ms                                                     | 307 ms: 1.09x faster                                                        |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 540 ms: 1.09x faster                                                        |
| async_tree_io_tg           | 936 ms                                                     | 875 ms: 1.07x faster                                                        |
| Geometric mean             | (ref)                                                      | 1.12x faster                                                                |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.4 ms: 1.12x faster                                                       |
| nbody          | 88.3 ms                                                    | 80.5 ms: 1.10x faster                                                       |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                      | 1.08x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.0 ms: 1.04x faster                                                       |
| regex_dna      | 221 ms                                                     | 215 ms: 1.03x faster                                                        |
| regex_effbot   | 3.67 ms                                                    | 3.63 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                      | 1.02x faster                                                                |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 87.4 ms                                                    | 76.0 ms: 1.15x faster                                                       |
| xml_etree_process    | 61.2 ms                                                    | 53.7 ms: 1.14x faster                                                       |
| tomli_loads          | 2.12 sec                                                   | 1.91 sec: 1.11x faster                                                      |
| xml_etree_parse      | 162 ms                                                     | 147 ms: 1.10x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                     | 97.4 ms: 1.10x faster                                                       |
| json_loads           | 28.9 us                                                    | 27.2 us: 1.06x faster                                                       |
| pickle_dict          | 34.8 us                                                    | 32.9 us: 1.06x faster                                                       |
| json_dumps           | 10.7 ms                                                    | 10.2 ms: 1.05x faster                                                       |
| unpickle_list        | 5.34 us                                                    | 5.19 us: 1.03x faster                                                       |
| unpickle_pure_python | 218 us                                                     | 213 us: 1.02x faster                                                        |
| pickle_pure_python   | 305 us                                                     | 302 us: 1.01x faster                                                        |
| pickle               | 11.5 us                                                    | 11.5 us: 1.01x slower                                                       |
| pickle_list          | 5.11 us                                                    | 5.18 us: 1.02x slower                                                       |
| Geometric mean       | (ref)                                                      | 1.06x faster                                                                |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                       |
| python_startup_no_site | 7.11 ms                                                    | 7.07 ms: 1.00x faster                                                       |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.72 ms: 1.16x faster                                                       |
| genshi_text     | 23.7 ms                                                    | 24.4 ms: 1.03x slower                                                       |
| django_template | 34.8 ms                                                    | 36.0 ms: 1.03x slower                                                       |
| genshi_xml      | 51.6 ms                                                    | 56.4 ms: 1.09x slower                                                       |
| Geometric mean  | (ref)                                                      | 1.00x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 26.7 us: 1.49x faster                                                       |
| deepcopy                   | 367 us                                                     | 254 us: 1.45x faster                                                        |
| scimark_fft                | 392 ms                                                     | 306 ms: 1.28x faster                                                        |
| richards_super             | 57.4 ms                                                    | 45.7 ms: 1.25x faster                                                       |
| deepcopy_reduce            | 3.35 us                                                    | 2.67 us: 1.25x faster                                                       |
| richards                   | 50.9 ms                                                    | 40.7 ms: 1.25x faster                                                       |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.21 ms: 1.25x faster                                                       |
| async_tree_memoization     | 463 ms                                                     | 380 ms: 1.22x faster                                                        |
| async_tree_memoization_tg  | 444 ms                                                     | 371 ms: 1.20x faster                                                        |
| async_tree_none            | 378 ms                                                     | 320 ms: 1.18x faster                                                        |
| crypto_pyaes               | 77.5 ms                                                    | 66.0 ms: 1.17x faster                                                       |
| spectral_norm              | 116 ms                                                     | 100 ms: 1.16x faster                                                        |
| go                         | 145 ms                                                     | 125 ms: 1.16x faster                                                        |
| mako                       | 11.2 ms                                                    | 9.72 ms: 1.16x faster                                                       |
| xml_etree_generate         | 87.4 ms                                                    | 76.0 ms: 1.15x faster                                                       |
| bpe_tokeniser              | 5.02 sec                                                   | 4.38 sec: 1.15x faster                                                      |
| xml_etree_process          | 61.2 ms                                                    | 53.7 ms: 1.14x faster                                                       |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 536 ms: 1.14x faster                                                        |
| float                      | 78.9 ms                                                    | 70.4 ms: 1.12x faster                                                       |
| tomli_loads                | 2.12 sec                                                   | 1.91 sec: 1.11x faster                                                      |
| mdp                        | 2.79 sec                                                   | 2.52 sec: 1.11x faster                                                      |
| scimark_lu                 | 122 ms                                                     | 110 ms: 1.10x faster                                                        |
| xml_etree_parse            | 162 ms                                                     | 147 ms: 1.10x faster                                                        |
| scimark_monte_carlo        | 69.2 ms                                                    | 62.7 ms: 1.10x faster                                                       |
| xml_etree_iterparse        | 107 ms                                                     | 97.4 ms: 1.10x faster                                                       |
| pathlib                    | 17.3 ms                                                    | 15.7 ms: 1.10x faster                                                       |
| coverage                   | 93.1 ms                                                    | 84.7 ms: 1.10x faster                                                       |
| nbody                      | 88.3 ms                                                    | 80.5 ms: 1.10x faster                                                       |
| async_tree_none_tg         | 336 ms                                                     | 307 ms: 1.09x faster                                                        |
| sqlite_synth               | 2.99 us                                                    | 2.73 us: 1.09x faster                                                       |
| scimark_sor                | 127 ms                                                     | 117 ms: 1.09x faster                                                        |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 540 ms: 1.09x faster                                                        |
| async_tree_io_tg           | 936 ms                                                     | 875 ms: 1.07x faster                                                        |
| gc_traversal               | 3.98 ms                                                    | 3.72 ms: 1.07x faster                                                       |
| json_loads                 | 28.9 us                                                    | 27.2 us: 1.06x faster                                                       |
| pyflate                    | 484 ms                                                     | 457 ms: 1.06x faster                                                        |
| telco                      | 8.41 ms                                                    | 7.95 ms: 1.06x faster                                                       |
| fannkuch                   | 402 ms                                                     | 380 ms: 1.06x faster                                                        |
| pickle_dict                | 34.8 us                                                    | 32.9 us: 1.06x faster                                                       |
| json_dumps                 | 10.7 ms                                                    | 10.2 ms: 1.05x faster                                                       |
| logging_format             | 6.47 us                                                    | 6.14 us: 1.05x faster                                                       |
| pprint_safe_repr           | 758 ms                                                     | 722 ms: 1.05x faster                                                        |
| chaos                      | 61.3 ms                                                    | 58.4 ms: 1.05x faster                                                       |
| pprint_pformat             | 1.56 sec                                                   | 1.49 sec: 1.05x faster                                                      |
| thrift                     | 823 us                                                     | 787 us: 1.05x faster                                                        |
| create_gc_cycles           | 1.82 ms                                                    | 1.74 ms: 1.05x faster                                                       |
| regex_v8                   | 25.1 ms                                                    | 24.0 ms: 1.04x faster                                                       |
| json                       | 5.31 ms                                                    | 5.09 ms: 1.04x faster                                                       |
| deltablue                  | 3.25 ms                                                    | 3.14 ms: 1.04x faster                                                       |
| typing_runtime_protocols   | 165 us                                                     | 160 us: 1.03x faster                                                        |
| logging_simple             | 5.74 us                                                    | 5.57 us: 1.03x faster                                                       |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                        |
| unpickle_list              | 5.34 us                                                    | 5.19 us: 1.03x faster                                                       |
| regex_dna                  | 221 ms                                                     | 215 ms: 1.03x faster                                                        |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.03x faster                                                        |
| unpickle_pure_python       | 218 us                                                     | 213 us: 1.02x faster                                                        |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                                        |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                       |
| asyncio_tcp                | 508 ms                                                     | 499 ms: 1.02x faster                                                        |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                                      |
| logging_silent             | 105 ns                                                     | 103 ns: 1.01x faster                                                        |
| pickle_pure_python         | 305 us                                                     | 302 us: 1.01x faster                                                        |
| regex_effbot               | 3.67 ms                                                    | 3.63 ms: 1.01x faster                                                       |
| tornado_http               | 94.6 ms                                                    | 94.0 ms: 1.01x faster                                                       |
| python_startup_no_site     | 7.11 ms                                                    | 7.07 ms: 1.00x faster                                                       |
| sqlglot_normalize          | 110 ms                                                     | 110 ms: 1.00x faster                                                        |
| bench_thread_pool          | 834 us                                                     | 837 us: 1.00x slower                                                        |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                       |
| pickle                     | 11.5 us                                                    | 11.5 us: 1.01x slower                                                       |
| 2to3                       | 274 ms                                                     | 277 ms: 1.01x slower                                                        |
| pickle_list                | 5.11 us                                                    | 5.18 us: 1.02x slower                                                       |
| sqlglot_optimize           | 55.5 ms                                                    | 56.5 ms: 1.02x slower                                                       |
| genshi_text                | 23.7 ms                                                    | 24.4 ms: 1.03x slower                                                       |
| raytrace                   | 267 ms                                                     | 275 ms: 1.03x slower                                                        |
| docutils                   | 2.83 sec                                                   | 2.92 sec: 1.03x slower                                                      |
| django_template            | 34.8 ms                                                    | 36.0 ms: 1.03x slower                                                       |
| async_generators           | 442 ms                                                     | 458 ms: 1.04x slower                                                        |
| sqlglot_transpile          | 1.63 ms                                                    | 1.70 ms: 1.04x slower                                                       |
| sympy_str                  | 282 ms                                                     | 297 ms: 1.05x slower                                                        |
| sympy_expand               | 473 ms                                                     | 502 ms: 1.06x slower                                                        |
| nqueens                    | 81.4 ms                                                    | 86.8 ms: 1.07x slower                                                       |
| hexiom                     | 6.30 ms                                                    | 6.87 ms: 1.09x slower                                                       |
| generators                 | 29.6 ms                                                    | 32.4 ms: 1.09x slower                                                       |
| genshi_xml                 | 51.6 ms                                                    | 56.4 ms: 1.09x slower                                                       |
| sympy_sum                  | 156 ms                                                     | 171 ms: 1.10x slower                                                        |
| sympy_integrate            | 20.5 ms                                                    | 22.7 ms: 1.11x slower                                                       |
| pylint                     | 317 ms                                                     | 360 ms: 1.13x slower                                                        |
| Geometric mean             | (ref)                                                      | 1.06x faster                                                                |

Benchmark hidden because not significant (7): async_tree_io, unpickle, coroutines, sqlglot_parse, comprehensions, regex_compile, dulwich_log
Ignored benchmarks (9) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, html5lib, mypy2, pycparser
Ignored benchmarks (1) of results/bm-20240919-3.14.0a0-cae9e43-JIT/bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.08x