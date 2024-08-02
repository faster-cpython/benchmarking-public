# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0a2
- machine: linux-x86_64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.07x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 0.95x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 288 ms: 1.05x slower                                       |
| chameleon      | 7.22 ms                                                    | 7.54 ms: 1.04x slower                                      |
| docutils       | 2.83 sec                                                   | 2.73 sec: 1.04x faster                                     |
| tornado_http   | 94.6 ms                                                    | 99.5 ms: 1.05x slower                                      |
| Geometric mean | (ref)                                                      | 1.03x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 611 ms                                                     | 731 ms: 1.20x slower                                       |
| async_tree_none            | 378 ms                                                     | 456 ms: 1.21x slower                                       |
| async_tree_memoization     | 463 ms                                                     | 583 ms: 1.26x slower                                       |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 760 ms: 1.29x slower                                       |
| async_tree_io              | 939 ms                                                     | 1.22 sec: 1.30x slower                                     |
| async_tree_io_tg           | 936 ms                                                     | 1.25 sec: 1.34x slower                                     |
| async_tree_memoization_tg  | 444 ms                                                     | 611 ms: 1.38x slower                                       |
| async_tree_none_tg         | 336 ms                                                     | 471 ms: 1.40x slower                                       |
| Geometric mean             | (ref)                                                      | 1.29x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 196 ms: 1.02x slower                                       |
| float          | 78.9 ms                                                    | 92.4 ms: 1.17x slower                                      |
| nbody          | 88.3 ms                                                    | 119 ms: 1.34x slower                                       |
| Geometric mean | (ref)                                                      | 1.17x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_dna      | 221 ms                                                     | 224 ms: 1.01x slower                                       |
| regex_effbot   | 3.67 ms                                                    | 3.73 ms: 1.02x slower                                      |
| regex_v8       | 25.1 ms                                                    | 25.9 ms: 1.03x slower                                      |
| regex_compile  | 137 ms                                                     | 157 ms: 1.15x slower                                       |
| Geometric mean | (ref)                                                      | 1.05x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_list          | 5.11 us                                                    | 4.94 us: 1.03x faster                                      |
| pickle               | 11.5 us                                                    | 11.1 us: 1.03x faster                                      |
| unpickle_list        | 5.34 us                                                    | 5.21 us: 1.03x faster                                      |
| pickle_dict          | 34.8 us                                                    | 34.0 us: 1.02x faster                                      |
| json_loads           | 28.9 us                                                    | 28.2 us: 1.02x faster                                      |
| xml_etree_parse      | 162 ms                                                     | 158 ms: 1.02x faster                                       |
| json_dumps           | 10.7 ms                                                    | 10.6 ms: 1.01x faster                                      |
| pickle_pure_python   | 305 us                                                     | 308 us: 1.01x slower                                       |
| xml_etree_process    | 61.2 ms                                                    | 61.8 ms: 1.01x slower                                      |
| unpickle             | 15.1 us                                                    | 15.6 us: 1.03x slower                                      |
| xml_etree_generate   | 87.4 ms                                                    | 90.2 ms: 1.03x slower                                      |
| xml_etree_iterparse  | 107 ms                                                     | 112 ms: 1.04x slower                                       |
| unpickle_pure_python | 218 us                                                     | 240 us: 1.10x slower                                       |
| tomli_loads          | 2.12 sec                                                   | 2.39 sec: 1.13x slower                                     |
| Geometric mean       | (ref)                                                      | 1.01x slower                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.3 ms: 1.04x faster                                      |
| python_startup_no_site | 7.11 ms                                                    | 9.00 ms: 1.27x slower                                      |
| Geometric mean         | (ref)                                                      | 1.10x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-----------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 11.2 ms                                                    | 13.7 ms: 1.22x slower                                      |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols   | 165 us                                                     | 122 us: 1.35x faster                                       |
| create_gc_cycles           | 1.82 ms                                                    | 1.46 ms: 1.24x faster                                      |
| deepcopy_reduce            | 3.35 us                                                    | 3.18 us: 1.05x faster                                      |
| asyncio_tcp                | 508 ms                                                     | 487 ms: 1.04x faster                                       |
| python_startup             | 10.8 ms                                                    | 10.3 ms: 1.04x faster                                      |
| docutils                   | 2.83 sec                                                   | 2.73 sec: 1.04x faster                                     |
| coroutines                 | 23.2 ms                                                    | 22.4 ms: 1.03x faster                                      |
| pickle_list                | 5.11 us                                                    | 4.94 us: 1.03x faster                                      |
| pickle                     | 11.5 us                                                    | 11.1 us: 1.03x faster                                      |
| sqlite_synth               | 2.99 us                                                    | 2.91 us: 1.03x faster                                      |
| asyncio_websockets         | 567 ms                                                     | 552 ms: 1.03x faster                                       |
| unpickle_list              | 5.34 us                                                    | 5.21 us: 1.03x faster                                      |
| pickle_dict                | 34.8 us                                                    | 34.0 us: 1.02x faster                                      |
| json_loads                 | 28.9 us                                                    | 28.2 us: 1.02x faster                                      |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                     |
| richards                   | 50.9 ms                                                    | 49.8 ms: 1.02x faster                                      |
| xml_etree_parse            | 162 ms                                                     | 158 ms: 1.02x faster                                       |
| scimark_lu                 | 122 ms                                                     | 120 ms: 1.02x faster                                       |
| json                       | 5.31 ms                                                    | 5.22 ms: 1.02x faster                                      |
| deepcopy                   | 367 us                                                     | 362 us: 1.02x faster                                       |
| json_dumps                 | 10.7 ms                                                    | 10.6 ms: 1.01x faster                                      |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                      |
| pickle_pure_python         | 305 us                                                     | 308 us: 1.01x slower                                       |
| xml_etree_process          | 61.2 ms                                                    | 61.8 ms: 1.01x slower                                      |
| regex_dna                  | 221 ms                                                     | 224 ms: 1.01x slower                                       |
| regex_effbot               | 3.67 ms                                                    | 3.73 ms: 1.02x slower                                      |
| pidigits                   | 191 ms                                                     | 196 ms: 1.02x slower                                       |
| bench_thread_pool          | 834 us                                                     | 854 us: 1.02x slower                                       |
| sympy_sum                  | 156 ms                                                     | 160 ms: 1.02x slower                                       |
| logging_silent             | 105 ns                                                     | 108 ns: 1.03x slower                                       |
| dulwich_log                | 67.2 ms                                                    | 69.0 ms: 1.03x slower                                      |
| coverage                   | 93.1 ms                                                    | 95.6 ms: 1.03x slower                                      |
| unpickle                   | 15.1 us                                                    | 15.6 us: 1.03x slower                                      |
| regex_v8                   | 25.1 ms                                                    | 25.9 ms: 1.03x slower                                      |
| deepcopy_memo              | 39.7 us                                                    | 41.0 us: 1.03x slower                                      |
| xml_etree_generate         | 87.4 ms                                                    | 90.2 ms: 1.03x slower                                      |
| sqlglot_parse              | 1.32 ms                                                    | 1.36 ms: 1.03x slower                                      |
| async_generators           | 442 ms                                                     | 457 ms: 1.03x slower                                       |
| sqlglot_transpile          | 1.63 ms                                                    | 1.70 ms: 1.04x slower                                      |
| xml_etree_iterparse        | 107 ms                                                     | 112 ms: 1.04x slower                                       |
| sympy_integrate            | 20.5 ms                                                    | 21.3 ms: 1.04x slower                                      |
| sympy_str                  | 282 ms                                                     | 294 ms: 1.04x slower                                       |
| sympy_expand               | 473 ms                                                     | 493 ms: 1.04x slower                                       |
| chameleon                  | 7.22 ms                                                    | 7.54 ms: 1.04x slower                                      |
| sqlglot_normalize          | 110 ms                                                     | 115 ms: 1.05x slower                                       |
| logging_simple             | 5.74 us                                                    | 6.03 us: 1.05x slower                                      |
| 2to3                       | 274 ms                                                     | 288 ms: 1.05x slower                                       |
| tornado_http               | 94.6 ms                                                    | 99.5 ms: 1.05x slower                                      |
| scimark_sor                | 127 ms                                                     | 134 ms: 1.05x slower                                       |
| meteor_contest             | 110 ms                                                     | 116 ms: 1.05x slower                                       |
| sqlglot_optimize           | 55.5 ms                                                    | 58.5 ms: 1.05x slower                                      |
| logging_format             | 6.47 us                                                    | 6.86 us: 1.06x slower                                      |
| pprint_safe_repr           | 758 ms                                                     | 809 ms: 1.07x slower                                       |
| pyflate                    | 484 ms                                                     | 521 ms: 1.08x slower                                       |
| crypto_pyaes               | 77.5 ms                                                    | 83.3 ms: 1.08x slower                                      |
| pprint_pformat             | 1.56 sec                                                   | 1.68 sec: 1.08x slower                                     |
| gc_traversal               | 3.98 ms                                                    | 4.29 ms: 1.08x slower                                      |
| pycparser                  | 1.16 sec                                                   | 1.26 sec: 1.09x slower                                     |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 5.74 ms: 1.09x slower                                      |
| pathlib                    | 17.3 ms                                                    | 19.0 ms: 1.10x slower                                      |
| unpickle_pure_python       | 218 us                                                     | 240 us: 1.10x slower                                       |
| scimark_fft                | 392 ms                                                     | 436 ms: 1.11x slower                                       |
| fannkuch                   | 402 ms                                                     | 450 ms: 1.12x slower                                       |
| tomli_loads                | 2.12 sec                                                   | 2.39 sec: 1.13x slower                                     |
| go                         | 145 ms                                                     | 163 ms: 1.13x slower                                       |
| regex_compile              | 137 ms                                                     | 157 ms: 1.15x slower                                       |
| nqueens                    | 81.4 ms                                                    | 94.1 ms: 1.16x slower                                      |
| raytrace                   | 267 ms                                                     | 310 ms: 1.16x slower                                       |
| float                      | 78.9 ms                                                    | 92.4 ms: 1.17x slower                                      |
| mypy2                      | 742 ms                                                     | 869 ms: 1.17x slower                                       |
| scimark_monte_carlo        | 69.2 ms                                                    | 81.4 ms: 1.18x slower                                      |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 731 ms: 1.20x slower                                       |
| async_tree_none            | 378 ms                                                     | 456 ms: 1.21x slower                                       |
| spectral_norm              | 116 ms                                                     | 140 ms: 1.21x slower                                       |
| chaos                      | 61.3 ms                                                    | 74.2 ms: 1.21x slower                                      |
| mako                       | 11.2 ms                                                    | 13.7 ms: 1.22x slower                                      |
| comprehensions             | 16.6 us                                                    | 20.9 us: 1.26x slower                                      |
| async_tree_memoization     | 463 ms                                                     | 583 ms: 1.26x slower                                       |
| python_startup_no_site     | 7.11 ms                                                    | 9.00 ms: 1.27x slower                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 760 ms: 1.29x slower                                       |
| async_tree_io              | 939 ms                                                     | 1.22 sec: 1.30x slower                                     |
| async_tree_io_tg           | 936 ms                                                     | 1.25 sec: 1.34x slower                                     |
| nbody                      | 88.3 ms                                                    | 119 ms: 1.34x slower                                       |
| hexiom                     | 6.30 ms                                                    | 8.49 ms: 1.35x slower                                      |
| async_tree_memoization_tg  | 444 ms                                                     | 611 ms: 1.38x slower                                       |
| async_tree_none_tg         | 336 ms                                                     | 471 ms: 1.40x slower                                       |
| deltablue                  | 3.25 ms                                                    | 4.67 ms: 1.44x slower                                      |
| Geometric mean             | (ref)                                                      | 1.07x slower                                               |

Benchmark hidden because not significant (5): richards_super, generators, mdp, telco, dask
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, thrift
Ignored benchmarks (1) of results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 0.95x