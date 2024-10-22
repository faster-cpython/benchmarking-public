# Results vs. 3.13.0

- fork: python
- ref: db6f5e193315a3bbfa7b
- machine: linux-x86_64
- commit hash: db6f5e1
- commit date: 2024-08-13
- overall geometric mean: 1.46x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x slower
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-linux-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 395 ms: 1.49x slower                                                  |
| docutils       | 2.58 sec                                               | 3.34 sec: 1.29x slower                                                |
| html5lib       | 64.5 ms                                                | 98.3 ms: 1.52x slower                                                 |
| tornado_http   | 91.5 ms                                                | 138 ms: 1.51x slower                                                  |
| Geometric mean | (ref)                                                  | 1.45x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-linux-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 456 ms: 1.02x faster                                                  |
| asyncio_websockets         | 555 ms                                                 | 553 ms: 1.00x faster                                                  |
| async_tree_io_tg           | 825 ms                                                 | 840 ms: 1.02x slower                                                  |
| async_tree_io              | 843 ms                                                 | 906 ms: 1.07x slower                                                  |
| async_tree_none_tg         | 320 ms                                                 | 350 ms: 1.09x slower                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 602 ms: 1.11x slower                                                  |
| asyncio_tcp                | 488 ms                                                 | 561 ms: 1.15x slower                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 2.07 sec: 1.15x slower                                                |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 662 ms: 1.15x slower                                                  |
| async_tree_none            | 354 ms                                                 | 412 ms: 1.16x slower                                                  |
| async_tree_memoization     | 442 ms                                                 | 517 ms: 1.17x slower                                                  |
| async_generators           | 433 ms                                                 | 559 ms: 1.29x slower                                                  |
| coroutines                 | 22.5 ms                                                | 32.1 ms: 1.43x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.13x slower                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-linux-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 184 ms: 1.01x faster                                                  |
| float          | 78.5 ms                                                | 142 ms: 1.80x slower                                                  |
| nbody          | 85.7 ms                                                | 222 ms: 2.59x slower                                                  |
| Geometric mean | (ref)                                                  | 1.67x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-linux-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.51 ms: 1.11x faster                                                 |
| regex_dna      | 220 ms                                                 | 218 ms: 1.01x faster                                                  |
| regex_v8       | 25.3 ms                                                | 26.0 ms: 1.03x slower                                                 |
| regex_compile  | 131 ms                                                 | 217 ms: 1.66x slower                                                  |
| Geometric mean | (ref)                                                  | 1.11x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-linux-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 156 ms                                                 | 149 ms: 1.04x faster                                                  |
| xml_etree_iterparse  | 102 ms                                                 | 113 ms: 1.10x slower                                                  |
| json_loads           | 27.0 us                                                | 32.4 us: 1.20x slower                                                 |
| xml_etree_generate   | 87.0 ms                                                | 110 ms: 1.27x slower                                                  |
| json_dumps           | 10.4 ms                                                | 13.5 ms: 1.30x slower                                                 |
| xml_etree_process    | 60.4 ms                                                | 88.8 ms: 1.47x slower                                                 |
| tomli_loads          | 2.11 sec                                               | 3.26 sec: 1.54x slower                                                |
| pickle_pure_python   | 300 us                                                 | 572 us: 1.90x slower                                                  |
| unpickle_pure_python | 213 us                                                 | 411 us: 1.92x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.37x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-linux-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 13.7 ms: 1.30x slower                                                 |
| python_startup_no_site | 6.99 ms                                                | 9.31 ms: 1.33x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.32x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-linux-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 50.3 ms                                                | 82.1 ms: 1.63x slower                                                 |
| django_template | 34.4 ms                                                | 59.2 ms: 1.72x slower                                                 |
| genshi_text     | 22.9 ms                                                | 39.6 ms: 1.73x slower                                                 |
| mako            | 11.1 ms                                                | 21.0 ms: 1.89x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.74x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-linux-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| gc_traversal               | 3.81 ms                                                | 3.02 ms: 1.26x faster                                                 |
| create_gc_cycles           | 1.61 ms                                                | 1.38 ms: 1.17x faster                                                 |
| regex_effbot               | 3.88 ms                                                | 3.51 ms: 1.11x faster                                                 |
| xml_etree_parse            | 156 ms                                                 | 149 ms: 1.04x faster                                                  |
| async_tree_memoization_tg  | 465 ms                                                 | 456 ms: 1.02x faster                                                  |
| pidigits                   | 186 ms                                                 | 184 ms: 1.01x faster                                                  |
| regex_dna                  | 220 ms                                                 | 218 ms: 1.01x faster                                                  |
| asyncio_websockets         | 555 ms                                                 | 553 ms: 1.00x faster                                                  |
| bench_mp_pool              | 24.0 ms                                                | 23.9 ms: 1.00x faster                                                 |
| async_tree_io_tg           | 825 ms                                                 | 840 ms: 1.02x slower                                                  |
| regex_v8                   | 25.3 ms                                                | 26.0 ms: 1.03x slower                                                 |
| async_tree_io              | 843 ms                                                 | 906 ms: 1.07x slower                                                  |
| async_tree_none_tg         | 320 ms                                                 | 350 ms: 1.09x slower                                                  |
| xml_etree_iterparse        | 102 ms                                                 | 113 ms: 1.10x slower                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 602 ms: 1.11x slower                                                  |
| pathlib                    | 17.1 ms                                                | 19.2 ms: 1.12x slower                                                 |
| asyncio_tcp                | 488 ms                                                 | 561 ms: 1.15x slower                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 2.07 sec: 1.15x slower                                                |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 662 ms: 1.15x slower                                                  |
| json                       | 5.20 ms                                                | 6.04 ms: 1.16x slower                                                 |
| async_tree_none            | 354 ms                                                 | 412 ms: 1.16x slower                                                  |
| async_tree_memoization     | 442 ms                                                 | 517 ms: 1.17x slower                                                  |
| mdp                        | 2.74 sec                                               | 3.21 sec: 1.17x slower                                                |
| deepcopy                   | 352 us                                                 | 417 us: 1.18x slower                                                  |
| json_loads                 | 27.0 us                                                | 32.4 us: 1.20x slower                                                 |
| telco                      | 8.45 ms                                                | 10.4 ms: 1.23x slower                                                 |
| pylint                     | 313 ms                                                 | 395 ms: 1.26x slower                                                  |
| xml_etree_generate         | 87.0 ms                                                | 110 ms: 1.27x slower                                                  |
| docutils                   | 2.58 sec                                               | 3.34 sec: 1.29x slower                                                |
| async_generators           | 433 ms                                                 | 559 ms: 1.29x slower                                                  |
| generators                 | 28.8 ms                                                | 37.4 ms: 1.30x slower                                                 |
| json_dumps                 | 10.4 ms                                                | 13.5 ms: 1.30x slower                                                 |
| python_startup             | 10.6 ms                                                | 13.7 ms: 1.30x slower                                                 |
| scimark_fft                | 369 ms                                                 | 484 ms: 1.31x slower                                                  |
| coverage                   | 83.7 ms                                                | 111 ms: 1.33x slower                                                  |
| meteor_contest             | 108 ms                                                 | 143 ms: 1.33x slower                                                  |
| python_startup_no_site     | 6.99 ms                                                | 9.31 ms: 1.33x slower                                                 |
| deepcopy_reduce            | 3.17 us                                                | 4.28 us: 1.35x slower                                                 |
| pycparser                  | 1.19 sec                                               | 1.63 sec: 1.36x slower                                                |
| deepcopy_memo              | 38.0 us                                                | 52.2 us: 1.37x slower                                                 |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 6.95 ms: 1.38x slower                                                 |
| bpe_tokeniser              | 4.69 sec                                               | 6.57 sec: 1.40x slower                                                |
| coroutines                 | 22.5 ms                                                | 32.1 ms: 1.43x slower                                                 |
| sympy_integrate            | 19.9 ms                                                | 28.8 ms: 1.45x slower                                                 |
| xml_etree_process          | 60.4 ms                                                | 88.8 ms: 1.47x slower                                                 |
| nqueens                    | 80.6 ms                                                | 119 ms: 1.47x slower                                                  |
| 2to3                       | 265 ms                                                 | 395 ms: 1.49x slower                                                  |
| tornado_http               | 91.5 ms                                                | 138 ms: 1.51x slower                                                  |
| html5lib                   | 64.5 ms                                                | 98.3 ms: 1.52x slower                                                 |
| thrift                     | 796 us                                                 | 1.22 ms: 1.54x slower                                                 |
| tomli_loads                | 2.11 sec                                               | 3.26 sec: 1.54x slower                                                |
| crypto_pyaes               | 73.0 ms                                                | 113 ms: 1.55x slower                                                  |
| sympy_str                  | 274 ms                                                 | 425 ms: 1.55x slower                                                  |
| typing_runtime_protocols   | 159 us                                                 | 249 us: 1.56x slower                                                  |
| sqlglot_optimize           | 53.9 ms                                                | 85.9 ms: 1.59x slower                                                 |
| sqlglot_normalize          | 107 ms                                                 | 171 ms: 1.59x slower                                                  |
| sympy_expand               | 462 ms                                                 | 748 ms: 1.62x slower                                                  |
| richards                   | 48.1 ms                                                | 78.3 ms: 1.63x slower                                                 |
| genshi_xml                 | 50.3 ms                                                | 82.1 ms: 1.63x slower                                                 |
| fannkuch                   | 381 ms                                                 | 625 ms: 1.64x slower                                                  |
| spectral_norm              | 115 ms                                                 | 189 ms: 1.64x slower                                                  |
| regex_compile              | 131 ms                                                 | 217 ms: 1.66x slower                                                  |
| pyflate                    | 460 ms                                                 | 773 ms: 1.68x slower                                                  |
| pprint_safe_repr           | 744 ms                                                 | 1.27 sec: 1.71x slower                                                |
| sympy_sum                  | 150 ms                                                 | 256 ms: 1.71x slower                                                  |
| django_template            | 34.4 ms                                                | 59.2 ms: 1.72x slower                                                 |
| genshi_text                | 22.9 ms                                                | 39.6 ms: 1.73x slower                                                 |
| pprint_pformat             | 1.51 sec                                               | 2.64 sec: 1.75x slower                                                |
| richards_super             | 54.4 ms                                                | 95.4 ms: 1.75x slower                                                 |
| comprehensions             | 16.4 us                                                | 28.8 us: 1.76x slower                                                 |
| float                      | 78.5 ms                                                | 142 ms: 1.80x slower                                                  |
| logging_simple             | 5.66 us                                                | 10.3 us: 1.82x slower                                                 |
| logging_format             | 6.25 us                                                | 11.6 us: 1.85x slower                                                 |
| logging_silent             | 102 ns                                                 | 191 ns: 1.87x slower                                                  |
| scimark_monte_carlo        | 66.3 ms                                                | 124 ms: 1.88x slower                                                  |
| mako                       | 11.1 ms                                                | 21.0 ms: 1.89x slower                                                 |
| pickle_pure_python         | 300 us                                                 | 572 us: 1.90x slower                                                  |
| unpickle_pure_python       | 213 us                                                 | 411 us: 1.92x slower                                                  |
| sqlglot_transpile          | 1.57 ms                                                | 3.08 ms: 1.96x slower                                                 |
| hexiom                     | 6.13 ms                                                | 12.0 ms: 1.96x slower                                                 |
| sqlglot_parse              | 1.27 ms                                                | 2.63 ms: 2.08x slower                                                 |
| scimark_lu                 | 115 ms                                                 | 240 ms: 2.09x slower                                                  |
| chaos                      | 58.4 ms                                                | 125 ms: 2.14x slower                                                  |
| go                         | 142 ms                                                 | 306 ms: 2.16x slower                                                  |
| scimark_sor                | 122 ms                                                 | 266 ms: 2.17x slower                                                  |
| raytrace                   | 262 ms                                                 | 598 ms: 2.29x slower                                                  |
| nbody                      | 85.7 ms                                                | 222 ms: 2.59x slower                                                  |
| deltablue                  | 3.15 ms                                                | 8.34 ms: 2.65x slower                                                 |
| bench_thread_pool          | 815 us                                                 | 3.11 ms: 3.82x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.46x slower                                                          |
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.36x
- 95% likely to have a slowdown of 1.34x
- 99% likely to have a slowdown of 1.31x

# Memory
- memory change: 1.16x