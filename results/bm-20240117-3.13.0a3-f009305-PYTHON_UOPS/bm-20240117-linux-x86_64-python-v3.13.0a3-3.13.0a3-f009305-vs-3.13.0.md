# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a3
- machine: linux-x86_64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.10x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: 0.96x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 282 ms: 1.06x slower                                       |
| chameleon      | 6.85 ms                                                | 7.24 ms: 1.06x slower                                      |
| docutils       | 2.58 sec                                               | 2.71 sec: 1.05x slower                                     |
| tornado_http   | 91.5 ms                                                | 97.8 ms: 1.07x slower                                      |
| Geometric mean | (ref)                                                  | 1.06x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| asyncio_websockets         | 555 ms                                                 | 551 ms: 1.01x faster                                       |
| asyncio_tcp                | 488 ms                                                 | 492 ms: 1.01x slower                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                     |
| async_generators           | 433 ms                                                 | 461 ms: 1.07x slower                                       |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 718 ms: 1.25x slower                                       |
| async_tree_memoization_tg  | 465 ms                                                 | 587 ms: 1.26x slower                                       |
| async_tree_none            | 354 ms                                                 | 448 ms: 1.27x slower                                       |
| async_tree_memoization     | 442 ms                                                 | 574 ms: 1.30x slower                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 727 ms: 1.34x slower                                       |
| async_tree_none_tg         | 320 ms                                                 | 449 ms: 1.40x slower                                       |
| async_tree_io              | 843 ms                                                 | 1.20 sec: 1.43x slower                                     |
| async_tree_io_tg           | 825 ms                                                 | 1.21 sec: 1.46x slower                                     |
| Geometric mean             | (ref)                                                  | 1.20x slower                                               |

Benchmark hidden because not significant (1): coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 190 ms: 1.02x slower                                       |
| float          | 78.5 ms                                                | 94.1 ms: 1.20x slower                                      |
| nbody          | 85.7 ms                                                | 119 ms: 1.39x slower                                       |
| Geometric mean | (ref)                                                  | 1.19x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.74 ms: 1.04x faster                                      |
| regex_v8       | 25.3 ms                                                | 24.6 ms: 1.03x faster                                      |
| regex_dna      | 220 ms                                                 | 228 ms: 1.04x slower                                       |
| regex_compile  | 131 ms                                                 | 153 ms: 1.17x slower                                       |
| Geometric mean | (ref)                                                  | 1.03x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 300 us                                                 | 301 us: 1.00x slower                                       |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                      |
| xml_etree_process    | 60.4 ms                                                | 61.1 ms: 1.01x slower                                      |
| pickle               | 11.6 us                                                | 11.8 us: 1.02x slower                                      |
| xml_etree_parse      | 156 ms                                                 | 159 ms: 1.02x slower                                       |
| xml_etree_generate   | 87.0 ms                                                | 89.5 ms: 1.03x slower                                      |
| unpickle_list        | 4.96 us                                                | 5.14 us: 1.04x slower                                      |
| json_loads           | 27.0 us                                                | 28.2 us: 1.04x slower                                      |
| pickle_list          | 5.01 us                                                | 5.24 us: 1.05x slower                                      |
| pickle_dict          | 33.2 us                                                | 35.0 us: 1.06x slower                                      |
| unpickle             | 14.9 us                                                | 16.1 us: 1.08x slower                                      |
| unpickle_pure_python | 213 us                                                 | 234 us: 1.10x slower                                       |
| xml_etree_iterparse  | 102 ms                                                 | 112 ms: 1.10x slower                                       |
| tomli_loads          | 2.11 sec                                               | 2.61 sec: 1.24x slower                                     |
| Geometric mean       | (ref)                                                  | 1.06x slower                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.1 ms: 1.05x faster                                      |
| python_startup_no_site | 6.99 ms                                                | 8.72 ms: 1.25x slower                                      |
| Geometric mean         | (ref)                                                  | 1.09x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 11.1 ms                                                | 14.2 ms: 1.28x slower                                      |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols   | 159 us                                                 | 117 us: 1.37x faster                                       |
| mypy2                      | 1.07 sec                                               | 865 ms: 1.24x faster                                       |
| create_gc_cycles           | 1.61 ms                                                | 1.49 ms: 1.08x faster                                      |
| python_startup             | 10.6 ms                                                | 10.1 ms: 1.05x faster                                      |
| regex_effbot               | 3.88 ms                                                | 3.74 ms: 1.04x faster                                      |
| gc_traversal               | 3.81 ms                                                | 3.69 ms: 1.03x faster                                      |
| mdp                        | 2.74 sec                                               | 2.67 sec: 1.03x faster                                     |
| regex_v8                   | 25.3 ms                                                | 24.6 ms: 1.03x faster                                      |
| asyncio_websockets         | 555 ms                                                 | 551 ms: 1.01x faster                                       |
| deepcopy_reduce            | 3.17 us                                                | 3.15 us: 1.00x faster                                      |
| pickle_pure_python         | 300 us                                                 | 301 us: 1.00x slower                                       |
| richards                   | 48.1 ms                                                | 48.3 ms: 1.00x slower                                      |
| richards_super             | 54.4 ms                                                | 54.7 ms: 1.01x slower                                      |
| asyncio_tcp                | 488 ms                                                 | 492 ms: 1.01x slower                                       |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                     |
| xml_etree_process          | 60.4 ms                                                | 61.1 ms: 1.01x slower                                      |
| pidigits                   | 186 ms                                                 | 190 ms: 1.02x slower                                       |
| generators                 | 28.8 ms                                                | 29.3 ms: 1.02x slower                                      |
| deepcopy                   | 352 us                                                 | 359 us: 1.02x slower                                       |
| telco                      | 8.45 ms                                                | 8.62 ms: 1.02x slower                                      |
| pickle                     | 11.6 us                                                | 11.8 us: 1.02x slower                                      |
| xml_etree_parse            | 156 ms                                                 | 159 ms: 1.02x slower                                       |
| sqlite_synth               | 2.85 us                                                | 2.91 us: 1.02x slower                                      |
| xml_etree_generate         | 87.0 ms                                                | 89.5 ms: 1.03x slower                                      |
| unpickle_list              | 4.96 us                                                | 5.14 us: 1.04x slower                                      |
| regex_dna                  | 220 ms                                                 | 228 ms: 1.04x slower                                       |
| scimark_lu                 | 115 ms                                                 | 119 ms: 1.04x slower                                       |
| bench_thread_pool          | 815 us                                                 | 848 us: 1.04x slower                                       |
| json_loads                 | 27.0 us                                                | 28.2 us: 1.04x slower                                      |
| pickle_list                | 5.01 us                                                | 5.24 us: 1.05x slower                                      |
| docutils                   | 2.58 sec                                               | 2.71 sec: 1.05x slower                                     |
| pickle_dict                | 33.2 us                                                | 35.0 us: 1.06x slower                                      |
| meteor_contest             | 108 ms                                                 | 114 ms: 1.06x slower                                       |
| chameleon                  | 6.85 ms                                                | 7.24 ms: 1.06x slower                                      |
| sqlglot_parse              | 1.27 ms                                                | 1.34 ms: 1.06x slower                                      |
| 2to3                       | 265 ms                                                 | 282 ms: 1.06x slower                                       |
| sympy_integrate            | 19.9 ms                                                | 21.1 ms: 1.06x slower                                      |
| sqlglot_transpile          | 1.57 ms                                                | 1.67 ms: 1.06x slower                                      |
| async_generators           | 433 ms                                                 | 461 ms: 1.07x slower                                       |
| tornado_http               | 91.5 ms                                                | 97.8 ms: 1.07x slower                                      |
| pathlib                    | 17.1 ms                                                | 18.3 ms: 1.07x slower                                      |
| deepcopy_memo              | 38.0 us                                                | 40.8 us: 1.07x slower                                      |
| sympy_expand               | 462 ms                                                 | 495 ms: 1.07x slower                                       |
| sympy_sum                  | 150 ms                                                 | 161 ms: 1.08x slower                                       |
| unpickle                   | 14.9 us                                                | 16.1 us: 1.08x slower                                      |
| sqlglot_optimize           | 53.9 ms                                                | 58.4 ms: 1.08x slower                                      |
| sqlglot_normalize          | 107 ms                                                 | 116 ms: 1.08x slower                                       |
| scimark_sor                | 122 ms                                                 | 134 ms: 1.09x slower                                       |
| dask                       | 338 ms                                                 | 369 ms: 1.09x slower                                       |
| logging_simple             | 5.66 us                                                | 6.20 us: 1.09x slower                                      |
| dulwich_log                | 63.0 ms                                                | 69.0 ms: 1.10x slower                                      |
| unpickle_pure_python       | 213 us                                                 | 234 us: 1.10x slower                                       |
| pprint_safe_repr           | 744 ms                                                 | 816 ms: 1.10x slower                                       |
| xml_etree_iterparse        | 102 ms                                                 | 112 ms: 1.10x slower                                       |
| go                         | 142 ms                                                 | 156 ms: 1.10x slower                                       |
| sympy_str                  | 274 ms                                                 | 302 ms: 1.10x slower                                       |
| pprint_pformat             | 1.51 sec                                               | 1.70 sec: 1.12x slower                                     |
| logging_format             | 6.25 us                                                | 7.07 us: 1.13x slower                                      |
| coverage                   | 83.7 ms                                                | 95.0 ms: 1.13x slower                                      |
| raytrace                   | 262 ms                                                 | 302 ms: 1.15x slower                                       |
| crypto_pyaes               | 73.0 ms                                                | 85.0 ms: 1.16x slower                                      |
| pyflate                    | 460 ms                                                 | 536 ms: 1.17x slower                                       |
| regex_compile              | 131 ms                                                 | 153 ms: 1.17x slower                                       |
| nqueens                    | 80.6 ms                                                | 95.4 ms: 1.18x slower                                      |
| fannkuch                   | 381 ms                                                 | 454 ms: 1.19x slower                                       |
| float                      | 78.5 ms                                                | 94.1 ms: 1.20x slower                                      |
| scimark_monte_carlo        | 66.3 ms                                                | 81.4 ms: 1.23x slower                                      |
| tomli_loads                | 2.11 sec                                               | 2.61 sec: 1.24x slower                                     |
| scimark_fft                | 369 ms                                                 | 457 ms: 1.24x slower                                       |
| python_startup_no_site     | 6.99 ms                                                | 8.72 ms: 1.25x slower                                      |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 718 ms: 1.25x slower                                       |
| chaos                      | 58.4 ms                                                | 73.6 ms: 1.26x slower                                      |
| async_tree_memoization_tg  | 465 ms                                                 | 587 ms: 1.26x slower                                       |
| async_tree_none            | 354 ms                                                 | 448 ms: 1.27x slower                                       |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 6.38 ms: 1.27x slower                                      |
| mako                       | 11.1 ms                                                | 14.2 ms: 1.28x slower                                      |
| async_tree_memoization     | 442 ms                                                 | 574 ms: 1.30x slower                                       |
| comprehensions             | 16.4 us                                                | 21.6 us: 1.32x slower                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 727 ms: 1.34x slower                                       |
| spectral_norm              | 115 ms                                                 | 154 ms: 1.34x slower                                       |
| nbody                      | 85.7 ms                                                | 119 ms: 1.39x slower                                       |
| async_tree_none_tg         | 320 ms                                                 | 449 ms: 1.40x slower                                       |
| hexiom                     | 6.13 ms                                                | 8.65 ms: 1.41x slower                                      |
| async_tree_io              | 843 ms                                                 | 1.20 sec: 1.43x slower                                     |
| async_tree_io_tg           | 825 ms                                                 | 1.21 sec: 1.46x slower                                     |
| deltablue                  | 3.15 ms                                                | 4.85 ms: 1.54x slower                                      |
| Geometric mean             | (ref)                                                  | 1.10x slower                                               |

Benchmark hidden because not significant (6): json, unpack_sequence, bench_mp_pool, logging_silent, pycparser, coroutines
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, bpe_tokeniser, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: 0.96x