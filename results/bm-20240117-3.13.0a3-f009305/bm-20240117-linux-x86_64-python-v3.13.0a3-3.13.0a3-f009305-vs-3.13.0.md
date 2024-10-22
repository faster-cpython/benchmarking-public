# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a3
- machine: linux-x86_64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 0.95x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 270 ms: 1.02x slower                                       |
| docutils       | 2.58 sec                                               | 2.68 sec: 1.04x slower                                     |
| html5lib       | 64.5 ms                                                | 67.9 ms: 1.05x slower                                      |
| tornado_http   | 91.5 ms                                                | 96.8 ms: 1.06x slower                                      |
| Geometric mean | (ref)                                                  | 1.03x slower                                               |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| coroutines                 | 22.5 ms                                                | 22.3 ms: 1.01x faster                                      |
| asyncio_tcp                | 488 ms                                                 | 493 ms: 1.01x slower                                       |
| asyncio_websockets         | 555 ms                                                 | 563 ms: 1.01x slower                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.83 sec: 1.02x slower                                     |
| async_generators           | 433 ms                                                 | 454 ms: 1.05x slower                                       |
| async_tree_none            | 354 ms                                                 | 446 ms: 1.26x slower                                       |
| async_tree_memoization_tg  | 465 ms                                                 | 586 ms: 1.26x slower                                       |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 724 ms: 1.26x slower                                       |
| async_tree_memoization     | 442 ms                                                 | 574 ms: 1.30x slower                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 734 ms: 1.35x slower                                       |
| async_tree_none_tg         | 320 ms                                                 | 447 ms: 1.40x slower                                       |
| async_tree_io              | 843 ms                                                 | 1.21 sec: 1.43x slower                                     |
| async_tree_io_tg           | 825 ms                                                 | 1.21 sec: 1.47x slower                                     |
| Geometric mean             | (ref)                                                  | 1.20x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 191 ms: 1.02x slower                                       |
| nbody          | 85.7 ms                                                | 89.5 ms: 1.04x slower                                      |
| float          | 78.5 ms                                                | 82.0 ms: 1.04x slower                                      |
| Geometric mean | (ref)                                                  | 1.04x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.68 ms: 1.06x faster                                      |
| regex_v8       | 25.3 ms                                                | 25.4 ms: 1.00x slower                                      |
| regex_dna      | 220 ms                                                 | 230 ms: 1.05x slower                                       |
| Geometric mean | (ref)                                                  | 1.00x faster                                               |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| xml_etree_process    | 60.4 ms                                                | 59.9 ms: 1.01x faster                                      |
| pickle               | 11.6 us                                                | 11.5 us: 1.00x faster                                      |
| pickle_list          | 5.01 us                                                | 4.98 us: 1.00x faster                                      |
| xml_etree_generate   | 87.0 ms                                                | 87.4 ms: 1.01x slower                                      |
| pickle_pure_python   | 300 us                                                 | 302 us: 1.01x slower                                       |
| pickle_dict          | 33.2 us                                                | 33.8 us: 1.02x slower                                      |
| unpickle_pure_python | 213 us                                                 | 218 us: 1.02x slower                                       |
| tomli_loads          | 2.11 sec                                               | 2.16 sec: 1.02x slower                                     |
| xml_etree_parse      | 156 ms                                                 | 161 ms: 1.03x slower                                       |
| xml_etree_iterparse  | 102 ms                                                 | 106 ms: 1.04x slower                                       |
| unpickle_list        | 4.96 us                                                | 5.25 us: 1.06x slower                                      |
| json_loads           | 27.0 us                                                | 28.7 us: 1.06x slower                                      |
| unpickle             | 14.9 us                                                | 15.9 us: 1.07x slower                                      |
| Geometric mean       | (ref)                                                  | 1.02x slower                                               |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.4 ms: 1.02x faster                                      |
| python_startup_no_site | 6.99 ms                                                | 8.92 ms: 1.28x slower                                      |
| Geometric mean         | (ref)                                                  | 1.12x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| django_template | 34.4 ms                                                | 34.7 ms: 1.01x slower                                      |
| genshi_text     | 22.9 ms                                                | 23.2 ms: 1.01x slower                                      |
| mako            | 11.1 ms                                                | 11.3 ms: 1.02x slower                                      |
| genshi_xml      | 50.3 ms                                                | 52.1 ms: 1.03x slower                                      |
| Geometric mean  | (ref)                                                  | 1.02x slower                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols   | 159 us                                                 | 110 us: 1.45x faster                                       |
| mypy2                      | 1.07 sec                                               | 865 ms: 1.23x faster                                       |
| create_gc_cycles           | 1.61 ms                                                | 1.51 ms: 1.07x faster                                      |
| mdp                        | 2.74 sec                                               | 2.58 sec: 1.06x faster                                     |
| regex_effbot               | 3.88 ms                                                | 3.68 ms: 1.06x faster                                      |
| flaskblogging              | 9.11 ms                                                | 8.79 ms: 1.04x faster                                      |
| spectral_norm              | 115 ms                                                 | 111 ms: 1.03x faster                                       |
| python_startup             | 10.6 ms                                                | 10.4 ms: 1.02x faster                                      |
| deepcopy_reduce            | 3.17 us                                                | 3.11 us: 1.02x faster                                      |
| go                         | 142 ms                                                 | 140 ms: 1.01x faster                                       |
| coroutines                 | 22.5 ms                                                | 22.3 ms: 1.01x faster                                      |
| scimark_lu                 | 115 ms                                                 | 114 ms: 1.01x faster                                       |
| crypto_pyaes               | 73.0 ms                                                | 72.3 ms: 1.01x faster                                      |
| scimark_fft                | 369 ms                                                 | 366 ms: 1.01x faster                                       |
| comprehensions             | 16.4 us                                                | 16.3 us: 1.01x faster                                      |
| xml_etree_process          | 60.4 ms                                                | 59.9 ms: 1.01x faster                                      |
| bench_mp_pool              | 24.0 ms                                                | 23.8 ms: 1.01x faster                                      |
| gc_traversal               | 3.81 ms                                                | 3.78 ms: 1.01x faster                                      |
| deepcopy                   | 352 us                                                 | 350 us: 1.01x faster                                       |
| pickle                     | 11.6 us                                                | 11.5 us: 1.00x faster                                      |
| pickle_list                | 5.01 us                                                | 4.98 us: 1.00x faster                                      |
| hexiom                     | 6.13 ms                                                | 6.10 ms: 1.00x faster                                      |
| sympy_integrate            | 19.9 ms                                                | 20.0 ms: 1.00x slower                                      |
| regex_v8                   | 25.3 ms                                                | 25.4 ms: 1.00x slower                                      |
| xml_etree_generate         | 87.0 ms                                                | 87.4 ms: 1.01x slower                                      |
| pickle_pure_python         | 300 us                                                 | 302 us: 1.01x slower                                       |
| django_template            | 34.4 ms                                                | 34.7 ms: 1.01x slower                                      |
| asyncio_tcp                | 488 ms                                                 | 493 ms: 1.01x slower                                       |
| deepcopy_memo              | 38.0 us                                                | 38.4 us: 1.01x slower                                      |
| sqlglot_parse              | 1.27 ms                                                | 1.28 ms: 1.01x slower                                      |
| raytrace                   | 262 ms                                                 | 264 ms: 1.01x slower                                       |
| sqlite_synth               | 2.85 us                                                | 2.88 us: 1.01x slower                                      |
| telco                      | 8.45 ms                                                | 8.55 ms: 1.01x slower                                      |
| richards_super             | 54.4 ms                                                | 55.1 ms: 1.01x slower                                      |
| generators                 | 28.8 ms                                                | 29.2 ms: 1.01x slower                                      |
| asyncio_websockets         | 555 ms                                                 | 563 ms: 1.01x slower                                       |
| genshi_text                | 22.9 ms                                                | 23.2 ms: 1.01x slower                                      |
| pprint_pformat             | 1.51 sec                                               | 1.53 sec: 1.02x slower                                     |
| mako                       | 11.1 ms                                                | 11.3 ms: 1.02x slower                                      |
| sqlglot_optimize           | 53.9 ms                                                | 54.8 ms: 1.02x slower                                      |
| sympy_sum                  | 150 ms                                                 | 152 ms: 1.02x slower                                       |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.10 ms: 1.02x slower                                      |
| richards                   | 48.1 ms                                                | 48.9 ms: 1.02x slower                                      |
| sqlglot_normalize          | 107 ms                                                 | 109 ms: 1.02x slower                                       |
| pickle_dict                | 33.2 us                                                | 33.8 us: 1.02x slower                                      |
| meteor_contest             | 108 ms                                                 | 110 ms: 1.02x slower                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.83 sec: 1.02x slower                                     |
| 2to3                       | 265 ms                                                 | 270 ms: 1.02x slower                                       |
| sqlglot_transpile          | 1.57 ms                                                | 1.61 ms: 1.02x slower                                      |
| unpickle_pure_python       | 213 us                                                 | 218 us: 1.02x slower                                       |
| tomli_loads                | 2.11 sec                                               | 2.16 sec: 1.02x slower                                     |
| aiohttp                    | 1.14 ms                                                | 1.17 ms: 1.02x slower                                      |
| pidigits                   | 186 ms                                                 | 191 ms: 1.02x slower                                       |
| chaos                      | 58.4 ms                                                | 59.9 ms: 1.03x slower                                      |
| pyflate                    | 460 ms                                                 | 471 ms: 1.03x slower                                       |
| deltablue                  | 3.15 ms                                                | 3.23 ms: 1.03x slower                                      |
| logging_silent             | 102 ns                                                 | 105 ns: 1.03x slower                                       |
| xml_etree_parse            | 156 ms                                                 | 161 ms: 1.03x slower                                       |
| gunicorn                   | 1.23 ms                                                | 1.27 ms: 1.03x slower                                      |
| bench_thread_pool          | 815 us                                                 | 842 us: 1.03x slower                                       |
| genshi_xml                 | 50.3 ms                                                | 52.1 ms: 1.03x slower                                      |
| scimark_monte_carlo        | 66.3 ms                                                | 68.6 ms: 1.03x slower                                      |
| docutils                   | 2.58 sec                                               | 2.68 sec: 1.04x slower                                     |
| json                       | 5.20 ms                                                | 5.39 ms: 1.04x slower                                      |
| logging_simple             | 5.66 us                                                | 5.89 us: 1.04x slower                                      |
| xml_etree_iterparse        | 102 ms                                                 | 106 ms: 1.04x slower                                       |
| logging_format             | 6.25 us                                                | 6.53 us: 1.04x slower                                      |
| nbody                      | 85.7 ms                                                | 89.5 ms: 1.04x slower                                      |
| float                      | 78.5 ms                                                | 82.0 ms: 1.04x slower                                      |
| regex_dna                  | 220 ms                                                 | 230 ms: 1.05x slower                                       |
| async_generators           | 433 ms                                                 | 454 ms: 1.05x slower                                       |
| html5lib                   | 64.5 ms                                                | 67.9 ms: 1.05x slower                                      |
| fannkuch                   | 381 ms                                                 | 402 ms: 1.06x slower                                       |
| unpickle_list              | 4.96 us                                                | 5.25 us: 1.06x slower                                      |
| tornado_http               | 91.5 ms                                                | 96.8 ms: 1.06x slower                                      |
| dulwich_log                | 63.0 ms                                                | 66.8 ms: 1.06x slower                                      |
| json_loads                 | 27.0 us                                                | 28.7 us: 1.06x slower                                      |
| unpickle                   | 14.9 us                                                | 15.9 us: 1.07x slower                                      |
| scimark_sor                | 122 ms                                                 | 131 ms: 1.07x slower                                       |
| pathlib                    | 17.1 ms                                                | 18.5 ms: 1.08x slower                                      |
| coverage                   | 83.7 ms                                                | 95.8 ms: 1.14x slower                                      |
| async_tree_none            | 354 ms                                                 | 446 ms: 1.26x slower                                       |
| async_tree_memoization_tg  | 465 ms                                                 | 586 ms: 1.26x slower                                       |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 724 ms: 1.26x slower                                       |
| python_startup_no_site     | 6.99 ms                                                | 8.92 ms: 1.28x slower                                      |
| async_tree_memoization     | 442 ms                                                 | 574 ms: 1.30x slower                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 734 ms: 1.35x slower                                       |
| async_tree_none_tg         | 320 ms                                                 | 447 ms: 1.40x slower                                       |
| async_tree_io              | 843 ms                                                 | 1.21 sec: 1.43x slower                                     |
| async_tree_io_tg           | 825 ms                                                 | 1.21 sec: 1.47x slower                                     |
| Geometric mean             | (ref)                                                  | 1.03x slower                                               |

Benchmark hidden because not significant (11): djangocms, pycparser, regex_compile, thrift, pylint, nqueens, pprint_safe_repr, chameleon, sympy_str, json_dumps, sympy_expand
Ignored benchmarks (3) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, dask, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 0.95x