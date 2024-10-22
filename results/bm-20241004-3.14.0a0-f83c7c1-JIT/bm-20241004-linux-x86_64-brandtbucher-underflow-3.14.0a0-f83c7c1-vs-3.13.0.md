# Results vs. 3.13.0

- fork: brandtbucher
- ref: underflow
- machine: linux-x86_64
- commit hash: f83c7c1
- commit date: 2024-10-04
- overall geometric mean: 1.03x slower
- HPT reliability: 62.93%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 291 ms: 1.10x slower                                             |
| docutils       | 2.58 sec                                               | 3.07 sec: 1.19x slower                                           |
| html5lib       | 64.5 ms                                                | 71.3 ms: 1.10x slower                                            |
| tornado_http   | 91.5 ms                                                | 102 ms: 1.12x slower                                             |
| Geometric mean | (ref)                                                  | 1.13x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 393 ms: 1.18x faster                                             |
| async_tree_none            | 354 ms                                                 | 324 ms: 1.09x faster                                             |
| async_tree_memoization     | 442 ms                                                 | 415 ms: 1.07x faster                                             |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.00x slower                                             |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                           |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 557 ms: 1.02x slower                                             |
| asyncio_tcp                | 488 ms                                                 | 502 ms: 1.03x slower                                             |
| coroutines                 | 22.5 ms                                                | 23.4 ms: 1.04x slower                                            |
| async_generators           | 433 ms                                                 | 454 ms: 1.05x slower                                             |
| async_tree_io              | 843 ms                                                 | 890 ms: 1.06x slower                                             |
| async_tree_io_tg           | 825 ms                                                 | 877 ms: 1.06x slower                                             |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                     |

Benchmark hidden because not significant (2): async_tree_none_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 78.5 ms                                                | 71.3 ms: 1.10x faster                                            |
| nbody          | 85.7 ms                                                | 81.5 ms: 1.05x faster                                            |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                             |
| Geometric mean | (ref)                                                  | 1.05x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.67 ms: 1.06x faster                                            |
| regex_v8       | 25.3 ms                                                | 24.7 ms: 1.02x faster                                            |
| regex_dna      | 220 ms                                                 | 217 ms: 1.01x faster                                             |
| regex_compile  | 131 ms                                                 | 155 ms: 1.18x slower                                             |
| Geometric mean | (ref)                                                  | 1.02x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 77.0 ms: 1.13x faster                                            |
| xml_etree_process    | 60.4 ms                                                | 55.4 ms: 1.09x faster                                            |
| xml_etree_parse      | 156 ms                                                 | 147 ms: 1.06x faster                                             |
| unpickle_pure_python | 213 us                                                 | 202 us: 1.05x faster                                             |
| xml_etree_iterparse  | 102 ms                                                 | 97.4 ms: 1.05x faster                                            |
| json_dumps           | 10.4 ms                                                | 10.1 ms: 1.03x faster                                            |
| unpickle             | 14.9 us                                                | 14.6 us: 1.02x faster                                            |
| tomli_loads          | 2.11 sec                                               | 2.08 sec: 1.02x faster                                           |
| pickle               | 11.6 us                                                | 11.6 us: 1.01x slower                                            |
| pickle_list          | 5.01 us                                                | 5.07 us: 1.01x slower                                            |
| unpickle_list        | 4.96 us                                                | 5.14 us: 1.04x slower                                            |
| pickle_dict          | 33.2 us                                                | 34.8 us: 1.05x slower                                            |
| json_loads           | 27.0 us                                                | 28.3 us: 1.05x slower                                            |
| pickle_pure_python   | 300 us                                                 | 318 us: 1.06x slower                                             |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.00x faster                                            |
| python_startup_no_site | 6.99 ms                                                | 7.07 ms: 1.01x slower                                            |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.86 ms: 1.13x faster                                            |
| genshi_text     | 22.9 ms                                                | 24.3 ms: 1.06x slower                                            |
| django_template | 34.4 ms                                                | 41.1 ms: 1.19x slower                                            |
| genshi_xml      | 50.3 ms                                                | 70.3 ms: 1.40x slower                                            |
| Geometric mean  | (ref)                                                  | 1.12x slower                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 26.6 us: 1.43x faster                                            |
| deepcopy                   | 352 us                                                 | 267 us: 1.32x faster                                             |
| richards                   | 48.1 ms                                                | 40.6 ms: 1.19x faster                                            |
| async_tree_memoization_tg  | 465 ms                                                 | 393 ms: 1.18x faster                                             |
| richards_super             | 54.4 ms                                                | 46.2 ms: 1.18x faster                                            |
| scimark_fft                | 369 ms                                                 | 313 ms: 1.18x faster                                             |
| deepcopy_reduce            | 3.17 us                                                | 2.69 us: 1.18x faster                                            |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.44 ms: 1.13x faster                                            |
| xml_etree_generate         | 87.0 ms                                                | 77.0 ms: 1.13x faster                                            |
| mako                       | 11.1 ms                                                | 9.86 ms: 1.13x faster                                            |
| telco                      | 8.45 ms                                                | 7.51 ms: 1.13x faster                                            |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.12x faster                                             |
| scimark_monte_carlo        | 66.3 ms                                                | 60.0 ms: 1.11x faster                                            |
| float                      | 78.5 ms                                                | 71.3 ms: 1.10x faster                                            |
| async_tree_none            | 354 ms                                                 | 324 ms: 1.09x faster                                             |
| xml_etree_process          | 60.4 ms                                                | 55.4 ms: 1.09x faster                                            |
| crypto_pyaes               | 73.0 ms                                                | 67.0 ms: 1.09x faster                                            |
| pathlib                    | 17.1 ms                                                | 15.7 ms: 1.09x faster                                            |
| mdp                        | 2.74 sec                                               | 2.52 sec: 1.09x faster                                           |
| async_tree_memoization     | 442 ms                                                 | 415 ms: 1.07x faster                                             |
| xml_etree_parse            | 156 ms                                                 | 147 ms: 1.06x faster                                             |
| regex_effbot               | 3.88 ms                                                | 3.67 ms: 1.06x faster                                            |
| bpe_tokeniser              | 4.69 sec                                               | 4.43 sec: 1.06x faster                                           |
| unpickle_pure_python       | 213 us                                                 | 202 us: 1.05x faster                                             |
| nbody                      | 85.7 ms                                                | 81.5 ms: 1.05x faster                                            |
| xml_etree_iterparse        | 102 ms                                                 | 97.4 ms: 1.05x faster                                            |
| pyflate                    | 460 ms                                                 | 440 ms: 1.04x faster                                             |
| sqlite_synth               | 2.85 us                                                | 2.74 us: 1.04x faster                                            |
| go                         | 142 ms                                                 | 136 ms: 1.04x faster                                             |
| json_dumps                 | 10.4 ms                                                | 10.1 ms: 1.03x faster                                            |
| gc_traversal               | 3.81 ms                                                | 3.69 ms: 1.03x faster                                            |
| json                       | 5.20 ms                                                | 5.05 ms: 1.03x faster                                            |
| scimark_lu                 | 115 ms                                                 | 112 ms: 1.03x faster                                             |
| regex_v8                   | 25.3 ms                                                | 24.7 ms: 1.02x faster                                            |
| unpickle                   | 14.9 us                                                | 14.6 us: 1.02x faster                                            |
| tomli_loads                | 2.11 sec                                               | 2.08 sec: 1.02x faster                                           |
| thrift                     | 796 us                                                 | 784 us: 1.02x faster                                             |
| regex_dna                  | 220 ms                                                 | 217 ms: 1.01x faster                                             |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.01x faster                                             |
| scimark_sor                | 122 ms                                                 | 122 ms: 1.01x faster                                             |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.00x faster                                            |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.00x slower                                             |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                           |
| pickle                     | 11.6 us                                                | 11.6 us: 1.01x slower                                            |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                             |
| python_startup_no_site     | 6.99 ms                                                | 7.07 ms: 1.01x slower                                            |
| pickle_list                | 5.01 us                                                | 5.07 us: 1.01x slower                                            |
| comprehensions             | 16.4 us                                                | 16.8 us: 1.02x slower                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 557 ms: 1.02x slower                                             |
| asyncio_tcp                | 488 ms                                                 | 502 ms: 1.03x slower                                             |
| coverage                   | 83.7 ms                                                | 86.5 ms: 1.03x slower                                            |
| pprint_pformat             | 1.51 sec                                               | 1.56 sec: 1.03x slower                                           |
| chaos                      | 58.4 ms                                                | 60.4 ms: 1.03x slower                                            |
| unpickle_list              | 4.96 us                                                | 5.14 us: 1.04x slower                                            |
| coroutines                 | 22.5 ms                                                | 23.4 ms: 1.04x slower                                            |
| logging_format             | 6.25 us                                                | 6.52 us: 1.04x slower                                            |
| deltablue                  | 3.15 ms                                                | 3.29 ms: 1.04x slower                                            |
| pickle_dict                | 33.2 us                                                | 34.8 us: 1.05x slower                                            |
| typing_runtime_protocols   | 159 us                                                 | 167 us: 1.05x slower                                             |
| json_loads                 | 27.0 us                                                | 28.3 us: 1.05x slower                                            |
| async_generators           | 433 ms                                                 | 454 ms: 1.05x slower                                             |
| nqueens                    | 80.6 ms                                                | 85.1 ms: 1.06x slower                                            |
| async_tree_io              | 843 ms                                                 | 890 ms: 1.06x slower                                             |
| logging_simple             | 5.66 us                                                | 5.99 us: 1.06x slower                                            |
| pickle_pure_python         | 300 us                                                 | 318 us: 1.06x slower                                             |
| async_tree_io_tg           | 825 ms                                                 | 877 ms: 1.06x slower                                             |
| genshi_text                | 22.9 ms                                                | 24.3 ms: 1.06x slower                                            |
| create_gc_cycles           | 1.61 ms                                                | 1.72 ms: 1.07x slower                                            |
| raytrace                   | 262 ms                                                 | 282 ms: 1.08x slower                                             |
| pycparser                  | 1.19 sec                                               | 1.30 sec: 1.09x slower                                           |
| logging_silent             | 102 ns                                                 | 111 ns: 1.09x slower                                             |
| 2to3                       | 265 ms                                                 | 291 ms: 1.10x slower                                             |
| html5lib                   | 64.5 ms                                                | 71.3 ms: 1.10x slower                                            |
| bench_thread_pool          | 815 us                                                 | 902 us: 1.11x slower                                             |
| tornado_http               | 91.5 ms                                                | 102 ms: 1.12x slower                                             |
| hexiom                     | 6.13 ms                                                | 6.97 ms: 1.14x slower                                            |
| sympy_expand               | 462 ms                                                 | 537 ms: 1.16x slower                                             |
| sqlglot_transpile          | 1.57 ms                                                | 1.83 ms: 1.16x slower                                            |
| dulwich_log                | 63.0 ms                                                | 73.6 ms: 1.17x slower                                            |
| sqlglot_normalize          | 107 ms                                                 | 126 ms: 1.17x slower                                             |
| regex_compile              | 131 ms                                                 | 155 ms: 1.18x slower                                             |
| sympy_str                  | 274 ms                                                 | 323 ms: 1.18x slower                                             |
| sqlglot_optimize           | 53.9 ms                                                | 63.8 ms: 1.18x slower                                            |
| docutils                   | 2.58 sec                                               | 3.07 sec: 1.19x slower                                           |
| django_template            | 34.4 ms                                                | 41.1 ms: 1.19x slower                                            |
| sqlglot_parse              | 1.27 ms                                                | 1.54 ms: 1.21x slower                                            |
| generators                 | 28.8 ms                                                | 35.3 ms: 1.22x slower                                            |
| sympy_sum                  | 150 ms                                                 | 191 ms: 1.28x slower                                             |
| pylint                     | 313 ms                                                 | 400 ms: 1.28x slower                                             |
| sympy_integrate            | 19.9 ms                                                | 26.1 ms: 1.31x slower                                            |
| genshi_xml                 | 50.3 ms                                                | 70.3 ms: 1.40x slower                                            |
| unpack_sequence            | 42.4 ns                                                | 106 ns: 2.50x slower                                             |
| bench_mp_pool              | 24.0 ms                                                | 60.9 ms: 2.54x slower                                            |
| Geometric mean             | (ref)                                                  | 1.03x slower                                                     |

Benchmark hidden because not significant (4): async_tree_none_tg, async_tree_cpu_io_mixed, pprint_safe_repr, fannkuch
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 62.93% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.07x