# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a2
- machine: linux-x86_64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.10x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: 0.95x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 288 ms: 1.09x slower                                       |
| chameleon      | 6.85 ms                                                | 7.54 ms: 1.10x slower                                      |
| docutils       | 2.58 sec                                               | 2.73 sec: 1.05x slower                                     |
| tornado_http   | 91.5 ms                                                | 99.5 ms: 1.09x slower                                      |
| Geometric mean | (ref)                                                  | 1.08x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| asyncio_websockets         | 555 ms                                                 | 552 ms: 1.01x faster                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                     |
| async_generators           | 433 ms                                                 | 457 ms: 1.06x slower                                       |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 731 ms: 1.27x slower                                       |
| async_tree_none            | 354 ms                                                 | 456 ms: 1.29x slower                                       |
| async_tree_memoization_tg  | 465 ms                                                 | 611 ms: 1.31x slower                                       |
| async_tree_memoization     | 442 ms                                                 | 583 ms: 1.32x slower                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 760 ms: 1.40x slower                                       |
| async_tree_io              | 843 ms                                                 | 1.22 sec: 1.45x slower                                     |
| async_tree_none_tg         | 320 ms                                                 | 471 ms: 1.47x slower                                       |
| async_tree_io_tg           | 825 ms                                                 | 1.25 sec: 1.52x slower                                     |
| Geometric mean             | (ref)                                                  | 1.22x slower                                               |

Benchmark hidden because not significant (2): coroutines, asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 196 ms: 1.05x slower                                       |
| float          | 78.5 ms                                                | 92.4 ms: 1.18x slower                                      |
| nbody          | 85.7 ms                                                | 119 ms: 1.38x slower                                       |
| Geometric mean | (ref)                                                  | 1.20x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.73 ms: 1.04x faster                                      |
| regex_dna      | 220 ms                                                 | 224 ms: 1.02x slower                                       |
| regex_v8       | 25.3 ms                                                | 25.9 ms: 1.03x slower                                      |
| regex_compile  | 131 ms                                                 | 157 ms: 1.20x slower                                       |
| Geometric mean | (ref)                                                  | 1.05x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle               | 11.6 us                                                | 11.1 us: 1.04x faster                                      |
| pickle_list          | 5.01 us                                                | 4.94 us: 1.01x faster                                      |
| xml_etree_parse      | 156 ms                                                 | 158 ms: 1.02x slower                                       |
| json_dumps           | 10.4 ms                                                | 10.6 ms: 1.02x slower                                      |
| xml_etree_process    | 60.4 ms                                                | 61.8 ms: 1.02x slower                                      |
| pickle_dict          | 33.2 us                                                | 34.0 us: 1.03x slower                                      |
| pickle_pure_python   | 300 us                                                 | 308 us: 1.03x slower                                       |
| xml_etree_generate   | 87.0 ms                                                | 90.2 ms: 1.04x slower                                      |
| unpickle             | 14.9 us                                                | 15.6 us: 1.05x slower                                      |
| json_loads           | 27.0 us                                                | 28.2 us: 1.05x slower                                      |
| unpickle_list        | 4.96 us                                                | 5.21 us: 1.05x slower                                      |
| xml_etree_iterparse  | 102 ms                                                 | 112 ms: 1.09x slower                                       |
| unpickle_pure_python | 213 us                                                 | 240 us: 1.13x slower                                       |
| tomli_loads          | 2.11 sec                                               | 2.39 sec: 1.13x slower                                     |
| Geometric mean       | (ref)                                                  | 1.04x slower                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.3 ms: 1.02x faster                                      |
| python_startup_no_site | 6.99 ms                                                | 9.00 ms: 1.29x slower                                      |
| Geometric mean         | (ref)                                                  | 1.12x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 11.1 ms                                                | 13.7 ms: 1.23x slower                                      |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols   | 159 us                                                 | 122 us: 1.30x faster                                       |
| mypy2                      | 1.07 sec                                               | 869 ms: 1.23x faster                                       |
| create_gc_cycles           | 1.61 ms                                                | 1.46 ms: 1.10x faster                                      |
| pickle                     | 11.6 us                                                | 11.1 us: 1.04x faster                                      |
| regex_effbot               | 3.88 ms                                                | 3.73 ms: 1.04x faster                                      |
| python_startup             | 10.6 ms                                                | 10.3 ms: 1.02x faster                                      |
| pickle_list                | 5.01 us                                                | 4.94 us: 1.01x faster                                      |
| asyncio_websockets         | 555 ms                                                 | 552 ms: 1.01x faster                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                     |
| xml_etree_parse            | 156 ms                                                 | 158 ms: 1.02x slower                                       |
| mdp                        | 2.74 sec                                               | 2.79 sec: 1.02x slower                                     |
| json_dumps                 | 10.4 ms                                                | 10.6 ms: 1.02x slower                                      |
| regex_dna                  | 220 ms                                                 | 224 ms: 1.02x slower                                       |
| sqlite_synth               | 2.85 us                                                | 2.91 us: 1.02x slower                                      |
| xml_etree_process          | 60.4 ms                                                | 61.8 ms: 1.02x slower                                      |
| pickle_dict                | 33.2 us                                                | 34.0 us: 1.03x slower                                      |
| regex_v8                   | 25.3 ms                                                | 25.9 ms: 1.03x slower                                      |
| deepcopy                   | 352 us                                                 | 362 us: 1.03x slower                                       |
| pickle_pure_python         | 300 us                                                 | 308 us: 1.03x slower                                       |
| generators                 | 28.8 ms                                                | 29.6 ms: 1.03x slower                                      |
| richards                   | 48.1 ms                                                | 49.8 ms: 1.04x slower                                      |
| xml_etree_generate         | 87.0 ms                                                | 90.2 ms: 1.04x slower                                      |
| scimark_lu                 | 115 ms                                                 | 120 ms: 1.04x slower                                       |
| unpickle                   | 14.9 us                                                | 15.6 us: 1.05x slower                                      |
| json_loads                 | 27.0 us                                                | 28.2 us: 1.05x slower                                      |
| bench_thread_pool          | 815 us                                                 | 854 us: 1.05x slower                                       |
| unpickle_list              | 4.96 us                                                | 5.21 us: 1.05x slower                                      |
| richards_super             | 54.4 ms                                                | 57.2 ms: 1.05x slower                                      |
| pidigits                   | 186 ms                                                 | 196 ms: 1.05x slower                                       |
| logging_silent             | 102 ns                                                 | 108 ns: 1.05x slower                                       |
| pycparser                  | 1.19 sec                                               | 1.26 sec: 1.05x slower                                     |
| docutils                   | 2.58 sec                                               | 2.73 sec: 1.05x slower                                     |
| async_generators           | 433 ms                                                 | 457 ms: 1.06x slower                                       |
| unpack_sequence            | 42.4 ns                                                | 44.8 ns: 1.06x slower                                      |
| logging_simple             | 5.66 us                                                | 6.03 us: 1.06x slower                                      |
| sympy_sum                  | 150 ms                                                 | 160 ms: 1.07x slower                                       |
| sympy_expand               | 462 ms                                                 | 493 ms: 1.07x slower                                       |
| sympy_integrate            | 19.9 ms                                                | 21.3 ms: 1.07x slower                                      |
| meteor_contest             | 108 ms                                                 | 116 ms: 1.08x slower                                       |
| sqlglot_normalize          | 107 ms                                                 | 115 ms: 1.08x slower                                       |
| sympy_str                  | 274 ms                                                 | 294 ms: 1.08x slower                                       |
| sqlglot_parse              | 1.27 ms                                                | 1.36 ms: 1.08x slower                                      |
| deepcopy_memo              | 38.0 us                                                | 41.0 us: 1.08x slower                                      |
| sqlglot_transpile          | 1.57 ms                                                | 1.70 ms: 1.08x slower                                      |
| sqlglot_optimize           | 53.9 ms                                                | 58.5 ms: 1.09x slower                                      |
| tornado_http               | 91.5 ms                                                | 99.5 ms: 1.09x slower                                      |
| 2to3                       | 265 ms                                                 | 288 ms: 1.09x slower                                       |
| pprint_safe_repr           | 744 ms                                                 | 809 ms: 1.09x slower                                       |
| xml_etree_iterparse        | 102 ms                                                 | 112 ms: 1.09x slower                                       |
| scimark_sor                | 122 ms                                                 | 134 ms: 1.10x slower                                       |
| dulwich_log                | 63.0 ms                                                | 69.0 ms: 1.10x slower                                      |
| logging_format             | 6.25 us                                                | 6.86 us: 1.10x slower                                      |
| chameleon                  | 6.85 ms                                                | 7.54 ms: 1.10x slower                                      |
| dask                       | 338 ms                                                 | 372 ms: 1.10x slower                                       |
| pprint_pformat             | 1.51 sec                                               | 1.68 sec: 1.11x slower                                     |
| pathlib                    | 17.1 ms                                                | 19.0 ms: 1.11x slower                                      |
| unpickle_pure_python       | 213 us                                                 | 240 us: 1.13x slower                                       |
| gc_traversal               | 3.81 ms                                                | 4.29 ms: 1.13x slower                                      |
| pyflate                    | 460 ms                                                 | 521 ms: 1.13x slower                                       |
| tomli_loads                | 2.11 sec                                               | 2.39 sec: 1.13x slower                                     |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.74 ms: 1.14x slower                                      |
| coverage                   | 83.7 ms                                                | 95.6 ms: 1.14x slower                                      |
| crypto_pyaes               | 73.0 ms                                                | 83.3 ms: 1.14x slower                                      |
| go                         | 142 ms                                                 | 163 ms: 1.15x slower                                       |
| nqueens                    | 80.6 ms                                                | 94.1 ms: 1.17x slower                                      |
| float                      | 78.5 ms                                                | 92.4 ms: 1.18x slower                                      |
| fannkuch                   | 381 ms                                                 | 450 ms: 1.18x slower                                       |
| scimark_fft                | 369 ms                                                 | 436 ms: 1.18x slower                                       |
| raytrace                   | 262 ms                                                 | 310 ms: 1.19x slower                                       |
| regex_compile              | 131 ms                                                 | 157 ms: 1.20x slower                                       |
| spectral_norm              | 115 ms                                                 | 140 ms: 1.22x slower                                       |
| scimark_monte_carlo        | 66.3 ms                                                | 81.4 ms: 1.23x slower                                      |
| mako                       | 11.1 ms                                                | 13.7 ms: 1.23x slower                                      |
| chaos                      | 58.4 ms                                                | 74.2 ms: 1.27x slower                                      |
| comprehensions             | 16.4 us                                                | 20.9 us: 1.27x slower                                      |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 731 ms: 1.27x slower                                       |
| python_startup_no_site     | 6.99 ms                                                | 9.00 ms: 1.29x slower                                      |
| async_tree_none            | 354 ms                                                 | 456 ms: 1.29x slower                                       |
| async_tree_memoization_tg  | 465 ms                                                 | 611 ms: 1.31x slower                                       |
| async_tree_memoization     | 442 ms                                                 | 583 ms: 1.32x slower                                       |
| nbody                      | 85.7 ms                                                | 119 ms: 1.38x slower                                       |
| hexiom                     | 6.13 ms                                                | 8.49 ms: 1.39x slower                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 760 ms: 1.40x slower                                       |
| async_tree_io              | 843 ms                                                 | 1.22 sec: 1.45x slower                                     |
| async_tree_none_tg         | 320 ms                                                 | 471 ms: 1.47x slower                                       |
| deltablue                  | 3.15 ms                                                | 4.67 ms: 1.48x slower                                      |
| async_tree_io_tg           | 825 ms                                                 | 1.25 sec: 1.52x slower                                     |
| Geometric mean             | (ref)                                                  | 1.10x slower                                               |

Benchmark hidden because not significant (6): coroutines, asyncio_tcp, bench_mp_pool, telco, deepcopy_reduce, json
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, bpe_tokeniser, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: 0.95x