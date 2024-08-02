# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0a3
- machine: linux-x86_64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.07x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 0.95x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 282 ms: 1.03x slower                                       |
| docutils       | 2.83 sec                                                   | 2.71 sec: 1.04x faster                                     |
| tornado_http   | 94.6 ms                                                    | 97.8 ms: 1.03x slower                                      |
| Geometric mean | (ref)                                                      | 1.01x slower                                               |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 611 ms                                                     | 718 ms: 1.18x slower                                       |
| async_tree_none            | 378 ms                                                     | 448 ms: 1.18x slower                                       |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 727 ms: 1.24x slower                                       |
| async_tree_memoization     | 463 ms                                                     | 574 ms: 1.24x slower                                       |
| async_tree_io              | 939 ms                                                     | 1.20 sec: 1.28x slower                                     |
| async_tree_io_tg           | 936 ms                                                     | 1.21 sec: 1.29x slower                                     |
| async_tree_memoization_tg  | 444 ms                                                     | 587 ms: 1.32x slower                                       |
| async_tree_none_tg         | 336 ms                                                     | 449 ms: 1.34x slower                                       |
| Geometric mean             | (ref)                                                      | 1.26x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 190 ms: 1.01x faster                                       |
| float          | 78.9 ms                                                    | 94.1 ms: 1.19x slower                                      |
| nbody          | 88.3 ms                                                    | 119 ms: 1.35x slower                                       |
| Geometric mean | (ref)                                                      | 1.17x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.6 ms: 1.02x faster                                      |
| regex_effbot   | 3.67 ms                                                    | 3.74 ms: 1.02x slower                                      |
| regex_dna      | 221 ms                                                     | 228 ms: 1.03x slower                                       |
| regex_compile  | 137 ms                                                     | 153 ms: 1.12x slower                                       |
| Geometric mean | (ref)                                                      | 1.04x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| unpickle_list        | 5.34 us                                                    | 5.14 us: 1.04x faster                                      |
| json_loads           | 28.9 us                                                    | 28.2 us: 1.03x faster                                      |
| json_dumps           | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                      |
| xml_etree_parse      | 162 ms                                                     | 159 ms: 1.02x faster                                       |
| pickle_pure_python   | 305 us                                                     | 301 us: 1.01x faster                                       |
| pickle_dict          | 34.8 us                                                    | 35.0 us: 1.01x slower                                      |
| xml_etree_generate   | 87.4 ms                                                    | 89.5 ms: 1.02x slower                                      |
| pickle_list          | 5.11 us                                                    | 5.24 us: 1.03x slower                                      |
| pickle               | 11.5 us                                                    | 11.8 us: 1.03x slower                                      |
| xml_etree_iterparse  | 107 ms                                                     | 112 ms: 1.04x slower                                       |
| unpickle             | 15.1 us                                                    | 16.1 us: 1.06x slower                                      |
| unpickle_pure_python | 218 us                                                     | 234 us: 1.07x slower                                       |
| tomli_loads          | 2.12 sec                                                   | 2.61 sec: 1.23x slower                                     |
| Geometric mean       | (ref)                                                      | 1.03x slower                                               |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.1 ms: 1.07x faster                                      |
| python_startup_no_site | 7.11 ms                                                    | 8.72 ms: 1.23x slower                                      |
| Geometric mean         | (ref)                                                      | 1.07x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|-----------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 11.2 ms                                                    | 14.2 ms: 1.26x slower                                      |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols   | 165 us                                                     | 117 us: 1.41x faster                                       |
| create_gc_cycles           | 1.82 ms                                                    | 1.49 ms: 1.22x faster                                      |
| gc_traversal               | 3.98 ms                                                    | 3.69 ms: 1.08x faster                                      |
| python_startup             | 10.8 ms                                                    | 10.1 ms: 1.07x faster                                      |
| deepcopy_reduce            | 3.35 us                                                    | 3.15 us: 1.06x faster                                      |
| richards                   | 50.9 ms                                                    | 48.3 ms: 1.05x faster                                      |
| richards_super             | 57.4 ms                                                    | 54.7 ms: 1.05x faster                                      |
| mdp                        | 2.79 sec                                                   | 2.67 sec: 1.05x faster                                     |
| docutils                   | 2.83 sec                                                   | 2.71 sec: 1.04x faster                                     |
| unpickle_list              | 5.34 us                                                    | 5.14 us: 1.04x faster                                      |
| asyncio_tcp                | 508 ms                                                     | 492 ms: 1.03x faster                                       |
| asyncio_websockets         | 567 ms                                                     | 551 ms: 1.03x faster                                       |
| sqlite_synth               | 2.99 us                                                    | 2.91 us: 1.03x faster                                      |
| logging_silent             | 105 ns                                                     | 102 ns: 1.03x faster                                       |
| json_loads                 | 28.9 us                                                    | 28.2 us: 1.03x faster                                      |
| coroutines                 | 23.2 ms                                                    | 22.7 ms: 1.02x faster                                      |
| json                       | 5.31 ms                                                    | 5.19 ms: 1.02x faster                                      |
| deepcopy                   | 367 us                                                     | 359 us: 1.02x faster                                       |
| regex_v8                   | 25.1 ms                                                    | 24.6 ms: 1.02x faster                                      |
| json_dumps                 | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                      |
| scimark_lu                 | 122 ms                                                     | 119 ms: 1.02x faster                                       |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                     |
| xml_etree_parse            | 162 ms                                                     | 159 ms: 1.02x faster                                       |
| pickle_pure_python         | 305 us                                                     | 301 us: 1.01x faster                                       |
| generators                 | 29.6 ms                                                    | 29.3 ms: 1.01x faster                                      |
| pidigits                   | 191 ms                                                     | 190 ms: 1.01x faster                                       |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                      |
| pickle_dict                | 34.8 us                                                    | 35.0 us: 1.01x slower                                      |
| sqlglot_parse              | 1.32 ms                                                    | 1.34 ms: 1.01x slower                                      |
| bench_thread_pool          | 834 us                                                     | 848 us: 1.02x slower                                       |
| regex_effbot               | 3.67 ms                                                    | 3.74 ms: 1.02x slower                                      |
| coverage                   | 93.1 ms                                                    | 95.0 ms: 1.02x slower                                      |
| sqlglot_transpile          | 1.63 ms                                                    | 1.67 ms: 1.02x slower                                      |
| xml_etree_generate         | 87.4 ms                                                    | 89.5 ms: 1.02x slower                                      |
| telco                      | 8.41 ms                                                    | 8.62 ms: 1.02x slower                                      |
| deepcopy_memo              | 39.7 us                                                    | 40.8 us: 1.03x slower                                      |
| pickle_list                | 5.11 us                                                    | 5.24 us: 1.03x slower                                      |
| dulwich_log                | 67.2 ms                                                    | 69.0 ms: 1.03x slower                                      |
| 2to3                       | 274 ms                                                     | 282 ms: 1.03x slower                                       |
| pickle                     | 11.5 us                                                    | 11.8 us: 1.03x slower                                      |
| regex_dna                  | 221 ms                                                     | 228 ms: 1.03x slower                                       |
| pycparser                  | 1.16 sec                                                   | 1.19 sec: 1.03x slower                                     |
| sympy_integrate            | 20.5 ms                                                    | 21.1 ms: 1.03x slower                                      |
| tornado_http               | 94.6 ms                                                    | 97.8 ms: 1.03x slower                                      |
| meteor_contest             | 110 ms                                                     | 114 ms: 1.04x slower                                       |
| sympy_sum                  | 156 ms                                                     | 161 ms: 1.04x slower                                       |
| xml_etree_iterparse        | 107 ms                                                     | 112 ms: 1.04x slower                                       |
| async_generators           | 442 ms                                                     | 461 ms: 1.04x slower                                       |
| sympy_expand               | 473 ms                                                     | 495 ms: 1.05x slower                                       |
| scimark_sor                | 127 ms                                                     | 134 ms: 1.05x slower                                       |
| sqlglot_optimize           | 55.5 ms                                                    | 58.4 ms: 1.05x slower                                      |
| pathlib                    | 17.3 ms                                                    | 18.3 ms: 1.05x slower                                      |
| sqlglot_normalize          | 110 ms                                                     | 116 ms: 1.06x slower                                       |
| unpickle                   | 15.1 us                                                    | 16.1 us: 1.06x slower                                      |
| sympy_str                  | 282 ms                                                     | 302 ms: 1.07x slower                                       |
| unpickle_pure_python       | 218 us                                                     | 234 us: 1.07x slower                                       |
| pprint_safe_repr           | 758 ms                                                     | 816 ms: 1.08x slower                                       |
| logging_simple             | 5.74 us                                                    | 6.20 us: 1.08x slower                                      |
| go                         | 145 ms                                                     | 156 ms: 1.08x slower                                       |
| logging_format             | 6.47 us                                                    | 7.07 us: 1.09x slower                                      |
| pprint_pformat             | 1.56 sec                                                   | 1.70 sec: 1.09x slower                                     |
| crypto_pyaes               | 77.5 ms                                                    | 85.0 ms: 1.10x slower                                      |
| pyflate                    | 484 ms                                                     | 536 ms: 1.11x slower                                       |
| regex_compile              | 137 ms                                                     | 153 ms: 1.12x slower                                       |
| fannkuch                   | 402 ms                                                     | 454 ms: 1.13x slower                                       |
| raytrace                   | 267 ms                                                     | 302 ms: 1.13x slower                                       |
| scimark_fft                | 392 ms                                                     | 457 ms: 1.17x slower                                       |
| mypy2                      | 742 ms                                                     | 865 ms: 1.17x slower                                       |
| nqueens                    | 81.4 ms                                                    | 95.4 ms: 1.17x slower                                      |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 718 ms: 1.18x slower                                       |
| scimark_monte_carlo        | 69.2 ms                                                    | 81.4 ms: 1.18x slower                                      |
| async_tree_none            | 378 ms                                                     | 448 ms: 1.18x slower                                       |
| float                      | 78.9 ms                                                    | 94.1 ms: 1.19x slower                                      |
| chaos                      | 61.3 ms                                                    | 73.6 ms: 1.20x slower                                      |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 6.38 ms: 1.21x slower                                      |
| python_startup_no_site     | 7.11 ms                                                    | 8.72 ms: 1.23x slower                                      |
| tomli_loads                | 2.12 sec                                                   | 2.61 sec: 1.23x slower                                     |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 727 ms: 1.24x slower                                       |
| async_tree_memoization     | 463 ms                                                     | 574 ms: 1.24x slower                                       |
| mako                       | 11.2 ms                                                    | 14.2 ms: 1.26x slower                                      |
| async_tree_io              | 939 ms                                                     | 1.20 sec: 1.28x slower                                     |
| async_tree_io_tg           | 936 ms                                                     | 1.21 sec: 1.29x slower                                     |
| comprehensions             | 16.6 us                                                    | 21.6 us: 1.30x slower                                      |
| async_tree_memoization_tg  | 444 ms                                                     | 587 ms: 1.32x slower                                       |
| spectral_norm              | 116 ms                                                     | 154 ms: 1.33x slower                                       |
| async_tree_none_tg         | 336 ms                                                     | 449 ms: 1.34x slower                                       |
| nbody                      | 88.3 ms                                                    | 119 ms: 1.35x slower                                       |
| hexiom                     | 6.30 ms                                                    | 8.65 ms: 1.37x slower                                      |
| deltablue                  | 3.25 ms                                                    | 4.85 ms: 1.49x slower                                      |
| Geometric mean             | (ref)                                                      | 1.07x slower                                               |

Benchmark hidden because not significant (3): xml_etree_process, dask, chameleon
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, thrift
Ignored benchmarks (1) of results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 0.95x