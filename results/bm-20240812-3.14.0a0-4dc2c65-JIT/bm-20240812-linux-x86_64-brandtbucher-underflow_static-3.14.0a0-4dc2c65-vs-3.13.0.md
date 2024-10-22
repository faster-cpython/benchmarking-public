# Results vs. 3.13.0

- fork: brandtbucher
- ref: underflow_static
- machine: linux-x86_64
- commit hash: 4dc2c65
- commit date: 2024-08-12
- overall geometric mean: 1.00x slower
- HPT reliability: 72.85%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 282 ms: 1.06x slower                                                    |
| docutils       | 2.58 sec                                               | 3.30 sec: 1.28x slower                                                  |
| html5lib       | 64.5 ms                                                | 69.6 ms: 1.08x slower                                                   |
| tornado_http   | 91.5 ms                                                | 95.3 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                  | 1.11x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 393 ms: 1.18x faster                                                    |
| async_tree_none            | 354 ms                                                 | 327 ms: 1.08x faster                                                    |
| async_tree_none_tg         | 320 ms                                                 | 302 ms: 1.06x faster                                                    |
| async_tree_memoization     | 442 ms                                                 | 421 ms: 1.05x faster                                                    |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 530 ms: 1.02x faster                                                    |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 565 ms: 1.02x faster                                                    |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                  |
| async_tree_io_tg           | 825 ms                                                 | 866 ms: 1.05x slower                                                    |
| async_generators           | 433 ms                                                 | 454 ms: 1.05x slower                                                    |
| asyncio_tcp                | 488 ms                                                 | 515 ms: 1.05x slower                                                    |
| async_tree_io              | 843 ms                                                 | 903 ms: 1.07x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                            |

Benchmark hidden because not significant (1): coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.5 ms: 1.11x faster                                                   |
| nbody          | 85.7 ms                                                | 80.3 ms: 1.07x faster                                                   |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                  | 1.06x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.75 ms: 1.04x faster                                                   |
| regex_dna      | 220 ms                                                 | 218 ms: 1.01x faster                                                    |
| regex_v8       | 25.3 ms                                                | 26.0 ms: 1.03x slower                                                   |
| regex_compile  | 131 ms                                                 | 146 ms: 1.11x slower                                                    |
| Geometric mean | (ref)                                                  | 1.02x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 80.5 ms: 1.08x faster                                                   |
| tomli_loads          | 2.11 sec                                               | 1.97 sec: 1.07x faster                                                  |
| xml_etree_process    | 60.4 ms                                                | 56.6 ms: 1.07x faster                                                   |
| unpickle_pure_python | 213 us                                                 | 203 us: 1.05x faster                                                    |
| xml_etree_parse      | 156 ms                                                 | 148 ms: 1.05x faster                                                    |
| xml_etree_iterparse  | 102 ms                                                 | 99.1 ms: 1.03x faster                                                   |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                   |
| pickle_pure_python   | 300 us                                                 | 303 us: 1.01x slower                                                    |
| json_loads           | 27.0 us                                                | 27.8 us: 1.03x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.00x slower                                                   |
| python_startup_no_site | 6.99 ms                                                | 7.18 ms: 1.03x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.91 ms: 1.12x faster                                                   |
| django_template | 34.4 ms                                                | 35.8 ms: 1.04x slower                                                   |
| genshi_text     | 22.9 ms                                                | 24.9 ms: 1.09x slower                                                   |
| genshi_xml      | 50.3 ms                                                | 56.8 ms: 1.13x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 26.0 us: 1.46x faster                                                   |
| richards                   | 48.1 ms                                                | 35.2 ms: 1.37x faster                                                   |
| richards_super             | 54.4 ms                                                | 40.2 ms: 1.35x faster                                                   |
| deepcopy                   | 352 us                                                 | 268 us: 1.31x faster                                                    |
| scimark_fft                | 369 ms                                                 | 310 ms: 1.19x faster                                                    |
| async_tree_memoization_tg  | 465 ms                                                 | 393 ms: 1.18x faster                                                    |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.30 ms: 1.17x faster                                                   |
| deepcopy_reduce            | 3.17 us                                                | 2.75 us: 1.15x faster                                                   |
| spectral_norm              | 115 ms                                                 | 100 ms: 1.15x faster                                                    |
| mako                       | 11.1 ms                                                | 9.91 ms: 1.12x faster                                                   |
| crypto_pyaes               | 73.0 ms                                                | 65.5 ms: 1.11x faster                                                   |
| float                      | 78.5 ms                                                | 70.5 ms: 1.11x faster                                                   |
| telco                      | 8.45 ms                                                | 7.62 ms: 1.11x faster                                                   |
| async_tree_none            | 354 ms                                                 | 327 ms: 1.08x faster                                                    |
| xml_etree_generate         | 87.0 ms                                                | 80.5 ms: 1.08x faster                                                   |
| tomli_loads                | 2.11 sec                                               | 1.97 sec: 1.07x faster                                                  |
| scimark_sor                | 122 ms                                                 | 114 ms: 1.07x faster                                                    |
| nbody                      | 85.7 ms                                                | 80.3 ms: 1.07x faster                                                   |
| xml_etree_process          | 60.4 ms                                                | 56.6 ms: 1.07x faster                                                   |
| pathlib                    | 17.1 ms                                                | 16.1 ms: 1.06x faster                                                   |
| async_tree_none_tg         | 320 ms                                                 | 302 ms: 1.06x faster                                                    |
| unpickle_pure_python       | 213 us                                                 | 203 us: 1.05x faster                                                    |
| async_tree_memoization     | 442 ms                                                 | 421 ms: 1.05x faster                                                    |
| xml_etree_parse            | 156 ms                                                 | 148 ms: 1.05x faster                                                    |
| fannkuch                   | 381 ms                                                 | 365 ms: 1.04x faster                                                    |
| bpe_tokeniser              | 4.69 sec                                               | 4.53 sec: 1.04x faster                                                  |
| regex_effbot               | 3.88 ms                                                | 3.75 ms: 1.04x faster                                                   |
| scimark_lu                 | 115 ms                                                 | 111 ms: 1.03x faster                                                    |
| json                       | 5.20 ms                                                | 5.04 ms: 1.03x faster                                                   |
| xml_etree_iterparse        | 102 ms                                                 | 99.1 ms: 1.03x faster                                                   |
| logging_silent             | 102 ns                                                 | 99.3 ns: 1.03x faster                                                   |
| logging_simple             | 5.66 us                                                | 5.52 us: 1.03x faster                                                   |
| scimark_monte_carlo        | 66.3 ms                                                | 64.6 ms: 1.03x faster                                                   |
| mdp                        | 2.74 sec                                               | 2.67 sec: 1.03x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 530 ms: 1.02x faster                                                    |
| logging_format             | 6.25 us                                                | 6.11 us: 1.02x faster                                                   |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 565 ms: 1.02x faster                                                    |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                    |
| pyflate                    | 460 ms                                                 | 453 ms: 1.01x faster                                                    |
| thrift                     | 796 us                                                 | 787 us: 1.01x faster                                                    |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                   |
| regex_dna                  | 220 ms                                                 | 218 ms: 1.01x faster                                                    |
| gc_traversal               | 3.81 ms                                                | 3.78 ms: 1.01x faster                                                   |
| python_startup             | 10.6 ms                                                | 10.6 ms: 1.00x slower                                                   |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.01x slower                                                    |
| bench_thread_pool          | 815 us                                                 | 820 us: 1.01x slower                                                    |
| pickle_pure_python         | 300 us                                                 | 303 us: 1.01x slower                                                    |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                  |
| pprint_safe_repr           | 744 ms                                                 | 759 ms: 1.02x slower                                                    |
| pycparser                  | 1.19 sec                                               | 1.22 sec: 1.02x slower                                                  |
| regex_v8                   | 25.3 ms                                                | 26.0 ms: 1.03x slower                                                   |
| python_startup_no_site     | 6.99 ms                                                | 7.18 ms: 1.03x slower                                                   |
| json_loads                 | 27.0 us                                                | 27.8 us: 1.03x slower                                                   |
| pprint_pformat             | 1.51 sec                                               | 1.56 sec: 1.03x slower                                                  |
| raytrace                   | 262 ms                                                 | 271 ms: 1.04x slower                                                    |
| nqueens                    | 80.6 ms                                                | 83.6 ms: 1.04x slower                                                   |
| django_template            | 34.4 ms                                                | 35.8 ms: 1.04x slower                                                   |
| tornado_http               | 91.5 ms                                                | 95.3 ms: 1.04x slower                                                   |
| async_tree_io_tg           | 825 ms                                                 | 866 ms: 1.05x slower                                                    |
| async_generators           | 433 ms                                                 | 454 ms: 1.05x slower                                                    |
| go                         | 142 ms                                                 | 149 ms: 1.05x slower                                                    |
| asyncio_tcp                | 488 ms                                                 | 515 ms: 1.05x slower                                                    |
| typing_runtime_protocols   | 159 us                                                 | 169 us: 1.06x slower                                                    |
| 2to3                       | 265 ms                                                 | 282 ms: 1.06x slower                                                    |
| async_tree_io              | 843 ms                                                 | 903 ms: 1.07x slower                                                    |
| html5lib                   | 64.5 ms                                                | 69.6 ms: 1.08x slower                                                   |
| genshi_text                | 22.9 ms                                                | 24.9 ms: 1.09x slower                                                   |
| coverage                   | 83.7 ms                                                | 92.4 ms: 1.10x slower                                                   |
| create_gc_cycles           | 1.61 ms                                                | 1.78 ms: 1.11x slower                                                   |
| regex_compile              | 131 ms                                                 | 146 ms: 1.11x slower                                                    |
| chaos                      | 58.4 ms                                                | 65.3 ms: 1.12x slower                                                   |
| sqlglot_normalize          | 107 ms                                                 | 120 ms: 1.12x slower                                                    |
| sqlglot_optimize           | 53.9 ms                                                | 60.3 ms: 1.12x slower                                                   |
| hexiom                     | 6.13 ms                                                | 6.88 ms: 1.12x slower                                                   |
| sympy_expand               | 462 ms                                                 | 519 ms: 1.12x slower                                                    |
| genshi_xml                 | 50.3 ms                                                | 56.8 ms: 1.13x slower                                                   |
| sqlglot_parse              | 1.27 ms                                                | 1.46 ms: 1.15x slower                                                   |
| sqlglot_transpile          | 1.57 ms                                                | 1.84 ms: 1.17x slower                                                   |
| sympy_str                  | 274 ms                                                 | 323 ms: 1.18x slower                                                    |
| sympy_integrate            | 19.9 ms                                                | 24.4 ms: 1.23x slower                                                   |
| docutils                   | 2.58 sec                                               | 3.30 sec: 1.28x slower                                                  |
| sympy_sum                  | 150 ms                                                 | 191 ms: 1.28x slower                                                    |
| pylint                     | 313 ms                                                 | 404 ms: 1.29x slower                                                    |
| generators                 | 28.8 ms                                                | 41.3 ms: 1.43x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.00x slower                                                            |

Benchmark hidden because not significant (4): bench_mp_pool, deltablue, comprehensions, coroutines
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 72.85% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.10x