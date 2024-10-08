# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: underflow_known_dyna
- machine: linux-x86_64
- commit hash: 7ad3776
- commit date: 2024-09-06
- overall geometric mean: 1.03x faster
- HPT reliability: 99.67%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 285 ms: 1.04x slower                                                        |
| docutils       | 2.83 sec                                                   | 3.25 sec: 1.15x slower                                                      |
| html5lib       | 67.2 ms                                                    | 69.1 ms: 1.03x slower                                                       |
| tornado_http   | 94.6 ms                                                    | 103 ms: 1.09x slower                                                        |
| Geometric mean | (ref)                                                      | 1.08x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                                        |
| async_tree_memoization     | 463 ms                                                     | 406 ms: 1.14x faster                                                        |
| async_tree_memoization_tg  | 444 ms                                                     | 406 ms: 1.09x faster                                                        |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 563 ms: 1.09x faster                                                        |
| async_tree_none_tg         | 336 ms                                                     | 311 ms: 1.08x faster                                                        |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 546 ms: 1.08x faster                                                        |
| async_tree_io_tg           | 936 ms                                                     | 900 ms: 1.04x faster                                                        |
| Geometric mean             | (ref)                                                      | 1.08x faster                                                                |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.9 ms: 1.11x faster                                                       |
| nbody          | 88.3 ms                                                    | 79.6 ms: 1.11x faster                                                       |
| pidigits       | 191 ms                                                     | 185 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                      | 1.08x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 221 ms                                                     | 216 ms: 1.02x faster                                                        |
| regex_v8       | 25.1 ms                                                    | 24.6 ms: 1.02x faster                                                       |
| regex_effbot   | 3.67 ms                                                    | 3.62 ms: 1.01x faster                                                       |
| regex_compile  | 137 ms                                                     | 151 ms: 1.10x slower                                                        |
| Geometric mean | (ref)                                                      | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_process    | 61.2 ms                                                    | 54.3 ms: 1.13x faster                                                       |
| xml_etree_generate   | 87.4 ms                                                    | 77.8 ms: 1.12x faster                                                       |
| xml_etree_parse      | 162 ms                                                     | 148 ms: 1.10x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                     | 98.7 ms: 1.09x faster                                                       |
| unpickle_pure_python | 218 us                                                     | 201 us: 1.08x faster                                                        |
| tomli_loads          | 2.12 sec                                                   | 2.00 sec: 1.06x faster                                                      |
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                       |
| pickle_dict          | 34.8 us                                                    | 34.1 us: 1.02x faster                                                       |
| json_loads           | 28.9 us                                                    | 28.5 us: 1.01x faster                                                       |
| unpickle_list        | 5.34 us                                                    | 5.29 us: 1.01x faster                                                       |
| pickle               | 11.5 us                                                    | 11.6 us: 1.01x slower                                                       |
| pickle_pure_python   | 305 us                                                     | 310 us: 1.02x slower                                                        |
| pickle_list          | 5.11 us                                                    | 5.27 us: 1.03x slower                                                       |
| Geometric mean       | (ref)                                                      | 1.04x faster                                                                |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.01x faster                                                       |
| python_startup_no_site | 7.11 ms                                                    | 7.17 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                      | 1.00x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.70 ms: 1.16x faster                                                       |
| genshi_text     | 23.7 ms                                                    | 23.9 ms: 1.01x slower                                                       |
| django_template | 34.8 ms                                                    | 37.9 ms: 1.09x slower                                                       |
| genshi_xml      | 51.6 ms                                                    | 63.5 ms: 1.23x slower                                                       |
| Geometric mean  | (ref)                                                      | 1.04x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 26.0 us: 1.53x faster                                                       |
| deepcopy                   | 367 us                                                     | 263 us: 1.40x faster                                                        |
| richards_super             | 57.4 ms                                                    | 42.8 ms: 1.34x faster                                                       |
| richards                   | 50.9 ms                                                    | 38.4 ms: 1.33x faster                                                       |
| scimark_fft                | 392 ms                                                     | 309 ms: 1.27x faster                                                        |
| deepcopy_reduce            | 3.35 us                                                    | 2.64 us: 1.27x faster                                                       |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.44 ms: 1.19x faster                                                       |
| crypto_pyaes               | 77.5 ms                                                    | 65.4 ms: 1.18x faster                                                       |
| spectral_norm              | 116 ms                                                     | 99.9 ms: 1.16x faster                                                       |
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                                        |
| mako                       | 11.2 ms                                                    | 9.70 ms: 1.16x faster                                                       |
| async_tree_memoization     | 463 ms                                                     | 406 ms: 1.14x faster                                                        |
| bpe_tokeniser              | 5.02 sec                                                   | 4.45 sec: 1.13x faster                                                      |
| xml_etree_process          | 61.2 ms                                                    | 54.3 ms: 1.13x faster                                                       |
| xml_etree_generate         | 87.4 ms                                                    | 77.8 ms: 1.12x faster                                                       |
| float                      | 78.9 ms                                                    | 70.9 ms: 1.11x faster                                                       |
| nbody                      | 88.3 ms                                                    | 79.6 ms: 1.11x faster                                                       |
| mdp                        | 2.79 sec                                                   | 2.54 sec: 1.10x faster                                                      |
| xml_etree_parse            | 162 ms                                                     | 148 ms: 1.10x faster                                                        |
| async_tree_memoization_tg  | 444 ms                                                     | 406 ms: 1.09x faster                                                        |
| pathlib                    | 17.3 ms                                                    | 15.9 ms: 1.09x faster                                                       |
| xml_etree_iterparse        | 107 ms                                                     | 98.7 ms: 1.09x faster                                                       |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 563 ms: 1.09x faster                                                        |
| unpickle_pure_python       | 218 us                                                     | 201 us: 1.08x faster                                                        |
| async_tree_none_tg         | 336 ms                                                     | 311 ms: 1.08x faster                                                        |
| logging_silent             | 105 ns                                                     | 97.3 ns: 1.08x faster                                                       |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 546 ms: 1.08x faster                                                        |
| telco                      | 8.41 ms                                                    | 7.83 ms: 1.07x faster                                                       |
| sqlite_synth               | 2.99 us                                                    | 2.79 us: 1.07x faster                                                       |
| coverage                   | 93.1 ms                                                    | 87.0 ms: 1.07x faster                                                       |
| scimark_lu                 | 122 ms                                                     | 115 ms: 1.06x faster                                                        |
| tomli_loads                | 2.12 sec                                                   | 2.00 sec: 1.06x faster                                                      |
| thrift                     | 823 us                                                     | 780 us: 1.05x faster                                                        |
| fannkuch                   | 402 ms                                                     | 382 ms: 1.05x faster                                                        |
| gc_traversal               | 3.98 ms                                                    | 3.78 ms: 1.05x faster                                                       |
| go                         | 145 ms                                                     | 138 ms: 1.05x faster                                                        |
| chaos                      | 61.3 ms                                                    | 58.5 ms: 1.05x faster                                                       |
| pyflate                    | 484 ms                                                     | 462 ms: 1.05x faster                                                        |
| async_tree_io_tg           | 936 ms                                                     | 900 ms: 1.04x faster                                                        |
| json_dumps                 | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                       |
| pidigits                   | 191 ms                                                     | 185 ms: 1.03x faster                                                        |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.03x faster                                                        |
| pprint_pformat             | 1.56 sec                                                   | 1.51 sec: 1.03x faster                                                      |
| pprint_safe_repr           | 758 ms                                                     | 738 ms: 1.03x faster                                                        |
| scimark_sor                | 127 ms                                                     | 124 ms: 1.03x faster                                                        |
| scimark_monte_carlo        | 69.2 ms                                                    | 67.4 ms: 1.03x faster                                                       |
| regex_dna                  | 221 ms                                                     | 216 ms: 1.02x faster                                                        |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                                        |
| regex_v8                   | 25.1 ms                                                    | 24.6 ms: 1.02x faster                                                       |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                                      |
| pickle_dict                | 34.8 us                                                    | 34.1 us: 1.02x faster                                                       |
| create_gc_cycles           | 1.82 ms                                                    | 1.78 ms: 1.02x faster                                                       |
| asyncio_tcp                | 508 ms                                                     | 500 ms: 1.02x faster                                                        |
| regex_effbot               | 3.67 ms                                                    | 3.62 ms: 1.01x faster                                                       |
| json_loads                 | 28.9 us                                                    | 28.5 us: 1.01x faster                                                       |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.01x faster                                                       |
| unpickle_list              | 5.34 us                                                    | 5.29 us: 1.01x faster                                                       |
| comprehensions             | 16.6 us                                                    | 16.5 us: 1.01x faster                                                       |
| json                       | 5.31 ms                                                    | 5.27 ms: 1.01x faster                                                       |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                       |
| genshi_text                | 23.7 ms                                                    | 23.9 ms: 1.01x slower                                                       |
| python_startup_no_site     | 7.11 ms                                                    | 7.17 ms: 1.01x slower                                                       |
| pickle                     | 11.5 us                                                    | 11.6 us: 1.01x slower                                                       |
| bench_thread_pool          | 834 us                                                     | 846 us: 1.01x slower                                                        |
| pickle_pure_python         | 305 us                                                     | 310 us: 1.02x slower                                                        |
| html5lib                   | 67.2 ms                                                    | 69.1 ms: 1.03x slower                                                       |
| logging_simple             | 5.74 us                                                    | 5.91 us: 1.03x slower                                                       |
| nqueens                    | 81.4 ms                                                    | 83.8 ms: 1.03x slower                                                       |
| raytrace                   | 267 ms                                                     | 275 ms: 1.03x slower                                                        |
| pickle_list                | 5.11 us                                                    | 5.27 us: 1.03x slower                                                       |
| 2to3                       | 274 ms                                                     | 285 ms: 1.04x slower                                                        |
| async_generators           | 442 ms                                                     | 460 ms: 1.04x slower                                                        |
| sqlglot_normalize          | 110 ms                                                     | 119 ms: 1.08x slower                                                        |
| sqlglot_optimize           | 55.5 ms                                                    | 60.1 ms: 1.08x slower                                                       |
| sqlglot_transpile          | 1.63 ms                                                    | 1.78 ms: 1.09x slower                                                       |
| django_template            | 34.8 ms                                                    | 37.9 ms: 1.09x slower                                                       |
| hexiom                     | 6.30 ms                                                    | 6.86 ms: 1.09x slower                                                       |
| tornado_http               | 94.6 ms                                                    | 103 ms: 1.09x slower                                                        |
| pycparser                  | 1.16 sec                                                   | 1.27 sec: 1.10x slower                                                      |
| regex_compile              | 137 ms                                                     | 151 ms: 1.10x slower                                                        |
| dulwich_log                | 67.2 ms                                                    | 74.1 ms: 1.10x slower                                                       |
| sympy_expand               | 473 ms                                                     | 530 ms: 1.12x slower                                                        |
| generators                 | 29.6 ms                                                    | 33.2 ms: 1.12x slower                                                       |
| sympy_str                  | 282 ms                                                     | 319 ms: 1.13x slower                                                        |
| sqlglot_parse              | 1.32 ms                                                    | 1.52 ms: 1.15x slower                                                       |
| docutils                   | 2.83 sec                                                   | 3.25 sec: 1.15x slower                                                      |
| sympy_integrate            | 20.5 ms                                                    | 24.9 ms: 1.21x slower                                                       |
| sympy_sum                  | 156 ms                                                     | 189 ms: 1.21x slower                                                        |
| genshi_xml                 | 51.6 ms                                                    | 63.5 ms: 1.23x slower                                                       |
| pylint                     | 317 ms                                                     | 416 ms: 1.31x slower                                                        |
| Geometric mean             | (ref)                                                      | 1.03x faster                                                                |

Benchmark hidden because not significant (6): typing_runtime_protocols, logging_format, async_tree_io, deltablue, unpickle, coroutines
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240906-3.14.0a0-7ad3776-JIT/bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776.json: unpack_sequence

# HPT report

- Reliability score: 99.67% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.10x