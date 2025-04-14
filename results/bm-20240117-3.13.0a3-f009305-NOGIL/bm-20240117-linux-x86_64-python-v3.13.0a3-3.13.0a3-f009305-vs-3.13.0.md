# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a3
- machine: linux-x86_64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.162x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 290 ms: 1.09x slower                                       |
| chameleon      | 6.94 ms                                                | 7.87 ms: 1.14x slower                                      |
| docutils       | 2.59 sec                                               | 2.95 sec: 1.14x slower                                     |
| html5lib       | 64.2 ms                                                | 70.5 ms: 1.10x slower                                      |
| tornado_http   | 92.4 ms                                                | 102 ms: 1.10x slower                                       |
| Geometric mean | (ref)                                                  | 1.11x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| asyncio_websockets         | 552 ms                                                 | 560 ms: 1.01x slower                                       |
| coroutines                 | 22.7 ms                                                | 23.6 ms: 1.04x slower                                      |
| async_generators           | 436 ms                                                 | 476 ms: 1.09x slower                                       |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 838 ms: 1.45x slower                                       |
| async_tree_memoization_tg  | 464 ms                                                 | 702 ms: 1.51x slower                                       |
| async_tree_none            | 351 ms                                                 | 533 ms: 1.52x slower                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 848 ms: 1.55x slower                                       |
| async_tree_memoization     | 442 ms                                                 | 704 ms: 1.59x slower                                       |
| async_tree_none_tg         | 321 ms                                                 | 537 ms: 1.68x slower                                       |
| async_tree_io_tg           | 857 ms                                                 | 1.50 sec: 1.75x slower                                     |
| async_tree_io              | 842 ms                                                 | 1.49 sec: 1.77x slower                                     |
| Geometric mean             | (ref)                                                  | 1.43x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                       |
| float          | 79.2 ms                                                | 88.3 ms: 1.11x slower                                      |
| nbody          | 87.0 ms                                                | 105 ms: 1.21x slower                                       |
| Geometric mean | (ref)                                                  | 1.10x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 23.7 ms: 1.10x faster                                      |
| regex_effbot   | 3.73 ms                                                | 3.52 ms: 1.06x faster                                      |
| regex_compile  | 132 ms                                                 | 139 ms: 1.05x slower                                       |
| Geometric mean | (ref)                                                  | 1.03x faster                                               |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 310 us                                                 | 318 us: 1.03x slower                                       |
| json_dumps           | 10.6 ms                                                | 11.0 ms: 1.04x slower                                      |
| tomli_loads          | 2.14 sec                                               | 2.24 sec: 1.05x slower                                     |
| json_loads           | 27.2 us                                                | 29.3 us: 1.08x slower                                      |
| xml_etree_process    | 60.6 ms                                                | 65.4 ms: 1.08x slower                                      |
| unpickle_pure_python | 216 us                                                 | 234 us: 1.08x slower                                       |
| xml_etree_generate   | 86.7 ms                                                | 94.2 ms: 1.09x slower                                      |
| xml_etree_parse      | 156 ms                                                 | 172 ms: 1.11x slower                                       |
| xml_etree_iterparse  | 101 ms                                                 | 114 ms: 1.12x slower                                       |
| Geometric mean       | (ref)                                                  | 1.07x slower                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 12.1 ms: 1.03x faster                                      |
| python_startup_no_site | 6.96 ms                                                | 10.5 ms: 1.51x slower                                      |
| Geometric mean         | (ref)                                                  | 1.21x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| genshi_text     | 23.5 ms                                                | 24.6 ms: 1.05x slower                                      |
| django_template | 35.2 ms                                                | 37.3 ms: 1.06x slower                                      |
| genshi_xml      | 50.9 ms                                                | 55.0 ms: 1.08x slower                                      |
| mako            | 11.1 ms                                                | 12.0 ms: 1.08x slower                                      |
| Geometric mean  | (ref)                                                  | 1.07x slower                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| create_gc_cycles           | 2.41 ms                                                | 1.26 ms: 1.92x faster                                      |
| typing_runtime_protocols   | 165 us                                                 | 124 us: 1.33x faster                                       |
| gc_traversal               | 4.37 ms                                                | 3.52 ms: 1.24x faster                                      |
| regex_v8                   | 26.2 ms                                                | 23.7 ms: 1.10x faster                                      |
| regex_effbot               | 3.73 ms                                                | 3.52 ms: 1.06x faster                                      |
| python_startup             | 12.5 ms                                                | 12.1 ms: 1.03x faster                                      |
| bench_mp_pool              | 24.0 ms                                                | 23.5 ms: 1.02x faster                                      |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.02x faster                                       |
| crypto_pyaes               | 75.3 ms                                                | 74.5 ms: 1.01x faster                                      |
| pyflate                    | 471 ms                                                 | 469 ms: 1.00x faster                                       |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                       |
| asyncio_websockets         | 552 ms                                                 | 560 ms: 1.01x slower                                       |
| richards                   | 48.7 ms                                                | 49.6 ms: 1.02x slower                                      |
| richards_super             | 54.9 ms                                                | 56.0 ms: 1.02x slower                                      |
| deepcopy_reduce            | 3.20 us                                                | 3.27 us: 1.02x slower                                      |
| pickle_pure_python         | 310 us                                                 | 318 us: 1.03x slower                                       |
| deepcopy                   | 358 us                                                 | 368 us: 1.03x slower                                       |
| go                         | 144 ms                                                 | 149 ms: 1.04x slower                                       |
| coroutines                 | 22.7 ms                                                | 23.6 ms: 1.04x slower                                      |
| json_dumps                 | 10.6 ms                                                | 11.0 ms: 1.04x slower                                      |
| genshi_text                | 23.5 ms                                                | 24.6 ms: 1.05x slower                                      |
| tomli_loads                | 2.14 sec                                               | 2.24 sec: 1.05x slower                                     |
| regex_compile              | 132 ms                                                 | 139 ms: 1.05x slower                                       |
| sqlglot_normalize          | 108 ms                                                 | 113 ms: 1.05x slower                                       |
| django_template            | 35.2 ms                                                | 37.3 ms: 1.06x slower                                      |
| meteor_contest             | 109 ms                                                 | 115 ms: 1.06x slower                                       |
| dulwich_log                | 64.3 ms                                                | 68.4 ms: 1.06x slower                                      |
| sqlglot_optimize           | 53.7 ms                                                | 57.3 ms: 1.07x slower                                      |
| telco                      | 8.54 ms                                                | 9.10 ms: 1.07x slower                                      |
| scimark_lu                 | 113 ms                                                 | 120 ms: 1.07x slower                                       |
| pycparser                  | 1.20 sec                                               | 1.29 sec: 1.07x slower                                     |
| sqlglot_parse              | 1.27 ms                                                | 1.36 ms: 1.07x slower                                      |
| comprehensions             | 16.5 us                                                | 17.7 us: 1.07x slower                                      |
| pylint                     | 313 ms                                                 | 335 ms: 1.07x slower                                       |
| scimark_fft                | 364 ms                                                 | 391 ms: 1.07x slower                                       |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 5.42 ms: 1.07x slower                                      |
| mdp                        | 2.72 sec                                               | 2.93 sec: 1.08x slower                                     |
| sqlglot_transpile          | 1.58 ms                                                | 1.71 ms: 1.08x slower                                      |
| hexiom                     | 6.16 ms                                                | 6.64 ms: 1.08x slower                                      |
| json_loads                 | 27.2 us                                                | 29.3 us: 1.08x slower                                      |
| xml_etree_process          | 60.6 ms                                                | 65.4 ms: 1.08x slower                                      |
| genshi_xml                 | 50.9 ms                                                | 55.0 ms: 1.08x slower                                      |
| pathlib                    | 17.5 ms                                                | 18.9 ms: 1.08x slower                                      |
| deepcopy_memo              | 39.1 us                                                | 42.4 us: 1.08x slower                                      |
| scimark_sor                | 124 ms                                                 | 134 ms: 1.08x slower                                       |
| mako                       | 11.1 ms                                                | 12.0 ms: 1.08x slower                                      |
| unpickle_pure_python       | 216 us                                                 | 234 us: 1.08x slower                                       |
| xml_etree_generate         | 86.7 ms                                                | 94.2 ms: 1.09x slower                                      |
| nqueens                    | 78.4 ms                                                | 85.2 ms: 1.09x slower                                      |
| 2to3                       | 267 ms                                                 | 290 ms: 1.09x slower                                       |
| logging_format             | 6.40 us                                                | 6.96 us: 1.09x slower                                      |
| raytrace                   | 267 ms                                                 | 291 ms: 1.09x slower                                       |
| async_generators           | 436 ms                                                 | 476 ms: 1.09x slower                                       |
| pprint_safe_repr           | 728 ms                                                 | 796 ms: 1.09x slower                                       |
| logging_silent             | 102 ns                                                 | 111 ns: 1.09x slower                                       |
| logging_simple             | 5.72 us                                                | 6.26 us: 1.09x slower                                      |
| pprint_pformat             | 1.49 sec                                               | 1.64 sec: 1.10x slower                                     |
| scimark_monte_carlo        | 67.4 ms                                                | 74.0 ms: 1.10x slower                                      |
| html5lib                   | 64.2 ms                                                | 70.5 ms: 1.10x slower                                      |
| deltablue                  | 3.23 ms                                                | 3.56 ms: 1.10x slower                                      |
| tornado_http               | 92.4 ms                                                | 102 ms: 1.10x slower                                       |
| xml_etree_parse            | 156 ms                                                 | 172 ms: 1.11x slower                                       |
| generators                 | 29.0 ms                                                | 32.3 ms: 1.11x slower                                      |
| float                      | 79.2 ms                                                | 88.3 ms: 1.11x slower                                      |
| xml_etree_iterparse        | 101 ms                                                 | 114 ms: 1.12x slower                                       |
| chaos                      | 58.1 ms                                                | 65.2 ms: 1.12x slower                                      |
| chameleon                  | 6.94 ms                                                | 7.87 ms: 1.14x slower                                      |
| docutils                   | 2.59 sec                                               | 2.95 sec: 1.14x slower                                     |
| sympy_integrate            | 19.9 ms                                                | 23.0 ms: 1.16x slower                                      |
| nbody                      | 87.0 ms                                                | 105 ms: 1.21x slower                                       |
| sympy_str                  | 275 ms                                                 | 342 ms: 1.25x slower                                       |
| sympy_expand               | 463 ms                                                 | 644 ms: 1.39x slower                                       |
| sympy_sum                  | 150 ms                                                 | 216 ms: 1.43x slower                                       |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 838 ms: 1.45x slower                                       |
| python_startup_no_site     | 6.96 ms                                                | 10.5 ms: 1.51x slower                                      |
| async_tree_memoization_tg  | 464 ms                                                 | 702 ms: 1.51x slower                                       |
| async_tree_none            | 351 ms                                                 | 533 ms: 1.52x slower                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 848 ms: 1.55x slower                                       |
| async_tree_memoization     | 442 ms                                                 | 704 ms: 1.59x slower                                       |
| async_tree_none_tg         | 321 ms                                                 | 537 ms: 1.68x slower                                       |
| async_tree_io_tg           | 857 ms                                                 | 1.50 sec: 1.75x slower                                     |
| async_tree_io              | 842 ms                                                 | 1.49 sec: 1.77x slower                                     |
| bench_thread_pool          | 822 us                                                 | 2.54 ms: 3.09x slower                                      |
| coverage                   | 84.0 ms                                                | 690 ms: 8.21x slower                                       |
| thrift                     | 809 us                                                 | 9.30 ms: 11.49x slower                                     |
| fannkuch                   | 404 ms                                                 | 4.97 sec: 12.29x slower                                    |
| Geometric mean             | (ref)                                                  | 1.20x slower                                               |

Benchmark hidden because not significant (3): json, regex_dna, mypy2
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (11) of results/bm-20240117-3.13.0a3-f009305-NOGIL/bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.162x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: 0.99x